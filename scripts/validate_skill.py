#!/usr/bin/env python3
"""Validate UI Compose against a portable Agent Skills contract and OpenAI UI metadata.

This repository-owned checker intentionally follows the strict common subset we
ship to current coding-agent packagers. Compatibility guidance belongs in the
Markdown body rather than an extra top-level frontmatter key so stricter
packagers do not reject the skill.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_FRONTMATTER = {
    "name",
    "description",
    "license",
    "metadata",
    "allowed-tools",
}


def split_frontmatter(text: str) -> tuple[dict, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration as exc:
        raise ValueError("SKILL.md frontmatter is not closed with ---") from exc
    metadata = yaml.safe_load("\n".join(lines[1:end])) or {}
    if not isinstance(metadata, dict):
        raise ValueError("SKILL.md frontmatter must be a YAML mapping")
    return metadata, "\n".join(lines[end + 1 :])


def validate_skill(root: Path, expected_install_name: str | None) -> list[str]:
    errors: list[str] = []
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return [f"missing {skill_path}"]

    text = skill_path.read_text(encoding="utf-8")
    try:
        metadata, body = split_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    unknown = set(metadata) - ALLOWED_FRONTMATTER
    if unknown:
        errors.append(f"unsupported SKILL.md frontmatter fields: {sorted(unknown)}")

    name = metadata.get("name")
    description = metadata.get("description")

    if not isinstance(name, str) or not name:
        errors.append("frontmatter `name` is required")
    else:
        if len(name) > 64:
            errors.append("frontmatter `name` must be <= 64 characters")
        if not NAME_RE.fullmatch(name):
            errors.append("frontmatter `name` must use lowercase letters, numbers, and single hyphens")
        if expected_install_name and name != expected_install_name:
            errors.append(
                f"frontmatter name {name!r} does not match expected install directory {expected_install_name!r}"
            )

    if not isinstance(description, str) or not description.strip():
        errors.append("frontmatter `description` is required and must be non-empty")
    elif len(description) > 1024:
        errors.append("frontmatter `description` must be <= 1024 characters")

    if not body.strip():
        errors.append("SKILL.md must contain Markdown instructions after frontmatter")

    if len(text.splitlines()) > 500:
        errors.append("SKILL.md exceeds the recommended 500-line progressive-disclosure budget")

    openai_path = root / "agents" / "openai.yaml"
    if openai_path.exists():
        openai = yaml.safe_load(openai_path.read_text(encoding="utf-8")) or {}
        if not isinstance(openai, dict):
            errors.append("agents/openai.yaml must be a YAML mapping")
        else:
            interface = openai.get("interface")
            if not isinstance(interface, dict):
                errors.append("agents/openai.yaml must contain an `interface` mapping")
            else:
                display_name = interface.get("display_name")
                short_description = interface.get("short_description")
                default_prompt = interface.get("default_prompt")
                if not isinstance(display_name, str) or not display_name.strip():
                    errors.append("OpenAI interface.display_name is required")
                if not isinstance(short_description, str) or not (25 <= len(short_description) <= 64):
                    errors.append("OpenAI interface.short_description must be 25-64 characters")
                if not isinstance(default_prompt, str) or not default_prompt.strip():
                    errors.append("OpenAI interface.default_prompt is required")
                elif name and f"${name}" not in default_prompt:
                    errors.append(f"OpenAI default_prompt should invoke the skill as ${name}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir", nargs="?", default=".")
    parser.add_argument("--expected-install-name", default=None)
    args = parser.parse_args()

    root = Path(args.skill_dir).resolve()
    errors = validate_skill(root, args.expected_install_name)
    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

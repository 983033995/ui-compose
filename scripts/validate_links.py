#!/usr/bin/env python3
"""Validate repository-local references in Markdown and the Skill entrypoint."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")
SKILL_PATH_RE = re.compile(
    r"`((?:agents|evals|references|schemas|scripts)/[^`\s]+)`"
)
IGNORED_PARTS = {".git", ".codegraph", "dist", "node_modules"}


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if path.is_file() and not IGNORED_PARTS.intersection(path.relative_to(root).parts)
    )


def unfenced_text(text: str) -> str:
    lines: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        stripped = line.lstrip()
        marker = stripped[:3]
        if marker in {"```", "~~~"}:
            fence = None if fence == marker else marker if fence is None else fence
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def markdown_target(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        return value[1 : value.index(">")]
    return value.split(maxsplit=1)[0]


def local_path(root: Path, source: Path, target: str) -> tuple[Path | None, str | None]:
    if not target or target.startswith(("#", "//")):
        return None, None
    parsed = urlsplit(target)
    if parsed.scheme:
        return None, None
    path_text = unquote(parsed.path)
    if not path_text:
        return None, None
    candidate = (root / path_text.lstrip("/")) if path_text.startswith("/") else (source.parent / path_text)
    resolved = candidate.resolve()
    try:
        resolved.relative_to(root)
    except ValueError:
        return None, f"reference escapes repository root: {target}"
    return resolved, None


def validate(root: Path) -> tuple[list[str], int, int]:
    errors: list[str] = []
    files = markdown_files(root)
    checked = 0

    for source in files:
        rel = source.relative_to(root)
        text = unfenced_text(source.read_text(encoding="utf-8"))
        targets = [markdown_target(match.group(1)) for match in MARKDOWN_LINK_RE.finditer(text)]
        if rel == Path("SKILL.md"):
            targets.extend(match.group(1) for match in SKILL_PATH_RE.finditer(text))

        for target in targets:
            resolved, error = local_path(root, source, target)
            if error:
                errors.append(f"[{rel}] {error}")
                continue
            if resolved is None:
                continue
            checked += 1
            if not resolved.exists():
                errors.append(f"[{rel}] missing local reference: {target}")

    return errors, len(files), checked


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors, file_count, checked = validate(root)
    if errors:
        print("Link validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"Link validation passed: {file_count} Markdown file(s), {checked} local reference(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

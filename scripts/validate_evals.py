#!/usr/bin/env python3
"""Validate UI Compose eval result records.

Result files are optional during early development. When JSON results exist under
`evals/results/`, each record must match the schema, refer to a real eval case,
use real Pattern/Skeleton IDs when provided, and contain an internally consistent
rubric total.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "evals" / "results"
SCHEMA_PATH = ROOT / "schemas" / "eval-result.schema.json"
PATTERN_REGISTRY = ROOT / "references" / "patterns" / "registry.yaml"
SKELETON_REGISTRY = ROOT / "references" / "skeletons" / "registry.yaml"
CASES_DIR = ROOT / "evals" / "cases"

CASE_FILE_RE = re.compile(r"^(\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*)\.md$")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def real_case_ids() -> set[str]:
    ids = set()
    for path in CASES_DIR.glob("*.md"):
        match = CASE_FILE_RE.match(path.name)
        if match:
            ids.add(match.group(1))
    return ids


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    patterns = load_yaml(PATTERN_REGISTRY)["patterns"]
    skeletons = load_yaml(SKELETON_REGISTRY)["skeletons"]
    pattern_ids = {item["id"] for item in patterns}
    skeleton_ids = {item["id"] for item in skeletons}
    case_ids = real_case_ids()

    result_files = sorted(
        path for path in RESULTS_DIR.rglob("*.json") if path.is_file()
    ) if RESULTS_DIR.exists() else []

    errors: list[str] = []

    for path in result_files:
        rel = path.relative_to(ROOT)
        try:
            result = load_json(path)
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"[{rel}] invalid JSON: {exc}")
            continue

        for error in sorted(validator.iter_errors(result), key=lambda e: list(e.path)):
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            errors.append(f"[{rel}] {location}: {error.message}")

        case_id = result.get("case_id")
        if case_id and case_id not in case_ids:
            errors.append(f"[{rel}] references missing eval case: {case_id}")

        skeleton_id = result.get("selected_skeleton")
        if skeleton_id and skeleton_id not in skeleton_ids:
            errors.append(f"[{rel}] references missing skeleton: {skeleton_id}")

        for pattern_id in result.get("selected_patterns", []):
            if pattern_id not in pattern_ids:
                errors.append(f"[{rel}] references missing pattern: {pattern_id}")

        rubric = result.get("rubric")
        if isinstance(rubric, dict):
            keys = [
                "visual_quality",
                "design_consistency",
                "task_fit",
                "host_stack_compliance",
                "accessibility",
                "responsive",
                "build_runtime_success",
                "dependency_discipline",
                "anti_slop",
            ]
            if all(isinstance(rubric.get(key), (int, float)) for key in keys):
                calculated = round(sum(rubric[key] for key in keys), 4)
                reported = rubric.get("total")
                if isinstance(reported, (int, float)) and abs(calculated - reported) > 0.0001:
                    errors.append(
                        f"[{rel}] rubric.total={reported} does not equal component sum {calculated}"
                    )

        if result.get("build_status") == "passed":
            artifacts = result.get("artifacts", {})
            if not artifacts.get("desktop") or not artifacts.get("mobile"):
                errors.append(
                    f"[{rel}] passed rendered run requires desktop and mobile artifact references"
                )

    if errors:
        print("Eval validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Eval validation passed: {len(result_files)} observed result record(s).")
    if not result_files:
        print("No benchmark result JSON exists yet; delivery readiness must not count rendered evidence.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

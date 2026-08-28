#!/usr/bin/env python3
"""Validate UI Compose eval fixtures and observed result records.

Fixture contracts describe the host environment for repeatable benchmark cases.
Observed result files are optional during early development. When JSON results
exist under `evals/results/`, each record must match the schema, refer to a real
eval case, use real Pattern/Skeleton IDs when provided, and contain an internally
consistent rubric total.
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
FIXTURES_DIR = ROOT / "evals" / "harness" / "fixtures"
RESULT_SCHEMA_PATH = ROOT / "schemas" / "eval-result.schema.json"
FIXTURE_SCHEMA_PATH = ROOT / "schemas" / "eval-fixture.schema.json"
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


def schema_errors(validator, value, rel: Path) -> list[str]:
    errors = []
    for error in sorted(validator.iter_errors(value), key=lambda e: list(e.path)):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"[{rel}] {location}: {error.message}")
    return errors


def main() -> int:
    result_schema = load_json(RESULT_SCHEMA_PATH)
    fixture_schema = load_json(FIXTURE_SCHEMA_PATH)
    result_validator = Draft202012Validator(result_schema, format_checker=FormatChecker())
    fixture_validator = Draft202012Validator(fixture_schema, format_checker=FormatChecker())

    patterns = load_yaml(PATTERN_REGISTRY)["patterns"]
    skeletons = load_yaml(SKELETON_REGISTRY)["skeletons"]
    pattern_ids = {item["id"] for item in patterns}
    skeleton_ids = {item["id"] for item in skeletons}
    case_ids = real_case_ids()

    result_files = sorted(
        path for path in RESULTS_DIR.rglob("*.json") if path.is_file()
    ) if RESULTS_DIR.exists() else []
    fixture_files = sorted(FIXTURES_DIR.glob("*.yaml")) if FIXTURES_DIR.exists() else []

    errors: list[str] = []
    fixture_ids: set[str] = set()
    fixture_case_coverage: set[str] = set()

    for path in fixture_files:
        rel = path.relative_to(ROOT)
        try:
            fixture = load_yaml(path)
        except (yaml.YAMLError, OSError) as exc:
            errors.append(f"[{rel}] invalid YAML: {exc}")
            continue

        errors.extend(schema_errors(fixture_validator, fixture, rel))
        if not isinstance(fixture, dict):
            continue

        fixture_id = fixture.get("id")
        if fixture_id:
            if fixture_id in fixture_ids:
                errors.append(f"[{rel}] duplicate fixture id: {fixture_id}")
            fixture_ids.add(fixture_id)

        for case_id in fixture.get("case_ids", []):
            if case_id not in case_ids:
                errors.append(f"[{rel}] references missing eval case: {case_id}")
            fixture_case_coverage.add(case_id)

        deps = set(fixture.get("dependencies", []))
        forbidden = set(fixture.get("forbidden_default_dependencies", []))
        overlap = sorted(deps & forbidden)
        if overlap:
            errors.append(
                f"[{rel}] dependencies also listed as forbidden defaults: {overlap}"
            )

    for path in result_files:
        rel = path.relative_to(ROOT)
        try:
            result = load_json(path)
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"[{rel}] invalid JSON: {exc}")
            continue

        errors.extend(schema_errors(result_validator, result, rel))

        case_id = result.get("case_id")
        if case_id and case_id not in case_ids:
            errors.append(f"[{rel}] references missing eval case: {case_id}")

        host_fixture_ref = result.get("host_fixture_ref")
        if host_fixture_ref and host_fixture_ref not in fixture_ids:
            errors.append(f"[{rel}] references missing fixture: {host_fixture_ref}")

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

    print(
        f"Eval validation passed: {len(fixture_files)} fixture contract(s), "
        f"{len(result_files)} observed result record(s)."
    )
    if fixture_files:
        covered = ", ".join(sorted(fixture_case_coverage))
        print(f"Fixture-covered cases: {covered}")
    if not result_files:
        print("No benchmark result JSON exists yet; delivery readiness must not count rendered evidence.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

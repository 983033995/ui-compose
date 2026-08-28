#!/usr/bin/env python3
"""Validate UI Compose registries and their cross-references.

Requires:
  pip install pyyaml jsonschema
"""
from __future__ import annotations

import datetime as _dt
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
STALE_VERIFICATION_DAYS = 90
# CI commonly runs in UTC while source verification may be recorded in a
# maintainer's local timezone. Allow a one-day skew, but reject anything beyond
# that as a genuine future-date error.
MAX_FUTURE_DATE_SKEW_DAYS = 1

REGISTRIES = {
    "sources": ROOT / "references/sources/registry.yaml",
    "patterns": ROOT / "references/patterns/registry.yaml",
    "skeletons": ROOT / "references/skeletons/registry.yaml",
}

SCHEMAS = {
    "sources": ROOT / "schemas/source-registry.schema.json",
    "patterns": ROOT / "schemas/pattern-registry.schema.json",
    "skeletons": ROOT / "schemas/skeleton-registry.schema.json",
}

KNOWN_ADAPTERS = {
    "react-tailwind",
    "vue-element-plus",
    "vue-unocss",
    "generic-css",
}


def normalize(value):
    if isinstance(value, (_dt.date, _dt.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: normalize(v) for k, v in value.items()}
    if isinstance(value, list):
        return [normalize(v) for v in value]
    return value


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return normalize(yaml.safe_load(fh))


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def validate_schema(name: str, data, schema) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        location = ".".join(str(p) for p in error.absolute_path) or "<root>"
        errors.append(f"[{name}] {location}: {error.message}")
    return errors


def duplicate_ids(items) -> set[str]:
    seen = set()
    duplicates = set()
    for item in items:
        item_id = item["id"]
        if item_id in seen:
            duplicates.add(item_id)
        seen.add(item_id)
    return duplicates


def main() -> int:
    data = {name: load_yaml(path) for name, path in REGISTRIES.items()}
    schemas = {name: load_json(path) for name, path in SCHEMAS.items()}

    errors: list[str] = []
    warnings: list[str] = []

    for name in REGISTRIES:
        errors.extend(validate_schema(name, data[name], schemas[name]))

    collections = {
        "sources": data["sources"]["sources"],
        "patterns": data["patterns"]["patterns"],
        "skeletons": data["skeletons"]["skeletons"],
    }

    for name, items in collections.items():
        for duplicate in sorted(duplicate_ids(items)):
            errors.append(f"[{name}] duplicate id: {duplicate}")

    source_ids = {item["id"] for item in collections["sources"]}
    pattern_ids = {item["id"] for item in collections["patterns"]}

    for pattern in collections["patterns"]:
        for evidence in pattern.get("evidence", []):
            if evidence not in source_ids:
                errors.append(
                    f"[patterns] {pattern['id']} references missing source evidence: {evidence}"
                )

        for adapter in pattern.get("adapters", {}):
            if adapter not in KNOWN_ADAPTERS:
                errors.append(
                    f"[patterns] {pattern['id']} uses unknown adapter: {adapter}"
                )

        low_density, high_density = pattern["density"]
        low_motion, high_motion = pattern["motion"]
        if low_density > high_density:
            errors.append(f"[patterns] {pattern['id']} density range is reversed")
        if low_motion > high_motion:
            errors.append(f"[patterns] {pattern['id']} motion range is reversed")

    for skeleton in collections["skeletons"]:
        for pattern_id in skeleton.get("recommended_patterns", []):
            if pattern_id not in pattern_ids:
                errors.append(
                    f"[skeletons] {skeleton['id']} references missing pattern: {pattern_id}"
                )

    today = _dt.datetime.now(_dt.timezone.utc).date()
    for source in collections["sources"]:
        if source.get("license", "").startswith("verify") and not source.get("canonical_url"):
            warnings.append(
                f"[sources] {source['id']} still needs canonical_url before license verification"
            )

        last_verified = source.get("last_verified")
        canonical_url = source.get("canonical_url")
        if last_verified and not canonical_url:
            errors.append(
                f"[sources] {source['id']} has last_verified but no canonical_url"
            )
        elif last_verified:
            try:
                verified_date = _dt.date.fromisoformat(last_verified)
            except ValueError:
                errors.append(
                    f"[sources] {source['id']} has invalid last_verified date: {last_verified}"
                )
            else:
                age_days = (today - verified_date).days
                if age_days < -MAX_FUTURE_DATE_SKEW_DAYS:
                    errors.append(
                        f"[sources] {source['id']} last_verified is too far in the future: {last_verified}"
                    )
                elif age_days < 0:
                    warnings.append(
                        f"[sources] {source['id']} last_verified is one local-timezone day ahead of UTC: {last_verified}"
                    )
                elif age_days > STALE_VERIFICATION_DAYS:
                    warnings.append(
                        f"[sources] {source['id']} verification is {age_days} days old; re-check upstream"
                    )

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(
        "Validation passed: "
        f"{len(collections['sources'])} sources, "
        f"{len(collections['patterns'])} patterns, "
        f"{len(collections['skeletons'])} skeletons."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

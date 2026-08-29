# Eval results

This directory stores **observed benchmark evidence**, not planned expectations.

Do not add a result file until the corresponding run has actually been executed. Never fabricate screenshots, build results, model outputs, dependency diffs, or rubric scores to make UI Compose appear more mature.

## File naming

Use one JSON file per run:

```text
evals/results/<case-id>/<mode>-<run-id>.json
```

Example:

```text
evals/results/01-vue-element-plus-orders/ui-compose-2026-08-29-a.json
```

Screenshots or other local artifacts should live beside the run or under a clearly referenced artifact folder:

```text
evals/results/01-vue-element-plus-orders/
  ui-compose-2026-08-29-a.json
  ui-compose-2026-08-29-a-desktop.png
  ui-compose-2026-08-29-a-mobile.png
```

The JSON record must conform to `schemas/eval-result.schema.json`.

## Required evidence

A completed run should record:

- case ID
- run mode
- exact model identifier
- UI Compose/skill version or commit
- timestamp
- exact prompt path and immutable prompt revision
- fixture ID and immutable fixture revision
- package-lock (or equivalent dependency baseline) SHA-256
- selected skeleton/patterns when available
- dependency changes
- build/runtime status
- desktop/mobile artifact references
- keyboard notes
- reduced-motion notes
- rubric component scores and total
- hard failures
- decision-error classes

A run may use `build_status: not-run` or null screenshot references while work is in progress, but such a record is **not rendered benchmark evidence** and must not be counted toward delivery readiness.

## Comparison discipline

When comparing modes, keep the host fixture and task brief stable:

- model-only
- generic-frontend-design
- taste-oriented
- ui-compose
- taste-plus-ui-compose

Do not alter one mode's brief after seeing its output unless the case version changes for all modes.

## Score integrity

The rubric component subtotal is the sum of its weighted dimensions:

- visual quality: 25
- design consistency: 15
- task fit: 15
- host-stack compliance: 10
- accessibility: 10
- responsive: 10
- build/runtime success: 5
- dependency discipline: 5
- anti-slop: 5

Without a hard failure, `rubric.total` equals that component subtotal. When a run fails to build or records any hard failure, `rubric.total` is capped at 59 as defined in `evals/rubric.md`; the component values remain available for diagnosis.

## What counts as real benchmark evidence

For delivery-readiness purposes, a run should normally have:

1. `build_status: passed`
2. non-null desktop and mobile screenshots
3. keyboard/focus notes where interactive controls exist
4. reduced-motion notes where motion exists
5. dependency changes recorded, including an empty array when none changed
6. no unresolved runtime hard failure

CI validates the record structure and internal references. It does not certify that a human reviewer agrees with the visual score.

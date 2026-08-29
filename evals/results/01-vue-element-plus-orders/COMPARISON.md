# Eval 01 — Vue + Element Plus Orders

Status: **evidence closed for the first observed comparison run**.

This comparison records what was actually rendered and reviewed for the frozen Vue 3 + Element Plus fixture. It is not a universal quality claim about every model run.

## Compared runs

| Mode | Result record | Score | Build | Hard failures | Decision errors |
| --- | --- | ---: | --- | --- | --- |
| model-only | `model-only-2026-08-28-a.json` | 81 | passed | none | `wrong-skeleton` |
| ui-compose | `ui-compose-2026-08-28-a.json` | 59 (capped; raw 89) | passed | inaccessible primary row inspection | `accessibility-failure` |

Observed raw component delta: **+8 points** for UI Compose on this fixture. After the automatic hard-failure cap, the recorded total delta is **-22 points**.

## What improved

UI Compose selected `master-detail-workspace` with `dense-filter-toolbar`, `master-detail-preview`, and `sticky-contextual-actions`. The rendered desktop view keeps the collection visible beside a 340px preview pane, while mobile uses an explicit list-then-detail flow with a Back action. The run also preserved Element Plus/local wrappers, changed no dependencies, produced no console/page errors, and had no page-level overflow.

The model-only run stayed host-native and keyboard-friendly, but used an Element Plus dialog for inspection. That covers the list and loses the list context the case explicitly asked to preserve, so it was recorded as `wrong-skeleton`.

## What regressed

The UI Compose run lost keyboard row inspection. Its table row inspection is driven by `@row-click` without row `tabIndex`, Enter/Space handling, or keyboard next/previous preview navigation. That is recorded as `accessibility-failure`.

The model-only run did better on this specific interaction: rows were focusable and Enter/Space opened the inspection dialog.

This means the observed result is **not** “UI Compose wins everywhere.” The useful conclusion is narrower:

> UI Compose materially improved composition choice, task fit, and responsive inspection flow, but the adapter/recipe path failed to preserve an accessibility behavior that the simpler baseline happened to implement.

## Evidence set

Model-only:

- `model-only-2026-08-28-a-desktop.png`
- `model-only-2026-08-28-a-desktop-detail.png`
- `model-only-2026-08-28-a-mobile.png`
- `model-only-2026-08-28-a-mobile-detail.png`
- `evals/harness/artifacts/eval-01/model-only-2026-08-28-a-metrics.json`

UI Compose:

- `ui-compose-2026-08-28-a-desktop.png`
- `ui-compose-2026-08-28-a-desktop-detail.png`
- `ui-compose-2026-08-28-a-mobile.png`
- `ui-compose-2026-08-28-a-mobile-detail.png`
- `evals/harness/artifacts/eval-01/ui-compose-2026-08-28-a-metrics.json`

Both result records include build/runtime notes, keyboard notes, reduced-motion notes, dependency changes, selected composition decisions, rubric components, hard failures, and decision errors.

## Product decision

Eval 01 is sufficiently complete to move on. Do **not** rerun merely to erase the accessibility failure from history. Keep it as empirical evidence and turn it into a concrete regression test for future runs:

- row inspection must be keyboard-operable;
- master-detail preview must preserve equivalent keyboard access to pointer inspection;
- if keyboard next/previous is part of the selected recipe, verify it explicitly.

The next high-information case is **Eval 02 — Agent Chat**, where the main questions shift from layout selection to streaming/tool/approval lifecycle, persistent composer behavior, hidden-chain-of-thought boundaries, mobile reachability, and accessible state transitions.

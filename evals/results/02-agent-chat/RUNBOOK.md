# Eval 02 — Comparative runbook

This runbook freezes how the first **model-only vs UI Compose** Agent Chat comparison must be executed. It exists to prevent post-hoc changes to the fixture or acceptance criteria after seeing a result.

## Frozen baseline

Start both runs from the same host fixture:

- fixture: `evals/harness/apps/agent-chat-baseline`
- fixture contract: `evals/harness/fixtures/agent-chat.yaml`
- case: `evals/cases/02-agent-chat.md`
- baseline evidence reference: `evals/results/02-agent-chat/BASELINE-EVIDENCE.md`

Do not change the product brief, required states, forbidden dependencies, viewport checks, or hard-failure criteria between modes.

## Run A — model-only

Give the coding model the Eval 02 case/task and frozen host project without UI Compose guidance.

The model may inspect the host project but must not be given `SKILL.md`, Pattern/Skeleton registries, recipes, physics, adapters, or composition-selection guidance.

Record:

- model/provider/version
- prompt used
- starting commit
- changed files
- dependency diff
- build/runtime result
- selected/implicit layout strategy observed by reviewer
- desktop and mobile screenshots
- capture `metrics.json`
- keyboard/focus notes
- reduced-motion notes
- rubric components
- hard failures
- decision errors

## Run B — ui-compose

Start again from the exact same frozen host baseline.

Give the coding model the same product task plus UI Compose using the normal skill contract. The model should perform:

`Host Read → Host Contract → Design Read → Skeleton → Pattern Set → Recipe → Adapter → Verify`

Record explicitly:

- detected Host Contract
- selected Skeleton
- selected Patterns
- recipes/adapters used
- rejected alternatives when relevant
- dependency decision
- the same evidence fields required for model-only

## Shared capture gate

Both transformed runs must pass through the same browser capture checks used by the baseline. Do not weaken checks per mode.

Minimum machine-observed checks:

- no console/page errors
- no horizontal overflow at desktop or 390px
- streaming state exists
- tool queued/running/success/failure states are distinguishable with text
- approval-required state exists and names consequence + scope
- disconnected and retryable-error states exist
- Stop, Retry, and approval actions are keyboard-operable with visible focus
- composer remains reachable around 390×844 and reduced-height 390×560
- reduced-motion disables transient caret animation
- no rendered hidden-chain-of-thought/reasoning-claim copy

## Hard failures

Use the case/fixture contract as authoritative. In particular:

- claims hidden chain-of-thought is visible
- fabricated progress presented as provider fact
- tool failure visually indistinguishable from success
- consequential approval is ambiguous about action or scope
- approval makes the destructive/consequential action the ambiguous default
- composer becomes unreachable under mobile keyboard conditions
- unnecessary full AI/component library replaces the host system
- runtime/build failure

Do not convert a hard failure into a small rubric deduction merely because the screen looks polished.

## Comparison discipline

The baseline itself receives no comparative score. Score only the two transformed runs.

A valid conclusion must distinguish at least:

1. **composition quality** — workspace structure, information hierarchy, task fit;
2. **state completeness** — streaming, tools, approval, disconnected/error/retry;
3. **host integration** — host primitives/tokens and dependency discipline;
4. **interaction quality** — keyboard, focus, stop/retry/approval, composer reachability;
5. **AI safety/semantics** — provider-visible activity only, no hidden-CoT claims;
6. **responsive quality** — 390px behavior and no page overflow.

Do not claim UI Compose wins if it improves structure while regressing accessibility or lifecycle correctness. Preserve regressions as evidence, as done in Eval 01.

## Result storage

Only after an actual transformed run exists, add a result record under:

`evals/results/02-agent-chat/`

Suggested names:

- `model-only-YYYY-MM-DD-a.json`
- `ui-compose-YYYY-MM-DD-a.json`

Store committed screenshots or stable artifact references required by the Eval Result schema. Then add `COMPARISON.md` summarizing observed deltas and regressions.

# Eval 02 — Prompt contract

Status: **frozen before transformed runs**.

This document defines the prompt envelope for the first model-only vs UI Compose Agent Chat comparison. It prevents prompt drift between modes while keeping evaluator instrumentation separate from product requirements.

## Shared task text

Give both runs this same task text verbatim:

```text
Work in the provided Agent Chat host fixture.

Build an AI agent conversation workspace that supports:
- streamed assistant output;
- tool invocation with queued, running, success, and failure states;
- source/context inspection;
- user approval before a consequential action;
- stop and retry behavior;
- a persistent composer with attachments;
- mobile behavior around 390px;
- loading, disconnected, and failed states.

Preserve the existing host primitive/token system unless a concrete behavioral requirement cannot be met with it. Do not expose or fabricate hidden chain-of-thought. Product-visible execution state must reflect provider/runtime-visible state. Approval must make the action, affected scope, and consequence clear before commit.

Keep the evaluator-only semantic hooks documented in CAPTURE-CONTRACT.md attached to the corresponding real product states and controls. You may freely change layout, styling, component hierarchy, CSS classes, and visible copy. Do not add evaluator-only visible UI or fake product state to satisfy the benchmark.

Run the fixture's existing tests/build checks after implementation. Do not edit benchmark result files or scoring criteria.
```

## Run A — model-only envelope

Provide only:

1. the frozen host fixture;
2. `evals/cases/02-agent-chat.md`;
3. the shared task text above;
4. `evals/harness/apps/agent-chat-baseline/CAPTURE-CONTRACT.md` solely as evaluator instrumentation.

Do **not** provide or point the model to:

- `SKILL.md`;
- Source / Pattern / Skeleton registries;
- recipes or Physics guidance;
- composition-selection guidance;
- UI Compose adapters;
- `references/ai-native-evidence-2026-08-31.md`;
- previous Eval 01 conclusions or Eval 02 scoring expectations.

The evaluator may know these materials exist, but the model-only coding context must not contain their guidance.

## Run B — UI Compose envelope

Provide the exact same frozen host fixture, case, shared task text, and capture contract, then additionally invoke UI Compose through its normal skill entry point.

Do not hand-pick Patterns or a Skeleton in the prompt. The coding model must derive them through the normal pipeline:

`Host Read → Host Contract → Design Read → Skeleton → Pattern Set → Recipe → Adapter → Verify`

The model should record its detected Host Contract, chosen Skeleton/Patterns, rejected alternatives when material, adapter/recipe decisions, and dependency decision as normal evaluation evidence.

## Controlled variables

For the first comparison, keep these identical across both modes:

- model/provider/version;
- frozen fixture starting revision;
- shared task text;
- repository state outside the mode-specific guidance;
- execution environment and package manager;
- build/test/capture workflow;
- viewport sizes;
- rubric and hard-failure criteria;
- evaluator observability hooks.

The only intended independent variable is **UI Compose guidance available vs unavailable**.

If a run requires a product fix unrelated to missing evaluator hooks, do not patch it before scoring. Preserve the failure as evidence. If only an evaluator hook was lost while the real product state/control still exists, restore the hook without changing visible behavior and recapture; mark the first capture invalid rather than failed.

## Result provenance

Each result record must identify:

- the model/provider/version;
- the exact starting fixture revision;
- the transformed branch/source revision;
- this prompt contract as `prompt_ref` (or a stable generated prompt derived from it);
- the commit SHA containing the exact prompt contract as `prompt_revision`;
- the capture artifact/run id and capture source SHA;
- dependency diff from the same frozen start.

Do not create `COMPARISON.md` until both valid transformed runs exist under these controls.

# AI-native evidence pass — 2026-08-31

Purpose: strengthen Eval 02 and future AI-native composition without turning protocol/component projects into default runtime dependencies.

## Promotion rule

These projects are evidence of durable interaction/state decisions. UI Compose should re-express the decisions through the detected host stack unless the host already uses the source stack and the dependency is justified.

## AG-UI

Canonical: https://github.com/ag-ui-protocol/ag-ui
License: MIT
Status checked: 2026-08-31

Durable evidence:

- agent UI is an event/state lifecycle, not a stream of decorative chat bubbles;
- message, tool, state and human-in-the-loop transitions need distinct observable states;
- transport is separable from UI composition (SSE/WebSocket/etc. must not dictate the visual system);
- frontend state must be able to reconcile incremental updates without fabricating progress.

Useful for existing Patterns:

- `ai-conversation-thread`
- `ai-tool-execution-card`
- `ai-activity-summary`
- `human-approval-gate`

Do not:

- make AG-UI a required transport/runtime;
- map protocol event names 1:1 to visible chrome when a simpler host-native state is clearer;
- expose hidden reasoning merely because an event stream contains provider/runtime metadata.

## assistant-ui/tool-ui

Canonical: https://github.com/assistant-ui/tool-ui
License: MIT
Status checked: 2026-08-31

Durable evidence:

- tool payloads should not default to raw JSON dumps;
- tool calls can resolve into task-shaped host UI: approval cards, forms, tables, diffs, media and progress;
- schemas/validated payload shapes help keep rendering bounded and predictable;
- approval UI must communicate the action and its consequence before the user commits.

Useful for existing Patterns:

- `ai-tool-execution-card`
- `human-approval-gate`
- future artifact/output patterns if repeated eval evidence supports promotion.

Do not:

- install the component catalog solely because a tool returns JSON;
- copy its visual identity into a non-React host;
- treat every tool output as a card when inline text or the host's existing table/form is better.

## A2UI

Canonical: https://github.com/a2ui-project/a2ui
License: Apache-2.0
Status checked: 2026-08-31
Current maturity: public preview / v1.0 specification release-candidate path; evolving.

Durable evidence candidate:

- agent-generated UI should be declarative data mapped into a trusted, pre-approved host component catalog rather than arbitrary executable UI code;
- structure and implementation vocabulary should remain separable;
- incremental UI updates should target stable component IDs/state rather than regenerate an entire page blindly;
- trust boundaries belong in the renderer/adapter, not in model styling instructions.

This aligns strongly with `Host Read → Host Contract → ... → Adapter`, but is **not yet promoted to a canonical Pattern** because protocol/renderers are still evolving and UI Compose has not yet observed a repeated eval need for agent-generated arbitrary forms/cards.

## Candidate registry decisions

### Ready to strengthen existing Pattern evidence

1. `ai-tool-execution-card`
   - candidate evidence: assistant-ui/tool-ui
   - reason: second independent source for task-shaped tool output and explicit status/action UI.

2. `human-approval-gate`
   - candidate evidence: assistant-ui/tool-ui plus AG-UI human-in-the-loop semantics
   - reason: consequence-aware approval is now supported by both component-level and protocol-level evidence.

3. `ai-conversation-thread` / `ai-activity-summary`
   - candidate evidence: AG-UI
   - reason: incremental event lifecycle reinforces explicit observable state without requiring provider-specific presentation.

### Hold as research candidate

`trusted-generative-ui-slot` (working name)

Possible structure:

- trusted component catalog
- declarative payload
- bounded data binding
- incremental update target
- validation/error fallback
- explicit user action boundary

Risks:

- protocol churn;
- arbitrary generated-form complexity;
- security boundary confusion;
- runtime/schema dependency creep;
- turning every AI response into generative UI.

Promotion gate: require at least one additional independent mature source plus an eval where ordinary message/tool Patterns are insufficient.

## Eval 02 consequences

Eval 02 should continue to score product-visible lifecycle rather than protocol compliance. Strengthen review with these assertions:

- queued/running/success/failure are derived from actual host/runtime state, not decorative timers;
- failed tools never reuse success styling or collapse into an indistinguishable generic card;
- structured tool output is rendered in the smallest task-appropriate host primitive, not raw JSON by default;
- approval identifies action, scope and consequence before commit;
- approval/reject remain keyboard operable with visible focus;
- provider-visible activity may be summarized, but hidden chain-of-thought must not be claimed or rendered;
- no new AI UI/protocol dependency is added unless the transformed run demonstrates a behavioral need the host cannot already satisfy.

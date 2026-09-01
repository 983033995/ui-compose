# AI-native evidence pass — 2026-08-31

Purpose: strengthen Eval 02 and future AI-native composition without turning protocol/component projects into default runtime dependencies.

Last reviewed: 2026-09-01.

## Promotion rule

These projects are evidence of durable interaction/state decisions. UI Compose should re-express the decisions through the detected host stack unless the host already uses the source stack and the dependency is justified.

A protocol or SDK is not automatically a Pattern. Prefer the smallest product-visible representation that preserves task semantics and the host trust boundary.

## AG-UI

Canonical: https://github.com/ag-ui-protocol/ag-ui
License: MIT
Status checked: 2026-09-01

Durable evidence:

- agent UI is an event/state lifecycle, not a stream of decorative chat bubbles;
- message, tool, state and human-in-the-loop transitions need distinct observable states;
- transport is separable from UI composition (SSE/WebSocket/etc. must not dictate the visual system);
- frontend state must be able to reconcile incremental updates without fabricating progress;
- shared state is explicitly bidirectional and persistent across agent/frontend interactions, reinforcing stable state reconciliation rather than whole-thread regeneration.

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
Status checked: 2026-09-01

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

Canonical: https://a2ui.org/ and https://github.com/a2ui-project/a2ui
License: Apache-2.0
Status checked: 2026-09-01
Current maturity: v0.9 stable family, v0.9.1 current; v1.0 remains candidate/evolving.

Durable evidence candidate:

- agent-generated UI can be declarative data mapped into a trusted, pre-approved host component catalog rather than arbitrary executable UI code;
- structure and application data remain separable;
- streamed messages can progressively create/update a surface and its data model rather than regenerate an entire page blindly;
- incremental UI updates target stable surfaces/components/state;
- trust boundaries belong in the renderer/component catalog, not in model styling instructions;
- the same abstract surface can render through platform-native widgets, reinforcing Adapter ownership of implementation vocabulary.

This aligns strongly with `Host Read → Host Contract → Design Read → Skeleton → Pattern Set → Adapter → Verify`, but is **not yet promoted to a canonical Pattern** because UI Compose has not observed a repeated eval need where ordinary conversation/tool Patterns are insufficient.

## MCP Apps

Canonical: https://github.com/modelcontextprotocol/ext-apps
Specification family: MCP UI extension (`io.modelcontextprotocol/ui`)
Status checked: 2026-09-01

Durable evidence candidate:

- some tool outputs genuinely need an embedded interactive application rather than a message/card/form primitive;
- UI resources are predeclared and associated with tools rather than being arbitrary HTML emitted inline by the model;
- the host owns capability negotiation, sandboxing, display mode and bridge permissions;
- UI and tool data remain separable: the host can preload/review a UI resource while dynamic data arrives through tool execution;
- bidirectional interaction can remain auditable through the host bridge;
- progressive enhancement matters: hosts without the UI extension still need meaningful non-UI tool results/fallbacks.

Important distinction from A2UI:

- A2UI is primarily a **host-native declarative rendering** model: agent data is mapped into a trusted component catalog;
- MCP Apps is primarily a **sandboxed embedded-app** model: a predeclared HTML resource runs inside a host-controlled iframe/bridge;
- these are different trust/performance/composition boundaries and must not be collapsed into one default implementation strategy.

Current risk:

- MCP Apps is still evolving; the 2026-07-28 capability-negotiation documentation has active mismatch reports in the official repository;
- host support varies;
- iframe/app-bridge cost is materially higher than a host-native Pattern;
- a full embedded app should therefore be an escalation path, not the default response to structured tool output.

Do not:

- add `@modelcontextprotocol/ext-apps` as a UI Compose runtime dependency;
- iframe ordinary approvals, short forms or tables that the host primitive system can already express;
- assume every MCP-capable host supports MCP Apps;
- treat host-provided theme variables as permission to clone another host's visual identity.

## AI output escalation ladder

Use this as a research decision aid, not a new Registry entry:

1. **text / inline status** — enough for simple explanations or compact state;
2. **existing host primitive** — table, form, diff, approval, media, details;
3. **trusted declarative host-native surface** — candidate when the agent must compose a bounded interactive surface from an approved catalog;
4. **sandboxed embedded app** — candidate only when the interaction is genuinely application-like (canvas, complex dashboard/modeler, rich direct manipulation) and the host explicitly supports it.

Escalate only when the previous level cannot satisfy the task. Each escalation increases state, security, accessibility, responsive and dependency/integration cost.

## Candidate registry decisions

### Ready to strengthen existing Pattern evidence

1. `ai-tool-execution-card`
   - candidate evidence: assistant-ui/tool-ui + AG-UI lifecycle semantics
   - reason: task-shaped tool output and explicit execution state are independently supported.

2. `human-approval-gate`
   - candidate evidence: assistant-ui/tool-ui + AG-UI human-in-the-loop semantics
   - reason: consequence-aware approval is supported by both component-level and protocol-level evidence.

3. `ai-conversation-thread` / `ai-activity-summary`
   - candidate evidence: AG-UI
   - reason: incremental event/state lifecycle reinforces explicit observable state without provider-specific chrome.

### Hold as research candidates

`trusted-generative-ui-slot` (working name)

Possible structure:

- trusted component catalog
- declarative payload
- bounded data binding
- incremental update target
- validation/error fallback
- explicit user action boundary

Independent support now exists from A2UI plus the broader MCP Apps/tool-UI ecosystem for richer-than-text interactive outputs, but **promotion still fails the eval gate**: UI Compose has not yet observed a benchmark where ordinary host message/tool/form/table Patterns are insufficient.

`embedded-tool-app-surface` (working name)

Possible structure:

- predeclared UI resource
- host capability negotiation
- sandboxed execution boundary
- tool/data bridge
- host theme/context bridge
- fallback non-UI result
- explicit fullscreen/inline/PiP eligibility

Hold outside the Registry until at least one real eval requires direct-manipulation/application-like tool UI and demonstrates that a host-native surface is insufficient.

Risks across both candidates:

- protocol churn;
- arbitrary generated-form/app complexity;
- security boundary confusion;
- runtime/schema/bridge dependency creep;
- turning every AI response into generative UI;
- host portability claims that exceed actual host capability support.

## Eval consequences

Eval 02 should continue to score product-visible lifecycle rather than protocol compliance. Strengthen review with these assertions:

- queued/running/success/failure are derived from actual host/runtime state, not decorative timers;
- failed tools never reuse success styling or collapse into an indistinguishable generic card;
- structured tool output is rendered in the smallest task-appropriate host primitive, not raw JSON by default;
- approval identifies action, scope and consequence before commit;
- approval/reject remain keyboard operable with visible focus;
- provider-visible activity may be summarized, but hidden chain-of-thought must not be claimed or rendered;
- no new AI UI/protocol dependency is added unless the transformed run demonstrates a behavioral need the host cannot already satisfy;
- choosing declarative generative UI or an embedded app without a demonstrated task need counts as unnecessary complexity/dependency/integration cost, even if visually impressive.

Future eval need: add a separate generative/direct-manipulation case only after Eval 02 is closed, so Eval 02 remains a clean test of agent-chat lifecycle rather than being expanded post-hoc.

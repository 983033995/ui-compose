# Canonical pattern recipes

This file turns selected Pattern IDs into host-neutral implementation guidance. Recipes describe **structure, behavior, state, and interaction contracts**. They are not React/Vue/Tailwind snippets and must be adapted through Host Read + the selected adapter.

A canonical Pattern should not remain a registry label forever. If a pattern cannot yet explain how it behaves without cloning a source implementation, treat it as research evidence rather than a mature recipe.

## `dense-filter-toolbar`

**Use when:** high-frequency data browsing requires search, filter, sort, result context, and contextual actions.

**Structure:**

```text
primary search | high-frequency filters | view/sort options | result count | contextual actions
active filter summary / clear-all when needed
```

**Recipe:**

- Keep the most frequent search/filter controls visible; push low-frequency filters into one secondary surface.
- Search should usually own the largest flexible width.
- Do not create a card around every control; the toolbar is one compositional row/region.
- Active filters must remain inspectable after a popover/dropdown closes.
- Bulk actions appear only when selection exists and must not cause the whole toolbar to reflow unpredictably.
- On narrow screens, preserve search + primary filter entry first; move the remainder to a sheet/popover or stacked second row.
- Loading must not erase filter state.

**Avoid:** duplicated filter state, hidden active filters, arbitrary control widths, animated keyboard navigation.

## `master-detail-preview`

**Use when:** users repeatedly browse a collection and inspect/triage items without losing collection context.

**Structure:**

```text
collection/list
  ↕ focused item
preview/detail region
primary detail actions
```

**Recipe:**

- Keep selection/focus in the collection while the detail region updates.
- Arrow/next-prev navigation updates the preview without stealing focus into the detail pane.
- Preview loading should preserve the shell and focused-row identity.
- Escape closes an optional transient preview and returns focus to the originating row.
- Desktop may use split pane, peek panel, or drawer based on available space.
- Mobile should normally become list → detail route/sheet rather than shrinking a two-pane desktop layout.
- Destructive or state-changing actions belong in the detail region, not hidden behind hover-only row controls.

**Avoid:** mobile two-pane overflow, focus loss after every preview update, full-page navigation for every triage action when context retention matters.

## `ai-conversation-thread`

**Use when:** an AI surface needs messaging, streaming, tool/activity parts, retry, sources, and a persistent composer.

**Structure:**

```text
scrollable thread
  ├─ user turn
  └─ assistant turn
       ├─ answer content
       ├─ optional activity/tool parts
       ├─ sources
       └─ retry/error affordance
persistent composer
```

**Recipe:**

- Keep stable content stable while new content streams.
- Treat tool calls, approvals, and sources as typed message parts rather than forcing everything into chat bubbles.
- Autoscroll only while the user is already following the tail; never fight manual scrolling.
- Failed assistant turns preserve already-produced content when technically possible and expose retry.
- Completed streaming state removes active indicators such as the caret/shimmer.
- Composer stays spatially predictable and respects mobile keyboard/safe-area behavior.

See `../ai-primitives.md` for streaming and tool-state recipes.

## `ai-tool-execution-card`

**Use when:** an agent invokes tools whose lifecycle matters to the user.

**Structure:**

```text
tool identity | concise action | status
optional input summary
optional output summary / error
inspect details / retry
```

**Recipe:**

- One compact row/card per invocation; do not render raw JSON as primary chrome.
- State color belongs on icon/status, not a full-card success/error wash.
- `queued → running → success|failed|cancelled` must be visually distinguishable without relying on animation.
- Large payloads belong behind accessible disclosure.
- Retry appears only when meaningful and should preserve the original action context.
- Do not pulse or shimmer the whole card.

## `human-approval-gate`

**Use when:** the user must approve, reject, choose, or confirm an agent action.

**Structure:**

```text
what is being decided
why / consequence
options or requested change
secondary action | primary action
```

**Recipe:**

- State the consequence before the action buttons.
- One decision should be visually primary; avoid presenting a dense settings form as an approval gate.
- Choice rows must be keyboard operable and expose selected state semantically.
- Submitting disables duplicate submission but keeps the selected choice visible.
- Destructive approval is never the visually ambiguous default.
- Rejection/cancel should be a first-class path when the workflow permits it.

## `persistent-composer`

**Use when:** a conversational/agent surface needs prompt entry across the whole task lifecycle.

**Structure:**

```text
context/attachment affordances | growing input | optional mode/command entry | send/stop
```

**Recipe:**

- Start compact; grow vertically with content instead of opening as a large empty textarea.
- Reuse host input/button/overlay primitives.
- Slash-command or mode menus open near the composer without covering the current input unnecessarily.
- Arrow-key menu movement is instant.
- Send switches to stop/cancel only when the product can actually cancel.
- Disabled/submitting states preserve readable text rather than blanking the input.
- On mobile, account for virtual keyboard and safe-area insets.

## `sticky-contextual-actions`

**Use when:** selected rows/items expose temporary bulk or save actions.

**Structure:**

```text
selection summary | primary contextual action | secondary actions | dismiss/clear
```

**Recipe:**

- Hidden when no selection/context exists.
- Placement must not cover important content; reserve safe space or anchor to a known region.
- Selection count/context remains visible while submitting.
- Clearing selection dismisses the action surface predictably.
- Do not move ordinary global actions into this surface just because space exists.

## Recipe maturity rule

When adding a new canonical Pattern, include at least:

1. when to use it;
2. structural regions/roles;
3. required states;
4. host-neutral behavior recipe;
5. mobile/accessibility consequence where relevant;
6. failure/anti-pattern notes.

Keep recipes concise enough for on-demand reading. Source evidence belongs in `registry.yaml`; provenance belongs in `../sources/`.
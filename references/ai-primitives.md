# AI-native primitives

AI interfaces need explicit states for streaming, tools, approvals, sources, progress, retry, and task lifecycle. Treat external products such as AI Elements and Beautiful UI as evidence of useful interaction decisions, not as a requirement to copy their code, tokens, or wording.

Always adapt to the host project's component system and tokens. CSS below uses `--host-*` placeholders: map them onto the host theme and remove the placeholders in the final implementation.

## 1. Streaming response

A streaming answer should remain readable while content arrives.

Good behavior:

- keep already-rendered text stable
- indicate only the in-flight tail or active status
- avoid typewriter animation over the whole response
- preserve scroll position unless the user is already following the tail
- expose stop/cancel when the product supports it
- provide a clear reduced-motion path

Do not animate every token or blur long passages.

### Host-neutral recipe

Only the last few in-flight tokens are eligible for soft treatment. The active caret is a 2px bar while generation is running. **Unmount or hide it when generation is complete.** A completed answer must not keep blinking as if it is still active.

```css
.stream-caret {
  display: inline-block;
  width: 2px;
  height: 1.05em;
  margin-left: 1.5px;
  border-radius: 1px;
  background: var(--host-fg);
  vertical-align: text-bottom;
}
.stream-caret[hidden] { display: none; }
.stream-tail {
  filter: blur(1.4px);
  -webkit-mask-image: linear-gradient(90deg, #000 25%, #0004);
          mask-image: linear-gradient(90deg, #000 25%, #0004);
}
@media (prefers-reduced-motion: reduce) {
  .stream-tail {
    filter: none;
    -webkit-mask-image: none;
    mask-image: none;
  }
}
```

Split the streamed string into a stable head and the last ~2–3 in-flight tokens. Apply `.stream-tail` only while streaming. When the provider emits `done`, render all text normally and remove/hide the caret.

Status-line shimmer, if used, belongs on an activity label, never on the answer body.

```css
@keyframes host-shimmer-text {
  0% { background-position: 150%; }
  100% { background-position: -50%; }
}
.shimmer-line {
  background-image: linear-gradient(
    90deg,
    var(--host-muted) 0%,
    var(--host-fg) 50%,
    var(--host-muted) 100%
  );
  background-size: 220% 100%;
  background-clip: text;
  color: transparent;
  animation: host-shimmer-text 1.6s linear infinite;
}
@media (prefers-reduced-motion: reduce) {
  .shimmer-line {
    animation: none;
    color: var(--host-muted);
    background: none;
  }
}
```

## 2. Activity / reasoning summary

Never imply access to hidden chain-of-thought. Use labels such as Activity, Progress, Execution trace, Reasoning summary, Search activity, or Tool activity only for provider-exposed summaries, product-owned progress events, or actual tool events.

Recommended structure:

```text
status line + elapsed time
  └─ optional expandable summary
       ├─ search/tool step
       ├─ product-owned progress event
       └─ provider-exposed summary
```

Collapsed by default is often appropriate for secondary activity. Expansion must be keyboard accessible and should not block the main answer. For animated disclosure, use an interruptible short height/fade transition; keyboard-driven toggles may be instant under reduced motion.

## 3. Tool execution

Do not dump raw JSON as the primary UI.

Compact tool execution should show tool identity, concise action label, queued/running/success/failed/cancelled state, a small input/output summary, and retry or inspect-details when useful. Full payloads or logs belong in an expandable region.

State color should usually live on the status/icon, not wash the entire card.

### Host-neutral recipe

```html
<div class="tool-row" data-state="running">
  <span class="tool-row-icon" aria-hidden="true"></span>
  <span class="tool-row-title">Read SKILL.md</span>
  <span class="tool-row-meta">running</span>
</div>
```

```css
.tool-row {
  display: flex;
  align-items: center;
  gap: var(--host-space-2, .5rem);
  min-height: 1.75rem;
  padding: .25rem .5rem;
  border-radius: var(--host-radius-control, 8px);
  background: var(--host-surface);
  box-shadow: 0 0 0 1px var(--host-border);
  font-size: .75rem;
}
.tool-row-title { min-width: 0; flex: 1; }
.tool-row-meta { color: var(--host-muted); }
.tool-row[data-state="failed"] .tool-row-icon { color: var(--host-danger); }
```

## 4. Human approval gate

Approval UI must explain the decision and consequence before asking for confirmation.

Recommended structure:

```text
decision context
consequence summary
options / requested change
secondary action   primary action
```

Required states: awaiting decision, selected, submitting, approved, rejected, failed.

### Host-neutral recipe

Show one clear question at a time. Use selectable rows or the host's accessible choice primitive. Selected state should be visually explicit without filling the entire surface with brand color. Footer hierarchy: quiet secondary action + clear primary action. Destructive approval must never be the ambiguous default.

## 5. Composer

The composer is a persistent work surface, not automatically a giant textarea.

Common capabilities: auto-growing input, attachments, context/source entry, slash commands, model/mode picker only when needed, and send/stop.

Host-neutral defaults:

- resting height around 40–44px when compatible with host controls
- grows with content rather than starting oversized
- `/` command menu opens near the composer and follows host overlay behavior
- arrow-key highlight is instant
- mobile verifies virtual-keyboard overlap and safe-area behavior

## 6. Sources and context

Useful forms include quiet inline citations, a source list below the answer, expandable context cards, filename/URL labels, and retrieved-chunk metadata when relevant. Avoid turning every source into a loud badge or carousel.

## 7. Task lifecycle

```text
queued → running → completed
                 ↘ failed
                 ↘ cancelled
```

A task row may include action label, real progress/count, duration, output link, and retry. Do not fabricate percentages. Use indeterminate progress when the system cannot provide a meaningful estimate. Do not pulse the whole row for state changes.

## 8. Recommendation / next action

Keep recommendations concise and decisions explicit. Do not add confidence gauges or percentages unless the number is calibrated and useful.

## 9. Motion policy for AI surfaces

Most AI-native UI should be calmer than marketing UI.

- status changes: subtle opacity/position change
- disclosure: short interruptible height/fade transition
- keyboard-driven movement: instant
- tool state changes: avoid pulsing whole rows
- streaming: no global shimmer across content
- reduced motion: remove non-essential animation
- never use `transition: all`

Use `references/physics.md` for fallback timing/radius/type guidance when the host has no equivalent tokens.

## 10. Verification checklist

- [ ] streaming text remains readable
- [ ] active caret disappears when generation completes
- [ ] user can stop/cancel when supported
- [ ] tool states include failure and retry paths
- [ ] approvals explain consequences
- [ ] composer works with keyboard and mobile virtual keyboard
- [ ] sources are inspectable without overwhelming the answer
- [ ] no fabricated progress percentages
- [ ] no wording implies hidden chain-of-thought
- [ ] reduced motion is supported
- [ ] all interactive states remain accessible

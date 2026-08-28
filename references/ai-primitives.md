# AI-native primitives

AI interfaces need explicit states for streaming, tools, approvals, sources, progress, retry, and task lifecycle. Treat external products such as AI Elements and Beautiful UI as evidence of useful interaction decisions, not as a requirement to copy their code, tokens, or wording.

Always adapt to the host project's component system and tokens. CSS below uses `--host-*` placeholders — map them onto the host theme, then delete the placeholders.

## 1. Streaming response

A streaming answer should remain readable while content arrives.

Good behavior:

- keep already-rendered text stable
- indicate only the in-flight tail or status
- avoid typewriter animation over the whole response
- preserve scroll position unless the user is already following the tail
- expose stop/cancel when the product supports it
- reduced-motion path must remain clear

Do not animate every token or blur long passages.

### Host-neutral recipe

Only the last few in-flight tokens are soft. The caret is a 2px bar, solid while tokens arrive, blinking when idle.

```css
@keyframes host-caret-blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}
.stream-caret {
  display: inline-block;
  width: 2px;
  height: 1.05em;
  margin-left: 1.5px;
  border-radius: 1px;
  background: var(--host-fg);
  vertical-align: text-bottom;
  animation: host-caret-blink 1s step-end infinite;
}
.stream-caret.is-streaming { animation: none; }
.stream-tail {
  filter: blur(1.6px);
  -webkit-mask-image: linear-gradient(90deg, #000 20%, #0003);
          mask-image: linear-gradient(90deg, #000 20%, #0003);
}
@media (prefers-reduced-motion: reduce) {
  .stream-caret { animation: none; }
  .stream-tail { filter: none; -webkit-mask-image: none; mask-image: none; }
}
```

Split the streamed string on whitespace. Head renders normally. Tail (last ~3 tokens while streaming) uses `.stream-tail`. Caret gets `.is-streaming` until `done`.

Status-line shimmer, if used, belongs on the activity label — never on the answer body.

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

Never imply access to hidden chain-of-thought.

Use labels such as:

- Activity
- Progress
- Execution trace
- Reasoning summary
- Search activity
- Tool activity

Only show provider-exposed summaries, product-owned progress events, or actual tool events.

Recommended structure:

```text
status line + elapsed time
  └─ optional expandable summary
       ├─ search/tool step
       ├─ product-owned progress event
       └─ provider-exposed summary
```

Collapsed by default is often appropriate for secondary activity. Expansion must be keyboard accessible and should not block the main answer.

Height disclosure: `grid-template-rows: 0fr → 1fr`, ~180ms ease-out, interruptible. Keyboard toggle is instant under reduced motion.

## 3. Tool execution

Do not dump raw JSON as the primary UI.

Compact tool execution should show:

- tool identity
- concise action label
- queued/running/success/failed/cancelled state
- small input summary
- small output summary
- retry or inspect details when useful

Full payloads, code, or logs belong in an expandable detail region.

State color should usually live on the status/icon, not wash the entire card.

### Host-neutral recipe

One compact row per tool call. Hairline ring, chip radius, 12px type. Status color on the icon only.

```html
<div class="tool-chip" data-state="running">
  <span class="tool-chip-icon" aria-hidden="true"></span>
  <span class="tool-chip-title">Read SKILL.md</span>
  <span class="tool-chip-meta">queued → running</span>
</div>
```

```css
.tool-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  height: 1.75rem;
  padding: 0 0.5rem;
  border-radius: var(--host-radius-chip, 6px);
  background: var(--host-surface);
  box-shadow: 0 0 0 1px var(--host-border);
  font-size: 12px;
}
.tool-chip-meta { color: var(--host-muted); }
.tool-chip[data-state="failed"] .tool-chip-icon { color: var(--host-danger); }
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

Required states:

- awaiting decision
- selected
- submitting
- approved
- rejected
- failed

Destructive approval should never be the ambiguous default.

### Host-neutral recipe

One question visible. Options are selectable rows, not radio soup. Footer: quiet secondary + solid primary. Pagination in tabular nums if stacked.

Selected option: 1px primary ring, not a fill wash of the whole row.

## 5. Composer

The composer is a persistent work surface, not automatically a giant textarea.

Common capabilities:

- auto-growing input
- attachment entry
- source/context entry
- slash command entry
- model/mode picker when the product truly needs it
- send / stop

Keyboard navigation should be immediate. Do not animate the highlight that follows arrow-key selection.

On mobile, verify virtual-keyboard overlap and safe-area behavior.

Resting height ~44px, grows with input. `/` opens commands *above* the bar. Command highlight that follows arrow keys is instant.

## 6. Sources and context

Sources should support verification without dominating the answer.

Useful forms:

- quiet inline citation
- source list below the answer
- expandable context cards
- filename / URL / document label
- retrieved chunk metadata when relevant

Avoid turning every source into a loud badge or carousel.

Inline sources are quiet text links, not chips in the paragraph. Follow-ups sit **under** the answer as secondary actions, not in the prose.

## 7. Task lifecycle

Long-running agent work should expose explicit lifecycle states:

```text
queued → running → completed
                 ↘ failed
                 ↘ cancelled
```

A task row may include:

- action label
- progress or count when real
- duration
- artifact/output link
- retry for failed work

Do not fabricate percentages. Use indeterminate progress when the underlying system cannot provide a meaningful estimate.

Progress (`68%`, `12/12`) is tabular-nums. Do not pulse the whole row. Failed uses restrained danger color on the label only.

## 8. Recommendation / next action

When the model proposes an action, keep the recommendation concise and make the decision explicit.

Useful structure:

```text
recommendation
short rationale / confidence wording when meaningful
primary action   alternatives
```

Do not add gauge charts or confidence percentages unless the number is actually calibrated and useful.

## 9. Motion policy for AI surfaces

Most AI-native UI should be calmer than marketing UI.

- status changes: subtle opacity/position change
- disclosure: short interruptible height/fade transition
- keyboard-driven movement: instant
- tool state changes: avoid pulsing whole rows
- streaming: no global shimmer across content
- reduced motion: remove non-essential animation
- never use `transition: all`

A small status shimmer or caret can be acceptable when it communicates active work, but the rest of the interface should remain stable.

Enter: 180–220ms ease-out. Menus from a trigger: ~160ms from 0.95, origin at the trigger. Press scale: pick 0.94 or 0.96 for the whole app, not both.

## 10. Verification checklist

- [ ] streaming text remains readable
- [ ] user can stop/cancel when supported
- [ ] tool states include failure and retry paths
- [ ] approvals explain consequences
- [ ] composer works with keyboard and mobile virtual keyboard
- [ ] sources are inspectable without overwhelming the answer
- [ ] no fabricated progress percentages
- [ ] no wording implies hidden chain-of-thought
- [ ] reduced motion is supported
- [ ] all interactive states remain accessible

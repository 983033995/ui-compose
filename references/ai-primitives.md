# AI-native primitives

AI interfaces need explicit states for streaming, tools, approvals, sources, progress, retry, and task lifecycle. Treat external products such as AI Elements and Beautiful UI as evidence of useful interaction decisions, not as a requirement to copy their code, tokens, or wording.

Always adapt to the host project's component system and tokens.

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

## 6. Sources and context

Sources should support verification without dominating the answer.

Useful forms:

- quiet inline citation
- source list below the answer
- expandable context cards
- filename / URL / document label
- retrieved chunk metadata when relevant

Avoid turning every source into a loud badge or carousel.

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

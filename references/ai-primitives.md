# AI-native primitives (Beautiful UI, reverse-engineered)

Source: [beautifului.dev](https://www.beautifului.dev/) — copy-paste
primitives for chat agents, thinking, streaming, approvals, tool calls.
There is no package. Reimplement against **this app's tokens**.

Reverse-engineered from their CSS (oklch tokens, Inter, 14px base,
`--ease-out-strong: cubic-bezier(.23, 1, .32, 1)`, hairline shadows,
radii 6/8/10/14).

Map their names onto `@theme`:

| Beautiful UI | This app |
| --- | --- |
| `--page` / `--canvas` / `--surface` / `--field` | `--color-bg` / `--color-surface` |
| `--ink` / `--ink-2` / `--ink-3` | `--color-fg` / `--color-muted` |
| `--line` / `--line-strong` | `--color-border` |
| `--accent` | `--color-primary` |
| `--radius-chip: 6px` `--radius-control: 8px` `--radius-card: 10px` `--radius-window: 14px` | concentric scale in `design-ui` |
| `--shadow-hairline: 0 0 0 1px var(--line)` | prefer over drop shadows |
| `--ease-out-strong` | `--ease-out` / `cubic-bezier(0.23, 1, 0.32, 1)` |

Their document extras worth copying once in `src/styles.css`:

```css
html {
  font-feature-settings: "cv11", "ss01";
  letter-spacing: -0.01em;
}
::selection {
  background: color-mix(in oklab, var(--color-primary) 18%, transparent);
}

/* Optional editorial canvas — marketing or docs shells only, never dashboards */
.stripe-canvas {
  background-color: var(--color-bg);
  background-image: repeating-linear-gradient(
    -45deg,
    transparent 0,
    transparent 7px,
    color-mix(in oklab, var(--color-fg) 6%, transparent) 7px,
    color-mix(in oklab, var(--color-fg) 6%, transparent) 8px
  );
  background-attachment: fixed;
}
```

All recipes below respect `prefers-reduced-motion`. Do not add `motion`
for these — they are CSS + a few state classes.

---

## 1. Streaming text

Not a typewriter on the whole paragraph. Streamed tokens are sharp; only
the **in-flight tail** is soft, plus a 2px caret.

```css
@keyframes caret-blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}
.stream-caret {
  display: inline-block;
  width: 2px;
  height: 1.05em;
  margin-left: 1.5px;
  border-radius: 1px;
  background: var(--color-fg);
  vertical-align: text-bottom;
  translate: 0 -0.5px;
  animation: caret-blink 1s step-end infinite;
}
.stream-caret.is-streaming { animation: none; } /* solid while tokens arrive */
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

```tsx
function StreamedAnswer({ text, done }: { text: string; done: boolean }) {
  const words = text.split(/(\s+)/);
  const tail = done ? [] : words.slice(-3);
  const head = done ? words : words.slice(0, -3);
  return (
    <p className="text-pretty text-fg">
      {head.join("")}
      {tail.length > 0 && <span className="stream-tail">{tail.join("")}</span>}
      <span className={done ? "stream-caret" : "stream-caret is-streaming"} />
    </p>
  );
}
```

Inline sources are quiet text links (`text-muted underline-offset-2`), not
chips in the paragraph. Follow-ups sit **under** the answer as secondary
buttons, not in the prose.

---

## 2. Thinking trace

Collapsed by default. Label is elapsed time, not "Thinking...✨". Expand
reveals steps; optional tabs (Steps / Reasoning / Search / Code).

```tsx
<button
  className="flex items-center gap-2 text-[12.5px] font-medium text-muted hover:text-fg"
  onClick={() => setOpen((v) => !v)}
>
  <span className="size-1.5 rounded-full bg-muted" />
  Thought for {seconds}s
</button>
{open && (
  <ol className="mt-2 space-y-1 border-l border-border pl-3 text-[12.5px] text-muted">
    {steps.map((s) => (
      <li key={s}>{s}</li>
    ))}
  </ol>
)}
```

Motion: height via `grid-template-rows: 0fr → 1fr` (interruptible), 180ms
`--ease-out`. No bounce. Keyboard toggle is instant under reduced motion.

While still thinking, use **shimmer-on-the-status-line**, not a spinner:

```css
@keyframes shimmer-text {
  0% { background-position: 150%; }
  100% { background-position: -50%; }
}
.shimmer-line {
  background-image: linear-gradient(
    90deg,
    var(--color-muted) 0%,
    var(--color-fg) 50%,
    var(--color-muted) 100%
  );
  background-size: 220% 100%;
  background-clip: text;
  color: transparent;
  animation: shimmer-text 1.6s linear infinite;
}
@media (prefers-reduced-motion: reduce) {
  .shimmer-line {
    animation: none;
    color: var(--color-muted);
    background: none;
  }
}
```

---

## 3. Pixel-grid loader

Beautiful UI's "Churning 7.9s" — a small matrix of dots with staggered
`pixel-on`, plus elapsed time in tabular nums. Use instead of a page-level
spinner.

```css
@keyframes pixel-on {
  0%, 100% { opacity: 0.15; }
  18%, 42% { opacity: 1; }
  62% { opacity: 0.15; }
}
.pixel {
  width: 4px;
  height: 4px;
  border-radius: 1px;
  background: var(--color-fg);
  animation: pixel-on 1.2s ease-in-out infinite;
}
@media (prefers-reduced-motion: reduce) {
  .pixel { animation: none; opacity: 0.5; }
}
```

```tsx
function PixelLoader({ label, seconds }: { label: string; seconds: number }) {
  return (
    <div className="flex items-center gap-3 text-[12.5px] text-muted">
      <div className="grid grid-cols-4 gap-0.5">
        {Array.from({ length: 16 }, (_, i) => (
          <span key={i} className="pixel" style={{ animationDelay: `${(i % 8) * 70}ms` }} />
        ))}
      </div>
      <span>
        {label} <span className="tabular-nums text-fg">{seconds.toFixed(1)}s</span>
      </span>
    </div>
  );
}
```

---

## 4. Tool chips

Compact rows, not JSON dumps. One chip per tool call: icon, verb + file,
quiet meta (line count, duration, pass/fail).

```tsx
<div className="flex flex-wrap gap-1.5">
  {tools.map((t) => (
    <div
      key={t.id}
      className="flex h-7 items-center gap-1.5 rounded-[6px] bg-surface px-2 text-[12px] text-fg shadow-[0_0_0_1px_var(--color-border)]"
    >
      <Icon className="size-3.5 text-muted" />
      <span className="font-medium">{t.title}</span>
      <span className="text-muted">{t.meta}</span>
    </div>
  ))}
</div>
```

Diff-ish meta uses mono + muted (`+74 −41`, `built in 1.2s`). Status
color only on the small check, never on the whole chip.

Code excerpts belong in a follow-up `<pre>` with `text-[12px] leading-5`,
not inside the chip.

---

## 5. Approval card (human in the loop)

Stacked questions. One question visible. Options are selectable chips,
not a form of radio soup. Footer: quiet Skip + solid Continue. Pagination
`1 / 3` in tabular nums.

```tsx
<section className="rounded-[10px] bg-surface p-4 shadow-[0_0_0_1px_var(--color-border)]">
  <p className="text-[13px] font-medium">{question}</p>
  <div className="mt-3 flex flex-col gap-1.5">
    {options.map((o) => (
      <button
        key={o}
        className="h-9 rounded-[8px] px-3 text-left text-[13px] shadow-[0_0_0_1px_var(--color-border)] hover:bg-surface"
        data-selected={o === selected}
      >
        {o}
      </button>
    ))}
  </div>
  <footer className="mt-4 flex items-center justify-between">
    <span className="tabular-nums text-[12px] text-muted">{index + 1} / {total}</span>
    <div className="flex gap-2">
      <button className="h-8 px-3 text-[12px] text-muted">Skip</button>
      <button className="h-8 rounded-[8px] bg-primary px-3 text-[12px] font-medium text-primary-fg">
        Continue
      </button>
    </div>
  </footer>
</section>
```

Selected option: `shadow-[0_0_0_1px_var(--color-primary)]`, not a fill
wash of the whole row.

---

## 6. Prompt bar / composer

Rounded field, not a giant textarea. `@` sources, `/` command palette,
model picker, send. Height ~44px at rest, grows with input.

```tsx
<form className="flex items-end gap-2 rounded-[10px] bg-surface p-1.5 shadow-[0_0_0_1px_var(--color-border)]">
  <button type="button" className="grid size-9 place-items-center text-muted" aria-label="Attach">
    <Plus className="size-4" />
  </button>
  <textarea
    rows={1}
    placeholder="Message"
    className="min-h-9 flex-1 resize-none bg-transparent py-2 text-[14px] outline-none"
  />
  <button type="submit" className="grid size-9 place-items-center rounded-[8px] bg-primary text-primary-fg" aria-label="Send">
    <ArrowUp className="size-4" />
  </button>
</form>
```

`/` opens a list of commands above the bar (`pop-in` 160ms from 0.95,
origin bottom). Keyboard navigation is **instant** (Emil: never animate
highlight that follows keys).

---

## 7. Task rows

Live agent work. Each row: index or status dot, verb phrase, quiet counts,
right-aligned state (`Running` / `Completed` / `Failed`). Failed uses
restrained red on the label only.

Progress (`68%`, `12/12`) is tabular-nums. Do not pulse the whole row.

---

## 8. Recommendation + context cards

Recommendation: one sentence ask, confidence as a short muted label
("High confidence"), two actions (Accept / Alternatives). No gauge
charts unless the product is actually about that number.

Context: retrieved chunk, character count in muted, source filename as a
quiet link. Stack, don't carousel, unless there are many.

---

## 9. Shared motion used by these primitives

```css
@keyframes fade-up {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes pop-in {
  from { opacity: 0; transform: scale(0.95); }
  to   { opacity: 1; transform: scale(1); }
}
.pressable:enabled:active { scale: 0.94; }
```

- Enter: `fade-up` 180–220ms `cubic-bezier(.23,1,.32,1)`
- Menus from a trigger: `pop-in` 160ms, origin at the trigger
- Press: `scale(0.94)` — Beautiful UI uses 0.94, `design-ui` uses 0.96.
  Pick **one per app** and stick to it (prefer 0.96 for product chrome,
  0.94 only if the whole AI surface is matching Beautiful UI)

Never `transition: all`. Enumerate `opacity, transform, box-shadow,
background-color, color`.

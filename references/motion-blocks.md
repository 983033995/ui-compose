# Distinctive motion blocks

Chrome recipes (menus, modals, tooltips, sliding pills, number pop-in,
icon swap, error shake, skeleton reveal) already live in
`design-ui/references/refined-ui.md` and `animations.md`. Use those
first.

This file is the **extra** blocks reverse-engineered from beUI, Rare UI,
transitions.dev, and Emil's constraints. CSS-first. Add `motion` only if
it is already in `package.json`.

Hard rules (Emil Kowalski):

- If the user will see it many times a day, or it follows the keyboard →
  **no animation**
- UI motion **≤ 300ms**
- Name the purpose or delete the motion
- `prefers-reduced-motion: reduce` on every recipe
- Never `transition: all`; never enter from `scale(0)`

---

## 1. 3D tilt + glare (beUI Tilt Card)

Pointer-tracked perspective on a **rare** marketing/feature card. Do not
put this on every list row, table, or button.

```tsx
function TiltCard({ children }: { children: React.ReactNode }) {
  const ref = useRef<HTMLDivElement>(null);
  function onMove(e: React.PointerEvent) {
    const el = ref.current;
    if (!el) return;
    const r = el.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width;
    const py = (e.clientY - r.top) / r.height;
    el.style.setProperty("--rx", `${(0.5 - py) * 8}deg`);
    el.style.setProperty("--ry", `${(px - 0.5) * 10}deg`);
    el.style.setProperty("--gx", `${px * 100}%`);
    el.style.setProperty("--gy", `${py * 100}%`);
  }
  function onLeave() {
    const el = ref.current;
    if (!el) return;
    el.style.setProperty("--rx", "0deg");
    el.style.setProperty("--ry", "0deg");
  }
  return (
    <div
      ref={ref}
      onPointerMove={onMove}
      onPointerLeave={onLeave}
      className="tilt relative rounded-[14px] bg-surface p-5 shadow-[0_0_0_1px_var(--color-border)]"
    >
      <div
        aria-hidden
        className="pointer-events-none absolute inset-0 rounded-[14px] opacity-0 transition-opacity duration-200 group-hover:opacity-100"
        style={{
          background:
            "radial-gradient(420px circle at var(--gx, 50%) var(--gy, 50%), color-mix(in oklab, var(--color-fg) 18%, transparent), transparent 40%)",
        }}
      />
      {children}
    </div>
  );
}
```

```css
.tilt {
  transform: perspective(900px) rotateX(var(--rx, 0deg)) rotateY(var(--ry, 0deg));
  transform-style: preserve-3d;
  transition: transform 180ms cubic-bezier(0.23, 1, 0.32, 1);
}
@media (prefers-reduced-motion: reduce) {
  .tilt { transform: none; transition: none; }
}
@media (hover: none) {
  .tilt { transform: none; }
}
```

Cap tilt at ~8–10deg. More than that looks like a souvenir shop.

---

## 2. Morphing-height panel (beUI Morphing Modal)

One surface, inner views swap, **height morphs**. Content cross-fades with
a 2px blur. Use for settings that switch panes, checkout steps, "family
app" sheets — not for every dialog.

```css
.morph-panel {
  overflow: hidden;
  transition: height 220ms cubic-bezier(0.23, 1, 0.32, 1);
}
.morph-view {
  transition: opacity 180ms ease, filter 180ms ease;
}
.morph-view.is-exit {
  opacity: 0;
  filter: blur(2px);
  pointer-events: none;
}
@media (prefers-reduced-motion: reduce) {
  .morph-panel, .morph-view { transition: none; filter: none; }
}
```

Measure the incoming view (`offsetHeight`) and set the panel height before
swapping content. Exit 150ms, enter 220ms. Do not animate `padding`.

---

## 3. Toast stack (beUI Animated Toast Stack)

Toasts rise from one corner, stack with a slight scale-down on older
items, swipe to dismiss. Spatial: enter and exit along the **same axis**
(Emil / Sonner) so the swipe gesture matches.

- Newest at the front, `scale(1)`; the one behind `scale(0.96)` + 8px
  translate; third `scale(0.92)`
- Enter: 220ms up + fade; exit: 150ms the same way
- Auto-dismiss ~4.2s (beUI default)
- Status morph (loading → success) is an **icon swap** from `design-ui`,
  not a new card

Do not invent a fourth toast library if `sonner` or a local stack exists.

---

## 4. Grid reveal (Rare UI)

Hero media or a feature panel appears cell-by-cell. One use per page,
on first paint only.

```css
@keyframes grid-cell {
  from { opacity: 0; transform: scale(0.96); }
  to   { opacity: 1; transform: scale(1); }
}
.grid-reveal > * {
  animation: grid-cell 320ms cubic-bezier(0.23, 1, 0.32, 1) both;
}
.grid-reveal > *:nth-child(1) { animation-delay: 0ms; }
.grid-reveal > *:nth-child(2) { animation-delay: 40ms; }
.grid-reveal > *:nth-child(3) { animation-delay: 80ms; }
/* stagger 40ms; cap at ~12 cells */
@media (prefers-reduced-motion: reduce) {
  .grid-reveal > * { animation: none; }
}
```

---

## 5. Fluid orb (Rare UI, ambient only)

WebGL orb with drifting color patches — ChatGPT-voice energy. Use as a
**listening / generating** mark in an agent product, 48–80px, one on
screen. Do not use as a hero background.

If WebGL is too heavy for the app, fake the ambient with the pixel-grid
loader from `ai-primitives.md` instead.

---

## 6. Streaming + thinking (transitions.dev verbs)

Already specified in `ai-primitives.md`:

| Verb | Recipe |
| --- | --- |
| Tokens arriving | stream-tail blur + solid caret |
| Idle after stream | blinking 2px caret |
| Model is thinking | shimmer-line on the status, then swap to "Thought for Ns" |
| Skeleton → content | cross-fade 400ms, optional 2px blur (design-ui) |

Do not also bounce, sparkle, or gradient-wash the text.

---

## 7. When to ship zero motion

Copy this test before adding a recipe:

| Interaction | Motion? |
| --- | --- |
| Command palette open from keyboard | No |
| Highlight moving with arrow keys | No (instant background) |
| App / overlay open that happens dozens of times a day | No |
| Hover on a nav item used all session | Color/opacity only, 0–80ms or none |
| Primary button press | Optional `scale(0.96)`, 150ms |
| Modal / sheet the user opens a few times a session | Yes, design-ui modal/panel |
| First-run hero, rare success, first thinking reveal | Yes, once |
| Streaming tokens | Yes, the tail/caret only |

A faster spinner (or no spinner — just the pixel grid + elapsed time)
improves *perceived* speed more than a 400ms flourish.

---

## 8. Origin-aware surfaces (beUI + design-ui)

Dropdowns and morphing menus scale from the **trigger**, not the viewport
center. Centered dialogs stay center-origin at `--motion-scale-modal`
(~0.96). Close is faster than open.

If you find yourself animating the outer page wrapper so a badge can pop,
you picked the wrong node — animate the badge.

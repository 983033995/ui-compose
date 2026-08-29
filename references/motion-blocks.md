# Distinctive motion blocks

Use these recipes only after Host Read confirms they fit the product and stack. They are **traits to translate**, not React/Tailwind defaults.

Hard rules:

- If the user will see it many times a day, or it follows the keyboard → **no animation**
- Do not animate product icons on navigation, tables, or repeating chrome
- UI motion is generally **≤ 300ms**
- Name the purpose or delete the motion
- provide `prefers-reduced-motion: reduce`
- never `transition: all`; never enter ordinary UI from `scale(0)`

---

## 1. 3D tilt + glare

Pointer-tracked perspective on a rare marketing/feature card. Do not use on every list row, table, or button.

Framework-neutral behavior:

1. read pointer position inside the card;
2. set CSS custom properties `--rx`, `--ry`, `--gx`, `--gy`;
3. reset rotation on pointer leave;
4. disable transform on reduced motion and coarse/no-hover pointers.

```css
.tilt {
  position: relative;
  transform: perspective(900px) rotateX(var(--rx, 0deg)) rotateY(var(--ry, 0deg));
  transform-style: preserve-3d;
  transition: transform 180ms cubic-bezier(0.23, 1, 0.32, 1);
}

.tilt::after {
  content: "";
  pointer-events: none;
  position: absolute;
  inset: 0;
  border-radius: inherit;
  opacity: 0;
  transition: opacity 180ms ease;
  background: radial-gradient(
    420px circle at var(--gx, 50%) var(--gy, 50%),
    color-mix(in oklab, currentColor 18%, transparent),
    transparent 40%
  );
}

.tilt:hover::after { opacity: 1; }

@media (prefers-reduced-motion: reduce), (hover: none) {
  .tilt { transform: none; transition: none; }
  .tilt::after { display: none; }
}
```

This replaces the previous example's broken `group-hover` relationship and avoids binding the recipe to React/Tailwind.

Cap tilt at ~8–10deg.

---

## 2. Morphing-height panel

One surface, inner views swap, and the container height morphs. Useful for infrequent settings/checkout/sheet flows.

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

Measure the incoming content height using the host framework's normal lifecycle tools. Do not animate padding.

---

## 3. Toast stack

If the host already has a toast system, keep it. Improve only stack physics/visual hierarchy if necessary.

Suggested behavior:

- newest at scale 1
- older items recede slightly
- enter ~220ms; exit ~150ms along the same axis
- swipe direction should match exit direction
- loading → success should morph status inside the same toast rather than create a new toast

Do not install a fourth toast library for this effect.

---

## 4. Grid reveal

Hero media or a feature panel appears cell-by-cell. One use per page, first paint only.

```css
@keyframes grid-cell {
  from { opacity: 0; transform: scale(0.96); }
  to   { opacity: 1; transform: scale(1); }
}
.grid-reveal > * {
  animation: grid-cell 320ms cubic-bezier(0.23, 1, 0.32, 1) both;
}
@media (prefers-reduced-motion: reduce) {
  .grid-reveal > * { animation: none; }
}
```

Stagger lightly and cap the number of animated cells.

---

## 5. Ambient orb

A small animated mark can communicate listening/generating state. Keep it small and singular. Prefer CSS/canvas/WebGL only when the product meaning justifies the cost.

Do not use it as a generic full-page AI background.

---

## 6. Streaming / agent activity

For AI surfaces:

| State | Motion treatment |
| --- | --- |
| tokens arriving | stream-tail / caret only |
| running activity | subtle status-line animation |
| tool state change | compact icon/status transition |
| skeleton → content | short cross-fade, optional tiny blur |

Do not imply hidden chain-of-thought. Animate only provider-exposed activity/progress or summarized reasoning.

---

## 7. When to ship zero motion

| Interaction | Motion? |
| --- | --- |
| Command palette from keyboard | No |
| Arrow-key highlight | No |
| Frequently used app overlay | Usually no |
| Nav hover | Color/opacity only or none |
| Primary button press | Optional subtle press |
| Rare modal/sheet | Yes, restrained |
| First-run hero / rare success | Yes, once |
| Streaming tokens | Tail/caret only |

---

## 8. Origin-aware surfaces

Menus/dropdowns should appear from their trigger/spatial origin. Centered dialogs stay center-origin. Exit is usually quicker than enter.

Animate the smallest node that communicates the state change; do not move the entire page just to make a badge or icon feel alive.

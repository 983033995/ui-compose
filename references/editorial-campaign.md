# Editorial campaign register (SOLESHIFT° / SWIRL°)

Source: Shams (@ShamsAmin56) Hailuo H3 prototypes —

- Footwear: [SOLESHIFT°](https://x.com/ShamsAmin56/status/2092902214683832340)
- Ice cream: [SWIRL°](https://x.com/ShamsAmin56/status/2092188350476337613)

These are **motion-graphics campaign landings**, not product chrome.
They look "designed" because the **structure is locked** and only the
**SKU world** (palette, motif, headline, transition personality)
swaps on hover. That is still Lego — a skeleton plus per-item skins.

Use this register for: DTC / lookbook / flavor or colorway explorers,
fashion, food, toys, anything sold as a *character*.

Do **not** use for: dashboards, settings, chat, CRUD, docs. There the
anti-slop bans still win (no blobs, no bounce-on-everything, no
carnival type).

---

## What makes it distinctive

Not "colorful sneakers on a cream background." The system:

1. **One locked chrome.** Logo + nav + bag count + six SKU cards never
   move. Camera is front-facing, almost locked. No orbit, no zoom.
2. **The SKU owns the world.** Hovering a card swaps hero product,
   giant title, 3-word staccato subline, background palette, *and* the
   motif family. Interaction always reads:
   `cursor → card reacts → hero appears → headline changes → world transforms`.
3. **Y2K × editorial, not videogame and not glassmorphism.** Warm cream
   paper, chunky rounded display type, numbered chips, organic blobs /
   checkers / squiggles / halftone as *controlled* decoration.
4. **Visual hierarchy is the whole tip** (author's words). Order:
   hero product (65–70% of the stage) → giant name → subline → CTA →
   SKU rail → nav. Decor stays off the UI.
5. **Each SKU gets a different transition personality**, still one
   design system. Cloud pops elastic; pixel *assembles*; chrome *orbits*;
   toxic *overshoots*. Same tracks, different verbs.

---

## Skeleton (steal the tracks)

```
┌─────────────────────────────────────────────────────┐
│  MARK°          COLLECTION  ABOUT  SHOP      BAG 00 │
│                                                     │
│   GIANT NAME          ╔══════════════╗              │
│   THREE. WORD. LINE.  ║  HERO ~70%   ║   [ 06 ]     │
│   CTA →               ║   product    ║   cropped    │
│                       ╚══════════════╝   numeral    │
│                                                     │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐         │
│  │ 01 │ │ 02 │ │ 03 │ │ 04 │ │ 05 │ │ 06 │         │
│  └────┘ └────┘ └────┘ └────┘ └────┘ └────┘         │
└─────────────────────────────────────────────────────┘
```

```tsx
<div className="campaign relative min-h-dvh overflow-hidden bg-[var(--sku-paper)] text-[var(--sku-ink)]">
  <header className="relative z-20 flex h-14 items-center justify-between px-5">
    <span className="text-sm font-semibold tracking-wide">SOLESHIFT°</span>
    <nav className="hidden gap-6 text-[11px] font-medium tracking-[0.18em] md:flex">
      <a href="#collection">COLLECTION</a>
      <a href="#about">ABOUT</a>
      <a href="#shop">SHOP</a>
    </nav>
    <span className="text-[11px] tracking-[0.18em]">BAG 00</span>
  </header>

  <main className="relative z-10 grid min-h-[calc(100dvh-3.5rem-7.5rem)] items-center gap-6 px-5 lg:grid-cols-[minmax(0,0.9fr)_minmax(0,1.2fr)]">
    <div>
      <p className="campaign-display text-5xl font-black leading-[0.9] tracking-tight md:text-7xl">
        {sku.name}
      </p>
      <p className="mt-3 text-sm font-semibold tracking-[0.22em] text-[var(--sku-ink-2)]">
        {sku.subline}
      </p>
      <a className="mt-6 inline-flex items-center gap-2 text-sm font-semibold" href="#shop">
        {sku.cta} <span aria-hidden>→</span>
      </a>
    </div>
    <div className="relative grid place-items-center">
      <span className="pointer-events-none absolute -right-6 select-none text-[28vw] font-black leading-none text-[var(--sku-accent)] opacity-30">
        {sku.index}
      </span>
      <img src={sku.hero} alt={sku.name} className="relative z-10 w-[70%] max-w-xl object-contain" />
    </div>
  </main>

  <ul className="relative z-20 grid grid-cols-3 gap-2 px-5 pb-6 md:grid-cols-6">
    {skus.map((s) => (
      <li key={s.id}>{/* card */}</li>
    ))}
  </ul>
</div>
```

Logo always has the degree mark (`°`). Nav is tracked small caps. Bag
is a count, not an icon soup. Hero product is a **cutout**, not in a
device mock.

---

## Tokens (cream paper + SKU worlds)

Base is warm paper, not pure white and not dark-first.

```css
.campaign {
  --sku-paper: #f6efe4;
  --sku-ink: #161412;
  --sku-ink-2: color-mix(in oklab, var(--sku-ink) 55%, var(--sku-paper));
  --sku-line: color-mix(in oklab, var(--sku-ink) 12%, var(--sku-paper));
  --radius-chip: 8px;
  --radius-card: 18px;
  --radius-stage: 28px;
  --font-display: "Fredoka", "Cooper Black", ui-rounded, system-ui, sans-serif;
  --font-meta: ui-sans-serif, system-ui, sans-serif;
}
.campaign-display {
  font-family: var(--font-display);
  font-weight: 800;
  text-wrap: balance;
  letter-spacing: -0.04em;
}
```

Each SKU is a **world**, not a hex on a button. Pair a paper stain, a
hard accent, and a motif family. From the SOLESHIFT lineup:

| SKU | Paper stain | Accent | Motif family | Transition verb |
| --- | --- | --- | --- | --- |
| 01 Cloud Pop | cream + lavender | pastel pink | glossy bubbles, stars, halftone | elastic scale-up |
| 02 Blaze Wave | cream + orange | electric blue | liquid ribbons, speed lines, warped checkers | graphic wipe |
| 03 Pixel Stack | cream + cyan | yellow / black | pixel squares, stepped grid, modular blocks | assemble from blocks |
| 04 Chrome Orbit | silver-cream | acid lime + purple | orbital rings, chrome spheres, looping paths | curved orbital sweep |
| 05 Blush Puffer | blush + burgundy | pink | inflated blobs, stitch lines, soft spheres | circular wipe + cushion |
| 06 Toxic X-Ray | cream + turquoise | toxic lime | grid floor, lime waves, purple squiggles | overshoot pop |

Ice-cream SWIRL° uses the same machine (Noir charcoal spirals, Matcha
ribbons, Sakura inflated type, etc.). Copy the *machine*, not the
flavors.

Implement as data, then paint with CSS variables:

```ts
type SkuWorld = {
  id: string;
  index: string; // "01"
  name: string;
  subline: string; // "SOFT. BOLD. DREAMY."
  cta: string;     // "STEP INTO FUN →"
  paper: string;
  accent: string;
  motif: "bubbles" | "waves" | "pixels" | "orbit" | "plush" | "xray";
  verb: "elastic" | "wipe" | "assemble" | "orbit" | "cushion" | "overshoot";
};
```

On activate:

```css
.campaign {
  --sku-paper: v-bind(sku.paper);
  --sku-accent: v-bind(sku.accent);
  transition: background-color 280ms cubic-bezier(0.22, 1, 0.36, 1);
}
```

---

## Type

- **Display:** chunky, rounded, slightly tight tracking. Cooper Black /
  Fredoka / "inflated bubble" energy. Product names are enormous and
  may tuck *behind* the hero for depth, but must stay readable.
- **Subline:** three words, periods, tracked. `SOFT. BOLD. DREAMY.`
  Never a sentence.
- **Meta / nav:** clean geometric sans, 11–12px, wide tracking
  (`0.18–0.22em`), weight 500–600. Never the display face.
- **Numbers:** tabular, padded (`01` not `1`). The giant cropped index
  behind the hero is a graphic, not a heading.

Hide outgoing type with a mask *before* revealing the next word so
interpolated garbage letters never show (the H3 prompt's accuracy rule
— same rule for FLIP / view-transition text swaps).

---

## SKU rail (the actual control)

Cards are the only playful control. Nav does not bounce.

```tsx
<button
  onMouseEnter={() => setSku(s.id)}
  onFocus={() => setSku(s.id)}
  className="sku-card group relative rounded-[18px] bg-[var(--sku-paper)] p-2 text-left shadow-[0_0_0_1px_var(--sku-line)]"
  data-active={s.id === sku.id}
>
  <img src={s.thumb} alt="" className="aspect-square w-full object-contain" />
  <span className="mt-1 flex items-center gap-1.5 text-[11px] font-semibold">
    <span className="grid size-5 place-items-center rounded-[6px] bg-[var(--sku-accent)] text-[10px] text-[var(--sku-paper)]">
      {s.index}
    </span>
    {s.name}
  </span>
</button>
```

```css
.sku-card {
  transition: transform 220ms cubic-bezier(0.34, 1.4, 0.64, 1),
              box-shadow 180ms ease;
}
.sku-card:hover,
.sku-card[data-active="true"] {
  transform: translateY(-6px) scale(1.04);
  box-shadow: 0 0 0 2px var(--sku-accent), 0 12px 24px color-mix(in oklab, var(--sku-ink) 12%, transparent);
}
@media (prefers-reduced-motion: reduce) {
  .sku-card { transition: box-shadow 120ms ease; }
  .sku-card:hover, .sku-card[data-active="true"] { transform: none; }
}
```

Scale cap **1.04**. Author specified ~104%. More than 1.08 looks toyish.
Keyboard focus must do the same swap as hover (not hover-only).

---

## Motion (campaign exception to the 300ms rule)

App chrome still follows Emil: nav, bag, keyboard highlight = **instant**.
The **hero world swap** is the show. Budget:

| Beat | Duration | Ease |
| --- | --- | --- |
| Card lift | 180–220ms | spring / `cubic-bezier(0.34, 1.4, 0.64, 1)` |
| Hero enter (elastic / overshoot) | 420–560ms | spring, bounce ≤ 0.35 |
| Graphic wipe / assemble | 280–400ms | masked shapes, not opacity-only |
| Background stain | 280ms | `--ease-out` |
| Outgoing type | 120ms masked | hide before incoming |
| Incoming type | 220ms | slight squash-stretch, then settle |
| Final hold micro-motion | loop, tiny | motif drift only, 4–8px |

Verbs (pick per SKU, one each):

| Verb | How |
| --- | --- |
| elastic | `scale(0.92 → 1.06 → 1)` + 8px rise |
| wipe | colored shape layer `clip-path` or `inset()` across the stage |
| assemble | hero grid of 12–20 squares staggered 30ms (Rare UI grid-reveal) |
| orbit | enter along a 40–80px arc (`offset-path`) |
| cushion | circular clip expand, slower settle |
| overshoot | `scale(0.8 → 1.08 → 1)` + accent outline flash |

Keep the page **camera-locked**. Tilt the hero toward the cursor at most
4deg (see `motion-blocks.md` tilt, then *halve* it). No cinematic dolly.

Reduced motion: hard-cut the SKU world (palette + image + type), skip
wipes/bounce/wiggle. The hierarchy still has to work as a still.

---

## Motifs (SVG, not photos)

Decor is 2D graphic, sitting *behind* the product. Families:

- bubbles / spheres (radial gradients, 3–7 circles)
- ribbons / waves (`path` stroke, 4–6px)
- pixel / checker (`repeating-conic-gradient` or a 8px grid)
- orbital rings (stroke circles, dashed)
- blobs (`border-radius: 60% 40% 70% 30%` + slow rotate)
- halftone (`radial-gradient` dots, 6–10px)
- stars / squiggles (inline SVG, `currentColor` = `--sku-accent`)

Cap: **one family per SKU**, 4–8 shapes on stage. Do not stack
checker + blobs + stars + halftone + ribbons at once — that is the
Magic UI slop pile, just louder.

---

## Hard rules (so this doesn't become carnival slop)

- Locked chrome. If the header jumps, you broke the system.
- Six (or a small odd/even set) SKUs, not an infinite carousel.
- Product cutouts are immutable assets. Never morph shoe A into shoe B.
- One display face + one meta face. No third "fun" font.
- Color is per-SKU, but the **paper** stays cream-family. Don't jump to
  a black full-bleed unless the SKU world is explicitly noir.
- Bounce lives on the **SKU card and hero only**. Nav, bag, links: no.
- Hierarchy test: squint. You should still read Name → Product → Rail.
- This register is opt-in. Default landings still use the quiet
  marketing skeleton in `layout-steal.md`.

---

## Agent move

When the user asks for a playful product explorer / Y2K campaign /
"like that shoe site":

1. Steal this skeleton, not a generic 3-up landing.
2. Encode SKUs as data (`SkuWorld`).
3. Implement hover/focus → world swap before any blob SVG.
4. One transition verb per SKU, from the table.
5. Pair with `motion-blocks.md` for tilt / grid-reveal if needed.
6. Keep `design-ui` tokens for checkout, cart, account — those stay
   the quiet app-interior register. Do not carry bounce into the bag.

# Editorial campaign register

This register captures the composition logic behind expressive DTC/lookbook/product-explorer experiences. It is **not** a template for dashboards, settings, CRUD, chat, or ordinary app chrome.

The useful idea is not a specific brand or color palette. It is a **locked composition with item-owned visual worlds**.

Use for: fashion, food, toys, colorways, flavors, collectible/product campaigns.

Do not use for: dense app interiors, admin UI, settings, documentation, generic SaaS dashboards.

---

## What makes the pattern work

1. **Locked chrome.** Brand/nav/cart/rail positions remain stable.
2. **The selected item owns the world.** Activation changes hero, display copy, palette, motif family, and transition personality as one coordinated state change.
3. **Editorial hierarchy.** Hero product first, display name second, supporting line/CTA third, selector rail fourth.
4. **Controlled motifs.** One motif family per item world instead of effect stacking.
5. **Different transition verbs, one system.** Each item may enter differently, but layout tracks and interaction rules stay fixed.

Interaction reads:

`pointer/tap/focus → selector reacts → hero changes → copy changes → world changes`

---

## Skeleton

```text
┌─────────────────────────────────────────────────────┐
│  MARK           COLLECTION  ABOUT  SHOP       CART  │
│                                                     │
│   GIANT NAME          ╔══════════════╗              │
│   SHORT SUBLINE       ║  HERO ~70%   ║   BIG INDEX  │
│   CTA →               ║   product    ║              │
│                       ╚══════════════╝              │
│                                                     │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐         │
│  │ 01 │ │ 02 │ │ 03 │ │ 04 │ │ 05 │ │ 06 │         │
│  └────┘ └────┘ └────┘ └────┘ └────┘ └────┘         │
└─────────────────────────────────────────────────────┘
```

Translate this into the host framework. Do not copy the exact brand mark, naming, typography, or product art from a reference.

---

## World model

Keep the item-specific world in data:

```ts
type ProductWorld = {
  id: string;
  index: string;
  name: string;
  subline: string;
  cta: string;
  paper: string;
  ink: string;
  accent: string;
  motif: "bubbles" | "waves" | "pixels" | "orbit" | "plush" | "xray";
  verb: "elastic" | "wipe" | "assemble" | "orbit" | "cushion" | "overshoot";
};
```

On activation, map world values to host state and CSS custom properties. This is framework neutral:

```css
.campaign {
  background: var(--world-paper);
  color: var(--world-ink);
  transition: background-color 280ms cubic-bezier(0.22, 1, 0.36, 1),
              color 180ms ease;
}
```

Then set `--world-paper`, `--world-ink`, and `--world-accent` from the framework's normal state/style binding mechanism. Do not use Vue-only `v-bind()` inside React examples or React-only JSX as the canonical recipe.

---

## Activation model

The selector must work for mouse, keyboard, and touch.

Minimum behavior:

- pointer hover may preview on devices that support hover;
- keyboard focus/select must be fully operable;
- tap/click must activate the item on touch devices;
- active state must persist independently of hover;
- reduced motion must preserve all information as a still state.

Pseudo-behavior:

```text
on hover (hover-capable): preview(item)
on focus: preview(item)
on click/tap: activate(item)
on Enter/Space: activate(item)
```

Do not make a campaign selector hover-only.

---

## Typography

Use the host project's licensed/available type system.

- Display: expressive, large, tight tracking, but readable.
- Supporting line: short and rhythmic; avoid generic filler copy.
- Meta/nav: restrained geometric/system sans.
- Numbers: tabular/padded when used as visual indices.

One display face + one meta face is enough.

---

## Motion budget

The hero world swap is the expressive moment. App-like controls remain calm.

| Beat | Typical duration | Notes |
| --- | ---: | --- |
| selector lift | 180–220ms | subtle spring or ease-out |
| hero enter | 420–560ms | only for rare expressive campaigns |
| graphic wipe/assemble | 280–400ms | spatial transition, not random opacity |
| background palette | ~280ms | coordinated with hero |
| outgoing type | ~120ms | hide cleanly |
| incoming type | ~220ms | restrained settle |

Possible verbs:

- elastic — small overshoot then settle
- wipe — colored shape/mask crosses stage
- assemble — staggered grid pieces resolve into hero
- orbit — curved spatial entry
- cushion — circular reveal with soft settle
- overshoot — stronger scale/rise, used sparingly

Reduced motion: hard-cut world state; no bounce/wipe/orbit.

---

## Motif families

Choose one family per world:

- bubbles/spheres
- ribbons/waves
- pixel/checker
- orbital rings
- soft blobs
- halftone
- stars/squiggles

Cap decoration. The motif supports the product; it does not become a sampler of every trendy effect library.

---

## Hard rules

- locked chrome; avoid layout jumps between items;
- product/media assets remain discrete; do not fake morphing one SKU into another;
- selector + hero may be playful; navigation and cart controls remain restrained;
- one display face + one meta face;
- active state works with click/tap, not hover only;
- hierarchy must still work without animation;
- this register is opt-in, not the default landing-page style;
- learn the interaction machine, not the source brand identity.

---

## Agent move

When a user asks for a playful product explorer or editorial campaign:

1. choose this skeleton before effects;
2. encode product worlds as data;
3. implement accessible activation for hover/focus/click/tap;
4. coordinate hero, copy, palette, and motif as one state;
5. choose at most one transition verb per world;
6. keep checkout/account/cart application surfaces in the host's normal product register.

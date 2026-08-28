# Steal the skeleton first

Models place boxes randomly when the canvas is blank. They are competent at
swapping copy, tokens, and small controls *inside* a real structure.

Do layout before color. Do structure before motion.

## Method

1. Pick the **page type** (marketing, app shell, settings, chat, dashboard,
   empty state, pricing, article).
2. Copy a real skeleton — from shadcn blocks, ReUI, or the recipes below —
   including max-width, grid tracks, padding, and which piece is sticky.
3. Delete their colors, fonts, and decorative blobs. Keep the **tracks**.
4. Map every color/radius/shadow to this app's `@theme` tokens.
5. Fill with real content. Empty cells get a designed empty state, not a
   gray rectangle.

If you cannot name which skeleton you stole, you invented one — that's how
slop starts.

## Registers (do not mix)

From swagui: one token set, two densities.

| Register | Base type | Gaps | Radius | Use |
| --- | --- | --- | --- | --- |
| **Marketing** | 16–18px body, display headings `clamp` | `--space-6`–`--space-8` | larger (`--radius-xl` cards) | Landing, pricing, blog |
| **App interior** | 13–14px body, 12px meta | `--space-2`–`--space-4` | tighter (`--radius-control` / `--radius-card`) | Dashboards, chat, settings, CRUD |
| **Editorial campaign** | chunky display + 11px tracked meta | generous stage, tight rail | cards 18 / stage 28 | DTC lookbooks only — `editorial-campaign.md` |
| **3D / WebGL moment** | same as the host register | canvas fills the stage, HTML overlays | n/a (scene, not chrome) | One Community ThreeUI item — `threeui.md` |

Beautiful UI itself runs at `font-size: 14px` on the document with
`letter-spacing: -0.01em` — that's the app-interior register.

## Canonical skeletons (Tailwind v4)

Use these as starting markup. Swap tokens, not the tracks.

### Product shell — docs / settings / tool

Stolen from Beautiful UI's own chrome: `max-w-[960px]`, hairline frame,
sticky 288px aside, dashed separators.

```tsx
<div className="mx-auto max-w-[960px] bg-bg shadow-[0_0_0_1px_var(--color-border)]">
  <div className="lg:grid lg:grid-cols-[288px_minmax(0,1fr)]">
    <aside className="border-b border-dashed border-border px-5 py-8 lg:sticky lg:top-0 lg:h-dvh lg:overflow-y-auto lg:border-r lg:border-b-0">
      {/* brand + nav */}
    </aside>
    <main className="min-w-0 px-5 py-10 sm:px-8">{/* pages */}</main>
  </div>
</div>
```

### App shell — list + detail

```tsx
<div className="grid h-dvh grid-rows-[auto_1fr] bg-bg">
  <header className="flex h-12 items-center gap-3 border-b border-border px-3">
    {/* mark + title + primary action */}
  </header>
  <div className="grid min-h-0 md:grid-cols-[minmax(240px,320px)_1fr]">
    <section className="min-h-0 overflow-y-auto border-b border-border md:border-r md:border-b-0">
      {/* list rows */}
    </section>
    <section className="min-h-0 overflow-y-auto p-5">{/* detail */}</section>
  </div>
</div>
```

### Marketing landing

```tsx
<div className="bg-bg text-fg">
  <header className="mx-auto flex h-14 max-w-6xl items-center justify-between px-4">
    {/* mark + nav + CTA */}
  </header>
  <section className="mx-auto max-w-6xl px-4 py-20 md:py-28">
    <p className="text-sm text-muted">{/* eyebrow */}</p>
    <h1 className="mt-3 max-w-3xl text-balance text-4xl font-semibold tracking-tight md:text-6xl">
      {/* one sentence */}
    </h1>
    <p className="mt-5 max-w-xl text-pretty text-muted">{/* support */}</p>
    <div className="mt-8 flex flex-wrap gap-3">{/* primary + secondary */}</div>
  </section>
  <section className="mx-auto grid max-w-6xl gap-4 px-4 pb-24 sm:grid-cols-2 lg:grid-cols-3">
    {/* 3-up feature cards — same inner template */}
  </section>
</div>
```

Do not add a gradient blob behind the hero. Do not center-align long body
copy. One primary CTA.

### Dashboard

```tsx
<div className="grid h-dvh grid-cols-[auto_1fr] bg-bg">
  <nav className="w-14 border-r border-border md:w-52">{/* icons + labels */}</nav>
  <div className="grid min-h-0 grid-rows-[auto_1fr]">
    <header className="flex h-12 items-center justify-between border-b border-border px-4">
      {/* crumbs + search + user */}
    </header>
    <main className="min-h-0 overflow-y-auto p-4 md:p-6">
      <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">{/* KPI cards */}</div>
      <div className="mt-4 grid gap-4 xl:grid-cols-[minmax(0,2fr)_minmax(280px,1fr)]">
        {/* chart */}
        {/* side list */}
      </div>
    </main>
  </div>
</div>
```

KPI cards share one inner template (label, tabular number, muted delta).
Do not invent four different card layouts.

### Chat / agent

```tsx
<div className="mx-auto grid h-dvh max-w-3xl grid-rows-[auto_1fr_auto] bg-bg">
  <header className="flex h-12 items-center justify-between border-b border-border px-4">
    {/* thread title + model */}
  </header>
  <div className="min-h-0 overflow-y-auto px-4 py-6">{/* messages + tools */}</div>
  <div className="border-t border-border p-3">{/* prompt bar */}</div>
</div>
```

Composer stays at the bottom, messages scroll, thinking/tool chips sit in
the message column — see `ai-primitives.md`.

## Spacing and width (refuse hallucination)

If a value is not on the scale, it does not ship.

| Role | Token |
| --- | --- |
| Control height | 32px compact / 40–44px comfortable |
| Page gutter | `--space-4` (16) mobile, `--space-6` (24) desktop |
| Card padding | `--space-4` or `--space-5` |
| Stack between sections | `--space-6` app / `--space-8` marketing |
| Reading measure | 60–75ch |
| Product max | 960–1080px |
| Marketing max | 1120–1200px (`max-w-6xl`) |

Ban `p-[13px]`, `gap-[17px]`, `max-w-[847px]`. If you need a new step, add
it to `@theme` once.

## Hairline frame (Beautiful UI / swagui)

Prefer a 1px tokenized ring over a fat border or drop shadow:

```css
.shell {
  box-shadow: 0 0 0 1px var(--color-border);
}
```

Dark mode: the same ring, just a lighter `--color-border`. Do not add a
second ambient shadow on every card.

Dashed separators (`border-dashed border-border`) are a legitimate quiet
divider on editorial/product-docs shells. Do not use them on dense data
tables.

## Extraction prompt (when you do have a screenshot or URL)

If the user points at a site they like:

1. Extract **structure** (tracks, widths, sticky bits, density register)
2. Extract **tokens** (surfaces, ink steps, one accent, radii, type)
3. Write them into `src/styles.css` `@theme`
4. Rebuild with *our* components on that skeleton

Do not clone brand assets, illustrations, or copy. Steal the system, not
the identity.

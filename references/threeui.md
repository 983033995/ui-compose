# ThreeUI — 3D / WebGL Lego

Sources:

- Site: [threeui.com](https://threeui.com)
- Community (MIT, 160+): [github.com/MengTo/threeui](https://github.com/MengTo/threeui)
- npm: `@designcodeio/threeui`
- Meng To: [open-source announcement](https://x.com/MengTo/status/2090817187900780961)

This is the **3D register** of the same Lego idea. Do not invent a
WebGL hero, particle field, liquid-metal button, or kinetic type from a
blank canvas. Steal a ThreeUI block, then retune palette / lighting /
copy. That is the whole skill, applied to GPU.

Florin on the launch post: *this solves one of the harder parts of
agent-built UI: starting with good taste.* Josh: *hand it over, change
the theme and motion, never touch the procedural JS.*

Use when the user asked for a **real 3D moment** (hero scene, shader
background, 3D product stage, WebGL button). Skip for dashboards,
settings, chat, CRUD. Those stay CSS + shadcn.

---

## What it actually is

Not a second shadcn. A **catalog of copy-ready procedural scenes**:

| Layer | Count (Community, Aug 2026) |
| --- | --- |
| Parent components | 50 |
| Routes | 111 |
| Free variants + singletons | 164 browse results |
| Typical scene | 100–200 KB, procedural JS, no glTF required |

Pro adds 50+ extra, MCP, and per-item skills/prompts. Community is
enough for the method. Do not scrape Pro source.

Categories (steal by job, not by "it looks cool"):

| Job | Category | Community starting points |
| --- | --- | --- |
| Opening hero (scene + HTML chrome) | Hero | Sylva — Living Green, Complete Shelf, Bestsellers Book |
| Full marketing page | Landing Pages | Sketchbook, Kage |
| Atmosphere behind HTML | Backgrounds | Predictive Arc, CRT, Liquid Form, Constellation Field, Portal Field, Warp Field |
| Reusable 3D object | Three.js | Structure Flow, Landscape, Bookshelf, Woven Cloth, Temple Night |
| One fancy control | Buttons | Liquid Metal, Circle/Rectangle, Shader, Thinking, Launch, Tactile |
| Kinetic type | Text Animation | Text Path Studies, Gallery Heading, Semantic Bloom, Typography Vortex |
| Chrome flourish | UI Elements | Brand Orbs, Character Carousel, Diagnostics Panel, Animated Top Dock |
| CSS-only cousin | CSS / Motion Design | Use only if WebGL is overkill |

A **background** is the visual layer. A **hero** is that layer plus
nav, copy, CTA. Do not drop a full landing template into an app shell.

---

## Agent workflow (do this, in order)

1. **Name the job** in one sentence: "shader field behind a quiet hero"
   or "one liquid-metal generate button". If you cannot name it, you do
   not need ThreeUI.
2. **Pick one Community item** from the table. Open
   [threeui.com/browse](https://threeui.com/browse) or the GitHub
   `src/shaders/` / `src/package-components/` tree. Prefer an item whose
   *interaction* matches, not just the thumbnail.
3. **Copy source, don't rewrite GLSL.** Install
   `@designcodeio/threeui` **or** paste the component folder. Subpath
   import to keep the graph small:

   ```tsx
   import { AtTheHorizon } from "@designcodeio/threeui/components/AtTheHorizon";
   import "@designcodeio/threeui/style.css";
   ```

   Full-document scenes need their runtime files at the same
   root-relative URLs. Copy from
   `node_modules/@designcodeio/threeui/lib-dist/assets/` into `public/`,
   or pass `sourceUrl` / `assetBaseUrl`.
4. **Retune, don't restyle from zero.** Change copy, CSS variables /
   palette, lights, camera distance, particle count. Keep the
   interaction (cursor field, dock magnification, CRT scan). Meng To's
   promise: *skills your agent can use to customize them while keeping
   them looking amazing.*
5. **Seat it behind real HTML.** Canvas is a layer. Links, type, and
   CTAs stay DOM. See the mount recipe below.
6. **Cap: one GPU scene per view.** Do not stack Predictive Arc +
   Liquid Metal + Typography Vortex + Magic UI particles.

If the user has ThreeUI Pro, the MCP at `https://threeui.com/api/mcp`
is the catalog API: `search_catalog` → `get_item_prompt` →
`get_item_source`. Still one item. MCP does not license carnival.

---

## Mount recipe (every scene)

Reverse-engineered from `src/shaders/community.css`. Every Community
mount shares this shell. Copy it; do not invent a new one.

```css
.threeui-mount {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  width: 100%;
  min-height: 100%;
  background: var(--scene-paper, #030304);
}
.threeui-mount > canvas,
.threeui-mount iframe {
  position: absolute;
  inset: 0;
  display: block;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 180ms ease-out;
  pointer-events: none; /* HTML on top stays clickable */
}
.threeui-mount > canvas.is-ready,
.threeui-mount iframe.is-ready {
  opacity: 1;
}
.threeui-mount .chrome {
  position: relative;
  z-index: 2;
}
@media (prefers-reduced-motion: reduce) {
  .threeui-mount > canvas { transition: none; }
}
```

Paper tones from the catalog (pick the one that matches the scene,
then map onto `@theme`):

| Scene family | Paper |
| --- | --- |
| Dark fields (CRT, vortex, temple, predictive-arc default) | `#030304` / `#05070a` / `#08090a` |
| Light fields (predictive-arc light, type vortex light) | `#f3f5f8` / `#f3f6f1` / `#eef1f6` |
| Warm analog (landscape, Japanese tower, sketchbook) | `#ecdcbc` / `#ece7dc` |

HTML chrome on top of a dark field must keep contrast. Do not put
`--fg` gray-on-gray over a shader.

Pointer events: **none** on the canvas unless the scene *is* the
control (OrbitControls product viewer, liquid-metal button). Backgrounds
must never steal scroll or clicks.

---

## Fingerprints (site + components)

ThreeUI's own chrome is a quiet product-docs shell. Steal the
discipline, not a clone.

**Appearance machine** (`src/theme.ts`):

- Mode: `light | dark | system`
- Palette, stored separately per scheme: `mono | sepia | azure | moss | mauve`
- Default stored theme: **dark**, palette **mono**
- Applied as `data-theme`, `data-scheme`, `data-palette` on `<html>`

**Type**

- Display / UI: Geist
- Meta: Fragment Mono, 8–10px, tracking `0.10–0.12em`, weight 400
- Headings in article-list: 18–44px (container-query `cqw`), weight 600,
  tracking `-0.02em`, line-height 1.08

**Surfaces**

- Hairline borders `#292929` / `#2a2a28` (dark), `#d9dce3` (light)
- Dock: `border-radius: 11px` outer, `7px` items, `rgba(14,14,14,.86)` +
  `backdrop-filter: blur(18px) saturate(75%)`
- Soft inset highlight `inset 0 1px rgba(255,255,255,.035)`
- Optional 12% fractal-noise overlay, `mix-blend-mode: soft-light`
  (one overlay, not grain on every card)

**Motion**

- Ready-fade: **180ms ease-out** (universal)
- Dock hover: 150–180ms on color/border, magnification via width/height
- Reduced motion: dock transform none; button frame transition none
- Mobile ≤ 600px: kill dock magnification (`transform: none !important`)

**Container queries** on article headings and the top dock. Prefer
`cqw` over viewport for anything inside a preview frame.

Map these onto existing `@theme` tokens. Do not add Geist + Fragment
Mono if the app already has a pair; keep the *roles* (display vs 8–10px
tracked meta).

---

## Performance and disposal (non-optional)

From ThreeUI's own FAQ and from Sebastian on the launch thread
(agent edits leak GPU memory):

- `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`
- Pause RAF when the canvas is off-screen (`IntersectionObserver`)
- On unmount: `geometry.dispose()`, `material.dispose()`,
  `texture.dispose()`, `renderer.dispose()`, cancel RAF, remove
  listeners. SPAs that skip this crash after a few route changes.
- Lower particle / marching counts on mobile. Provide a **still
  poster** (`<img>` or first frame) when WebGL fails or
  `prefers-reduced-motion: reduce`.
- Test contrast of HTML over the live shader, not over the thumbnail.

Decorative 3D is a progressive enhancement. The page must read with
the canvas deleted.

---

## Hard rules

- **One GPU scene per view.** Same cap as Rare UI / orbs / beam.
- ThreeUI does **not** replace shadcn. Buttons that are actually
  buttons (submit, dialog, menu) stay in the primitive kit. Liquid-metal
  is a marketing CTA, not a form control.
- Do not mix ThreeUI + Magic UI + Aceternity + Rare orbs on one page.
  Pick **one** decorative family.
- Do not use ThreeUI inside app interiors (chat, table, settings).
  Canvas UI / Beautiful UI already cover "mark over live HTML" for
  product chrome.
- Do not rewrite a 200 KB procedural scene "to make it ours". Retune
  parameters. If the interaction is wrong, pick a different catalog item.
- Community is MIT. Remote thumbnails on threeui.com are **not**
  redistributable; use the source, not hotlinked previews.
- Pro MCP/CLI is entitled. Do not paste Pro implementation into this
  repo or a client app unless the user has a license.

---

## When CSS is enough

Reach for ThreeUI only after this filter fails:

| Want | CSS / canvas-2d first |
| --- | --- |
| Thinking orb as status | AICSS / `ai-primitives.md` / orbs.jakubantalik.com |
| One beam on a selected card | beam.jakubantalik.com (8px / 3px blur / 200ms) |
| Grid-reveal, tilt card, toast stack | `motion-blocks.md` (beUI / Rare UI) |
| Kinetic type that is just a heading | CSS clip / mask; Text Path Studies only if the type *is* the piece |
| Grain overlay | One SVG turbulence, already in ThreeUI chrome — don't add a scene for grain |

Three.js when the user asked for a **scene**: product spin, living
landscape, CRT terminal, liquid metal, cloth, bookshelf. Otherwise it
is slop with a GPU bill.

---

## Pairing

| Concern | Owner |
| --- | --- |
| Tokens, type, radii, anti-slop | `design-ui` + this skill §3 |
| App / docs skeleton | `layout-steal.md` |
| Campaign / Y2K explorer | `editorial-campaign.md` (2D). ThreeUI can be the *hero product stage* under that chrome, not a second motif family |
| 3D / WebGL moment | **this file** |
| Distinctive CSS motion | `motion-blocks.md` |

Quiet landing + one Structure Flow or Predictive Arc is the default
tasteful move. Loud landing + Sylva + liquid-metal + vortex type is a
demo reel, not a product.

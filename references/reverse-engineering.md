# Reverse-engineering notes

Method used on every site below: fetch HTML/CSS (not marketing copy),
read tokens, radii, shadows, keyframes, density, then decide **steal /
skip / one-shot**. Do not clone brands. Reimplement fingerprints against
the app's `@theme`.

How to read a card:

| Field | Meaning |
| --- | --- |
| Job | What to steal it for |
| Fingerprints | CSS/motion facts from the live site |
| Steal | Patterns that survive restyling |
| Skip | What becomes slop if copied wholesale |
| Agent move | Concrete action |

---

## A. AI-native chrome (the actual job of most agent UIs)

### Beautiful UI — [beautifului.dev](https://www.beautifului.dev/)

Crafted primitives for chat, thinking, streaming, approvals, tools.

**Fingerprints (from their CSS):**

- Document: `font-size: 14px`, `letter-spacing: -0.01em`, Inter with
  `font-feature-settings: "cv11", "ss01"`
- Color: oklch steps `--page --canvas --surface --field --ink --ink-2
  --ink-3 --line --accent` + semantic `--green --orange --red` tints
- Radius: chip **6** / control **8** / card **10** / window **14**
- Elevation: hairline first (`0 0 0 1px var(--line)`), then optional
  multi-stop soft shadow. Dark: white ring at ~10–15% + real shadow
- Ease: `--ease-out-strong: cubic-bezier(.23, 1, .32, 1)`
- Press: `scale(0.94)`. Pop-in: `scale(.95)` at **160ms**
- Streaming: in-flight tail `filter: blur(1.6px)` + right-edge mask;
  caret `2×1.05em`, `step-end` blink 1s; solid while tokens arrive
- Loader: 4×4 pixel grid, `@keyframes pixel-on` opacity `.15 → 1`
- Thinking: collapsed "Thought for Ns"; shimmer on the status line
  (`background-position 150% → -50%`), not a page spinner
- Canvas (docs only): `-45deg` 7px/1px stripe, never on dashboards

**Steal:** the primitive set, hairline rings, 14px interior register,
streaming caret/tail, pixel loader, concentric radii.
**Skip:** ice-cream demo copy, stripe canvas on app chrome, 0.94 press
if the rest of the app already uses 0.96 — pick one.
**Agent move:** implement `ai-primitives.md`. Do not iframe.

### AICSS — [aicss.dev](https://www.aicss.dev/)

Same job as Beautiful UI, ships React / Vue / Svelte. Orbs are a first-
class thinking mark.

**Fingerprints:**

- Keyframes: `ab-shimmer` (`background-position -200%`), `ab-caret`,
  `ab-blink`, `ab-modal-pop` from **`scale(.985)`** (even quieter than
  Beautiful UI's 0.95), `cardIn` = `translateY(6px) + blur(2px)`
- Thinking orbs: a state machine of CSS orbs — `breathe`, `wave`,
  `comet`, `focus`, `revolve`, `bloom`, `converge`, `handoff`,
  `ring-chase`, `globe-spin`. Opacity rest vs active, blur 2–2.4px,
  scale 0.35 → 1.2, `cubic-bezier(.66,0,.34,1)` on wave
- Prompt input: spinning border (`ab-pi-border-spin`), chips/pills
  enter/exit, menu pop
- Streaming: sentence-level `tr-sentence-in` (opacity 0 → 1), not
  whole-paragraph typewriter

**Steal:** quieter modal scale (0.985), sentence-level stream reveal,
orb as *status* not decoration, Vue/Svelte ports if the app is not React.
**Skip:** running three orb states at once; spinning borders on every
input.
**Agent move:** if you need a thinking mark, one orb (or pixel grid).
Map orb states onto real agent phases (idle / think / tool / stream).

### AI Elements — [elements.ai-sdk.dev](https://elements.ai-sdk.dev/)

shadcn registry **wired to Vercel AI SDK**: Conversation, Message,
Reasoning, Chain of Thought, Tool, Confirmation, Prompt Input, Sources,
Suggestion, Task, Queue, Plan, Shimmer, plus code (artifact, file tree,
terminal) and voice.

**Steal:** composition API and state names (Reasoning duration, Tool
status, Confirmation). Use when the app already speaks AI SDK.
**Skip:** installing it *and* Beautiful UI *and* AICSS. One AI chrome
set per app.
**Agent move:** `npx shadcn add` from this registry only if AI SDK is
already a dependency. Otherwise reimplement the same slots from
`ai-primitives.md`.

### Cult UI — [cult-ui.com](https://www.cult-ui.com/)

shadcn blocks with an unusually high density of **agent patterns**
(streaming, thought chains, expandable composer, HITL cards).

**Steal:** composer/toolbar expansion, thought-chain layout, HITL card
stack.
**Skip:** particle CTAs, wave textures, "premium marketing" effects on
an app interior.
**Agent move:** copy one agent block's structure, restyle to tokens.

### LiveKit Agents UI

Voice-agent chrome on shadcn + AI Elements: session, transcript,
audio visualizer, I/O controls.

**Steal:** only if the product is actually voice. Visualizer +
transcript + mute/session are the skeleton.
**Skip:** using a voice visualizer as a fake "AI is thinking" on a
text-only app.

---

## B. Motion / delight (use as seasoning)

### transitions.dev

Recipe book keyed by **visible verb** (menu origin-aware, number
pop-in, skeleton reveal, streaming text, thinking states…).

**Steal:** the verb → recipe map. Durations already in `design-ui`
and `motion-blocks.md`.
**Skip:** stacking three recipes on one click; copying demo ms blindly.

### beUI — [beui.dev](https://beui.dev/)

Motion registry on shadcn + Motion: tilt card (perspective + cursor
glare), morphing-height modal (blur cross-fade), toast stack with
status morph, dock, dynamic island, bottom sheet.

**Steal:** morphing-height panel, origin-aware toast stack, tilt on
**one** marketing card.
**Skip:** metallic buttons, bloom menus, and island clones on CRUD.
**Agent move:** CSS-first ports in `motion-blocks.md`. Add `motion`
only if `package.json` already has it.

### Rare UI — [rareui.com](https://rareui.com/)

Uncommon one-offs: `fluid-orb`, `grid-reveal`, `gravity-letters`,
`bounce-sidebar`, `proximity-sidebar`, `step-player`,
`scroll-progress`, `notification-bell`.

Install: `npx shadcn@latest add swamimalode07/rare-ui/{name}`

**Steal:** one ambient piece (orb for listening, grid-reveal for a
hero).
**Skip:** a page made of gravity letters + bouncing sidebars.

### Orbs — [orbs.jakubantalik.com](https://orbs.jakubantalik.com/)

Dotted thought-orbs. Nine states, two sizes, auto theme. System UI
stack, 150ms default, linear shimmer.

**Steal:** the idea of **named states** (idle / think / tool / error)
instead of one looping spinner.
**Skip:** custom WebGL if CSS dots suffice.

### Border Beam — [beam.jakubantalik.com](https://beam.jakubantalik.com/)

Animated glowing border. Their own site is the fingerprint:

- `--c-bg: #070707`, surfaces at `rgba(217,217,217,.05)`
- Tabs: **200ms** `cubic-bezier(.22, 1, .36, 1)`
- Page swap: 8px slide + **3px blur**, 200ms, same ease
- Shimmer: 2s linear, band 400%, base `#6f6c6c` → highlight `#ededed`

**Steal:** the 200ms / 8px / 3px-blur page recipe (also in
transitions.dev). Beam itself: **one** primary CTA or a selected
card, never every tile.
**Skip:** rainbow chasing borders on tables, inputs, nav.

### Magic UI — [magicui.design](https://magicui.design/)

Marquee, shine border, retro grid, animated beam, particles. React +
Tailwind + Motion. Highest slop-risk library in this list because
agents love to sprinkle all of it on a hero.

**Steal:** at most **one** (a logo marquee *or* a shine on the
primary button).
**Skip:** retro-grid + particles + shine + marquee together. That
*is* the slop look.

### Aceternity UI — [ui.aceternity.com](https://ui.aceternity.com/)

Landing-page motion: glare card, globe, bento, text-reveal, canvas
cards. 200+ blocks.

**Steal:** bento **structure** (tracks, not the glare). One text
reveal on a marketing hero.
**Skip:** GitHub globe + glare + generate-text on an app shell.
Bundle and a11y cost is real; reduced-motion is mandatory.

### Originkit — [originkit.dev](https://www.originkit.dev/)

Free animated kit, copy / Framer / MCP. Treat like Magic UI: one
effect, restyle, don't theme the app around it.

### Canvas UI — [canvasui.dev](https://canvasui.dev/)

WebGL / html-in-canvas effects over **live HTML**. Cross-framework.

**Steal:** only for a hero or a generative mark. Keep the actual UI
in the DOM (selectable, a11y).
**Skip:** putting product chrome inside a canvas. Screen readers and
forms die.

### Skiper UI — [skiper-ui.com](https://skiper-ui.com/)

"Un-common" shadcn components (dynamic island, image cursor trail,
devouring-details sign-in). One file per component, CLI install.

**Steal:** one uncommon interaction if it matches the product (island
for a live session, not for settings).
**Skip:** cursor trails on data-entry screens.

---

## C. Primitive kits and page blocks (the skeleton)

### shadcn/ui — [ui.shadcn.com](https://ui.shadcn.com/)

Default kit for this skill. Copy-own, Radix, Tailwind tokens.
2026 also ships **chat primitives** (Message, Bubble, Attachment,
MessageScroller). Prefer those for chat *layout*; keep Beautiful UI
fingerprints for stream/think/caret.

**Steal:** Button, Input, Dialog, Sheet, Menu, Tabs, Card, Table,
Skeleton, and the chat layout pieces.
**Skip:** generating a parallel kit.

### ReUI — [reui.io/components](https://reui.io/components)

1100+ compositions on shadcn: data grid, filters, kanban, gantt,
stepper, file upload, charts.

**Steal:** dashboard skeletons and data-heavy patterns.
**Skip:** their theme. Rebuild on app tokens.

### Kibo UI — [kibo-ui.com](https://www.kibo-ui.com/)

Composable shadcn registry: Gantt, Kanban, Editor. Same rule as ReUI.
Pick **either** ReUI or Kibo for data views, not both.

### coss ui — [coss.com/ui](https://coss.com/ui)

Base UI instead of Radix. Same job as shadcn. **Do not mix.**

### shadcnblocks / 21st.dev / Tailark

Page-level blocks (hero, pricing, dashboard shells). Rexan Wong's
method lives here: paste the **tracks**, delete their colors, fill.

**Steal:** CSS grid tracks, max-width, sticky bits, density.
**Skip:** stock illustrations, gradient heroes, "Live" badges.

### swagui — [swagui.rohoswagger.com](https://swagui.rohoswagger.com)

Philosophy more than components:

- Identity is **fixed**: radius, type scale, shadow, motion curve
- Color is the only preset
- Surfaces = `color-mix()` of fg/bg → dark mode is free
- Two registers: compact app interior vs generous marketing

**Steal:** the philosophy. Encode it in `@theme`.

### Design System Checklist — [designsystemchecklist.com](https://www.designsystemchecklist.com/)

Coverage audit (color, type, space, elevation, motion, content, a11y).
Use as a finish gate, not a visual style.

### You Don't Need Animations — [emilkowal.ski/ui/you-dont-need-animations](https://emilkowal.ski/ui/you-dont-need-animations)

- Purpose first
- High-frequency / keyboard → **zero** motion
- UI motion < 300ms (180ms dropdown beats 400ms)
- Spatial consistency (toasts enter and exit on the same axis)

---

## D. Cross-site fingerprints (the shared physics)

These numbers recur. Treat them as the default physics of "not slop":

| Token | Recurring value | Seen on |
| --- | --- | --- |
| Ease | `cubic-bezier(.23,1,.32,1)` or `(.22,1,.36,1)` | Beautiful UI, beam, transitions |
| Open | 180–220ms | almost all |
| Close | 150ms | design-ui, Emil |
| Enter scale | 0.95–0.985, **never 0** | Beautiful UI 0.95, AICSS 0.985 |
| Press | 0.94–0.96 | Beautiful UI 0.94, design-ui 0.96 |
| Stream tail | 1.6–2px blur + mask | Beautiful UI |
| Caret | 2px × ~1em, step-end 1s | Beautiful UI, AICSS |
| Card enter | 6–8px `translateY` + optional 2px blur | AICSS `cardIn`, beam page |
| Hairline | `0 0 0 1px` tokenized ring | Beautiful UI, swagui |
| Interior type | 13–14px, tracking -0.01em | Beautiful UI |
| App max-width | 960–1080px | Beautiful UI 960 |
| Marketing max | 1120–1200px | common blocks |
| Radius nest | chip 6 / control 8 / card 10–12 / window 14–16 | Beautiful UI |

If a generated UI uses 400ms, `scale(0)`, `transition: all`, or
`p-[13px]`, it has left this physics.

---

## E. Decision tree

```
Is it an AI product (chat / agent / copilot)?
  yes → AI chrome from Beautiful UI fingerprints
        + shadcn chat layout (or AI Elements if AI SDK is already there)
        + one thinking mark (pixel grid or one orb)
  no  → skip AI primitives

Is it a dashboard / data app?
  yes → shadcn + ReUI or Kibo skeleton (one of them)
  no  → continue

Is it a marketing landing?
  yes → steal a block skeleton (shadcnblocks / Tailark structure)
        + at most ONE effect (beam or tilt or text-reveal)
  no  → app interior register (14px, tight gaps)

Need a distinctive moment?
  yes → one beUI/Rare/Skiper piece, restyle to tokens
  no  → do not add Magic UI "just because"
```

**Hard cap:** 3–7 stolen blocks per surface, one primitive kit, one
AI-chrome family, one decorative effect.

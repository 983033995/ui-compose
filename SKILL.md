---
name: ui-lego
description: >
  Compose frontend from proven UI blocks instead of inventing from a blank
  canvas. Use whenever you build or restyle pages, dashboards, landing pages,
  AI-product chrome (chat, thinking, streaming, approvals, tool calls), or
  any interface that would otherwise look like generic "AI slop". Encodes the
  Lego workflow from public agent-UI practice plus reverse-engineered recipes
  from Beautiful UI, AICSS, AI Elements, beUI, Rare UI, transitions.dev,
  shadcn, ReUI, Kibo, Magic UI, Aceternity, and related registries.
  Triggers on "frontend", "UI", "looks like AI", "slop", "polish",
  "landing", "dashboard", "chat UI", "agent UI", "component library",
  "make it look good", "design system", "Y2K", "lookbook", "campaign",
  "product explorer", "footwear", "DTC".
metadata:
  short-description: "Lego frontend: steal structure, compose proven blocks, anti-slop AI-native UI"
user-invocable: false
---

# UI Lego

AI is good at filling details and terrible at inventing taste, spacing, or
structure. Do not ask it (you) to design a UI from zero. Steal a skeleton,
compose real components like Lego, then customize.

This skill is the **composition workflow**. Visual tokens, anti-slop bans,
typography, surfaces, and chrome motion still live in **`design-ui`** — open
that too. This file tells you *how to pick blocks and wire them* so the result
does not look vibe-coded.

**Read `references/` on demand (do not inline all of them):**
- `references/goals.md` — what this skill is for, and what it is not
- `references/sources.md` — which library to steal from, for what
- `references/reverse-engineering.md` — CSS fingerprints, steal/skip, decision tree
- `references/layout-steal.md` — steal the skeleton before styling
- `references/ai-primitives.md` — reverse-engineered AI-native chrome (Beautiful UI)
- `references/motion-blocks.md` — distinctive motion blocks (beUI / Rare UI / Emil)
- `references/editorial-campaign.md` — Y2K × editorial DTC landings (SOLESHIFT° / SWIRL°)

---

## 0. Pairing with `design-ui`

| Concern | Owner |
| --- | --- |
| Tokens, color cap, type, concentric radii, anti-slop bans | `design-ui` |
| Chrome motion catalog (menu, modal, tooltip, number pop-in) | `design-ui` `references/` |
| *Which* blocks to compose, layout skeleton, AI-native primitives | **this skill** |
| When *not* to animate | this skill §4 + Emil |

Never invent a second token set. Map any stolen block onto the `@theme`
tokens already defined in `src/styles.css`.

---

## 1. The Lego workflow (do this in order)

Copied from the method that actually works in the wild (Peng, Machina, Rexan
Wong, Greg Isenberg, Ole Lehmann):

1. **Positive reference.** Name one real product feel (Linear / Raycast /
   Stripe / Notion / a specific block library). Do not say "make it modern".
2. **Negative reference.** Explicitly ban the slop tells (see §3). Treat them
   as an anti-target, not a vibe.
3. **Steal the skeleton first** (`references/layout-steal.md`). Layout and
   spacing before color, motion, or illustration. Paste a real block's
   structure (grid, max-width, header/body/aside) and *fill* it.
4. **Pick 3–7 blocks** from `references/sources.md`. Prefer copy-own
   components (shadcn / ReUI / coss) over generating a button from scratch.
5. **Inspect → pick → integrate → customize.** Once the agent has actual
   component source, editing is easy. Inventing source is how slop happens.
6. **One style guide.** If the app has no tokens yet, write them once in
   `src/styles.css` `@theme` *before* any JSX hex. Every later component
   references that file — this is how consistency happens.
7. **Restrain motion.** High-frequency and keyboard-driven UI: no animation.
   Infrequent, explanatory, or spatial UI: use a recipe from `design-ui` or
   `references/motion-blocks.md`. UI motion ≤ 300ms.

Quote that is the whole skill: *give the model a professional skeleton, not a
blank canvas.*

---

## 2. Source picker (default for this stack)

This workspace is TanStack Start + React 19 + Tailwind v4 + Radix. Prefer
**copy-own** source over new npm UI kits.

| Need | Steal from | Notes |
| --- | --- | --- |
| Buttons, dialogs, inputs, menus, cards, tabs, sheets | **shadcn/ui** (Radix already in tree) | Default. Generate into `src/components/ui` |
| Chat *layout* (message, bubble, scroller) | shadcn 2026 chat components | Layout only; stream/think still from `ai-primitives.md` |
| Dashboard / data-heavy compositions | [ReUI](https://reui.io/components) **or** [Kibo](https://www.kibo-ui.com/) | Pick one. Data grid, filters, kanban, gantt, stepper |
| Base-UI-flavored primitives | [coss ui](https://coss.com/ui) | Same job as shadcn; do not mix kits in one app |
| AI chat, thinking, streaming, tool calls, approvals | `references/ai-primitives.md` | Beautiful UI fingerprints. AICSS if Vue/Svelte |
| AI SDK already in the app | [AI Elements](https://elements.ai-sdk.dev/) | Don't also install Beautiful UI / AICSS |
| Voice agent | LiveKit Agents UI | Only if the product is actually voice |
| Distinctive motion (tilt, morphing panel, toast stack) | `references/motion-blocks.md` (beUI) | CSS-first; add `motion` only if already in `package.json` |
| One ambient mark (orb, grid-reveal, beam) | Rare UI / [orbs](https://orbs.jakubantalik.com/) / [beam](https://beam.jakubantalik.com/) | **One** per surface |
| Landing-page structure | shadcnblocks / Tailark / ReUI blocks | Steal tracks, delete their theme |
| Landing-page *effect* | Magic UI / Aceternity / Originkit / Skiper | **At most one.** These are the slop-risk kits |
| Playful product explorer / Y2K campaign | `references/editorial-campaign.md` | Locked chrome + SKU-owned worlds. Not for dashboards |
| Token / theme discipline | swagui idea: surfaces from `color-mix` of fg/bg | Dark mode for free; radius/type/shadow stay fixed |

**Do not install** a second component library next to shadcn. One kit, restyle
with tokens.

---

## 3. Anti-slop (the tells — hard fails)

These are the negative reference. If a screenshot of the app would match this
list, rewrite the surface before calling UI done.

- Gradient-blob / aurora / mesh / "AI purple" heroes **on app chrome**
  (campaign register may use *one motif family* of blobs — see
  `editorial-campaign.md`)
- Glassmorphism soup, rainbow borders, neon glow
- Emoji as icons or in chrome copy
- Inter-everywhere with no weight/size hierarchy
- Cards with identical radius to their inner controls
- Elements floating with no grid, no max-width, no shared gutter
- Lorem / gray placeholder boxes in a finished view
- Every control bouncing, glittering, or using `transition: all`
  (campaign: bounce is allowed on **SKU cards + hero only**)
- Purple/violet/gold as the brand accent unless the user named that brand
  **or** a SKU world in the campaign register
- "Live" badges, shimmer on static text, decorative grain on every panel
- AI inventing spacing like `p-[13px]` / `gap-[17px]` instead of the scale

Comment that matters: **design systems beat vibe coding** — models hallucinate
spacing tokens unless you give them one scale and refuse ad-hoc values.

---

## 4. Motion: purpose, frequency, speed

From Emil Kowalski, *You Don't Need Animations*:

- **Purpose first.** If you cannot name what the motion explains, delete it.
- **Frequency.** Daily / many-times-an-hour / keyboard-initiated → **no
  animation**. Raycast does not animate open. Highlight that follows arrow
  keys must be instant.
- **Speed.** UI motion generally **under 300ms**. 180ms dropdown beats 400ms.
- **Asymmetric.** Enter a bit slower, exit quicker. Never `scale(0)`.
- **Interruptible.** CSS transitions for hover/open/close; keyframes only for
  one-shot sequences (success check, error shake).
- **Reduced motion.** Every recipe has a `prefers-reduced-motion` branch.

Chrome recipes (menus, modals, tooltips, sliding pills, number pop-in) are
already in `design-ui`. Use `references/motion-blocks.md` only for the
distinctive blocks (tilt, morphing height panel, toast stack, grid-reveal,
streaming caret).

---

## 5. AI-native surfaces (when the product talks to a model)

If the app streams tokens, shows tools, asks the user to approve, or has a
composer: implement primitives from `references/ai-primitives.md`. Do not
fake them with a single `<pre>` and a spinner.

Minimum set for any agent/chat view:

1. **Streaming text** — tail blur + caret, not a blinking block cursor on the
   whole paragraph
2. **Thinking trace** — collapsed by default, elapsed time, expandable steps
3. **Tool chips** — compact, file + status, not a wall of JSON
4. **Composer / prompt bar** — `@` sources, `/` commands, one primary send
5. **Approval card** — when the model needs a human decision before acting

Loading is a **pixel-grid or shimmer-on-status-line**, not a centered CSS
spinner on a blank page.

---

## 6. Layout rules that actually kill slop

From the layout-steal posts: models place elements randomly unless you give
them a skeleton.

- One content `max-width` (marketing ~1120–1200px, product ~960–1080px, reading
  ~60–75ch). Gutters from the spacing scale, not magic numbers.
- CSS grid for page chrome (`header / aside / main` or `header / main /
  footer`). Flex only inside a cell.
- **Steal a block's structure first** (hero + 3-up + quote + footer, or
  app-shell + list + detail). Then swap copy and tokens.
- Marketing and app interiors are two registers: marketing is generous
  (large type, big gaps); app interiors are compact (13–14px base, tight
  toolbars). Do not mix.
- A **third register** exists for campaign/lookbook pages only:
  `references/editorial-campaign.md` (cream paper, chunky type, SKU-owned
  worlds, hover swaps the whole stage). Never carry its bounce/blobs into
  app chrome.
- Mobile (~390px) first. No horizontal overflow. Tap targets ≥ 44px.

---

## Finish checklist

- [ ] Tokens exist in `@theme`; stolen blocks remapped onto them (no second kit)
- [ ] Layout skeleton stolen, not invented; one max-width + grid
- [ ] ≤ 5 colors, ≤ 2 fonts, concentric radii, no ad-hoc hex / arbitrary px
- [ ] None of the §3 slop tells
- [ ] Motion has a purpose and a frequency test; ≤ 300ms; reduced-motion safe
- [ ] If it's an AI product: streaming / thinking / tools / composer are real primitives
- [ ] Eyeballed in a real browser (AGENTS.md verification), not just curl

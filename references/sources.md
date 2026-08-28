# Source catalog

Pick one kit for primitives. Compose special blocks on top. Never mix two
button/input systems in the same app.

CSS fingerprints, steal/skip, and the decision tree live in
`reverse-engineering.md`. This file is the shopping list.

Prefer **copy-own** source (shadcn CLI / paste) over new npm UI kits.

## Primitive kits (pick one)

| Kit | Use when | How |
| --- | --- | --- |
| [shadcn/ui](https://ui.shadcn.com/) | Default | Copy into `src/components/ui`; restyle via tokens. 2026 chat layout: Message, Bubble, Attachment, MessageScroller |
| [coss ui](https://coss.com/ui) | You want Base UI, not Radix | Same copy-own model. **Do not** add it next to shadcn |
| [ReUI](https://reui.io/components) | Dashboards, data grids, filters, kanban, steppers, upload | Compositions *on* shadcn — steal structure, not theme |
| [Kibo UI](https://www.kibo-ui.com/) | Gantt, Kanban, Editor on shadcn | Pick **either** ReUI or Kibo for data views, not both |

**Reach for shadcn first** for: Button, Input, Textarea, Label, Dialog,
AlertDialog, Sheet, DropdownMenu, Popover, Select, Tabs, Badge, Card,
Separator, Skeleton, Tooltip, Toggle, Switch, Checkbox, Radio, Table.

## AI-native chrome (pick one family)

| Source | Use when | Notes |
| --- | --- | --- |
| [Beautiful UI](https://www.beautifului.dev/) | Default for text agents | No package. Reimplement `ai-primitives.md` |
| [AICSS](https://www.aicss.dev/) | Need Vue/Svelte, or orb-as-status | React/Vue/Svelte. Orbs are a state machine, not decoration |
| [AI Elements](https://elements.ai-sdk.dev/) | App already uses Vercel AI SDK | shadcn registry. Don't also vendor Beautiful UI |
| [Cult UI](https://www.cult-ui.com/) | Want a thought-chain / HITL block | Steal one agent block's structure |
| LiveKit Agents UI | Product is actually voice | Session, transcript, visualizer, I/O |

Minimum set for any agent view: streaming text, thinking trace, tool
chips, composer, approval card. See `ai-primitives.md`.

## Motion / delight (one or two, not a carnival)

| Source | Steal | Skip |
| --- | --- | --- |
| [transitions.dev](https://transitions.dev/) | Verb → recipe map | Stacking three recipes on one click |
| [beUI](https://beui.dev/) | Tilt, morphing-height panel, toast stack, dock, island, sheet | Metallic / bloom on CRUD |
| [Rare UI](https://rareui.com/components) | One ambient: fluid-orb, grid-reveal, step-player | Gravity letters on every view. CLI: `npx shadcn@latest add swamimalode07/rare-ui/{name}` |
| [Orbs](https://orbs.jakubantalik.com/) | Named thinking states (idle/think/tool) | Custom WebGL when CSS dots suffice |
| [Border Beam](https://beam.jakubantalik.com/) | One CTA/selected card; 200ms / 8px / 3px-blur page recipe | Rainbow beam on every tile |
| [Magic UI](https://magicui.design/) | At most one (marquee *or* shine) | Retro-grid + particles + shine together = slop |
| [Aceternity](https://ui.aceternity.com/) | Bento **structure**; one text-reveal | Globe + glare + generate-text on an app shell |
| [Originkit](https://www.originkit.dev/) | One free animated piece | Theming the app around it |
| [Canvas UI](https://canvasui.dev/) | Hero / generative mark over live HTML | Product chrome inside a canvas |
| [Skiper UI](https://skiper-ui.com/) | One uncommon interaction (island, trail) | Cursor trails on data-entry |
| [ThreeUI](https://threeui.com) | One real 3D/WebGL moment (hero, shader field, liquid-metal CTA). Community MIT: `@designcodeio/threeui` / [MengTo/threeui](https://github.com/MengTo/threeui) | Inventing GLSL. Stacking with Magic UI. GPU inside chat/CRUD. See `threeui.md` |
| [You Don't Need Animations](https://emilkowal.ski/ui/you-dont-need-animations) | When to ship **zero** motion | — |

Rare UI names: `fluidorb`, `gridreveal`, `gravityletters`,
`bouncesidebar`, `proximitysidebar`, `stepplayer`,
`scrollprogressindicator`, `notificationbell`, `otpinput`, `codeblock`,
`durationpicker`, `foldercomponent`, `githubactivity`, `emojireaction`.

beUI names: File Tree, Morphing Modal, Animated Toast Stack, Action Swap,
Dock, Dynamic Island, Command Palette, Tilt Card, Bottom Sheet, Number
Animation.

CSS-first ports: `motion-blocks.md`. Add `motion` only if already
installed.

## Tokens, layout, audit

| Source | Steal |
| --- | --- |
| Sibling `design-ui` skill (if present) | Token block for the host app |
| [swagui](https://swagui.rohoswagger.com) | Fixed identity (radius/type/shadow/ease). Color-only presets. `color-mix` surfaces. Two densities |
| [Design System Checklist](https://www.designsystemchecklist.com/) | Coverage audit, not a look |
| shadcn blocks / [shadcnblocks](https://www.shadcnblocks.com/) / Tailark / 21st.dev | Page **tracks** (hero, pricing, app shell). Delete their theme |

Beautiful UI's own chrome is a strong product-docs shell: `max-w-[960px]`,
dashed hairline, sticky 288px aside. See `layout-steal.md`.

## Workflow sources (why this skill exists)

These posts independently converged on the same method. Follow the method,
not the links as a cargo cult.

- Peng (@pengsonal): send the agent the resource → inspect → pick →
  integrate and customize. "Like Lego."
- Machina (@EXM7777): collect modules, fetch the full list, integrate
  into a foundation.
- Rexan Wong: AI fills details but cannot invent structure. Paste a
  professional layout, then design into it.
- Greg / SIP: screenshot admired sites → extract a design system → every
  future component references that file.
- Saadat: `design.md` + a reusable component library.
- Ole Lehmann: positive reference + negative (slop) reference + extra
  thinking on design work.
- Tran Mau Tri Tam / Nero: additional agent-ready kits (AICSS, orbs,
  beam, canvas, originkit).
- Keisuke: micro-interaction registries (copy-own, not a closed API).
- Shams (@ShamsAmin56): Y2K × editorial campaign landings (SOLESHIFT°,
  SWIRL°) — locked chrome, SKU-owned worlds, hover swaps the stage.
  See `editorial-campaign.md`.
- Meng To (@MengTo): ThreeUI — copy-ready Three.js scenes, 100–200 KB
  procedural, "give the prompt to your agent". Same Lego method for GPU.
  See `threeui.md`.
- Comment on Peng's post: models hallucinate spacing tokens.
  **Design systems > vibe coding.**

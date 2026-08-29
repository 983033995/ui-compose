# Grok source research — 2026-08-28

Second opinion for GPT to fold into #1. This is not a competing rewrite and not a license to install every kit on a Twitter list.

**Verdict:** keep Host Read. Take the DESIGN.md *shape* from Refero. Do not paste third-party product DESIGN.md files into a host. Do not grow the Source Registry from UI-kit shopping lists.

Fold accepted points in, then delete this file.

## Inputs

1. [Alok — “best modern UI component libraries”](https://x.com/alok619308/status/2093373247576486077)  
   CollectUI, Cue, Aceternity, Watermelon, 21st.dev, shadcnstudio, React Bits, Motion Primitives, Fancy Components, UI Layouts Pro, Number Flow, Component Gallery.
2. [Adham Dannaway — 2000 DESIGN.md files](https://x.com/adhamdannaway/status/2093343847262929064)  
   [styles.refero.design](https://styles.refero.design) by Mike Bespalov. Claimed free-to-use, structured for a model: colors, type, spacing, layouts.

## What is actually useful

### Refero Styles — methodology, not a skin pack

Reusable trait:

> After Host Read, a model-readable contract can list color roles, type roles, spacing/radius, layout tracks, and do/don’t rules so later steps stop inventing tokens.

Risk if copied literally: the catalog is 2,000 *other products’* identities. Dropping Linear/Stripe DESIGN.md into a Vue + Element Plus app is brand-copy. Refero MCP / `refero_skill` is a paid research product, not a UI Compose runtime.

**Do:** emit a compact host DESIGN.md from detected host tokens.  
**Do not:** `npx skills add referodesign/refero_skill` as a default.  
**Do not:** treat “free to use” marketing copy as a copy-own license. Keep `verify-upstream`.

### Component Gallery — host diversity, not a primitive kit

95 design systems × the same job (accordion, tabs, tree, pagination). Teaches anatomy-over-pixels: pick the host’s Accordion, do not import a foreign one because a gallery screenshot looked nicer.

Inspiration only. Third-party design-system material; no copy-own path.

### Motion Primitives — named motion verbs

MIT (`ibelick/motion-primitives`). Better evidence than Magic UI / Aceternity for *origin-aware, purpose-built motion* rather than effect stacking. Still React-specific. Reimplement the verb with the host motion stack; do not add `motion` only to fade a toolbar.

### Number Flow — tabular number physics

MIT (`barvian/number-flow`). Digit-wise, layout-stable numeric updates with reduced-motion default. Too small for a new Pattern ID. Belongs in `physics.md`. Do not add a number library to a B2B table that already has `toLocaleString()`.

## What was rejected

| Source | Why not canonical |
| --- | --- |
| Aceternity | Already an `effect-reference`, `inspiration-only-by-default`, high-slop-risk |
| Cue / cuedesign.space | Author promo, unclear license, Awwwards-ornament risk |
| CollectUI | Screenshot gallery; pattern recognition without extractable traits; brand-copy risk |
| 21st.dev, shadcnstudio | shadcn block catalogs; duplicate `shadcn` + high generic-dashboard slop |
| React Bits, Fancy Components | Effect samplers; overlap Magic UI |
| Watermelon, UI Layouts Pro | No independent durable trait found; paid-layout boundary on Pro |
| motionprompts.dev (reply) | Prompt pack, not a composition decision |

Research that only lengthens the website list must not merge. `references/sources.md` already says this.

## What GPT should fold

Already applied on this branch:

1. Source Registry: `refero-styles`, `component-gallery`, `motion-primitives`, `number-flow`
2. Host Read: host DESIGN.md contract (values from the host, structure may follow public DESIGN.md conventions)
3. SKILL.md Design Read: one short rule against third-party DESIGN.md identity substitution
4. Physics: tabular number motion + reduced-motion
5. Provenance / composition-selection: hard reject “ingest a catalog DESIGN.md as the host identity”
6. Reverse-engineering: shopping-list rejection example

Do **not**:

- add a `tabular-number-flow` Pattern until a second independent source needs it
- add adapters
- add Cue / 21st / shadcnstudio / React Bits
- install Refero MCP as a skill dependency
- claim Refero files are copy-safe
- reopen eval 01 quality claims; those already have observed records on #1

## Eval hypothesis (not a new case)

If a marketing/landing eval (case 06) or KPI strip is generated from a Twitter kit list, expect `unnecessary-dependency` + `wrong-motion` + `brand-copy-risk`. The failure is selecting Aceternity/React Bits before Host Read.

## Relation to PR #2

Same shape as `review/grok-compose-v0.3`: keep architecture, restore a missing implementable bit (here: Design Read contract), tell GPT what *not* to absorb from noisy public lists.

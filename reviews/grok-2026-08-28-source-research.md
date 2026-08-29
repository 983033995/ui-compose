# Grok source research — 2026-08-28

Second opinion for GPT to fold into #1. This is not a competing rewrite and not a license to install every kit on a Twitter list.

**Verdict:** keep Host Read. Take the DESIGN.md *shape* from Refero. Do not paste third-party product DESIGN.md files into a host. Do not grow the Source Registry from UI-kit shopping lists.

Fold accepted points in, then delete this file.

## Inputs

1. [Alok — “best modern UI component libraries”](https://x.com/alok619308/status/2093373247576486077)  
   CollectUI, Cue, Aceternity, Watermelon, 21st.dev, shadcnstudio, React Bits, Motion Primitives, Fancy Components, UI Layouts Pro, Number Flow, Component Gallery.
2. [Adham Dannaway — 2000 DESIGN.md files](https://x.com/adhamdannaway/status/2093343847262929064)  
   [styles.refero.design](https://styles.refero.design) by Mike Bespalov. Claimed free-to-use, structured for a model: colors, type, spacing, layouts.
3. [Kailash — animated icon sites](https://x.com/kail_designs/status/2093371585940038033)  
   lucide-animated, itshover, Lottie icon pack, Iconsax animated, Font Awesome animate. Quoted static list: Iconsax, Morphicons, Isocons, Iconly, Lucide, Hugeicons, Phosphor, Nucleo.
4. [Nazday — high-quality design work](https://x.com/nazmijavierl/status/2093281628949033026)  
   posts.design, CollectUI, 60fps.design, ogfolio, seesaw.website.
5. [George / prodmgmt.world — Refactoring UI plugin](https://x.com/nurijanian/status/2093292007267745999)  
   https://github.com/gnurio/refactoring-ui-plugin (all rights reserved, not affiliated with Tailwind Labs).

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

### Refactoring UI — methodology, not a sibling skill

The unaffiliated plugin encodes ten review passes (hierarchy, type, color, spacing, buttons, clutter, empty states, shadows, contrast, grouping). License is **all rights reserved**. The book is proprietary.

Reusable traits (already folded into `physics.md`, not copied from plugin files):

- one primary per region; de-emphasize competitors with weight/color/space, not size-alone
- action hierarchy mapped to **host** button variants (primary / secondary / tertiary / destructive)
- empty states need a next action, not a decorative illustration
- do not invent a palette or type scale when Host Read found one

**Do not** vendor `gnurio/refactoring-ui-plugin` SKILL.md files. **Do not** install it as a default sibling skill. **Do not** assume Tailwind because that plugin does.

### 60fps.design — observed motion, not a Lottie pack

Screenshot gallery of real-product micro-interactions. Extract the *verb* (purpose, origin, duration) like other observed-behavior sources. Do not clone Apple/Linear motion or add Lottie because a gallery clip looked expensive.

### Icons — Host Read, not eight new sources

If the host already has `@element-plus/icons-vue` / Lucide / Phosphor, reuse it. Animated icon kits are a second motion stack; they fail on nav, tables, and repeating chrome. Lucide-animated is MIT and still the wrong default for a B2B interior.

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
| Icon shopping lists (Iconsax, Morphicons, Hugeicons, Nucleo, Iconly, …) | Host Read detects one set; eight registry rows would be a kit picker |
| lucide-animated / Lottie icon packs | Animated-icon kit; slop on app chrome; second motion stack |
| posts.design / ogfolio / seesaw | Screenshot galleries; no extractable host-neutral trait beyond CollectUI (already rejected) |

Research that only lengthens the website list must not merge. `references/sources.md` already says this.

## What GPT should fold

Already applied on this branch:

1. Source Registry: `refero-styles`, `component-gallery`, `motion-primitives`, `number-flow`, `refactoring-ui`, `sixty-fps`
2. Host Read: host DESIGN.md contract + icon-set detection (no second family, no animated-icon default)
3. SKILL.md Design Read + anti-slop: DESIGN.md identity substitution; second icon family; two filled primaries
4. Physics: tabular numbers, emphasis (one primary per region), action hierarchy, empty-state-as-action
5. Provenance + composition-selection: DESIGN.md corpora; books/unaffiliated ARR plugins; second icon family / animated-icon kit
6. Reverse-engineering: two shopping-list worked examples

Do **not**:

- add a `tabular-number-flow` Pattern until a second independent source needs it
- add adapters
- add Cue / 21st / shadcnstudio / React Bits / icon marketplaces / lucide-animated
- install Refero MCP or the Refactoring UI plugin as a skill dependency
- copy plugin SKILL.md files or book prose into this repo
- claim Refero files are copy-safe
- reopen eval 01 quality claims; those already have observed records on #1

## Eval hypothesis (not a new case)

If a marketing/landing eval (case 06) or KPI strip is generated from a Twitter kit list, expect `unnecessary-dependency` + `wrong-motion` + `brand-copy-risk`. The failure is selecting Aceternity/React Bits before Host Read.

## Relation to PR #2

Same shape as `review/grok-compose-v0.3`: keep architecture, restore a missing implementable bit (here: Design Read contract), tell GPT what *not* to absorb from noisy public lists.

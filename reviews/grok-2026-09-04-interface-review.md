# Grok source research — interface review / Brand Lock (2026-09-04)

Second opinion for GPT to fold into `main`. Not a competing rewrite and not a license to `npx skills add` every popular interface skill.

**Verdict:** keep Host Read. Take evidence grades and accessibility-first review order from Jakub Krehel's MIT skills. Take reference-role lock from the Lovart branding write-up. Do not vendor sibling `SKILL.md` files. Do not grow the registry from another inspiration shopping list.

Fold accepted points in, then delete this file.

## Inputs

1. [meng shao / Jakub Krehel interface skills](https://x.com/shao__meng/status/2095691784500506793) → [jakubkrehel/skills](https://github.com/jakubkrehel/skills) (MIT). Domain skills (`better-ui/typography/colors/accessibility/layout/writing`) plus process skills (`better-interface`, `interface-review`, `break`, `variant`, `explain-interface`).
2. [AmirMušić — one reference → brand system](https://x.com/amirmushich/status/2095182776249049456) → Lovart-sponsored workflow + [brand-system-skill](https://github.com/amirmushichge/brand-system-skill) (CC-BY-4.0, Lovart Agent runtime).
3. [Dzianis — 4 sites I keep open](https://x.com/thedzianis/status/2095057887525769286) — GetLayers.ai, curated.design, 60fps.design, swiped.design.

## What is actually useful

### Evidence grades (explain-interface)

Reusable trait:

> Measured / Derived / Inferred. Do not present inferred CSS as measured. Do not invent values from a screenshot beyond sampled color/contrast. Do not dump a whole system when the question was one effect.

This is the missing quality bar for `reverse-engineering.md`. Already folded.

### Accessibility-first review + state stress

`better-interface` order: accessibility → layout → writing → typography → colors → ui. Cap findings. Evidence not taste. One root cause per row. Default read-only.

`break`: render long text / empty / ~320px in the **host** environment and observe before judging.

`variant`: three answers on **one** axis; tradeoff table; never mark a favourite.

Do **not** install the pack as a sibling runtime. UI Compose already owns composition. These are Verify/research traits.

### Brand Lock — reference roles, not a canvas product

Reusable trait:

> Each reference may control identity, composition, or scene — not all three. The Host Contract / approved kit owns identity. Scene references may not rewrite type, color, or motif. One approved anchor beats twenty disconnected generations. Approve the direction before generating volume.

This is Design Read + editorial locked-chrome, not a reason to add Lovart.

The skill is CC-BY-4.0 and Lovart-specific. Extract the role rule; do not vendor the file.

## What was rejected

| Source | Why not canonical |
| --- | --- |
| GetLayers.ai | Paid cinematic prompt catalog (Dzianis/Textura). Same class as MotionSites/ScrollTide |
| curated.design | Live-site screenshot gallery; no new host-neutral trait |
| swiped.design | Design-content gallery; no new trait |
| 60fps.design | Already rejected as a registry row on the source-research pass |
| Lovart Brand System Skill | CC-BY-4.0 + Lovart runtime; Brand Lock only |
| `npx skills add jakubkrehel/skills` as default | Scope overlap; UI Compose is the engine |

## What GPT should fold

Already applied on this branch:

1. Source Registry: `interfaces-skills` (MIT methodology; `runtime_dependency_default: false`)
2. `reverse-engineering.md` — evidence grades; reference roles; sibling-skill and GetLayers worked examples
3. SKILL.md Design Read + Verify — reference roles; a11y/layout before polish; stress long/empty/~320px; Measured vs Inferred
4. Provenance — sibling agent skills; GetLayers listed with prompt catalogs
5. CHANGELOG — removed the dangling pointer to the already-deleted motion-catalog review file

Do **not**:

- vendor `jakubkrehel/skills` or the Lovart `SKILL.md`
- add GetLayers / curated / swiped / 60fps / Lovart as sources
- add a `scroll-scrub-hero` or `brand-lock` Pattern
- add adapters
- reopen eval 01/04 quality claims
- treat `better-colors` palette generation as a Host Contract replacement

## Eval hypothesis

If an agent `npx skills add jakubkrehel/skills` beside UI Compose, expect competing review pipelines and Host Read being skipped. If eval 06/08 is generated from GetLayers prompts, expect the same `unnecessary-dependency` + `wrong-skeleton` + `prompt-catalog-stack` failures already named for MotionSites.

## Relation to PR #3 / #4

Same shape: keep architecture, restore a missing implementable bit (here: evidence-graded reverse-engineering + Verify order), tell GPT what *not* to absorb from public skill/shopping lists.

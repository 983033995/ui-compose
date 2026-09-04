# Changelog

## Unreleased

### Changed

- Renamed the GitHub repository and local project directory from `ui-lego` to `ui-compose`.
- Refreshed Eval 02 baseline provenance against the strengthened browser capture gate.

### Validation

- Added repository-local Markdown and `SKILL.md` reference validation to CI.

### Provenance

- Verified coss against its official AGPL-3.0 repository and kept it reference-only by default.
- Verified AICSS's MIT free-component boundary plus separate paid/locked component terms.

### Motion prompt-catalog pass (2026-08-29)

Folded from MotionSites / ScrollTide threads without turning UI Compose into a cinematic prompt picker:

- Scroll-scrubbed media as a host-neutral motion verb (`motion-blocks.md` §9): bind one video/poster to scroll progress, optional lerp, no autoplay loop, poster on reduced motion. Marketing / `immersive-hero` only.
- Physics: scroll-tied media is distance-mapped, not a 300ms timer; never on app interiors.
- Provenance: paid prompt catalogs are inspiration-only. Do not vendor prompt text or adopt their baked React + Tailwind + Framer Motion + lucide stack.
- Composition hard rejects: prompt-catalog default stack replacing the host; cinematic scroll-tied media on an app interior.
- Eval 06 hard failures for prompt-catalog stack, scroll-video default, and autoplaying hero without a reduced-motion poster.
- Explicitly did **not** add MotionSites, ScrollTide, or leaked prompt dumps to the Source Registry.

### Interface-review / Brand Lock pass (2026-09-04)

Folded from public interface-skill and branding-workflow threads without installing sibling skills:

- Reverse-engineering evidence grades: Measured / Derived / Inferred. Do not present inferred CSS as measured.
- Design Read reference roles: identity vs composition vs scene (Brand Lock as methodology, not a Lovart runtime).
- Verify: accessibility/layout before color/polish; stress long text, empty, and ~320px.
- `interfaces-skills` (`jakubkrehel/skills`, MIT) as methodology evidence. Do not vendor their `SKILL.md` files or `npx skills add` as a default.
- GetLayers classified with MotionSites/ScrollTide as a paid prompt catalog. curated.design / swiped.design stay out of the registry.

See `reviews/grok-2026-09-04-interface-review.md` until those notes are folded and deleted.

## 0.3.0 — Composition Intelligence foundation

### Added

- `references/patterns/registry.yaml` for reusable product/UI decisions independent of source libraries.
- `references/skeletons/registry.yaml` for page-level composition structures.
- `references/composition-selection.md` for host-aware skeleton/pattern selection and risk filtering.
- `references/physics.md` for host-neutral fallback UI physics: timing, easing, type/measure, radius nesting, elevation, action hierarchy, tabular-number behavior, and AI-streaming behavior.
- `references/patterns/recipes.md` for host-neutral implementation recipes attached to mature canonical Pattern IDs.
- Initial recipes for dense filter toolbar, master/detail preview, AI conversation thread, AI tool execution, human approval, persistent composer, and sticky contextual actions.
- JSON Schemas for Source, Pattern, Skeleton, Fixture, and observed Eval Result records.
- `scripts/validate_registries.py` for schema and cross-reference validation.
- `scripts/validate_skill.py` for Agent Skills frontmatter/name/description checks, progressive-disclosure budget, and OpenAI UI metadata validation.
- `scripts/validate_evals.py` for benchmark Fixture/Result validation, references, rubric arithmetic, and rendered-artifact requirements.
- GitHub Actions workflow to run skill + registry + eval validation on pushes and pull requests.
- `DELIVERY.md` defining stable-release gates, hard blockers, and a 100-point project-readiness model.
- `evals/harness/README.md` defining a reproducible rendered-benchmark execution and capture protocol.
- `evals/results/README.md` defining how observed benchmark evidence, screenshots, build status, dependency diffs, and scores are stored without fabricating results.
- Repeatable eval case format plus a nine-case host/product diversity matrix.
- Linear and Raycast as product-interaction evidence in the Source Registry.

### Second-opinion / recipe restoration

Integrated the useful parts of Grok PR #2 without merging its older review branch directly:

- retained Host Read, Source/Pattern/Skeleton registries, adapters, provenance, fixtures, and eval architecture;
- moved framework compatibility guidance out of top-level `SKILL.md` frontmatter for stricter packager compatibility;
- fixed SKILL pointers so Skeleton and Pattern selection come from their registries before Source evidence lookup;
- changed the Pattern target from a hard 3–7 quota to the **smallest coherent compatible set**;
- restored implementable AI recipes and shared UI physics without reintroducing React/shadcn assumptions;
- fixed the streaming-caret completion bug: completed responses remove/hide active caret state;
- demoted synthetic numeric composition scoring to qualitative ranking after authoritative hard rejects;
- split anti-slop guidance into hard failures and contextual heuristics rather than banning editorial conventions globally.

### Source-research / Host Contract pass

Selectively integrated the durable parts of Grok PR #3 without merging that review branch wholesale:

- formalized **Host Contract** as the output of Host Read, giving the pipeline `Host Read → Host Contract → Design Read → Skeleton → Pattern Set → Recipe → Adapter → Verify`;
- added typography and icon-system detection to Host Read so the host implementation vocabulary includes active type and icon conventions, not only components/tokens;
- allowed DESIGN.md-style structure only as a model-readable host-contract format; values must come from the current host rather than Linear, Stripe, Refero, or another catalog identity;
- made third-party design-contract identity substitution and an unjustified second icon family authoritative reject conditions;
- kept animated icons across repeated app chrome and two equally loud primary actions as **strong heuristics**, not universal hard failures;
- added host-neutral emphasis/action hierarchy and actionable empty/error/zero-data guidance to shared Physics;
- added tabular-number/layout-stability guidance without introducing a new Pattern or default animation dependency;
- strengthened provenance boundaries around public DESIGN.md catalogs, proprietary design methods, and unaffiliated plugins;
- added Refero Styles as design-contract methodology evidence, Number Flow as numeric-motion evidence, and Refactoring UI as proprietary methodology evidence;
- deliberately did **not** promote Component Gallery, screenshot galleries, icon-pack lists, or ambiguous same-name Motion Primitives sources into the canonical Source Registry;
- codified “shopping lists are not research”: a source-research pass must improve Host Read/Host Contract, Pattern/Recipe/Physics, provenance, or an Eval hypothesis rather than merely grow the registry.

### Validation

CI checks:

- strict portable Agent Skills frontmatter and install-name contract
- required `name` and `description` metadata
- SKILL.md progressive-disclosure line budget
- current OpenAI `agents/openai.yaml` interface metadata shape
- registry JSON Schema conformance and duplicate IDs
- Pattern evidence pointing to real Source IDs
- Skeleton recommendations pointing to real Pattern IDs
- known adapter IDs and valid density/motion ranges
- source verification metadata consistency and stale-verification warnings
- benchmark Fixture schema, Case references, and dependency-policy consistency
- Eval Result schema and Fixture/Case/Pattern/Skeleton references
- rubric component-sum consistency
- desktop/mobile artifact references for passed rendered runs

Source verification dates allow a one-day local-timezone/UTC skew so CI does not falsely reject a verification recorded just after local midnight; larger future-date errors still fail.

### Changed

- Updated `agents/openai.yaml` to the current `interface.display_name`, `short_description`, and `default_prompt` structure.
- Reframed `goals.md` around host-native composition and measurable decision quality.
- Reworked `taste-dials.md` into an optional Design Direction input layer instead of a copied external-skill workflow.
- Replaced `reverse-engineering.md` website/CSS fingerprint shopping with an **Observe → Evidence → Trait → Pattern → Provenance → Host adaptation → Verify** protocol.
- Replaced `sources.md` library shopping list with a source-evidence guide backed by the structured registry.
- Reworked `threeui.md` into a host-aware, provenance-safe WebGL evidence adapter with performance, fallback, accessibility, lifecycle, and tier/asset-boundary gates.
- Updated README to document Composition Intelligence, Recipe/Physics layers, Agent Skill validation, delivery gates, eval matrix, benchmark harness, observed-result protocol, and CI.

### Provenance verification

Verified and recorded canonical source/license metadata where authoritative evidence was available:

- shadcn/ui — MIT
- ReUI free/public catalog — MIT, with paid-catalog boundary recorded
- Kibo UI — MIT
- Vercel AI Elements — Apache-2.0
- Magic UI — MIT
- ThreeUI Community code and ThreeUI-authored Community assets — MIT, while external assets/fonts/Pro/Beta boundaries remain explicit
- taste-skill — MIT

Sources without sufficient authoritative evidence remain `verify-upstream` rather than being guessed into a copy-safe state. Refero Styles and Number Flow remain conservative `verify-upstream` entries until authoritative licensing is recorded; Refactoring UI is recorded as proprietary methodology evidence rather than copy-own source.

### Research policy

A research pass should no longer grow the canonical source list merely because a site looks interesting. It should improve at least one durable asset: Host Read / Host Contract, Source metadata, Pattern evidence/recipe, shared Physics, Skeleton evidence, provenance/risk guidance, or an Eval hypothesis.

### Next

- Finish and normalize the first rendered Eval 01 comparison before making measured-quality claims.
- Execute eval 02 next with the same build/screenshot/keyboard/reduced-motion/dependency evidence discipline.
- Record comparative results with the structured Eval Result schema.
- Continue canonical-URL/license verification for remaining `verify-upstream` source entries.
- Add adapters only when real eval failures demonstrate a host-integration gap.

## 0.2.0 — UI Compose architecture

### Changed

- Renamed the skill identity from `ui-lego` to `ui-compose`.
- Reframed the project from a block/library picker into a stack-aware UI composition engine.
- Replaced React/Tailwind/Radix assumptions with mandatory Host Read detection.
- Made external UI libraries reference/evidence sources rather than default runtime dependencies.
- Made sibling design-system skills optional instead of required.
- Added explicit fallback accessibility/responsive/state quality gates.
- Reworded AI "thinking" guidance to avoid implying access to hidden chain-of-thought.

### Added

- `references/host-read.md`
- stack adapters for React/Tailwind, Vue/Element Plus, Vue/UnoCSS, and generic CSS/design systems
- structured `references/sources/registry.yaml`
- `references/sources/provenance.md`
- `evals/rubric.md`

### Fixed

- Tilt glare example no longer relies on a missing Tailwind `group` parent.
- Editorial campaign example no longer mixes React JSX with Vue-only CSS `v-bind()`.
- Product-world selection explicitly supports click/tap as well as hover/focus.

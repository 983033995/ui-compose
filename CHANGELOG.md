# Changelog

## 0.3.0 — Composition Intelligence foundation

### Added

- `references/patterns/registry.yaml` for reusable product/UI decisions independent of source libraries.
- `references/skeletons/registry.yaml` for page-level composition structures.
- `references/composition-selection.md` for host-aware skeleton/pattern selection and risk filtering.
- `references/physics.md` for host-neutral fallback UI physics: timing, easing, type/measure, radius nesting, elevation, and AI-streaming behavior.
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

### Source research pass (2026-08-29)

Folded from public DESIGN.md / UI-kit threads without turning UI Compose into a kit picker:

- `refero-styles` as a methodology reference for model-readable DESIGN.md *shape*; values must come from Host Read, not from catalog product identities.
- `component-gallery` as inspiration-only host-diversity evidence (same job, different anatomy across design systems).
- `motion-primitives` (MIT) as a motion-reference for named, origin-aware verbs — reimplement on the host stack.
- `number-flow` (MIT) as evidence for layout-stable tabular number motion, recorded in `physics.md` rather than as a new Pattern.
- Provenance + composition-selection hard reject: ingesting a third-party DESIGN.md as the host identity; adding a second icon family or animated-icon kit on chrome.
- Explicit rejection of shopping-list sources (Cue, CollectUI, 21st.dev, shadcnstudio, React Bits, Fancy Components, Aceternity-as-new-row).
- `refactoring-ui` as a methodology reference (proprietary book + unaffiliated all-rights-reserved plugin). Host-neutral traits only: one primary per region, action hierarchy on host buttons, empty states with a next action. Do not vendor plugin files.
- `sixty-fps` as inspiration-only observed-motion evidence; brand-copy risk recorded.
- Host Read icon-set detection: reuse the existing family; animated icon kits are a second motion stack and default off on product chrome.
- Physics: emphasis + action hierarchy. Anti-slop: second icon family, two filled primaries in one region.

See `reviews/grok-2026-08-28-source-research.md` until those notes are folded and deleted.

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

Sources without sufficient authoritative evidence remain `verify-upstream` rather than being guessed into a copy-safe state.

### Research policy

A research pass should no longer grow the canonical source list merely because a site looks interesting. It should improve at least one durable asset: Source metadata, Pattern evidence/recipe, Skeleton evidence, provenance/risk guidance, or an Eval hypothesis.

### Next

- Build realistic executable fixture apps for the first high-information benchmark batch, especially eval 01 and 02.
- Execute real rendered benchmark outputs and capture build results, desktop/mobile screenshots, keyboard/reduced-motion notes, dependency diffs, and rubric scores.
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

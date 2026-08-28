# Changelog

## 0.3.0 — Composition Intelligence foundation

### Added

- `references/patterns/registry.yaml` for reusable product/UI decisions independent of source libraries.
- `references/skeletons/registry.yaml` for page-level composition structures.
- `references/composition-selection.md` for host-aware skeleton/pattern selection and risk filtering.
- JSON Schemas for Source, Pattern, Skeleton, and observed Eval Result records.
- `scripts/validate_registries.py` for schema and cross-reference validation.
- `scripts/validate_skill.py` for Agent Skills frontmatter/name/description checks, progressive-disclosure budget, and OpenAI UI metadata validation.
- `scripts/validate_evals.py` for observed benchmark record validation, case/pattern/skeleton references, rubric arithmetic, and rendered-artifact requirements.
- GitHub Actions workflow to run skill + registry + eval-result validation on pushes and pull requests.
- `DELIVERY.md` defining stable-release gates, hard blockers, and a 100-point project-readiness model.
- `evals/harness/README.md` defining a reproducible rendered-benchmark execution and capture protocol.
- `evals/results/README.md` defining how observed benchmark evidence, screenshots, build status, dependency diffs, and scores are stored without fabricating results.
- Repeatable eval case format plus a nine-case host/product diversity matrix:
  - Vue 3 + Element Plus order management
  - AI agent chat/tool/approval workflow
  - product settings
  - React + Tailwind/local-primitives data workspace
  - Vue + UnoCSS CRM
  - SaaS marketing landing
  - editorial product explorer
  - restrained WebGL hero
  - unfamiliar custom/internal design system
- Linear and Raycast as product-interaction evidence in the Source Registry.

### Validation

CI now checks:

- Agent Skills frontmatter and install-name contract
- required `name` and `description` metadata
- SKILL.md progressive-disclosure line budget
- current OpenAI `agents/openai.yaml` interface metadata shape
- registry JSON Schema conformance
- duplicate IDs
- Pattern evidence pointing to real Source IDs
- Skeleton recommendations pointing to real Pattern IDs
- known adapter IDs
- valid density/motion ranges
- source verification metadata consistency
- eval-result JSON Schema conformance
- Eval → Case / Pattern / Skeleton references
- rubric component-sum consistency
- desktop and mobile artifact references for runs marked `build_status: passed`

The combined Agent Skill + Registry + Eval Result validation workflow has completed successfully. Zero observed benchmark results are allowed during development, but that state is explicitly excluded from delivery-readiness evidence.

### Changed

- Updated `agents/openai.yaml` to the current `interface.display_name`, `short_description`, and `default_prompt` structure.
- Reframed `goals.md` around host-native composition and measurable decision quality.
- Reworked `taste-dials.md` into an optional Design Direction input layer instead of a copied external-skill workflow.
- Replaced `reverse-engineering.md` website/CSS fingerprint shopping with an **Observe → Evidence → Trait → Pattern → Provenance → Host adaptation → Verify** protocol.
- Replaced `sources.md` library shopping list with a source-evidence guide backed by the structured registry.
- Reworked `threeui.md` into a host-aware, provenance-safe WebGL evidence adapter with performance, fallback, accessibility, lifecycle, and tier/asset-boundary gates.
- Updated README to document Composition Intelligence, Agent Skill validation, current OpenAI metadata, the delivery gate, full eval matrix, benchmark harness, observed-result protocol, and CI.

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

A research pass should no longer grow the canonical source list merely because a site looks interesting. It should improve at least one durable asset: Source metadata, Pattern evidence, Skeleton evidence, provenance/risk guidance, or an Eval hypothesis.

### Next

- Build realistic host fixture contracts/apps for the first high-information benchmark batch: cases 01, 02, 04, and 09.
- Execute the first real rendered benchmark outputs and capture build results, desktop/mobile screenshots, keyboard/reduced-motion notes, dependency diffs, and rubric scores.
- Record comparative results with the structured Eval Result schema.
- Add robust source-freshness/link checks without making transient network failures a hard build failure.
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

# Changelog

## 0.3.0 — Composition Intelligence foundation

### Added

- `references/patterns/registry.yaml` for reusable product/UI decisions independent of source libraries.
- `references/skeletons/registry.yaml` for page-level composition structures.
- `references/composition-selection.md` for host-aware skeleton/pattern selection and risk filtering.
- JSON Schemas for Source, Pattern, and Skeleton registries.
- `scripts/validate_registries.py` for schema and cross-reference validation.
- GitHub Actions workflow to run registry validation on pushes and pull requests.
- Repeatable eval case format plus initial fixtures for:
  - Vue 3 + Element Plus order management
  - AI agent chat/tool/approval workflows
  - product settings
- Linear and Raycast as product-interaction evidence in the Source Registry.

### Validation

Registry validation now checks:

- schema conformance
- duplicate IDs
- Pattern evidence pointing to real Source IDs
- Skeleton recommendations pointing to real Pattern IDs
- known adapter IDs
- valid density/motion ranges
- source verification metadata consistency

The first GitHub Actions registry-validation run completed successfully.

### Changed

- Reframed `goals.md` around host-native composition and measurable decision quality.
- Reworked `taste-dials.md` into an optional Design Direction input layer instead of a copied external-skill workflow.
- Replaced `reverse-engineering.md` website/CSS fingerprint shopping with an Evidence → Trait → Pattern → Host-native implementation research protocol.
- Replaced `sources.md` library shopping list with a source-evidence guide backed by the structured registry.
- Reworked `threeui.md` into a host-aware, provenance-safe WebGL evidence adapter with performance, fallback, accessibility, and lifecycle gates.
- Updated README to document Composition Intelligence, validation, schemas, CI and initial evals.

### Research policy

A research pass should no longer grow the canonical source list merely because a site looks interesting. It should improve at least one durable asset: Source metadata, Pattern evidence, Skeleton evidence, provenance/risk guidance, or an Eval hypothesis.

### Next

- Run the first real benchmark outputs for the initial eval fixtures and capture screenshots/results.
- Add Agent Skills/frontmatter validation to CI after confirming the current validator contract.
- Add link/source-freshness checks without making network instability a hard build failure.
- Continue license/canonical-URL verification for `verify-upstream` source entries.
- Add adapters only when eval failures demonstrate a real host-integration gap.

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

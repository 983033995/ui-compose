# Source Provenance Policy

UI Compose learns from public UI libraries, products, demos, and agent skills, but it is not a repackaging layer for third-party source code.

## Four source modes

### 1. Methodology reference

Use ideas such as design-reading frameworks, density/motion controls, or evaluation heuristics. Do not copy prose wholesale.

### 2. Observed trait

Record behavior that can be independently reimplemented:

- hierarchy
- spacing rhythm
- motion duration/easing
- layout relationship
- interaction/state model
- density
- visual physics such as borders/radii/shadows

Observed traits should be expressed generically and implemented with host-native code.

### 3. Public copy-own source

Only copy source when the upstream project explicitly permits it and when copying is useful to the host architecture. Keep upstream license/attribution obligations intact.

### 4. Inspiration only

For proprietary, paid, unclear, or brand-heavy sources, use only high-level design/interaction insight. Do not reproduce protected assets, copy, illustrations, brand identity, or source code.

## Registry requirements

Every source in `registry.yaml` should eventually record:

- canonical URL
- source mode
- license or `verify-upstream`
- what UI Compose extracts
- whether source copying is permitted
- framework scope
- runtime dependency default
- known risks
- last verification date

## Important license rule

The MIT license of UI Compose applies to original material in this repository. It does **not** relicense third-party code, assets, trademarks, or proprietary designs.

## Brand boundary

Reference products are direction/evidence, not targets for cloning. A result should be recognizable as native to the host project, not as a disguised copy of Linear, Stripe, Notion, Apple, or any library showcase.

## Maintenance rule

When upstream terms or licenses are unclear, mark the source `verify-upstream` and default to **trait reimplementation** or **inspiration only** until verified.

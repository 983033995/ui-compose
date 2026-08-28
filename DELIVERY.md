# Delivery readiness

UI Compose is **delivery-ready** only when the project can demonstrate repeatable composition quality, host-stack discipline, provenance safety and maintainability. A large source catalog or polished README is not sufficient.

## Release gate

A stable release should satisfy all required gates below.

### 1. Skill contract

- `SKILL.md` has valid current Agent Skills metadata.
- Host Read is mandatory and no default framework/primitive kit leaks into the core contract.
- referenced files exist and progressive disclosure remains understandable.
- AI guidance does not imply access to hidden chain-of-thought.

### 2. Registry integrity

- Source, Pattern and Skeleton registries pass schema validation.
- no duplicate IDs.
- all Pattern evidence resolves to Source IDs.
- all Skeleton recommendations resolve to Pattern IDs.
- adapters use known IDs.
- canonical source metadata is present for every source promoted beyond provisional research status.

### 3. Provenance and dependency safety

- every canonical source has an explicit provenance mode.
- `verify-upstream` entries are not treated as copy-safe.
- proprietary product evidence is behavior/structure only.
- runtime dependency is never implied merely because a source provides evidence.
- trademark, paid-source and asset boundaries are documented where relevant.

### 4. Host diversity

At minimum, benchmark cases cover:

- Vue 3 + Element Plus
- Vue 3 + UnoCSS or another utility-first Vue host
- React + Tailwind/local primitives
- an existing/custom design system with no assumption of Tailwind or Radix

A Pattern that only works because one framework's component API is assumed is not yet framework-independent composition knowledge.

### 5. Product diversity

At minimum, benchmark cases cover:

- dense/data-heavy app interior
- settings/form workflow
- AI-native agent workflow
- marketing/landing surface
- expressive/editorial or WebGL surface

The skill must not optimize only for attractive landing pages or only for dashboards.

### 6. Rendered verification

For representative cases capture:

- desktop render
- ~390px mobile render
- loading/empty/error states where relevant
- keyboard/focus behavior
- reduced-motion notes
- build/runtime result
- dependency diff

Severe mobile overflow, inaccessible primary controls, broken builds or replacement of the host primitive system are hard failures.

### 7. Comparative eval

Run representative cases under the same host/task fixture in multiple modes when practical:

- model only
- generic frontend-design skill
- taste-oriented skill
- UI Compose
- taste-oriented skill + UI Compose

UI Compose does not need to win every visual-preference comparison. It should show consistent gains in composition choice, task fit, host compliance, dependency discipline and product-state coverage without regressing accessibility or runtime correctness.

### 8. CI and maintenance

Required checks must run automatically on pull requests.

Minimum stable-release CI:

- registry validation
- skill/frontmatter validation
- internal-reference/link sanity checks

Network-dependent source freshness checks should be informative or separately scheduled unless they are made robust against transient failures.

### 9. Documentation consistency

- README, SKILL, Goals, research protocol, adapters and registries describe the same architecture.
- no legacy `ui-lego` behavior remains except historical/rename notes.
- no canonical documentation says to “steal” a brand, default to shadcn, or install libraries before Host Read.

## Suggested maturity scoring

Use a 100-point project-readiness score separate from individual UI eval scores:

| Area | Weight |
| --- | ---: |
| Skill contract and architecture | 15 |
| Registry integrity | 15 |
| Provenance/license safety | 10 |
| Host diversity | 10 |
| Product diversity | 10 |
| Real rendered eval evidence | 20 |
| CI/automation | 10 |
| Documentation/maintenance | 10 |

Interpretation:

- **<70** — research/prototype
- **70–84** — usable beta
- **85–94** — release candidate
- **95–100** — delivery-ready, assuming no hard failures

A hard failure in build/runtime safety, primary accessibility, provenance, or host-system replacement blocks delivery-ready status regardless of numeric score.

## Current state

The architecture, registries, schema validation, initial CI and first eval contracts now exist. The largest remaining gap is **real rendered benchmark evidence**, followed by current Agent Skills validation and completion of source provenance verification.

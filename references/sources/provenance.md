# Source Provenance Policy

UI Compose learns from public UI libraries, products, demos, and agent skills, but it is not a repackaging layer for third-party source code.

## Four source modes

### 1. Methodology reference

Use ideas such as design-reading frameworks, density/motion controls, evaluation heuristics, or model-readable design-contract structure. Do not copy prose wholesale.

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

## DESIGN.md / model-readable design contracts

Public DESIGN.md catalogs are **methodology references**, not host identities.

Allowed:

- borrow the document shape: semantic color roles, type roles, spacing/radius/elevation, icon conventions, layout tracks, motion stack, and do/don't rules
- populate that shape from Host Read of the current repository
- point to existing host token/theme/design-system files instead of duplicating them

Not allowed:

- paste another product's DESIGN.md into the host as its visual identity
- treat a catalog entry as a skin or theme preset
- copy distinctive fonts, illustrations, product copy, brand tokens, or protected assets
- install a paid research MCP/skill as a UI Compose runtime dependency

Until authoritative licensing is recorded, keep catalog-style methodology sources `verify-upstream` and use only the abstract structure/traits.

## Books and unaffiliated plugins

Books, courses, and third-party plugins that encode proprietary design material are methodology references unless their own license clearly permits more.

Allowed:

- independently stated host-neutral traits such as clear primary-action hierarchy, grouping by proximity, spacing rhythm, functional elevation, and actionable empty states
- mapping those traits onto the host's existing primitives and tokens

Not allowed:

- copying proprietary book diagrams/prose into this repository
- vendoring unaffiliated plugin `SKILL.md` files merely because they summarize a book or design system
- assuming Tailwind/shadcn/React because the external plugin does

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

Substituting a third-party design contract for the host's own token/primitive identity is a brand-copy failure even when no source code was copied.

## Paid prompt catalogs

Libraries that sell or give away “copy this prompt into Lovable / Bolt / Cursor / Claude” packs (MotionSites, ScrollTide, motionprompts.dev, and similar) are **inspiration-only**. They are not Source Registry rows and not a Host Contract.

Allowed:

- extract a host-neutral motion *verb* already observed independently (scroll-scrubbed media, one ambient moment, poster fallback)
- use that verb only on the matching surface, implemented with the host motion stack

Not allowed:

- vendoring prompt text, paid blueprints, or leaked prompt dumps into this repository
- adopting the catalog's baked stack (typically React + Vite + Tailwind + Framer Motion + lucide) as if Host Read had found it
- treating cinematic scroll-video / liquid-glass / 3D-hero as the default landing for every product
- installing a prompt catalog, MCP, or unlimited-prompt SKU as a UI Compose runtime dependency

## Maintenance rule

When upstream terms or licenses are unclear, mark the source `verify-upstream` and default to **trait reimplementation** or **inspiration only** until verified.

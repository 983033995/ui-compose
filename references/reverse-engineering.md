# Reverse-engineering protocol

UI Compose studies proven interfaces to extract reusable decisions. The goal is not to copy a site, vendor its source, or reproduce its brand identity. Research should convert external evidence into implementation-independent patterns that can be re-expressed with the host project's own primitives and tokens.

## Research pipeline

Use this sequence:

**Observe → Record Evidence → Extract Trait → Map to Pattern → Check Provenance → Adapt to Host → Verify**

### 1. Observe

Inspect the interface at the level that matters for composition:

- region relationships and layout tracks
- information hierarchy and density
- control grouping
- keyboard and pointer interaction models
- loading, empty, error and approval states
- motion purpose, duration and spatial causality
- responsive behavior
- accessibility behavior

Do not start by copying CSS values.

### 2. Record evidence

For every external source, record only the facts that support a reusable decision:

```text
Source:
Surface/job:
Observed behavior:
Reusable trait:
Risk if copied literally:
License/provenance status:
Candidate Pattern ID:
```

The canonical source belongs in `references/sources/registry.yaml`.

### 3. Extract the trait

Convert brand-specific implementation into an independent design decision.

Examples:

```text
Linear Peek
→ preserve list context while inspecting detail
→ master-detail-preview

Display/view options
→ group/order/visibility behind one persistent control
→ view-options-control

AI tool card
→ expose tool identity + state + compact input/output + failure
→ ai-tool-execution-card
```

A trait should remain useful even when typography, colors, component library and framework change.

### 4. Map to a Pattern or Skeleton

Do not add a new registry item just because a source looks interesting.

Add or extend a Pattern only when the observation represents a repeatable product decision. Add a Skeleton only when it describes durable page-region relationships.

Prefer multiple independent sources supporting the same Pattern over one source producing many near-duplicate Pattern IDs.

### 5. Check provenance

Use `references/sources/provenance.md`.

Possible research modes:

- methodology reference
- observed trait
- public copy-own source
- inspiration only

Rules:

- unknown license → do not copy source
- proprietary product → observed behavior only
- trademarks, illustrations, copy and brand assets are never part of the reusable Pattern
- public source code remains under its upstream license
- `MIT` in this repository applies only to original UI Compose material

### 6. Adapt to the host

External sources provide evidence. The host project provides the implementation vocabulary.

Adapt in this order:

1. existing host component
2. existing host utility or primitive
3. small host-native reimplementation
4. copy-own upstream source only when license and architecture justify it
5. new dependency only when substantial behavior cannot reasonably be reproduced with the host stack

Never introduce a second button/input/dialog system simply because the reference source uses one.

## What to capture from different source types

### Product interfaces

Useful evidence:

- workflow structure
- navigation model
- preview/detail relationships
- keyboard model
- state visibility
- density and hierarchy

Do not reproduce brand styling.

### Component libraries

Useful evidence:

- compound component structure
- accessible control behavior
- data-heavy composition patterns
- primitive boundaries

Treat runtime installation as a separate architecture decision.

### Motion and effect libraries

Useful evidence:

- visible interaction verb
- duration/easing relationship
- origin and spatial causality
- reduced-motion strategy

Effects should not become page architecture.

### AI-native libraries and products

Useful evidence:

- streaming states
- tool execution lifecycle
- approvals
- source/context inspection
- composer behavior
- retry/cancel/error handling

Never imply access to hidden chain-of-thought. Use provider-exposed activity, progress or reasoning summaries only.

### Editorial and marketing sites

Useful evidence:

- section rhythm
- composition tracks
- content hierarchy
- controlled motif systems
- campaign-specific transitions

Avoid cloning logos, copy, product imagery, distinctive illustrations or signature brand identity.

## Promotion criteria

An observation should enter the Pattern Registry only when most of these are true:

- useful across more than one product or source
- independent of specific brand styling
- solves a recognizable user or product job
- can be implemented in multiple host stacks
- accessibility implications are understood
- mobile behavior can be described
- risks are explicit

If not, keep it as source research evidence rather than a canonical Pattern.

## Shopping lists are not research

A public thread of “best UI component libraries” is an input, not a Source Registry patch.

Worked example (2026-08-28):

```text
Aceternity          → already aceternity (inspiration-only, high-slop)
Cue / CollectUI     → no extractable host-neutral trait; promo / screenshot risk
21st.dev / shadcnstudio → duplicate shadcn + block-kit slop
React Bits / Fancy  → overlap magic-ui
Motion Primitives   → named motion verb; add as motion-reference, reimplement
Number Flow         → tabular number physics; not a Pattern
Component Gallery   → cross-system anatomy; inspiration-only
Refero DESIGN.md    → methodology for host DESIGN.md shape; never paste product identity
```

Only the last four improved a durable asset. The rest stayed out.

## Research quality bar

Good reverse-engineering produces statements like:

> Preserve collection context while letting the user inspect adjacent records using keyboard next/previous navigation.

Poor reverse-engineering produces statements like:

> Copy this panel's exact shadow, font, gradient and radius.

The first becomes durable composition intelligence. The second becomes a visual clone.

## Output of a research pass

A useful research pass should end with some combination of:

- Source Registry update
- new evidence for an existing Pattern
- a justified new Pattern or Skeleton candidate
- risk/provenance note
- Eval case or failure hypothesis

Research that only increases the list of websites without improving one of those assets should not be merged.

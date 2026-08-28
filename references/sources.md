# Source evidence guide

UI Compose does not maintain a shopping list of UI libraries to install. External products, component libraries, motion catalogs, design methods and campaign sites are **evidence sources** for reusable composition decisions.

The machine-readable source of truth is:

- [`sources/registry.yaml`](sources/registry.yaml) — source identity, role, framework, traits, integration mode, license/provenance status and risks
- [`sources/provenance.md`](sources/provenance.md) — what can be observed, reimplemented, copied or only used as inspiration
- [`patterns/registry.yaml`](patterns/registry.yaml) — reusable decisions extracted from one or more sources
- [`skeletons/registry.yaml`](skeletons/registry.yaml) — page-level composition structures
- [`reverse-engineering.md`](reverse-engineering.md) — research protocol

## Source roles

A source may contribute evidence in one or more roles:

| Role | Useful evidence |
| --- | --- |
| Product interface | workflow, density, hierarchy, keyboard model, state visibility |
| Component/composition library | compound structure, accessible behavior, reusable product patterns |
| AI-native UI | streaming, tool lifecycle, approvals, source/context inspection, composer states |
| Motion/effect catalog | interaction verbs, duration/easing relationships, spatial causality, reduced-motion strategy |
| Marketing/editorial site | tracks, section rhythm, motif discipline, expressive transitions |
| Design methodology | design-read process, constraints, evaluation heuristics |
| 3D/WebGL catalog | scene roles, progressive enhancement, performance/disposal practices |

## Selection rule

Do not select a source first and then force its components into the project.

Use this order:

```text
Product job
→ Host Read
→ Skeleton
→ Pattern needs
→ Source evidence when useful
→ Host-native implementation
```

A source can support a Pattern without becoming a runtime dependency.

## Dependency discipline

When a useful source suggests an implementation, choose in this order:

1. existing host component
2. existing host utility or primitive
3. small host-native reimplementation of the observed trait
4. copy-own upstream source only when license and architecture justify it
5. new dependency only when meaningful behavior cannot reasonably be reproduced with the host stack

There is no universal default primitive kit. If the host already uses Element Plus, Ant Design, a local design system, Base UI, Radix, native HTML controls, or another established system, that system remains the implementation vocabulary unless the task explicitly calls for migration.

## Evidence quality

Good evidence describes durable decisions:

- preserve list context while inspecting detail
- expose active filter state near the data it affects
- group ordering/visibility controls behind one display-options surface
- make tool execution state inspectable without showing raw payloads by default
- keep a persistent composer reachable while the mobile keyboard is open
- use one ambient visual moment rather than decorating every surface

Weak evidence is mostly visual fingerprinting:

- exact shadow values
- a brand's font pair
- a proprietary illustration style
- copied marketing copy
- a distinctive gradient or logo treatment

Those details should not become canonical Patterns.

## Adding a new source

Before adding a source to the registry, answer:

1. What product decision does it teach?
2. Does that decision already exist as a Pattern?
3. Does it add independent evidence or merely duplicate another source?
4. What is the provenance/license mode?
5. Is runtime dependency actually justified?
6. What risks should an agent know about?

If the only reason is “the site looks cool,” keep researching until a reusable decision can be stated.

## AI-specific rule

AI sources may expose activity, progress, summarized reasoning, tool execution, approval and source/context state. UI Compose must never claim that hidden chain-of-thought is available or fabricate execution steps that the provider did not expose.

## Research output

Every meaningful source-research pass should improve at least one durable asset:

- Source Registry metadata
- Pattern evidence
- Skeleton evidence
- risk/provenance guidance
- Eval case or failure hypothesis

Otherwise the research should not increase the canonical knowledge base.

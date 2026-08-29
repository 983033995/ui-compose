# Composition selection

UI Compose should choose the smallest coherent set of patterns from host constraints and task intent. Do not treat selection as a library popularity contest.

## Inputs

Collect these from Host Read + Design Read:

- surface: app-interior | ai-native | marketing | campaign
- jobs: search, filter, edit, approve, compare, stream, tool-use, etc.
- host framework/component system
- host token, typography, and icon systems
- density target
- motion target
- mobile/touch constraints
- accessibility constraints
- SSR/hydration constraints
- dependency budget
- positive and negative references

## Selection pipeline

1. **Filter skeletons by surface + jobs.**
2. **Pick one primary skeleton.** Prefer the simplest skeleton that satisfies the task.
3. **Load recommended patterns** from that skeleton.
4. **Add only the extra patterns** needed for missing jobs or required states.
5. **Reject patterns** that require a competing primitive/icon system, violate host constraints, or primarily copy source identity.
6. **Load host-neutral recipes** for the selected canonical patterns from `patterns/recipes.md` when available.
7. **Adapt the selected set** to the host stack and Host Contract.
8. **Verify rendered behavior** before adding decorative patterns.

Target the **smallest sufficient set**. Complex product surfaces often land around 3–7 patterns, but specialized surfaces may need only 1–2. Never pad a composition with irrelevant patterns to satisfy a numeric quota.

## Hard rejects (authoritative)

These override any ranking hint:

- wrong surface => reject
- inaccessible primary interaction => reject
- requires replacing the host primitive system without justification => reject
- substitutes a third-party DESIGN.md/catalog skin for the host identity => reject
- adds a second icon family without a strong host/product reason => reject
- brand-copy strategy => reject
- unjustified dependency with no substantial behavioral need => reject
- mobile-breaking layout for a mobile-required task => reject
- prompt-catalog / template-pack default stack replacing the detected host => reject
- cinematic scroll-tied media or WebGL hero on an app-interior surface => reject

Animated icons across repeated product chrome are a **strong risk heuristic**, not an absolute ban. Require a clear interaction or brand reason and a reduced-motion path.

Two equally loud filled primary actions in one region are also a **hierarchy warning**, not an automatic reject. Peer decisions such as Approve/Reject may justify it.

## Ranking hint (optional)

When several candidates all pass the hard gates, rank them qualitatively rather than pretending to compute precise scores.

Useful dimensions:

- job match
- surface match
- host compatibility
- density alignment
- motion alignment
- state coverage
- dependency cost
- accessibility risk
- mobile risk
- slop risk
- brand-copy risk
- host-identity substitution risk

Use labels such as **strong match / acceptable / weak match / reject**. Do not report a synthetic numeric confidence score unless a real eval system computes it.

## Composition budget

More patterns do not mean a better design.

- 1 primary skeleton
- smallest sufficient functional pattern set
- 0–1 ambient/decorative pattern family
- 0 competing primitive kits by default
- 0 second icon families by default
- 0 new motion dependencies for simple opacity/transform transitions

If two patterns solve the same job, keep the one with better host fit and lower risk.

## Example: Vue + Element Plus B2B order management

Input:

```text
surface: app-interior
jobs: search, filter, browse, inspect, bulk-action
density: 8
motion: 1
host: Vue 3 + Element Plus
mobile: required
```

Selection:

```text
skeleton: master-detail-workspace
patterns:
  - dense-filter-toolbar
  - master-detail-preview
  - view-options-control
  - sticky-contextual-actions
adapter: vue-element-plus
new UI dependencies: none
```

Implementation consequence: preserve Element Plus behavioral primitives and icon conventions, improve composition around them, and use route/sheet fallback on mobile instead of forcing a desktop split pane.

Rejected: Aceternity/MotionSites cinematic scroll-video, Framer Motion, a second icon family, `immersive-hero`. Wrong surface + prompt-catalog stack.

## Example: B2B SaaS marketing landing

Input:

```text
surface: marketing
jobs: value-prop, proof, workflow-explain, trust, cta
density: 3
motion: 3
host: existing product tokens + button/link primitives (framework unspecified)
```

Selection:

```text
skeleton: marketing-proof-landing
patterns:
  - single-ambient-moment
adapter: host primitives
new UI dependencies: none
```

Rejected: `immersive-hero` + scroll-tied 300-frame video + Framer Motion. Eval 06 asks for restrained proof, not a prompt-catalog cinematic. Upgrade to scroll-scrubbed media only when the brief's product demo *is* the media and Host Read has a motion stack that can bind scroll without a new library.

## Example: AI agent task runner

Input:

```text
surface: ai-native
jobs: progress, tool-use, approval, output
density: 7
motion: 1
```

Selection:

```text
skeleton: agent-task-workspace
patterns:
  - ai-activity-summary
  - ai-tool-execution-card
  - human-approval-gate
```

Never fabricate hidden reasoning. Activity or reasoning UI must show only provider-exposed summaries, tool events, or product-owned progress states.

## Evidence vs implementation

Pattern evidence may come from Linear, Raycast, AI Elements, ReUI, Kibo, or other products. Evidence means a product demonstrates a useful interaction or structural decision. It does not mean UI Compose should clone markup, CSS, assets, copy, or brand identity.

A useful observed example is Linear's Peek model: focused list items can be previewed without fully navigating away, while keyboard movement updates the preview. Treat that as evidence for `master-detail-preview`, not as a mandate to reproduce Linear's exact UI.

Public DESIGN.md catalogs are evidence for how a model-readable host contract can be structured. Their values are not implementation input unless they were independently observed in the current host.

## Decision log

For non-trivial work, leave a concise internal decision summary:

```text
Skeleton: master-detail-workspace
Patterns: dense-filter-toolbar, master-detail-preview, sticky-contextual-actions
Why: high-frequency B2B browse/edit flow, high density, low motion
Rejected: animated card grid (slop risk), second primitive/icon kit (host-system cost)
Adapter: Vue + Element Plus
Verification focus: mobile detail flow, keyboard focus, bulk selection state
```

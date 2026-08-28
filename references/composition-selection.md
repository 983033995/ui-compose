# Composition selection

UI Compose should choose a small coherent set of patterns from host constraints and task intent. Do not treat selection as a library popularity contest.

## Inputs

Collect these from Host Read + Design Read:

- surface: app-interior | ai-native | marketing | campaign
- jobs: search, filter, edit, approve, compare, stream, tool-use, etc.
- host framework/component system
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
4. **Add at most the few extra patterns** needed for missing jobs or states.
5. **Reject patterns** that require a competing primitive system, violate host constraints, or primarily copy source identity.
6. **Adapt the selected set** to the host stack.
7. **Verify rendered behavior** before adding decorative patterns.

Default target: one skeleton + roughly 3–7 patterns.

## Heuristic score

Do not imply false mathematical precision. Use the score only to rank close candidates.

```text
score =
  + job_match * 5
  + surface_match * 4
  + host_compatibility * 4
  + density_alignment * 2
  + motion_alignment * 1
  + state_coverage * 2
  - dependency_cost * 4
  - accessibility_risk * 4
  - mobile_risk * 3
  - slop_risk * 3
  - brand_copy_risk * 5
```

Required gates override score:

- wrong surface => reject
- inaccessible primary interaction => reject
- requires replacing the host primitive system without justification => reject
- brand-copy strategy => reject
- mobile-breaking layout for a mobile-required task => reject

## Composition budget

More patterns do not mean a better design.

- 1 skeleton
- 3–7 functional patterns
- 0–1 ambient/decorative pattern family
- 0 competing primitive kits by default
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

Implementation consequence: preserve Element Plus behavioral primitives, improve composition around them, and use route/sheet fallback on mobile instead of forcing a desktop split pane.

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
  - sticky-contextual-actions
```

Never fabricate hidden reasoning. Activity or reasoning UI must show only provider-exposed summaries, tool events, or product-owned progress states.

## Evidence vs implementation

Pattern evidence may come from Linear, Raycast, AI Elements, ReUI, Kibo, or other products. Evidence means the product demonstrates a useful interaction or structural decision. It does not mean UI Compose should clone markup, CSS, assets, copy, or brand identity.

A useful observed example is Linear's Peek model: focused list items can be previewed without fully navigating away, while keyboard movement updates the preview. Treat that as evidence for the `master-detail-preview` interaction, not as a mandate to reproduce Linear's exact UI.

## Decision log

For non-trivial work, leave a concise internal decision summary:

```text
Skeleton: master-detail-workspace
Patterns: dense-filter-toolbar, master-detail-preview, sticky-contextual-actions
Why: high-frequency B2B browse/edit flow, high density, low motion
Rejected: animated card grid (slop risk), second primitive kit (dependency cost)
Adapter: Vue + Element Plus
Verification focus: mobile detail flow, keyboard focus, bulk selection state
```

# Adapter: Generic CSS / Existing Design System

Use this adapter when no framework-specific adapter matches or when the host already has a mature internal design system.

## Default stance

The existing product system wins.

Do not introduce a public UI library simply because a reference pattern came from one. Extract the relationship and behavior, then implement it with the host's existing DOM/components and CSS conventions.

## Translation checklist

For each selected pattern, separate:

- **structure** — hierarchy, grid, sticky/fixed regions, responsive order
- **tokens** — color roles, spacing, radius, type, borders, shadows
- **interaction** — focus, hover, selection, open/close, keyboard
- **motion** — duration, easing, transform, reduced-motion behavior
- **states** — loading, empty, error, disabled, success

Map each concern to the closest host primitive/token.

## CSS rules

- prefer semantic custom properties already present;
- preserve cascade/layer conventions;
- avoid global selectors for one-off composition fixes;
- use container/media queries consistent with the host;
- do not reproduce a reference's exact brand colors/type treatment;
- keep motion CSS small and interruptible.

## New primitive threshold

Create a new local primitive only if the pattern appears more than once or encodes meaningful product behavior. Otherwise keep the implementation local to the surface.

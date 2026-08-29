# ThreeUI / WebGL evidence adapter

ThreeUI is a useful research source for a narrow job: **one intentional 3D/WebGL moment** such as a hero scene, product stage, shader field, or generative visual mark.

It is not a default dependency, a primitive kit, or a reason to put GPU effects inside ordinary product UI.

## Source boundary

Canonical sources should be recorded in `references/sources/registry.yaml` and verified before source-level reuse.

Treat ThreeUI in one of two modes:

1. **Observed-trait evidence** — learn scene composition, DOM/canvas layering, performance constraints, reduced-motion behavior, and visual restraint.
2. **Copy-own upstream source** — only when the exact upstream item/license permits it and the host architecture benefits from reuse.

Do not assume that every site asset, thumbnail, paid component, MCP result, or Pro implementation is covered by the Community license. Verify the exact item before copying source.

## When this pattern is eligible

Use WebGL only when the product job explicitly benefits from a scene:

- marketing hero
- 3D product presentation
- generative brand mark
- immersive editorial stage
- shader-backed visualization

Usually reject it for:

- dashboards
- tables
- settings
- forms
- chat threads
- CRUD workspaces
- high-frequency navigation

The Pattern Registry owns the canonical decision: `single-webgl-stage`.

## Host Read first

Before introducing any WebGL implementation, inspect:

- whether Three.js or another renderer already exists
- framework and lifecycle model
- existing motion stack
- route/view mounting behavior
- performance budget
- SSR/hydration constraints
- mobile requirements
- reduced-motion expectations
- existing visual/brand system

A React/Three.js example is evidence, not a portable implementation for a Vue, Svelte, native-canvas, or custom-renderer host.

## Composition rule

One GPU scene should normally correspond to one visual responsibility.

```text
real HTML chrome
  ↓
accessible heading / copy / CTA / navigation
  ↓
canvas scene as progressive visual layer
```

The page must remain understandable and operable if the canvas fails or is removed.

Do not put essential text, forms, navigation, approvals, or primary product controls exclusively inside the canvas.

## Adaptation order

1. Reuse an existing host scene/renderer if one already solves the job.
2. Reimplement a small observed trait using the host renderer.
3. Reuse a permitted upstream Community item when license and architecture justify it.
4. Add a new renderer/dependency only when the interaction genuinely requires it.

Do not add Three.js just to reproduce grain, a glow, a simple orb, a gradient, or a basic text reveal that CSS/canvas-2D can handle.

## Performance contract

Any `single-webgl-stage` implementation should address:

- device pixel ratio cap where appropriate
- resize handling
- off-screen pause or throttling
- animation frame cleanup
- geometry/material/texture disposal where the renderer requires it
- listener cleanup
- lower-cost mobile behavior
- graceful WebGL failure
- reduced-motion fallback, ideally a still poster or static state

SPA route changes are part of the test. A scene that leaks renderer resources is a product bug, not merely a performance optimization opportunity.

## Interaction contract

Background canvas should usually use no pointer capture so HTML controls remain operable.

Enable direct canvas input only when the scene itself is the intended control, for example:

- product orbit viewer
- interactive 3D configurator
- deliberately interactive hero stage

Keyboard and screen-reader access must remain available for any equivalent product action.

## Visual restraint

A WebGL scene is already a high-salience motif. Do not stack it with several unrelated decorative systems such as particles, glow beams, cursor trails, animated grids and multiple ambient orbs.

Prefer:

> one scene + restrained host-native chrome

rather than:

> one scene + every motion/effect library discovered during research

## What to extract from ThreeUI-like sources

Good reusable evidence includes:

- one GPU stage per view
- DOM chrome above/beside canvas
- progressive scene readiness
- reduced-motion/static fallback
- renderer cleanup discipline
- interaction-specific pointer capture
- scene/job matching

Brand-specific fonts, exact palettes, thumbnails, proprietary assets and paid-source implementations should not become canonical UI Compose patterns.

## Eval failures

Treat these as significant failures:

- WebGL added to an app interior without product justification
- new heavyweight renderer for a CSS-level effect
- essential content inaccessible without canvas
- no reduced-motion/failure fallback
- resource leak across route mounts
- mobile frame cost ignored
- multiple high-salience decorative systems competing in one view
- copied source without verified permission

## Agent move

1. Confirm the user/product job actually needs a 3D scene.
2. Perform Host Read.
3. Select `single-webgl-stage` only if it survives dependency/performance/accessibility risk checks.
4. Use ThreeUI or similar projects as evidence; verify license before source reuse.
5. Keep meaningful UI in the DOM.
6. Verify mobile, reduced motion, failure fallback and lifecycle cleanup.

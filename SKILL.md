---
name: ui-compose
description: >
  Stack-aware UI composition skill for coding agents. Detect the host frontend
  stack and design system first, then compose proven layout, interaction, motion,
  and AI-native patterns without directly depending on or cloning popular UI
  libraries. Use for dashboards, app interiors, landing pages, AI interfaces,
  product explorers, redesigns, and frontend polish when the result must feel
  intentional rather than generic or "AI slop".
license: MIT
metadata:
  short-description: "Stack-aware UI composition engine for coding agents"
---

# UI Compose

UI Compose is a **composition engine**, not a component library and not a
license to install every popular UI kit.

Works with React, Vue, Svelte, Tailwind, UnoCSS, CSS/SCSS, and existing design
systems through adapter guidance. The core contract is framework-agnostic.

The goal is to extract the *useful traits* of proven interfaces — information
architecture, layout tracks, density, interaction models, motion physics,
state patterns, and AI-native primitives — and re-express them using the host
project's existing framework, tokens, components, and conventions.

> Taste decides the direction. UI Compose decides how to build it.

## Core contract

Do not begin by choosing a library. Begin by understanding the host.

**Host Read → Design Read → Skeleton → Pattern Set → Adapter → Verify**

Read references only when needed:

- `references/host-read.md` — framework/design-system detection protocol
- `references/skeletons/registry.yaml` — page-level region relationships
- `references/patterns/registry.yaml` — reusable product/UI decisions
- `references/composition-selection.md` — host-aware skeleton/pattern selection
- `references/adapters/` — stack-specific integration
- `references/physics.md` — shared motion/type/radius defaults
- `references/layout-steal.md` — human expansion of skeletons
- `references/ai-primitives.md` — AI-native UI states and recipes
- `references/motion-blocks.md` — distinctive motion recipes
- `references/sources/registry.yaml` — evidence sources and provenance
- `references/sources/provenance.md` — license boundaries
- `references/goals.md` — goals, non-goals, principles
- `evals/rubric.md` — quality rubric

Do not inline the registries up front. Look up the chosen skeleton and the
3–7 pattern IDs after Host Read and Design Read.

---

## 0. Host Read — mandatory before design decisions

Before changing UI, inspect the repository and state the host contract in a
short internal note:

1. **Framework/runtime** — React, Vue, Svelte, Nuxt, Next, Vite, etc.
2. **Styling system** — Tailwind, UnoCSS, CSS Modules, SCSS, CSS-in-JS, plain CSS.
3. **Primitive/component system** — shadcn/Radix, Element Plus, Ant Design,
   Base UI, custom design system, or none.
4. **Existing tokens** — colors, spacing, radius, typography, shadows, z-index.
5. **Motion stack** — CSS only, Motion/Framer Motion, Vue transitions, GSAP, none.
6. **Existing product patterns** — shell, cards, forms, tables, dialogs, loading,
   error/empty states, mobile behavior.
7. **Constraints** — browser targets, accessibility rules, bundle budget,
   SSR/hydration, mobile/touch, existing architecture.

Never assume React, Tailwind, Radix, or `src/styles.css`.

If an existing design system exists, **adapt to it**. Do not install a second
button/input/modal system merely because a reference library contains a good
pattern.

If no design-system skill is available, enforce the fallback quality gates in
§8 yourself.

---

## 1. Design Read

Write one concise interpretation before implementation:

> Reading this as: `<surface>` for `<audience>`, `<vibe>`, leaning toward
> `<design direction>`.

Then set three dials from `references/taste-dials.md`:

- `VARIANCE` — visual novelty / composition asymmetry
- `MOTION` — amount and prominence of movement
- `DENSITY` — information density and spacing compression

Treat values as directional, not a universal preset. Product interiors are
usually denser and calmer than campaigns/marketing pages.

Pick:

- one **positive reference**: the interaction/layout feel to learn from;
- one **negative reference**: the slop/tells to avoid.

Do not clone brand identity, copy, illustrations, or proprietary source.

---

## 2. Choose a skeleton before styling

Pick **one** skeleton from `references/skeletons/registry.yaml`. Use
`references/layout-steal.md` only as the human expansion of that ID.

Examples:

- `master-detail-workspace`
- `data-workspace`
- `settings-workspace`
- `agent-chat-workspace`
- `agent-task-workspace`
- `marketing-proof-landing`
- `editorial-product-explorer`
- `immersive-hero`

Steal **tracks and relationships**, not pixels:

- max-width strategy
- grid/flex regions
- hierarchy
- gutters
- sticky/fixed regions
- list/detail relationships
- mobile collapse order

The skeleton should make the page coherent before color, animation, or visual
ornament is added.

---

## 3. Compose traits, not libraries

Select roughly 3–7 **pattern IDs** from `references/patterns/registry.yaml`
using `references/composition-selection.md`. Start from the skeleton's
`recommended_patterns`, then add only what the job still lacks.

Hard rejects beat any ranking hint: wrong surface, replacing the host
primitive system, inaccessible primary interaction, brand-copy, or a
mobile-breaking layout on a mobile-required task.

Popular libraries are evidence for a pattern, not default runtime
dependencies. Consult `references/sources/registry.yaml` only after pattern
IDs are chosen, and only to check provenance / integration mode.

### Dependency rule

Prefer this order:

1. existing host component
2. existing host utility / primitive
3. reimplement a small observed pattern using host primitives
4. copy-own source **only when license and architecture make it appropriate**
5. add a dependency only when its behavior is substantial enough to justify it

Do not mix competing primitive systems in one surface unless the repository
already does so intentionally.

---

## 4. Adapt to the host stack

Use the closest adapter in `references/adapters/`.

Adapters do not redefine the visual direction. They translate a selected
pattern into the host's implementation vocabulary.

Current adapter baseline:

- `react-tailwind.md`
- `vue-element-plus.md`
- `vue-unocss.md`
- `generic-css.md`

If no exact adapter exists, follow the generic rules:

- keep existing component APIs
- map colors/space/radius/type to existing tokens
- use existing responsive conventions
- preserve form semantics and validation behavior
- preserve SSR/hydration constraints
- reuse current icon set
- avoid new runtime dependencies for purely visual effects

---

## 5. Anti-slop hard fails

Rewrite the surface before calling it done if it exhibits these generic tells
without a deliberate product reason:

- random aurora/mesh/AI-purple decoration on app chrome
- glassmorphism on every panel
- rainbow borders / neon glow without brand rationale
- emoji used as product UI icons
- ad-hoc spacing that bypasses the host scale (`p-[13px]`, `gap-[17px]`)
- identical radius everywhere regardless of nesting
- Inter-everywhere with no weight/size hierarchy
- floating elements with no shared grid/gutter logic
- lorem/placeholder boxes in a finished view
- animation on every click or keyboard action
- `transition: all`
- em-dash in UI copy; numbered eyebrows (`001 · Capabilities`)
- "Live" badges or shimmer on static text
- purple/violet as the silent brand accent
- fake dashboards/screenshots built from decorative rectangles
- three equal marketing cards simply because the model needs a section
- copied visual identity from a reference product

Campaign/editorial surfaces can be more expressive, but must still use one
coherent motif family rather than an effect sampler.

Shared defaults for time, radius, type, and streaming: `references/physics.md`.

---

## 6. Motion policy

Motion explains state, hierarchy, causality, or spatial change. Otherwise,
delete it.

- high-frequency / keyboard-driven interactions: usually instant
- hover/focus/open/close: prefer CSS transitions when sufficient
- general UI motion: usually ≤ 300ms
- enter may be slightly slower than exit
- avoid `scale(0)` for ordinary UI
- animations must be interruptible where repeated interaction is possible
- always provide a `prefers-reduced-motion` path
- do not add a motion library only to animate opacity/translate

Use `references/motion-blocks.md` for distinctive recipes.

---

## 7. AI-native surfaces

For model/agent products, do not reduce the experience to "chat bubbles +
spinner". Compose explicit states for:

- streaming response
- progress/activity summary
- tool invocation status
- approval / human decision gate
- sources/context
- composer state
- retry/error/cancel
- queued/running/success/failed task states

Do **not** imply that hidden chain-of-thought is available. UI labels such as
"Thinking trace" should represent only provider-exposed progress, summarized
reasoning, or tool/activity traces. Prefer names like **Activity**, **Progress**,
**Execution trace**, or **Reasoning summary** when appropriate.

See `references/ai-primitives.md`. Use the host-neutral recipes there; map
colors and radii to host tokens.

---

## 8. Fallback quality gates

Even when there is no sibling design skill, every finished implementation must
pass these minimum gates:

- semantic HTML / correct native controls where applicable
- keyboard reachable and operable
- visible focus state
- accessible names/labels
- sufficient contrast
- reduced-motion support
- touch targets appropriate for mobile usage
- no accidental horizontal overflow
- responsive hierarchy, not merely shrinking desktop
- loading, empty, error, disabled, and success states where the flow requires them
- host tokens/conventions reused instead of creating an untracked parallel theme

---

## 9. Verification

Never finish from source inspection alone.

Verify in the real rendered environment when tooling allows:

1. desktop target width
2. ~390px mobile width
3. keyboard navigation
4. hover/focus/active/disabled states
5. loading/empty/error states
6. reduced motion
7. console/hydration errors
8. overflow and layout jumps

Then compare the result against the chosen positive and negative references:

- Did we inherit useful structure/behavior?
- Did we accidentally inherit brand identity or source-specific gimmicks?
- Does the result still look native to the host project?

---

## Finish checklist

- [ ] Host Read completed; no framework/library was assumed
- [ ] Design Read + V/M/D direction declared
- [ ] One skeleton ID chosen from the skeleton registry before styling
- [ ] 3–7 pattern IDs selected from the pattern registry; sources used as evidence only
- [ ] Existing host component/token system preserved
- [ ] No competing primitive kit added without a strong reason
- [ ] Anti-slop hard fails removed
- [ ] Motion passes purpose/frequency/reduced-motion tests
- [ ] AI UI exposes activity summaries, not hidden chain-of-thought
- [ ] Accessibility/responsive/state gates pass
- [ ] Rendered result verified in-browser when possible

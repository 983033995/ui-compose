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

UI Compose is a **composition engine**, not a component library and not a license to install every popular UI kit.

Works with React, Vue, Svelte, Tailwind, UnoCSS, CSS/SCSS, and existing design systems through adapter guidance. The core contract is framework-agnostic.

The goal is to extract useful traits of proven interfaces — information architecture, layout tracks, density, interaction models, motion physics, state patterns, and AI-native primitives — and re-express them using the host project's existing framework, tokens, components, icons, and conventions.

> Taste decides the direction. UI Compose decides how to build it.

## Core contract

Do not begin by choosing a library. Begin by understanding the host.

**Host Read → Host Contract → Design Read → Skeleton → Pattern Set → Recipe → Adapter → Verify**

`Host Contract` is the compact internal representation produced by Host Read. It may be a short note, structured object, or DESIGN.md-shaped summary; do not create a new file unless the task actually benefits from one.

Read references only when needed:

- `references/host-read.md` — framework/design-system detection protocol and Host Contract shape
- `references/skeletons/registry.yaml` — page-level region relationships
- `references/patterns/registry.yaml` — reusable product/UI decisions
- `references/patterns/recipes.md` — host-neutral implementation recipes for canonical patterns
- `references/composition-selection.md` — host-aware skeleton/pattern selection
- `references/adapters/` — stack-specific integration
- `references/physics.md` — shared motion/type/radius/action-hierarchy defaults
- `references/layout-steal.md` — human expansion of skeletons
- `references/ai-primitives.md` — AI-native UI states and recipes
- `references/motion-blocks.md` — distinctive motion recipes
- `references/sources/registry.yaml` — evidence sources and provenance
- `references/sources/provenance.md` — license boundaries
- `references/goals.md` — goals, non-goals, principles
- `evals/rubric.md` — quality rubric

Do not inline registries up front. Look up the chosen skeleton and only the compatible pattern IDs needed for the task after Host Read and Design Read.

---

## 0. Host Read — mandatory before design decisions

Before changing UI, inspect the repository and state the host contract in a short internal note:

1. **Framework/runtime** — React, Vue, Svelte, Nuxt, Next, Vite, etc.
2. **Styling system** — Tailwind, UnoCSS, CSS Modules, SCSS, CSS-in-JS, plain CSS.
3. **Primitive/component system** — shadcn/Radix, Element Plus, Ant Design, Base UI, custom design system, or none.
4. **Existing tokens** — colors, spacing, radius, typography, shadows, z-index.
5. **Typography roles** — active font stack, body/meta/title sizes and weight hierarchy.
6. **Icon system** — existing package/SVG convention, stroke/fill family, size roles.
7. **Motion stack** — CSS only, Motion/Framer Motion, Vue transitions, GSAP, none.
8. **Existing product patterns** — shell, cards, forms, tables, dialogs, loading, error/empty states, mobile behavior.
9. **Constraints** — browser targets, accessibility rules, bundle budget, SSR/hydration, mobile/touch, existing architecture.

Never assume React, Tailwind, Radix, or `src/styles.css`.

If an existing design system exists, **adapt to it**. Do not install a second button/input/modal system merely because a reference library contains a good pattern. Do not add a second icon family merely because a reference screenshot uses one.

If a model-readable design contract helps later steps, derive its **shape** from general conventions but derive its **values** from Host Read. Never paste a Linear, Stripe, Refero, or other external DESIGN.md/catalog identity into the project as if it were the host design system.

If no design-system skill is available, enforce the fallback quality gates in §8 yourself.

---

## 1. Design Read

Write one concise interpretation before implementation:

> Reading this as: `<surface>` for `<audience>`, `<vibe>`, leaning toward `<design direction>`.

Then set three dials from `references/taste-dials.md`:

- `VARIANCE` — visual novelty / composition asymmetry
- `MOTION` — amount and prominence of movement
- `DENSITY` — information density and spacing compression

Treat values as directional, not a universal preset. Product interiors are usually denser and calmer than campaigns/marketing pages.

Pick one positive reference and one negative reference. Do not clone brand identity, copy, illustrations, or proprietary source.

---

## 2. Choose a skeleton before styling

Pick **one** skeleton from `references/skeletons/registry.yaml`. Use `references/layout-steal.md` only as the human expansion of that ID.

Examples:

- `master-detail-workspace`
- `data-workspace`
- `settings-workspace`
- `agent-chat-workspace`
- `agent-task-workspace`
- `marketing-proof-landing`
- `editorial-product-explorer`
- `immersive-hero`

Extract tracks and relationships, not pixels: max-width strategy, grid/flex regions, hierarchy, gutters, sticky/fixed regions, list/detail relationships, and mobile collapse order.

The skeleton should make the page coherent before color, animation, or ornament is added.

---

## 3. Compose traits, not libraries

Select the **smallest coherent compatible set** of pattern IDs from `references/patterns/registry.yaml` using `references/composition-selection.md`.

Complex product surfaces will often use roughly 3–7 patterns. Narrow, specialized, or expressive surfaces may legitimately use only 1–2 when that is the complete compatible set. Never add irrelevant patterns merely to satisfy a quota.

Start from the skeleton's `recommended_patterns`, then add only what the job or required states still lack. Consult `references/patterns/recipes.md` for host-neutral implementation guidance.

Hard rejects beat any ranking hint: wrong surface, replacing the host primitive system, inaccessible primary interaction, third-party design-contract identity substitution, unjustified second icon family, brand-copy, unjustified dependency, or a mobile-breaking layout on a mobile-required task.

Popular libraries are evidence for a pattern, not default runtime dependencies. Consult `references/sources/registry.yaml` only after pattern IDs are chosen, and only to check provenance / integration mode.

### Dependency rule

Prefer this order:

1. existing host component
2. existing host utility / primitive
3. reimplement a small observed pattern using host primitives
4. copy-own source only when license and architecture make it appropriate
5. add a dependency only when its behavior is substantial enough to justify it

Do not mix competing primitive or icon systems in one surface unless the repository already does so intentionally.

---

## 4. Adapt to the host stack

Use the closest adapter in `references/adapters/`.

Adapters translate a selected pattern into the host's implementation vocabulary. They do not redefine the visual direction.

Current baseline: React + Tailwind, Vue + Element Plus, Vue + UnoCSS, and generic CSS/existing design system.

If no exact adapter exists, keep existing component APIs, map values to host tokens, preserve form semantics and SSR/hydration constraints, reuse the current icon set, and avoid new runtime dependencies for purely visual effects.

---

## 5. Anti-slop hard fails and heuristics

Rewrite before calling a surface done when it exhibits these hard failures without a deliberate product reason:

- random aurora/mesh/AI-purple decoration on app chrome
- glassmorphism on every panel
- rainbow borders / neon glow without brand rationale
- emoji used as product UI icons
- a second icon family introduced without a host/product reason
- third-party DESIGN.md/catalog identity substituted for host tokens/primitives
- ad-hoc spacing that bypasses the host scale (`p-[13px]`, `gap-[17px]`)
- identical radius everywhere regardless of nesting
- floating elements with no shared grid/gutter logic
- lorem/placeholder boxes in a finished view
- animation on every click or keyboard action
- `transition: all`
- "Live" badges or shimmer on static text
- fake dashboards/screenshots built from decorative rectangles
- three equal marketing cards simply because the model needs a section
- copied visual identity from a reference product

Treat these as **slop heuristics**, not universal bans: Inter-everywhere with no hierarchy, em-dash-heavy UI copy, numbered eyebrows such as `001 · Capabilities`, silent purple/violet brand accents, animated icons across repeated product chrome, and two equally loud filled primary actions in one region. Flag them when they appear by default with no product/brand rationale; allow them when they are intentional and coherent with the surface.

Campaign/editorial surfaces can be more expressive, but must still use one coherent motif family rather than an effect sampler.

Shared defaults for time, radius, type, action hierarchy, tabular numbers, and streaming: `references/physics.md`.

---

## 6. Motion policy

Motion explains state, hierarchy, causality, or spatial change. Otherwise, delete it.

- high-frequency / keyboard-driven interactions: usually instant
- hover/focus/open/close: prefer CSS transitions when sufficient
- general UI motion: usually ≤ 300ms
- enter may be slightly slower than exit
- avoid `scale(0)` for ordinary UI
- animations must be interruptible where repeated interaction is possible
- always provide a `prefers-reduced-motion` path
- do not add a motion library only to animate opacity/translate
- repeated navigation/table/toolbar icons stay static by default unless animation communicates real state or brand behavior

Use `references/physics.md` for shared defaults and `references/motion-blocks.md` for distinctive recipes.

---

## 7. AI-native surfaces

For model/agent products, do not reduce the experience to "chat bubbles + spinner". Compose explicit states for streaming response, progress/activity summary, tool invocation, approval, sources/context, composer state, retry/error/cancel, and queued/running/success/failed tasks.

Do **not** imply hidden chain-of-thought is available. Labels such as Activity, Progress, Execution trace, or Reasoning summary must represent only provider-exposed summaries, actual tool events, or product-owned progress.

See `references/ai-primitives.md`. Use the host-neutral recipes there and map colors/radii to host tokens.

---

## 8. Fallback quality gates

Every finished implementation must pass semantic HTML/native-control correctness, keyboard operability, visible focus, accessible naming, contrast, reduced motion, mobile touch targets, no accidental horizontal overflow, responsive hierarchy, required loading/empty/error/disabled/success states, useful recovery/next actions where applicable, and reuse of host tokens/conventions.

---

## 9. Verification

Never finish from source inspection alone. Verify desktop, ~390px mobile, keyboard navigation, interactive states, loading/empty/error, reduced motion, console/hydration errors, overflow, layout jumps, and dependency changes.

Then compare against positive and negative references: inherit useful structure/behavior without inheriting source identity, and keep the result native to the host project.

---

## Finish checklist

- [ ] Host Read completed; no framework/library was assumed
- [ ] Host Contract captures active tokens, typography, icons, motion, layout and constraints
- [ ] Any DESIGN.md-shaped contract uses host-derived values, not catalog identity
- [ ] Design Read + V/M/D direction declared
- [ ] One skeleton ID chosen from the skeleton registry before styling
- [ ] Smallest coherent compatible pattern set selected; no quota-padding
- [ ] Canonical patterns use host-neutral recipes where available
- [ ] Existing host component/token/icon system preserved
- [ ] No competing primitive or icon kit added without a strong reason
- [ ] Anti-slop hard fails removed; heuristics judged in context
- [ ] Motion passes purpose/frequency/reduced-motion tests
- [ ] AI UI exposes activity summaries, not hidden chain-of-thought
- [ ] Accessibility/responsive/state gates pass
- [ ] Rendered result verified in-browser when possible

# Goals

UI Compose exists because coding agents can write valid frontend code and still make poor product decisions. The main failure is not syntax. It is composition without context: generic cards, arbitrary spacing, mismatched primitives, fashionable effects, weak product states, and layouts that ignore the host system.

## Primary goal

Give a coding agent a repeatable method to compose interfaces from proven structural and interaction decisions while keeping the result native to the host project.

The operating sequence is:

**Host Read → Design Read → Skeleton → Pattern Set → Adapter → Verify**

Success looks like:

- the host framework, component system and tokens are preserved
- page architecture is chosen before decorative styling
- patterns are selected because they fit the product job, density and interaction model
- external libraries/products are treated as evidence, not default dependencies
- AI-native UI exposes real streaming/tool/approval/error states without implying hidden chain-of-thought
- motion has a purpose, respects interaction frequency, and supports reduced motion
- mobile, keyboard, loading, empty, error and destructive states are intentionally designed
- the result does not visually clone a reference brand

## Secondary goals

1. **Catalog decisions, not libraries.** Record reusable patterns and skeletons independently from the sources that inspired them.
2. **Adapt, do not cargo-cult.** Re-express useful structure, interaction and motion using the host implementation vocabulary.
3. **Teach restraint.** High-frequency and keyboard interactions should usually be instant or nearly instant. Decorative motion must earn its cost.
4. **Stay primitive-system consistent.** Reuse the host button/input/dialog/table system unless there is a strong, explicit reason not to.
5. **Keep provenance visible.** Source code, assets, trademarks and licenses remain upstream concerns; observations and independently reimplemented traits belong in UI Compose.
6. **Measure decisions.** Eval failures should be classified as wrong skeleton, wrong pattern, wrong density, ignored host system, unnecessary dependency, missing state, accessibility failure, or brand-copy risk.

## Non-goals

UI Compose is not:

- a new npm component library
- a replacement design system
- a visual clone of Linear, Stripe, Apple, Raycast, Beautiful UI, or any other product
- permission to combine multiple primitive kits in one app
- a bundle of trendy effects
- a reason to add Tailwind, Radix, Motion, GSAP, Three.js, or any other dependency when the host does not need it
- a replacement for a dedicated visual-direction/taste skill

A design-direction skill can decide *what the interface should feel like*. UI Compose decides *how the interface should be structured and implemented in the host project*.

## Agent contract

When this skill is loaded, the agent should:

1. perform Host Read before proposing implementation
2. state the inferred surface, audience, density and motion direction
3. choose a page skeleton before styling details
4. select the smallest coherent pattern set, usually 3–7 patterns
5. prefer host-native implementation over introducing a new UI dependency
6. use the relevant stack adapter
7. implement required product states, not only the happy path
8. verify desktop, mobile, keyboard, focus, reduced motion, overflow and runtime behavior
9. avoid copying reference identity, proprietary assets or unverified source code

## Outcome the user should feel

The interface should feel intentionally designed for the product and naturally implemented in its existing codebase. The user should not need to know which external products or libraries informed the decisions, because the final result should belong to the host application.

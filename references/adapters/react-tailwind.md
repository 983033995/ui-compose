# Adapter: React + Tailwind

Use this adapter only when Host Read confirms React and Tailwind are active in the product.

## Preserve first

- Reuse existing local primitives before adding shadcn/Radix/Base UI.
- Reuse the project's Tailwind theme aliases and semantic classes.
- Keep routing, data fetching, form handling, and state patterns unchanged unless the task requires otherwise.

## Pattern translation

When importing a visual idea from another source:

1. copy the layout relationship, not its brand classes;
2. map spacing/radius/type/color to host utilities;
3. keep control semantics and accessibility behavior;
4. avoid arbitrary-value utilities when a project token exists;
5. avoid a new animation dependency for simple CSS transitions.

## Dependency policy

If Radix/shadcn already exist, they may be used for missing accessible primitives.
If they do not exist, do not add them merely to reproduce one card, toolbar, badge, or disclosure.

## Verification

Check class conflicts, dark mode, responsive states, focus-visible, hydration, and purge/content configuration when generating new utility patterns.

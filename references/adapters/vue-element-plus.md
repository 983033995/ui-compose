# Adapter: Vue + Element Plus

Use this adapter when Host Read confirms Vue and Element Plus are the active product primitives.

## Preserve the product vocabulary

- Prefer existing wrappers around `el-*` components.
- Keep current form validation, table behavior, dialog/drawer conventions, and icon usage.
- Treat Element Plus as the behavioral primitive layer, not the final visual identity.

## Translating external UI traits

When a reference has a stronger composition than the host:

- reproduce its layout tracks with CSS Grid/Flex;
- tune density through existing spacing variables/classes;
- restyle Element Plus with project tokens and scoped/global overrides already used by the repo;
- wrap only where a reusable product behavior is missing;
- do not port React JSX or Radix interaction code into Vue.

## Data-heavy surfaces

For dashboards/CRUD:

- keep `el-table`, `el-form`, pagination, selection, validation, and accessibility behavior when they already solve the job;
- improve the surrounding composition: filter hierarchy, toolbar density, master/detail layout, empty/loading states, bulk actions, sticky regions;
- avoid replacing a mature table with a visually attractive custom grid unless requirements demand it.

## Motion

Prefer Vue `<Transition>` or CSS when the repo already uses them. Do not add a JS animation library for simple fades, height changes, drawers, or hover feedback.

## Common failure to avoid

External block libraries often make controls visually compact by changing DOM and semantics. In Element Plus projects, preserve component behavior and move the visual idea into tokens, wrapper layout, slots, and scoped styling instead.

# Host Read

Host Read is the first phase of UI Compose. It prevents the skill from treating every frontend as React + Tailwind + shadcn.

## Output

Before implementation, derive a compact host contract:

```text
Framework: Vue 3 + Vite
Styling: UnoCSS + scoped CSS
Components: Element Plus + local wrappers
Tokens: CSS variables in src/styles/tokens.css
Motion: Vue Transition + CSS only
Icons: @element-plus/icons-vue
Constraints: desktop-first B2B app, SSR none, mobile secondary
```

Do not invent missing facts. If a fact cannot be detected, mark it `unknown` and use the least invasive fallback.

## Detection order

1. package manager and manifests
2. framework/runtime config
3. styling config and global styles
4. component imports and local wrappers
5. token/theme definitions
6. motion dependencies and existing transitions
7. representative pages/components
8. accessibility and lint/test conventions

## Evidence to inspect

### Framework/runtime

- `package.json`
- `vite.config.*`, `next.config.*`, `nuxt.config.*`, `svelte.config.*`
- `src/main.*`, app/router entry files

### Styling

- `tailwind.config.*`, `uno.config.*`, PostCSS config
- global CSS/SCSS
- CSS Modules usage
- styled-components/emotion/vanilla-extract/etc.

### Component system

Search imports for:

- Element Plus
- Ant Design
- Radix
- shadcn-generated components
- Base UI
- Headless UI
- local `components/ui` or internal packages

The existence of a dependency does not automatically make it the active product primitive system. Inspect actual usage.

### Tokens

Find:

- CSS custom properties
- Tailwind/Uno theme aliases
- design-token packages
- typography scales
- spacing/radius/shadow variables
- dark-mode conventions

Prefer semantic tokens already used by product surfaces.

### Existing patterns

Inspect at least one representative implementation for each relevant class:

- shell/navigation
- form
- data table/list
- modal/drawer
- card/panel
- loading/empty/error

This tells UI Compose what "native to this repo" means.

## Integration decision

After detection, choose one:

### A. Preserve

Use existing components and only change composition/tokens/spacing. Default for mature products.

### B. Extend

Create a small local primitive or wrapper when a needed behavior is missing.

### C. Reimplement trait

Translate an observed external pattern into host-native code without bringing in the external library.

### D. Copy-own

Only for source that explicitly permits it and when copying is architecturally cleaner than imitation. Preserve attribution/license requirements.

### E. Add dependency

Last resort. Use when the behavior is substantial, maintained, accessible, and expensive to recreate safely.

## Host DESIGN.md contract

If a later step needs a model-readable design file, write it from **this host**, not from an external product catalog.

Public DESIGN.md corpora (for example Refero Styles) are evidence of *how to structure* a contract: color roles, type roles, spacing/radius, layout tracks, motion stack, and do/don’t rules. They are not a skin pack.

Capture only what Host Read actually found:

```text
Color roles: bg, surface, fg, muted, border, primary, danger
Type roles: existing host font stack and size tokens
Spacing / radius / elevation: existing host tokens
Layout tracks: observed on representative pages
Motion: existing stack + prefers-reduced-motion path
Do / don't: host conventions that later steps must not invent around
```

Do not paste a Linear, Stripe, or catalog DESIGN.md into the repo and call it Design Read. That is host-identity substitution (brand-copy).

If the host already has `tokens.css`, a theme file, or a design-system package, point at those files. Do not create a parallel theme that the rest of the product does not use.

## Red flags

Stop and reconsider if an implementation would:

- add a second form/control primitive system
- add Tailwind to a non-Tailwind codebase only for one block
- introduce React-specific source into Vue/Svelte
- bypass existing tokens with arbitrary colors/spacing
- replace accessible existing components with prettier but weaker custom HTML
- create a parallel theme file that the rest of the product does not use
- paste a third-party product DESIGN.md over the host token system

## Rule

External projects provide **evidence of good decisions**. The host project provides the **implementation vocabulary**.

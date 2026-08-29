# Host Read

Host Read is the first phase of UI Compose. It prevents the skill from treating every frontend as React + Tailwind + shadcn.

## Output

Before implementation, derive a compact host contract:

```text
Framework: Vue 3 + Vite
Styling: UnoCSS + scoped CSS
Components: Element Plus + local wrappers
Tokens: CSS variables in src/styles/tokens.css
Typography: host font stack + existing size/weight roles
Icons: @element-plus/icons-vue
Motion: Vue Transition + CSS only
Layout: desktop-first B2B shell, dense data surfaces
Constraints: SSR none, mobile secondary, accessibility required
```

This **Host Contract** is an internal decision representation. It may be written as a short note, structured object, or DESIGN.md-shaped summary when that helps a later agent step. Do not create a new file in the host repository unless the task actually benefits from one.

Do not invent missing facts. If a fact cannot be detected, mark it `unknown` and use the least invasive fallback.

## Detection order

1. package manager and manifests
2. framework/runtime config
3. styling config and global styles
4. component imports and local wrappers
5. token/theme definitions
6. typography and icon conventions
7. motion dependencies and existing transitions
8. representative pages/components
9. accessibility and lint/test conventions

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

### Typography

Find the roles the product actually uses before inventing a new scale:

- font stack
- body/meta/title sizes
- weight hierarchy
- line-height and measure conventions
- tabular-number usage where numeric alignment matters

### Icons

Find the icon package or SVG convention already in use (`@element-plus/icons-vue`, `lucide-react`, Phosphor, Font Awesome, inline SVG, SVG sprites, internal icon components).

- If a set exists, **reuse it**. A second icon family without a strong product reason is a host-system violation.
- Animated icon kits are an additional motion language. Keep them off repeated product chrome such as navigation, tables, toolbars, and settings by default; require an explicit interaction/brand reason before introducing them.
- If the host has no icon system, choose one family that matches the primitive system and use it consistently. Do not mix outline, filled, and animated families casually.

### Existing patterns

Inspect at least one representative implementation for each relevant class:

- shell/navigation
- form
- data table/list
- modal/drawer
- card/panel
- loading/empty/error

This tells UI Compose what "native to this repo" means.

## Host Contract / DESIGN.md shape

If a later step needs a model-readable design contract, it may use a DESIGN.md-like **shape**, but the values must come from this host.

Useful fields:

```text
Color roles: bg, surface, fg, muted, border, primary, danger
Type roles: existing host font stack and size/weight tokens
Spacing / radius / elevation: existing host tokens
Icon system: existing family, fill/stroke convention, size roles
Layout tracks: observed shell/content/list/detail relationships
Motion: existing stack + prefers-reduced-motion path
Do / don't: host conventions later steps must preserve
```

External DESIGN.md catalogs are methodology references only. Never paste a Linear, Stripe, Refero, or other product contract into the project and call it the host identity.

If the host already has `tokens.css`, theme files, a design-system package, Storybook, or design documentation, point to those sources rather than creating a parallel theme.

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

## Red flags

Stop and reconsider if an implementation would:

- add a second form/control primitive system
- add Tailwind to a non-Tailwind codebase only for one block
- introduce React-specific source into Vue/Svelte
- bypass existing tokens with arbitrary colors/spacing
- replace accessible existing components with prettier but weaker custom HTML
- create a parallel theme file that the rest of the product does not use
- substitute a third-party DESIGN.md or catalog skin for the host identity
- add a second icon family without justification
- introduce animated icons across repeated product chrome with no interaction/brand reason

## Rule

External projects provide **evidence of good decisions**. The host project provides the **implementation vocabulary**.

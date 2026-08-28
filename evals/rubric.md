# UI Compose Evaluation Rubric

UI Compose should be measured against representative frontend tasks, not judged only by how persuasive the skill text sounds.

## Benchmark modes

For each case, compare when practical:

1. model only
2. generic frontend-design skill
3. taste-oriented skill
4. UI Compose
5. taste-oriented skill + UI Compose

Do not publish benchmark numbers until the cases are actually run.

## Weighted score

| Dimension | Weight | What good looks like |
| --- | ---: | --- |
| Visual quality | 25 | clear hierarchy, intentional spacing, coherent composition |
| Design consistency | 15 | one system for type, radius, color, surface, density |
| Task fit | 15 | page structure matches the product/workflow instead of generic showcase UI |
| Host-stack compliance | 10 | reuses existing framework, primitives, tokens, architecture |
| Accessibility | 10 | semantics, labels, keyboard, focus, contrast, reduced motion |
| Responsive behavior | 10 | mobile hierarchy is intentionally composed, no accidental overflow |
| Build/runtime success | 5 | compiles/renders with no obvious runtime or hydration failure |
| Dependency discipline | 5 | no unnecessary second UI/motion stack |
| Anti-slop | 5 | generic AI tells and effect stacking are absent |

Total: 100.

## Automatic hard fails

A case cannot score above 59 if any of these are true:

- does not build/render
- replaces host framework/component system unnecessarily
- breaks primary interaction semantics
- has severe mobile overflow
- inaccessible primary controls
- directly clones a reference brand identity

## Suggested initial cases

### App interiors

- B2B SaaS dashboard with filters + data table
- settings page with sections and destructive action
- master/detail CRUD workspace
- command/search surface

### AI products

- agent chat with streaming + tool execution + approval
- task run detail with activity/progress/error/retry

### Marketing / expressive

- SaaS landing page
- editorial DTC product explorer
- restrained 3D hero with DOM content

### Host diversity

- React + Tailwind + existing local primitives
- Vue 3 + Element Plus
- Vue 3 + UnoCSS
- existing custom design system + plain CSS/SCSS

## Review process

For each run capture:

- prompt/task brief
- host repo snapshot/fixture
- generated diff
- desktop screenshot
- mobile screenshot
- dependency changes
- build/test result
- rubric score and notes

The most valuable failure signal is not "looks bad". Record the decision error:

- wrong skeleton
- wrong density
- ignored host tokens
- unnecessary dependency
- inappropriate motion
- copied reference identity
- missing product state
- inaccessible control

Those failure classes should drive future skill changes.

# Design direction dials

UI Compose can consume visual-direction guidance from another design/taste skill, but it should not vendor or depend on that skill's implementation. The useful interface is a small set of directional signals that inform skeleton and pattern selection.

Reference methodology: `leonxlnx/taste-skill`.

## Principle

Taste decides the direction. UI Compose decides how to build it.

A taste-oriented skill may answer questions such as:

- how expressive should the page feel?
- how much motion is appropriate?
- how dense should information be?
- which visual register fits the audience and product?

UI Compose then converts those signals into host-native composition decisions.

## Design Read

Before selecting a skeleton, summarize the intended register in one line:

> Reading this as: <surface> for <audience>, with a <visual register>, density <1–10>, motion <1–10>.

If evidence is strong enough, infer and proceed. Ask a clarifying question only when the ambiguity materially changes the product structure.

Useful signals, in order:

1. surface/job
2. audience
3. existing brand/design system
4. reference screenshots or URLs
5. explicit vibe words
6. accessibility/performance/regulatory constraints

Constraints override aesthetics.

## Directional dials

UI Compose uses three optional 1–10 dials:

| Dial | Low | High | What it influences |
| --- | --- | --- | --- |
| `DESIGN_VARIANCE` | regular, symmetric, restrained | asymmetric, editorial, experimental | skeleton family and section rhythm |
| `MOTION_INTENSITY` | instant/functional | expressive/cinematic | whether motion patterns are eligible |
| `VISUAL_DENSITY` | gallery/marketing | cockpit/data-heavy | spacing, grouping, control density, table/list decisions |

These are directional, not universal presets.

Typical starting ranges:

| Surface | Variance | Motion | Density |
| --- | ---: | ---: | ---: |
| app interior / dashboard | 3–5 | 1–3 | 7–9 |
| settings | 2–4 | 0–2 | 5–7 |
| AI chat / agent workspace | 3–5 | 1–3 | 5–8 |
| SaaS marketing | 5–8 | 3–6 | 2–5 |
| editorial campaign | 7–9 | 5–8 | 2–5 |
| immersive/WebGL hero | 6–9 | 5–8 | 1–4 |
| public-sector / trust-heavy | 2–4 | 0–2 | 4–6 |

Do not apply a marketing baseline to an app interior.

## How dials affect composition

### High density

Prefer:

- data workspace or master/detail skeletons
- 1px separators and strong grouping
- compact controls
- visible filter state
- contextual bulk actions
- tabular numbers where appropriate

Avoid:

- one card per field
- decorative whitespace that weakens scanability
- oversized marketing typography

### High motion

Motion patterns become eligible only when they support hierarchy, state or spatial causality.

Requirements:

- reduced-motion path
- no animation on every keyboard action
- no new motion library for simple opacity/translate
- no stacking multiple motion systems without a strong reason

### High variance

Allow more asymmetry and editorial composition, but preserve readable hierarchy and responsive behavior. High variance does not justify random offsets or broken alignment.

## Anti-default signals

These are common generic-AI tells and should trigger a negative-reference check:

- AI-purple mesh gradients with no brand rationale
- glassmorphism across the entire product shell
- three equal feature cards by default
- fake dashboard screenshots made from empty rectangles
- random pills/status dots that represent no real state
- repeated eyebrow labels on every section
- large centered dark hero regardless of product context
- decorative motion on high-frequency controls

## Pairing with external taste/design skills

A separate visual-direction skill is useful for landing pages, portfolios, redesigns and expressive marketing surfaces. UI Compose should consume its conclusions, not copy its implementation text.

Recommended handoff:

```text
Design/taste skill
  → surface + audience + visual register + V/M/D
UI Compose
  → Host Read
  → Skeleton
  → Pattern Set
  → Adapter
  → Verify
```

For app interiors, dashboards, settings, AI-native workflows and data-heavy products, UI Compose should remain the primary composition layer.

## Agent move

1. Perform Host Read.
2. State the Design Read and optional V/M/D values.
3. Use those values as filters when selecting skeletons/patterns.
4. Prefer the smallest coherent pattern set.
5. Keep implementation native to the host stack.
6. Verify the output against both positive and negative references.

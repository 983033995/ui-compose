# Goals

This skill exists because coding agents can write CSS and still ship
interfaces that look vibe-coded. The failure is not syntax. It is **taste
without a skeleton**: random spacing, invented buttons, gradient-blob
heroes, and motion on every click.

## Primary goal

Give an agent a **closed method** to compose frontend from proven blocks
so the output reads as a designed product, not as "AI slop".

Success looks like:

- One visual system (tokens, radius, type, density) used everywhere
- Layout stolen from a real skeleton, not invented cell-by-cell
- Primitives copied/owned (shadcn-class) instead of generated from zero
- AI-product chrome (stream, think, tools, approve, composer) uses real
  primitives, not a spinner plus a `<pre>`
- Motion has a purpose, a frequency test, and a duration ≤ 300ms
- A screenshot would not match the slop tell-list

## Secondary goals

1. **Catalog, don't cargo-cult.** Name which library to steal from for
   which job, and which ones are decoration that become slop if overused.
2. **Reverse, don't iframe.** For sites with no npm package, extract the
   actual CSS fingerprints (easing, radii, caret, shimmer) and reimplement
   against the app's tokens.
3. **Teach restraint.** Emil Kowalski's rule is part of the goal: the
   best animation is often no animation. Keyboard and high-frequency UI
   stay instant.
4. **Stay kit-monogamous.** One primitive kit per app. Restyle stolen
   blocks onto that kit's tokens. Never mix shadcn + MUI + HeroUI in one
   tree.

## Non-goals

- Not a new component library or npm package
- Not a Figma file or a visual clone of Linear/Stripe/Beautiful UI
- Not permission to dump Magic UI / Aceternity / ThreeUI scenes on every
  surface. One decorative family, one GPU scene, or none.
- Not a replacement for a sibling design-system skill (tokens, type,
  a11y). This skill owns *composition*; that skill owns *the system*

## Agent contract

When this skill is loaded, the agent must:

1. Name a **positive reference** (a real product or one block library)
2. Name a **negative reference** (the slop tell-list)
3. Steal a **layout skeleton** before choosing colors
4. Pick **3–7 blocks** from `sources.md`, mapped onto existing tokens
5. If the product talks to a model, implement the AI-native minimum set
   in `ai-primitives.md`
6. Refuse ad-hoc spacing (`p-[13px]`) and a second component kit

## Outcome the user should feel

The UI looks like someone with taste laid the tracks, and the agent
filled them. Editing later is easy because the source of every block is
known and owned.

# Eval 06 — SaaS Marketing Landing

## Goal

Evaluate whether UI Compose can create an expressive but product-specific marketing page without falling into generic AI-landing defaults or cloning a reference brand.

## Host fixture

- existing product/brand tokens
- existing button/link/navigation primitives
- framework is intentionally unspecified
- no new animation or UI library should be assumed
- desktop and mobile required

## Task brief

Build a landing page for a B2B workflow product with:

- clear value proposition and primary CTA
- credible product proof
- workflow/product explanation
- customer or trust evidence
- differentiated section rhythm
- restrained motion
- responsive navigation and CTA hierarchy

## Expected composition

Primary skeleton:

- `marketing-proof-landing`

Expected pattern candidates:

- `single-ambient-moment` when brand direction supports it
- product-proof sections using real workflow/state evidence rather than fake dashboard rectangles

## Host integration expectations

- reuse host typography, color and interaction primitives
- infer a coherent visual register before choosing decorative treatment
- use one motif family rather than several unrelated trendy effects
- preserve semantic heading hierarchy and useful content order on mobile
- motion should reinforce reveal/hierarchy, not decorate every control

## Hard failures

- generic centered dark hero with AI-purple mesh and three equal cards by default
- invented logos/testimonials presented as real evidence
- copied reference brand identity, copy or illustration language
- fake dashboard blocks with no meaningful product state
- adds animation/effect libraries for simple CSS-level motion
- mobile reordering weakens the value proposition or CTA path

## Review notes

Visual novelty is not enough. Score product specificity, content hierarchy, proof quality and anti-slop discipline separately from raw aesthetic preference.

# Eval 07 — Editorial Product Explorer

## Goal

Evaluate whether UI Compose can create an expressive campaign/product experience from a locked composition plus item-owned visual worlds without relying on hover-only interaction or cloning a reference brand.

## Host fixture

- existing ecommerce/brand application
- product data and accessible HTML controls already exist
- framework intentionally unspecified
- no assumption of GSAP, Motion, React or Tailwind
- touch/mobile and reduced motion required

## Task brief

Build a campaign explorer for a small product collection where selecting an item changes the page's visual world while keeping the core layout understandable.

Required behavior:

- persistent product selector
- click/tap and keyboard activation
- hover preview only as progressive enhancement
- selected state persists independent of hover
- product-specific media/accent/background treatment
- CTA and core product information remain accessible
- reduced-motion path

## Expected composition

Primary skeleton:

- `editorial-product-explorer`

Expected pattern candidates:

- `editorial-world-switch`
- `single-ambient-moment` only if it belongs to the selected world

## Host integration expectations

- use CSS variables/tokens or equivalent host state to express each product world
- one coherent motif family per world
- typography must use licensed/available host assets
- interaction works without hover and without animation
- visual transformation should not reorder essential content unpredictably

## Hard failures

- hover is the only activation mechanism
- active selection disappears when pointer leaves
- copied brand copy, imagery, type treatment or signature campaign identity
- multiple unrelated effect systems compete on one screen
- reduced motion simply removes feedback/state clarity
- touch targets or selected state are inaccessible

## Review notes

This case should reward expressive composition and interaction clarity together. A beautiful hover-only desktop demo is a hard product failure.

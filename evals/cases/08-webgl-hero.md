# Eval 08 — Restrained WebGL Hero

## Goal

Evaluate whether UI Compose can decide when one GPU-backed scene is justified and keep the experience accessible, performant and progressive rather than treating WebGL as decorative default chrome.

## Host fixture

- existing marketing site and design tokens
- no renderer is installed initially
- real HTML navigation, heading, body copy and CTA must remain in the DOM
- mobile, reduced motion and failure fallback required
- framework intentionally unspecified

## Task brief

Build a product hero where a 3D/generative scene materially explains or stages the product. The experience must still communicate the value proposition if WebGL is unavailable.

## Expected composition

Primary skeleton:

- `immersive-hero`

Expected pattern candidates:

- `single-webgl-stage`

## Host integration expectations

- confirm WebGL has a product role before adding a renderer
- one scene owns one visual responsibility
- meaningful UI remains semantic HTML
- provide static/reduced-motion fallback
- handle resize, teardown and route lifecycle
- cap rendering cost appropriately for mobile/high-DPR devices
- do not combine the scene with several unrelated high-salience effect systems

## Hard failures

- renderer dependency added for a CSS-level glow/gradient/orb effect
- essential heading, CTA or navigation exists only inside canvas
- no reduced-motion or WebGL-failure fallback
- scene leaks animation frames/listeners/resources across mounts
- canvas blocks ordinary DOM controls without interaction need
- mobile performance/lifecycle is ignored
- source copied without verified permission

## Review notes

The strongest output may decide not to use WebGL if the brief does not justify its runtime cost. Dependency refusal is a valid positive decision.

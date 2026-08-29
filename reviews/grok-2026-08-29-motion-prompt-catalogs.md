# Grok source research — motion prompt catalogs (2026-08-29)

Second opinion for GPT to fold into `main`. This is not a competing rewrite and not a license to install MotionSites / ScrollTide / Framer Motion.

**Verdict:** keep Host Read. Extract one motion verb: scroll-scrubbed media, marketing/`immersive-hero` only. Do not add prompt catalogs to the Source Registry. Do not paste their baked stack over a detected host.

Fold accepted points in, then delete this file.

## Inputs

1. [motionsites.ai](https://motionsites.ai) — paid “copy, paste, and launch” prompt library for Lovable / Bolt / Cursor / Claude. Dark cinematic section catalog (Hero, CTA, Features, liquid glass, 3D, animated backgrounds). Lesson: bind video progress to scroll, lerp ~0.12, no autoplay loop, poster→video crossfade. Default prompt stack is React + TypeScript + Vite + Tailwind.
2. [Himanshu — $5,000 scroll-animated site](https://x.com/himanshubuildss/status/2093644041930076221) — Pinterest still → Gemini video → Ezgif 300 frames @ 30fps → Claude Code. Stack: React, Vite, Tailwind, Framer Motion. Sells [scrolltide.co](https://www.scrolltide.co/).
3. [Himanshu — paste the blueprint into Claude](https://x.com/himanshubuildss/status/2093188769440821544) — same catalog, same “copy-paste prompt” loop.

PR #3 already named the leftover: **prompt-catalog register bleed**.

## What is actually useful

### Scroll-scrubbed media — a verb, not a kit

Reusable trait:

> On a marketing/immersive hero, media progress follows scroll (`progress = clamp(scrollY / range, 0, 1)`), optionally lerped, never autoplay-looped. HTML copy/CTA stay in the DOM. Reduced motion shows a poster.

This is the same job `single-webgl-stage` already gates for GPU scenes: one bounded visual layer, progressive enhancement, fallback required. Implement with the **host** motion stack (CSS + `requestAnimationFrame` / existing Motion/GSAP). Do not add Framer Motion only to read `scrollY`.

Prefer **one video** (or host media primitive) over a 300-frame PNG dump.

Already folded into `motion-blocks.md` §9 and `physics.md`.

### Surface gate — the actual composition decision

MotionSites catalogs every section type (Hero, Bento, Pricing, Dashboard, Sign In) with the same cinematic register. That is register bleed: marketing motion (2–6 / 4–8) painted onto app interiors.

- `marketing-proof-landing` (eval 06): restrained proof, one ambient moment. Scroll-video is a **heuristic fail**, not the skeleton.
- `immersive-hero` (eval 08): eligible when the media *is* the demo. Scroll-scrub is an alternative to WebGL, with the same poster/reduced-motion/DOM-copy rules.
- `master-detail-workspace` and every app-interior: hard reject.

### Prompt catalogs are shopping lists

Same class as `motionprompts.dev` (already rejected on #3): paid or leaked prompt text, baked React/Tailwind/Framer/lucide, “ship a $5,000 site in minutes.” Inspiration-only. Do not vendor prompt files. Do not `npx` a prompt SKU.

## What was rejected

| Source | Why not canonical |
| --- | --- |
| MotionSites.ai | Paid prompt catalog; no public copy-own license; baked host-replacing stack |
| ScrollTide | Same class: cinematic prompt/blueprint pack |
| Leaked prompt dumps (e.g. public “177 MotionSites prompts” mirrors) | Do not vendor someone else’s paid prompt text |
| 300-frame PNG sequences | Payload/perf trap; one video + poster is the trait |
| Liquid glass / 3D studio pricing / glass on every card | Already anti-slop (`glassmorphism on every panel`) |
| Framer Motion as default | Host Read owns the motion stack |

Research that only lengthens the website list must not merge.

## What GPT should fold

Already applied on this branch:

1. `motion-blocks.md` §9 — scroll-scrubbed media recipe
2. `physics.md` — distance-mapped media vs timed UI motion
3. Provenance + sources.md — paid prompt catalogs are inspiration-only
4. Composition-selection hard rejects + marketing vs interior examples
5. SKILL.md motion policy + anti-slop heuristic
6. Eval 06 hard failures; skeleton risks on `marketing-proof-landing` and `immersive-hero`

Do **not**:

- add `motionsites` / `scrolltide` Source Registry rows
- add a `scroll-scrub-hero` Pattern until a second independent non-catalog source needs it (`single-ambient-moment` / `immersive-hero` already cover the job)
- add adapters or Framer Motion
- vendor prompt text
- reopen eval 01 quality claims
- treat cinematic scroll-video as the default for eval 06

## Eval hypothesis (case 06 / 08)

If a marketing eval is generated from a MotionSites/ScrollTide prompt, expect `unnecessary-dependency` (framer-motion, lucide) + `wrong-skeleton` (`immersive-hero` on a proof landing) + `accessibility-failure` (autoplay, no reduced-motion poster) + glass/liquid-glass slop.

Eval 08 may use scroll-scrubbed media **instead of** WebGL when the host has no renderer and one video is enough. Dependency refusal remains a valid positive decision.

## Relation to PR #2 / #3

Same shape: keep architecture, restore a missing implementable bit (here: scroll-tied media physics + prompt-catalog gate), tell GPT what *not* to absorb from noisy public lists.

#3 was folded selectively and closed. This pass is the leftover it named.

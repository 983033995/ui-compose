# Taste dials (from taste-skill)

Source: [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill)
Announce: [shao__meng](https://x.com/shao__meng/status/2093148263621017886)
Author: [@LexnLin](https://github.com/leonxlnx)

Do **not** vendor their 1200-line `SKILL.md`. This file is the
intersection: what ui-lego was missing, mapped onto our registers.
Install the upstream skill when the job is a **landing / portfolio /
redesign** and you want their full pre-flight:

```bash
npx skills add https://github.com/leonxlnx/taste-skill --skill "design-taste-frontend"
```

Thesis (theirs): *LLM design is bad because the model skips
understanding and pastes a default aesthetic.*

Thesis (ours, still true): *even with taste, inventing components from
zero is how slop happens.* Read the room, then steal a block.

taste-skill is **explicitly not** for dashboards, data tables, or
multi-step product UI. Those stay this skill + shadcn / ReUI / Kibo.

---

## Pairing

| Job | Who leads |
| --- | --- |
| App interior, chat, CRUD, AI chrome | **ui-lego** (`layout-steal`, `ai-primitives`) |
| 3D / WebGL moment | **ui-lego** (`threeui.md`) |
| Y2K / lookbook campaign | **ui-lego** (`editorial-campaign.md`) |
| New landing / portfolio / marketing | taste-skill dials **then** ui-lego blocks |
| Redesign of an existing site | taste-skill §11 audit **then** ui-lego restyle |
| Comp images before code | their `image-to-code` / `imagegen-frontend-*` |

One primitive kit still wins. Their §2 map (Fluent, Carbon, Polaris,
GOV.UK, USWDS, Primer) is the exception: if the brief *is* that
product, install the **official** package. Do not hand-roll a fake
GOV.UK. Do not mix it with shadcn.

Honesty rule they nailed: there is **no** `liquid-glass.css`. Web
glass is an approximation. Label it.

---

## 0. Design Read (before any block)

Output one line, then pick blocks:

> Reading this as: \<page kind> for \<audience>, with a \<vibe>
> language, leaning toward \<system or family>.

If the read actually forks, ask **one** question. Never a
questionnaire. If you can infer, declare and go.

Signals, in order: page kind, vibe words, linked URLs / screenshots,
audience, existing brand assets, quiet constraints (a11y, public
sector, kids). Constraints override vibe.

Anti-default (same as our §3, restated as *skip-the-room* tells):
AI-purple mesh, centered hero on dark, three equal feature cards,
glass on everything, Inter + slate-900.

---

## 1. Three knobs (1-10)

Set after the Design Read. Comment on the source post: *putting
density on its own knob is the useful part.*

| Knob | 1 | 10 | Drives |
| --- | --- | --- | --- |
| `DESIGN_VARIANCE` | symmetry, 12-col | masonry, 20vw empty | layout family |
| `MOTION_INTENSITY` | hover/active only | scroll hijack, magnetic | which motion file |
| `VISUAL_DENSITY` | gallery `py-32` | cockpit, mono numbers | spacing + card ban |

**Baseline they use for landings:** `8 / 6 / 4`.
**Baseline we use for app interiors:** `4 / 2 / 8`.
Do not paste their landing baseline onto a dashboard.

### Signal → values

| Signal | V | M | D |
| --- | --- | --- | --- |
| minimal / Linear / editorial | 5-6 | 3-4 | 2-3 |
| premium consumer / Apple-y | 7-8 | 5-7 | 3-4 |
| playful / Awwwards / agency | 9-10 | 8-10 | 3-4 |
| Y2K campaign (`editorial-campaign.md`) | 8-9 | 6-8 | 3-4 |
| ThreeUI hero (`threeui.md`) | 7-8 | 6-8 | 3 |
| trust / public-sector / GOV.UK | 3-4 | 2-3 | 4-5 |
| app interior / dashboard / chat | 3-5 | 1-3 | 7-9 |
| redesign preserve | match | match+1 | match |
| redesign overhaul | +2 | +2 | match |

Variance > 4: avoid a centered hero unless the brief is a manifesto.
Motion > 3: reduced-motion branch is mandatory.
Motion > 7: GSAP pin/scrub only, isolated `'use client'` leaf. CSS
first otherwise (`motion-blocks.md`). Never
`window.addEventListener("scroll")`. Never mix GSAP + Motion +
Three.js in one tree.
Density > 7: no generic cards; 1px rules; tabular numbers.

Their landing default `min-h-[100dvh]` (never `h-screen`) is the
viewport rule. Keep it.

---

## 2. Tells we did not already ban

Our §3 covers blobs, glass soup, emoji icons, Inter-everywhere,
identical radii, `p-[13px]`, purple-as-brand. Add these for
**user-facing copy and marketing chrome**. They do not apply to this
skill file.

**Copy / type**

- Em-dash (`—`) and en-dash-as-separator (`–`) in UI copy. Hyphen `-`
  for compounds and ranges. (Their #1 production tell.)
- Filler verbs: Elevate, Seamless, Unleash, Next-Gen, Revolutionize
- Startup names: Acme, Nexus, SmartFlow, Cloudly
- Jane Doe / Sarah Chan avatars and egg SVGs
- Fake-precise specs (`92%`, `4.1×`) unless the brief gave the number
- "Quietly in use at" / "From the field" / "On our desks"
- Numbered eyebrows (`00 / INDEX`, `001 · Capabilities`)
- Hero version stamps (`V0.6`, `INVITE-ONLY`) unless it is a launch

**Chrome**

- Eyebrow (`uppercase tracking`) **at most 1 per 3 sections**
- Logo wall inside the hero (it goes *under*)
- Scroll cues (`Scroll to explore`, mouse-wheel icon)
- Decorative status dots that are not real state
- Div-fake product screenshots (rects pretending to be a dashboard)
- Pills overlaid on photos; fake photo credits on stock
- Three equal feature cards; 3+ zigzag image/text rows in a row
- Split header: big left title + floating right explainer
- Beige + brass + espresso as the *default* premium-consumer palette
  (`#f5f1ea` / `#b08947` / `#1a1714` family). Rotate: cold luxury,
  forest, black-and-tan, cobalt+cream, olive+brick.
  **Override:** `editorial-campaign.md` cream paper is opt-in when the
  user asked for that register, not the silent default for cookware.

**Type defaults**

- Do not default Fraunces or Instrument Serif. Sans display first
  (Geist, Cabinet Grotesk, Satoshi). Serif only when the brief names
  one or the family is actually editorial/heritage.
- Mixed-family emphasis in one headline is amateur. Italic/bold of the
  *same* face.
- Italic display words with `y g j p q`: `line-height` ≥ 1.1, or the
  descender clips.

**Hero stack (marketing only)**

Max 4 text bits: optional eyebrow, headline ≤ 2 lines, subtext ≤ 20
words, 1 primary CTA + optional secondary. No trust strip, no pricing
teaser, no feature bullets in the hero. Top padding ≤ `pt-24`.
Nav: one line at desktop, height ≤ 80px.

---

## 3. Redesign (do not skip)

Classify first: greenfield / preserve / overhaul. If unclear, one
question: keep the brand, or start visually from scratch?

Audit on paper before CSS: tokens, IA, content blocks, signature
interactions, slop to retire, current dial reading, **SEO baseline**.
SEO migration is the #1 redesign risk.

Never change silently: URL slugs, primary nav labels, form field names
or order, logo/wordmark, legal/consent copy.

Modernise in this order and stop when the brief is done:

1. Type
2. Spacing / rhythm
3. Color (keep brand accent; LILA override if they are already purple)
4. Motion layer
5. Hero recomposition
6. Replace a block only if it is unsalvageable

---

## 4. Image → code (optional extra Lego step)

When there is no site to steal from and an image tool exists:

1. Generate a reference frame (`imagegen-frontend-web` / mobile)
2. Analyze layout tracks (this is still `layout-steal.md`)
3. Implement from tracks + our source picker, not from vibes

Empty grey boxes in a "finished" marketing view are still a fail.
Div-fake screenshots are a fail. Prefer a generated still or a real
component preview.

---

## Agent move

1. Design Read (one line).
2. Set V / M / D from the table. Write them in the reply.
3. If landing/portfolio/redesign: load upstream taste-skill for the
   60-item pre-flight. If app interior: ignore their landing baseline.
4. Pick 3-7 blocks from `sources.md` as always.
5. Run *their* copy/eyebrow/hero tells plus *our* §3 slop list.

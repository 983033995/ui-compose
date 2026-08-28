# ui-lego

An agent skill for composing frontend from proven UI blocks so
AI-generated interfaces don't look like slop.

Coding agents can write CSS and still ship random spacing, invented
buttons, gradient-blob heroes, and motion on every click. This skill
replaces "design it from a blank canvas" with a closed method:

**positive reference → negative (slop) reference → steal a skeleton →
pick 3–7 blocks → map onto one token set → restrain motion.**

## Goals

Full contract: [`references/goals.md`](references/goals.md)

- One visual system per app (tokens, radius, type, density)
- Layout stolen from a real skeleton, not invented cell-by-cell
- Copy-own primitives (shadcn-class) instead of generating a button
- AI-product chrome (stream, think, tools, approve, composer) is real
- Motion has a purpose, a frequency test, and duration ≤ 300ms
- Kit-monogamy: never mix two button/input systems

Non-goals: not an npm component library, not a Linear/Stripe clone,
not permission to dump Magic UI on every surface.

## Install

Drop the folder into the host agent's skills directory.

| Agent | Path |
| --- | --- |
| Claude Code / Codex-style | `.claude/skills/ui-lego/` (keep `SKILL.md` + `references/`) |
| Cursor | `.cursor/skills/ui-lego/` or project rules that point at `SKILL.md` |
| Grok Build | `.grok/skills/ui-lego/` |

The skill is `SKILL.md`. Depth is loaded on demand from `references/`.

## What's inside

| File | What it is |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Workflow, source picker, anti-slop tells, checklists |
| [`references/goals.md`](references/goals.md) | Primary / secondary / non-goals, agent contract |
| [`references/sources.md`](references/sources.md) | Library shopping list (when to use which) |
| [`references/reverse-engineering.md`](references/reverse-engineering.md) | CSS fingerprints from the live sites, steal/skip, decision tree |
| [`references/layout-steal.md`](references/layout-steal.md) | Canonical skeletons (app shell, dashboard, chat, marketing) |
| [`references/ai-primitives.md`](references/ai-primitives.md) | Implementable streaming / thinking / tools / composer |
| [`references/motion-blocks.md`](references/motion-blocks.md) | Tilt, morphing panel, toast stack, when to ship zero motion |
| [`references/editorial-campaign.md`](references/editorial-campaign.md) | Y2K × editorial DTC landings (SOLESHIFT° / SWIRL°) |
| [`references/threeui.md`](references/threeui.md) | 3D / WebGL Lego — ThreeUI catalog, mount, disposal |

## Method (short)

1. Name a real product feel. Do not say "make it modern".
2. Ban the slop tells (aurora hero, emoji icons, `transition: all`,
   `p-[13px]`, purple as default accent).
3. Steal layout tracks first. Color later.
4. Pick 3–7 blocks from `sources.md`. One primitive kit.
5. If the product talks to a model, implement the AI-native minimum set.
6. Keyboard and high-frequency UI: no animation. Everything else ≤ 300ms.

## Reverse-engineering

Libraries were not summarized from their homepages. HTML/CSS was fetched
and tokens, radii, easings, and keyframes recorded. Recurring physics:

- Ease `cubic-bezier(.23, 1, .32, 1)` (or `.22, 1, .36, 1`)
- Open 180–220ms, close ~150ms, enter scale 0.95–0.985 — never `scale(0)`
- Streaming caret 2px × 1em; in-flight tail ~1.6px blur + mask
- Hairline rings `0 0 0 1px`; interior type 13–14px, tracking -0.01em
- Nested radii chip 6 / control 8 / card 10 / window 14

Per-site steal/skip: [`references/reverse-engineering.md`](references/reverse-engineering.md)

Catalog includes Beautiful UI, AICSS, AI Elements, Cult UI, LiveKit
Agents UI, shadcn, ReUI, Kibo, coss, beUI, Rare UI, transitions.dev,
Magic UI, Aceternity, Originkit, Canvas UI, Skiper, orbs, border-beam,
swagui, ThreeUI (Meng To), SOLESHIFT°/SWIRL° campaign register, and
the "you don't need animations" rule.

## Pairing

If the host repo has a design-system skill (`design-ui` or similar),
that skill owns tokens, type, and a11y. This skill owns composition:
which block, which skeleton, which AI primitive. Map stolen blocks onto
the host tokens. Do not invent a second palette.

## License

MIT. The referenced sites remain their authors' work; this repo records
a method and reimplementation notes, not a copy of their components.

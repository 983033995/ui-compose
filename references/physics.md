# Shared UI physics

Host-neutral defaults that recur across restrained product UI. Map every value onto the host token scale. Do not copy these numbers when the host already defines the role.

This file is **physics**, not a library. It exists so agents stop inventing `400ms`, `scale(0)`, `p-[13px]`, and `transition: all`.

## Easing and time

| Role | Default | Notes |
| --- | --- | --- |
| Ease out | `cubic-bezier(0.23, 1, 0.32, 1)` or `cubic-bezier(0.22, 1, 0.36, 1)` | Pick one per app if the host has no equivalent |
| Open / enter | 180–220ms | Menus, sheets, popovers |
| Close / exit | ~150ms | Usually faster than enter |
| Enter scale | 0.95–0.985 | Never `scale(0)` for ordinary UI |
| Press | 0.94–0.96 | Pick one per app and keep it |
| Card enter | 6–8px `translateY`, optional 2px blur | Marketing / rare surfaces only |
| Keyboard highlight | 0ms | Instant background/color |

High-frequency and keyboard-driven interaction: no motion.

Always ship `prefers-reduced-motion: reduce`. Never `transition: all`. Enumerate only the properties that actually change.

Scroll-tied media (marketing / immersive-hero only) is not a timed animation. Map `progress` to scroll, optionally lerp `0.08–0.15` per frame, and snap to a poster under reduced motion. Do not use this physics on app interiors. See `motion-blocks.md` §9.

## Type and measure

These are fallback ranges, not mandatory constants. Prefer host typography and spacing tokens first.

| Role | Fallback |
| --- | --- |
| App-interior body | 13–14px |
| App meta / chrome | 12–12.5px |
| Compact control height | 32px |
| Comfortable control height | 40–44px |
| Reading measure | 60–75ch |
| Product max width | 960–1080px |
| Marketing max width | 1120–1200px |

Refuse ad-hoc spacing (`p-[13px]`, `gap-[17px]`, `max-w-[847px]`) when it bypasses an existing host scale. If a role is genuinely missing, add a token once instead of scattering arbitrary values.

Do not invent a new type scale when the host already has one. Prefer a small set of host size roles and weights. Hierarchy should come from size, weight, color, and spacing together rather than escalating every heading.

## Emphasis and action hierarchy

A region should have a clear primary action or decision. Competing actions become quieter through the host's existing button variants, color, weight, or placement.

Typical mapping:

| Role | Host-native mapping | Use |
| --- | --- | --- |
| Primary | filled / primary variant | save, submit, confirm |
| Secondary | default / outline | cancel, alternative |
| Tertiary | text / ghost / link | optional low-frequency action |
| Destructive | host danger variant | delete, reject, remove |
| Disabled | host disabled state | unavailable action with readable label |

Two equally loud filled actions in one region are a **strong hierarchy warning**, not an automatic failure. Keep both only when the product genuinely presents peer decisions such as Accept/Decline or Approve/Reject.

Empty, error, and zero-data states should usually provide a meaningful next action when one exists: clear filters, retry, create, connect, or return. A decorative illustration alone is not a useful recovery state.

## Radius nesting

Keep concentric roles, not one radius for every node:

| Role | Typical fallback | Use |
| --- | ---: | --- |
| Chip | 6px | badges, tiny tags |
| Control | 8px | buttons, inputs |
| Card | 10–12px | panels |
| Window | 14–16px | dialogs, sheets |

The important rule is relational: nested radii should normally step inward rather than making card, control, and chip visually identical. Host tokens override these example numbers.

## Elevation

Prefer an existing tokenized border/ring before inventing a heavy drop shadow.

```css
box-shadow: 0 0 0 1px var(--host-border);
```

Do not add ambient shadows to every panel. Use hierarchy, spacing, surface contrast, and borders first.

## Streaming (AI surfaces)

Only the in-flight tail is eligible for transient treatment. Already-rendered text stays sharp.

| Token | Fallback |
| --- | --- |
| Caret | 2px × ~1em while generation is active |
| Tail | subtle blur/fade on only the last few in-flight tokens |
| Status shimmer | status line only, never the answer body |

When generation is complete, remove or hide the active caret. Do not leave a completed answer blinking as if it is still working.

Reduced motion: no shimmer, no animated caret, no blur-based movement cue.

See `ai-primitives.md` for the full state set.

## Tabular numbers

When visible numeric values change, keep neighboring layout stable first and add motion only when the change itself communicates useful live state.

| Role | Fallback |
| --- | --- |
| Layout | `font-variant-numeric: tabular-nums` or reserved width |
| Live digit transition | ~200–320ms ease-out when appropriate |
| Table sort / keyboard updates | instant; no per-digit motion |
| Reduced motion | snap directly to the new value |
| Density | product interiors usually skip decorative number motion |

Do not add a number-animation library for static table cells or ordinary formatted amounts. Number-flow libraries are evidence for the trait, not default dependencies.

## Registers

Use these as directional bands, not mathematical laws.

| Register | Density | Motion |
| --- | ---: | ---: |
| App interior | 6–10 | 0–3 |
| AI-native | 5–9 | 0–3 |
| Settings | 4–7 | 0–2 |
| Marketing | 2–5 | 2–6 |
| Editorial campaign | 2–6 | 4–8 |
| WebGL moment | 1–4 | 4–8 |

Marketing baselines do not belong on dashboards. Campaign bounce does not belong on nav, tables, or checkout. Scroll-tied video / 300-frame sequences belong on `immersive-hero` when the media is the demo — not on `marketing-proof-landing` by default, and never on app interiors.

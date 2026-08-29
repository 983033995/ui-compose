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

When a visible numeric value changes (KPI, price, remaining count), keep the layout stable. Animate only if the change is a continuous live update, not a keyboard-driven table sort.

| Role | Fallback |
| --- | --- |
| Digit transition | 200–320ms ease-out, per digit, direction from sign of delta |
| Layout | tabular nums / reserved width so adjacent digits do not shove the row |
| Reduced motion | snap to the new value; no spin, no fade-per-glyph |
| Density | app interiors usually skip this; marketing metrics may use it once |

Do not add a number-animation library to format a static table cell. Prefer host typography (`font-variant-numeric: tabular-nums`) first. Number Flow is evidence for the trait, not a default dependency.

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

Marketing baselines do not belong on dashboards. Campaign bounce does not belong on nav, tables, or checkout.
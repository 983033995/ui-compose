# Shared UI physics

Host-neutral defaults that recur across restrained product UI. Map every value onto the host token scale. Do not copy these numbers when the host already defines the role.

This file is **physics**, not a library. It exists so agents stop inventing `400ms`, `scale(0)`, `p-[13px]`, and `transition: all`.

## Easing and time

| Role | Default | Notes |
| --- | --- | --- |
| Ease out | `cubic-bezier(0.23, 1, 0.32, 1)` or `cubic-bezier(0.22, 1, 0.36, 1)` | One per app |
| Open / enter | 180–220ms | Menus, sheets, popovers |
| Close / exit | ~150ms | Faster than enter |
| Enter scale | 0.95–0.985 | Never `scale(0)` for ordinary UI |
| Press | 0.94–0.96 | Pick one per app and keep it |
| Card enter | 6–8px `translateY`, optional 2px blur | Marketing / rare surfaces only |
| Keyboard highlight | 0ms | Instant background/color |

High-frequency and keyboard-driven interaction: no motion.

Always ship `prefers-reduced-motion: reduce`. Never `transition: all`. Enumerate `opacity, transform, box-shadow, background-color, color`.

## Type and measure

| Role | Default |
| --- | --- |
| App-interior body | 13–14px, tracking `-0.01em` |
| App meta / chrome | 12–12.5px |
| Compact control height | 32px |
| Comfortable control height | 40–44px |
| Reading measure | 60–75ch |
| Product max width | 960–1080px |
| Marketing max width | 1120–1200px |

Refuse ad-hoc spacing (`p-[13px]`, `gap-[17px]`, `max-w-[847px]`). If a step is missing, add it once to the host scale.

## Radius nesting

Keep concentric roles, not one radius for every node:

| Role | Typical px | Use |
| --- | ---: | --- |
| Chip | 6 | badges, tiny tags |
| Control | 8 | buttons, inputs |
| Card | 10–12 | panels |
| Window | 14–16 | dialogs, sheets |

Inner radius must be smaller than the parent. Identical radius on card and inner control is a hard fail.

## Elevation

Prefer a 1px tokenized ring over a fat border or drop shadow:

```css
box-shadow: 0 0 0 1px var(--host-border);
```

Dark mode: the same ring, lighter border token. Do not add a second ambient shadow on every card.

Dashed separators are legitimate on editorial / docs shells. Do not use them on dense data tables.

## Streaming (AI surfaces)

Only the in-flight tail is soft. Already-rendered text stays sharp.

| Token | Default |
| --- | --- |
| Caret | 2px × ~1em, `step-end` 1s blink when idle |
| Caret while tokens arrive | solid (no blink) |
| Tail | ~1.6px blur + right-edge fade mask, last few tokens only |
| Status shimmer | status line only, never the whole answer |

Reduced motion: solid caret, no blur, no shimmer.

See `ai-primitives.md` for the full state set. Copy CSS from there and retarget host tokens.

## Registers

Do not mix these on one surface.

| Register | Density | Motion |
| --- | ---: | ---: |
| App interior | 6–10 | 0–3 |
| AI-native | 5–9 | 0–3 |
| Settings | 4–7 | 0–2 |
| Marketing | 2–5 | 2–6 |
| Editorial campaign | 2–6 | 4–8 |
| WebGL moment | 1–4 | 4–8 |

Marketing baselines do not belong on dashboards. Campaign bounce does not belong on nav, tables, or checkout.

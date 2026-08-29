# Adapter: Vue + UnoCSS

Use when Host Read confirms Vue and UnoCSS are active.

## Rules

- Reuse existing Uno shortcuts, presets, theme aliases, and variant conventions.
- Prefer semantic shortcuts over long one-off atomic strings when a pattern repeats.
- Do not import Tailwind-specific class recipes verbatim; translate intent into the host Uno vocabulary.
- Keep existing Vue component APIs and composition patterns.
- Use scoped CSS for exceptional visual fingerprints when atomic utilities would become unreadable.

## Translating reference traits

For each selected external trait, identify:

1. structure — grid, alignment, sticky/fixed behavior;
2. visual tokens — surface, text hierarchy, radius, border, shadow;
3. interaction — hover/focus/open/close/selection;
4. motion — duration/easing/transform;
5. state — loading/empty/error/disabled.

Then implement those five concerns with the host's existing Vue + UnoCSS conventions.

## Avoid

- adding Tailwind only to consume a copied block;
- arbitrary values when a semantic Uno token exists;
- duplicating theme values between Uno config and local CSS;
- using animation utilities on high-frequency keyboard interactions.

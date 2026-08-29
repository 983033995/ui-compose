# Extract the skeleton first

Blank-canvas generation often produces arbitrary boxes. UI Compose should choose a proven page architecture first, then adapt it to the host project.

Do layout before color. Do structure before motion.

## Method

1. Identify the **surface** and primary **jobs**.
2. Choose one skeleton from `references/skeletons/registry.yaml`.
3. Preserve useful relationships: tracks, hierarchy, gutters, sticky regions, list/detail behavior, mobile collapse order.
4. Discard source-specific colors, type, assets, copy, and decorative identity.
5. Map implementation to the host project's tokens, components, and responsive conventions.
6. Fill real states: loading, empty, error, disabled, success, selection, and mobile.

If the skeleton cannot be named or justified, stop and choose one before styling.

## Registers

| Register | Typical density | Typical motion | Use |
| --- | ---: | ---: | --- |
| Marketing | 2–5 | 2–6 | Landing, launch, pricing, docs hero |
| App interior | 6–10 | 0–3 | Dashboards, CRUD, settings, tables, search |
| AI-native | 5–9 | 0–3 | Chat, task execution, approvals, tools |
| Editorial campaign | 2–6 | 4–8 | DTC lookbooks and expressive product worlds |
| WebGL moment | 1–4 | 4–8 | One bounded 3D/visualization stage |

These are directional, not universal presets.

## Canonical skeletons

The structured registry is authoritative: `references/skeletons/registry.yaml`.

Current baseline includes:

- `master-detail-workspace`
- `data-workspace`
- `settings-workspace`
- `command-workspace`
- `agent-chat-workspace`
- `agent-task-workspace`
- `marketing-proof-landing`
- `editorial-product-explorer`
- `immersive-hero`

### Master/detail workspace

Use when users repeatedly browse a collection and inspect or edit one item.

```text
Desktop
┌────────────────────────────────────────────┐
│ topbar                                     │
├───────────────┬────────────────────────────┤
│ toolbar/list  │ detail                     │
│               │                            │
└───────────────┴────────────────────────────┘

Mobile
list → detail route/sheet
```

Do not force a desktop split pane onto a narrow viewport.

### Data workspace

Use for operational dashboards, reporting, inventory, and high-frequency data tools.

```text
app-nav
  └─ page-header
      └─ controls
          └─ summary
              └─ primary data region
                  └─ secondary data region
```

The primary data region should dominate. Do not manufacture decorative KPI cards or charts when they do not support a real decision.

### Settings workspace

Use stable navigation + readable sections. Keep destructive actions visually and semantically separated. Avoid wrapping every setting in an identical card.

### Command workspace

Command surfaces should optimize for speed, ranking, keyboard operation, and a clear pointer/touch fallback. Preview is optional and should never steal focus unexpectedly.

### Agent workspace

Chat and task execution are different skeletons:

- chat: thread + activity + composer
- task runner: progress + execution list + output/artifacts + approval

Do not reduce both to generic chat bubbles.

### Marketing proof landing

Prioritize one claim, one proof sequence, and one primary CTA. Avoid the default "three equal feature cards" unless the content genuinely has three equal concepts.

### Editorial / immersive surfaces

These may be expressive, but composition still comes first. Use one coherent motif family, preserve touch access, and provide reduced-motion/performance fallbacks.

## Spacing and width

Use the host scale. Do not invent arbitrary values merely to match a screenshot.

Typical roles to map into host tokens:

- compact control height
- comfortable control height
- mobile page gutter
- desktop page gutter
- card/section padding
- reading measure
- bounded product width
- marketing max width

If the host does not have the needed token, add a deliberate reusable step rather than scattered one-off values.

## Reference extraction protocol

When the user points at a screenshot, site, or product:

1. Extract **structure** — regions, tracks, hierarchy, sticky behavior, collapse order.
2. Extract **interaction** — focus model, preview, command behavior, selection, states.
3. Extract **density and motion** — how much information and movement the task actually needs.
4. Extract **tokens as relationships**, not literal brand values — surface hierarchy, contrast steps, radius nesting, type hierarchy.
5. Rebuild using the host project's implementation vocabulary.

Do not clone brand assets, illustrations, copy, source code, or a proprietary visual identity. Learn from the system; re-express the decision.

# Rendered benchmark harness

The harness defines how UI Compose benchmark runs should be executed and captured. It is intentionally implementation-agnostic: the same protocol should work whether the host fixture is Vue, React, UnoCSS, Tailwind, or an internal design system.

## Goal

Produce reproducible evidence for the claims in `DELIVERY.md` without tuning the test after seeing one model's output.

A benchmark run should separate three things:

1. **Case contract** — the product job and host constraints in `evals/cases/`.
2. **Generated implementation** — the code produced under one comparison mode.
3. **Observed result** — build/runtime/artifact/score evidence stored under `evals/results/`.

## Recommended fixture layout

A future executable fixture may use:

```text
evals/harness/fixtures/
  vue-element-plus/
  vue-unocss/
  react-tailwind-local-primitives/
  custom-design-system/
```

Fixtures should be intentionally small but realistic enough to expose host behavior:

- package manifest and lockfile
- theme/tokens
- existing primitive wrappers
- one representative existing screen
- lint/build scripts
- accessibility conventions where applicable

Do not create an empty starter and call it an “existing design system” test.

## Run isolation

Each comparison mode starts from the same clean fixture commit/snapshot.

Recommended run modes:

```text
model-only
generic-frontend-design
taste-oriented
ui-compose
taste-plus-ui-compose
```

Do not let one mode inherit dependencies or generated files from another mode.

## Capture protocol

For each run:

### Before

Record:

- fixture identifier/commit
- package lock hash or equivalent dependency baseline
- model identifier
- skill/mode identifier
- exact prompt/case version
- UI Compose commit/version when used

### Generate

Let the model/agent modify the fixture under the selected mode.

Do not manually fix composition decisions before scoring. If a run cannot build, record the failure rather than repairing it and presenting the repaired result as the original run.

### Build

Run the fixture's normal install/build/test workflow.

Record:

- passed / failed / not-run
- relevant error summary
- dependency additions/removals/updates
- runtime console/hydration errors

### Render

Capture at minimum:

- desktop viewport (recommended 1440×900 or fixture-specific equivalent)
- mobile viewport around 390×844

When meaningful, also capture:

- loading
- empty
- error
- selected/bulk-action state
- open detail/dialog/sheet
- AI tool running/failure/approval state

Screenshots should use the same viewport and representative data across comparison modes.

### Interaction checks

Record short factual notes for:

- keyboard traversal and visible focus
- primary control labels/semantics
- mobile overflow and touch target behavior
- reduced-motion path
- state persistence (filters, selection, preview, approval)

Do not infer accessibility from visual appearance alone.

### Score

Apply `evals/rubric.md` after the run is captured.

Record decision errors separately from visual scores. Examples:

- `wrong-skeleton`
- `ignored-host-system`
- `unnecessary-dependency`
- `missing-state`
- `mobile-failure`

A visually attractive result can still fail composition quality.

## Dependency diff

Dependency discipline is a first-class benchmark signal.

At minimum compare package manifests before/after and classify each change:

```json
{
  "name": "some-package",
  "change": "added",
  "reason": "model added a second dialog primitive system"
}
```

An empty list is meaningful evidence when UI Compose completes the task using the host vocabulary.

## Screenshot integrity

Artifacts should show the actual rendered output from the recorded run. Do not:

- mock a screenshot after the fact
- replace a failed state with a design-tool recreation
- crop away overflow or broken regions to improve appearance
- compare different data/viewport states between modes

Image optimization is fine if it does not alter visible content.

## Result record

Store the observed run as JSON following:

- `schemas/eval-result.schema.json`
- `evals/results/README.md`

Run:

```bash
python scripts/validate_evals.py
```

A result with `build_status: passed` must reference both desktop and mobile artifacts. This makes “rendered benchmark evidence” a verifiable repository state rather than a narrative claim.

## Minimal first benchmark batch

Do not attempt all nine cases at once. The first empirical batch should maximize information gain:

1. `01-vue-element-plus-orders` — tests host preservation + dense B2B composition.
2. `02-agent-chat` — tests AI-native state modeling.
3. `04-react-tailwind-data-workspace` — tests React/Tailwind without shadcn-by-default.
4. `09-custom-design-system` — strongest framework/primitive portability test.

Once these are stable, extend into marketing/editorial/WebGL cases.

## What the harness should tell us

The benchmark is useful only if it can answer questions such as:

- Does UI Compose choose better page architecture than model-only generation?
- Does it preserve the host component system more consistently?
- Does it add fewer unnecessary dependencies?
- Does it cover product states that generic visual skills omit?
- Does combining a taste skill with UI Compose improve visual direction without degrading product structure?
- Which failures justify adding a new Pattern, Skeleton, Adapter, or rule?

If an eval failure cannot be connected to one of those decisions, avoid growing the skill merely to optimize a benchmark screenshot.

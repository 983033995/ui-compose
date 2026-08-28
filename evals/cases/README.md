# UI Compose Eval Cases

Eval cases turn the rubric into repeatable product-design tasks. A case is not a visual snapshot specification; it defines the host constraints, product job, expected composition decisions and failure conditions that UI Compose should reason about.

## Case contract

Each case should include:

1. **Goal** — what capability is under evaluation.
2. **Host fixture** — framework, styling, component system and existing constraints.
3. **Task brief** — the user-visible product job.
4. **Expected composition** — likely skeleton and pattern candidates. These are review expectations, not pixel prescriptions.
5. **Host integration expectations** — what must be preserved or reused.
6. **Hard failures** — conditions that should cap the rubric score.
7. **Review notes** — decision errors worth recording separately.

## Run modes

When practical, run the same case in these modes:

- model only
- generic frontend-design skill
- taste-oriented skill
- UI Compose
- taste-oriented skill + UI Compose

Keep the host fixture and task brief identical between modes.

## Capture

For every run record:

- model and skill versions
- prompt
- selected skeleton/patterns if exposed
- dependency changes
- build/test result
- desktop screenshot
- ~390px mobile screenshot
- keyboard/reduced-motion notes
- rubric score
- decision-error classes

Do not tune the case after seeing one model's output unless the change is versioned and applied to every comparison mode.

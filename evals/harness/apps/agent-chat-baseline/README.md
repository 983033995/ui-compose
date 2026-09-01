# Agent Chat executable fixture

Executable baseline for **Eval 02 — Agent Chat**.

This fixture intentionally uses no public UI component kit. Its implementation vocabulary is a tiny host-owned primitive layer plus semantic HTML/CSS, so benchmark runs can reveal whether an agent preserves the host system or imports a familiar AI/component stack without justification.

## Contract covered

- streaming response with keyboard-operable Stop
- tool queued / running / success / failure states with textual status
- consequential approval naming both consequence and scope
- disconnected and retryable-error states
- persistent composer at desktop and ~390px mobile widths, including a reduced-height keyboard simulation
- visible focus and reduced-motion fallback
- provider-exposed events only; no fabricated hidden chain-of-thought

## Commands

```bash
pnpm install --frozen-lockfile
pnpm test
pnpm build
pnpm dev
```

`pnpm test` validates the source contract. `pnpm build` emits a dependency-free static `dist/` directory.

CI additionally installs Playwright **ephemerally as benchmark infrastructure**, launches the built fixture, and captures desktop/mobile screenshots plus machine metrics for overflow, keyboard actions, focus outline, reduced motion, composer reachability, runtime errors, required states, and hidden-reasoning copy. Playwright is not part of the host UI dependency contract.

The capture layer uses semantic `data-state`, `data-action`, and `data-eval` hooks rather than incidental CSS classes or exact visible copy. See `CAPTURE-CONTRACT.md`. These hooks are evaluation instrumentation only: transformed runs may freely change layout, styling, component boundaries and user-facing wording while preserving observable product semantics.

For isolated evidence, `.github/workflows/build-eval-fixtures.yml` can be run manually against the transformed branch with an `eval02_run_id` and one of `baseline`, `model-only`, or `ui-compose`. Each run writes to its own artifact directory and records the source SHA in `metrics.json`.

This fixture is a host baseline, not an Eval result. Model-only and UI Compose result records must only be added after actual transformed runs are captured and reviewed.

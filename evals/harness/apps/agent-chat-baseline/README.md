# Agent Chat executable fixture

Executable baseline for **Eval 02 — Agent Chat**.

This fixture intentionally uses no public UI component kit. Its implementation vocabulary is a tiny host-owned primitive layer plus semantic HTML/CSS, so benchmark runs can reveal whether an agent preserves the host system or imports a familiar AI/component stack without justification.

## Contract covered

- streaming response with keyboard-operable Stop
- tool queued / running / success / failure states with textual status
- consequential approval naming both consequence and scope
- disconnected and retryable-error states
- persistent composer at desktop and ~390px mobile widths
- visible focus and reduced-motion fallback
- provider-exposed events only; no fabricated hidden chain-of-thought

## Commands

```bash
pnpm install --frozen-lockfile
pnpm test
pnpm build
pnpm dev
```

`pnpm test` validates the fixture contract. `pnpm build` emits a dependency-free static `dist/` directory for later rendered capture.

This fixture is a host baseline, not an Eval result. Model-only and UI Compose result records must only be added after actual rendered runs are captured and reviewed.

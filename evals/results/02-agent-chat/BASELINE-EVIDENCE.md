# Eval 02 — Agent Chat baseline evidence

Status: **rendered baseline ready; comparative model runs pending**.

This file records CI-observed evidence for the frozen host baseline only. It is **not** a model-only or UI Compose benchmark result and carries no rubric score.

## Provenance

- Host fixture: `evals/harness/apps/agent-chat-baseline`
- Fixture contract: `evals/harness/fixtures/agent-chat.yaml`
- Case: `evals/cases/02-agent-chat.md`
- Captured branch head: `e208c20b6175d5119442422b89e288f524e0a4f8`
- Build Eval Fixtures run: `33242319428`
- Artifact: `eval-02-agent-chat-baseline`
- Artifact id: `9711722658`
- Artifact digest: `sha256:2fcdd076ccbd0bd7f3bec1efb5c65e2a0ff50a38ef81fc6b21b94fc970a7faea`

## Rendered evidence

The CI capture produced:

- `desktop.png` at 1440×1000
- `mobile.png` at 390×844
- `metrics.json`

Observed metrics:

| Check | Observation |
| --- | --- |
| Console errors | none |
| Page errors | none |
| Desktop horizontal overflow | false |
| Mobile horizontal overflow | false |
| Required lifecycle states | all 8 present |
| Hidden reasoning / chain-of-thought copy in rendered UI | false |
| Stop keyboard activation | passed |
| Retry keyboard activation | passed |
| Approve keyboard activation | passed |
| Focus outline on Stop/Retry/Approve | solid 2px |
| Mobile composer at 390×844 | reachable; top 689, bottom 844 |
| Reduced-height keyboard simulation at 390×560 | composer reachable; top 405, bottom 560 |
| Focus after keyboard simulation | `#message` textarea |
| Reduced-motion media query | matched |
| Streaming caret animation under reduced motion | `none` |
| Hard failures | none |

Required rendered states confirmed:

- `streaming`
- `tool-queued`
- `tool-running`
- `tool-success`
- `tool-failure`
- `approval-required`
- `disconnected`
- `retryable-error`

## What this proves

The frozen host fixture and evidence pipeline are usable for a fair comparison. They can distinguish runtime/state/accessibility/mobile failures without depending on subjective visual review alone.

The baseline also establishes the host constraints that transformed runs must preserve:

- no default AI/component-library dependency;
- provider-visible activity only, never fabricated hidden chain-of-thought;
- textual tool status, not color-only state;
- explicit approval consequence and scope;
- keyboard-operable Stop, Retry, and approval actions;
- composer reachable at ~390px and under a reduced-height virtual-keyboard simulation;
- reduced-motion fallback;
- no page-level horizontal overflow.

## What this does not prove

No comparative claim is valid yet. We still need two actual transformed runs from the same frozen baseline:

1. `model-only`
2. `ui-compose`

Their source changes, dependency changes, build/runtime result, rendered screenshots, machine metrics, composition decisions, rubric scores, hard failures, and decision errors must be recorded before Eval 02 can be closed.

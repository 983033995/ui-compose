# Eval 02 capture observability contract

This file defines **evaluation-only hooks** that must survive both transformed runs. They do not prescribe layout, styling, component hierarchy, copy, framework, or product architecture.

The purpose is to let the same browser capture script observe model-only and UI Compose runs without depending on incidental CSS class names or exact English copy.

## Stable hooks

Transformed runs may redesign or refactor the UI, but must preserve these semantic hooks on the element that owns the behavior:

| Hook | Meaning |
| --- | --- |
| `data-state="streaming"` | active streamed assistant output |
| `data-state="tool-queued"` | queued tool execution |
| `data-state="tool-running"` | running tool execution |
| `data-state="tool-success"` | successful tool execution |
| `data-state="tool-failure"` | failed tool execution |
| `data-state="approval-required"` | consequential action awaiting approval |
| `data-state="disconnected"` | disconnected provider/session state |
| `data-state="retryable-error"` | retryable failure state |
| `data-action="stop"` | Stop control |
| `data-action="retry"` | Retry control |
| `data-action="approve"` | approval control |
| `data-eval="composer"` | persistent composer container |
| `data-eval="message-input"` | primary composer text input |
| `data-eval="stream-caret"` | transient streaming caret/indicator used for reduced-motion verification |
| `data-eval="action-notice"` | evaluator-visible action result/status node |

The action notice also exposes `data-eval-result` after an action. Current required values are `stop`, `retry`, `approve`, and `send`. Visible user copy may change independently.

## What may change freely

- CSS classes
- DOM nesting and component boundaries
- typography and spacing
- desktop/mobile composition
- visible action/status copy, provided semantics remain clear
- framework implementation details
- tool-detail presentation
- source/context inspection presentation

## Invalid run vs product failure

Removing or renaming these hooks makes the automated capture unable to compare the two modes fairly. Treat that as an **invalid benchmark run**, not as a product-quality hard failure. Restore the hooks without changing visible product behavior, then recapture.

Do not add evaluator-only UI or hidden product state just to satisfy the benchmark. The hooks must annotate real product-visible state and real controls.

## Run metadata

`capture.mjs` accepts:

- `EVAL_RUN_ID` — stable artifact directory/id
- `EVAL_MODE` — `baseline`, `model-only`, or `ui-compose`
- `EVAL_SOURCE_SHA` — source commit recorded in `metrics.json`
- `EVAL_BASE_URL` — optional fixture URL override
- `EVAL_OUTPUT_DIR` — optional artifact directory override

The default remains the frozen `agent-chat-baseline`, so ordinary fixture CI behavior is unchanged.

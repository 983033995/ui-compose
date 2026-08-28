# Eval 01 — Vue 3 + Element Plus Order Workspace

## Goal

Evaluate whether UI Compose can produce a dense B2B order-management workspace that feels native to an existing Vue 3 + Element Plus product without adding a second UI system.

## Host fixture

- Vue 3 + Vite + TypeScript
- Element Plus already installed
- existing CSS variables for color, spacing, radius and typography
- no Tailwind
- no Radix/shadcn
- existing table, dialog and form wrappers

## Task brief

Build an order management page with:

- keyword search
- order status filtering
- date filtering
- result count
- dense order list/table
- row inspection without losing list context
- multi-select bulk action
- loading, empty and error states
- mobile behavior around 390px

## Expected composition

Primary skeleton:

- `master-detail-workspace`

Expected pattern candidates:

- `dense-filter-toolbar`
- `master-detail-preview`
- `view-options-control`
- `sticky-contextual-actions`

## Host integration expectations

- reuse Element Plus controls and existing wrappers
- do not add Tailwind, shadcn, Radix or another table library
- adapt spacing/radius/type to existing host tokens
- preserve accessible labels and keyboard semantics

## Hard failures

- introduces another primitive/control system without necessity
- renders table as generic card grid
- master/detail layout causes severe mobile overflow
- bulk actions do not communicate selected scope
- filter state is visually hidden
- primary controls are pointer-only

## Review notes

Record wrong-skeleton, wrong-density, dependency, accessibility and mobile failures separately from visual polish issues.

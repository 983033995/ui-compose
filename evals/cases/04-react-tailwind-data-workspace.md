# Eval 04 — React + Tailwind Data Workspace

## Goal

Evaluate whether UI Compose can compose a dense analytics/data workspace in a React + Tailwind host while respecting existing local primitives rather than assuming shadcn/Radix must be introduced.

## Host fixture

- React 19 + Vite + TypeScript
- Tailwind already installed
- local Button/Input/Select/Popover/Table primitives already exist
- CSS variables define color, radius and typography
- no shadcn CLI setup
- no Radix dependency

## Task brief

Build a customer analytics workspace with:

- searchable/filterable records
- segment/status filtering
- configurable visible columns
- sorting/grouping controls
- dense table/list view
- selection and contextual bulk actions
- summary metrics that support, rather than replace, the data workspace
- loading, empty and error states
- ~390px mobile strategy

## Expected composition

Primary skeleton:

- `data-workspace`

Expected pattern candidates:

- `dense-filter-toolbar`
- `view-options-control`
- `sticky-contextual-actions`

## Host integration expectations

- reuse existing local controls
- use existing Tailwind theme/token vocabulary
- do not install shadcn/Radix merely because reference evidence came from those ecosystems
- metrics should not turn the entire page into a generic card dashboard
- table semantics and keyboard access remain intact

## Hard failures

- adds a second primitive system without a missing-behavior justification
- replaces the core table workflow with decorative cards
- hides active filter/sort state
- mobile strategy is horizontal overflow only
- bulk action scope is ambiguous
- uses arbitrary Tailwind values when host tokens already cover the role

## Review notes

This case specifically tests the distinction between “React + Tailwind” and “shadcn by default.” Dependency discipline is a first-class score dimension.

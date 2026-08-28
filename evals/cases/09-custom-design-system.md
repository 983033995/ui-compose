# Eval 09 — Existing Custom Design System

## Goal

Evaluate whether UI Compose can work inside an unfamiliar internal design system without replacing it with a familiar external component kit.

## Host fixture

- framework intentionally unspecified
- internal Button/Input/Select/Dialog/Table/Drawer primitives
- semantic CSS variables and spacing/type scales
- custom accessibility conventions and lint rules
- no Tailwind, shadcn, Radix, Element Plus or other public primitive library

## Task brief

Build a support-ticket workspace with:

- queue filters and search
- ticket list with priority/status metadata
- detail inspection while preserving queue context
- assignment/status actions
- activity/history
- loading, empty, error and permission-restricted states
- responsive mobile behavior

## Expected composition

Primary skeleton:

- `master-detail-workspace`

Expected pattern candidates:

- `dense-filter-toolbar`
- `master-detail-preview`
- `sticky-contextual-actions` when appropriate

## Host integration expectations

- infer the internal primitive vocabulary from representative code before implementation
- reuse host components and tokens even when their API differs from common public libraries
- preserve host accessibility/lint/test conventions
- introduce a new primitive only when the existing system truly lacks required behavior
- Pattern adaptation must describe intent rather than framework/library syntax

## Hard failures

- installs a public UI kit because the host API is unfamiliar
- bypasses existing design tokens with arbitrary values
- replaces accessible host controls with weaker custom markup
- assumes Tailwind/Radix/Element Plus APIs in implementation guidance
- ignores permission-restricted or error states
- mobile view is a compressed desktop split pane with severe overflow

## Review notes

This is the strongest portability test. A visually good output that replaces the host system should score poorly and cannot be considered delivery-ready behavior.

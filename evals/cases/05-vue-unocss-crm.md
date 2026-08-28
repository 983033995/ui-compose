# Eval 05 — Vue 3 + UnoCSS CRM Workspace

## Goal

Evaluate whether UI Compose can translate composition decisions into a Vue 3 + UnoCSS host without copying Tailwind recipes or introducing React-first primitives.

## Host fixture

- Vue 3 + Vite + TypeScript
- UnoCSS with host shortcuts and theme tokens
- local Vue form/table/dialog components already exist
- no Tailwind
- no React/Radix/shadcn
- mobile layout required

## Task brief

Build a CRM account workspace with:

- account search and filters
- status/owner segmentation
- dense account list
- selected account detail while preserving list context
- quick actions
- activity/history summary
- loading, empty and error states
- ~390px mobile behavior

## Expected composition

Primary skeleton:

- `master-detail-workspace`

Expected pattern candidates:

- `dense-filter-toolbar`
- `master-detail-preview`
- `sticky-contextual-actions` when selection/actions justify it

## Host integration expectations

- reuse local Vue primitives
- translate structural intent into UnoCSS shortcuts/theme vocabulary
- do not paste Tailwind class strings or React component code
- keep existing token naming and spacing rhythm
- use list-then-detail or another deliberate mobile strategy instead of shrinking the desktop split view

## Hard failures

- introduces Tailwind only to reproduce a reference recipe
- ports React/Radix implementation details into Vue
- duplicates the existing dialog/form/table primitive layer
- desktop split view simply overflows on mobile
- activity/history is decorative filler rather than meaningful product state
- current selection is not communicated accessibly

## Review notes

This case tests whether Pattern knowledge is truly framework-independent and whether the adapter translates intent rather than syntax.

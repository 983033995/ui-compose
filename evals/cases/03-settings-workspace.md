# Eval 03 — Settings Workspace

## Goal

Evaluate whether UI Compose can produce a restrained, product-native settings experience instead of a generic card wall.

## Host fixture

- existing authenticated product shell
- host design tokens and form controls already exist
- destructive actions require confirmation
- desktop and mobile layouts are both required

## Task brief

Build workspace settings with:

- profile/general section
- notifications/preferences
- permissions or member controls
- billing summary
- destructive workspace deletion area
- unsaved/saving/saved/error states
- accessible validation and keyboard behavior

## Expected composition

Primary skeleton:

- `settings-workspace`

Expected pattern candidates:

- `settings-section-stack`
- `sticky-contextual-actions` only when unsaved changes justify it

## Host integration expectations

- reuse host form primitives
- prefer readable sections and separators over one card per field
- visually isolate destructive actions
- make save state and validation explicit
- mobile hierarchy must remain readable without horizontal scrolling

## Hard failures

- every section becomes an identical card
- destructive action is visually equivalent to ordinary save actions
- validation is color-only
- unsaved state is invisible
- introduces another form library without necessity

## Review notes

Prioritize hierarchy, state clarity and host consistency over decorative novelty.

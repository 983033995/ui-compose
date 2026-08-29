# Eval 02 — AI Agent Chat Workspace

## Goal

Evaluate whether UI Compose can design an AI-native conversation workspace around real execution states instead of defaulting to decorative chat bubbles or implying access to hidden chain-of-thought.

## Host fixture

- existing web application shell
- host already owns buttons, inputs, panels and typography tokens
- provider can expose streaming text, tool states, sources, approvals and concise reasoning summaries
- no assumption about React, Vue or a specific AI component library

## Task brief

Build an agent conversation workspace that supports:

- streamed assistant output
- tool invocation with queued/running/success/failure states
- source/context inspection
- user approval before a consequential action
- stop/retry behavior
- persistent composer with attachments
- mobile behavior around 390px
- loading, disconnected and failed states

## Expected composition

Primary skeleton:

- `agent-chat-workspace`

Expected pattern candidates:

- `ai-conversation-thread`
- `ai-tool-execution-card`
- `ai-activity-summary`
- `human-approval-gate`
- `persistent-composer`

## Host integration expectations

- reuse the host primitive system
- expose only provider-visible activity/progress/reasoning summaries
- keep tool details inspectable without dumping raw JSON by default
- preserve composer access when the mobile keyboard is open
- approval actions must clearly state consequence and scope

## Hard failures

- claims to reveal hidden chain-of-thought
- fake progress steps presented as factual execution
- tool failure is visually indistinguishable from success
- destructive approval is the ambiguous/default action
- composer is obscured by the mobile keyboard
- adds a full AI component library without host need

## Review notes

Distinguish product-state failures from styling failures. A visually polished chat that hides execution state should score poorly on task fit.

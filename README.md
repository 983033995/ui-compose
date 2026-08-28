# UI Compose

**UI Compose is a stack-aware UI composition engine for coding agents.**

It does not exist to install or copy popular UI libraries. It studies the useful parts of proven interfaces — layout systems, density, interaction models, motion physics, AI-native states, and product-specific composition patterns — then re-expresses those traits using the host project's own framework, components, tokens, and conventions.

> Taste decides the direction. UI Compose decides how to build it.

## Why this exists

Coding agents can generate valid frontend code and still produce generic UI: random spacing, disconnected cards, fashionable effects with no product logic, unnecessary dependencies, or interfaces that ignore the host design system.

UI Compose replaces blank-canvas generation with a decision pipeline:

**Host Read → Design Read → Skeleton → Pattern Set → Adapter → Verify**

The key difference from a component library is that the output should remain **native to the host project**.

## What UI Compose learns from external libraries

Popular UI projects are treated as research sources, not defaults.

UI Compose may extract traits such as:

- app-shell and master/detail relationships
- dense data toolbars
- nested radius hierarchy
- stream/progress/tool/approval states for AI products
- menu/panel motion physics
- editorial product-world switching
- restrained ambient marks
- single-scene WebGL composition

It should not blindly install, vendor, or clone the source library.

See:

- [`references/sources/registry.yaml`](references/sources/registry.yaml) — structured source/trait registry
- [`references/sources/provenance.md`](references/sources/provenance.md) — source and license boundaries

## Core workflow

### 1. Host Read

Before design decisions, detect:

- framework/runtime
- styling system
- active component/primitive system
- existing tokens/design system
- motion stack
- representative product patterns
- accessibility/responsive/runtime constraints

Never assume React, Tailwind, Radix, or a particular file layout.

### 2. Design Read

Interpret the surface, audience, product register, and visual direction. Use V/M/D (variance / motion / density) as directional controls rather than universal presets.

### 3. Skeleton

Choose the page architecture before styling. Layout relationships and information hierarchy do more to prevent generic AI UI than another effect library.

### 4. Pattern Set

Select roughly 3–7 useful traits/patterns. Prefer translating traits into host-native code over importing a library.

### 5. Adapter

Apply the closest stack adapter. Current baseline:

- React + Tailwind
- Vue + Element Plus
- Vue + UnoCSS
- Generic CSS / existing design system

### 6. Verify

Render and inspect desktop/mobile, keyboard/focus states, loading/empty/error states, reduced motion, overflow, and runtime errors.

## AI-native UI

UI Compose treats AI products as a first-class category. It provides composition guidance for:

- streaming response
- activity/progress summary
- tool execution state
- approval gates
- composer/context
- retry/error/cancel
- task lifecycle

It intentionally avoids implying that hidden chain-of-thought is available. UI should expose provider-supported activity, summarized reasoning, or execution traces only.

## Project structure

```text
ui-compose/
  SKILL.md
  README.md
  references/
    host-read.md
    layout-steal.md
    ai-primitives.md
    motion-blocks.md
    editorial-campaign.md
    threeui.md
    taste-dials.md
    adapters/
      react-tailwind.md
      vue-element-plus.md
      vue-unocss.md
      generic-css.md
    sources/
      registry.yaml
      provenance.md
  evals/
    rubric.md
```

The repository is still early. The goal of v0.2 is to establish the architecture before expanding the source catalog further.

## Install

Use the Agent Skills convention supported by your coding agent. For portable repo-level usage, prefer a folder named after the skill, for example:

```text
.agents/skills/ui-compose/
  SKILL.md
  references/
  evals/
```

Some clients also support their own compatibility locations such as `.cursor/skills/`, `.claude/skills/`, or `$CODEX_HOME/skills` for user-level installation. Keep the folder name aligned with the `name: ui-compose` frontmatter.

## Evaluation

The project will not claim quality improvements based only on the prompt text. The benchmark plan is defined in [`evals/rubric.md`](evals/rubric.md).

Initial evaluation targets include:

- B2B dashboard
- settings/CRUD workspace
- AI agent chat + tools + approval
- SaaS landing
- editorial product explorer
- WebGL hero
- React/Tailwind host
- Vue/Element Plus host
- Vue/UnoCSS host
- existing internal design system

## Non-goals

UI Compose is not:

- an npm component library
- a replacement design system
- a clone of popular product brands
- a bundle of fashionable effects
- permission to mix multiple primitive kits
- a reason to replace accessible host controls with custom markup

## Source policy

External projects remain their authors' work. UI Compose records original methodology, abstractions, and independently reimplementable observations. Upstream source code/assets/trademarks retain their original licenses and rights.

## License

MIT for original material in this repository. Third-party material is not relicensed by this project.

# UI Compose

**UI Compose is a stack-aware UI composition engine for coding agents.**

It does not exist to install or copy popular UI libraries. It studies useful decisions from proven interfaces — layout systems, density, interaction models, motion physics, AI-native states, and product-specific composition patterns — then re-expresses those traits using the host project's own framework, components, tokens, and conventions.

> Taste decides the direction. UI Compose decides how to build it.

## Why this exists

Coding agents can generate valid frontend code and still produce generic UI: random spacing, disconnected cards, fashionable effects with no product logic, unnecessary dependencies, weak product states, or interfaces that ignore the host design system.

UI Compose replaces blank-canvas generation with a decision pipeline:

**Host Read → Design Read → Skeleton → Pattern Set → Recipe → Adapter → Verify**

The result should remain **native to the host project**.

## Composition Intelligence

UI Compose separates four kinds of reusable knowledge plus page-level composition:

1. **Source Registry** — where a useful decision was observed and what its provenance/license boundary is.
2. **Pattern Registry** — reusable UI decisions independent of any one source library or brand.
3. **Pattern Recipes** — host-neutral implementation behavior for mature canonical patterns.
4. **Adapters** — translation from a selected recipe into the host project's implementation vocabulary.

**Skeleton Registry** organizes Patterns into page-level product workflows.

A source can provide evidence for a Pattern without becoming a runtime dependency.

```text
Vue 3 + Element Plus + B2B orders + high density + low motion
  ↓
master-detail-workspace
  ↓
dense-filter-toolbar
master-detail-preview
view-options-control
sticky-contextual-actions
  ↓
host-neutral recipes
  ↓
Vue + Element Plus adapter
  ↓
0 new UI primitive systems
```

Core references:

- [`references/host-read.md`](references/host-read.md)
- [`references/composition-selection.md`](references/composition-selection.md)
- [`references/physics.md`](references/physics.md)
- [`references/sources/registry.yaml`](references/sources/registry.yaml)
- [`references/patterns/registry.yaml`](references/patterns/registry.yaml)
- [`references/patterns/recipes.md`](references/patterns/recipes.md)
- [`references/skeletons/registry.yaml`](references/skeletons/registry.yaml)
- [`references/sources/provenance.md`](references/sources/provenance.md)
- [`DELIVERY.md`](DELIVERY.md)

## External sources are evidence, not defaults

Popular UI libraries, products and campaign sites are research sources. UI Compose may extract durable traits such as app-shell/master-detail relationships, dense data toolbars, keyboard-first command surfaces, view/display options, AI streaming/tool/approval states, editorial product-world switching, restrained ambient motion, and single-scene WebGL composition.

It should not blindly install, vendor, or clone source libraries, products, brands, copy, assets, or proprietary identity.

Research follows:

**Observe → Record Evidence → Extract Trait → Map to Pattern → Write Recipe → Check Provenance → Adapt to Host → Verify**

A research pass should improve at least one durable asset: Source metadata, Pattern evidence/recipe, Skeleton evidence, provenance/risk guidance, or an Eval hypothesis.

## Core workflow

### 1. Host Read

Detect framework/runtime, styling, primitive/component system, tokens, motion stack, representative product patterns, and accessibility/responsive/runtime constraints.

Never assume React, Tailwind, Radix, shadcn, or a particular file layout.

### 2. Design Read

Interpret surface, audience, product register and visual direction. Optional variance/motion/density dials act as filters, not universal presets.

### 3. Skeleton

Choose page architecture before decorative styling.

### 4. Pattern Set

Select the **smallest coherent compatible set** that covers the product jobs and required states. Complex product surfaces often use 3–7 patterns; narrow or specialized surfaces may legitimately use only 1–2. Never pad a composition to satisfy a quota.

### 5. Recipe

For mature canonical patterns, use the host-neutral behavior contracts in [`references/patterns/recipes.md`](references/patterns/recipes.md). Shared fallback motion/type/radius guidance lives in [`references/physics.md`](references/physics.md). Host tokens and established conventions always win over fallback values.

### 6. Adapter

Current baseline adapters:

- React + Tailwind
- Vue + Element Plus
- Vue + UnoCSS
- Generic CSS / existing design system

### 7. Verify

Inspect desktop/mobile, keyboard/focus, loading/empty/error states, reduced motion, overflow, dependency changes, and runtime behavior.

## AI-native UI

AI products are a first-class category. UI Compose covers streaming response, activity/progress summary, tool execution lifecycle, approval gates, source/context inspection, persistent composer, retry/error/cancel, and task lifecycle.

`references/ai-primitives.md` includes host-neutral recipes for active streaming indicators, compact tool rows, approval behavior, and composer behavior. Completed generation must remove active streaming indicators such as the caret; a finished answer must not keep looking active.

UI must expose only provider-supported activity, summarized reasoning, or execution traces. It must not imply access to hidden chain-of-thought.

## Project structure

```text
ui-compose/
  SKILL.md
  README.md
  DELIVERY.md
  agents/
    openai.yaml
  references/
    host-read.md
    composition-selection.md
    physics.md
    reverse-engineering.md
    layout-steal.md
    ai-primitives.md
    motion-blocks.md
    editorial-campaign.md
    threeui.md
    taste-dials.md
    adapters/
    sources/
      registry.yaml
      provenance.md
    patterns/
      registry.yaml
      recipes.md
    skeletons/
      registry.yaml
  schemas/
    source-registry.schema.json
    pattern-registry.schema.json
    skeleton-registry.schema.json
    eval-fixture.schema.json
    eval-result.schema.json
  scripts/
    validate_skill.py
    validate_registries.py
    validate_evals.py
  evals/
    rubric.md
    cases/
      README.md
      01-vue-element-plus-orders.md
      02-agent-chat.md
      03-settings-workspace.md
      04-react-tailwind-data-workspace.md
      05-vue-unocss-crm.md
      06-saas-marketing-landing.md
      07-editorial-product-explorer.md
      08-webgl-hero.md
      09-custom-design-system.md
    harness/
      README.md
      fixtures/
        vue-element-plus-orders.yaml
        agent-chat.yaml
        react-tailwind-data-workspace.yaml
        custom-design-system.yaml
    results/
      README.md
  .github/workflows/
    validate.yml
```

## Validation

```bash
python -m pip install pyyaml jsonschema
python scripts/validate_skill.py . --expected-install-name ui-compose
python scripts/validate_registries.py
python scripts/validate_evals.py
```

CI currently checks Agent Skills metadata, OpenAI UI metadata, progressive-disclosure budget, registry schema/cross-references, source verification metadata/freshness, Fixture contracts, Eval Result references, rubric arithmetic, and desktop/mobile artifact requirements for passed rendered runs.

The Skill frontmatter intentionally uses a strict portable subset. Framework compatibility guidance lives in the Markdown body instead of a top-level `compatibility` field so stricter packagers do not reject the skill.

## Install

Use the Agent Skills convention supported by your coding agent. For portable repo-level usage, prefer a folder named after the skill:

```text
.agents/skills/ui-compose/
  SKILL.md
  references/
  scripts/
  agents/
```

Some clients also support compatibility locations such as `.cursor/skills/`, `.claude/skills/`, or `$CODEX_HOME/skills`. Keep the install folder aligned with `name: ui-compose`.

## Evaluation

The rubric is in [`evals/rubric.md`](evals/rubric.md), repeatable task contracts are in [`evals/cases/`](evals/cases/), the execution protocol is in [`evals/harness/README.md`](evals/harness/README.md), observed run records are documented in [`evals/results/README.md`](evals/results/README.md), and stable-release criteria are in [`DELIVERY.md`](DELIVERY.md).

The current nine-case matrix covers Vue 3 + Element Plus B2B orders, AI agent chat + tools + approval, settings/form workflow, React + Tailwind/local-primitives data workspace, Vue + UnoCSS CRM, SaaS marketing landing, editorial product explorer, restrained WebGL hero, and an unfamiliar custom/internal design system.

The first empirical batch prioritizes cases 01, 02, 04 and 09. These have machine-validated Fixture Contracts that pin the host framework/primitive system, existing dependencies, forbidden default dependencies, required product states, accessibility contract, mobile contract, representative files, and build commands.

Fixture Contracts are not benchmark results. They define the clean host baseline from which every comparison mode should start. No benchmark score is considered real until an observed result record exists.

The largest remaining delivery gap is **real executable fixtures and rendered benchmark evidence**: buildable fixture apps, generated comparison runs, desktop/mobile screenshots, keyboard/reduced-motion notes, dependency diffs, and comparative scores. Eval 01 and 02 remain the first release-critical runs.

## Delivery readiness

A stable release is not based on documentation volume. [`DELIVERY.md`](DELIVERY.md) defines a 100-point project-readiness gate across skill architecture, registry integrity, provenance, host/product diversity, rendered eval evidence, CI, and maintenance.

A build/runtime failure, primary accessibility failure, provenance violation, or unnecessary replacement of the host primitive system blocks delivery-ready status regardless of numeric score.

## Non-goals

UI Compose is not an npm component library, a replacement design system, a clone of popular product brands, a bundle of fashionable effects, permission to mix multiple primitive kits, or a reason to replace accessible host controls with custom markup.

## Source policy

External projects remain their authors' work. UI Compose records original methodology, abstractions, and independently reimplementable observations. Upstream source code/assets/trademarks retain their original licenses and rights.

## License

MIT for original material in this repository. Third-party material is not relicensed by this project.

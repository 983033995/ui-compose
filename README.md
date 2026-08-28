# UI Compose

**UI Compose is a stack-aware UI composition engine for coding agents.**

It does not exist to install or copy popular UI libraries. It studies useful decisions from proven interfaces — layout systems, density, interaction models, motion physics, AI-native states, and product-specific composition patterns — then re-expresses those traits using the host project's own framework, components, tokens, and conventions.

> Taste decides the direction. UI Compose decides how to build it.

## Why this exists

Coding agents can generate valid frontend code and still produce generic UI: random spacing, disconnected cards, fashionable effects with no product logic, unnecessary dependencies, weak product states, or interfaces that ignore the host design system.

UI Compose replaces blank-canvas generation with a decision pipeline:

**Host Read → Design Read → Skeleton → Pattern Set → Adapter → Verify**

The result should remain **native to the host project**.

## Composition Intelligence

UI Compose separates three kinds of knowledge:

1. **Source Registry** — where a useful decision was observed and what its provenance/license boundary is.
2. **Pattern Registry** — reusable UI decisions independent of any one source library or brand.
3. **Skeleton Registry** — page-level region relationships that organize patterns into a product workflow.

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
Vue + Element Plus adapter
  ↓
0 new UI primitive systems
```

Core references:

- [`references/host-read.md`](references/host-read.md)
- [`references/composition-selection.md`](references/composition-selection.md)
- [`references/sources/registry.yaml`](references/sources/registry.yaml)
- [`references/patterns/registry.yaml`](references/patterns/registry.yaml)
- [`references/skeletons/registry.yaml`](references/skeletons/registry.yaml)
- [`references/sources/provenance.md`](references/sources/provenance.md)
- [`DELIVERY.md`](DELIVERY.md)

## External sources are evidence, not defaults

Popular UI libraries, products and campaign sites are research sources. UI Compose may extract durable traits such as:

- app-shell and master/detail relationships
- dense data toolbars
- keyboard-first command surfaces
- view/display options
- AI streaming/tool/approval states
- editorial product-world switching
- restrained ambient motion
- single-scene WebGL composition

It should not blindly install, vendor, or clone source libraries, products, brands, copy, assets, or proprietary identity.

Research follows:

**Observe → Record Evidence → Extract Trait → Map to Pattern → Check Provenance → Adapt to Host → Verify**

A research pass should improve at least one durable asset: Source metadata, Pattern evidence, Skeleton evidence, provenance/risk guidance, or an Eval hypothesis.

The Source Registry records canonical URLs and verified licenses when authoritative evidence is available. Unverified entries remain explicitly marked rather than guessed.

## Core workflow

### 1. Host Read

Detect framework/runtime, styling, primitive/component system, tokens, motion stack, representative product patterns, and accessibility/responsive/runtime constraints.

Never assume React, Tailwind, Radix, shadcn, or a particular file layout.

### 2. Design Read

Interpret surface, audience, product register and visual direction. Optional variance/motion/density dials act as filters, not universal presets.

### 3. Skeleton

Choose page architecture before decorative styling.

### 4. Pattern Set

Select the smallest coherent set, usually 3–7 patterns, that fits the product job and host constraints.

### 5. Adapter

Current baseline adapters:

- React + Tailwind
- Vue + Element Plus
- Vue + UnoCSS
- Generic CSS / existing design system

### 6. Verify

Inspect desktop/mobile, keyboard/focus, loading/empty/error states, reduced motion, overflow, dependency changes, and runtime behavior.

## AI-native UI

AI products are a first-class category. UI Compose covers:

- streaming response
- activity/progress summary
- tool execution lifecycle
- approval gates
- source/context inspection
- persistent composer
- retry/error/cancel
- task lifecycle

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
    skeletons/
      registry.yaml
  schemas/
    source-registry.schema.json
    pattern-registry.schema.json
    skeleton-registry.schema.json
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

CI currently checks:

- Agent Skills frontmatter/name/description contract
- current OpenAI `agents/openai.yaml` interface metadata shape
- progressive-disclosure line budget
- registry JSON Schema conformance
- duplicate IDs
- Pattern → Source evidence references
- Skeleton → Pattern references
- adapter IDs
- density/motion ranges
- source verification metadata consistency
- eval-result schema conformance
- Eval → Case / Pattern / Skeleton references
- rubric arithmetic
- desktop/mobile artifact references for passed rendered runs

These checks run on pushes and pull requests.

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

The current nine-case matrix covers:

- Vue 3 + Element Plus B2B orders
- AI agent chat + tools + approval
- settings/form workflow
- React + Tailwind/local-primitives data workspace
- Vue + UnoCSS CRM
- SaaS marketing landing
- editorial product explorer
- restrained WebGL hero
- unfamiliar custom/internal design system

The first empirical batch should prioritize cases 01, 02, 04 and 09 because together they test dense B2B composition, AI-native state modeling, React/Tailwind without shadcn-by-default, and unfamiliar internal design-system portability.

No benchmark score is considered real until an observed result record exists. The largest remaining delivery gap is **real rendered benchmark evidence**: build results, desktop/mobile screenshots, keyboard/reduced-motion notes, dependency diffs, and comparative scores.

## Delivery readiness

A stable release is not based on documentation volume. [`DELIVERY.md`](DELIVERY.md) defines a 100-point project-readiness gate across skill architecture, registry integrity, provenance, host/product diversity, rendered eval evidence, CI, and maintenance.

A build/runtime failure, primary accessibility failure, provenance violation, or unnecessary replacement of the host primitive system blocks delivery-ready status regardless of numeric score.

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

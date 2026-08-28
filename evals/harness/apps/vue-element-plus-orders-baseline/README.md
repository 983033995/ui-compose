# Eval 01 host baseline — Vue + Element Plus orders

This is the executable **clean host baseline** for `01-vue-element-plus-orders`.
It is intentionally not the UI Compose solution.

The fixture provides a small but non-empty existing product environment:

- Vue 3 + Vite + TypeScript
- Element Plus as the established primitive layer
- semantic host CSS variables
- local `AppTable` and `AppDialog` wrappers
- an existing order screen with basic search, table, dialog, loading, empty and error behavior
- no Tailwind, Radix, shadcn, Ant Design, or second table/dialog system

The benchmark task still has to design the dense status/date filtering, result-count hierarchy, master/detail preservation, multi-select bulk actions, deliberate mobile strategy, and complete state treatment described by the case contract.

## Local commands

```bash
corepack enable
corepack prepare pnpm@9.15.4 --activate
pnpm install --no-frozen-lockfile
pnpm test
pnpm build
pnpm dev
```

The first CI run intentionally generates `pnpm-lock.yaml`. Once the generated lockfile is committed, the fixture install command should switch to `pnpm install --frozen-lockfile` for benchmark reproducibility.

## Benchmark isolation

Every comparison mode must start from the same clean fixture commit/tree. Generated code for one mode must never be reused by another mode.

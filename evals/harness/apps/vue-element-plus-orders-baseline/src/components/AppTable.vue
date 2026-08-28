<script setup lang="ts">
import { nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { ElTable } from 'element-plus'
import type { OrderRecord } from '../types/order'

const props = withDefaults(
  defineProps<{
    rows: OrderRecord[]
    loading?: boolean
  }>(),
  {
    loading: false,
  },
)

const emit = defineEmits<{
  inspect: [row: OrderRecord]
  selectionChange: [rows: OrderRecord[]]
}>()

const root = ref<HTMLElement | null>(null)
let observer: MutationObserver | null = null

function syncRowAccessibility() {
  const rows = root.value?.querySelectorAll<HTMLElement>('tbody tr.el-table__row') ?? []
  rows.forEach((row, index) => {
    row.tabIndex = 0
    const order = props.rows[index]
    if (order) row.setAttribute('aria-label', `Open ${order.id} details`)
  })
}

function inspectFromKeyboard(event: KeyboardEvent) {
  if (event.key !== 'Enter' && event.key !== ' ') return
  const target = event.target as HTMLElement | null
  const row = target?.closest<HTMLElement>('tr.el-table__row')
  if (!row || !root.value?.contains(row)) return
  if (target?.closest('button, a, input, select, textarea, [role="checkbox"]')) return

  const rows = Array.from(root.value.querySelectorAll<HTMLElement>('tbody tr.el-table__row'))
  const index = rows.indexOf(row)
  const order = props.rows[index]
  if (!order) return

  event.preventDefault()
  emit('inspect', order)
}

async function resyncRows() {
  await nextTick()
  syncRowAccessibility()
}

onMounted(async () => {
  await resyncRows()
  if (!root.value) return
  observer = new MutationObserver(syncRowAccessibility)
  observer.observe(root.value, { childList: true, subtree: true })
})

onBeforeUnmount(() => observer?.disconnect())
watch(() => props.rows, resyncRows)
</script>

<template>
  <div ref="root" class="app-table-shell" @keydown="inspectFromKeyboard">
    <ElTable
      :data="rows"
      :loading="loading"
      row-key="id"
      stripe
      class="app-table"
      @row-click="emit('inspect', $event)"
      @selection-change="emit('selectionChange', $event)"
    >
      <slot />
    </ElTable>
  </div>
</template>

<style scoped>
.app-table-shell {
  width: 100%;
}

.app-table {
  width: 100%;
  border-radius: var(--host-radius-md);
  box-shadow: 0 0 0 1px var(--host-border);
  overflow: hidden;
}
</style>

<script setup lang="ts">
import { ElTable } from 'element-plus'
import type { OrderRecord } from '../types/order'

withDefaults(
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
</script>

<template>
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
</template>

<style scoped>
.app-table {
  width: 100%;
  border-radius: var(--host-radius-md);
  box-shadow: 0 0 0 1px var(--host-border);
  overflow: hidden;
}
</style>

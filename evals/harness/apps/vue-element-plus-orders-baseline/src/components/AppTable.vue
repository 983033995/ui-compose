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

defineEmits<{
  inspect: [row: OrderRecord]
}>()
</script>

<template>
  <ElTable
    v-loading="loading"
    :data="rows"
    row-key="id"
    stripe
    class="app-table"
    @row-click="$emit('inspect', $event)"
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

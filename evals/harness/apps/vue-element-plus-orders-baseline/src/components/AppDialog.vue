<script setup lang="ts">
import { ElDialog } from 'element-plus'

const props = withDefaults(
  defineProps<{
    modelValue: boolean
    title: string
    width?: string
  }>(),
  {
    width: '520px',
  },
)

const emit = defineEmits<{
  'update:modelValue': [value: boolean]
}>()
</script>

<template>
  <ElDialog
    :model-value="props.modelValue"
    :title="props.title"
    :width="props.width"
    @update:model-value="emit('update:modelValue', $event)"
  >
    <slot />
    <template #footer>
      <slot name="footer" />
    </template>
  </ElDialog>
</template>

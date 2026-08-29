<script setup lang="ts">
import { computed, ref } from 'vue'
import { ElAlert, ElButton, ElEmpty, ElInput, ElTableColumn, ElTag } from 'element-plus'
import AppDialog from '../components/AppDialog.vue'
import AppTable from '../components/AppTable.vue'
import type { OrderRecord } from '../types/order'

const orders: OrderRecord[] = [
  { id: 'SO-10481', customer: 'Northstar Retail', amount: 12840, status: 'Processing', createdAt: '2026-08-26', owner: 'Mia Chen' },
  { id: 'SO-10480', customer: 'Harbor Systems', amount: 6420, status: 'Pending', createdAt: '2026-08-26', owner: 'Leo Park' },
  { id: 'SO-10479', customer: 'Atlas Components', amount: 21990, status: 'Completed', createdAt: '2026-08-25', owner: 'Mia Chen' },
  { id: 'SO-10478', customer: 'Birch & Stone', amount: 3170, status: 'Cancelled', createdAt: '2026-08-25', owner: 'Ava Singh' },
  { id: 'SO-10477', customer: 'Kiteworks Labs', amount: 8860, status: 'Processing', createdAt: '2026-08-24', owner: 'Leo Park' },
]

const query = ref('')
const loading = ref(false)
const error = ref(false)
const selectedOrder = ref<OrderRecord | null>(null)

const filteredOrders = computed(() => {
  const needle = query.value.trim().toLowerCase()
  if (!needle) return orders
  return orders.filter((order) =>
    [order.id, order.customer, order.owner, order.status]
      .join(' ')
      .toLowerCase()
      .includes(needle),
  )
})

function statusType(status: OrderRecord['status']) {
  if (status === 'Completed') return 'success'
  if (status === 'Cancelled') return 'danger'
  if (status === 'Processing') return 'primary'
  return 'warning'
}
</script>

<template>
  <section class="baseline-page" aria-labelledby="orders-title">
    <header class="page-header">
      <div>
        <p class="eyebrow">Operations</p>
        <h1 id="orders-title">Orders</h1>
        <p class="subtitle">Existing host screen used as the benchmark starting point.</p>
      </div>
      <ElButton>Export</ElButton>
    </header>

    <div class="host-toolbar" aria-label="Existing order controls">
      <ElInput
        v-model="query"
        clearable
        aria-label="Search existing orders"
        placeholder="Search order, customer, owner"
        class="search-input"
      />
      <div class="toolbar-actions">
        <ElButton @click="loading = !loading">Toggle loading</ElButton>
        <ElButton @click="error = !error">Toggle error</ElButton>
      </div>
    </div>

    <ElAlert
      v-if="error"
      type="error"
      :closable="false"
      title="Orders could not be loaded"
      description="This fixture exposes a real host error state for benchmark runs."
    />

    <ElEmpty
      v-else-if="!loading && filteredOrders.length === 0"
      description="No matching orders"
    />

    <AppTable
      v-else
      :rows="filteredOrders"
      :loading="loading"
      @inspect="selectedOrder = $event"
    >
      <ElTableColumn prop="id" label="Order" width="130" />
      <ElTableColumn prop="customer" label="Customer" min-width="180" />
      <ElTableColumn label="Status" width="130">
        <template #default="scope">
          <ElTag :type="statusType(scope.row.status)" effect="plain">
            {{ scope.row.status }}
          </ElTag>
        </template>
      </ElTableColumn>
      <ElTableColumn prop="owner" label="Owner" width="140" />
      <ElTableColumn prop="createdAt" label="Created" width="120" />
      <ElTableColumn label="Amount" width="130" align="right">
        <template #default="scope">
          ${{ scope.row.amount.toLocaleString() }}
        </template>
      </ElTableColumn>
    </AppTable>

    <AppDialog
      :model-value="Boolean(selectedOrder)"
      title="Order details"
      @update:model-value="(open) => { if (!open) selectedOrder = null }"
    >
      <dl v-if="selectedOrder" class="detail-list">
        <div><dt>Order</dt><dd>{{ selectedOrder.id }}</dd></div>
        <div><dt>Customer</dt><dd>{{ selectedOrder.customer }}</dd></div>
        <div><dt>Status</dt><dd>{{ selectedOrder.status }}</dd></div>
        <div><dt>Owner</dt><dd>{{ selectedOrder.owner }}</dd></div>
      </dl>
      <template #footer>
        <ElButton @click="selectedOrder = null">Close</ElButton>
      </template>
    </AppDialog>
  </section>
</template>

<style scoped>
.baseline-page {
  width: min(1180px, calc(100% - 48px));
  margin: 0 auto;
  padding: var(--host-space-8) 0;
}

.page-header,
.host-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--host-space-4);
}

.page-header {
  margin-bottom: var(--host-space-6);
}

.eyebrow,
.subtitle {
  margin: 0;
  color: var(--host-muted);
  font-size: var(--host-text-sm);
}

h1 {
  margin: var(--host-space-1) 0 var(--host-space-2);
  font-size: var(--host-text-xl);
  line-height: 1.2;
}

.host-toolbar {
  margin-bottom: var(--host-space-4);
}

.search-input {
  max-width: 320px;
}

.toolbar-actions {
  display: flex;
  gap: var(--host-space-2);
}

.detail-list {
  display: grid;
  gap: var(--host-space-3);
  margin: 0;
}

.detail-list > div {
  display: grid;
  grid-template-columns: 110px 1fr;
  gap: var(--host-space-3);
}

.detail-list dt {
  color: var(--host-muted);
}

.detail-list dd {
  margin: 0;
}

@media (max-width: 640px) {
  .baseline-page {
    width: min(100% - 24px, 1180px);
    padding-top: var(--host-space-5);
  }

  .page-header,
  .host-toolbar {
    align-items: stretch;
    flex-direction: column;
  }

  .search-input {
    max-width: none;
  }

  .toolbar-actions {
    flex-wrap: wrap;
  }
}
</style>

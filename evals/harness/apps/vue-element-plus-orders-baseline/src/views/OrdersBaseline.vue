<script setup lang="ts">
import { computed, ref } from 'vue'
import {
  ElAlert,
  ElButton,
  ElDatePicker,
  ElEmpty,
  ElInput,
  ElOption,
  ElSelect,
  ElTableColumn,
  ElTag,
} from 'element-plus'
import AppDialog from '../components/AppDialog.vue'
import AppTable from '../components/AppTable.vue'
import type { OrderRecord, OrderStatus } from '../types/order'

const orders: OrderRecord[] = [
  { id: 'SO-10481', customer: 'Northstar Retail', amount: 12840, status: 'Processing', createdAt: '2026-08-26', owner: 'Mia Chen' },
  { id: 'SO-10480', customer: 'Harbor Systems', amount: 6420, status: 'Pending', createdAt: '2026-08-26', owner: 'Leo Park' },
  { id: 'SO-10479', customer: 'Atlas Components', amount: 21990, status: 'Completed', createdAt: '2026-08-25', owner: 'Mia Chen' },
  { id: 'SO-10478', customer: 'Birch & Stone', amount: 3170, status: 'Cancelled', createdAt: '2026-08-25', owner: 'Ava Singh' },
  { id: 'SO-10477', customer: 'Kiteworks Labs', amount: 8860, status: 'Processing', createdAt: '2026-08-24', owner: 'Leo Park' },
]

const query = ref('')
const status = ref<OrderStatus | ''>('')
const dateRange = ref<string[]>([])
const loading = ref(false)
const error = ref(false)
const selectedOrder = ref<OrderRecord | null>(null)
const selectedRows = ref<OrderRecord[]>([])
const bulkMessage = ref('')

const filteredOrders = computed(() => {
  const needle = query.value.trim().toLowerCase()
  const [start, end] = dateRange.value

  return orders.filter((order) => {
    const matchesQuery = !needle || [order.id, order.customer, order.owner, order.status]
      .join(' ')
      .toLowerCase()
      .includes(needle)
    const matchesStatus = !status.value || order.status === status.value
    const matchesDate = !start || !end || (order.createdAt >= start && order.createdAt <= end)
    return matchesQuery && matchesStatus && matchesDate
  })
})

function statusType(value: OrderRecord['status']) {
  if (value === 'Completed') return 'success'
  if (value === 'Cancelled') return 'danger'
  if (value === 'Processing') return 'primary'
  return 'warning'
}

function clearFilters() {
  query.value = ''
  status.value = ''
  dateRange.value = []
}

function handleSelectionChange(rows: OrderRecord[]) {
  selectedRows.value = rows
  bulkMessage.value = ''
}

function runBulkAction(action: string) {
  bulkMessage.value = `${action} applied to ${selectedRows.value.length} selected order${selectedRows.value.length === 1 ? '' : 's'}.`
}
</script>

<template>
  <section class="orders-page" aria-labelledby="orders-title">
    <header class="page-header">
      <div>
        <p class="eyebrow">Operations</p>
        <h1 id="orders-title">Orders</h1>
        <p class="subtitle">Review, filter and manage customer orders.</p>
      </div>
      <ElButton>Export</ElButton>
    </header>

    <div class="filter-card" aria-label="Order filters">
      <ElInput
        v-model="query"
        clearable
        aria-label="Search orders"
        placeholder="Search order, customer, owner"
        class="search-input"
      />
      <ElSelect v-model="status" clearable aria-label="Filter by status" placeholder="Status" class="status-select">
        <ElOption label="Pending" value="Pending" />
        <ElOption label="Processing" value="Processing" />
        <ElOption label="Completed" value="Completed" />
        <ElOption label="Cancelled" value="Cancelled" />
      </ElSelect>
      <ElDatePicker
        v-model="dateRange"
        type="daterange"
        value-format="YYYY-MM-DD"
        start-placeholder="Start date"
        end-placeholder="End date"
        aria-label="Filter by order date"
        class="date-filter"
      />
      <ElButton @click="clearFilters">Reset</ElButton>
    </div>

    <div class="result-row" aria-live="polite">
      <strong>{{ filteredOrders.length }} orders</strong>
      <span v-if="selectedRows.length">{{ selectedRows.length }} selected</span>
    </div>

    <ElAlert
      v-if="bulkMessage"
      class="bulk-message"
      type="success"
      :closable="true"
      :title="bulkMessage"
      @close="bulkMessage = ''"
    />

    <div v-if="selectedRows.length" class="bulk-bar" aria-label="Bulk actions">
      <span>{{ selectedRows.length }} selected</span>
      <div>
        <ElButton size="small" @click="runBulkAction('Export')">Export selected</ElButton>
        <ElButton size="small" type="primary" @click="runBulkAction('Status update')">Update status</ElButton>
      </div>
    </div>

    <ElAlert
      v-if="error"
      type="error"
      :closable="false"
      title="Orders could not be loaded"
      description="Try again or review the current filters."
    />

    <ElEmpty
      v-else-if="!loading && filteredOrders.length === 0"
      description="No matching orders"
    >
      <ElButton @click="clearFilters">Clear filters</ElButton>
    </ElEmpty>

    <div v-else class="table-scroll">
      <AppTable
        :rows="filteredOrders"
        :loading="loading"
        @inspect="selectedOrder = $event"
        @selection-change="handleSelectionChange"
      >
        <ElTableColumn type="selection" width="48" />
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
    </div>

    <div class="debug-state" aria-label="Fixture state controls">
      <ElButton text @click="loading = !loading">Toggle loading</ElButton>
      <ElButton text @click="error = !error">Toggle error</ElButton>
    </div>

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
        <div><dt>Created</dt><dd>{{ selectedOrder.createdAt }}</dd></div>
        <div><dt>Amount</dt><dd>${{ selectedOrder.amount.toLocaleString() }}</dd></div>
      </dl>
      <template #footer>
        <ElButton @click="selectedOrder = null">Close</ElButton>
        <ElButton type="primary">Edit order</ElButton>
      </template>
    </AppDialog>
  </section>
</template>

<style scoped>
.orders-page {
  width: min(1180px, calc(100% - 48px));
  margin: 0 auto;
  padding: var(--host-space-8) 0;
}

.page-header,
.result-row,
.bulk-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--host-space-4);
}

.page-header {
  margin-bottom: var(--host-space-6);
}

.eyebrow,
.subtitle,
.result-row span {
  margin: 0;
  color: var(--host-muted);
  font-size: var(--host-text-sm);
}

h1 {
  margin: var(--host-space-1) 0 var(--host-space-2);
  font-size: var(--host-text-xl);
  line-height: 1.2;
}

.filter-card {
  display: flex;
  align-items: center;
  gap: var(--host-space-3);
  padding: var(--host-space-4);
  margin-bottom: var(--host-space-4);
  border-radius: var(--host-radius-lg);
  background: var(--host-surface);
  box-shadow: 0 0 0 1px var(--host-border);
}

.search-input { width: 280px; }
.status-select { width: 150px; }
.date-filter { width: 300px; }

.result-row {
  margin-bottom: var(--host-space-3);
  font-size: var(--host-text-sm);
}

.bulk-bar {
  position: sticky;
  top: var(--host-space-3);
  z-index: 2;
  margin-bottom: var(--host-space-3);
  padding: var(--host-space-3) var(--host-space-4);
  border-radius: var(--host-radius-md);
  background: var(--host-surface);
  box-shadow: 0 4px 18px rgb(23 32 51 / 10%), 0 0 0 1px var(--host-border);
}

.bulk-bar > div {
  display: flex;
  gap: var(--host-space-2);
}

.bulk-message {
  margin-bottom: var(--host-space-3);
}

.table-scroll {
  overflow-x: auto;
}

.debug-state {
  display: flex;
  justify-content: flex-end;
  gap: var(--host-space-2);
  margin-top: var(--host-space-3);
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

.detail-list dt { color: var(--host-muted); }
.detail-list dd { margin: 0; }

@media (max-width: 760px) {
  .orders-page {
    width: min(100% - 24px, 1180px);
    padding-top: var(--host-space-5);
  }

  .page-header {
    align-items: stretch;
    flex-direction: column;
  }

  .filter-card {
    align-items: stretch;
    flex-direction: column;
  }

  .search-input,
  .status-select,
  .date-filter {
    width: 100%;
  }

  .bulk-bar {
    align-items: stretch;
    flex-direction: column;
  }

  .bulk-bar > div {
    flex-wrap: wrap;
  }
}
</style>

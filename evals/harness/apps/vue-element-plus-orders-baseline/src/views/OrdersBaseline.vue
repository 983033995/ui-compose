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

const filtersActive = computed(() => Boolean(query.value || status.value || dateRange.value.length))

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

function inspectOrder(order: OrderRecord) {
  selectedOrder.value = order
}

function closeMobileDetail() {
  selectedOrder.value = null
}
</script>

<template>
  <section class="orders-page" :class="{ 'has-mobile-detail': selectedOrder }" aria-labelledby="orders-title">
    <header class="page-header">
      <div class="title-block">
        <p class="eyebrow">Operations</p>
        <div class="title-row">
          <h1 id="orders-title">Orders</h1>
          <span class="result-count" aria-live="polite">{{ filteredOrders.length }}</span>
        </div>
        <p class="subtitle">Triage orders without losing list context.</p>
      </div>
      <ElButton>Export</ElButton>
    </header>

    <div class="dense-toolbar" aria-label="Order filters">
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
        start-placeholder="Start"
        end-placeholder="End"
        aria-label="Filter by order date"
        class="date-filter"
      />
      <ElButton v-if="filtersActive" text @click="clearFilters">Clear</ElButton>
      <span class="toolbar-spacer" />
      <span class="toolbar-summary">{{ filteredOrders.length }} of {{ orders.length }}</span>
    </div>

    <ElAlert
      v-if="bulkMessage"
      class="workspace-alert"
      type="success"
      :closable="true"
      :title="bulkMessage"
      @close="bulkMessage = ''"
    />

    <ElAlert
      v-if="error"
      class="workspace-alert"
      type="error"
      :closable="false"
      title="Orders could not be loaded"
      description="Retry or adjust the current filters."
    />

    <div v-else class="workspace">
      <section class="collection-pane" aria-label="Order list">
        <div v-if="selectedRows.length" class="selection-bar" aria-label="Bulk actions">
          <strong>{{ selectedRows.length }} selected</strong>
          <div class="selection-actions">
            <ElButton size="small" @click="runBulkAction('Export')">Export</ElButton>
            <ElButton size="small" type="primary" @click="runBulkAction('Status update')">Update status</ElButton>
          </div>
        </div>

        <ElEmpty
          v-if="!loading && filteredOrders.length === 0"
          description="No matching orders"
          class="empty-state"
        >
          <ElButton @click="clearFilters">Clear filters</ElButton>
        </ElEmpty>

        <div v-else class="table-scroll">
          <AppTable
            :rows="filteredOrders"
            :loading="loading"
            @inspect="inspectOrder"
            @selection-change="handleSelectionChange"
          >
            <ElTableColumn type="selection" width="44" />
            <ElTableColumn prop="id" label="Order" width="116" />
            <ElTableColumn prop="customer" label="Customer" min-width="168" />
            <ElTableColumn label="Status" width="118">
              <template #default="scope">
                <ElTag :type="statusType(scope.row.status)" effect="plain" size="small">
                  {{ scope.row.status }}
                </ElTag>
              </template>
            </ElTableColumn>
            <ElTableColumn prop="owner" label="Owner" width="120" />
            <ElTableColumn prop="createdAt" label="Created" width="112" />
            <ElTableColumn label="Amount" width="118" align="right">
              <template #default="scope">
                ${{ scope.row.amount.toLocaleString() }}
              </template>
            </ElTableColumn>
          </AppTable>
        </div>
      </section>

      <aside class="detail-pane" :class="{ empty: !selectedOrder }" aria-label="Order preview">
        <template v-if="selectedOrder">
          <div class="detail-header">
            <ElButton class="mobile-back" text @click="closeMobileDetail">← Back</ElButton>
            <div>
              <p class="detail-kicker">Order preview</p>
              <h2>{{ selectedOrder.id }}</h2>
            </div>
            <ElTag :type="statusType(selectedOrder.status)" effect="plain">
              {{ selectedOrder.status }}
            </ElTag>
          </div>

          <dl class="detail-list">
            <div><dt>Customer</dt><dd>{{ selectedOrder.customer }}</dd></div>
            <div><dt>Owner</dt><dd>{{ selectedOrder.owner }}</dd></div>
            <div><dt>Created</dt><dd>{{ selectedOrder.createdAt }}</dd></div>
            <div><dt>Amount</dt><dd>${{ selectedOrder.amount.toLocaleString() }}</dd></div>
          </dl>

          <section class="detail-section" aria-labelledby="fulfillment-title">
            <h3 id="fulfillment-title">Fulfillment</h3>
            <p>Payment verified. Inventory allocation is ready for the next operational step.</p>
          </section>

          <div class="detail-actions">
            <ElButton>View history</ElButton>
            <ElButton type="primary">Edit order</ElButton>
          </div>
        </template>

        <div v-else class="preview-empty">
          <strong>Select an order</strong>
          <span>Its details will stay visible beside the list.</span>
        </div>
      </aside>
    </div>

    <div class="debug-state" aria-label="Fixture state controls">
      <ElButton text @click="loading = !loading">Toggle loading</ElButton>
      <ElButton text @click="error = !error">Toggle error</ElButton>
    </div>
  </section>
</template>

<style scoped>
.orders-page {
  width: min(1320px, calc(100% - 40px));
  margin: 0 auto;
  padding: var(--host-space-6) 0;
}

.page-header,
.title-row,
.dense-toolbar,
.selection-bar,
.detail-header,
.detail-actions {
  display: flex;
  align-items: center;
}

.page-header {
  justify-content: space-between;
  gap: var(--host-space-4);
  margin-bottom: var(--host-space-5);
}

.title-row {
  gap: var(--host-space-2);
}

.eyebrow,
.subtitle,
.detail-kicker,
.toolbar-summary,
.preview-empty span,
.detail-section p {
  margin: 0;
  color: var(--host-muted);
  font-size: var(--host-text-sm);
}

h1,
h2,
h3 {
  margin: 0;
}

h1 {
  font-size: var(--host-text-xl);
  line-height: 1.2;
}

h2 {
  margin-top: var(--host-space-1);
  font-size: var(--host-text-lg);
}

h3 {
  margin-bottom: var(--host-space-2);
  font-size: var(--host-text-sm);
}

.result-count {
  min-width: 28px;
  padding: 2px 8px;
  border-radius: 999px;
  background: var(--host-surface-muted);
  color: var(--host-muted);
  font-size: var(--host-text-xs);
  font-variant-numeric: tabular-nums;
  text-align: center;
}

.dense-toolbar {
  gap: var(--host-space-2);
  min-height: 48px;
  padding: var(--host-space-2);
  margin-bottom: var(--host-space-3);
  border-radius: var(--host-radius-md);
  background: var(--host-surface);
  box-shadow: 0 0 0 1px var(--host-border);
}

.search-input { width: 260px; }
.status-select { width: 138px; }
.date-filter { width: 260px; }
.toolbar-spacer { flex: 1; }
.toolbar-summary { white-space: nowrap; font-variant-numeric: tabular-nums; }

.workspace-alert {
  margin-bottom: var(--host-space-3);
}

.workspace {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 340px;
  min-height: 560px;
  overflow: hidden;
  border-radius: var(--host-radius-lg);
  background: var(--host-surface);
  box-shadow: 0 0 0 1px var(--host-border);
}

.collection-pane {
  position: relative;
  min-width: 0;
  padding: var(--host-space-3);
  border-right: 1px solid var(--host-border);
}

.selection-bar {
  position: sticky;
  top: var(--host-space-3);
  z-index: 3;
  justify-content: space-between;
  gap: var(--host-space-3);
  min-height: 42px;
  padding: var(--host-space-2) var(--host-space-3);
  margin-bottom: var(--host-space-2);
  border-radius: var(--host-radius-sm);
  background: var(--host-surface);
  box-shadow: 0 6px 20px rgb(23 32 51 / 12%), 0 0 0 1px var(--host-border);
  font-size: var(--host-text-sm);
}

.selection-actions {
  display: flex;
  gap: var(--host-space-2);
}

.table-scroll {
  overflow-x: auto;
}

.empty-state {
  min-height: 420px;
}

.detail-pane {
  min-width: 0;
  padding: var(--host-space-5);
  background: var(--host-surface-muted);
}

.detail-pane.empty {
  display: grid;
  place-items: center;
}

.detail-header {
  justify-content: space-between;
  gap: var(--host-space-3);
  padding-bottom: var(--host-space-4);
  border-bottom: 1px solid var(--host-border);
}

.mobile-back {
  display: none;
}

.detail-list {
  display: grid;
  gap: var(--host-space-3);
  margin: var(--host-space-5) 0;
}

.detail-list > div {
  display: grid;
  grid-template-columns: 90px 1fr;
  gap: var(--host-space-3);
}

.detail-list dt {
  color: var(--host-muted);
  font-size: var(--host-text-sm);
}

.detail-list dd {
  margin: 0;
  font-size: var(--host-text-sm);
  font-weight: 600;
}

.detail-section {
  padding: var(--host-space-4) 0;
  border-top: 1px solid var(--host-border);
  border-bottom: 1px solid var(--host-border);
}

.detail-section p {
  line-height: 1.55;
}

.detail-actions {
  justify-content: flex-end;
  gap: var(--host-space-2);
  margin-top: var(--host-space-5);
}

.preview-empty {
  display: grid;
  gap: var(--host-space-2);
  max-width: 220px;
  text-align: center;
}

.debug-state {
  display: flex;
  justify-content: flex-end;
  gap: var(--host-space-2);
  margin-top: var(--host-space-2);
}

@media (max-width: 860px) {
  .orders-page {
    width: min(100% - 24px, 1320px);
    padding-top: var(--host-space-5);
  }

  .page-header {
    align-items: stretch;
    flex-direction: column;
  }

  .dense-toolbar {
    align-items: stretch;
    flex-wrap: wrap;
  }

  .search-input {
    flex: 1 1 100%;
    width: 100%;
  }

  .status-select,
  .date-filter {
    flex: 1 1 220px;
    width: auto;
  }

  .workspace {
    display: block;
    min-height: 0;
  }

  .collection-pane {
    border-right: 0;
  }

  .detail-pane {
    display: none;
    min-height: 520px;
    background: var(--host-surface);
  }

  .has-mobile-detail .collection-pane {
    display: none;
  }

  .has-mobile-detail .detail-pane {
    display: block;
  }

  .mobile-back {
    display: inline-flex;
    margin-left: calc(var(--host-space-2) * -1);
  }

  .detail-header {
    align-items: flex-start;
  }
}

@media (max-width: 520px) {
  .dense-toolbar {
    flex-direction: column;
  }

  .status-select,
  .date-filter {
    flex-basis: auto;
    width: 100%;
  }

  .toolbar-spacer {
    display: none;
  }

  .toolbar-summary {
    padding-left: var(--host-space-1);
  }

  .selection-bar {
    align-items: stretch;
    flex-direction: column;
  }

  .selection-actions {
    flex-wrap: wrap;
  }
}
</style>

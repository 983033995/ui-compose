export type OrderStatus = 'Pending' | 'Processing' | 'Completed' | 'Cancelled'

export interface OrderRecord {
  id: string
  customer: string
  amount: number
  status: OrderStatus
  createdAt: string
  owner: string
}

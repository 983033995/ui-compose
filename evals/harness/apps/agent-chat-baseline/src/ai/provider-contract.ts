export type ProviderEvent =
  | { type: 'text-delta'; text: string }
  | { type: 'tool-queued'; tool: string }
  | { type: 'tool-running'; tool: string; summary: string }
  | { type: 'tool-success'; tool: string; summary: string }
  | { type: 'tool-failure'; tool: string; error: string }
  | { type: 'approval-required'; title: string; consequence: string; scope: string }
  | { type: 'disconnected'; message: string }
  | { type: 'retryable-error'; message: string }
  | { type: 'reasoning-summary'; summary: string };

// `reasoning-summary` means a concise provider-exposed or product-owned progress summary only.
// It must never be used to fabricate or expose hidden chain-of-thought.
export const baselineEvents: ProviderEvent[] = [
  { type: 'text-delta', text: 'I found a recent billing mismatch.' },
  { type: 'tool-running', tool: 'account_history', summary: 'Reading 4 recent account events.' },
  { type: 'approval-required', title: 'Apply billing credit?', consequence: 'Adds a one-time $24 credit.', scope: 'Customer account AC-2048 only.' }
];

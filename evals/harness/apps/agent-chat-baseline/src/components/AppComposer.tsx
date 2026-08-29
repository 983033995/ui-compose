export interface AppComposerContract {
  value: string;
  busy: boolean;
  connected: boolean;
  onSend: (value: string) => void;
  onStop: () => void;
}

// Host-owned composer contract. The rendered composer remains reachable at mobile widths,
// exposes a keyboard-operable Stop action while busy, and preserves focus after send/retry.
export function AppComposer(contract: AppComposerContract) {
  return contract;
}

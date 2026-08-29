export type AppButtonVariant = 'primary' | 'secondary' | 'tertiary' | 'destructive';

export interface AppButtonContract {
  label: string;
  variant?: AppButtonVariant;
  disabled?: boolean;
  action: () => void;
}

// Host-owned primitive contract. Implementations must preserve native button semantics,
// visible focus, disabled state, and a readable text label or accessible name.
export function AppButton(contract: AppButtonContract) {
  return contract;
}

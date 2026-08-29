export const requiredAgentStates = [
  'streaming',
  'tool-queued',
  'tool-running',
  'tool-success',
  'tool-failure',
  'approval-required',
  'disconnected',
  'retryable-error'
] as const;

export const baselineRules = {
  toolStatusUsesText: true,
  approvalNamesConsequenceAndScope: true,
  stopRetryApprovalKeyboardOperable: true,
  persistentMobileComposer: true,
  hiddenChainOfThoughtAvailable: false,
  extraUiDependencies: [] as string[]
};

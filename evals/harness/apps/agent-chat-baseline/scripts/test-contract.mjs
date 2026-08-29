import { readFile } from 'node:fs/promises';

const read = (path) => readFile(path, 'utf8');
const [pkg, app, css, provider, button, composer, view] = await Promise.all([
  read('package.json'), read('src/app.js'), read('src/styles.css'), read('src/ai/provider-contract.ts'),
  read('src/components/AppButton.tsx'), read('src/components/AppComposer.tsx'), read('src/views/AgentBaseline.tsx')
]);

const requiredStates = ['streaming','tool-queued','tool-running','tool-success','tool-failure','approval-required','disconnected','retryable-error'];
for (const state of requiredStates) {
  if (!app.includes(state) && !view.includes(state)) throw new Error(`missing required state: ${state}`);
}

for (const forbidden of ['ai-elements','shadcn','radix-ui','framer-motion']) {
  if (pkg.includes(forbidden)) throw new Error(`forbidden default dependency: ${forbidden}`);
}

const checks = [
  [provider.includes('hidden chain-of-thought'), 'provider contract must state hidden-CoT boundary'],
  [provider.includes('consequence') && provider.includes('scope'), 'approval provider contract must include consequence and scope'],
  [app.includes('Approve $24 credit') && app.includes('AC-2048'), 'approval UI must name action and scope'],
  [app.includes('data-action="stop"') && app.includes('data-action="retry"'), 'stop and retry actions required'],
  [app.includes("event.key !== 'Enter'") && app.includes('event.shiftKey') && app.includes('composer.requestSubmit()'), 'composer must send on Enter and preserve Shift+Enter newline'],
  [button.includes('visible focus') && css.includes(':focus-visible'), 'focus-visible contract required'],
  [composer.includes('mobile widths') && css.includes('grid-template-rows: auto minmax(0, 1fr) auto') && css.includes('height: 100dvh'), 'persistent mobile composer layout contract required'],
  [css.includes('prefers-reduced-motion: reduce'), 'reduced motion rule required'],
  [css.includes('@media (max-width: 600px)'), 'mobile layout rule required']
];
for (const [ok, message] of checks) if (!ok) throw new Error(message);

console.log('agent-chat-baseline: contract checks passed');

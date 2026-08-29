const app = document.querySelector('#app');

const toolStates = [
  ['tool-queued', 'Queued', 'Search customer records', 'Waiting for an execution slot.'],
  ['tool-running', 'Running', 'Check account history', 'Reading 4 recent account events.'],
  ['tool-success', 'Completed', 'Load support policy', 'Policy context loaded successfully.'],
  ['tool-failure', 'Failed', 'Update billing note', 'Permission denied. No change was made.']
];

function button(label, variant = 'secondary', attrs = '') {
  return `<button class="app-button app-button--${variant}" ${attrs}>${label}</button>`;
}

function toolCard([state, label, title, detail]) {
  return `<article class="tool-card" data-state="${state}" aria-label="Tool ${label}">
    <div class="tool-card__head"><span class="state-dot" aria-hidden="true"></span><strong>${title}</strong><span class="status-text">${label}</span></div>
    <p>${detail}</p>
    <details><summary>Details</summary><pre>${state === 'tool-failure' ? 'error: permission_denied' : 'event: ' + state}</pre></details>
  </article>`;
}

app.innerHTML = `
  <main class="shell">
    <header class="topbar">
      <div><p class="eyebrow">Support agent</p><h1>Account review</h1></div>
      <div class="connection" data-state="disconnected" role="status"><span aria-hidden="true">●</span> Connection interrupted ${button('Reconnect', 'tertiary', 'data-action="reconnect"')}</div>
    </header>

    <section class="thread" aria-label="Conversation">
      <article class="message message--user"><p class="message__role">You</p><p>Check the customer history, explain the issue, and ask before making any account change.</p></article>

      <article class="message message--assistant" data-state="streaming" aria-live="polite">
        <p class="message__role">Assistant · generating</p>
        <p>I found a recent billing mismatch. I’m checking the account history and policy before suggesting a change.<span class="stream-caret" aria-hidden="true"></span></p>
        ${button('Stop', 'secondary', 'data-action="stop"')}
      </article>

      <section class="activity" aria-label="Tool activity">
        <div class="section-title"><h2>Activity</h2><span>Provider-exposed tool events</span></div>
        ${toolStates.map(toolCard).join('')}
      </section>

      <article class="approval" data-state="approval-required" role="region" aria-labelledby="approval-title">
        <p class="message__role">Approval required</p>
        <h2 id="approval-title">Apply a $24 billing credit?</h2>
        <p>This will add a one-time $24 credit to customer account <strong>AC-2048</strong>. It does not change the subscription or future invoices.</p>
        <div class="approval__actions">
          ${button('Approve $24 credit', 'primary', 'data-action="approve"')}
          ${button('Reject', 'secondary', 'data-action="reject"')}
        </div>
      </article>

      <article class="error-card" data-state="retryable-error" role="alert">
        <div><strong>Couldn’t refresh customer notes</strong><p>The request timed out. Existing conversation content is still available.</p></div>
        ${button('Retry', 'secondary', 'data-action="retry"')}
      </article>
    </section>

    <form class="composer" aria-label="Message composer">
      <label for="message">Message</label>
      <textarea id="message" rows="2" placeholder="Ask a follow-up…"></textarea>
      <div class="composer__footer"><span>Enter to send · Shift+Enter for newline</span>${button('Send', 'primary', 'type="submit"')}</div>
    </form>
  </main>`;

const setNotice = (text) => {
  let notice = document.querySelector('.action-notice');
  if (!notice) {
    notice = document.createElement('div');
    notice.className = 'action-notice';
    notice.setAttribute('role', 'status');
    document.body.appendChild(notice);
  }
  notice.textContent = text;
};

document.addEventListener('click', (event) => {
  const action = event.target.closest('[data-action]')?.dataset.action;
  if (!action) return;
  const messages = {
    reconnect: 'Reconnect requested.', stop: 'Generation stopped.', approve: 'Credit approval recorded.', reject: 'Credit rejected.', retry: 'Retry requested.'
  };
  setNotice(messages[action]);
  if (action === 'stop') {
    const streaming = document.querySelector('[data-state="streaming"]');
    streaming.dataset.state = 'stopped';
    streaming.querySelector('.message__role').textContent = 'Assistant · stopped';
    streaming.querySelector('.stream-caret')?.remove();
  }
});

document.querySelector('.composer').addEventListener('submit', (event) => {
  event.preventDefault();
  const input = document.querySelector('#message');
  if (!input.value.trim()) return;
  setNotice('Message queued.');
  input.value = '';
  input.focus();
});

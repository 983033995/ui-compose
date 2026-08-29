import { chromium } from 'playwright';
import { mkdir, writeFile } from 'node:fs/promises';

const outDir = '../../artifacts/eval-02/agent-chat-baseline';
await mkdir(outDir, { recursive: true });

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
const page = await context.newPage();
const consoleErrors = [];
const pageErrors = [];
page.on('console', (message) => { if (message.type() === 'error') consoleErrors.push(message.text()); });
page.on('pageerror', (error) => pageErrors.push(String(error)));

await page.goto('http://127.0.0.1:4173', { waitUntil: 'networkidle' });
await page.screenshot({ path: `${outDir}/desktop.png`, fullPage: true });

const requiredStates = ['streaming','tool-queued','tool-running','tool-success','tool-failure','approval-required','disconnected','retryable-error'];
const desktop = await page.evaluate((states) => ({
  viewport: { width: innerWidth, height: innerHeight },
  horizontalOverflow: document.documentElement.scrollWidth > innerWidth + 1,
  states: Object.fromEntries(states.map((state) => [state, Boolean(document.querySelector(`[data-state="${state}"]`))])),
  hiddenReasoningCopyPresent: /chain-of-thought|hidden reasoning/i.test(document.body.innerText)
}), requiredStates);

async function keyboardCheck(selector, expectedNotice) {
  await page.reload({ waitUntil: 'networkidle' });
  const locator = page.locator(selector);
  let reachable = false;
  for (let step = 0; step < 64; step += 1) {
    await page.keyboard.press('Tab');
    if (await locator.evaluate((element) => document.activeElement === element)) {
      reachable = true;
      break;
    }
  }
  if (!reachable) return { reachable: false, visibleFocus: false, activated: false, notice: null };
  const focus = await locator.evaluate((element) => {
    const style = getComputedStyle(element);
    const outlineWidth = Number.parseFloat(style.outlineWidth);
    return {
      tag: element.tagName,
      outlineStyle: style.outlineStyle,
      outlineWidth: style.outlineWidth,
      visibleFocus: style.outlineStyle !== 'none' && outlineWidth > 0
    };
  });
  await page.keyboard.press('Enter');
  await page.locator('.action-notice').waitFor({ state: 'visible' });
  const notice = await page.locator('.action-notice').innerText();
  return { reachable, ...focus, activated: notice === expectedNotice, notice };
}

const keyboard = {
  stop: await keyboardCheck('[data-action="stop"]', 'Generation stopped.'),
  retry: await keyboardCheck('[data-action="retry"]', 'Retry requested.'),
  approve: await keyboardCheck('[data-action="approve"]', 'Credit approval recorded.')
};

await page.reload({ waitUntil: 'networkidle' });
const messageInput = page.locator('#message');
await messageInput.focus();
await messageInput.fill('Keyboard message');
await page.keyboard.press('Shift+Enter');
const shiftEnterAddsNewline = (await messageInput.inputValue()).endsWith('\n');
await page.keyboard.press('Enter');
await page.locator('.action-notice').waitFor({ state: 'visible' });
const composerKeyboard = {
  shiftEnterAddsNewline,
  enterSends: await page.locator('.action-notice').innerText() === 'Message queued.',
  valueAfterSend: await messageInput.inputValue(),
  focusPreserved: await messageInput.evaluate((element) => document.activeElement === element)
};

await page.setViewportSize({ width: 390, height: 844 });
await page.reload({ waitUntil: 'networkidle' });
await page.screenshot({ path: `${outDir}/mobile.png`, fullPage: true });
const mobile = await page.evaluate(() => {
  const composer = document.querySelector('.composer').getBoundingClientRect();
  return {
    viewport: { width: innerWidth, height: innerHeight },
    horizontalOverflow: document.documentElement.scrollWidth > innerWidth + 1,
    composer: { top: composer.top, bottom: composer.bottom, left: composer.left, right: composer.right },
    composerReachable: composer.top >= 0 && composer.bottom <= innerHeight + 1
  };
});

await page.setViewportSize({ width: 390, height: 560 });
await page.locator('#message').focus();
const keyboardViewport = await page.evaluate(() => {
  const composer = document.querySelector('.composer').getBoundingClientRect();
  return {
    viewport: { width: innerWidth, height: innerHeight },
    composer: { top: composer.top, bottom: composer.bottom },
    composerReachable: composer.top >= 0 && composer.bottom <= innerHeight + 1,
    activeElement: document.activeElement?.id || document.activeElement?.tagName
  };
});

await page.emulateMedia({ reducedMotion: 'reduce' });
await page.reload({ waitUntil: 'networkidle' });
const reducedMotion = await page.evaluate(() => ({
  matched: matchMedia('(prefers-reduced-motion: reduce)').matches,
  caretAnimationName: getComputedStyle(document.querySelector('.stream-caret')).animationName
}));

const metrics = {
  evidenceLevel: 'rendered-ci',
  fixture: 'agent-chat',
  consoleErrors,
  pageErrors,
  desktop,
  keyboard,
  composerKeyboard,
  mobile,
  keyboardViewport,
  reducedMotion,
  hardFailures: [
    ...(consoleErrors.length || pageErrors.length ? ['runtime-error'] : []),
    ...(desktop.horizontalOverflow || mobile.horizontalOverflow ? ['horizontal-overflow'] : []),
    ...(!mobile.composerReachable || !keyboardViewport.composerReachable ? ['mobile-composer-unreachable'] : []),
    ...(Object.values(desktop.states).some((present) => !present) ? ['missing-required-state'] : []),
    ...(Object.values(keyboard).some((check) => !check.reachable || !check.visibleFocus || !check.activated) ? ['keyboard-action-failure'] : []),
    ...(!composerKeyboard.shiftEnterAddsNewline || !composerKeyboard.enterSends || composerKeyboard.valueAfterSend || !composerKeyboard.focusPreserved ? ['composer-keyboard-failure'] : []),
    ...(!reducedMotion.matched || reducedMotion.caretAnimationName !== 'none' ? ['reduced-motion-failure'] : []),
    ...(desktop.hiddenReasoningCopyPresent ? ['hidden-reasoning-copy'] : [])
  ]
};

await writeFile(`${outDir}/metrics.json`, JSON.stringify(metrics, null, 2) + '\n');
console.log(JSON.stringify(metrics, null, 2));
if (metrics.hardFailures.length) process.exitCode = 1;
await browser.close();

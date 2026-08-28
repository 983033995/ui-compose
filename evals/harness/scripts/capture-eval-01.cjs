const fs = require('node:fs')
const path = require('node:path')
const { chromium } = require('playwright')

const baseUrl = process.env.EVAL_URL || 'http://127.0.0.1:4173'
const artifactDir = process.env.ARTIFACT_DIR || path.resolve(process.cwd(), 'evidence')

fs.mkdirSync(artifactDir, { recursive: true })

async function isVisible(locator) {
  try {
    return await locator.isVisible()
  } catch {
    return false
  }
}

async function captureViewport(browser, name, viewport) {
  const context = await browser.newContext({ viewport })
  const page = await context.newPage()
  const consoleErrors = []
  const pageErrors = []

  page.on('console', (message) => {
    if (message.type() === 'error') consoleErrors.push(message.text())
  })
  page.on('pageerror', (error) => pageErrors.push(String(error)))

  await page.goto(baseUrl, { waitUntil: 'networkidle' })
  await page.locator('.el-table__body-wrapper tbody tr').first().waitFor({ state: 'visible' })

  const initialTableVisible = await isVisible(page.locator('.app-table'))
  const initialBodyOverflow = await page.evaluate(() => ({
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
  }))

  await page.screenshot({
    path: path.join(artifactDir, `${name}-default.png`),
    fullPage: true,
  })

  await page.keyboard.press('Tab')
  const focusState = await page.evaluate(() => {
    const element = document.activeElement
    if (!element || element === document.body) return null
    const style = getComputedStyle(element)
    return {
      tag: element.tagName.toLowerCase(),
      text: (element.textContent || '').trim().slice(0, 80),
      outlineStyle: style.outlineStyle,
      outlineWidth: style.outlineWidth,
      boxShadow: style.boxShadow,
    }
  })

  await page.locator('.el-table__body-wrapper tbody tr').first().click()
  await page.waitForTimeout(250)

  const dialogVisible = await isVisible(page.locator('.el-dialog'))
  const inlineDetailVisible = await isVisible(page.locator('.detail-header'))
  const tableVisibleAfterInspect = await isVisible(page.locator('.app-table'))
  const mobileBackVisible = await isVisible(page.locator('.mobile-back'))

  await page.screenshot({
    path: path.join(artifactDir, `${name}-detail.png`),
    fullPage: true,
  })

  const finalBodyOverflow = await page.evaluate(() => ({
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
  }))

  await context.close()

  return {
    viewport,
    initialTableVisible,
    initialBodyOverflow,
    focusState,
    detailMode: inlineDetailVisible ? 'inline-preview' : dialogVisible ? 'dialog' : 'none',
    dialogVisible,
    inlineDetailVisible,
    tableVisibleAfterInspect,
    mobileBackVisible,
    finalBodyOverflow,
    consoleErrors,
    pageErrors,
  }
}

async function checkReducedMotion(browser) {
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    reducedMotion: 'reduce',
  })
  const page = await context.newPage()
  await page.goto(baseUrl, { waitUntil: 'networkidle' })
  const matches = await page.evaluate(() => matchMedia('(prefers-reduced-motion: reduce)').matches)
  await context.close()
  return { emulationMatches: matches }
}

;(async () => {
  const browser = await chromium.launch({ headless: true })
  try {
    const desktop = await captureViewport(browser, 'desktop', { width: 1440, height: 1000 })
    const mobile = await captureViewport(browser, 'mobile', { width: 390, height: 844 })
    const reducedMotion = await checkReducedMotion(browser)

    const hardFailures = []
    for (const [name, result] of [['desktop', desktop], ['mobile', mobile]]) {
      if (!result.initialTableVisible) hardFailures.push(`${name}: order table is not visible initially`)
      if (result.initialBodyOverflow.overflow) hardFailures.push(`${name}: body overflows before interaction`)
      if (result.finalBodyOverflow.overflow) hardFailures.push(`${name}: body overflows after row inspection`)
      if (result.detailMode === 'none') hardFailures.push(`${name}: row inspection exposes no detail UI`)
      if (result.consoleErrors.length) hardFailures.push(`${name}: console errors detected`)
      if (result.pageErrors.length) hardFailures.push(`${name}: page errors detected`)
      if (!result.focusState) hardFailures.push(`${name}: keyboard Tab did not move focus to an interactive element`)
    }
    if (!reducedMotion.emulationMatches) hardFailures.push('reduced-motion emulation was not observed by the page')

    const metrics = {
      branch: process.env.GITHUB_REF_NAME || null,
      commit: process.env.GITHUB_SHA || null,
      capturedAt: new Date().toISOString(),
      evidenceLevel: 'rendered-ci',
      desktop,
      mobile,
      reducedMotion,
      hardFailures,
    }

    fs.writeFileSync(path.join(artifactDir, 'metrics.json'), JSON.stringify(metrics, null, 2))
    console.log(JSON.stringify(metrics, null, 2))

    if (hardFailures.length) process.exitCode = 1
  } finally {
    await browser.close()
  }
})().catch((error) => {
  console.error(error)
  process.exitCode = 1
})

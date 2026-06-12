#!/usr/bin/env node
/**
 * Validate every category page's mockups in a real headless browser.
 *
 * Catches what static checks can't: runtime JS errors, DOM mis-nesting
 * (orphan </div> pushing .config-panel out of its mockup), and nodes
 * that never receive .visible.
 *
 * Usage: PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node scripts/validate-mockups.js
 * Exits 1 if any page has a broken mockup.
 */
// Resolve playwright from the global install when not installed locally
// (e.g. when running ad hoc on a workstation without a package.json).
let chromium;
try {
  ({ chromium } = require('playwright'));
} catch {
  ({ chromium } = require('/opt/node22/lib/node_modules/playwright'));
}
const fs = require('fs');
const path = require('path');

const DIR = path.join(__dirname, '..', 'deploy-highlevel');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const files = fs.readdirSync(DIR).filter(f => f.includes('-cat') && f.endsWith('.html')).sort();
  let bad = 0;
  for (const f of files) {
    const errors = [];
    page.removeAllListeners('pageerror');
    page.on('pageerror', e => errors.push(e.message));
    await page.goto('file://' + path.join(DIR, f), { waitUntil: 'load' });
    await page.waitForTimeout(400);
    const rep = await page.evaluate(() => {
      const ms = Array.from(document.querySelectorAll('.ghl-mockup'));
      return {
        total: ms.length,
        noPanel: ms.filter(m => !m.querySelector('.config-panel')).map(m => m.dataset.mockup),
        notVisible: ms.filter(m => {
          const n = m.querySelectorAll('.ghl-node').length;
          const v = m.querySelectorAll('.ghl-node.visible').length;
          return n > 0 && v < n;
        }).map(m => m.dataset.mockup),
      };
    });
    const issues = [];
    if (rep.noPanel.length) issues.push('noPanel: ' + rep.noPanel.join(','));
    if (rep.notVisible.length) issues.push('hidden: ' + rep.notVisible.join(','));
    if (errors.length) issues.push('JS: ' + errors[0].slice(0, 80));
    if (issues.length) {
      bad++;
      console.log('✗', f, '·', issues.join(' | '));
    } else {
      console.log('✓', f, '·', rep.total, 'mockups');
    }
  }
  console.log(bad === 0 ? `ALL ${files.length} PAGES OK` : `${bad} pages broken`);
  await browser.close();
  process.exit(bad ? 1 : 0);
})().catch(e => { console.error('FATAL', e.message); process.exit(2); });

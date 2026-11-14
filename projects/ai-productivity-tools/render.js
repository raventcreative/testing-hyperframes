// Transparent PNG (no background) + preview on the navy AIpreneur background.
const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.join(__dirname, 'carousel.html')); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  const s = await p.$('.slide');
  await s.screenshot({ path: path.join(__dirname, 'out', 'slide-01_transparent.png'), omitBackground: true });
  await p.evaluate(() => { document.body.style.background = 'url(assets/bg.png) center/cover'; });
  await p.waitForTimeout(200);
  await s.screenshot({ path: path.join(__dirname, 'out', 'slide-01_preview-navy.png') });
  await b.close(); })();

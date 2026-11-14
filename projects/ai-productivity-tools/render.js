// Renders .slide to out/ as transparent PNG (no background) plus a white preview.
const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.join(__dirname, 'carousel.html')); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  const s = await p.$('.slide');
  await s.screenshot({ path: path.join(__dirname, 'out', 'slide-01_transparent.png'), omitBackground: true });
  await p.evaluate(() => document.body.style.background = '#fff');
  await s.screenshot({ path: path.join(__dirname, 'out', 'slide-01_preview-white.png') });
  await b.close(); })();

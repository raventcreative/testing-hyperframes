const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.join(__dirname, 'carousel.html')); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
  const s = await p.$$('.slide');
  for (let i = 0; i < s.length; i++) await s[i].screenshot({ path: path.join(__dirname, 'out', `slide-${String(i + 1).padStart(2, '0')}.png`) });
  await b.close(); })();

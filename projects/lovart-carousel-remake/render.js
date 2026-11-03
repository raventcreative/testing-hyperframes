// Render each .slide in carousel.html to out/slide-0N.png (1080x1350)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = __dirname;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.join(dir, 'carousel.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  const s = await p.$$('.slide');
  for (let i = 0; i < s.length; i++) {
    await s[i].screenshot({ path: path.join(dir, 'out', `slide-${String(i + 1).padStart(2, "0")}.png`) });
  }
  await b.close();
})();

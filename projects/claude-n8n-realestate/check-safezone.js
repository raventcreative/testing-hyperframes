// Fails if any visible element in a slide (except the slide itself) sits outside the safe zone.
const { chromium } = require('playwright');
const path = require('path');
const SAFE = { x0: 110, y0: 110, x1: 970, y1: 1240 };
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('http://localhost:8765/carousel.html');
  await p.evaluate(() => document.fonts.ready);
  const bad = await p.evaluate((S) => {
    const out = [];
    document.querySelectorAll('.slide').forEach((s, i) => {
      const o = s.getBoundingClientRect();
      s.querySelectorAll('*').forEach((el) => {
        const r = el.getBoundingClientRect();
        if (!r.width || !r.height || el.closest('defs')) return;
        const x0 = r.left - o.left, y0 = r.top - o.top, x1 = r.right - o.left, y1 = r.bottom - o.top;
        if (x0 < S.x0 - 0.5 || y0 < S.y0 - 0.5 || x1 > S.x1 + 0.5 || y1 > S.y1 + 0.5)
          out.push(`slide ${i + 1}: <${el.tagName.toLowerCase()} class="${el.className.baseVal ?? el.className}"> ${[x0, y0, x1, y1].map(Math.round)}`);
      });
    });
    return out;
  }, SAFE);
  console.log(bad.length ? bad.join('\n') : 'all inside safe zone');
  await b.close();
})();

const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  p.on('console', m => console.log('page:', m.text())); p.on('pageerror', e => console.log('err:', e.message));
  await p.goto('http://127.0.0.1:8765/' + (process.argv[2] || 'cover.html'));
  await p.evaluate(() => document.fonts.ready); await p.waitForFunction(() => window.__ready, null, { timeout: 60000 });
  await (await p.$('.slide')).screenshot({ path: path.join(__dirname, 'out', process.argv[3] || 'slide-01_cover.png') }); await b.close(); })();

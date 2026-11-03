// node shot.cjs <url-path-with-query> <out.png> [w h]   (static server on :8766 at mascot-bizman root)
const { chromium } = require('playwright');
(async () => {
  const [p, out, w = 1400, h = 1000] = process.argv.slice(2);
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const pg = await b.newPage({ viewport: { width: +w, height: +h } });
  pg.on('console', (m) => { if (m.type() === 'error' || m.type() === 'log') console.log('[page]', m.text()); });
  pg.on('pageerror', (e) => console.log('[pageerror]', e.message));
  await pg.goto('http://127.0.0.1:8766/' + p);
  await pg.waitForFunction(() => window.READY, null, { timeout: 120000 });
  await pg.evaluate(() => window.READY);
  await pg.screenshot({ path: out });
  await b.close();
})();

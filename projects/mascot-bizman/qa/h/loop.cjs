// node loop.cjs <query> <outdir> [frames=120] [step=1]  -> transparent PNG frames of loop.html (server :8766)
const { chromium } = require('playwright');
(async () => {
  const [qs, out, n = 120, step = 1] = process.argv.slice(2);
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const pg = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  pg.on('pageerror', (e) => console.log('[pageerror]', e.message));
  await pg.goto('http://127.0.0.1:8766/qa/h/loop.html?' + qs);
  await pg.waitForFunction(() => window.READY, null, { timeout: 120000 });
  await pg.evaluate(() => window.READY);
  for (let f = 0; f < +n; f += +step) {
    await pg.evaluate((f) => window.renderFrame(f), f);
    await pg.locator('#m').screenshot({ path: `${out}/f${String(f).padStart(4, '0')}.png`, omitBackground: true });
  }
  await b.close();
})();

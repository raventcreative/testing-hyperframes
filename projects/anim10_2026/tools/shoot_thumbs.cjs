// Strip thumbnails: a close-up of the robot in each of the 10 styles (same pose as the lookdev), saved full-size to OUT;
// tools/thumbs.py crops them to 144×144 chips (assets/thumbs/<style>.png).  Usage: node tools/shoot_thumbs.cjs <outdir>
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..'), PORT = 8772, OUT = path.resolve(process.argv[2] || 'production/thumbs_raw');
const ALL = ['lego', 'glow', 'comic', 'chalk', 'pixel', 'line', 'explainer', 'ps2', 'flat', 'cgi'];
const CAM = { yaw: 14, pitch: 4, dist: 2.35, target: [0.0, 0.6, 0], fov: 27 };
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const srv = spawn('python3', ['-m', 'http.server', String(PORT), '--bind', '127.0.0.1'], { cwd: ROOT, stdio: 'ignore' });
  let browser;
  try {
    for (let i = 0; i < 50; i++) { try { if ((await fetch(`http://127.0.0.1:${PORT}/tools/stylebot_test.html`)).ok) break; } catch (e) {} await new Promise((r) => setTimeout(r, 150)); }
    browser = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--use-gl=angle', '--enable-webgl', '--ignore-gpu-blocklist'] });
    const page = await browser.newPage({ viewport: { width: 900, height: 1000 } });
    page.on('pageerror', (e) => console.log('[pageerror]', e.message));
    await page.goto(`http://127.0.0.1:${PORT}/tools/stylebot_test.html`, { waitUntil: 'load' });
    await page.evaluate(() => window.__ready);
    for (const id of ALL) {
      const r = await page.evaluate(([id, cam]) => window.shoot(id, 1, cam), [id, CAM]);
      fs.writeFileSync(path.join(OUT, `${id}.png`), Buffer.from(r.png.split(',')[1], 'base64'));
      console.log(id, r.ms.toFixed(0), 'ms');
    }
  } finally { if (browser) await browser.close(); srv.kill(); }
})().catch((e) => { console.error(e); process.exit(1); });

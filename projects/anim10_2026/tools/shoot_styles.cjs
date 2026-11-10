// Lookdev shooter for StyleBot: one PNG per style (same pose), a contact sheet, sweep-transition frames, render timings.
// Runs headless Chromium with SwiftShader (same GL path as the HyperFrames renderer).
// Usage (from the project root):  node tools/shoot_styles.cjs [style ...]   (no args = all 10 + sheet + sweeps)
//   env PORT (default 8771), OUT (default production/lookdev), SWEEP="pixel,line" (A,B of the sweep frames)
// It starts `python3 -m http.server` on PORT in the project root and stops it when done.
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const PORT = +(process.env.PORT || 8771);
const OUT = path.resolve(ROOT, process.env.OUT || 'production/lookdev');
const ALL = ['lego', 'glow', 'comic', 'chalk', 'pixel', 'line', 'explainer', 'ps2', 'flat', 'cgi'];
const NAMES = { lego: 'Lego', glow: 'Glow Sketch', comic: 'Comic', chalk: 'Chalkboard', pixel: 'Pixel Art', line: 'Minimal Line', explainer: 'Explainer 3D', ps2: 'PS2 Style', flat: 'Flat Vector', cgi: 'CGI Motion' };
const args = process.argv.slice(2);
const POSE2 = args.includes('--pose2');
const ids = args.filter((a) => ALL.includes(a));
const only = ids.length > 0;
const list = only ? ids : ALL;
const save = (file, dataUrl) => fs.writeFileSync(path.join(OUT, file), Buffer.from(dataUrl.split(',')[1], 'base64'));
const waitPort = async () => { for (let i = 0; i < 50; i++) { try { const r = await fetch(`http://127.0.0.1:${PORT}/tools/stylebot_test.html`); if (r.ok) return; } catch (e) {} await new Promise((r) => setTimeout(r, 150)); } throw new Error('server did not start'); };

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const srv = spawn('python3', ['-m', 'http.server', String(PORT), '--bind', '127.0.0.1'], { cwd: ROOT, stdio: 'ignore' });
  let browser;
  try {
    await waitPort();
    browser = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--use-gl=angle', '--enable-webgl', '--ignore-gpu-blocklist'] });
    const page = await browser.newPage({ viewport: { width: 900, height: 1000 } });
    page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') console.log('[page]', m.text().slice(0, 400)); });
    page.on('pageerror', (e) => console.log('[pageerror]', e.message));
    await page.goto(`http://127.0.0.1:${PORT}/tools/stylebot_test.html`, { waitUntil: 'load' });
    await page.evaluate(() => window.__ready);
    const createMs = await page.evaluate(() => window.createMs);
    const gl = await page.evaluate(() => { const g = window.bot.renderer.getContext(); const e = g.getExtension('WEBGL_debug_renderer_info'); return e ? g.getParameter(e.UNMASKED_RENDERER_WEBGL) : g.getParameter(g.RENDERER); });
    console.log(`renderer: ${gl}`);
    console.log(`create() incl. GLB load + warm-up of all styles: ${createMs.toFixed(0)} ms`);
    const shots = [];
    for (const id of list) {
      const r = await page.evaluate((id) => window.shoot(id, 3), id);
      save(`${String(ALL.indexOf(id) + 1).padStart(2, '0')}_${id}.png`, r.png);
      console.log(`${id.padEnd(10)} ${r.ms.toFixed(0).padStart(5)} ms   (${r.all.map((x) => x.toFixed(0)).join(' / ')})`);
      shots.push({ label: `${ALL.indexOf(id) + 1}. ${NAMES[id]}`, sub: `${r.ms.toFixed(0)} ms`, png: r.png });
    }
    if (POSE2) for (const id of list) { save(`pose2_${id}.png`, await page.evaluate((id) => window.shootPose2(id), id)); console.log('pose2', id); }
    if (!only) {
      const sheet = await page.evaluate((items) => window.makeSheet(items, 5), shots);
      save('styles_sheet.png', sheet);
      const ck = await page.evaluate((ids) => window.checks(ids), ALL);
      console.log('determinism (same state rendered twice, other styles in between):', JSON.stringify(ck.det));
      console.log('hook flash (one frame per style, switching every frame), ms:', ck.flash.map(([i, ms]) => `${i}:${ms}`).join(' '));
      const [a, b] = (process.env.SWEEP || 'pixel,line').split(',');
      for (const u of [0.3, 0.5, 0.7]) {
        const r = await page.evaluate(([a, b, u]) => window.shootSweep(a, b, u, 18), [a, b, u]);
        save(`sweep_${a}_${b}_${String(Math.round(u * 100)).padStart(2, '0')}.png`, r.png);
        console.log(`sweep ${a}->${b} u=${u}: ${r.ms.toFixed(0)} ms`);
      }
    }
  } finally {
    if (browser) await browser.close();
    srv.kill();
  }
})().catch((e) => { console.error(e); process.exit(1); });

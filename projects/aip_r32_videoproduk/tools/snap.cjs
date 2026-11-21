// Real-runtime snapshots: node tools/snap.cjs <port> <outdir> t1 t2 ... -> outdir/f_<t>.png (seeks the GSAP timeline + dispatches hf-seek)
const { chromium } = require("playwright");
(async () => {
  const [port, out, ...ts] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  p.on("console", (m) => { if (m.type() === "error") console.error("console", m.text()); });
  await p.goto(`http://127.0.0.1:${port}/index.html`);
  await p.waitForFunction(() => window.__hf && window.__hf.buildReady && window.__hf.buildReady.vx && window.__hf.buildReady.mascot && window.__hf.buildReady.robot, null, { timeout: 90000 });
  await p.evaluate(async () => { await document.fonts.ready; await Promise.all(Object.values(window.__hf.buildReady)); });
  for (const t of ts) {
    await p.evaluate((t) => { window.__timelines.main.seek(t, false); window.dispatchEvent(new CustomEvent("hf-seek", { detail: { time: t } })); }, Number(t));
    await p.waitForTimeout(80);
    await p.screenshot({ path: `${out}/f_${(+t).toFixed(2)}.png` });
  }
  await b.close();
})();

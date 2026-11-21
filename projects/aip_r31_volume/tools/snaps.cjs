// node tools/snaps.cjs <port> <outdir> <t1,t2,...> [scale]  — loads the page once, seeks each time, saves PNG/JPG frames (full UI)
const { chromium } = require("playwright"); const fs = require("fs");
(async () => {
  const [port, out, ts, sc = "0.5"] = process.argv.slice(2); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on("pageerror", (e) => console.error("pageerror", e.message)); p.on("console", (m) => { if (m.type() === "error") console.error("console", m.text()); });
  await p.goto(`http://127.0.0.1:${port}/index.html`);
  await p.waitForFunction(() => window.__hf && window.__hf.buildReady && window.__hf.buildReady.vx && window.__hf.buildReady.mascot && window.__hf.buildReady.robot, null, { timeout: 120000 });
  await p.evaluate(async () => { await Promise.all(Object.values(window.__hf.buildReady)); });
  for (const T of ts.split(",").map(Number)) {
    await p.evaluate(async (t) => { window.__timelines.main.seek(t); const w = []; window.dispatchEvent(new CustomEvent("hf-seek", { detail: { time: t, waitUntil: (x) => w.push(x) } })); await Promise.all(w); }, T);
    await p.waitForTimeout(60);
    const f = `${out}/f_${T.toFixed(2).padStart(6, "0")}.jpg`;
    await p.screenshot({ path: f, type: "jpeg", quality: 85, scale: "css" });
  }
  await b.close();
})();

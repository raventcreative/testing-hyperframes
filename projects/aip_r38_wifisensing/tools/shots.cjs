// Dev stills: node tools/shots.cjs <port> <outdir> <t1,t2,...>  (serve the project root on <port>); SFX=<file> also dumps the sound events
const { chromium } = require("playwright");
(async () => {
  const [port, out, ts] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on("pageerror", (e) => console.error("pageerror", e.message)); p.on("console", (m) => { if (m.type() === "error") console.error("console", m.text()); });
  await p.goto(`http://127.0.0.1:${port}/index.html${process.env.Q || ""}`);
  await p.waitForFunction(() => window.__hf && window.__hf.buildReady && window.__hf.buildReady.ui && window.__hf.buildReady.mascot, null, { timeout: 60000 });
  await p.evaluate(() => Promise.all(Object.values(window.__hf.buildReady)));
  for (const t of (ts || "").split(",").filter(Boolean).map(Number)) {
    await p.evaluate((t) => { window.__timelines.main.seek(t); window.dispatchEvent(new CustomEvent("hf-seek", { detail: { time: t } })); }, t);
    await p.waitForTimeout(60);
    await p.screenshot({ path: `${out}/s_${t.toFixed(2).padStart(6, "0")}.png` });
  }
  if (process.env.SFX) require("fs").writeFileSync(process.env.SFX, JSON.stringify(await p.evaluate(() => window.R38_SFX)));
  await b.close();
})();

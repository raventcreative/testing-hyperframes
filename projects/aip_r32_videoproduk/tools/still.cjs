// Clean still at time T (UI hidden): node tools/still.cjs <port> <T> <out.png> [world|host|both]
const { chromium } = require("playwright");
(async () => {
  const [port, T, out, mode = "both"] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto(`http://127.0.0.1:${port}/index.html`);
  await p.waitForFunction(() => window.__hf && window.__hf.buildReady && window.__hf.buildReady.vx && window.__hf.buildReady.mascot && window.__hf.buildReady.robot, null, { timeout: 60000 });
  await p.evaluate(async (t) => { await Promise.all(Object.values(window.__hf.buildReady));
    window.__timelines.main.seek(t); document.getElementById("ui").style.display = "none";
    window.dispatchEvent(new CustomEvent("hf-seek", { detail: { time: t } })); }, Number(T));
  await p.evaluate((m) => { if (m === "world") document.getElementById("host").style.display = "none";
    if (m === "host") { document.getElementById("stage").style.display = "none"; const h2 = document.getElementById("host2"); if (h2) h2.style.display = "none"; document.documentElement.style.background = "transparent"; document.body.style.background = "transparent"; } }, mode);
  await p.waitForTimeout(500);
  await p.screenshot({ path: out, omitBackground: mode === "host" });
  await b.close();
})();

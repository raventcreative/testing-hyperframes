// node tools/cover_assets.cjs <port> <T>  -> thumbnail/topic3d.png (transparent) + thumbnail/host_cut.png (mascot only, transparent)
const { chromium } = require("playwright");
(async () => { const [port, T] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  let p = await b.newPage({ viewport: { width: 800, height: 800 } }); p.on("pageerror", (e) => console.error(e.message));
  await p.goto(`http://127.0.0.1:${port}/thumbnail/topic3d.html`); await p.waitForFunction(() => window.READY === true, null, { timeout: 60000 });
  await p.screenshot({ path: "thumbnail/topic3d.png", omitBackground: true });
  p = await b.newPage({ viewport: { width: 1080, height: 1920 } }); p.on("pageerror", (e) => console.error(e.message));
  await p.goto(`http://127.0.0.1:${port}/index.html`);
  await p.waitForFunction(() => window.__hf && window.__hf.buildReady && window.__hf.buildReady.mascot, null, { timeout: 120000 });
  await p.evaluate(async (t) => { await Promise.all(Object.values(window.__hf.buildReady)); window.__timelines.main.seek(t);
    for (const id of ["ui", "stage", "cohost"]) document.getElementById(id).style.display = "none";
    document.documentElement.style.background = "transparent"; document.body.style.background = "transparent";
    const w = []; window.dispatchEvent(new CustomEvent("hf-seek", { detail: { time: t, waitUntil: (x) => w.push(x) } })); await Promise.all(w); }, Number(T));
  await p.waitForTimeout(300); await p.screenshot({ path: "thumbnail/host_full.png", omitBackground: true }); await b.close(); })();

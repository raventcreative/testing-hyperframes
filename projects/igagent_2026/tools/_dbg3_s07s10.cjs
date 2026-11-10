const { chromium } = require("playwright");
(async () => {
  const b = await chromium.launch({ args: ["--use-gl=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1400, height: 1000 } });
  await p.goto("http://localhost:3020/#project/igagent_2026", { waitUntil: "load" });
  let f = null;
  for (let i = 0; i < 40 && !f; i++) { await p.waitForTimeout(500); f = p.frames().find((x) => x.url().includes("/preview")); }
  await p.waitForTimeout(6000);
  const r = await f.evaluate(() => {
    const o = document.getElementById("s08-old"); const tl = window.__timelines["s08"]; const tw = tl.getTweensOf(o)[1];
    const out = [];
    tl.seek(0.3); out.push("prog " + tw.progress() + " active " + tw.isActive() + " style " + o.style.clipPath);
    let pt = tw._pt.t._pt, n = 0; out.push("props " + JSON.stringify(tw._pt.t._props)); while (pt && n < 10) { out.push("pt p=" + pt.p + " b=" + String(pt.b).slice(0,90) + " pr=" + String(pt.pr) + " s=" + String(pt.s).slice(0, 80) + " c=" + pt.c + " e=" + String(pt.e).slice(0,80)); pt = pt._next; n++; }
    return out.join("\n");
  });
  console.log(r);
  await b.close();
})();

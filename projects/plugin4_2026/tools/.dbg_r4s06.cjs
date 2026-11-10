const { chromium } = require("playwright");
(async () => {
  const b = await chromium.launch({ args: ["--use-gl=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1400, height: 1000 } });
  await p.goto("http://localhost:3018/#project/plugin4_2026", { waitUntil: "load" });
  let f = null;
  for (let i = 0; i < 40 && !f; i++) { await p.waitForTimeout(500); f = p.frames().find((x) => x.url().includes("/preview")); }
  await p.waitForTimeout(6000);
  const info = await f.evaluate(async () => {
    await window.__player.seek(39.217); await new Promise((r) => setTimeout(r, 800));
    const bf = document.getElementById("r4-bf"), cs = getComputedStyle(bf);
    const out = ["bf bg=" + cs.backgroundColor + " bgimg=" + cs.backgroundImage + " op=" + cs.opacity];
    let e = bf; while (e) { const c = getComputedStyle(e); out.push(e.tagName + "#" + e.id + " op=" + c.opacity + " pos=" + c.position + " z=" + c.zIndex + " tf=" + c.transform + " mix=" + c.mixBlendMode + " filt=" + c.filter + " iso=" + c.isolation); e = e.parentElement; }
    const cx = document.getElementById("r4-cx"); const c2 = getComputedStyle(cx); out.push("cx z=" + c2.zIndex + " mix=" + c2.mixBlendMode + " pos=" + c2.position);
    const r = bf.getBoundingClientRect(); out.push("bf rect " + JSON.stringify(r));
    return out.join("\n");
  });
  console.log(info);
  const fe = await p.$("iframe"); const box = await fe.boundingBox(); console.log("iframe", JSON.stringify(box));
  await p.screenshot({ path: "/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/dbg_a.png" });
  await f.evaluate(() => { document.getElementById("r4-cx").style.visibility = "hidden"; });
  await p.waitForTimeout(300); await p.screenshot({ path: "/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/dbg_b.png" });
  await b.close();
})();

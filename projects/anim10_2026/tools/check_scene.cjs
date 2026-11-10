// Script-error check for scene compositions (snapshots fail SILENTLY when a scene script throws: the scene just stays static).
// Needs the shared preview server:  npx --yes hyperframes@0.8.186 preview . --port 3013 --no-open   (already running? curl localhost:3011)
// Usage: node tools/check_scene.cjs w02 w03      -> prints "ok <duration>" per scene, or the exception thrown by its script.
const { chromium } = require("playwright");
const ids = process.argv.slice(2);
(async () => {
  const b = await chromium.launch({ args: ["--use-gl=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1400, height: 1000 } });
  await p.goto("http://localhost:3013/#project/repo9_2026", { waitUntil: "load" });
  let f = null;
  for (let i = 0; i < 40 && !f; i++) { await p.waitForTimeout(500); f = p.frames().find((x) => x.url().includes("/preview")); }
  await p.waitForTimeout(6000);
  for (const id of ids) {
    const r = await f.evaluate(async (id) => {
      const tl = (window.__timelines || {})[id];
      if (tl) return "ok " + tl.duration().toFixed(3);
      const html = await (await fetch("compositions/" + id + ".html?x=" + Math.random())).text();
      const js = html.split("<script>")[1].split("</script>")[0];
      try { new Function(js)(); return "NOT REGISTERED (script ran without throwing when re-run: check the timeline key)"; }
      catch (e) { return "ERROR " + e.message + " @ " + (e.stack || "").split("\n").slice(1, 3).join(" | "); }
    }, id);
    console.log(id, r);
  }
  await b.close();
})();

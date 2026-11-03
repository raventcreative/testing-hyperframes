// Renders thumbnail/thumb.html to PNG. Usage (from project root, with a static server on :8765):
//   node thumbnail/render_thumb.cjs <t> <out.png> [mouth]
const { chromium } = require("playwright");
(async () => {
  const [t, out, mouth] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto(`http://127.0.0.1:8765/thumbnail/thumb.html?t=${t}${mouth ? "&mt=" + mouth : ""}`);
  await p.evaluate(() => window.THUMB_READY);
  await p.waitForTimeout(300);
  await p.screenshot({ path: out });
  await b.close();
})();

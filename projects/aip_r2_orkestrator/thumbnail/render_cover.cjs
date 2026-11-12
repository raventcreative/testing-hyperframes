// Renders thumbnail/cover.html to PNG. Usage (from project root, static server on :8782): node thumbnail/render_cover.cjs <out.png>
const { chromium } = require("playwright");
(async () => {
  const [out] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.setDefaultTimeout(300000); p.setDefaultNavigationTimeout(300000);   // the render box can be busy
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto("http://127.0.0.1:8782/thumbnail/cover.html" + (process.argv[3] ? "?" + process.argv[3] : ""));
  await p.evaluate(() => window.COVER_READY);
  await p.waitForTimeout(300);
  await p.screenshot({ path: out });
  await b.close();
})();

// Renders thumbnail/cover.html to PNG. Usage (from project root, static server on :8767): node thumbnail/render_cover.cjs <out.png>
const { chromium } = require("playwright");
(async () => {
  const [out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto("http://127.0.0.1:8767/thumbnail/cover.html");
  await p.evaluate(() => window.COVER_READY);
  await p.waitForTimeout(300);
  await p.screenshot({ path: out });
  await b.close();
})();

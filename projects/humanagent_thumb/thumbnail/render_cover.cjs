// Renders thumbnail/cover.html to PNG (file:// — no server needed). Usage (from the project root): node thumbnail/render_cover.cjs <out.png> [query]
const { chromium } = require("playwright");
const path = require("path");
(async () => {
  const [out, query] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto("file://" + path.resolve(__dirname, "cover.html") + (query ? "?" + query : ""));
  await p.waitForFunction(() => window.COVER_READY === true, null, { timeout: 60000 });
  await p.waitForTimeout(200);
  await p.screenshot({ path: out });
  await b.close();
})();

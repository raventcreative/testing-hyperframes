// Renders thumbnail/cover.html to PNG. Usage (from the project root, with a static server on :8833 serving the project root,
// e.g. `python3 -m http.server 8833`): node thumbnail/render_cover.cjs <out.png> [dsf=1]   (dsf 2 -> HD 2160x3840)
// COVER_URL=<url> overrides the page URL; extra query (mascot framing): COVER_Q="mx=540&my=2230&mh=1060".
const { chromium } = require("playwright");
(async () => {
  const [out, dsf] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: +(dsf || 1) });
  p.setDefaultTimeout(300000); p.setDefaultNavigationTimeout(300000);
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto((process.env.COVER_URL || "http://127.0.0.1:8833/thumbnail/cover.html") + (process.env.COVER_Q ? "?" + process.env.COVER_Q : ""));
  await p.evaluate(() => window.COVER_READY);
  await p.waitForTimeout(300);
  await p.screenshot({ path: out });
  await b.close();
})();

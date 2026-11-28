// node thumbnail/cover.cjs <out.png> [dsf]
const { chromium } = require("playwright"); const path = require("path");
(async () => { const [out, dsf] = process.argv.slice(2); const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: Number(dsf || 1) });
  await p.goto("file://" + path.resolve(__dirname, "cover.html")); await p.waitForFunction(() => window.COVER_READY === true);
  await p.waitForTimeout(300); await p.screenshot({ path: out }); await b.close(); })();

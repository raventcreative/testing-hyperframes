// Renders thumbnail/cover.html to PNG. Usage (from project root, static server on :8783): node thumbnail/render_cover.cjs <out.png> [query]
// Also prints the rects of the key layers (and any text that overflows its box) so overlaps can be checked numerically.
const { chromium } = require("playwright");
(async () => {
  const [out] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.setDefaultTimeout(600000);
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto("http://127.0.0.1:8783/thumbnail/cover.html" + (process.argv[3] ? "?" + process.argv[3] : ""), { timeout: 600000 });
  await p.evaluate(() => window.COVER_READY);
  await p.waitForTimeout(300);
  const info = await p.evaluate(() => {
    const r = (s) => { const e = document.querySelector(s); if (!e) return null; const b = e.getBoundingClientRect(); return [s, Math.round(b.left), Math.round(b.top), Math.round(b.right), Math.round(b.bottom)].join(" "); };
    const rows = ["#logo", "#eyebrow > span", "#h1", "#k1", "#term"].map(r);
    for (const sel of ["#h1", "#k1"]) { const e = document.querySelector(sel), g = document.createRange(); g.selectNodeContents(e); const b = g.getBoundingClientRect(); rows.push(`${sel} text ${Math.round(b.left)}-${Math.round(b.right)}`); }
    document.querySelectorAll(".cart .tx").forEach((e, k) => { const c = e.parentElement.getBoundingClientRect(), t = e.getBoundingClientRect(); rows.push(`cart${k} text right ${Math.round(t.right)} / cart right ${Math.round(c.right - 18)}`); });
    return rows.join("\n");
  });
  console.log(info);
  await p.screenshot({ path: out });
  await b.close();
})();

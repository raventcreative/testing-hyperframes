// Renders thumbnail/cover.html to PNG. Usage (from project root, static server on :8937): node thumbnail/render_cover.cjs <out.png> [query]
// Also prints the rects of the key layers (and any text that overflows its box) so overlaps can be checked numerically.
const { chromium } = require("playwright");
(async () => {
  const [out] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.setDefaultTimeout(600000);
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  p.on("requestfailed", (r) => console.error("requestfailed", r.url()));
  p.on("response", (r) => { if (r.status() >= 400) console.error("http", r.status(), r.url()); });
  await p.goto("http://127.0.0.1:8937/thumbnail/cover.html" + (process.argv[3] ? "?" + process.argv[3] : ""), { timeout: 600000 });
  await p.evaluate(() => window.COVER_READY);
  await p.waitForTimeout(300);
  const info = await p.evaluate(() => {
    const R = (e) => { const b = e.getBoundingClientRect(); return [Math.round(b.left), Math.round(b.top), Math.round(b.right), Math.round(b.bottom)]; };
    const r = (s) => { const e = document.querySelector(s); return e ? `${s} ${R(e).join(" ")}` : `${s} MISSING`; };
    const rows = ["#logo", "#chip > span", "#l1", "#h1", "#l3"].map(r);
    for (const sel of ["#l1", "#h1", "#l3"]) { const e = document.querySelector(sel), g = document.createRange(); g.selectNodeContents(e); const b = g.getBoundingClientRect(); rows.push(`${sel} text x ${Math.round(b.left)}-${Math.round(b.right)} y ${Math.round(b.top)}-${Math.round(b.bottom)}`); }
    document.querySelectorAll(".bp").forEach((e, k) => rows.push(`card${k} ${R(e).join(" ")}`));
    document.querySelectorAll(".bp .nm, .bp .ct").forEach((e) => { const t = e.getBoundingClientRect(), b = e.parentElement.getBoundingClientRect(); if (t.right > b.right - 6) rows.push(`OVERFLOW ${e.textContent} ${Math.round(t.right)} > ${Math.round(b.right)}`); });
    return rows.join("\n");
  });
  console.log(info);
  await p.screenshot({ path: out });
  await b.close();
})();

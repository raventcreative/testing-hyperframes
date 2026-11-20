// node thumbnail/render.cjs <page> <out.png> [query] [dsf] — static server on PORT at the project root. Prints text boxes (no-cut check).
const { chromium } = require("playwright");
(async () => {
  const [page, out, query = "", dsf = "1"] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const isLogo = page.includes("logo3d");
  const p = await b.newPage({ viewport: isLogo ? { width: 800, height: 800 } : { width: 1080, height: 1920 }, deviceScaleFactor: Number(dsf) });
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto(`http://127.0.0.1:${process.env.PORT}/thumbnail/${page}${query ? "?" + query : ""}`, { timeout: 120000 });
  await p.waitForFunction(() => window.COVER_READY === true || window.READY === true, null, { timeout: 60000 });
  if (!isLogo) console.log(await p.evaluate(() => ["#logo", "#chip span", "#h1", "#h2", "#tag", "#ico"].map((s) => { const e = document.querySelector(s); if (!e) return s + " -";
    const r = document.createRange(); r.selectNodeContents(e); const b = (e.tagName === "IMG" ? e : r).getBoundingClientRect(); return `${s} x ${Math.round(b.left)}-${Math.round(b.right)} y ${Math.round(b.top)}-${Math.round(b.bottom)}`; }).join("\n")));
  await p.screenshot({ path: out, omitBackground: true });
  await b.close();
})();

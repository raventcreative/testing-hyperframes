// R28 cover tools. Serve the project root first:  python3 -m http.server 8958 --bind 127.0.0.1
//   node thumbnail/render.cjs logo  -> thumbnail/logo3d_claude.png (transparent, then trimmed to logo3d_claude_cut.png by PIL)
//   node thumbnail/render.cjs cover -> thumbnail/COVER_SISTEM_1080x1920.png + COVER_SISTEM_HD_2160x3840.png
const { chromium } = require("playwright"); const path = require("path");
const PORT = process.env.PORT || 8958, D = __dirname;
(async () => {
  const what = process.argv[2];
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  if (what === "logo") {
    const p = await b.newPage({ viewport: { width: 800, height: 800 } });
    p.on("pageerror", (e) => console.error("pageerror", e.message));
    await p.goto(`http://127.0.0.1:${PORT}/thumbnail/logo3d.html`); await p.waitForFunction(() => window.READY === true, null, { timeout: 60000 });
    await p.screenshot({ path: path.join(D, "logo3d_claude.png"), omitBackground: true });
  } else {
    for (const [dsf, name] of [[1, "COVER_SISTEM_1080x1920.png"], [2, "COVER_SISTEM_HD_2160x3840.png"]]) {
      const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: dsf });
      await p.goto(`http://127.0.0.1:${PORT}/thumbnail/cover.html`); await p.waitForFunction(() => window.COVER_READY === true);
      await p.waitForTimeout(300);
      const w = await p.evaluate(() => ["#h1", "#h2", "#tag", "#chip span"].map((s) => { const e = document.querySelector(s), g = document.createRange(); g.selectNodeContents(e); const r = g.getBoundingClientRect(); return `${s} x ${Math.round(r.left)}-${Math.round(r.right)} y ${Math.round(r.top)}-${Math.round(r.bottom)}`; }));
      console.log(w.join("\n"));
      await p.screenshot({ path: path.join(D, name) }); await p.close();
    }
  }
  await b.close();
})();

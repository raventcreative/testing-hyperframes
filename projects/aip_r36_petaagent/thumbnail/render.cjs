// node thumbnail/render.cjs <port> <page.html?query> <out.png> [w] [h]  -> transparent screenshot of a WebGL page (serve the project root)
const { chromium } = require("playwright");
(async () => { const [port, page, out, w = 800, h = 800] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: Number(w), height: Number(h) } }); p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto(`http://127.0.0.1:${port}/thumbnail/${page}`); await p.waitForFunction(() => window.READY === true, null, { timeout: 90000 });
  await p.waitForTimeout(300); await p.screenshot({ path: out, omitBackground: true }); await b.close(); })();

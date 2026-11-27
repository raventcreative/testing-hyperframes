// node tools/logo3d.cjs <port> <name> <out.png>  (serve the project root on <port>)
const { chromium } = require("playwright");
(async () => { const [port, name, out] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 800, height: 800 } });
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto(`http://127.0.0.1:${port}/thumbnail/logo3d.html?name=${name}`); await p.waitForFunction(() => window.READY === true, null, { timeout: 30000 });
  await p.screenshot({ path: out, omitBackground: true }); await b.close(); })();

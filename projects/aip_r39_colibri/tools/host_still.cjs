// node tools/host_still.cjs <port> <t> <out.png>  (serve the project root on <port>) — transparent mascot still for the cover
const { chromium } = require("playwright");
(async () => { const [port, t, out] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1400, height: 1800 } }); p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto(`http://127.0.0.1:${port}/thumbnail/host.html?t=${t}`); await p.waitForFunction(() => window.READY === true, null, { timeout: 60000 });
  await p.screenshot({ path: out, omitBackground: true }); await b.close(); })();

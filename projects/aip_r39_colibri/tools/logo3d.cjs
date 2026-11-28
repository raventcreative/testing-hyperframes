// node tools/logo3d.cjs <port> <query> <out.png>   (serve the project root on <port>)
//   query "name=deepseek" -> 800x800 still · "name=deepseek&sheet=24" -> sprite strip (24 x 220 px) · "icon=cpu&col=%2301ccf7"
const { chromium } = require("playwright"); const fs = require("fs");
(async () => { const [port, q, out] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 800, height: 800 } });
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto(`http://127.0.0.1:${port}/thumbnail/logo3d.html?${q}`); await p.waitForFunction(() => window.READY === true, null, { timeout: 60000 });
  const sheet = await p.evaluate(() => window.SHEET || null);
  if (sheet) fs.writeFileSync(out, Buffer.from(sheet.split(",")[1], "base64")); else await p.screenshot({ path: out, omitBackground: true });
  await b.close(); })();

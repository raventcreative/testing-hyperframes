// Renders the 3D topic logos (tools/logo3d.html) into turntable frames + a still.
// Usage (serve tools/ on PORT first, e.g. `python3 -m http.server 8971 -d tools`):
//   node tools/logo3d.cjs <port> <name> <outdir> [n=36] [size=300]
// Writes <outdir>/<name>_f00.png … and <outdir>/<name>_still.png (800 px); tools/sprite.py packs the frames.
const { chromium } = require("playwright");
(async () => {
  const [port, name, outdir, n = "36", size = "300"] = process.argv.slice(2);
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: +size, height: +size } });
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  for (let i = 0; i < +n; i++) {
    await p.goto(`http://127.0.0.1:${port}/logo3d.html?name=${name}&n=${n}&frame=${i}&size=${size}`);
    await p.waitForFunction(() => window.READY === true, null, { timeout: 60000 });
    await p.screenshot({ path: `${outdir}/${name}_f${String(i).padStart(2, "0")}.png`, omitBackground: true });
  }
  await p.setViewportSize({ width: 800, height: 800 });
  await p.goto(`http://127.0.0.1:${port}/logo3d.html?name=${name}&still=1&size=800`);
  await p.waitForFunction(() => window.READY === true, null, { timeout: 60000 });
  await p.screenshot({ path: `${outdir}/${name}_still.png`, omitBackground: true });
  await b.close();
})();

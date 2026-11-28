// Renders tools/logo_sprites.html for each logo to assets/logos3d/<name>.png (1440x1440, 6x6 turntable). Static server on PORT.
const { chromium } = require("playwright");
const L = [["github", "#181717"], ["claude", "#D97757"], ["espressif", "#E7352C"], ["homeassistant", "#18BCF2"]];
(async () => {
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  for (const [n, c] of L) {
    const p = await b.newPage({ viewport: { width: 1440, height: 1440 } });
    p.on("pageerror", (e) => console.error("pageerror", e.message));
    await p.goto(`http://127.0.0.1:${process.env.PORT}/tools/logo_sprites.html?name=${n}&col=${encodeURIComponent(c)}`);
    await p.waitForFunction(() => window.READY === true, null, { timeout: 120000 });
    await p.locator("#c").screenshot({ path: `assets/logos3d/${n}.png`, omitBackground: true });
    console.log("ok", n); await p.close();
  }
  await b.close();
})();

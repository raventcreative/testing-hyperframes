// 3D logos from Simple Icons (CC0) via logo3d.html. Needs: python3 -m http.server 8766 here.
const { chromium } = require("playwright"); const fs = require("fs"); const path = require("path");
const L = [["claude", "D97757", -0.4], ["instagram", "FF0069", 0.35], ["tiktok", "FFFFFF", -0.35]];
(async () => {
  fs.mkdirSync(path.join(__dirname, "assets/3d"), { recursive: true });
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 700, height: 700 } });
  for (const [s, c, ry] of L) {
    await p.goto(`http://localhost:8766/logo3d.html?s=${s}&c=${c}&ry=${ry}`); await p.waitForFunction(() => window.READY, null, { timeout: 60000 });
    await p.screenshot({ path: path.join(__dirname, `assets/3d/${s}.png`), omitBackground: true }); console.log("ok", s);
  }
  await b.close();
})();

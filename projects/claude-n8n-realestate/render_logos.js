// Renders each Simple Icons logo as a 3D PNG (needs: python3 -m http.server 8765 in this folder). Output: assets/3d/<slug>.png (trimmed)
const { chromium } = require("playwright"); const fs = require("fs"); const path = require("path");
const L = [["claude", "D97757", -0.4], ["n8n", "EA4B71", 0.35], ["whatsapp", "25D366", -0.3], ["googlecalendar", "4285F4", 0.3], ["facebook", "0866FF", -0.3], ["gmail", "EA4335", 0.3]];
(async () => {
  fs.mkdirSync(path.join(__dirname, "assets/3d"), { recursive: true });
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 700, height: 700 } });
  for (const [s, c, ry] of L) {
    await p.goto(`http://localhost:8765/logo3d.html?s=${s}&c=${c}&ry=${ry}`); await p.waitForFunction(() => window.READY, null, { timeout: 60000 });
    await p.screenshot({ path: path.join(__dirname, `assets/3d/${s}.png`), omitBackground: true }); console.log("ok", s);
  }
  await b.close();
})();

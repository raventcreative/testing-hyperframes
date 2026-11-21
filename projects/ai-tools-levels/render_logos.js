// 3D logos (Simple Icons CC0 + Lobe Icons MIT) via logo3d.html. Needs: python3 -m http.server 8767 here.
const { chromium } = require("playwright"); const path = require("path");
const ALL = [["openai","FFFFFF",-0.35],["lovable","FE529A",0.35],["claudecode","D97757",-0.35],["capcut","FFFFFF",0.35],["hailuo","FF5538",-0.35],["kling","0DF35E",0.35],
 ["zapier","FF4F00",-0.35],["make","7B2CFF",0.35],["n8n","EA4B71",-0.35],["shopify","7AB55C",0.35],["framer","FFFFFF",-0.35],["replit","F26207",0.35],
 ["googlegemini","8E75B2",-0.35],["perplexity","1FB8CD",0.35],["notebooklm","FFFFFF",-0.35]];
const L = process.argv[2] ? ALL.filter(x => process.argv.slice(2).includes(x[0])) : ALL;
(async () => {
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 700, height: 700 } });
  for (const [s, c, ry] of L) {
    await p.goto(`http://localhost:8767/logo3d.html?s=${s}&c=${c}&ry=${ry}`); await p.waitForFunction(() => window.READY, null, { timeout: 60000 });
    await p.screenshot({ path: path.join(__dirname, `assets/3d/${s}.png`), omitBackground: true }); console.log("ok", s);
  }
  await b.close();
})();

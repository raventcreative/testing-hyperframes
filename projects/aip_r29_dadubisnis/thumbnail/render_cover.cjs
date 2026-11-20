// node thumbnail/render_cover.cjs <out.png> [dsf]  — renders thumbnail/cover.html (files served from disk via request routing)
const { chromium } = require("/opt/node-tools/node_modules/playwright");
const path = require("path"), fs = require("fs");
const MIME = { ".html": "text/html", ".js": "text/javascript", ".png": "image/png", ".woff2": "font/woff2", ".glb": "model/gltf-binary", ".wasm": "application/wasm" };
(async () => {
  const [out, dsf = "1"] = process.argv.slice(2); const root = path.resolve(__dirname, "..");
  const b = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: Number(dsf) });
  await p.route("http://proj.local/**", (r) => { const f = path.join(root, decodeURIComponent(new URL(r.request().url()).pathname));
    if (!fs.existsSync(f)) return r.fulfill({ status: 404, body: "" }); r.fulfill({ status: 200, path: f, contentType: MIME[path.extname(f)] || "application/octet-stream" }); });
  p.on("pageerror", (e) => console.error("pageerror", e.message));
  await p.goto(`http://proj.local/thumbnail/cover.html?dsf=${dsf}`);
  await p.waitForFunction(() => window.COVER_READY === true, null, { timeout: 120000 });
  await p.waitForTimeout(300); await p.screenshot({ path: out }); await b.close(); console.log("ok", out);
})();

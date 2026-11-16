// Renders prompt slides (2-6) to MP4: node render_video.js  -> out/slide-0N.mp4 (1080x1350, 30 fps, 7 s, H.264)
const { chromium } = require("playwright"); const path = require("path"); const fs = require("fs"); const { execFileSync } = require("child_process");
const FPS = 30, DUR = 7;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto("file://" + path.join(__dirname, "carousel.html")); await p.evaluate(() => document.fonts.ready);
  const n = await p.$$eval(".slide", (s) => s.length);
  for (let i = 1; i <= 5; i++) {
    const idx = i; // slides[1..5] are the prompt slides
    const dir = path.join(__dirname, "out", `frames${idx + 1}`); fs.mkdirSync(dir, { recursive: true });
    await p.evaluate((k) => { document.querySelectorAll(".slide").forEach((s, j) => (s.style.display = j === k ? "flex" : "none")); window.scrollTo(0, 0); }, idx);
    const el = (await p.$$(".slide"))[idx];
    for (let f = 0; f < FPS * DUR; f++) {
      await p.evaluate((t) => window.seek(t), f / FPS);
      await el.screenshot({ path: path.join(dir, `f${String(f).padStart(4, "0")}.jpg`), type: "jpeg", quality: 92 });
    }
    const out = path.join(__dirname, "out", `slide-0${idx + 1}.mp4`);
    execFileSync("ffmpeg", ["-v", "error", "-y", "-framerate", String(FPS), "-i", path.join(dir, "f%04d.jpg"), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", "-movflags", "+faststart", out]);
    for (const f of fs.readdirSync(dir)) fs.unlinkSync(path.join(dir, f)); fs.rmdirSync(dir);
    console.log("done", out);
  }
  await b.close();
})();

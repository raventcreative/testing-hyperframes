// Deterministic renderer for the website walkthrough.
//   node render/render.mjs [--q final|draft] [--stills 0.5,2.2] [--out out/final]
// final: 2x device scale (supersampled, Lanczos down to 1920x1080) + 3 motion-blur sub-frames (180deg shutter)
// Output: MP4 H.264 1920x1080 60fps on #00FF00, NO audio stream  +  VP9 alpha WebM (transparent)
import { createRequire } from 'node:module';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
const { chromium } = createRequire(import.meta.url)('playwright');

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(`--${k}`); return i >= 0 ? args[i + 1] : d; };
const Q = opt('q', 'final');
const OUT = path.resolve(ROOT, opt('out', 'out/final'));
const NAME = opt('name', '04_WEBSITE_PREVIEW_MASTERPAJAK_AI_16x9');
const FPS = 60, W = 1920, H = 1080;
const DSF = Q === 'final' ? 2 : 1;
const SUB = Q === 'final' ? 3 : 1;
const SHUTTER = 0.5;
fs.mkdirSync(OUT, { recursive: true });

const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.woff2': 'font/woff2' };
const server = http.createServer((req, res) => {
  let p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  const f = path.join(ROOT, 'src', p === '/' ? 'index.html' : p);
  if (!f.startsWith(path.join(ROOT, 'src')) || !fs.existsSync(f)) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'Content-Type': MIME[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});
await new Promise((r) => server.listen(0, r));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: DSF });
await page.goto(`http://127.0.0.1:${server.address().port}/`);
await page.waitForFunction(() => window.__ready || window.__error, null, { timeout: 60000 });
const err = await page.evaluate(() => window.__error);
if (err) { console.error(err); process.exit(1); }
const DUR = await page.evaluate(() => window.DURATION);
const FRAMES = Math.round(DUR * FPS);

const shot = async (t) => { await page.evaluate((v) => window.seek(v), t); return page.screenshot({ omitBackground: true, type: 'png' }); };

if (opt('stills')) {
  const dir = path.join(OUT, 'stills');
  fs.mkdirSync(dir, { recursive: true });
  for (const t of opt('stills').split(',').map(Number)) {
    const png = await shot(t);
    const f = path.join(dir, `web_${t.toFixed(2)}s.png`);
    await new Promise((res, rej) => {
      const p = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-i', '-', '-filter_complex',
        `[0:v]scale=${W}:${H}:flags=lanczos,format=rgba[a];color=c=0x00FF00:s=${W}x${H}[g];[g][a]overlay=format=rgb,format=rgb24`, '-frames:v', '1', f]);
      p.on('close', (c) => (c ? rej(new Error('ffmpeg')) : res()));
      p.stdin.end(png);
    });
    console.log('still', f);
  }
  await browser.close(); server.close(); process.exit(0);
}

// full render: SUB sub-frames per frame -> premultiply -> average -> unpremultiply
const sel = SUB > 1 ? `tmix=frames=${SUB},select='not(mod(n+1\\,${SUB}))',` : '';
const fc = [
  `[0:v]scale=${W}:${H}:flags=lanczos,format=rgba,premultiply=inplace=1,${sel}unpremultiply=inplace=1,setpts=N/${FPS}/TB,split[a][b]`,
  `color=c=0x00FF00:s=${W}x${H}:r=${FPS}:d=${DUR}[g]`,
  `[g][a]overlay=format=rgb:eof_action=repeat,scale=out_color_matrix=bt709:out_range=tv,format=yuv420p[green]`,
  `[b]format=yuva420p[alpha]`,
].join(';');
const mp4 = path.join(OUT, `${NAME}${Q === 'draft' ? '_DRAFT' : ''}.mp4`);
const webm = path.join(OUT, `${NAME}${Q === 'draft' ? '_DRAFT' : ''}_ALPHA.webm`);
const enc = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS * SUB), '-i', '-',
  '-filter_complex', fc,
  '-map', '[green]', '-an', '-c:v', 'libx264', '-preset', 'slow', '-crf', Q === 'final' ? '12' : '20', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-r', String(FPS),
  '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv', '-movflags', '+faststart', mp4,
  '-map', '[alpha]', '-an', '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p', '-b:v', '0', '-crf', '22', '-row-mt', '1', '-deadline', 'good', '-cpu-used', '4', '-r', String(FPS), webm,
], { stdio: ['pipe', 'inherit', 'inherit'] });
const t0 = Date.now();
for (let i = 0; i < FRAMES; i++) {
  for (let k = 0; k < SUB; k++) {
    const t = SUB === 1 ? i / FPS : i / FPS + ((k + 0.5) / SUB - 0.5) * (SHUTTER / FPS);
    const png = await shot(Math.max(0, Math.min(DUR - 1e-4, t)));
    if (!enc.stdin.write(png)) await new Promise((r) => enc.stdin.once('drain', r));
  }
  if (i % 60 === 0 || i === FRAMES - 1) {
    const per = (Date.now() - t0) / 1000 / (i + 1);
    console.log(`frame ${i + 1}/${FRAMES}  ${per.toFixed(2)} s/frame  eta ${Math.round(per * (FRAMES - i - 1))}s`);
  }
}
enc.stdin.end();
await new Promise((r) => enc.on('close', r));
await browser.close(); server.close();
console.log('wrote', mp4, webm);

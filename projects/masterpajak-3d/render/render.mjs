// Deterministic renderer: headless Chromium (WebGL) -> raw RGBA frames -> FFmpeg.
// Usage:
//   node render/render.mjs v1 [--q final|draft] [--from N --to M] [--stills 0.5,2,4.25] [--prores] [--out dir]
//   node render/render.mjs v1 --probe          (motion QC: screen-space trajectories -> JSON)
//   node render/render.mjs v1 --textures       (export document artwork PNGs + UV regions)
// Outputs (in --out, default ./out):
//   <NAME>.mp4            H.264, 1080x1080, 60 fps, yuv420p BT.709, composited on #00FF00, NO audio stream
//   <NAME>_ALPHA.webm     VP9 with true alpha (transparent background)
//   <NAME>_ALPHA.mov      ProRes 4444 with alpha (only with --prores)
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright'); // pre-installed globally
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const NAMES = {
  v1: '01_STEP_1_RESI_FLOATING_3D',
  v2: '02_STEP_1_REKENING_KORAN_FLOATING_3D',
  v3: '03_STEP_2_DOKUMEN_MENJADI_LAPORAN_KEUANGAN',
};
const args = process.argv.slice(2);
const shot = args[0];
const opt = (k, d) => { const i = args.indexOf(`--${k}`); return i >= 0 ? (args[i + 1] ?? true) : d; };
const flag = (k) => args.includes(`--${k}`);
const quality = opt('q', 'final');
const outDir = path.resolve(ROOT, opt('out', 'out'));
fs.mkdirSync(outDir, { recursive: true });

const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.woff2': 'font/woff2', '.ttf': 'font/ttf', '.svg': 'image/svg+xml', '.png': 'image/png', '.json': 'application/json' };
const server = http.createServer((req, res) => {
  let p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  if (p === '/') p = '/src/index.html';
  const f = path.join(ROOT, p);
  if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'Content-Type': MIME[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});
await new Promise((r) => server.listen(0, r));
const port = server.address().port;

const browser = await chromium.launch({
  args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--disable-gpu-sandbox'],
});
const page = await browser.newPage({ viewport: { width: 1200, height: 1200 } });
page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') console.log('[page]', m.text()); });
const extra = [opt('ssaa') && `&ssaa=${opt('ssaa')}`, opt('sub') && `&sub=${opt('sub')}`].filter(Boolean).join('');
await page.goto(`http://127.0.0.1:${port}/src/index.html?shot=${shot}&q=${quality}${extra}${flag('textures') ? '&mode=textures' : ''}`);
await page.waitForFunction(() => window.__ready || window.__error, null, { timeout: 180000 });
const err = await page.evaluate(() => window.__error);
if (err) { console.error(err); process.exit(1); }
if (flag('textures')) {
  const tex = await page.evaluate(() => window.TEXTURES);
  const dir = path.join(outDir, 'textures');
  fs.mkdirSync(dir, { recursive: true });
  for (const [k, v] of Object.entries(tex)) fs.writeFileSync(path.join(dir, `${k}.png`), Buffer.from(v.split(',')[1], 'base64'));
  fs.writeFileSync(path.join(dir, 'regions_uv.json'), JSON.stringify(await page.evaluate(() => window.REGIONS), null, 2));
  console.log('wrote textures to', dir);
  await browser.close(); server.close();
  process.exit(0);
}
const info = await page.evaluate(() => window.SHOT);
const W = 1080, H = 1080, FPS = info.fps;
console.log(`shot ${shot} (${NAMES[shot]}) ${info.duration}s = ${info.frames} frames, quality=${quality}`);

const grab = async (i) => Buffer.from(await page.evaluate((k) => window.renderFrame(k), i), 'base64');

// --- motion probe (QC): screen-space trajectories, no rendering ---
if (flag('probe')) {
  const rows = [];
  for (let i = 0; i < info.frames; i++) rows.push(await page.evaluate((k) => window.probe(k), i));
  const f = path.join(outDir, `${shot}_motion.json`);
  fs.writeFileSync(f, JSON.stringify({ fps: FPS, rows }));
  console.log('wrote', f);
  await browser.close(); server.close();
  process.exit(0);
}

// --- stills mode (QC): PNG on green + PNG with alpha ---
if (opt('stills')) {
  const times = String(opt('stills')).split(',').map(Number);
  const dir = path.join(outDir, 'stills');
  fs.mkdirSync(dir, { recursive: true });
  for (const t of times) {
    const i = Math.min(info.frames - 1, Math.round(t * FPS));
    const t0 = Date.now();
    const buf = await grab(i);
    const tag = `${shot}_${t.toFixed(2)}s`;
    await ffmpegOnce(buf, ['-filter_complex', `[0:v]vflip[a];color=c=0x00FF00:s=${W}x${H}[g];[g][a]overlay=format=rgb,format=rgb24`, '-frames:v', '1', path.join(dir, `${tag}.png`)]);
    console.log(`still ${tag} (${Date.now() - t0} ms)`);
  }
  await browser.close(); server.close();
  process.exit(0);
}

function ffmpegOnce(buf, outArgs) {
  return new Promise((resolve, reject) => {
    const p = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', `${W}x${H}`, '-i', '-', ...outArgs]);
    p.on('close', (c) => (c === 0 ? resolve() : reject(new Error('ffmpeg ' + c))));
    p.stdin.end(buf);
  });
}

// --- full render ---
const from = Number(opt('from', 0));
const to = Number(opt('to', info.frames));
const name = opt('name', NAMES[shot]) + (quality === 'draft' ? '_DRAFT' : '');
const mp4 = path.join(outDir, `${name}.mp4`);
const webm = path.join(outDir, `${name}_ALPHA.webm`);
const fc = [
  `[0:v]vflip,split=${flag('prores') ? 3 : 2}[a][b]${flag('prores') ? '[c]' : ''}`,
  `color=c=0x00FF00:s=${W}x${H}:r=${FPS}[g]`,
  `[g][a]overlay=format=rgb:shortest=1,scale=out_color_matrix=bt709:out_range=tv,format=yuv420p[green]`,
  `[b]format=yuva420p[alpha]`,
].join(';');
const ff = [
  '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', `${W}x${H}`, '-r', String(FPS), '-i', '-',
  '-filter_complex', fc,
  '-map', '[green]', '-an', '-c:v', 'libx264', '-preset', 'slow', '-crf', quality === 'final' ? '11' : '18',
  '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-r', String(FPS),
  '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv',
  '-movflags', '+faststart', mp4,
  '-map', '[alpha]', '-an', '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p', '-b:v', '0', '-crf', '20', '-row-mt', '1', '-deadline', 'good', '-cpu-used', '3', webm,
];
if (flag('prores')) {
  ff.push('-map', '[c]', '-an', '-c:v', 'prores_ks', '-profile:v', '4444', '-pix_fmt', 'yuva444p10le', '-alpha_bits', '16', path.join(outDir, `${name}_ALPHA.mov`));
}
const enc = spawn('ffmpeg', ff, { stdio: ['pipe', 'inherit', 'inherit'] });
const t0 = Date.now();
for (let i = from; i < to; i++) {
  const buf = await grab(i);
  if (!enc.stdin.write(buf)) await new Promise((r) => enc.stdin.once('drain', r));
  if (i % 30 === 0 || i === to - 1) {
    const el = (Date.now() - t0) / 1000;
    const per = el / (i - from + 1);
    process.stdout.write(`frame ${i + 1}/${to}  ${per.toFixed(2)} s/frame  eta ${Math.round(per * (to - i - 1))}s\n`);
  }
}
enc.stdin.end();
await new Promise((r) => enc.on('close', r));
await browser.close();
server.close();
console.log('wrote', mp4, webm);

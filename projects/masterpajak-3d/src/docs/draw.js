// Canvas drawing helpers shared by every document design.
import { BRAND, FONTS } from '../tokens.js';

export async function loadFonts(base = '/assets/fonts/') {
  const faces = [
    ['Rubik', 'rubik-latin-400-normal.woff2', '400'],
    ['Rubik', 'rubik-latin-500-normal.woff2', '500'],
    ['Rubik', 'rubik-latin-600-normal.woff2', '600'],
    ['Rubik', 'rubik-latin-700-normal.woff2', '700'],
    ['Rubik', 'rubik-latin-800-normal.woff2', '800'],
    ['JetBrains Mono', 'JetBrainsMono-Regular.ttf', '400'],
    ['JetBrains Mono', 'JetBrainsMono-Medium.ttf', '500'],
    ['JetBrains Mono', 'JetBrainsMono-Bold.ttf', '700'],
  ];
  await Promise.all(faces.map(async ([fam, file, weight]) => {
    const f = new FontFace(fam, `url(${base}${file})`, { weight });
    await f.load();
    document.fonts.add(f);
  }));
  await document.fonts.ready;
}

export function makeCanvas(w, h) {
  const c = document.createElement('canvas');
  c.width = w; c.height = h;
  return c;
}

// Document context: layout in "base" units, rendered at `scale`.
// Region rects are returned in UV space (v=0 at bottom) for the shader.
export class Doc {
  constructor(baseW, baseH, scale = 1, bg = BRAND.paper) {
    this.W = baseW; this.H = baseH; this.s = scale;
    this.canvas = makeCanvas(Math.round(baseW * scale), Math.round(baseH * scale));
    const g = this.canvas.getContext('2d');
    g.scale(scale, scale);
    g.fillStyle = bg;
    g.fillRect(0, 0, baseW, baseH);
    g.textBaseline = 'alphabetic';
    this.g = g;
    this.regions = {};
  }
  font(size, weight = 400, fam = FONTS.display) {
    this.g.font = `${weight} ${size}px "${fam}"`;
    return this;
  }
  text(str, x, y, { size = 28, weight = 400, fam = FONTS.display, color = BRAND.navyInk, align = 'left', spacing = 0 } = {}) {
    const g = this.g;
    this.font(size, weight, fam);
    g.fillStyle = color;
    g.textAlign = align;
    g.letterSpacing = `${spacing}px`;
    g.fillText(str, x, y);
    g.letterSpacing = '0px';
    return g.measureText(str).width;
  }
  measure(str, size, weight = 400, fam = FONTS.display, spacing = 0) {
    this.font(size, weight, fam);
    this.g.letterSpacing = `${spacing}px`;
    const w = this.g.measureText(str).width;
    this.g.letterSpacing = '0px';
    return w;
  }
  rect(x, y, w, h, color) { this.g.fillStyle = color; this.g.fillRect(x, y, w, h); }
  rrect(x, y, w, h, r, fill, stroke = null, lw = 2) {
    const g = this.g;
    g.beginPath();
    g.roundRect(x, y, w, h, r);
    if (fill) { g.fillStyle = fill; g.fill(); }
    if (stroke) { g.strokeStyle = stroke; g.lineWidth = lw; g.stroke(); }
  }
  hline(x1, x2, y, color = BRAND.line, lw = 2, dash = null) {
    const g = this.g;
    g.save();
    g.strokeStyle = color; g.lineWidth = lw;
    if (dash) g.setLineDash(dash);
    g.beginPath(); g.moveTo(x1, y); g.lineTo(x2, y); g.stroke();
    g.restore();
  }
  // register a region in base px (top-left origin) -> UV (bottom-left origin)
  region(name, x, y, w, h) {
    this.regions[name] = [x / this.W, 1 - (y + h) / this.H, (x + w) / this.W, 1 - y / this.H];
    return this.regions[name];
  }
  // MasterPajak "M" mark (vector redraw from screenshot). left = navy|white, right = yellow
  mark(x, y, size, leftColor = BRAND.navy, rightColor = BRAND.yellow) {
    const g = this.g;
    const k = size / 100;
    g.save();
    g.translate(x, y);
    g.scale(k, k);
    g.lineCap = 'round'; g.lineJoin = 'round'; g.lineWidth = 17;
    g.strokeStyle = leftColor;
    g.beginPath(); g.moveTo(14, 86); g.lineTo(14, 14); g.lineTo(50, 57); g.stroke();
    g.strokeStyle = rightColor;
    g.beginPath(); g.moveTo(50, 57); g.lineTo(86, 14); g.lineTo(86, 86); g.stroke();
    g.restore();
  }
  wordmark(x, y, size, color = BRAND.navy, leftMark = BRAND.navy) {
    this.mark(x, y - size * 0.86, size * 1.02, leftMark, BRAND.yellow);
    return this.text('MasterPajak AI', x + size * 1.32, y, { size, weight: 600, color });
  }
  check(x, y, size, color = BRAND.navy) {
    const g = this.g;
    g.save();
    g.strokeStyle = color; g.lineWidth = size * 0.16; g.lineCap = 'round'; g.lineJoin = 'round';
    g.beginPath();
    g.moveTo(x, y + size * 0.5); g.lineTo(x + size * 0.36, y + size * 0.84); g.lineTo(x + size, y + size * 0.12);
    g.stroke();
    g.restore();
  }
}

// deterministic PRNG
export function rng(seed = 1) {
  let s = seed >>> 0;
  return () => {
    s = (s + 0x6D2B79F5) >>> 0;
    let t = s;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export const rupiah = (n) => n.toLocaleString('id-ID');

// paper fibre bump map (tileable-ish noise), grayscale
export function paperBump(size = 512, seed = 7) {
  const c = makeCanvas(size, size);
  const g = c.getContext('2d');
  const img = g.createImageData(size, size);
  const r = rng(seed);
  // value noise at two octaves + fibres
  const grid = (n) => {
    const a = new Float32Array((n + 1) * (n + 1));
    for (let i = 0; i < a.length; i++) a[i] = r();
    for (let i = 0; i <= n; i++) { a[i * (n + 1) + n] = a[i * (n + 1)]; a[n * (n + 1) + i] = a[i]; }
    return (x, y) => {
      const fx = (x / size) * n, fy = (y / size) * n;
      const ix = Math.floor(fx), iy = Math.floor(fy);
      const tx = fx - ix, ty = fy - iy;
      const sx = tx * tx * (3 - 2 * tx), sy = ty * ty * (3 - 2 * ty);
      const v00 = a[iy * (n + 1) + ix], v10 = a[iy * (n + 1) + ix + 1];
      const v01 = a[(iy + 1) * (n + 1) + ix], v11 = a[(iy + 1) * (n + 1) + ix + 1];
      return (v00 * (1 - sx) + v10 * sx) * (1 - sy) + (v01 * (1 - sx) + v11 * sx) * sy;
    };
  };
  const n1 = grid(64), n2 = grid(160);
  for (let y = 0; y < size; y++) {
    for (let x = 0; x < size; x++) {
      const v = 0.5 + 0.28 * (n1(x, y) - 0.5) + 0.22 * (n2(x, y) - 0.5) + 0.12 * (r() - 0.5);
      const k = (y * size + x) * 4;
      const b = Math.max(0, Math.min(255, v * 255));
      img.data[k] = img.data[k + 1] = img.data[k + 2] = b;
      img.data[k + 3] = 255;
    }
  }
  g.putImageData(img, 0, 0);
  // faint fibres
  g.globalAlpha = 0.08;
  g.strokeStyle = '#000';
  for (let i = 0; i < 260; i++) {
    const x = r() * size, y = r() * size, a = r() * Math.PI, l = 6 + r() * 22;
    g.lineWidth = 0.6 + r();
    g.beginPath(); g.moveTo(x, y); g.lineTo(x + Math.cos(a) * l, y + Math.sin(a) * l); g.stroke();
  }
  return c;
}

// back side: plain stock with faint mirrored print-through of the front
export function backWithGhost(frontCanvas, color, ghost = 0.035) {
  const c = makeCanvas(frontCanvas.width, frontCanvas.height);
  const g = c.getContext('2d');
  g.fillStyle = color;
  g.fillRect(0, 0, c.width, c.height);
  g.save();
  g.globalAlpha = ghost;
  g.translate(c.width, 0);
  g.scale(-1, 1);
  g.filter = 'blur(2px) grayscale(1)';
  g.drawImage(frontCanvas, 0, 0);
  g.restore();
  return c;
}

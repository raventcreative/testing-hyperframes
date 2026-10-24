// v4 face clean-up for the rigged mascot copy (non-destructive: writes a new GLB).
//   node facepatch.mjs mask  <rigged.glb> <out_mask.raw>        -> UV mask (2048x2048 u8) of the baked mouth area
//   node facepatch.mjs apply <rigged.glb> <texdir with basecolor.png normal.png rm.png> <out.glb>
// apply: swaps in the cleaned base-colour texture (hair spots + baked mouth painted out, see
// tools/face_texture_clean.py), fills the sculpted mouth cavity with a smooth membrane
// (Laplacian, boundary fixed) and re-smooths its normals, so the procedural mouth sits on clean skin.
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import sharp from 'sharp';
import fs from 'fs';

const [mode, src, a3, a4] = process.argv.slice(2);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS);
const doc = await io.read(src);
const root = doc.getRoot();
const prim = root.listMeshes()[0].listPrimitives()[0];
const Pa = prim.getAttribute('POSITION'), P = Pa.getArray();
const UV = prim.getAttribute('TEXCOORD_0').getArray();
const IDX = prim.getIndices().getArray();
const N = P.length / 3;
const MC = [0.001, 0.521];
// mouth region (lips + cavity), object space
const inMouth = (v, pad = 0) => {
  const x = P[3 * v], y = P[3 * v + 1], z = P[3 * v + 2];
  return Math.abs(x - MC[0]) < 0.047 + pad && y > 0.487 - pad && y < 0.556 + pad && z > 0.06;
};

if (mode === 'mask') {
  const S = 2048, M = new Uint8Array(S * S);
  const tri = (a, b, c) => {
    const pts = [a, b, c].map((v) => [UV[2 * v] * S, UV[2 * v + 1] * S]);
    const minx = Math.max(0, Math.floor(Math.min(...pts.map((p) => p[0])))), maxx = Math.min(S - 1, Math.ceil(Math.max(...pts.map((p) => p[0]))));
    const miny = Math.max(0, Math.floor(Math.min(...pts.map((p) => p[1])))), maxy = Math.min(S - 1, Math.ceil(Math.max(...pts.map((p) => p[1]))));
    const [p0, p1, p2] = pts;
    const area = (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1]);
    if (Math.abs(area) < 1e-9) return;
    for (let y = miny; y <= maxy; y++) for (let x = minx; x <= maxx; x++) {
      const px = x + 0.5, py = y + 0.5;
      const w0 = ((p1[0] - px) * (p2[1] - py) - (p2[0] - px) * (p1[1] - py)) / area;
      const w1 = ((p2[0] - px) * (p0[1] - py) - (p0[0] - px) * (p2[1] - py)) / area;
      const w2 = 1 - w0 - w1;
      if (w0 >= -0.02 && w1 >= -0.02 && w2 >= -0.02) M[y * S + x] = 255;
    }
  };
  let n = 0;
  for (let i = 0; i < IDX.length; i += 3) {
    const a = IDX[i], b = IDX[i + 1], c = IDX[i + 2];
    if (inMouth(a, 0.002) + inMouth(b, 0.002) + inMouth(c, 0.002) >= 1) { tri(a, b, c); n++; }
  }
  fs.writeFileSync(a3, M);
  console.log('mouth triangles', n);
} else if (mode === 'apply') {
  // 1) texture
  for (const [re, f, q] of [[/basecolor/i, 'basecolor.png', 92], [/normal/i, 'normal.png', 95], [/_rm/i, 'rm.png', 95]]) {
    const t = root.listTextures().find((x) => re.test(x.getName() || ''));
    if (!t || !fs.existsSync(`${a3}/${f}`)) continue;
    const webp = await sharp(`${a3}/${f}`).webp({ quality: q }).toBuffer();
    t.setImage(new Uint8Array(webp)).setMimeType('image/webp');
    console.log('texture', f, webp.length);
  }
  // 2) adjacency
  const nb = Array.from({ length: N }, () => new Set());
  for (let i = 0; i < IDX.length; i += 3) {
    const t = [IDX[i], IDX[i + 1], IDX[i + 2]];
    for (const u of t) for (const w of t) if (u !== w) nb[u].add(w);
  }
  // free = cavity + inner lips (well inside the region); boundary ring stays fixed
  const free = [];
  for (let v = 0; v < N; v++) if (inMouth(v, -0.004)) free.push(v);
  const isFree = new Uint8Array(N); for (const v of free) isFree[v] = 1;
  const Q = Float64Array.from(P);
  // fit z = f(x, y) (quadratic) to the fixed skin ring around the mouth, then drop every free vertex
  // onto it: the cavity becomes a smooth skin surface with no flipped / missing triangles
  const ringV = new Set();
  for (const v of free) for (const w of nb[v]) if (!isFree[w] && P[3 * w + 2] > 0.06) ringV.add(w);
  for (let v = 0; v < N; v++) if (!isFree[v] && inMouth(v, 0.012) && !inMouth(v, -0.004) && P[3 * v + 2] > 0.09) ringV.add(v);
  const rows = [];
  for (const w of ringV) { const x = P[3 * w] - MC[0], y = P[3 * w + 1] - MC[1]; rows.push([[1, x, y, x * x, x * y, y * y], P[3 * w + 2]]); }
  const K = 6, AtA = Array.from({ length: K }, () => new Float64Array(K)), Atb = new Float64Array(K);
  for (const [r, z] of rows) for (let i = 0; i < K; i++) { Atb[i] += r[i] * z; for (let j = 0; j < K; j++) AtA[i][j] += r[i] * r[j]; }
  for (let i = 0; i < K; i++) AtA[i][i] += 1e-9;
  // gaussian elimination
  const M = AtA.map((r, i) => [...r, Atb[i]]);
  for (let c = 0; c < K; c++) {
    let pr = c; for (let r = c + 1; r < K; r++) if (Math.abs(M[r][c]) > Math.abs(M[pr][c])) pr = r;
    [M[c], M[pr]] = [M[pr], M[c]];
    for (let r = 0; r < K; r++) if (r !== c) { const f = M[r][c] / M[c][c]; for (let k = c; k <= K; k++) M[r][k] -= f * M[c][k]; }
  }
  const coef = M.map((r, i) => r[K] / r[i]);
  const f = (x, y) => { x -= MC[0]; y -= MC[1]; return coef[0] + coef[1] * x + coef[2] * y + coef[3] * x * x + coef[4] * x * y + coef[5] * y * y; };
  let maxRes = 0; for (const [r, z] of rows) maxRes = Math.max(maxRes, Math.abs(z - (coef[0] + coef[1] * r[1] + coef[2] * r[2] + coef[3] * r[3] + coef[4] * r[4] + coef[5] * r[5])));
  console.log('ring verts', ringV.size, 'fit max residual', maxRes.toFixed(5));
  for (const v of free) Q[3 * v + 2] = f(Q[3 * v], Q[3 * v + 1]) - 0.0003;
  const out = new Float32Array(Q);
  Pa.setArray(out);
  // 3) normals from the fitted surface (smooth skin shading across the patch)
  const Na = prim.getAttribute('NORMAL');
  if (Na) {
    const Nn = Na.getArray().slice();
    for (const v of free) {
      const x = Q[3 * v] - MC[0], y = Q[3 * v + 1] - MC[1];
      const dzdx = coef[1] + 2 * coef[3] * x + coef[4] * y, dzdy = coef[2] + coef[4] * x + 2 * coef[5] * y;
      const l = Math.hypot(dzdx, dzdy, 1); Nn[3 * v] = -dzdx / l; Nn[3 * v + 1] = -dzdy / l; Nn[3 * v + 2] = 1 / l;
    }
    Na.setArray(Nn);
  }
  // 4) the mouth area no longer needs the tangent-space normal map detail: handled in the texture step
  await io.write(a4, doc);
  console.log('patched', free.length, 'mouth verts ->', a4);
}

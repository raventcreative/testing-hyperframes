// LEGO: the robot rebuilt as a tidy brick sculpture. Each bone group (body / head / hands) is voxelised in its own build
// frame (the head straightened by HEAD_FIX so its rows line up with the body when it looks ahead, the mitts tilted so their
// white cap is the top layers) on a stud x plate grid, from a smooth implicit (moving-least-squares signed distance over the
// scan's surface samples, closed by an exterior flood fill), mirrored about the head / body centre lines. Cells are then
// laid as real parts: rows of three equal plates become bricks (2x4 .. 1x1, alternating direction per row = running bond),
// steps are plates; only exposed faces are emitted (world-unit bevels + seam grooves in the shader), studs are instanced.
// Colours: robot surface classes -> toy palette (white, black, trans-light-blue light bricks that glow). The visor is a
// smooth trans-black windscreen set behind a stepped white brick frame, with the printed glowing screen eyes; the wordmark
// is a printed 1x8 brick on a flat chest panel; the light ring is a row of trans-blue bricks under the cape.
// The set is brick-built too (seams + studs) on a studded baseplate (its studs ray-cast in the floor shader); glossy ABS
// under soft studio light; post: macro DOF, glow on the light bricks / eyes, FXAA (MSAA costs ~0.35 s/frame in SwiftShader).
import * as THREE from 'three';
import { makeRT, Pass, Blur, lc, FACE, hash1 } from '../common.js';
import { PAL, NPAL, LAYOUT } from '../set.js';
import { litSetMaterial, makeEnv } from '../lit.js';

const S = 0.036, PH = S * 0.4, HH = PH * 3;          // stud pitch, plate height, brick height (8 / 3.2 / 9.6 mm)
const STUD_R = S * 0.3, STUD_H = S * 0.2;
const HEAD_FIX = [-0.0775, -0.227, -0.1287];         // head bone rotation that makes the visor face +z (stage default)
// toy palette (sRGB): white, black, trans-light-blue (lit), dark bluish grey
const C_WHITE = 0, C_BLACK = 1, C_BLUE = 2, C_GREY = 3;
const BRICK = [0xe9eae7, 0x1d242c, 0x5fd0ff, 0x6c6e68];
// visor opening (straightened head frame): ellipse centre / radii; the glass reaches a bit further, under the frame
const VIS = { cx: 0.05, cy: 0.664, rx: 0.262, ry: 0.162 };

// ------------------------------------------------------------------ surface samples of the scan (rest pose)
function robotSamples(geo) {
  const A = geo.attributes, idx = geo.index.array, n = A.position.count, nt = idx.length / 3, m = n + nt;
  const P = new Float32Array(m * 3), N = new Float32Array(m * 3), K = new Float32Array(m * 3), G = new Uint8Array(m);
  const SN = A.aSmoothN || A.normal;
  for (let i = 0; i < n; i++) {
    P[3 * i] = A.position.getX(i); P[3 * i + 1] = A.position.getY(i); P[3 * i + 2] = A.position.getZ(i);
    N[3 * i] = SN.getX(i); N[3 * i + 1] = SN.getY(i); N[3 * i + 2] = SN.getZ(i);
    K[3 * i] = A.aCls.getX(i); K[3 * i + 1] = A.aCls.getY(i); K[3 * i + 2] = A._face.getZ(i);
    G[i] = A.skinWeight.getY(i) > A.skinWeight.getX(i) ? A.skinIndex.getY(i) : A.skinIndex.getX(i);
  }
  for (let t = 0; t < nt; t++) {
    const a = idx[3 * t], b = idx[3 * t + 1], c = idx[3 * t + 2], o = 3 * (n + t);
    let l = 0;
    for (let k = 0; k < 3; k++) {
      P[o + k] = (P[3 * a + k] + P[3 * b + k] + P[3 * c + k]) / 3;
      N[o + k] = N[3 * a + k] + N[3 * b + k] + N[3 * c + k]; l += N[o + k] * N[o + k];
      K[o + k] = (K[3 * a + k] + K[3 * b + k] + K[3 * c + k]) / 3;
    }
    l = Math.sqrt(l) || 1; N[o] /= l; N[o + 1] /= l; N[o + 2] /= l;
    G[n + t] = G[b] === G[c] ? G[b] : G[a];
  }
  return { P, N, K, G, m };
}

// rigid transform about a pivot (Matrix4)
const about = (pivot, rot) => new THREE.Matrix4().makeTranslation(pivot.x, pivot.y, pivot.z).multiply(rot).multiply(new THREE.Matrix4().makeTranslation(-pivot.x, -pivot.y, -pivot.z));

// ------------------------------------------------------------------ voxel build of one group
// frame F (bind -> build frame), members: groups whose surface closes the solid, sym: mirror x about xc, y0: row origin
function voxelGroup(smp, g, F, { members, xc = null, y0 = 0, bias = 0.3 * S }) {
  const { P, N, K, G, m } = smp;
  const e = F.elements, nm = new THREE.Matrix3().setFromMatrix4(F).elements;
  // samples of the member groups in the build frame
  const ids = []; for (let i = 0; i < m; i++) if (members.includes(G[i])) ids.push(i);
  const ns = ids.length, Q = new Float32Array(ns * 3), QN = new Float32Array(ns * 3), QK = new Float32Array(ns * 3), QG = new Uint8Array(ns);
  const mn = [1e9, 1e9, 1e9], mx = [-1e9, -1e9, -1e9];
  for (let j = 0; j < ns; j++) {
    const i = ids[j], x = P[3 * i], y = P[3 * i + 1], z = P[3 * i + 2], a = N[3 * i], b = N[3 * i + 1], c = N[3 * i + 2];
    const X = e[0] * x + e[4] * y + e[8] * z + e[12], Y = e[1] * x + e[5] * y + e[9] * z + e[13], Z = e[2] * x + e[6] * y + e[10] * z + e[14];
    Q[3 * j] = X; Q[3 * j + 1] = Y; Q[3 * j + 2] = Z;
    QN[3 * j] = nm[0] * a + nm[3] * b + nm[6] * c; QN[3 * j + 1] = nm[1] * a + nm[4] * b + nm[7] * c; QN[3 * j + 2] = nm[2] * a + nm[5] * b + nm[8] * c;
    QK[3 * j] = K[3 * i]; QK[3 * j + 1] = K[3 * i + 1]; QK[3 * j + 2] = K[3 * i + 2]; QG[j] = G[i];
    if (G[i] === g) { mn[0] = Math.min(mn[0], X); mn[1] = Math.min(mn[1], Y); mn[2] = Math.min(mn[2], Z); mx[0] = Math.max(mx[0], X); mx[1] = Math.max(mx[1], Y); mx[2] = Math.max(mx[2], Z); }
  }
  // grid (cells S x PH x S); x symmetric about xc when given; y rows aligned to y0 (multiples of 3 plates)
  let X0, NX;
  if (xc != null) { const k = Math.ceil(Math.max(xc - mn[0], mx[0] - xc) / S) + 2; X0 = xc - k * S; NX = 2 * k; }
  else { X0 = (Math.floor(mn[0] / S) - 2) * S; NX = Math.ceil(mx[0] / S) + 2 - Math.floor(mn[0] / S) + 2; }
  const l0 = Math.floor((mn[1] - y0) / HH) * 3 - 3, Y0 = y0 + l0 * PH, NY = Math.ceil((mx[1] - Y0) / HH) * 3 + 6;
  const Z0 = (Math.floor(mn[2] / S) - 2) * S, NZ = Math.ceil(mx[2] / S) + 2 - Math.floor(mn[2] / S) + 2;
  const NC = NX * NY * NZ, cid = (x, y, z) => (y * NZ + z) * NX + x;
  // sample hash (bucket 0.03)
  const R = 0.03, R2 = R * R, sig2 = 0.011 * 0.011, HB = 0.03;
  const bx0 = X0 - R, by0 = Y0 - R, bz0 = Z0 - R;
  const BX = Math.ceil((NX * S + 2 * R) / HB) + 1, BY = Math.ceil((NY * PH + 2 * R) / HB) + 1, BZ = Math.ceil((NZ * S + 2 * R) / HB) + 1;
  const bstart = new Int32Array(BX * BY * BZ + 1), bkey = new Int32Array(ns);
  for (let j = 0; j < ns; j++) {
    const ix = Math.floor((Q[3 * j] - bx0) / HB), iy = Math.floor((Q[3 * j + 1] - by0) / HB), iz = Math.floor((Q[3 * j + 2] - bz0) / HB);
    bkey[j] = ix < 0 || iy < 0 || iz < 0 || ix >= BX || iy >= BY || iz >= BZ ? -1 : (iy * BZ + iz) * BX + ix;
    if (bkey[j] >= 0) bstart[bkey[j] + 1]++;
  }
  for (let b = 0; b < BX * BY * BZ; b++) bstart[b + 1] += bstart[b];
  const fill = bstart.slice(0, BX * BY * BZ), bl = new Int32Array(bstart[BX * BY * BZ]);
  for (let j = 0; j < ns; j++) if (bkey[j] >= 0) bl[fill[bkey[j]]++] = j;
  // per cell: MLS signed distance, nearest sample, class votes (white, dark, blue, visor) of this group
  const D = new Float32Array(NC), near = new Uint8Array(NC), lab = new Int8Array(NC).fill(-1), nn = new Int32Array(NC).fill(-1);
  const V = new Float32Array(NC * 4);
  for (let y = 0; y < NY; y++) for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++) {
    const c = cid(x, y, z), px = X0 + (x + 0.5) * S, py = Y0 + (y + 0.5) * PH, pz = Z0 + (z + 0.5) * S;
    const ix = Math.floor((px - bx0) / HB), iy = Math.floor((py - by0) / HB), iz = Math.floor((pz - bz0) / HB);
    let sw = 0, sd = 0, best = R2, bj = -1;
    for (let dy = -1; dy <= 1; dy++) for (let dz = -1; dz <= 1; dz++) for (let dx = -1; dx <= 1; dx++) {
      const X = ix + dx, Y = iy + dy, Z = iz + dz; if (X < 0 || Y < 0 || Z < 0 || X >= BX || Y >= BY || Z >= BZ) continue;
      const b = (Y * BZ + Z) * BX + X;
      for (let h = bstart[b]; h < bstart[b + 1]; h++) {
        const j = bl[h], ex = px - Q[3 * j], ey = py - Q[3 * j + 1], ez = pz - Q[3 * j + 2], d2 = ex * ex + ey * ey + ez * ez;
        if (d2 >= R2) continue;
        const w = Math.exp(-d2 / sig2);
        sw += w; sd += w * (ex * QN[3 * j] + ey * QN[3 * j + 1] + ez * QN[3 * j + 2]);
        if (d2 < best) { best = d2; bj = j; }
        if (QG[j] === g) {
          const o = 4 * c, kw = QK[3 * j], kb = QK[3 * j + 1], kf = QK[3 * j + 2];
          if (kf > 0.3) V[o + 3] += w; else if (kb > 0.42) V[o + 2] += w; else if (kw > 0.5) V[o] += w; else V[o + 1] += w;
        }
      }
    }
    if (bj >= 0) { near[c] = 1; nn[c] = bj; lab[c] = QG[bj]; D[c] = sw > 1e-6 ? sd / sw : Math.sqrt(best); }
  }
  // exterior flood fill through cells away from the surface; interior far cells take the label of the closest near cell
  const ext = new Uint8Array(NC), q = new Int32Array(NC); let qh = 0, qt = 0;
  for (let y = 0; y < NY; y++) for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++)
    if ((x === 0 || y === 0 || z === 0 || x === NX - 1 || y === NY - 1 || z === NZ - 1)) { const c = cid(x, y, z); if (!near[c]) { ext[c] = 1; q[qt++] = c; } }
  const step = [1, -1, NX, -NX, NX * NZ, -NX * NZ];
  const inb = (c, k) => { const x = c % NX, z = Math.floor(c / NX) % NZ, y = Math.floor(c / (NX * NZ));
    return k === 0 ? x < NX - 1 : k === 1 ? x > 0 : k === 2 ? z < NZ - 1 : k === 3 ? z > 0 : k === 4 ? y < NY - 1 : y > 0; };
  while (qh < qt) { const c = q[qh++]; for (let k = 0; k < 6; k++) { if (!inb(c, k)) continue; const d = c + step[k]; if (ext[d] || near[d]) continue; ext[d] = 1; q[qt++] = d; } }
  qh = qt = 0; for (let c = 0; c < NC; c++) if (near[c]) q[qt++] = c;
  while (qh < qt) { const c = q[qh++]; for (let k = 0; k < 6; k++) { if (!inb(c, k)) continue; const d = c + step[k]; if (ext[d] || lab[d] >= 0) continue; lab[d] = lab[c]; q[qt++] = d; } }
  // inside-ness of this group (positive inside), mirrored about xc
  const v = new Float32Array(NC);
  for (let c = 0; c < NC; c++) v[c] = lab[c] !== g ? -0.05 : near[c] ? -D[c] : ext[c] ? -0.05 : 0.05;
  const mir = (c) => { const x = c % NX; return c - x + (NX - 1 - x); };
  if (xc != null) {
    const v2 = v.slice(); for (let c = 0; c < NC; c++) v[c] = 0.5 * (v2[c] + v2[mir(c)]);
    const V2 = V.slice(); for (let c = 0; c < NC; c++) { const d = mir(c); for (let k = 0; k < 4; k++) V[4 * c + k] = V2[4 * c + k] + V2[4 * d + k]; }
  }
  const occ = new Uint8Array(NC); for (let c = 0; c < NC; c++) occ[c] = v[c] > -bias ? 1 : 0;
  return { g, F, X0, Y0, Z0, NX, NY, NZ, NC, cid, mir, occ, v, D, V, near, nn, QN, Q, lab, l0, step, inb, sym: xc != null };
}

// colours from votes; isolated-cell cleanup; exposed-surface majority smoothing
function colourGroup(B) {
  const { NC, occ, V, NX, NY, NZ, cid } = B;
  const col = new Int8Array(NC).fill(-1);
  for (let c = 0; c < NC; c++) {
    if (!occ[c]) continue;
    const w = V[4 * c], d = V[4 * c + 1], b = V[4 * c + 2], vz = V[4 * c + 3], t = w + d + b + vz;
    // (visor votes left after the opening is cut are the frame round the glass: white)
    col[c] = t < 1e-3 ? (B.g < 2 ? C_WHITE : C_BLACK) : b > 0.3 * t ? C_BLUE : w + vz >= d ? C_WHITE : C_BLACK;
  }
  B.col = col;
}
function exposedMask(B) {
  const { NC, occ, step, inb } = B, ex = new Uint8Array(NC);
  for (let c = 0; c < NC; c++) if (occ[c]) for (let k = 0; k < 6; k++) if (!inb(c, k) || !occ[c + step[k]]) { ex[c] = 1; break; }
  return ex;
}
function cleanup(B, passes = 2) {
  const { NC, occ, step, inb, col } = B;
  for (let p = 0; p < passes; p++) {
    const rem = [], add = [];
    for (let c = 0; c < NC; c++) {
      let n = 0; const cc = [0, 0, 0, 0];
      for (let k = 0; k < 6; k++) if (inb(c, k) && occ[c + step[k]]) { n++; cc[col[c + step[k]]]++; }
      if (occ[c] && n <= 1) rem.push(c);
      else if (!occ[c] && n >= 5) add.push([c, cc.indexOf(Math.max(...cc))]);
    }
    for (const c of rem) { occ[c] = 0; col[c] = -1; }
    for (const [c, k] of add) { occ[c] = 1; col[c] = k; }
  }
}
// majority filter of surface colours over the 3x3x3 neighbourhood (exposed cells only); blue is kept as drawn
function smoothColours(B, iters = 2) {
  const { NX, NY, NZ, cid, col } = B;
  for (let it = 0; it < iters; it++) {
    const ex = exposedMask(B), out = col.slice();
    for (let y = 0; y < NY; y++) for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++) {
      const c = cid(x, y, z); if (!ex[c] || col[c] === C_BLUE) continue;
      const cc = [0, 0, 0, 0]; let tot = 0;
      for (let dy = -1; dy <= 1; dy++) for (let dz = -1; dz <= 1; dz++) for (let dx = -1; dx <= 1; dx++) {
        const X = x + dx, Y = y + dy, Z = z + dz; if (X < 0 || Y < 0 || Z < 0 || X >= NX || Y >= NY || Z >= NZ) continue;
        const d = cid(X, Y, Z); if (!ex[d]) continue; cc[col[d]]++; tot++;
      }
      if (cc[col[c]] * 3 < tot) { let bk = col[c], bv = -1; for (let k = 0; k < 4; k++) if (k !== C_BLUE && cc[k] > bv) { bv = cc[k]; bk = k; } out[c] = bk; }
    }
    col.set(out);
  }
}

// mitts: the white cap is the top plate layers of the (cap-up) build frame: best split of the votes, raised by `grow` plates
function capSplit(Bh, grow) {
  const { NX, NY, NZ, cid, occ, V, col } = Bh;
  const wl = new Float32Array(NY), dl = new Float32Array(NY);
  for (let y = 0; y < NY; y++) for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++) { const c = cid(x, y, z); if (!occ[c]) continue; wl[y] += V[4 * c]; dl[y] += V[4 * c + 1] + V[4 * c + 2]; }
  let best = 1e9, ly = 0;
  for (let s = 0; s <= NY; s++) { let e = 0; for (let y = 0; y < NY; y++) e += y >= s ? dl[y] : wl[y]; if (e < best) { best = e; ly = s; } }
  // grow the cap until it covers ~42% of the mitt's exposed votes (the scan's cap is thin at brick scale)
  const tot = wl.reduce((a, b) => a + b, 0) + dl.reduce((a, b) => a + b, 0);
  let acc = 0; for (let y = NY - 1; y >= ly; y--) acc += wl[y] + dl[y];
  while (ly > 0 && acc < 0.42 * tot) { ly--; acc += wl[ly] + dl[ly]; }
  ly -= grow;
  for (let y = 0; y < NY; y++) for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++) { const c = cid(x, y, z); if (occ[c]) col[c] = y >= ly ? C_WHITE : C_BLACK; }
  Bh.capLayer = ly;
}

// builder's palette: the helmet is all white shell (+ its blue ear lights), the cape white, a trans-blue ring under it,
// a black pod below (with its trans-blue base light). Only the lights come from the scan's classes.
function designColours(Bb, Bh) {
  { const { NC, occ, col } = Bh; for (let c = 0; c < NC; c++) if (occ[c] && col[c] !== C_BLUE) col[c] = C_WHITE; }
  const { NX, NY, NZ, cid, occ, col, Y0 } = Bb;
  let r0 = 1e9, r1 = -1e9;
  for (let y = 0; y < NY; y++) for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++) {
    const c = cid(x, y, z), py = Y0 + (y + 0.5) * PH; if (occ[c] && col[c] === C_BLUE && py > 0.1 && py < 0.32) { r0 = Math.min(r0, py); r1 = Math.max(r1, py); }
  }
  if (r0 > r1) { r0 = 0.2; r1 = 0.24; }
  for (let y = 0; y < NY; y++) for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++) {
    const c = cid(x, y, z), py = Y0 + (y + 0.5) * PH; if (!occ[c]) continue;
    if (py > r1) col[c] = C_WHITE; else if (py >= r0 && py <= r1) col[c] = col[c] === C_BLUE ? C_BLUE : C_BLACK; else if (col[c] !== C_BLUE || py > 0.06) col[c] = C_BLACK;
  }
  Bb.ring = [r0, r1];
}

// ------------------------------------------------------------------ lay parts: bricks (3 equal plates) + plates
function layParts(B, seed) {
  const { NX, NY, NZ, cid, occ, col, l0 } = B;
  const pid = new Int32Array(B.NC).fill(-1); let np = 0;
  const lens = [[4, 3, 2, 1], [3, 4, 2, 1], [2, 4, 3, 1], [4, 2, 3, 1], [3, 2, 4, 1], [2, 3, 4, 1]];
  const tileLayer = (mask, row, assign) => {
    const alongX = ((row + l0 / 3) & 1) === 0, par = (row + seed) & 1;
    const L1 = alongX ? NZ : NX, L2 = alongX ? NX : NZ;
    const at = (a, b) => (alongX ? b + a * NX : a + b * NX);   // (line a, position b) -> x + z * NX
    const used = new Uint8Array(NX * NZ);
    for (let a = 0; a < L1; a++) for (let b = 0; b < L2; b++) {
      const k0 = at(a, b); if (!mask[k0] || used[k0] || mask[k0] < 0) continue;
      const cl = mask[k0];
      const pref = lens[Math.floor(hash1(seed * 31.7 + row * 7.31 + a * 1.93 + b * 0.37) * lens.length)];
      let placed = false;
      for (const wdt of ((a + par) & 1) === 0 && a + 1 < L1 ? [2, 1] : [1]) {
        for (const len of pref) {
          if (b + len > L2) continue;
          let ok = true;
          for (let i = 0; i < wdt && ok; i++) for (let j = 0; j < len; j++) { const k = at(a + i, b + j); if (mask[k] !== cl || used[k]) { ok = false; break; } }
          if (!ok) continue;
          for (let i = 0; i < wdt; i++) for (let j = 0; j < len; j++) { const k = at(a + i, b + j); used[k] = 1; assign(k, np); }
          np++; placed = true; break;
        }
        if (placed) break;
      }
    }
  };
  const rows = Math.ceil(NY / 3);
  for (let r = 0; r < rows; r++) {
    // bricks: columns where the three plates of this row are occupied with one colour
    const full = new Int8Array(NX * NZ);
    for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++) {
      let ok = 3 * r + 2 < NY; const c0 = cid(x, 3 * r, z);
      for (let i = 0; i < 3 && ok; i++) { const c = cid(x, 3 * r + i, z); if (!occ[c] || col[c] !== col[c0]) ok = false; }
      full[x + z * NX] = ok ? col[c0] + 1 : 0;
    }
    tileLayer(full, r, (k, id) => { const x = k % NX, z = Math.floor(k / NX); for (let i = 0; i < 3; i++) pid[cid(x, 3 * r + i, z)] = id; });
    // plates: the rest of the row, plate by plate
    for (let i = 0; i < 3 && 3 * r + i < NY; i++) {
      const y = 3 * r + i, mask = new Int8Array(NX * NZ);
      for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++) { const c = cid(x, y, z); mask[x + z * NX] = occ[c] && pid[c] < 0 ? col[c] + 1 : 0; }
      tileLayer(mask, r + i, (k, id) => { pid[cid(k % NX, y, Math.floor(k / NX))] = id; });
    }
  }
  B.pid = pid; B.np = np;
}

// exposed faces (+ seam flags, world-unit face coords) and stud positions, in the build frame
function emitGroup(B, cols, { noStud } = {}) {
  const { NX, NY, NZ, X0, Y0, Z0, cid, occ, col, pid } = B;
  const pos = [], nor = [], colr = [], luv = [], sz = [], seam = [], t1 = [], t2 = [], ph = [], studs = [];
  const isOcc = (x, y, z) => x >= 0 && y >= 0 && z >= 0 && x < NX && y < NY && z < NZ && occ[cid(x, y, z)] === 1;
  const same = (k, x, y, z) => x >= 0 && y >= 0 && z >= 0 && x < NX && y < NY && z < NZ && pid[cid(x, y, z)] === pid[k];
  const dirs = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]];
  const tang = (d) => (d[1] !== 0 ? [[1, 0, 0], [0, 0, 1]] : d[0] !== 0 ? [[0, 0, 1], [0, 1, 0]] : [[1, 0, 0], [0, 1, 0]]);
  const half = [S / 2, PH / 2, S / 2];
  const pc = new THREE.Color();
  for (let y = 0; y < NY; y++) for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++) {
    const k = cid(x, y, z); if (!occ[k]) continue;
    // per-part tint: moulded plastic batches differ a hair
    const hv = hash1(pid[k] * 0.618 + B.g * 13.1);
    pc.copy(cols[col[k]]).multiplyScalar(col[k] === C_WHITE ? 0.965 + 0.05 * hv : 0.92 + 0.16 * hv);
    const cx = X0 + (x + 0.5) * S, cy = Y0 + (y + 0.5) * PH, cz = Z0 + (z + 0.5) * S;
    for (const d of dirs) {
      if (isOcc(x + d[0], y + d[1], z + d[2])) continue;
      const [T1, T2] = tang(d);
      const fc = [cx + d[0] * half[0], cy + d[1] * half[1], cz + d[2] * half[2]];
      const e1 = T1.map((v, i) => v * half[i]), e2 = T2.map((v, i) => v * half[i]);
      const s1 = 2 * (e1[0] + e1[1] + e1[2]), s2 = 2 * (e2[0] + e2[1] + e2[2]);
      const sm = [!same(k, x - T1[0], y - T1[1], z - T1[2]), !same(k, x + T1[0], y + T1[1], z + T1[2]), !same(k, x - T2[0], y - T2[1], z - T2[2]), !same(k, x + T2[0], y + T2[1], z + T2[2])].map(Number);
      const corners = [[-1, -1], [1, -1], [1, 1], [-1, 1]];
      const Vv = corners.map(([u, w]) => [fc[0] + e1[0] * u + e2[0] * w, fc[1] + e1[1] * u + e2[1] * w, fc[2] + e1[2] * u + e2[2] * w]);
      const crs = [T1[1] * T2[2] - T1[2] * T2[1], T1[2] * T2[0] - T1[0] * T2[2], T1[0] * T2[1] - T1[1] * T2[0]];
      const order = crs[0] * d[0] + crs[1] * d[1] + crs[2] * d[2] < 0 ? [0, 2, 1, 0, 3, 2] : [0, 1, 2, 0, 2, 3];
      for (const o of order) {
        pos.push(...Vv[o]); nor.push(...d); colr.push(pc.r, pc.g, pc.b);
        luv.push((corners[o][0] + 1) / 2 * s1, (corners[o][1] + 1) / 2 * s2); sz.push(s1, s2); seam.push(...sm); t1.push(...T1); t2.push(...T2); ph.push(hv);
      }
      if (d[1] === 1 && !(noStud && noStud(x, y, z))) studs.push([cx, cy + PH / 2, cz, pc.clone()]);
    }
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); geo.setAttribute('normal', new THREE.Float32BufferAttribute(nor, 3));
  geo.setAttribute('color', new THREE.Float32BufferAttribute(colr, 3)); geo.setAttribute('aLuv', new THREE.Float32BufferAttribute(luv, 2));
  geo.setAttribute('aSz', new THREE.Float32BufferAttribute(sz, 2)); geo.setAttribute('aPh', new THREE.Float32BufferAttribute(ph, 1));
  geo.setAttribute('aSeam', new THREE.Float32BufferAttribute(seam, 4)); geo.setAttribute('aT1', new THREE.Float32BufferAttribute(t1, 3)); geo.setAttribute('aT2', new THREE.Float32BufferAttribute(t2, 3));
  return { geo, studs };
}

// ABS plastic: vertex colours + world-unit bevels / seam grooves (box-filtered), glowing trans-blue light bricks
function brickMaterial() {
  const m = new THREE.MeshPhysicalMaterial({ vertexColors: true, roughness: 0.24, metalness: 0, clearcoat: 0.3, clearcoatRoughness: 0.12 });
  m.onBeforeCompile = (sh) => {
    sh.vertexShader = sh.vertexShader
      .replace('#include <common>', '#include <common>\nattribute vec2 aLuv; attribute vec2 aSz; attribute vec4 aSeam; attribute vec3 aT1; attribute vec3 aT2; attribute float aPh;\nvarying vec2 vLuv; varying vec2 vSz; varying vec4 vSeam; varying vec3 vT1; varying vec3 vT2; varying float vPh;')
      .replace('#include <begin_vertex>', '#include <begin_vertex>\nvLuv = aLuv; vSz = aSz; vSeam = aSeam; vPh = aPh; vT1 = normalize(mat3(modelViewMatrix) * aT1); vT2 = normalize(mat3(modelViewMatrix) * aT2);');
    sh.fragmentShader = sh.fragmentShader
      .replace('#include <common>', `#include <common>
        varying vec2 vLuv; varying vec2 vSz; varying vec4 vSeam; varying vec3 vT1; varying vec3 vT2; varying float vPh;
        // box-filtered coverage of the band [0, w] at distance d (footprint fw)
        float band(float d, float w, float fw) { fw = max(fw, 1e-6); return clamp((min(w, d + 0.5 * fw) - max(0.0, d - 0.5 * fw)) / fw, 0.0, 1.0); }`)
      .replace('#include <normal_fragment_maps>', `#include <normal_fragment_maps>
        vec4 ed = vec4(vLuv.x, vSz.x - vLuv.x, vLuv.y, vSz.y - vLuv.y);
        vec2 fw = fwidth(vLuv);
        const float BW = 0.0026, GW = 0.00045;
        vec4 bev = vSeam * vec4(band(ed.x, BW, fw.x), band(ed.y, BW, fw.x), band(ed.z, BW, fw.y), band(ed.w, BW, fw.y));
        bev *= bev * (3.0 - 2.0 * bev);
        normal = normalize(normal + (vT1 * (bev.y - bev.x) + vT2 * (bev.w - bev.z)) * 0.9 + (vT1 * (fract(vPh * 7.31) - 0.5) + vT2 * (fract(vPh * 13.7) - 0.5)) * 0.03);
        vec4 gr = vSeam * vec4(band(ed.x, GW, fw.x), band(ed.y, GW, fw.x), band(ed.z, GW, fw.y), band(ed.w, GW, fw.y));
        float groove = max(max(gr.x, gr.y), max(gr.z, gr.w));`)
      .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
        float isBlue = step(0.8, vColor.b) * step(vColor.r, 0.4);
        diffuseColor.rgb *= 1.0 - 0.8 * groove;
        totalEmissiveRadiance += vColor.rgb * isBlue * (2.2 - 1.6 * groove);`);
  };
  m.customProgramCacheKey = () => 'sb-lego-brick2';
  return m;
}
function studMaterial() {
  const m = new THREE.MeshPhysicalMaterial({ roughness: 0.24, metalness: 0, clearcoat: 0.3, clearcoatRoughness: 0.12 });
  m.onBeforeCompile = (sh) => {
    sh.fragmentShader = sh.fragmentShader.replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
      #ifdef USE_INSTANCING_COLOR
      float isBlue = step(0.8, vColor.b) * step(vColor.r, 0.4); totalEmissiveRadiance += vColor.rgb * isBlue * 2.2;
      #endif`);
  };
  m.customProgramCacheKey = () => 'sb-lego-stud2';
  return m;
}
function studGeometry(seg) {
  // open cylinder + top cap (no bottom: never seen), bevelled top edge
  const g = new THREE.CylinderGeometry(STUD_R, STUD_R, STUD_H, seg, 2, true); g.translate(0, STUD_H / 2, 0);
  const pos = g.attributes.position;
  for (let i = 0; i < pos.count; i++) if (pos.getY(i) > STUD_H * 0.99) { pos.setX(i, pos.getX(i) * 0.9); pos.setZ(i, pos.getZ(i) * 0.9); }
    else if (pos.getY(i) > STUD_H * 0.4) { pos.setY(i, STUD_H * 0.86); }
  const cap = new THREE.CircleGeometry(STUD_R * 0.9, seg); cap.rotateX(-Math.PI / 2); cap.translate(0, STUD_H, 0);
  const merged = new THREE.BufferGeometry();
  const nr = g.attributes.normal;
  for (let i = 0; i < pos.count; i++) if (pos.getY(i) > STUD_H * 0.99) { const x = nr.getX(i), z = nr.getZ(i); nr.setXYZ(i, x * 0.6, 0.8, z * 0.6); }
  const a = g.toNonIndexed(), b = cap.toNonIndexed();
  const P = new Float32Array([...a.attributes.position.array, ...b.attributes.position.array]);
  const N = new Float32Array([...a.attributes.normal.array, ...b.attributes.normal.array]);
  merged.setAttribute('position', new THREE.BufferAttribute(P, 3)); merged.setAttribute('normal', new THREE.BufferAttribute(N, 3));
  return merged;
}
function makeStuds(list, geo, mat, cols) {
  const m = new THREE.InstancedMesh(geo, mat, Math.max(1, list.length));
  const mt = new THREE.Matrix4(), c = new THREE.Color();
  list.forEach((s, i) => { mt.makeTranslation(s[0], s[1], s[2]); m.setMatrixAt(i, mt); c.copy(typeof s[3] === 'number' ? cols[s[3]] : s[3]); m.setColorAt(i, c); });
  m.count = list.length; m.castShadow = true; m.receiveShadow = true; m.frustumCulled = false;
  m.instanceMatrix.needsUpdate = true; if (m.instanceColor) m.instanceColor.needsUpdate = true;
  return m;
}

// ------------------------------------------------------------------ the robot as a brick build
function buildRobot(rig) {
  const geo = rig.mesh.geometry, smp = robotSamples(geo);
  const inv = rig.mesh.skeleton.boneInverses;
  const pivot = (g) => new THREE.Vector3().setFromMatrixPosition(inv[g].clone().invert());
  const F = [new THREE.Matrix4()];
  F[1] = about(pivot(1), new THREE.Matrix4().makeRotationFromEuler(new THREE.Euler(...HEAD_FIX, 'XYZ')));
  // mitts: tilt so the white cap direction (least-squares gradient of the white class) points up
  for (const h of [2, 3]) {
    const c = [0, 0, 0]; let n = 0, mw = 0;
    for (let i = 0; i < smp.m; i++) if (smp.G[i] === h) { for (let k = 0; k < 3; k++) c[k] += smp.P[3 * i + k]; mw += smp.K[3 * i]; n++; }
    for (let k = 0; k < 3; k++) c[k] /= n; mw /= n;
    const a = new THREE.Vector3();
    for (let i = 0; i < smp.m; i++) if (smp.G[i] === h) { const w = smp.K[3 * i] - mw; a.x += (smp.P[3 * i] - c[0]) * w; a.y += (smp.P[3 * i + 1] - c[1]) * w; a.z += (smp.P[3 * i + 2] - c[2]) * w; }
    a.normalize();
    // builder's licence: tip the cap a little towards the front so the white reads from the stage cameras
    a.add(new THREE.Vector3(0, 0.12, 0.38)).normalize();
    const qr = new THREE.Quaternion().setFromUnitVectors(a, new THREE.Vector3(0, 1, 0));
    F[h] = about(new THREE.Vector3(...c), new THREE.Matrix4().makeRotationFromQuaternion(qr));
    F[h].userData = { centre: c, cap: a.toArray() };
  }
  const B = [];
  B[0] = voxelGroup(smp, 0, F[0], { members: [0, 1], xc: 0.018, y0: 0 });
  B[1] = voxelGroup(smp, 1, F[1], { members: [0, 1], xc: VIS.cx, y0: 0 });
  B[2] = voxelGroup(smp, 2, F[2], { members: [2], xc: null, y0: F[2].userData.centre[1] });
  B[3] = voxelGroup(smp, 3, F[3], { members: [3], xc: null, y0: F[3].userData.centre[1] });
  for (const b of B) colourGroup(b);
  for (const h of [2, 3]) capSplit(B[h], 0);
  return { B, F, smp };
}

// baseplate studs, ray-cast per floor fragment: the view ray between stud height and the floor crosses at most a few
// cells; the first hit with a stud cylinder (side or top) gives the normal. Far cheaper than ~6k instanced cylinders.
const FLOOR_STUDS = /* glsl */ `
const float SR = ${STUD_R.toFixed(5)}, SH = ${STUD_H.toFixed(5)};
float gStud = 0.0, gStudAO = 1.0; vec3 gStudN = vec3(0.0, 1.0, 0.0);
#define FLOOR_STUD_REGION(p) (abs(p.x) < 1.72 && p.z > -1.27 && p.z < 1.12 && !(abs(p.x - ${LAYOUT.desk.x.toFixed(3)}) < ${(LAYOUT.desk.w / 2).toFixed(3)} && abs(p.z - ${LAYOUT.desk.z.toFixed(3)}) < ${(LAYOUT.desk.d / 2).toFixed(3)}) && length(p.xz - vec2(${LAYOUT.plant.x.toFixed(3)}, ${LAYOUT.plant.z.toFixed(3)})) > 0.13)
void floorStuds(vec3 wp) {
  vec3 ro = cameraPosition, rd = wp - ro;
  if (rd.y > -1e-5) return;
  float tT = (SH - ro.y) / rd.y, best = 2.0;
  vec2 a = ro.xz + rd.xz * tT;
  for (int k = 0; k < 4; k++) {
    vec2 c = (floor(mix(a, wp.xz, (float(k) + 0.5) * 0.25) / BS) + 0.5) * BS;
    vec2 o = ro.xz - c;
    float A = dot(rd.xz, rd.xz), Bq = dot(o, rd.xz), Cq = dot(o, o) - SR * SR, disc = Bq * Bq - A * Cq;
    if (disc < 0.0) continue;
    float t1 = (-Bq - sqrt(disc)) / A, y1 = ro.y + rd.y * t1;
    if (y1 > SH) { vec2 pt = a - c; if (dot(pt, pt) < SR * SR && tT < best) { best = tT; gStud = 2.0; gStudN = vec3(0.0, 1.0, 0.0); } }
    else if (y1 >= 0.0 && t1 < best) { best = t1; gStud = 1.0; gStudN = vec3(normalize(o + rd.xz * t1), 0.0).xzy; }
  }
  if (gStud < 0.5) { vec2 c = (floor(wp.xz / BS) + 0.5) * BS; gStudAO = mix(0.82, 1.0, smoothstep(SR, SR * 1.45, length(wp.xz - c))); }
  else if (gStud < 1.5) gStudAO = mix(0.86, 1.0, smoothstep(0.0, SH, ro.y + rd.y * best));
}
`;

// LEGO palette for the set (sRGB)
const SETCOL = {
  floor: 0xa0a5a9, wall: 0xe4cd9e, trim: 0x958a73, deskTop: 0x582a12, deskBody: 0xa0a5a9, monitor: 0x1b2a34, screen: 0x0d69ab,
  bar1: 0x4b9f4a, bar2: 0xf2cd37, bar3: 0xc91a09, bar4: 0x0055bf, board: 0xf4f4f0, boardFrame: 0x0a3463, leaf: 0x4b9f4a, pot: 0xa0522d,
  winFrame: 0xf4f4f0, sky: 0x9fd6f5, city: 0x9fd6f5, clock: 0xf4f4f0, clockHand: 0x1b2a34, keyboard: 0x6c6e68, mug: 0xc91a09, axis: 0x1b2a34, soil: 0x352100,
};

const COMP = /* glsl */ `
uniform sampler2D tC; uniform sampler2D tD; uniform sampler2D tDof; uniform sampler2D tGlow; uniform vec2 uNF; uniform float uFocus; uniform vec2 uRes;
varying vec2 vUv;
float viewZ(float d) { return uNF.x * uNF.y / ((uNF.y - uNF.x) * d - uNF.y); }
vec3 filmic(vec3 x) { return clamp((x * (2.51 * x + 0.03)) / (x * (2.43 * x + 0.59) + 0.14), 0.0, 1.0); }
// FXAA (3.11-style, console quality): luma from tone-compressed HDR, short edge search
float lumaT(vec2 uv) { vec3 c = texture2D(tC, uv).rgb; return sqrt(dot(c / (1.0 + c), vec3(0.299, 0.587, 0.114))); }
vec3 fxaa(vec2 uv) {
  vec2 px = 1.0 / uRes;
  vec3 cM = texture2D(tC, uv).rgb;
  float lM = sqrt(dot(cM / (1.0 + cM), vec3(0.299, 0.587, 0.114)));
  float lNW = lumaT(uv + px * vec2(-0.5, 0.5)), lNE = lumaT(uv + px * vec2(0.5, 0.5)), lSW = lumaT(uv + px * vec2(-0.5, -0.5)), lSE = lumaT(uv + px * vec2(0.5, -0.5));
  float lMin = min(lM, min(min(lNW, lNE), min(lSW, lSE))), lMax = max(lM, max(max(lNW, lNE), max(lSW, lSE)));
  if (lMax - lMin < max(0.04, lMax * 0.12)) return cM;
  vec2 dir = vec2(-((lNW + lNE) - (lSW + lSE)), (lNW + lSW) - (lNE + lSE));
  float dr = max((lNW + lNE + lSW + lSE) * 0.03125, 1.0 / 128.0);
  float rcp = 1.0 / (min(abs(dir.x), abs(dir.y)) + dr);
  dir = clamp(dir * rcp, -4.0, 4.0) * px;
  vec3 a = 0.5 * (texture2D(tC, uv - dir * (1.0 / 6.0)).rgb + texture2D(tC, uv + dir * (1.0 / 6.0)).rgb);
  vec3 b = a * 0.5 + 0.25 * (texture2D(tC, uv - dir * 0.5).rgb + texture2D(tC, uv + dir * 0.5).rgb);
  float lB = sqrt(dot(b / (1.0 + b), vec3(0.299, 0.587, 0.114)));
  return (lB < lMin || lB > lMax) ? a : b;
}
void main() {
  vec3 c = fxaa(vUv);
  float z = -viewZ(texture2D(tD, vUv).r);
  float coc = 0.85 * smoothstep(0.1, 0.8, clamp(abs(1.0 / uFocus - 1.0 / z) * uFocus * 1.5, 0.0, 1.0));
  c = mix(c, texture2D(tDof, vUv).rgb, coc);
  c += texture2D(tGlow, vUv).rgb * 0.9;
  c = filmic(c * 1.05);
  c = pow(c, vec3(1.0 / 2.2));
  vec2 v = vUv - 0.5; c *= 1.0 - 0.35 * dot(v, v);
  c += (h12(vUv * uRes) - 0.5) * 0.01;
  gl_FragColor = vec4(c, 1.0);
}`;

export default function createLego(ctx) {
  const { W, H, renderer, rig } = ctx;
  const scene = new THREE.Scene();
  scene.background = lc(0xe4cd9e);
  scene.environment = makeEnv(renderer, { bg: 0x9aa0a8, bgK: 0.5, panels: [
    { pos: [-2.0, 3.8, 2.6], size: [3.0, 2.2], look: [0, 0.5, 0], color: 0xfff6ec, intensity: 3.2 },
    { pos: [2.8, 2.2, 2.2], size: [1.6, 2.4], look: [0, 0.5, 0], color: 0xeaf2ff, intensity: 1.6 },
    { pos: [0.5, 3.0, -2.5], size: [3.0, 1.0], look: [0, 0.5, 0], color: 0xffffff, intensity: 1.2 },
  ] });
  scene.environmentIntensity = 0.75;
  // ---- robot bricks (build frames, one group per bone)
  const { B, F } = buildRobot(rig);
  const bones = rig.mesh.skeleton.bones, inv = rig.mesh.skeleton.boneInverses;
  const Finv = F.map((m) => m.clone().invert());
  const bmat = brickMaterial(), smat = studMaterial(), studGeo = studGeometry(12), studGeoLo = studGeometry(8);
  const brickCols = BRICK.map((h) => lc(h));
  // head: open the visor (cells in front of the glass) and frame it with white bricks
  const H1 = B[1];
  const inVis = (x, y, k) => { const px = H1.X0 + (x + 0.5) * S, py = H1.Y0 + (y + 0.5) * PH; return ((px - VIS.cx) / (VIS.rx * k)) ** 2 + ((py - VIS.cy) / (VIS.ry * k)) ** 2 < 1; };
  {
    const { NX, NY, NZ, cid, occ, col, D, near, nn, QN, Z0, lab } = H1;
    for (let y = 0; y < NY; y++) for (let x = 0; x < NX; x++) {
      const open = inVis(x, y, 1), ring = !open && inVis(x, y, 1.3);
      if (!open && !ring) continue;
      for (let z = 0; z < NZ; z++) {
        const c = cid(x, y, z), pz = Z0 + (z + 0.5) * S; if (pz < 0.06 || !near[c] || lab[c] !== 1) continue;
        const j = nn[c], sup = Math.abs(QN[3 * j]) * S / 2 + Math.abs(QN[3 * j + 1]) * PH / 2 + Math.abs(QN[3 * j + 2]) * S / 2;
        if (open && D[c] > -(sup + 0.004)) { occ[c] = 0; col[c] = -1; }
        if (ring && D[c] < sup * 0.9) { occ[c] = 1; col[c] = C_WHITE; }
      }
    }
  }
  for (const b of B) cleanup(b, 2);
  designColours(B[0], B[1]);
  for (const b of B) smoothColours(b, 1);
  // body: flat chest panel for the printed 1x8 wordmark brick (3 plates, centred on the collar's logo line)
  const B0 = B[0], LOGO_Y = 0.385;
  const chest = (() => {
    const { NX, NZ, cid, occ, col, Y0, Z0, X0 } = B0;
    const ly = Math.round((LOGO_Y - Y0) / PH - 1.5), xs = NX / 2 - 4;
    let zf = 0;
    for (let i = 0; i < 3; i++) for (let x = xs; x < xs + 8; x++) for (let z = 0; z < NZ; z++) if (occ[cid(x, ly + i, z)]) zf = Math.max(zf, z);
    for (let i = 0; i < 3; i++) for (let x = xs; x < xs + 8; x++) for (let z = zf; z >= 0; z--) { const c = cid(x, ly + i, z); if (occ[c] && z < zf - 1) break; occ[c] = 1; col[c] = C_WHITE; }
    return { ly, xs, zf, x0: X0 + xs * S, y0: Y0 + ly * PH, zFront: Z0 + (zf + 1) * S };
  })();
  for (const b of B) layParts(b, b.g * 3 + 1);
  { const { cid, pid } = B0; const id = B0.np++; for (let i = 0; i < 3; i++) for (let x = chest.xs; x < chest.xs + 8; x++) pid[cid(x, chest.ly + i, chest.zf)] = id; }
  const groups = [];
  for (let g = 0; g < 4; g++) {
    const { geo, studs } = emitGroup(B[g], brickCols, { noStud: g === 1 ? (x, y, z) => (inVis(x, y, 1) || inVis(x, y + 1, 1) || inVis(x, y + 2, 1)) && H1.Z0 + (z + 0.5) * S > 0.06 : null });
    const grp = new THREE.Group(); grp.matrixAutoUpdate = false;
    const mesh = new THREE.Mesh(geo, bmat); mesh.castShadow = true; mesh.receiveShadow = true; grp.add(mesh);
    grp.add(makeStuds(studs, studGeo, smat, brickCols));
    scene.add(grp); groups.push(grp);
  }
  // the wordmark print on the 1x8 chest brick (body group)
  {
    const pw = 8 * S - 0.003, ph = HH - 0.003;
    const pm = new THREE.MeshPhysicalMaterial({ color: lc(0x0a0c14), roughness: 0.32, clearcoat: 0.3, clearcoatRoughness: 0.15, transparent: true, depthWrite: false, map: rig.logoTex });
    pm.onBeforeCompile = (sh) => {
      sh.fragmentShader = sh.fragmentShader.replace('#include <map_fragment>', `
          vec2 lu = (vMapUv - vec2(0.06, 0.245)) / vec2(0.88, 0.51);
          float a = (lu.x > 0.0 && lu.x < 1.0 && lu.y > 0.0 && lu.y < 1.0) ? texture2D(map, vec2(lu.x, 1.0 - lu.y)).a : 0.0;
          diffuseColor.a *= a;`);
    };
    pm.customProgramCacheKey = () => 'sb-lego-print';
    const print = new THREE.Mesh(new THREE.PlaneGeometry(pw, ph), pm);
    print.position.set(chest.x0 + 4 * S, chest.y0 + 1.5 * PH, chest.zFront + 0.0004); print.renderOrder = 2;
    groups[0].add(print);
  }
  // smooth trans-black visor element with printed glowing eyes (skinned: follows the head), clipped to the opening
  const visMat = new THREE.MeshPhysicalMaterial({ color: lc(0x0d1018), roughness: 0.14, metalness: 0, clearcoat: 1, clearcoatRoughness: 0.11, emissive: 0xffffff, emissiveIntensity: 1 });
  const uFix = { value: F[1].clone() }, uFixInvR = { value: new THREE.Matrix3().setFromMatrix4(F[1]).transpose() };
  visMat.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, rig.shared.faceU, { uFix, uFixInvR });
    sh.vertexShader = sh.vertexShader.replace('#include <common>', '#include <common>\nattribute vec3 _face;\nuniform mat4 uFix;\nuniform mat3 uFixInvR;\nvarying vec3 vFace;\nvarying vec3 vRP;')
      // a moulded windscreen: shade with a smooth ellipsoid normal instead of the scan's creases (skinned like any normal)
      .replace('#include <beginnormal_vertex>', `vec3 qV = (uFix * vec4(position, 1.0)).xyz - vec3(${VIS.cx.toFixed(4)}, ${VIS.cy.toFixed(4)}, -0.06);
        vec3 objectNormal = uFixInvR * normalize(qV / vec3(0.42 * 0.42, 0.36 * 0.36, 0.335 * 0.335));`)
      .replace('#include <begin_vertex>', '#include <begin_vertex>\nvFace = _face; vRP = (uFix * vec4(position, 1.0)).xyz;');
    sh.fragmentShader = sh.fragmentShader.replace('#include <common>', '#include <common>\nvarying vec3 vFace;\nvarying vec3 vRP;\n' + FACE + `
        bool inOpen(vec2 p) {
          const vec2 G0 = vec2(${H1.X0.toFixed(5)}, ${H1.Y0.toFixed(5)}), GS = vec2(${S.toFixed(5)}, ${PH.toFixed(5)});
          vec2 e = ((floor((p - G0) / GS) + 0.5) * GS + G0 - vec2(${VIS.cx.toFixed(4)}, ${VIS.cy.toFixed(4)})) / vec2(${VIS.rx.toFixed(4)}, ${VIS.ry.toFixed(4)});
          return dot(e, e) < 1.0;
        }`)
      .replace('#include <clipping_planes_fragment>', `#include <clipping_planes_fragment>
        // the glass fills exactly the opening's cells (+ a quarter cell tucked under the frame)
        if (vRP.z < 0.06 || !(inOpen(vRP.xy) || inOpen(vRP.xy + vec2(${(0.25 * S).toFixed(4)}, 0.0)) || inOpen(vRP.xy - vec2(${(0.25 * S).toFixed(4)}, 0.0))
            || inOpen(vRP.xy + vec2(0.0, ${(0.4 * PH).toFixed(4)})))) discard;`)
      .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
        float fa = vFace.z > 0.01 ? screenFace(vFace.xy) * smoothstep(0.2, 0.6, vFace.z) : 0.0;
        diffuseColor.rgb = mix(diffuseColor.rgb, vec3(0.9, 0.97, 1.0), fa);
        totalEmissiveRadiance = vec3(0.55, 0.85, 1.0) * fa * 2.4 * uEyeGlow;`);
  };
  visMat.customProgramCacheKey = () => 'sb-lego-visor2';
  const visor = ctx.robotMesh(visMat); visor.castShadow = false; scene.add(visor);
  // ---- brick-built set: palette colours, brick seams + bevels from world position, studs on top faces
  const cols = [], rm = [];
  for (let i = 0; i < NPAL; i++) { const name = Object.keys(PAL).find((k) => PAL[k] === i); cols.push(lc(SETCOL[name] ?? 0xa0a5a9)); rm.push([name === 'sky' ? 1 : 0.3, 0]); }
  const em = cols.map(() => new THREE.Color(0, 0, 0)); em[PAL.sky] = lc(0x9fd6f5).multiplyScalar(0.9); em[PAL.city] = em[PAL.sky].clone(); em[PAL.screen] = lc(0x0d69ab).multiplyScalar(0.5);
  const setMat = litSetMaterial({ cols, rm, em, physical: true, key: 'lego', phys: { clearcoat: 0.3, clearcoatRoughness: 0.2 }, hooks: {
    pars: `const float BS = ${S.toFixed(4)}, BH = ${HH.toFixed(4)};\nfloat gSeam = 0.0;\n` + FLOOR_STUDS,
    normal: /* glsl */ `
      {
        vec3 wn = normalize((vec4(normal, 0.0) * viewMatrix).xyz);
        bool side = abs(wn.y) < 0.5 && vPal != ${PAL.sky} && vPal != ${PAL.city} && vPal != ${PAL.leaf} && vPal != ${PAL.screen};
        if (side) {
          float u = abs(wn.z) > 0.5 ? vWPos.x : vWPos.z;
          float row = floor(vWPos.y / BH);
          float fy = fract(vWPos.y / BH);
          float fx = fract((u + mod(row, 2.0) * 2.0 * BS) / (4.0 * BS));
          float ey = min(fy, 1.0 - fy) * BH, ex = min(fx, 1.0 - fx) * 4.0 * BS;
          gSeam = 1.0 - smoothstep(0.0, 0.0011, min(ey, ex));
          vec3 tU = abs(wn.z) > 0.5 ? vec3(1.0, 0.0, 0.0) : vec3(0.0, 0.0, 1.0);
          float by = (1.0 - smoothstep(0.0, 0.0035, ey)) * (fy < 0.5 ? -1.0 : 1.0);
          float bx = (1.0 - smoothstep(0.0, 0.0035, ex)) * (fx < 0.5 ? -1.0 : 1.0);
          normal = normalize(normal + (mat3(viewMatrix) * (vec3(0.0, 1.0, 0.0) * by + tU * bx)) * 0.8);
        }
        if (gStud > 0.5) normal = normalize(mat3(viewMatrix) * gStudN);
      }`,
    albedo: /* glsl */ `
      if (vPal == ${PAL.floor} && FLOOR_STUD_REGION(vWPos)) { floorStuds(vWPos); diffuseColor.rgb *= gStudAO * (gStud > 1.5 ? 1.04 : 1.0); }
      if (vPal == ${PAL.wall}) { float row = floor(vWPos.y / BH); float bi = floor((vWPos.x + mod(row, 2.0) * 2.0 * BS) / (4.0 * BS));
        float hb = h12(vec2(bi, row)); diffuseColor.rgb *= 0.97 + 0.05 * hb; if (hb > 0.9 && vWPos.y > 0.1) diffuseColor.rgb = vec3(0.29, 0.24, 0.16); }`,
    emissive: `diffuseColor.rgb *= 1.0 - 0.7 * gSeam; totalEmissiveRadiance *= 1.0 - 0.6 * gSeam;`,
  } });
  const setMesh = new THREE.Mesh(ctx.setGeo.sharp, setMat); setMesh.receiveShadow = true; setMesh.castShadow = true; scene.add(setMesh);
  // studs: baseplate (around the robot), desk top, window sill, board top, monitor top
  // (the baseplate's studs are ray-traced in the floor shader: FLOOR_STUDS)
  const studList = [];
  const addGrid = (x0, x1, z0, z1, y, col) => { for (let x = x0 + S / 2; x < x1; x += S) for (let z = z0 + S / 2; z < z1; z += S) studList.push([x, y, z, lc(col)]); };
  const D = LAYOUT.desk; addGrid(D.x - D.w / 2 + 0.02, D.x + D.w / 2 - 0.02, D.z - D.d / 2 + 0.02, D.z - 0.1, D.h, SETCOL.deskTop);
  addGrid(D.x + 0.25, D.x + D.w / 2 - 0.02, D.z - 0.1, D.z + D.d / 2 - 0.02, D.h, SETCOL.deskTop);
  const Wn = LAYOUT.win; addGrid(Wn.x0 - 0.08, Wn.x1 + 0.08, LAYOUT.wallZ + 0.0, LAYOUT.wallZ + 0.1, Wn.y0 - 0.05 + 0.003, SETCOL.winFrame);
  const Bd = LAYOUT.board; addGrid(Bd.x - Bd.w / 2 - 0.02, Bd.x + Bd.w / 2 + 0.02, Bd.z - 0.018, Bd.z + 0.018, Bd.y0 + Bd.h + 0.027, SETCOL.boardFrame);
  { const sp = makeStuds(studList, studGeoLo, smat, null); sp.castShadow = false; scene.add(sp); }
  // lights: soft studio
  scene.add(new THREE.HemisphereLight(0xffffff, 0xb8b2a8, 1.1));
  const key = new THREE.DirectionalLight(0xfff4e8, 2.6); key.position.set(-2.0, 3.6, 2.8); key.target.position.set(0, 0.4, -0.3);
  key.castShadow = true; key.shadow.mapSize.set(1024, 1024); key.shadow.bias = -0.0004; key.shadow.normalBias = 0.012;
  Object.assign(key.shadow.camera, { left: -2.0, right: 2.0, top: 2.2, bottom: -1.2, near: 0.5, far: 9 }); key.shadow.camera.updateProjectionMatrix();
  scene.add(key, key.target);
  const fill = new THREE.DirectionalLight(0xe8f0ff, 0.8); fill.position.set(2.4, 1.6, 2.2); scene.add(fill);
  // post: DOF from a half-res blur, glow from a quarter-res bright pass
  const rt = makeRT(W, H, { type: THREE.HalfFloatType, samples: 0, depthTexture: true });   // (MSAA costs ~0.35 s in SwiftShader: FXAA instead)
  const hw = Math.ceil(W / 2), hh = Math.ceil(H / 2), qw = Math.ceil(W / 4), qh = Math.ceil(H / 4);
  const rtH = makeRT(hw, hh, { depth: false, type: THREE.HalfFloatType });
  const rtQ = makeRT(qw, qh, { depth: false, type: THREE.HalfFloatType });
  const down = new Pass(`uniform sampler2D tSrc; uniform vec2 uTexel; varying vec2 vUv; void main() { gl_FragColor = (texture2D(tSrc, vUv + uTexel * vec2(-1.0)) + texture2D(tSrc, vUv + uTexel) + texture2D(tSrc, vUv + uTexel * vec2(1.0, -1.0)) + texture2D(tSrc, vUv + uTexel * vec2(-1.0, 1.0))) * 0.25; }`,
    { tSrc: { value: rt.texture }, uTexel: { value: new THREE.Vector2(0.5 / W, 0.5 / H) } });
  const bright = new Pass(`uniform sampler2D tSrc; uniform vec2 uTexel; varying vec2 vUv; void main() {
      vec3 s = (texture2D(tSrc, vUv + uTexel * vec2(-1.0)).rgb + texture2D(tSrc, vUv + uTexel).rgb + texture2D(tSrc, vUv + uTexel * vec2(1.0, -1.0)).rgb + texture2D(tSrc, vUv + uTexel * vec2(-1.0, 1.0)).rgb) * 0.25;
      gl_FragColor = vec4(max(s - vec3(1.15), 0.0), 1.0); }`,
    { tSrc: { value: rtH.texture }, uTexel: { value: new THREE.Vector2(0.5 / hw, 0.5 / hh) } });
  const blur = new Blur(hw, hh, THREE.HalfFloatType), blurQ = new Blur(qw, qh, THREE.HalfFloatType);
  const comp = new Pass(COMP, { tC: { value: rt.texture }, tD: { value: rt.depthTexture }, tDof: { value: null }, tGlow: { value: null }, uNF: { value: new THREE.Vector2() }, uFocus: { value: 4.5 }, uRes: { value: new THREE.Vector2(W, H) } });
  const tmp = new THREE.Vector3();
  return {
    render(target) {
      const r = ctx.renderer, rr = rig.rigRoot;
      const vis = ctx.robotVisible;
      for (let g = 0; g < 4; g++) { groups[g].matrix.multiplyMatrices(bones[g].matrixWorld, inv[g]).multiply(Finv[g]); groups[g].matrixWorldNeedsUpdate = true; groups[g].visible = vis; }
      visor.visible = vis;
      r.shadowMap.needsUpdate = true;
      r.setRenderTarget(rt); r.render(scene, ctx.camera);
      down.render(r, rtH);
      bright.render(r, rtQ);
      comp.u.tGlow.value = blurQ.run(r, rtQ.texture, 1.6, 2);
      comp.u.tDof.value = blur.run(r, rtH.texture, 1.5, 2);
      comp.u.uNF.value.set(ctx.camera.near, ctx.camera.far);
      comp.u.uFocus.value = ctx.camera.position.distanceTo(tmp.set(rr.position.x, 0.5 + rr.position.y, rr.position.z));
      comp.render(r, target);
    },
  };
}

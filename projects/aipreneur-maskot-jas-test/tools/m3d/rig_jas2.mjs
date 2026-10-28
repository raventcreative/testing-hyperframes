// SUIT MASCOT v2 (cute chibi boy, slim jacket, Tripo) — adapted from rig.mjs: new joint layout measured from the mesh
// cross-sections, mouth groove smoothed flat, cleaned base colour swapped in (jacket misprint + baked smile removed).
// Usage: node rig_jas.mjs <in_rt.glb> <basecolor_clean.png> <out.glb>
// Input : assets/mascot3d/mascot_rt.glb   (optimized from the original Tripo GLB)
// Output: assets/mascot3d/mascot_rigged.glb (+ JOINTS_0 / WEIGHTS_0 / _FACEMASK, 19-bone skin)
// Usage : node rig.mjs <in.glb> <out.glb>
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import sharp from 'sharp';

const [src, cleanTex, out] = process.argv.slice(2);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS);
const doc = await io.read(src);
const root = doc.getRoot();
const prim = root.listMeshes()[0].listPrimitives()[0];
let P = prim.getAttribute('POSITION').getArray();
let UV = prim.getAttribute('TEXCOORD_0').getArray();
let IDX = prim.getIndices().getArray();
let N = P.length / 3;
const Z = 0.025, ZA = 0.012;   // body line / arm line depth // depth of the bone line (body centre)

// ---- skeleton (rest pose, object space; +z = front, +x = character's LEFT) ----
const B = [
  ['hips', null, [0, 0.245, Z]],
  ['spine', 'hips', [0, 0.30, Z]],
  ['chest', 'spine', [0, 0.37, Z]],
  ['neck', 'chest', [0, 0.455, Z]],
  ['head', 'neck', [0, 0.49, Z]],
  ['shoulder_L', 'chest', [0.06, 0.43, Z]],
  ['upperarm_L', 'shoulder_L', [0.105, 0.425, ZA]],
  ['forearm_L', 'upperarm_L', [0.155, 0.345, ZA]],
  ['hand_L', 'forearm_L', [0.188, 0.296, ZA]],
  ['shoulder_R', 'chest', [-0.06, 0.43, Z]],
  ['upperarm_R', 'shoulder_R', [-0.105, 0.425, ZA]],
  ['forearm_R', 'upperarm_R', [-0.155, 0.345, ZA]],
  ['hand_R', 'forearm_R', [-0.188, 0.296, ZA]],
  ['thigh_L', 'hips', [0.055, 0.235, Z]],
  ['shin_L', 'thigh_L', [0.06, 0.125, Z]],
  ['foot_L', 'shin_L', [0.065, 0.045, Z]],
  ['thigh_R', 'hips', [-0.055, 0.235, Z]],
  ['shin_R', 'thigh_R', [-0.06, 0.125, Z]],
  ['foot_R', 'shin_R', [-0.065, 0.045, Z]],
];
const idxOf = Object.fromEntries(B.map((b, i) => [b[0], i]));
// segment each bone influences (from its head to tail)
const TAIL = {
  hips: [0, 0.30, Z], spine: [0, 0.37, Z], chest: [0, 0.45, Z], neck: [0, 0.49, Z], head: [0, 0.9, 0.0],
  'shoulder_L': [0.105, 0.425, ZA], 'upperarm_L': [0.155, 0.345, ZA], 'forearm_L': [0.188, 0.296, ZA], 'hand_L': [0.232, 0.215, ZA],
  'shoulder_R': [-0.105, 0.425, ZA], 'upperarm_R': [-0.155, 0.345, ZA], 'forearm_R': [-0.188, 0.296, ZA], 'hand_R': [-0.232, 0.215, ZA],
  'thigh_L': [0.06, 0.125, Z], 'shin_L': [0.065, 0.045, Z], 'foot_L': [0.08, 0.01, 0.12],
  'thigh_R': [-0.06, 0.125, Z], 'shin_R': [-0.065, 0.045, Z], 'foot_R': [-0.08, 0.01, 0.12],
};
function segDist(p, a, b) {
  const ab = [b[0] - a[0], b[1] - a[1], b[2] - a[2]], ap = [p[0] - a[0], p[1] - a[1], p[2] - a[2]];
  const l2 = ab[0] ** 2 + ab[1] ** 2 + ab[2] ** 2;
  let t = l2 ? (ap[0] * ab[0] + ap[1] * ab[1] + ap[2] * ab[2]) / l2 : 0; t = Math.max(0, Math.min(1, t));
  const d = [ap[0] - ab[0] * t, ap[1] - ab[1] * t, ap[2] - ab[2] * t];
  return Math.hypot(d[0], d[1], d[2]);
}
// region gate: which bones a vertex may use (prevents hair→arm, hand→thigh bleeding)
// ARM vs TORSO labelling (measured cross-sections): below y 0.315 the arm is a separate blob (|x| > 0.135); above it,
// a vertex is arm only if it lies inside the sleeve tube around the arm axis (3D distance) — the jacket's side panel
// and hem therefore never receive arm weights (no cloth dragged up when the arm lifts).
const AXIS = [[0.105, 0.425], [0.14, 0.38], [0.155, 0.34], [0.183, 0.30], [0.21, 0.27]];   // measured sleeve centres
function armDist(x, y, z) {
  const ax = Math.abs(x); let d = 9;
  for (let i = 0; i < AXIS.length - 1; i++) d = Math.min(d, segDist([ax, y, z], [AXIS[i][0], AXIS[i][1], ZA], [AXIS[i + 1][0], AXIS[i + 1][1], ZA]));
  return d;
}
// torso vertices fused to the inner sleeve (armpit band): they share a little of the upper-arm motion so the
// fused seam stretches over a wide area instead of one long sliver
function seamBand(x, y, z) { return Math.abs(x) > 0.095 && y > 0.33 && y < 0.42 && z < 0.05 && armDist(x, y, z) < 0.08; }   // armpit side/back only (never the front chest / logo)
function isArm(x, y, z) {
  const ax = Math.abs(x);
  if (y > 0.17 && y < 0.315) return ax > 0.132;
  if (y >= 0.315 && y < 0.45) {
    let d = 9;
    for (let i = 0; i < AXIS.length - 1; i++) d = Math.min(d, segDist([ax, y, z], [AXIS[i][0], AXIS[i][1], ZA], [AXIS[i + 1][0], AXIS[i + 1][1], ZA]));
    return d < 0.062 && ax > 0.085;
  }
  return false;
}
function allowed(x, y, z, arm) {
  const ax = Math.abs(x), side = x >= 0 ? 'L' : 'R';
  if (y > 0.49) return ['head'];
  if (y > 0.455) return ['neck', 'head', 'chest'];
  if (arm) return y > 0.385 ? [`upperarm_${side}`, `forearm_${side}`, `shoulder_${side}`, 'chest'] : [`upperarm_${side}`, `forearm_${side}`, `hand_${side}`];
  if (y > 0.395 && ax > 0.07) return ['chest', `shoulder_${side}`, `upperarm_${side}`, 'neck'];
  if (seamBand(x, y, z)) return ['chest', 'spine', `shoulder_${side}`, `upperarm_${side}`];
  if (y > 0.35) return ['chest', 'spine', `shoulder_${side}`, 'neck'];
  if (y > 0.25) return ['spine', 'hips', 'chest'];
  return ['hips', `thigh_${side}`, `shin_${side}`, `foot_${side}`];
}
// ---- SEAM CUT: the Tripo mesh fuses the inner sleeve to the jacket side below the armpit. Triangles that straddle
// arm / torso there are given to their majority side and the minority corners are duplicated, so the arm separates
// cleanly when it lifts (no stretched cloth strap). The shoulder top (y >= 0.40) stays continuous (blended).
let ARMV = new Uint8Array(N);
for (let v = 0; v < N; v++) ARMV[v] = isArm(P[3*v], P[3*v+1], P[3*v+2]) ? 1 : 0;
// label smoothing: majority vote over surface neighbours (UV-seam twins joined) in the arm/torso junction band,
// so the seam cut runs as a smooth armhole line instead of a saw-tooth (no ragged edge when the arm lifts)
{
  const nbr = Array.from({ length: N }, () => new Set());
  for (let t = 0; t < IDX.length; t += 3) { const a = IDX[t], b = IDX[t+1], c = IDX[t+2]; nbr[a].add(b).add(c); nbr[b].add(a).add(c); nbr[c].add(a).add(b); }
  const twin = new Map();
  for (let v = 0; v < N; v++) { const k = `${Math.round(P[3*v]*1e4)},${Math.round(P[3*v+1]*1e4)},${Math.round(P[3*v+2]*1e4)}`; const u = twin.get(k); if (u === undefined) twin.set(k, v); else { for (const w of nbr[v]) nbr[u].add(w); for (const w of nbr[u]) nbr[v].add(w); } }
  // 2-ring neighbourhoods for a wider vote
  for (let it = 0; it < 6; it++) {
    const nx = Uint8Array.from(ARMV); let ch = 0;
    for (let v = 0; v < N; v++) {
      const y = P[3*v+1]; if (y < 0.26 || y > 0.43 || Math.abs(P[3*v]) < 0.08) continue;
      let a = ARMV[v] ? 1 : 0, n = 1;
      for (const u of nbr[v]) { a += ARMV[u]; n++; for (const w of nbr[u]) { a += ARMV[w] * 0.5; n += 0.5; } }
      const lab = a / n > 0.5 ? 1 : 0; if (lab !== ARMV[v]) { nx[v] = lab; ch++; }
    }
    ARMV = nx; if (!ch) break;
  }
}
// label clean-up: islands of one label enclosed by the other (sleeve scraps tagged torso, jacket scraps tagged arm)
// take the label of what surrounds them, so nothing is left hanging when the arm moves
for (let pass = 0; pass < 2; pass++) {
  const par = new Int32Array(N).map((_, i) => i);
  const f = (x) => { while (par[x] !== x) { par[x] = par[par[x]]; x = par[x]; } return x; };
  for (let t = 0; t < IDX.length; t += 3) {
    const a = IDX[t], b = IDX[t+1], c = IDX[t+2];
    if (ARMV[a] === ARMV[b]) par[f(b)] = f(a); if (ARMV[a] === ARMV[c]) par[f(c)] = f(a); if (ARMV[b] === ARMV[c]) par[f(c)] = f(b);
  }
  { // UV charts are split at seams: join coincident vertices (same label) so components follow the real surface
    const first = new Map();
    for (let v = 0; v < N; v++) { const k = `${Math.round(P[3*v]*1e4)},${Math.round(P[3*v+1]*1e4)},${Math.round(P[3*v+2]*1e4)},${ARMV[v]}`;
      const u = first.get(k); if (u === undefined) first.set(k, v); else par[f(v)] = f(u); }
  }
  const size = new Map(); for (let v = 0; v < N; v++) { const r = f(v); size.set(r, (size.get(r) || 0) + 1); }
  // keep: the biggest torso component and the biggest arm component on each side
  let bestT = -1, bestTs = 0; const bestA = { L: [-1, 0], R: [-1, 0] };
  for (const [r, n] of size) {
    if (ARMV[r] === 0) { if (n > bestTs) { bestT = r; bestTs = n; } }
    else { const sd = P[3*r] >= 0 ? 'L' : 'R'; if (n > bestA[sd][1]) bestA[sd] = [r, n]; }
  }
  const keep = new Set([bestT, bestA.L[0], bestA.R[0]]);
  let flipped = 0;
  for (let v = 0; v < N; v++) { const r = f(v); if (!keep.has(r) && size.get(r) < 4000) { ARMV[v] = 1 - ARMV[v]; flipped++; } }
  console.log('label clean-up pass', pass, 'flipped', flipped);
  if (!flipped) break;
}
{
  const NRM = prim.getAttribute('NORMAL').getArray();
  const idx = Uint32Array.from(IDX); const dup = new Map(); const src = []; const lab = [];
  let cut = 0;
  for (let t = 0; t < idx.length; t += 3) {
    const vs = [idx[t], idx[t+1], idx[t+2]], ls = vs.map((v) => ARMV[v]);
    const na = ls[0] + ls[1] + ls[2]; if (na === 0 || na === 3) continue;
    const cy = (P[3*vs[0]+1] + P[3*vs[1]+1] + P[3*vs[2]+1]) / 3; if (cy >= 0.40) continue;
    const owner = na >= 2 ? 1 : 0; cut++;
    for (let k = 0; k < 3; k++) if (ls[k] !== owner) {
      const key = vs[k] * 2 + owner; let nv = dup.get(key);
      if (nv === undefined) { nv = N + src.length; dup.set(key, nv); src.push(vs[k]); lab.push(owner); }
      idx[t + k] = nv;
    }
  }
  const M = N + src.length;
  const nP = new Float32Array(M * 3), nN = new Float32Array(M * 3), nU = new Float32Array(M * 2), nA = new Uint8Array(M);
  nP.set(P); nN.set(NRM); nU.set(UV); nA.set(ARMV);
  src.forEach((v, i) => { const d = N + i; nP.set(P.subarray(3*v, 3*v+3), 3*d); nN.set(NRM.subarray(3*v, 3*v+3), 3*d); nU.set(UV.subarray(2*v, 2*v+2), 2*d); nA[d] = lab[i]; });
  prim.getAttribute('POSITION').setArray(nP); prim.getAttribute('NORMAL').setArray(nN); prim.getAttribute('TEXCOORD_0').setArray(nU);
  prim.getIndices().setArray(idx);
  P = nP; UV = nU; IDX = idx; N = M; ARMV = nA;
  for (const m of root.listMaterials()) m.setDoubleSided(true);   // the opened seam shows the dark jacket lining, never the background
  console.log('seam cut: triangles', cut, 'duplicated verts', src.length);
}
const nb = B.length;
let W = new Float32Array(N * nb);
for (let v = 0; v < N; v++) {
  const p = [P[3 * v], P[3 * v + 1], P[3 * v + 2]];
  const names = allowed(p[0], p[1], p[2], ARMV[v]);
  let s = 0;
  for (const n of names) {
    const i = idxOf[n];
    const d = segDist(p, B[i][2], TAIL[n]) + 0.004;
    const w = 1 / Math.pow(d, 6);
    W[v * nb + i] = w; s += w;
  }
  for (const n of names) W[v * nb + idxOf[n]] /= s;
}
for (let v = 0; v < N; v++) {
  const x = P[3*v], y = P[3*v+1], z = P[3*v+2];
  if (ARMV[v] || !seamBand(x, y, z)) continue;
  const d = armDist(x, y, z), share = 0.4 * Math.min(1, Math.max(0, (0.08 - d) / 0.03));
  const ua = idxOf[`upperarm_${x >= 0 ? 'L' : 'R'}`];
  for (let k = 0; k < nb; k++) W[v * nb + k] *= (1 - share);
  W[v * nb + ua] += share;
}
// Laplacian smoothing over mesh adjacency (keeps joints soft; head stays rigid)
const adj = Array.from({ length: N }, () => new Set());
for (let i = 0; i < IDX.length; i += 3) {
  const a = IDX[i], b = IDX[i + 1], c = IDX[i + 2];
  adj[a].add(b); adj[a].add(c); adj[b].add(a); adj[b].add(c); adj[c].add(a); adj[c].add(b);
}
for (let it = 0; it < 6; it++) {
  const W2 = new Float32Array(W);
  for (let v = 0; v < N; v++) {
    if (P[3 * v + 1] > 0.52) continue; // head/hair rigid
    const nbrs = adj[v]; if (!nbrs.size) continue;
    for (let k = 0; k < nb; k++) {
      let s = W[v * nb + k];
      for (const u of nbrs) s += W[u * nb + k];
      W2[v * nb + k] = s / (nbrs.size + 1);
    }
    // keep the gate: zero out bones the vertex may not use, renormalise
    const ok = allowed(P[3 * v], P[3 * v + 1], P[3 * v + 2], ARMV[v]).map((n) => idxOf[n]);
    let tot = 0; for (let k = 0; k < nb; k++) { if (!ok.includes(k)) W2[v * nb + k] = 0; tot += W2[v * nb + k]; }
    if (tot > 0) for (let k = 0; k < nb; k++) W2[v * nb + k] /= tot;
  }
  W = W2;
}
// extra smoothing in the shoulder / armpit band (removes saw-tooth weight edges where the arm joins the body)
for (let it = 0; it < 24; it++) {
  const W2 = new Float32Array(W);
  for (let v = 0; v < N; v++) {
    const x = P[3*v], y = P[3*v+1];
    if (!(y > 0.37 && y < 0.47 && Math.abs(x) > 0.05)) continue;
    const nbrs = adj[v]; if (!nbrs.size) continue;
    for (let k = 0; k < nb; k++) { let sm = W[v*nb+k]; for (const u of nbrs) sm += W[u*nb+k]; W2[v*nb+k] = sm / (nbrs.size + 1); }
    const ok = allowed(x, y, P[3*v+2], ARMV[v]).map((n) => idxOf[n]);
    let tot = 0; for (let k = 0; k < nb; k++) { if (!ok.includes(k)) W2[v*nb+k] = 0; tot += W2[v*nb+k]; }
    if (tot > 0) for (let k = 0; k < nb; k++) W2[v*nb+k] /= tot;
  }
  W = W2;
}
// unify weights of coincident vertices so UV seams never open under deformation
{
  const key = (v) => `${Math.round(P[3*v]*1e5)},${Math.round(P[3*v+1]*1e5)},${Math.round(P[3*v+2]*1e5)},${ARMV[v]}`;
  const groups = new Map();
  for (let v = 0; v < N; v++) { const k = key(v); let g = groups.get(k); if (!g) groups.set(k, (g = [])); g.push(v); }
  let merged = 0;
  for (const g of groups.values()) if (g.length > 1) {
    merged += g.length;
    for (let k = 0; k < nb; k++) { let s = 0; for (const v of g) s += W[v*nb+k]; s /= g.length; for (const v of g) W[v*nb+k] = s; }
  }
  console.log('seam-coincident verts unified', merged);
}
// keep top-4 influences
const J = new Uint16Array(N * 4), WW = new Float32Array(N * 4);
for (let v = 0; v < N; v++) {
  const arr = []; for (let k = 0; k < nb; k++) if (W[v * nb + k] > 1e-4) arr.push([W[v * nb + k], k]);
  arr.sort((a, b) => b[0] - a[0]); const top = arr.slice(0, 4); const s = top.reduce((a, b) => a + b[0], 0) || 1;
  if (!top.length) top.push([1, idxOf.hips]);
  top.forEach(([w, k], j) => { J[v * 4 + j] = k; WW[v * 4 + j] = w / s; });
}

// ---- face mask: UV islands that contain the eyes / mouth front surface ----
// union-find over triangles sharing vertices (welded mesh ⇒ islands = UV charts)
const parent = new Int32Array(N).map((_, i) => i);
const find = (x) => { while (parent[x] !== x) { parent[x] = parent[parent[x]]; x = parent[x]; } return x; };
for (let i = 0; i < IDX.length; i += 3) { const a = find(IDX[i]), b = find(IDX[i + 1]), c = find(IDX[i + 2]); parent[b] = a; parent[c] = a; }
const FEATURES = [[-0.091, 0.595], [0.091, 0.595], [0.0, 0.548], [0.09, 0.68], [-0.09, 0.68]]; // eye L(screen-left), eye R, mouth
const faceIslands = new Set();
for (const [fx, fy] of FEATURES) {
  let best = -1, bz = -9;
  for (let v = 0; v < N; v++) {
    const dx = P[3 * v] - fx, dy = P[3 * v + 1] - fy;
    if (dx * dx + dy * dy < 0.012 ** 2 && P[3 * v + 2] > bz) { bz = P[3 * v + 2]; best = v; }
  }
  if (best >= 0) faceIslands.add(find(best));
  console.log('feature', fx, fy, 'front z', bz.toFixed(4), 'island', best >= 0 ? find(best) : null);
}
const FM = new Float32Array(N);
let fmCount = 0;
for (let v = 0; v < N; v++) if (faceIslands.has(find(v)) && P[3 * v + 1] > 0.49) { FM[v] = 1; fmCount++; }

// the mouth is a sculpted cavity whose inner surface lives on other UV charts: include it by volume
let mouthCount = 0;
for (let v = 0; v < N; v++) {
  const x = P[3 * v], y = P[3 * v + 1], z = P[3 * v + 2];
  if (Math.abs(x) < 0.055 && y > 0.515 && y < 0.585 && z > 0.12 && !FM[v]) { FM[v] = 1; mouthCount++; }
}
console.log('mouth-cavity verts added', mouthCount);
// eye components (eyeball domes, whites, lash rims) that live on their own small charts
const baseTex = root.listTextures().find((t) => /basecolor/i.test(t.getName() || '')) || root.listTextures()[0];
const { data: px, info } = await sharp(Buffer.from(baseTex.getImage())).raw().toBuffer({ resolveWithObject: true });
const tex = (u, v) => { const x = Math.min(info.width - 1, Math.max(0, Math.round(u * (info.width - 1)))), y = Math.min(info.height - 1, Math.max(0, Math.round(v * (info.height - 1)))); const o = (y * info.width + x) * info.channels; return [px[o], px[o + 1], px[o + 2]]; };
const islandStats = new Map();
for (let v = 0; v < N; v++) {
  const r = find(v); let st = islandStats.get(r);
  if (!st) { st = { n: 0, bright: 0, x0: 9, x1: -9, y0: 9, y1: -9, z0: 9 }; islandStats.set(r, st); }
  st.n++; const x = P[3*v], y = P[3*v+1], z = P[3*v+2];
  st.x0 = Math.min(st.x0, x); st.x1 = Math.max(st.x1, x); st.y0 = Math.min(st.y0, y); st.y1 = Math.max(st.y1, y); st.z0 = Math.min(st.z0, z);
  const c = tex(UV[2*v], UV[2*v+1]); if (0.299*c[0] + 0.587*c[1] + 0.114*c[2] > 175) st.bright++;
}
const EYES = [[-0.091, 0.595, 0.045, 0.04], [0.091, 0.595, 0.045, 0.04]];
const eyeIslands = new Set();
for (let v = 0; v < N; v++) {
  const x = P[3*v], y = P[3*v+1], z = P[3*v+2]; if (z < 0.1) continue;
  for (const [cx, cy, rx, ry] of EYES) {
    const e = ((x - cx) / (rx * 1.3)) ** 2 + ((y - cy) / (ry * 1.35)) ** 2;
    if (e < 1) { const r = find(v); const st = islandStats.get(r);
      const compact = st.y1 < 0.68 && st.y0 > 0.53 && st.x1 - st.x0 < 0.13 && st.y1 - st.y0 < 0.11;
      if (compact && (st.bright / st.n > 0.25 || st.n < 400)) eyeIslands.add(r); }
  }
}
let eyeCount = 0;
for (let v = 0; v < N; v++) if (!FM[v] && eyeIslands.has(find(v))) { FM[v] = 1; eyeCount++; }
console.log('eye-component islands', eyeIslands.size, 'verts', eyeCount);
console.log('face-mask verts', fmCount, 'islands', faceIslands.size);

// ---- flatten the sculpted smile groove (Laplacian membrane, boundary fixed) and re-smooth its normals ----
{
  const inM = (v) => { const x = P[3*v], y = P[3*v+1], z = P[3*v+2]; return z > 0.15 && ((x / 0.036) ** 2 + ((y - 0.548) / 0.013) ** 2) < 1; };
  const Pa = prim.getAttribute('POSITION'), Na = prim.getAttribute('NORMAL');
  const ids = []; for (let v = 0; v < N; v++) if (inM(v)) ids.push(v);
  // UV-seam twins (same position, different UV) must move together or the surface cracks open
  const key = (v) => `${Math.round(P[3*v]*1e5)},${Math.round(P[3*v+1]*1e5)},${Math.round(P[3*v+2]*1e5)}`;
  const twins = new Map(); for (let v = 0; v < N; v++) { const k = key(v); let g = twins.get(k); if (!g) twins.set(k, (g = [])); g.push(v); }
  const grp = new Map(); for (const g of twins.values()) for (const v of g) grp.set(v, g);
  const idset = new Set(); for (const v of ids) for (const u of grp.get(v)) idset.add(u);
  const all = [...idset];
  const nbr = (v) => { const out = new Set(); for (const t of grp.get(v)) for (const u of adj[t]) out.add(u); return out; };
  const NB = new Map(all.map((v) => [v, [...nbr(v)]]));
  for (let it = 0; it < 60; it++) {
    const nx = new Map();
    for (const v of all) { let sx = 0, sy = 0, sz = 0, n = 0; for (const u of NB.get(v)) { sx += P[3*u]; sy += P[3*u+1]; sz += P[3*u+2]; n++; } if (n) nx.set(v, [sx/n, sy/n, sz/n]); }
    const done = new Set();
    for (const v of all) { if (done.has(v)) continue; const g = grp.get(v); let a = [0,0,0], c = 0;
      for (const u of g) { const q = nx.get(u); if (q) { a[0]+=q[0]; a[1]+=q[1]; a[2]+=q[2]; c++; } }
      if (c) for (const u of g) { P[3*u] = a[0]/c; P[3*u+1] = a[1]/c; P[3*u+2] = a[2]/c; done.add(u); } }
  }
  Pa.setArray(P);
  const NN = Na.getArray(), acc = new Float32Array(N * 3);
  for (let i = 0; i < IDX.length; i += 3) {
    const a = IDX[i], b = IDX[i+1], c = IDX[i+2];
    const e1 = [P[3*b]-P[3*a], P[3*b+1]-P[3*a+1], P[3*b+2]-P[3*a+2]], e2 = [P[3*c]-P[3*a], P[3*c+1]-P[3*a+1], P[3*c+2]-P[3*a+2]];
    const n = [e1[1]*e2[2]-e1[2]*e2[1], e1[2]*e2[0]-e1[0]*e2[2], e1[0]*e2[1]-e1[1]*e2[0]];
    for (const v of [a, b, c]) { acc[3*v] += n[0]; acc[3*v+1] += n[1]; acc[3*v+2] += n[2]; }
  }
  const near = (v) => { const x = P[3*v], y = P[3*v+1], z = P[3*v+2]; return z > 0.14 && ((x / 0.05) ** 2 + ((y - 0.548) / 0.025) ** 2) < 1; };
  for (let v = 0; v < N; v++) if (near(v)) { const l = Math.hypot(acc[3*v], acc[3*v+1], acc[3*v+2]) || 1; NN[3*v] = acc[3*v]/l; NN[3*v+1] = acc[3*v+1]/l; NN[3*v+2] = acc[3*v+2]/l; }
  Na.setArray(NN);
  console.log('mouth groove verts flattened', ids.length);
}
{
  const bt = root.listTextures().find((t) => /basecolor/i.test(t.getName() || ''));
  const webp = await sharp(cleanTex).webp({ quality: 92 }).toBuffer();
  bt.setImage(webp).setMimeType('image/webp');
  console.log('base colour swapped', webp.length);
}
// ---- write skin into the document ----
const buf = root.listBuffers()[0];
const joints = B.map(([name]) => doc.createNode(name));
B.forEach(([name, par, pos], i) => {
  const pp = par ? B[idxOf[par]][2] : [0, 0, 0];
  joints[i].setTranslation([pos[0] - pp[0], pos[1] - pp[1], pos[2] - pp[2]]);
  if (par) joints[idxOf[par]].addChild(joints[i]);
});
const rigRoot = doc.createNode('rig_root');
rigRoot.addChild(joints[0]);
const ibm = new Float32Array(16 * nb);
B.forEach(([, , pos], i) => { const m = [1,0,0,0, 0,1,0,0, 0,0,1,0, -pos[0],-pos[1],-pos[2],1]; ibm.set(m, 16 * i); });
const skin = doc.createSkin('mascot_skin').setSkeleton(joints[0]).setInverseBindMatrices(
  doc.createAccessor('ibm').setType('MAT4').setArray(ibm).setBuffer(buf));
joints.forEach((j) => skin.addJoint(j));
prim.setAttribute('JOINTS_0', doc.createAccessor('joints').setType('VEC4').setArray(J).setBuffer(buf));
prim.setAttribute('WEIGHTS_0', doc.createAccessor('weights').setType('VEC4').setArray(WW).setBuffer(buf));
prim.setAttribute('_FACEMASK', doc.createAccessor('facemask').setType('SCALAR').setArray(FM).setBuffer(buf));
const meshNode = root.listNodes().find((n) => n.getMesh());
meshNode.setSkin(skin);
meshNode.setName('mascot_mesh');
const scene = root.listScenes()[0];
scene.addChild(rigRoot);
await io.write(out, doc);
console.log('wrote', out, 'bones', nb, 'verts', N);

// SUIT MASCOT (chibi businessperson, Tripo) — adapted from rig.mjs: new joint layout measured from the mesh
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
const P = prim.getAttribute('POSITION').getArray();
const UV = prim.getAttribute('TEXCOORD_0').getArray();
const IDX = prim.getIndices().getArray();
const N = P.length / 3;
const Z = 0.03; // depth of the bone line (body centre)

// ---- skeleton (rest pose, object space; +z = front, +x = character's LEFT) ----
const B = [
  ['hips', null, [0, 0.245, Z]],
  ['spine', 'hips', [0, 0.30, Z]],
  ['chest', 'spine', [0, 0.37, Z]],
  ['neck', 'chest', [0, 0.455, Z]],
  ['head', 'neck', [0, 0.49, Z]],
  ['shoulder_L', 'chest', [0.07, 0.43, Z]],
  ['upperarm_L', 'shoulder_L', [0.125, 0.415, Z]],
  ['forearm_L', 'upperarm_L', [0.165, 0.34, Z]],
  ['hand_L', 'forearm_L', [0.205, 0.285, Z]],
  ['shoulder_R', 'chest', [-0.07, 0.43, Z]],
  ['upperarm_R', 'shoulder_R', [-0.125, 0.415, Z]],
  ['forearm_R', 'upperarm_R', [-0.165, 0.34, Z]],
  ['hand_R', 'forearm_R', [-0.205, 0.285, Z]],
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
  'shoulder_L': [0.125, 0.415, Z], 'upperarm_L': [0.165, 0.34, Z], 'forearm_L': [0.205, 0.285, Z], 'hand_L': [0.24, 0.215, Z],
  'shoulder_R': [-0.125, 0.415, Z], 'upperarm_R': [-0.165, 0.34, Z], 'forearm_R': [-0.205, 0.285, Z], 'hand_R': [-0.24, 0.215, Z],
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
// arm / torso separation line measured from cross-sections (arm is a separate blob below y 0.33)
const sep = (y) => (y < 0.33 ? 0.113 + (0.33 - y) * 0.6 : 0.113 + (y - 0.33) * 0.2);
function allowed(x, y) {
  const ax = Math.abs(x), side = x >= 0 ? 'L' : 'R';
  if (y > 0.49) return ['head'];
  if (y > 0.455) return ['neck', 'head', 'chest'];
  if (y < 0.35 && y > 0.18 && ax > sep(y)) return [`upperarm_${side}`, `forearm_${side}`, `hand_${side}`];
  if (y >= 0.35 && y < 0.44 && ax > sep(y)) return [`upperarm_${side}`, `shoulder_${side}`, 'chest'];
  if (y > 0.35) return ['chest', 'spine', `shoulder_${side}`, 'neck'];
  if (y > 0.25) return ['spine', 'hips', 'chest', `thigh_${side}`];
  return ['hips', `thigh_${side}`, `shin_${side}`, `foot_${side}`];
}
const nb = B.length;
let W = new Float32Array(N * nb);
for (let v = 0; v < N; v++) {
  const p = [P[3 * v], P[3 * v + 1], P[3 * v + 2]];
  const names = allowed(p[0], p[1]);
  let s = 0;
  for (const n of names) {
    const i = idxOf[n];
    const d = segDist(p, B[i][2], TAIL[n]) + 0.004;
    const w = 1 / Math.pow(d, 6);
    W[v * nb + i] = w; s += w;
  }
  for (const n of names) W[v * nb + idxOf[n]] /= s;
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
    const ok = allowed(P[3 * v], P[3 * v + 1]).map((n) => idxOf[n]);
    let tot = 0; for (let k = 0; k < nb; k++) { if (!ok.includes(k)) W2[v * nb + k] = 0; tot += W2[v * nb + k]; }
    if (tot > 0) for (let k = 0; k < nb; k++) W2[v * nb + k] /= tot;
  }
  W = W2;
}
// unify weights of coincident vertices so UV seams never open under deformation
{
  const key = (v) => `${Math.round(P[3*v]*1e5)},${Math.round(P[3*v+1]*1e5)},${Math.round(P[3*v+2]*1e5)}`;
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
const FEATURES = [[-0.092, 0.61], [0.09, 0.61], [0.0, 0.549], [0.1, 0.685], [-0.1, 0.685]]; // eye L(screen-left), eye R, mouth
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
const EYES = [[-0.092, 0.61, 0.045, 0.042], [0.09, 0.61, 0.045, 0.042]];
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
  const inM = (v) => { const x = P[3*v], y = P[3*v+1], z = P[3*v+2]; return z > 0.15 && ((x / 0.036) ** 2 + ((y - 0.549) / 0.013) ** 2) < 1; };
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
  const near = (v) => { const x = P[3*v], y = P[3*v+1], z = P[3*v+2]; return z > 0.14 && ((x / 0.05) ** 2 + ((y - 0.549) / 0.025) ** 2) < 1; };
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

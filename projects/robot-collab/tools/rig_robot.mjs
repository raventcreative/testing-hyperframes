// AI PRENEUR ROBOT — rig for the client's Tripo robot (one shell: helmet+collar+body, plus two floating hands).
// Bones: rig_root > body (whole shell, hover/lean) > head (helmet, soft blend over the collar seam), hand_L / hand_R (rigid, float freely).
// Adds _FACE (vec3: s, t, w) = visor screen coordinates (eye centres at s = ±1, t = 0) + visor weight, used by the runtime's screen-face shader.
// Usage: node rig_robot.mjs <in_tex.glb> <out_rigged.glb>
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
const [src, out] = process.argv.slice(2);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS);
const doc = await io.read(src);
const root = doc.getRoot();
const prim = root.listMeshes()[0].listPrimitives()[0];
const P = prim.getAttribute('POSITION').getArray(), NR = prim.getAttribute('NORMAL').getArray();
const IDX = prim.getIndices().getArray(); const N = P.length / 3;
// connected components over welded positions (hands are separate pieces)
const key = (v) => `${Math.round(P[3*v]*1e5)},${Math.round(P[3*v+1]*1e5)},${Math.round(P[3*v+2]*1e5)}`;
const par = new Int32Array(N).map((_, i) => i);
const find = (a) => { while (par[a] !== a) { par[a] = par[par[a]]; a = par[a]; } return a; };
const uni = (a, b) => { a = find(a); b = find(b); if (a !== b) par[a] = b; };
const seen = new Map(); for (let v = 0; v < N; v++) { const k = key(v); if (seen.has(k)) uni(v, seen.get(k)); else seen.set(k, v); }
for (let i = 0; i < IDX.length; i += 3) { uni(IDX[i], IDX[i+1]); uni(IDX[i+1], IDX[i+2]); }
const comps = new Map(); for (let v = 0; v < N; v++) { const r = find(v); if (!comps.has(r)) comps.set(r, []); comps.get(r).push(v); }
const list = [...comps.values()].sort((a, b) => b.length - a.length);
const main = list[0]; const hands = list.slice(1, 3);
const cen = (vs) => { let x = 0, y = 0, z = 0; for (const v of vs) { x += P[3*v]; y += P[3*v+1]; z += P[3*v+2]; } return [x / vs.length, y / vs.length, z / vs.length]; };
const hc = hands.map(cen); const iL = hc[0][0] > hc[1][0] ? 0 : 1;   // +x = character's LEFT
const handL = hands[iL], handR = hands[1 - iL]; const cL = hc[iL], cR = hc[1 - iL];
console.log('main', main.length, 'hand_L', handL.length, cL.map((a) => a.toFixed(3)), 'hand_R', handR.length, cR.map((a) => a.toFixed(3)));
const B = [
  ['body', null, [0.02, 0.36, 0.0]],
  ['head', 'body', [0.02, 0.50, 0.0]],
  ['hand_L', 'body', cL],
  ['hand_R', 'body', cR],
];
const ix = Object.fromEntries(B.map((b, i) => [b[0], i]));
const J = new Uint16Array(N * 4), W = new Float32Array(N * 4);
const ss = (a, b, x) => { const t = Math.max(0, Math.min(1, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
const isMain = new Uint8Array(N); for (const v of main) isMain[v] = 1;
for (const v of handL) { J[4*v] = ix.hand_L; W[4*v] = 1; }
for (const v of handR) { J[4*v] = ix.hand_R; W[4*v] = 1; }
let headN = 0;
for (const v of main) {
  const x = P[3*v], y = P[3*v+1];
  let wh = ss(0.455, 0.555, y);
  if (y < 0.58) wh *= 1 - ss(0.32, 0.40, Math.abs(x - 0.02));     // collar wings stay with the body
  J[4*v] = ix.body; J[4*v+1] = ix.head; W[4*v] = 1 - wh; W[4*v+1] = wh; if (wh > 0.5) headN++;
}
console.log('head-weighted verts', headN);
// visor screen coordinates
const O = [0.0879, 0.6297, 0.2443], R = [0.966, 0.125, -0.225], U = [-0.111, 0.991, 0.076], D = 0.0935;
const F = new Float32Array(N * 3); let vis = 0;
for (let v = 0; v < N; v++) {
  if (!isMain[v]) continue;
  const x = P[3*v], y = P[3*v+1], z = P[3*v+2];
  const q = [x - O[0], y - O[1], z - O[2]];
  F[3*v] = (q[0]*R[0] + q[1]*R[1] + q[2]*R[2]) / D; F[3*v+1] = (q[0]*U[0] + q[1]*U[1] + q[2]*U[2]) / D;
  const ell = ((x - 0.078) / 0.27) ** 2 + ((y - 0.647) / 0.18) ** 2;
  const w = z > 0.1 && NR[3*v+2] > 0.0 ? 1 - ss(0.80, 1.0, ell) : 0;
  F[3*v+2] = w; if (w > 0.5) vis++;
}
console.log('visor verts', vis);
const buf = root.listBuffers()[0];
const joints = B.map(([name]) => doc.createNode(name));
B.forEach(([, p, pos], i) => { const pp = p ? B[ix[p]][2] : [0, 0, 0]; joints[i].setTranslation([pos[0] - pp[0], pos[1] - pp[1], pos[2] - pp[2]]); if (p) joints[ix[p]].addChild(joints[i]); });
const rigRoot = doc.createNode('rig_root'); rigRoot.addChild(joints[0]);
const ibm = new Float32Array(16 * B.length);
B.forEach(([, , pos], i) => ibm.set([1,0,0,0, 0,1,0,0, 0,0,1,0, -pos[0],-pos[1],-pos[2],1], 16 * i));
const skin = doc.createSkin('robot_skin').setSkeleton(joints[0]).setInverseBindMatrices(doc.createAccessor('ibm').setType('MAT4').setArray(ibm).setBuffer(buf));
joints.forEach((j) => skin.addJoint(j));
prim.setAttribute('JOINTS_0', doc.createAccessor('joints').setType('VEC4').setArray(J).setBuffer(buf));
prim.setAttribute('WEIGHTS_0', doc.createAccessor('weights').setType('VEC4').setArray(W).setBuffer(buf));
prim.setAttribute('_FACE', doc.createAccessor('face').setType('VEC3').setArray(F).setBuffer(buf));
const meshNode = root.listNodes().find((n) => n.getMesh());
meshNode.setSkin(skin).setName('robot_mesh').setTranslation([0, 0, 0]);
root.listScenes()[0].addChild(rigRoot);
await io.write(out, doc);
console.log('wrote', out);

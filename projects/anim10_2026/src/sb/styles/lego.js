// LEGO: the robot rebuilt from bricks. The rest-pose mesh is voxelised per bone group (surface samples -> exterior
// flood fill), cells are merged into 1x1..1x4 bricks (direction alternating per layer, running bond), only exposed faces
// are emitted, with procedural bevels + seams; studs are instanced. Colours come from the robot's surface classes,
// quantised to a toy palette (white, black, dark bluish grey, trans-light-blue lights). The visor is one smooth
// trans-black "windscreen" element with printed glowing eyes; the wordmark is a printed 1x8 tile on the collar.
// Brick groups are attached rigidly to body / head / hands, so every pose still works. The set is brick-built too
// (seams + studs), standing on a studded baseplate; glossy ABS under soft studio light, slight macro depth of field.
import * as THREE from 'three';
import { makeRT, Pass, Blur, lc, FACE } from '../common.js';
import { PAL, NPAL, LAYOUT } from '../set.js';
import { litSetMaterial, makeEnv } from '../lit.js';

const S = 0.036, HH = S * 1.2;       // stud pitch, brick height
const STUD_R = S * 0.3, STUD_H = S * 0.2;
// toy palette (sRGB): white, black, dark bluish grey, trans-light-blue (lit), visor (unused: smooth piece)
const BRICK = [0xf2f3f2, 0x1b2a34, 0x6c6e68, 0x6fd3ff];
const VIS = { O: [0.0879, 0.6297, 0.2443], R: [0.966, 0.125, -0.225], U: [-0.111, 0.991, 0.076], D: 0.0935 };

// ------------------------------------------------------------------ voxelisation of the robot (rest pose)
function voxelize(geo) {
  const A = geo.attributes, idx = geo.index.array, n = A.position.count;
  const P = new Float32Array(n * 3), N = new Float32Array(n * 3), CL = new Float32Array(n * 3), B = new Uint8Array(n);
  for (let i = 0; i < n; i++) {
    P[3 * i] = A.position.getX(i); P[3 * i + 1] = A.position.getY(i); P[3 * i + 2] = A.position.getZ(i);
    N[3 * i] = A.normal.getX(i); N[3 * i + 1] = A.normal.getY(i); N[3 * i + 2] = A.normal.getZ(i);
    CL[3 * i] = A.aCls.getX(i); CL[3 * i + 1] = A.aCls.getY(i); CL[3 * i + 2] = A.aCls.getZ(i);
    B[i] = A.skinWeight.getY(i) > A.skinWeight.getX(i) ? A.skinIndex.getY(i) : A.skinIndex.getX(i);
  }
  const X0 = Math.floor(-0.56 / S), Z0 = Math.floor(-0.34 / S), NX = Math.ceil(0.56 / S) - X0 + 1, NY = Math.ceil(0.96 / HH) + 1, NZ = Math.ceil(0.34 / S) - Z0 + 1;
  const NC = NX * NY * NZ, G = 4;
  const cnt = new Uint16Array(G * NC * 4);              // class counts per cell: white, dark, blue, visor
  const cid = (x, y, z) => (y * NZ + z) * NX + x;
  for (let t = 0; t < idx.length; t += 3) {
    const a = idx[t], b = idx[t + 1], c = idx[t + 2], g = B[a];
    const ax = P[3 * a], ay = P[3 * a + 1], az = P[3 * a + 2];
    const ex = P[3 * b] - ax, ey = P[3 * b + 1] - ay, ez = P[3 * b + 2] - az, fx = P[3 * c] - ax, fy = P[3 * c + 1] - ay, fz = P[3 * c + 2] - az;
    const area = 0.5 * Math.hypot(ey * fz - ez * fy, ez * fx - ex * fz, ex * fy - ey * fx);
    const ns = Math.max(1, Math.min(48, Math.ceil(area / (S * S * 0.06))));
    for (let k = 0; k < ns; k++) {
      let r1 = (k * 0.6180339 + 0.13) % 1, r2 = (k * 0.7548777 + 0.37) % 1; if (r1 + r2 > 1) { r1 = 1 - r1; r2 = 1 - r2; }
      const w0 = 1 - r1 - r2;
      const x = ax + ex * r1 + fx * r2, y = ay + ey * r1 + fy * r2, z = az + ez * r1 + fz * r2;
      const nz = N[3 * a + 2] * w0 + N[3 * b + 2] * r1 + N[3 * c + 2] * r2;
      const cw = CL[3 * a] * w0 + CL[3 * b] * r1 + CL[3 * c] * r2, cb = CL[3 * a + 1] * w0 + CL[3 * b + 1] * r1 + CL[3 * c + 1] * r2;
      const ell = ((x - 0.078) / 0.27) ** 2 + ((y - 0.647) / 0.18) ** 2, front = z > 0.1 && nz > 0;
      let cls = cw > 0.5 || (front && ell < 1.6) ? 0 : 1; if (cb > 0.42) cls = 2; if (front && ell < 1.2 && g === 1) cls = 3;
      const ix = Math.floor(x / S) - X0, iy = Math.floor(y / HH), iz = Math.floor(z / S) - Z0;
      if (ix < 0 || iy < 0 || iz < 0 || ix >= NX || iy >= NY || iz >= NZ) continue;
      const o = (g * NC + cid(ix, iy, iz)) * 4 + cls; if (cnt[o] < 65000) cnt[o]++;
    }
  }
  // occupancy (visor cells stay open: the smooth visor element fills that hole), exterior flood fill per group
  const groups = [];
  for (let g = 0; g < G; g++) {
    const occ = new Uint8Array(NC), col = new Int8Array(NC).fill(-1);
    for (let i = 0; i < NC; i++) {
      const o = (g * NC + i) * 4, w = cnt[o], d = cnt[o + 1], bl = cnt[o + 2], v = cnt[o + 3], tot = w + d + bl + v;
      if (tot < 2 || v > (w + d + bl) * 0.7) continue;
      occ[i] = 1; col[i] = bl > (w + d) * 0.35 ? 3 : (w >= d * (g >= 2 ? 0.55 : 1) ? 0 : 1);
    }
    const ext = new Uint8Array(NC), q = [];
    for (let y = 0; y < NY; y++) for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++)
      if ((x === 0 || y === 0 || z === 0 || x === NX - 1 || y === NY - 1 || z === NZ - 1) && !occ[cid(x, y, z)]) { ext[cid(x, y, z)] = 1; q.push(x, y, z); }
    for (let h = 0; h < q.length; h += 3) {
      const x = q[h], y = q[h + 1], z = q[h + 2];
      for (const [dx, dy, dz] of [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]) {
        const X = x + dx, Y = y + dy, Z = z + dz; if (X < 0 || Y < 0 || Z < 0 || X >= NX || Y >= NY || Z >= NZ) continue;
        const k = cid(X, Y, Z); if (ext[k] || occ[k]) continue; ext[k] = 1; q.push(X, Y, Z);
      }
    }
    // interior (enclosed) cells are solid black
    for (let i = 0; i < NC; i++) if (!occ[i] && !ext[i]) { occ[i] = 1; col[i] = 1; }
    // cleanup: drop lone bricks sticking out (<= 1 solid face neighbour), fill pits (>= 4 solid face neighbours)
    const N6 = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]];
    const nb = (x, y, z, f) => { let c = 0; for (const [dx, dy, dz] of N6) { const X = x + dx, Y = y + dy, Z = z + dz; if (X < 0 || Y < 0 || Z < 0 || X >= NX || Y >= NY || Z >= NZ) continue; if (f(cid(X, Y, Z))) c++; } return c; };
    for (let pass = 0; pass < 2; pass++) {
      const rem = [], add = [];
      for (let y = 0; y < NY; y++) for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++) {
        const k = cid(x, y, z);
        if (occ[k] && nb(x, y, z, (j) => ext[j]) > 0 && nb(x, y, z, (j) => occ[j]) <= 1) rem.push(k);
        else if (ext[k] && nb(x, y, z, (j) => occ[j]) >= 4) {
          const cc = [0, 0, 0, 0]; for (const [dx, dy, dz] of N6) { const X = x + dx, Y = y + dy, Z = z + dz; if (X < 0 || Y < 0 || Z < 0 || X >= NX || Y >= NY || Z >= NZ) continue; const j = cid(X, Y, Z); if (occ[j] && col[j] >= 0) cc[col[j]]++; }
          add.push([k, cc.indexOf(Math.max(...cc))]);
        }
      }
      for (const k of rem) { occ[k] = 0; ext[k] = 1; col[k] = -1; }
      for (const [k, c] of add) { occ[k] = 1; ext[k] = 0; col[k] = c; }
    }
    groups.push({ occ, col, ext });
  }
  return { groups, NX, NY, NZ, X0, Z0, cid };
}

// merge cells into bricks, emit exposed faces (+ seams / bevel data) and stud positions
function buildBricks(vox, g) {
  const { NX, NY, NZ, X0, Z0, cid } = vox, { occ, col } = vox.groups[g];
  const bid = new Int32Array(NX * NY * NZ).fill(-1); let nb = 0;
  for (let y = 0; y < NY; y++) {
    const alongX = y % 2 === 0;
    const L1 = alongX ? NZ : NX, L2 = alongX ? NX : NZ;
    for (let a = 0; a < L1; a++) {
      let run = [];
      const flush = () => {
        // split a run into bricks of 4/3/2/1 with a running-bond offset on odd rows
        let i = 0, first = (y >> 1) % 2 === 1 && run.length > 2 ? 2 : 0;
        while (i < run.length) {
          let len = first || Math.min(4, run.length - i); first = 0;
          if (run.length - i - len === 1 && len > 2) len -= 1;
          for (let k = 0; k < len; k++) bid[run[i + k]] = nb;
          nb++; i += len;
        }
        run = [];
      };
      let prev = -2;
      for (let b = 0; b < L2; b++) {
        const x = alongX ? b : a, z = alongX ? a : b, k = cid(x, y, z);
        if (occ[k] && col[k] === prev) run.push(k);
        else { flush(); if (occ[k]) run.push(k); }
        prev = occ[k] ? col[k] : -2;
      }
      flush();
    }
  }
  const pos = [], nor = [], colr = [], luv = [], seam = [], t1 = [], t2 = [], studs = [];
  const ext = vox.groups[g].ext;
  const isExt = (x, y, z) => (x < 0 || y < 0 || z < 0 || x >= NX || y >= NY || z >= NZ) ? true : !!ext[cid(x, y, z)];
  const sameB = (k, x, y, z) => (x < 0 || y < 0 || z < 0 || x >= NX || y >= NY || z >= NZ) ? false : bid[cid(x, y, z)] === bid[k];
  const dirs = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]];
  const tang = (d) => (d[1] !== 0 ? [[1, 0, 0], [0, 0, 1]] : d[0] !== 0 ? [[0, 0, 1], [0, 1, 0]] : [[1, 0, 0], [0, 1, 0]]);
  const cols = BRICK.map((h) => lc(h));
  for (let y = 0; y < NY; y++) for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++) {
    const k = cid(x, y, z); if (!occ[k]) continue;
    const c = cols[col[k]];
    const cx = (x + X0 + 0.5) * S, cy = (y + 0.5) * HH, cz = (z + Z0 + 0.5) * S;
    for (const d of dirs) {
      if (!isExt(x + d[0], y + d[1], z + d[2])) continue;
      const [T1, T2] = tang(d);
      const half = [S / 2, HH / 2, S / 2];
      const fc = [cx + d[0] * half[0], cy + d[1] * half[1], cz + d[2] * half[2]];
      const e1 = T1.map((v, i) => v * half[i]), e2 = T2.map((v, i) => v * half[i]);
      // seams on the 4 edges: neighbour along -T1, +T1, -T2, +T2 belongs to another brick (or is empty)
      const sm = [!sameB(k, x - T1[0], y - T1[1], z - T1[2]), !sameB(k, x + T1[0], y + T1[1], z + T1[2]), !sameB(k, x - T2[0], y - T2[1], z - T2[2]), !sameB(k, x + T2[0], y + T2[1], z + T2[2])].map(Number);
      const corners = [[-1, -1], [1, -1], [1, 1], [-1, 1]];
      const V = corners.map(([u, v]) => [fc[0] + e1[0] * u + e2[0] * v, fc[1] + e1[1] * u + e2[1] * v, fc[2] + e1[2] * u + e2[2] * v]);
      // winding: (V0,V1,V2) normal should equal d
      const cr = [(V[1][1] - V[0][1]) * (V[2][2] - V[0][2]) - (V[1][2] - V[0][2]) * (V[2][1] - V[0][1]), (V[1][2] - V[0][2]) * (V[2][0] - V[0][0]) - (V[1][0] - V[0][0]) * (V[2][2] - V[0][2]), (V[1][0] - V[0][0]) * (V[2][1] - V[0][1]) - (V[1][1] - V[0][1]) * (V[2][0] - V[0][0])];
      const flip = cr[0] * d[0] + cr[1] * d[1] + cr[2] * d[2] < 0;
      const order = flip ? [0, 2, 1, 0, 3, 2] : [0, 1, 2, 0, 2, 3];
      for (const o of order) {
        pos.push(...V[o]); nor.push(...d); colr.push(c.r, c.g, c.b);
        luv.push((corners[o][0] + 1) / 2, (corners[o][1] + 1) / 2); seam.push(...sm); t1.push(...T1); t2.push(...T2);
      }
      if (d[1] === 1) studs.push([cx, (y + 1) * HH, cz, col[k]]);
    }
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); geo.setAttribute('normal', new THREE.Float32BufferAttribute(nor, 3));
  geo.setAttribute('color', new THREE.Float32BufferAttribute(colr, 3)); geo.setAttribute('aLuv', new THREE.Float32BufferAttribute(luv, 2));
  geo.setAttribute('aSeam', new THREE.Float32BufferAttribute(seam, 4)); geo.setAttribute('aT1', new THREE.Float32BufferAttribute(t1, 3)); geo.setAttribute('aT2', new THREE.Float32BufferAttribute(t2, 3));
  return { geo, studs };
}

// ABS plastic: physical material + vertex colours + procedural bevels / seams; glowing trans-blue bricks
function brickMaterial() {
  const m = new THREE.MeshPhysicalMaterial({ vertexColors: true, roughness: 0.3, metalness: 0, clearcoat: 0.35, clearcoatRoughness: 0.18 });
  m.onBeforeCompile = (sh) => {
    sh.vertexShader = sh.vertexShader
      .replace('#include <common>', '#include <common>\nattribute vec2 aLuv; attribute vec4 aSeam; attribute vec3 aT1; attribute vec3 aT2;\nvarying vec2 vLuv; varying vec4 vSeam; varying vec3 vT1; varying vec3 vT2;')
      .replace('#include <begin_vertex>', '#include <begin_vertex>\nvLuv = aLuv; vSeam = aSeam; vT1 = normalize(mat3(modelViewMatrix) * aT1); vT2 = normalize(mat3(modelViewMatrix) * aT2);');
    sh.fragmentShader = sh.fragmentShader
      .replace('#include <common>', '#include <common>\nvarying vec2 vLuv; varying vec4 vSeam; varying vec3 vT1; varying vec3 vT2;')
      .replace('#include <normal_fragment_maps>', `#include <normal_fragment_maps>
        float bw = 0.09;
        float e0 = vSeam.x * (1.0 - smoothstep(0.0, bw, vLuv.x)), e1 = vSeam.y * (1.0 - smoothstep(0.0, bw, 1.0 - vLuv.x));
        float e2 = vSeam.z * (1.0 - smoothstep(0.0, bw * 0.8, vLuv.y)), e3 = vSeam.w * (1.0 - smoothstep(0.0, bw * 0.8, 1.0 - vLuv.y));
        normal = normalize(normal + (vT1 * (e1 - e0) + vT2 * (e3 - e2)) * 1.1);
        float groove = max(max(vSeam.x * (1.0 - smoothstep(0.0, 0.022, vLuv.x)), vSeam.y * (1.0 - smoothstep(0.0, 0.022, 1.0 - vLuv.x))),
                           max(vSeam.z * (1.0 - smoothstep(0.0, 0.02, vLuv.y)), vSeam.w * (1.0 - smoothstep(0.0, 0.02, 1.0 - vLuv.y))));`)
      .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
        diffuseColor.rgb *= 1.0 - 0.75 * groove;
        float isBlue = step(0.8, vColor.b) * step(vColor.r, 0.4);
        totalEmissiveRadiance += vColor.rgb * isBlue * 0.9;`);
  };
  m.customProgramCacheKey = () => 'sb-lego-brick';
  return m;
}
function studMaterial() {
  const m = new THREE.MeshPhysicalMaterial({ roughness: 0.3, metalness: 0, clearcoat: 0.35, clearcoatRoughness: 0.18 });
  m.onBeforeCompile = (sh) => {
    sh.fragmentShader = sh.fragmentShader.replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
      #ifdef USE_INSTANCING_COLOR
      float isBlue = step(0.8, vColor.b) * step(vColor.r, 0.4); totalEmissiveRadiance += vColor.rgb * isBlue * 0.9;
      #endif`);
  };
  m.customProgramCacheKey = () => 'sb-lego-stud';
  return m;
}
function studGeometry(seg) {
  const g = new THREE.CylinderGeometry(STUD_R, STUD_R, STUD_H, seg, 1, false); g.translate(0, STUD_H / 2, 0);
  // bevel ring on the top edge
  const pos = g.attributes.position;
  for (let i = 0; i < pos.count; i++) if (pos.getY(i) > STUD_H * 0.99) { pos.setX(i, pos.getX(i) * 0.93); pos.setZ(i, pos.getZ(i) * 0.93); }
  g.computeVertexNormals(); return g;
}
function makeStuds(list, geo, mat, cols) {
  const m = new THREE.InstancedMesh(geo, mat, Math.max(1, list.length));
  const mt = new THREE.Matrix4(), c = new THREE.Color();
  list.forEach((s, i) => { mt.makeTranslation(s[0], s[1], s[2]); m.setMatrixAt(i, mt); c.copy(typeof s[3] === 'number' ? cols[s[3]] : s[3]); m.setColorAt(i, c); });
  m.count = list.length; m.castShadow = true; m.receiveShadow = true; m.frustumCulled = false;
  m.instanceMatrix.needsUpdate = true; if (m.instanceColor) m.instanceColor.needsUpdate = true;
  return m;
}

// LEGO palette for the set (sRGB)
const SETCOL = {
  floor: 0xa0a5a9, wall: 0xe4cd9e, trim: 0x958a73, deskTop: 0x582a12, deskBody: 0xa0a5a9, monitor: 0x1b2a34, screen: 0x0d69ab,
  bar1: 0x4b9f4a, bar2: 0xf2cd37, bar3: 0xc91a09, bar4: 0x0055bf, board: 0xf4f4f0, boardFrame: 0x0a3463, leaf: 0x4b9f4a, pot: 0xa0522d,
  winFrame: 0xf4f4f0, sky: 0x9fd6f5, city: 0x9fd6f5, clock: 0xf4f4f0, clockHand: 0x1b2a34, keyboard: 0x6c6e68, mug: 0xc91a09, axis: 0x1b2a34, soil: 0x352100,
};

const COMP = /* glsl */ `
uniform sampler2D tC; uniform sampler2D tD; uniform sampler2D tDof; uniform vec2 uNF; uniform float uFocus; uniform vec2 uRes;
varying vec2 vUv;
float viewZ(float d) { return uNF.x * uNF.y / ((uNF.y - uNF.x) * d - uNF.y); }
vec3 filmic(vec3 x) { return clamp((x * (2.51 * x + 0.03)) / (x * (2.43 * x + 0.59) + 0.14), 0.0, 1.0); }
void main() {
  vec3 c = texture2D(tC, vUv).rgb;
  float z = -viewZ(texture2D(tD, vUv).r);
  float coc = 0.85 * smoothstep(0.1, 0.8, clamp(abs(1.0 / uFocus - 1.0 / z) * uFocus * 1.5, 0.0, 1.0));
  c = mix(c, texture2D(tDof, vUv).rgb, coc);
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
  // ---- robot bricks (rest space, one group per bone)
  const vox = voxelize(rig.mesh.geometry);
  const bones = rig.mesh.skeleton.bones, inv = rig.mesh.skeleton.boneInverses;
  const bmat = brickMaterial(), smat = studMaterial(), studGeo = studGeometry(12), studGeoLo = studGeometry(8);
  const brickCols = BRICK.map((h) => lc(h));
  const groups = [];
  for (let g = 0; g < 4; g++) {
    const { geo, studs } = buildBricks(vox, g);
    const grp = new THREE.Group(); grp.matrixAutoUpdate = false;
    const mesh = new THREE.Mesh(geo, bmat); mesh.castShadow = true; mesh.receiveShadow = true; grp.add(mesh);
    grp.add(makeStuds(studs, studGeo, smat, brickCols));
    scene.add(grp); groups.push(grp);
  }
  // printed 1x8 tile with the wordmark on the collar front (body group)
  {
    const tw = 8 * S, th = S * 0.95, logo = rig.logoTex;
    const tileMat = new THREE.MeshPhysicalMaterial({ color: lc(0xf2f3f2), roughness: 0.22, clearcoat: 0.5, clearcoatRoughness: 0.1 });
    const tm = tileMat.clone(); tm.map = logo;
    tm.onBeforeCompile = (sh) => {
      sh.fragmentShader = sh.fragmentShader.replace('#include <map_fragment>', `
          vec2 lu = (vMapUv - vec2(0.06, 0.2)) / vec2(0.88, 0.6);
          float a = (lu.x > 0.0 && lu.x < 1.0 && lu.y > 0.0 && lu.y < 1.0) ? texture2D(map, vec2(lu.x, 1.0 - lu.y)).a : 0.0;
          diffuseColor.rgb = mix(diffuseColor.rgb, vec3(0.012, 0.014, 0.03), a);`);
    };
    tm.customProgramCacheKey = () => 'sb-lego-tile';
    const tile = new THREE.Mesh(new THREE.BoxGeometry(tw, th, S * 0.3), tileMat);
    const print = new THREE.Mesh(new THREE.PlaneGeometry(tw * 0.985, th * 0.97), tm); print.position.z = S * 0.151; tile.add(print);
    // in front of the collar's front-most cells at the logo height
    const { NX, NZ, X0, Z0, cid, groups: G } = vox; const iy = Math.floor(0.385 / HH); let zmax = 0;
    for (let z = 0; z < NZ; z++) for (let x = 0; x < NX; x++) { const xx = (x + X0 + 0.5) * S; if (Math.abs(xx - 0.02) < 0.12 && G[0].occ[cid(x, iy, z)] && !G[0].ext[cid(x, iy, z)]) zmax = Math.max(zmax, (z + Z0 + 1) * S); }
    tile.position.set(0.02, (iy + 0.5) * HH, zmax + S * 0.15); tile.castShadow = true;
    groups[0].add(tile);
  }
  // smooth trans-black visor element with printed glowing eyes (skinned: follows the head)
  const visMat = new THREE.MeshPhysicalMaterial({ color: lc(0x10131c), roughness: 0.06, metalness: 0, clearcoat: 1, clearcoatRoughness: 0.04, emissive: 0xffffff, emissiveIntensity: 1 });
  visMat.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, rig.shared.faceU);
    sh.vertexShader = sh.vertexShader.replace('#include <common>', '#include <common>\nattribute vec3 _face;\nvarying vec3 vFace;\nvarying vec3 vRP;')
      .replace('#include <begin_vertex>', '#include <begin_vertex>\nvFace = _face; vRP = position;');
    sh.fragmentShader = sh.fragmentShader.replace('#include <common>', '#include <common>\nvarying vec3 vFace;\nvarying vec3 vRP;\n' + FACE)
      .replace('#include <clipping_planes_fragment>', `#include <clipping_planes_fragment>
        float ellV = pow((vRP.x - 0.078) / 0.27, 2.0) + pow((vRP.y - 0.647) / 0.18, 2.0);
        if (ellV > 1.32 || vRP.z < 0.08) discard;`)
      .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
        float fa = vFace.z > 0.01 ? screenFace(vFace.xy) * smoothstep(0.2, 0.6, vFace.z) : 0.0;
        diffuseColor.rgb = mix(diffuseColor.rgb, vec3(0.9, 0.97, 1.0), fa);
        totalEmissiveRadiance = vec3(0.55, 0.85, 1.0) * fa * 1.6 * uEyeGlow;`);
  };
  visMat.customProgramCacheKey = () => 'sb-lego-visor';
  const visor = ctx.robotMesh(visMat); visor.castShadow = false; scene.add(visor);
  // ---- brick-built set: palette colours, brick seams + bevels from world position, studs on top faces
  const cols = [], rm = [];
  for (let i = 0; i < NPAL; i++) { const name = Object.keys(PAL).find((k) => PAL[k] === i); cols.push(lc(SETCOL[name] ?? 0xa0a5a9)); rm.push([name === 'sky' ? 1 : 0.3, 0]); }
  const em = cols.map(() => new THREE.Color(0, 0, 0)); em[PAL.sky] = lc(0x9fd6f5).multiplyScalar(0.9); em[PAL.city] = em[PAL.sky].clone(); em[PAL.screen] = lc(0x0d69ab).multiplyScalar(0.5);
  const setMat = litSetMaterial({ cols, rm, em, physical: true, key: 'lego', phys: { clearcoat: 0.3, clearcoatRoughness: 0.2 }, hooks: {
    pars: `const float BS = ${S.toFixed(4)}, BH = ${HH.toFixed(4)};\nfloat gSeam = 0.0;\n`,
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
      }`,
    albedo: /* glsl */ `
      if (vPal == ${PAL.wall}) { float row = floor(vWPos.y / BH); float bi = floor((vWPos.x + mod(row, 2.0) * 2.0 * BS) / (4.0 * BS));
        float hb = h12(vec2(bi, row)); diffuseColor.rgb *= 0.97 + 0.05 * hb; if (hb > 0.9 && vWPos.y > 0.1) diffuseColor.rgb = vec3(0.29, 0.24, 0.16); }`,
    emissive: `diffuseColor.rgb *= 1.0 - 0.7 * gSeam; totalEmissiveRadiance *= 1.0 - 0.6 * gSeam;`,
  } });
  const setMesh = new THREE.Mesh(ctx.setGeo.sharp, setMat); setMesh.receiveShadow = true; setMesh.castShadow = true; scene.add(setMesh);
  // studs: baseplate (around the robot), desk top, window sill, board top, monitor top
  const studList = [], base = lc(SETCOL.floor);
  for (let x = -1.7; x <= 1.7; x += S) for (let z = -1.25; z <= 1.1; z += S) {
    const xx = Math.round(x / S) * S + S / 2, zz = Math.round(z / S) * S + S / 2;
    const D = LAYOUT.desk, P = LAYOUT.plant, B = LAYOUT.board;
    if (Math.abs(xx - D.x) < D.w / 2 && Math.abs(zz - D.z) < D.d / 2) continue;
    if (Math.hypot(xx - P.x, zz - P.z) < 0.13) continue;
    studList.push([xx, 0, zz, base]);
  }
  const addGrid = (x0, x1, z0, z1, y, col) => { for (let x = x0 + S / 2; x < x1; x += S) for (let z = z0 + S / 2; z < z1; z += S) studList.push([x, y, z, lc(col)]); };
  const D = LAYOUT.desk; addGrid(D.x - D.w / 2 + 0.02, D.x + D.w / 2 - 0.02, D.z - D.d / 2 + 0.02, D.z - 0.1, D.h, SETCOL.deskTop);
  addGrid(D.x + 0.25, D.x + D.w / 2 - 0.02, D.z - 0.1, D.z + D.d / 2 - 0.02, D.h, SETCOL.deskTop);
  const Wn = LAYOUT.win; addGrid(Wn.x0 - 0.08, Wn.x1 + 0.08, LAYOUT.wallZ + 0.0, LAYOUT.wallZ + 0.1, Wn.y0 - 0.05 + 0.003, SETCOL.winFrame);
  const Bd = LAYOUT.board; addGrid(Bd.x - Bd.w / 2 - 0.02, Bd.x + Bd.w / 2 + 0.02, Bd.z - 0.018, Bd.z + 0.018, Bd.y0 + Bd.h + 0.027, SETCOL.boardFrame);
  { const bp = makeStuds(studList, studGeoLo, smat, null); bp.castShadow = false; scene.add(bp); }
  // lights: soft studio
  scene.add(new THREE.HemisphereLight(0xffffff, 0xb8b2a8, 1.1));
  const key = new THREE.DirectionalLight(0xfff4e8, 2.6); key.position.set(-2.0, 3.6, 2.8); key.target.position.set(0, 0.4, -0.3);
  key.castShadow = true; key.shadow.mapSize.set(1024, 1024); key.shadow.bias = -0.0004; key.shadow.normalBias = 0.012;
  Object.assign(key.shadow.camera, { left: -2.0, right: 2.0, top: 2.2, bottom: -1.2, near: 0.5, far: 9 }); key.shadow.camera.updateProjectionMatrix();
  scene.add(key, key.target);
  const fill = new THREE.DirectionalLight(0xe8f0ff, 0.8); fill.position.set(2.4, 1.6, 2.2); scene.add(fill);
  // post
  const rt = makeRT(W, H, { type: THREE.HalfFloatType, samples: 4, depthTexture: true });
  const hw = Math.ceil(W / 2), hh = Math.ceil(H / 2);
  const rtH = makeRT(hw, hh, { depth: false, type: THREE.HalfFloatType });
  const down = new Pass(`uniform sampler2D tSrc; uniform vec2 uTexel; varying vec2 vUv; void main() { gl_FragColor = (texture2D(tSrc, vUv + uTexel * vec2(-1.0)) + texture2D(tSrc, vUv + uTexel) + texture2D(tSrc, vUv + uTexel * vec2(1.0, -1.0)) + texture2D(tSrc, vUv + uTexel * vec2(-1.0, 1.0))) * 0.25; }`,
    { tSrc: { value: rt.texture }, uTexel: { value: new THREE.Vector2(0.5 / W, 0.5 / H) } });
  const blur = new Blur(hw, hh, THREE.HalfFloatType);
  const comp = new Pass(COMP, { tC: { value: rt.texture }, tD: { value: rt.depthTexture }, tDof: { value: null }, uNF: { value: new THREE.Vector2() }, uFocus: { value: 4.5 }, uRes: { value: new THREE.Vector2(W, H) } });
  const tmp = new THREE.Vector3();
  return {
    render(target) {
      const r = ctx.renderer, rr = rig.rigRoot;
      const vis = ctx.robotVisible;
      for (let g = 0; g < 4; g++) { groups[g].matrix.multiplyMatrices(bones[g].matrixWorld, inv[g]); groups[g].matrixWorldNeedsUpdate = true; groups[g].visible = vis; }
      visor.visible = vis;
      r.shadowMap.needsUpdate = true;
      r.setRenderTarget(rt); r.clear(); r.render(scene, ctx.camera);
      down.render(r, rtH);
      comp.u.tDof.value = blur.run(r, rtH.texture, 1.5, 2);
      comp.u.uNF.value.set(ctx.camera.near, ctx.camera.far);
      comp.u.uFocus.value = ctx.camera.position.distanceTo(tmp.set(rr.position.x, 0.5 + rr.position.y, rr.position.z));
      comp.render(r, target);
    },
  };
}

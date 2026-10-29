import * as THREE from 'three';

// A physically-plausible sheet of paper:
//  - real thickness (front face, back face, bevelled rim strip)
//  - rounded corners and optional torn zig-zag bottom edge (receipts)
//  - inextensible bending: folds/curls are integrated along an axis so arc length
//    is preserved (paper never stretches while folding)
//  - shader-driven "regions" on the printed face: marker highlights, wipes, bar growth
//
// Deformation spec (set every frame via sheet.deform = {...}):
//   axis:  [ax, ay]   unit vector in sheet plane along which bending happens
//   anchor: s0        coordinate along axis that stays fixed (e.g. 0 = centre)
//   theta: (s) => rad bend angle profile along the axis (+ = towards camera / +z)
//   bowX, bowY        gentle cylindrical bow (z += bowX*x^2 + bowY*y^2)

const MAX_REGIONS = 12;

export class PaperSheet extends THREE.Group {
  constructor(opts) {
    super();
    this.isPaperSheet = true;
    const {
      w, h, t,
      nx = 48, ny = 96,
      radius = 0.012,
      roundBottom = true,
      zigzag = null, // { teeth, depth }
      front, back, edgeColor = '#E9E6DE',
      roughness = 0.82, roughnessMap = null, backRoughnessMap = null,
      bump = null, bumpScale = 0.6,
      paperHex = '#FBFAF7',
    } = opts;
    this.w = w; this.h = h; this.t = t;
    this.nx = nx; this.ny = ny;
    this.deform = { axis: [0, 1], anchor: 0, theta: null, bowX: 0, bowY: 0 };
    this.centroid = new THREE.Vector3(); // mean of the deformed mid-surface (visual mass centre)

    // ---------- rest-space grid ----------
    const cols = nx + 1, rows = ny + 1;
    const N = cols * rows;
    this.rest = new Float32Array(N * 2);
    const uv = new Float32Array(N * 2);
    const yTop = h / 2;
    const yBot = -h / 2;
    const zzDepth = zigzag ? zigzag.depth : 0;
    for (let j = 0; j < rows; j++) {
      for (let i = 0; i < cols; i++) {
        let x = -w / 2 + (w * i) / nx;
        let y;
        if (zigzag && j === 0) {
          y = yBot + (i % 2 === 1 ? zzDepth : 0);
        } else if (zigzag) {
          const y0 = yBot + zzDepth * 1.25;
          y = y0 + ((yTop - y0) * (j - 1)) / (ny - 1);
        } else {
          y = yBot + (h * j) / ny;
        }
        // rounded corners
        const r = radius;
        const top = y > 0;
        if (r > 0 && (top || roundBottom) && !(zigzag && !top)) {
          const cx = Math.sign(x) * (w / 2 - r);
          const cy = Math.sign(y) * (h / 2 - r);
          if (Math.abs(x) > w / 2 - r && Math.abs(y) > h / 2 - r) {
            const dx = x - cx, dy = y - cy;
            const d = Math.hypot(dx, dy);
            if (d > r) { x = cx + (dx * r) / d; y = cy + (dy * r) / d; }
          }
        }
        const k = j * cols + i;
        this.rest[k * 2] = x;
        this.rest[k * 2 + 1] = y;
        uv[k * 2] = (x + w / 2) / w;
        uv[k * 2 + 1] = (y + h / 2) / h;
      }
    }

    // ---------- faces ----------
    const idx = [];
    const idxBack = [];
    for (let j = 0; j < ny; j++) {
      for (let i = 0; i < nx; i++) {
        const a = j * cols + i, b = a + 1, c = a + cols, d = c + 1;
        idx.push(a, b, d, a, d, c);
        idxBack.push(a, d, b, a, c, d);
      }
    }
    const uvBack = new Float32Array(N * 2);
    for (let k = 0; k < N; k++) { uvBack[k * 2] = 1 - uv[k * 2]; uvBack[k * 2 + 1] = uv[k * 2 + 1]; }

    const mkGeo = (uvs, index) => {
      const g = new THREE.BufferGeometry();
      g.setAttribute('position', new THREE.BufferAttribute(new Float32Array(N * 3), 3));
      g.setAttribute('normal', new THREE.BufferAttribute(new Float32Array(N * 3), 3));
      g.setAttribute('uv', new THREE.BufferAttribute(uvs, 2));
      g.setIndex(index);
      return g;
    };
    this.gFront = mkGeo(uv, idx);
    this.gBack = mkGeo(uvBack, idxBack);

    // ---------- rim (boundary loop) ----------
    const loop = [];
    for (let i = 0; i <= nx; i++) loop.push(i);                          // bottom L->R
    for (let j = 1; j <= ny; j++) loop.push(j * cols + nx);             // right B->T
    for (let i = nx - 1; i >= 0; i--) loop.push(ny * cols + i);         // top R->L
    for (let j = ny - 1; j >= 1; j--) loop.push(j * cols);              // left T->B
    this.loop = loop;
    const L = loop.length;
    // rest-space outward normals (2D) for each loop vertex
    this.loopOut = new Float32Array(L * 2);
    for (let q = 0; q < L; q++) {
      const p0 = loop[(q - 1 + L) % L], p1 = loop[(q + 1) % L];
      let tx = this.rest[p1 * 2] - this.rest[p0 * 2];
      let ty = this.rest[p1 * 2 + 1] - this.rest[p0 * 2 + 1];
      const l = Math.hypot(tx, ty) || 1;
      tx /= l; ty /= l;
      // loop is counter-clockwise -> outward = (ty, -tx)
      this.loopOut[q * 2] = ty;
      this.loopOut[q * 2 + 1] = -tx;
    }
    const RIM_ROWS = 5;
    this.RIM_ROWS = RIM_ROWS;
    const rimN = L * RIM_ROWS;
    const gRim = new THREE.BufferGeometry();
    gRim.setAttribute('position', new THREE.BufferAttribute(new Float32Array(rimN * 3), 3));
    gRim.setAttribute('normal', new THREE.BufferAttribute(new Float32Array(rimN * 3), 3));
    const rimIdx = [];
    for (let q = 0; q < L; q++) {
      const qn = (q + 1) % L;
      for (let r = 0; r < RIM_ROWS - 1; r++) {
        const a = q * RIM_ROWS + r, b = qn * RIM_ROWS + r, c = a + 1, d = b + 1;
        rimIdx.push(a, c, b, b, c, d);
      }
    }
    gRim.setIndex(rimIdx);
    this.gRim = gRim;

    // ---------- materials ----------
    const regionUniforms = {
      uRect: { value: Array.from({ length: MAX_REGIONS }, () => new THREE.Vector4(0, 0, 0, 0)) },
      uParam: { value: Array.from({ length: MAX_REGIONS }, () => new THREE.Vector4(0, 0, 0, 0)) },
      uTint: { value: Array.from({ length: MAX_REGIONS }, () => new THREE.Color(1, 1, 1)) },
      uCount: { value: 0 },
    };
    this.regionUniforms = regionUniforms;
    this.regions = [];

    const frontMat = new THREE.MeshStandardMaterial({
      map: front, roughness, roughnessMap, metalness: 0,
      bumpMap: bump, bumpScale, envMapIntensity: 0.55,
    });
    frontMat.onBeforeCompile = (shader) => {
      Object.assign(shader.uniforms, regionUniforms);
      shader.fragmentShader = shader.fragmentShader
        .replace('#include <common>', `#include <common>
          #define MAXR ${MAX_REGIONS}
          uniform vec4 uRect[MAXR];
          uniform vec4 uParam[MAXR];
          uniform vec3 uTint[MAXR];
          uniform int uCount;`)
        .replace('#include <map_fragment>', `#include <map_fragment>
          #ifdef USE_MAP
          for (int i = 0; i < MAXR; i++) {
            if (i >= uCount) break;
            vec4 r = uRect[i];
            vec4 p = uParam[i];
            vec2 q = vMapUv;
            float inside = step(r.x, q.x) * step(q.x, r.z) * step(r.y, q.y) * step(q.y, r.w);
            if (inside < 0.5) continue;
            float mode = p.y;
            float soft = 0.0035;
            if (mode < 0.5) {
              // marker: multiply tint, wipes left -> right with a soft leading edge
              float edge = mix(r.x, r.z, p.x);
              float m = 1.0 - smoothstep(edge - soft, edge + soft, q.x);
              m *= step(0.0001, p.x);
              diffuseColor.rgb = mix(diffuseColor.rgb, diffuseColor.rgb * uTint[i], m * p.z);
            } else if (mode < 1.5) {
              // reveal left -> right (content hidden behind paper colour)
              float edge = mix(r.x, r.z, p.x);
              float m = smoothstep(edge - soft, edge + soft, q.x);
              diffuseColor.rgb = mix(diffuseColor.rgb, uTint[i], m * p.z);
            } else if (mode < 2.5) {
              // reveal bottom -> top (bar growth)
              float edge = mix(r.y, r.w, p.x);
              float m = smoothstep(edge - 0.0015, edge + 0.0015, q.y);
              diffuseColor.rgb = mix(diffuseColor.rgb, uTint[i], m * p.z);
            } else {
              // fade in
              diffuseColor.rgb = mix(uTint[i], diffuseColor.rgb, p.x);
            }
          }
          #endif`);
    };
    const backMat = new THREE.MeshStandardMaterial({
      map: back, roughness: backRoughnessMap ? 1 : roughness, roughnessMap: backRoughnessMap, metalness: 0,
      bumpMap: bump, bumpScale, envMapIntensity: 0.55,
    });
    const rimMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(edgeColor), roughness: 0.9, metalness: 0, envMapIntensity: 0.6,
    });
    this.frontMat = frontMat;
    this.backMat = backMat;
    this.rimMat = rimMat;
    this.paperColor = new THREE.Color(paperHex);

    const mk = (g, m) => {
      const mesh = new THREE.Mesh(g, m);
      mesh.castShadow = true;
      mesh.receiveShadow = true;
      mesh.frustumCulled = false;
      this.add(mesh);
      return mesh;
    };
    this.mFront = mk(this.gFront, frontMat);
    this.mBack = mk(this.gBack, backMat);
    this.mRim = mk(this.gRim, rimMat);

    this._mid = new Float32Array(N * 3);
    this._nrm = new Float32Array(N * 3);
    this.update();
  }

  // regions: [{ rect:[u0,v0,u1,v1], mode:'marker'|'wipe'|'grow'|'fade', progress, strength, tint:'#hex' }]
  setRegions(list) {
    const U = this.regionUniforms;
    const modes = { marker: 0, wipe: 1, grow: 2, fade: 3 };
    U.uCount.value = Math.min(list.length, MAX_REGIONS);
    list.slice(0, MAX_REGIONS).forEach((r, i) => {
      U.uRect.value[i].set(r.rect[0], r.rect[1], r.rect[2], r.rect[3]);
      U.uParam.value[i].set(r.progress, modes[r.mode], r.strength ?? 1, 0);
      if (r.tint) U.uTint.value[i].set(r.tint);
      else U.uTint.value[i].copy(this.paperColor);
    });
  }

  update() {
    const { w, h, t, nx, ny } = this;
    const cols = nx + 1, rows = ny + 1, N = cols * rows;
    const d = this.deform;
    const ax = d.axis[0], ay = d.axis[1];
    const px = -ay, py = ax; // perpendicular (in-plane)
    const theta = d.theta;
    const bowX = d.bowX || 0, bowY = d.bowY || 0;

    // --- integrate centreline along the bend axis ---
    const sMax = Math.abs(ax) * w / 2 + Math.abs(ay) * h / 2 + 0.01;
    const M = 1024;
    const ds = (2 * sMax) / M;
    const P = new Float64Array(M + 1), Z = new Float64Array(M + 1), TH = new Float64Array(M + 1);
    const s0 = d.anchor || 0;
    const iA = Math.round((s0 + sMax) / ds);
    for (let k = 0; k <= M; k++) TH[k] = theta ? theta(-sMax + k * ds) : 0;
    P[iA] = -sMax + iA * ds; Z[iA] = 0;
    for (let k = iA + 1; k <= M; k++) {
      const th = 0.5 * (TH[k] + TH[k - 1]);
      P[k] = P[k - 1] + Math.cos(th) * ds;
      Z[k] = Z[k - 1] + Math.sin(th) * ds;
    }
    for (let k = iA - 1; k >= 0; k--) {
      const th = 0.5 * (TH[k] + TH[k + 1]);
      P[k] = P[k + 1] - Math.cos(th) * ds;
      Z[k] = Z[k + 1] - Math.sin(th) * ds;
    }
    const sample = (s) => {
      const f = (s + sMax) / ds;
      const i = Math.max(0, Math.min(M - 1, Math.floor(f)));
      const a = f - i;
      return [P[i] + (P[i + 1] - P[i]) * a, Z[i] + (Z[i + 1] - Z[i]) * a, TH[i] + (TH[i + 1] - TH[i]) * a];
    };

    const mid = this._mid, nrm = this._nrm;
    for (let k = 0; k < N; k++) {
      const x = this.rest[k * 2], y = this.rest[k * 2 + 1];
      const s = x * ax + y * ay;
      const wv = x * px + y * py;
      const [pp, zz, th] = sample(s);
      const c = Math.cos(th), sn = Math.sin(th);
      let X = wv * px + pp * ax;
      let Y = wv * py + pp * ay;
      let Zc = zz + bowX * x * x + bowY * y * y;
      // tangent along s (3D) = (c*ax, c*ay, sn); perp = (px, py, 0)
      // normal = T_s x perp
      let nX = c * ay * 0 - sn * py;
      let nY = sn * px - c * ax * 0;
      let nZ = c * ax * py - c * ay * px;
      // bow tilt (small-angle)
      nX -= 2 * bowX * x * nZ;
      nY -= 2 * bowY * y * nZ;
      const nl = Math.hypot(nX, nY, nZ) || 1;
      mid[k * 3] = X; mid[k * 3 + 1] = Y; mid[k * 3 + 2] = Zc;
      nrm[k * 3] = nX / nl; nrm[k * 3 + 1] = nY / nl; nrm[k * 3 + 2] = nZ / nl;
    }

    let sx = 0, sy = 0, sz = 0;
    for (let k = 0; k < N; k++) { sx += mid[k * 3]; sy += mid[k * 3 + 1]; sz += mid[k * 3 + 2]; }
    this.centroid.set(sx / N, sy / N, sz / N);

    const fp = this.gFront.attributes.position.array, fn = this.gFront.attributes.normal.array;
    const bp = this.gBack.attributes.position.array, bn = this.gBack.attributes.normal.array;
    const ht = t / 2;
    for (let k = 0; k < N * 3; k += 3) {
      for (let a = 0; a < 3; a++) {
        fp[k + a] = mid[k + a] + nrm[k + a] * ht;
        bp[k + a] = mid[k + a] - nrm[k + a] * ht;
        fn[k + a] = nrm[k + a];
        bn[k + a] = -nrm[k + a];
      }
    }
    this.gFront.attributes.position.needsUpdate = true;
    this.gFront.attributes.normal.needsUpdate = true;
    this.gBack.attributes.position.needsUpdate = true;
    this.gBack.attributes.normal.needsUpdate = true;

    // --- rim: rounded bevel from front edge, out, to back edge ---
    const rp = this.gRim.attributes.position.array, rn = this.gRim.attributes.normal.array;
    const R = this.RIM_ROWS;
    for (let q = 0; q < this.loop.length; q++) {
      const k = this.loop[q];
      const x = this.rest[k * 2], y = this.rest[k * 2 + 1];
      const s = x * ax + y * ay;
      const [, , th] = sample(s);
      const c = Math.cos(th), sn = Math.sin(th);
      const ox2 = this.loopOut[q * 2], oy2 = this.loopOut[q * 2 + 1];
      const os = ox2 * ax + oy2 * ay; // component along bend axis
      const ow = ox2 * px + oy2 * py; // component along perpendicular
      // map to 3D: os * T_s + ow * perp
      let oX = os * c * ax + ow * px;
      let oY = os * c * ay + ow * py;
      let oZ = os * sn;
      const ol = Math.hypot(oX, oY, oZ) || 1;
      oX /= ol; oY /= ol; oZ /= ol;
      const nX = nrm[k * 3], nY = nrm[k * 3 + 1], nZ = nrm[k * 3 + 2];
      for (let r = 0; r < R; r++) {
        const a = (r / (R - 1)) * Math.PI; // 0 -> front, pi -> back
        const ca = Math.cos(a), sa = Math.sin(a);
        const bulge = sa * ht * 0.55;
        const o = (k * 3);
        const v = (q * R + r) * 3;
        rp[v] = mid[o] + nX * ht * ca + oX * bulge;
        rp[v + 1] = mid[o + 1] + nY * ht * ca + oY * bulge;
        rp[v + 2] = mid[o + 2] + nZ * ht * ca + oZ * bulge;
        let mx = nX * ca + oX * sa, my = nY * ca + oY * sa, mz = nZ * ca + oZ * sa;
        const ml = Math.hypot(mx, my, mz) || 1;
        rn[v] = mx / ml; rn[v + 1] = my / ml; rn[v + 2] = mz / ml;
      }
    }
    this.gRim.attributes.position.needsUpdate = true;
    this.gRim.attributes.normal.needsUpdate = true;
  }

  // world-space position of a point given in UV of the printed face (front surface)
  surfacePoint(u, v, target = new THREE.Vector3()) {
    const cols = this.nx + 1;
    // nearest grid sample (good enough for anchoring connectors)
    let best = 0, bd = Infinity;
    const x = -this.w / 2 + u * this.w, y = -this.h / 2 + v * this.h;
    // coarse search on grid
    const i = Math.round(u * this.nx);
    let jGuess = Math.round(v * this.ny);
    for (let dj = -3; dj <= 3; dj++) {
      const j = Math.max(0, Math.min(this.ny, jGuess + dj));
      const k = j * cols + Math.max(0, Math.min(this.nx, i));
      const dx = this.rest[k * 2] - x, dy = this.rest[k * 2 + 1] - y;
      const dd = dx * dx + dy * dy;
      if (dd < bd) { bd = dd; best = k; }
    }
    const fp = this.gFront.attributes.position.array;
    target.set(fp[best * 3], fp[best * 3 + 1], fp[best * 3 + 2]);
    return this.localToWorld(target);
  }
}

// --- bend profiles -----------------------------------------------------------

// smooth crease: angle ramps from 0 to `angle` across a band of length `band` centred at c
export function crease(s, c, angle, band) {
  const x = (s - c) / band + 0.5;
  if (x <= 0) return 0;
  if (x >= 1) return angle;
  return angle * (x * x * (3 - 2 * x));
}

// gentle curl near an edge: angle grows quadratically after s1 (paper lifting)
export function curl(s, s1, s2, angle) {
  if (s <= s1) return 0;
  const x = Math.min(1, (s - s1) / (s2 - s1));
  return angle * x * x;
}

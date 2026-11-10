// Robot loading + pose state (same state shape as src/robot_base.js) + PBR face injection for lit styles.
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { FACE, LOGO, NOISE } from './common.js';

export async function loadRobot(url, logoUrl) {
  const gltf = await new GLTFLoader().loadAsync(url);
  const root = gltf.scene;
  const rig = { root, rigRoot: root.getObjectByName('rig_root'), bones: {}, mesh: null };
  root.traverse((o) => { if (o.isBone) rig.bones[o.name] = o; if (o.isSkinnedMesh) rig.mesh = o; });
  rig.rest = {}; for (const [n, b] of Object.entries(rig.bones)) rig.rest[n] = b.position.clone();
  const m = rig.mesh; m.frustumCulled = false;
  rig.orig = m.material;
  const faceU = {
    uBlink: { value: 0 }, uGaze: { value: new THREE.Vector2() }, uHappy: { value: 0 }, uTalk: { value: 0 },
    uBars: { value: new THREE.Vector4() }, uBar5: { value: 0 }, uEyeGlow: { value: 1 }, uSquint: { value: 0 }, uRing: { value: 1 },
  };
  const logo = await new THREE.TextureLoader().loadAsync(logoUrl);
  logo.flipY = false; logo.colorSpace = THREE.NoColorSpace; logo.anisotropy = 4; logo.needsUpdate = true;
  rig.shared = { faceU, map: { value: rig.orig.map }, emi: { value: rig.orig.emissiveMap }, logo: { value: logo } };
  rig.logoTex = logo;
  smoothNormals(m.geometry, 0.035, 2);
  rig.texPix = { base: imagePixels(rig.orig.map.image, 1024), emi: imagePixels(rig.orig.emissiveMap.image, 1024) };
  classifyVertices(m.geometry, rig.texPix);
  return rig;
}

export function imagePixels(img, size) {
  const c = document.createElement('canvas'); c.width = c.height = size;
  const g = c.getContext('2d', { willReadFrequently: true }); g.drawImage(img, 0, 0, size, size);
  return { size, data: g.getImageData(0, 0, size, size).data };
}
export function samplePix(p, u, v) {
  const x = Math.min(p.size - 1, Math.max(0, Math.floor(u * p.size))), y = Math.min(p.size - 1, Math.max(0, Math.floor(v * p.size)));
  const i = 4 * (y * p.size + x); return [p.data[i] / 255, p.data[i + 1] / 255, p.data[i + 2] / 255];
}

// aCls (white, blue, dark-grey): per-vertex surface classes sampled from the textures, then spatially filtered so region
// boundaries are clean curves (graphic styles threshold these instead of the noisy scan texture).
function classifyVertices(geo, tex) {
  const pa = geo.attributes.position, ua = geo.attributes.uv, n = pa.count;
  const P = new Float32Array(n * 3); for (let i = 0; i < n; i++) { P[3 * i] = pa.getX(i); P[3 * i + 1] = pa.getY(i); P[3 * i + 2] = pa.getZ(i); }
  const raw = new Float32Array(n * 3);
  for (let i = 0; i < n; i++) {
    const u = ua.getX(i), v = ua.getY(i), c = samplePix(tex.base, u, v), e = samplePix(tex.emi, u, v);
    const l = 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
    raw[3 * i] = l > 0.5 ? 1 : 0; raw[3 * i + 1] = e[2] > 0.45 ? 1 : 0; raw[3 * i + 2] = l > 0.22 && l <= 0.5 ? 1 : 0;
  }
  const cell = 0.02, grid = new Map(), key = (x, y, z) => (x + 512) * 1048576 + (y + 512) * 1024 + (z + 512);
  for (let i = 0; i < n; i++) { const k = key(Math.floor(P[3 * i] / cell), Math.floor(P[3 * i + 1] / cell), Math.floor(P[3 * i + 2] / cell)); let a = grid.get(k); if (!a) grid.set(k, (a = [])); a.push(i); }
  const out = new Float32Array(n * 3), R = [0.02, 0.009, 0.016];
  for (let i = 0; i < n; i++) {
    const x = P[3 * i], y = P[3 * i + 1], z = P[3 * i + 2], cx = Math.floor(x / cell), cy = Math.floor(y / cell), cz = Math.floor(z / cell);
    const s = [0, 0, 0], w = [0, 0, 0];
    for (let dx = -1; dx <= 1; dx++) for (let dy = -1; dy <= 1; dy++) for (let dz = -1; dz <= 1; dz++) {
      const a = grid.get(key(cx + dx, cy + dy, cz + dz)); if (!a) continue;
      for (const j of a) {
        const ex = P[3 * j] - x, ey = P[3 * j + 1] - y, ez = P[3 * j + 2] - z, d2 = ex * ex + ey * ey + ez * ez;
        for (let k = 0; k < 3; k++) { const r2 = R[k] * R[k]; if (d2 < r2) { const ww = 1 - d2 / r2; s[k] += raw[3 * j + k] * ww; w[k] += ww; } }
      }
    }
    for (let k = 0; k < 3; k++) out[3 * i + k] = w[k] > 0 ? s[k] / w[k] : raw[3 * i + k];
  }
  // hands: replace the scanned white-cap boundary by a best-fit plane cut (clean curve on the mitten)
  const si = geo.attributes.skinIndex, sw = geo.attributes.skinWeight;
  for (const bone of [2, 3]) {
    const ids = []; for (let i = 0; i < n; i++) if (si.getX(i) === bone && sw.getX(i) > 0.5) ids.push(i);
    if (ids.length < 50) continue;
    let c = [0, 0, 0], m = 0; for (const i of ids) { for (let k = 0; k < 3; k++) c[k] += P[3 * i + k]; m += out[3 * i]; }
    c = c.map((v) => v / ids.length); m /= ids.length;
    const a = [0, 0, 0]; for (const i of ids) for (let k = 0; k < 3; k++) a[k] += (P[3 * i + k] - c[k]) * (out[3 * i] - m);
    const al = Math.hypot(...a) || 1; for (let k = 0; k < 3; k++) a[k] /= al;
    const proj = ids.map((i) => (P[3 * i] - c[0]) * a[0] + (P[3 * i + 1] - c[1]) * a[1] + (P[3 * i + 2] - c[2]) * a[2]);
    const sorted = [...proj].sort((x, y) => x - y); const th = sorted[Math.min(sorted.length - 1, Math.floor((1 - m) * sorted.length))];
    ids.forEach((i, j) => { const d = (proj[j] - th) / 0.006; out[3 * i] = Math.max(0, Math.min(1, 0.5 + 0.5 * d)); });
  }
  geo.setAttribute('aCls', new THREE.BufferAttribute(out, 3));
}

// aSmoothN: normals averaged over a small radius (same-facing neighbours only, so thin shells keep both sides).
// Toon / line styles shade with these: clean terminator shapes, no faceting noise from the scan mesh.
function smoothNormals(geo, r, iters = 1) {
  // (GLB attributes may be interleaved: read them through the accessor, not .array)
  const pa = geo.attributes.position, na = geo.attributes.normal, n = pa.count;
  const P = new Float32Array(n * 3), N = new Float32Array(n * 3);
  for (let i = 0; i < n; i++) { P[3 * i] = pa.getX(i); P[3 * i + 1] = pa.getY(i); P[3 * i + 2] = pa.getZ(i); N[3 * i] = na.getX(i); N[3 * i + 1] = na.getY(i); N[3 * i + 2] = na.getZ(i); }
  const cell = r, grid = new Map(), key = (x, y, z) => (x + 512) * 1048576 + (y + 512) * 1024 + (z + 512);
  for (let i = 0; i < n; i++) {
    const k = key(Math.floor(P[3 * i] / cell), Math.floor(P[3 * i + 1] / cell), Math.floor(P[3 * i + 2] / cell));
    let a = grid.get(k); if (!a) grid.set(k, (a = [])); a.push(i);
  }
  let out = new Float32Array(n * 3); const r2 = r * r;
  for (let it = 0; it < iters; it++) {
  if (it > 0) { const src = out; out = new Float32Array(n * 3); for (let i = 0; i < 3 * n; i++) N[i] = src[i]; }
  for (let i = 0; i < n; i++) {
    const x = P[3 * i], y = P[3 * i + 1], z = P[3 * i + 2], nx = N[3 * i], ny = N[3 * i + 1], nz = N[3 * i + 2];
    const cx = Math.floor(x / cell), cy = Math.floor(y / cell), cz = Math.floor(z / cell);
    let sx = 0, sy = 0, sz = 0;
    for (let dx = -1; dx <= 1; dx++) for (let dy = -1; dy <= 1; dy++) for (let dz = -1; dz <= 1; dz++) {
      const a = grid.get(key(cx + dx, cy + dy, cz + dz)); if (!a) continue;
      for (const j of a) {
        const ex = P[3 * j] - x, ey = P[3 * j + 1] - y, ez = P[3 * j + 2] - z, d2 = ex * ex + ey * ey + ez * ez;
        if (d2 > r2) continue;
        const dt = nx * N[3 * j] + ny * N[3 * j + 1] + nz * N[3 * j + 2]; if (dt <= 0.2) continue;
        const w = (1 - d2 / r2) * dt; sx += N[3 * j] * w; sy += N[3 * j + 1] * w; sz += N[3 * j + 2] * w;
      }
    }
    const l = Math.hypot(sx, sy, sz) || 1; out[3 * i] = sx / l; out[3 * i + 1] = sy / l; out[3 * i + 2] = sz / l;
  }
  }
  geo.setAttribute('aSmoothN', new THREE.BufferAttribute(out, 3));
  // aBlobN: smoothed normal pulled towards the radial direction from its part's centre -> big, simple light shapes
  // (vector / pixel styles). Part = dominant skin bone (0 body, 1 head, 2 hand_L, 3 hand_R).
  const C = [[0.02, 0.33, 0.0], [0.03, 0.63, 0.03], [0.386, 0.224, 0.02], [-0.38, 0.282, 0.142]];
  const si = geo.attributes.skinIndex, sw = geo.attributes.skinWeight, blob = new Float32Array(n * 3);
  for (let i = 0; i < n; i++) {
    let b = si.getX(i), w = sw.getX(i); if (sw.getY(i) > w) { b = si.getY(i); w = sw.getY(i); }
    const c = C[b] || C[0];
    let rx = P[3 * i] - c[0], ry = (P[3 * i + 1] - c[1]) * (b === 0 ? 0.6 : 1), rz = P[3 * i + 2] - c[2]; const rl = Math.hypot(rx, ry, rz) || 1;
    rx /= rl; ry /= rl; rz /= rl;
    let bx = out[3 * i] * 0.45 + rx * 0.55, by = out[3 * i + 1] * 0.45 + ry * 0.55, bz = out[3 * i + 2] * 0.45 + rz * 0.55; const bl = Math.hypot(bx, by, bz) || 1;
    blob[3 * i] = bx / bl; blob[3 * i + 1] = by / bl; blob[3 * i + 2] = bz / bl;
  }
  geo.setAttribute('aBlobN', new THREE.BufferAttribute(blob, 3));
}

// pose: root {x,y,z,rx,ry,rz,s}, bones {name:[rx,ry,rz]}, offs {name:[dx,dy,dz]}, face {...}, ring, visible
export function applyState(rig, s) {
  const R = s.root || {}, rr = rig.rigRoot;
  rr.position.set(R.x || 0, R.y || 0, R.z || 0); rr.rotation.set(R.rx || 0, R.ry || 0, R.rz || 0, 'YXZ');
  const k = R.s == null ? 1 : R.s; rr.scale.set(k, k, k);
  for (const [n, b] of Object.entries(rig.bones)) {
    const v = (s.bones && s.bones[n]) || [0, 0, 0]; b.rotation.set(v[0], v[1], v[2], 'XYZ');
    const o = (s.offs && s.offs[n]) || [0, 0, 0]; b.position.set(rig.rest[n].x + o[0], rig.rest[n].y + o[1], rig.rest[n].z + o[2]);
  }
  const f = s.face || {}, u = rig.shared.faceU;
  u.uBlink.value = f.blink || 0; u.uGaze.value.set(...(f.gaze || [0, 0])); u.uHappy.value = f.happy || 0; u.uSquint.value = f.squint || 0;
  u.uTalk.value = f.talk || 0; const b = f.bars || [0, 0, 0, 0, 0]; u.uBars.value.set(b[0], b[1], b[2], b[3]); u.uBar5.value = b[4] || 0;
  u.uEyeGlow.value = f.glow == null ? 1 : f.glow;
  u.uRing.value = s.ring == null ? 1 : s.ring;
  rig.visible = s.visible !== false;
  rig.root.updateMatrixWorld(true);
}

// lit (MeshStandard/Physical) robot material with the screen face injected; opts tune the look per style
export function litRobotMaterial(rig, opts = {}) {
  const src = rig.orig;
  const mat = new (opts.physical ? THREE.MeshPhysicalMaterial : THREE.MeshStandardMaterial)({
    map: src.map, normalMap: opts.noNormal ? null : src.normalMap, roughnessMap: src.roughnessMap, metalnessMap: src.metalnessMap,
    emissiveMap: src.emissiveMap, emissive: new THREE.Color(1, 1, 1), emissiveIntensity: 1, metalness: src.metalness, roughness: src.roughness,
  });
  if (opts.physical) { mat.clearcoat = opts.clearcoat ?? 0.6; mat.clearcoatRoughness = opts.clearcoatRoughness ?? 0.12; }
  if (src.normalScale && mat.normalMap) mat.normalScale.copy(src.normalScale);
  const u = rig.shared.faceU;
  const P = {
    uTint: { value: new THREE.Vector3(...(opts.tintWhite || [1, 1, 1])) }, uDarkTint: { value: new THREE.Vector3(...(opts.tintDark || [1, 1, 1])) },
    uEmiCol: { value: new THREE.Vector3(...(opts.emi || [1, 1, 1])) }, uEyeCol: { value: new THREE.Vector3(...(opts.eye || [0.82, 0.92, 1.0])) },
    uEyeAlb: { value: new THREE.Vector3(...(opts.eyeAlb || [0.93, 0.97, 1.0])) }, uRough: { value: new THREE.Vector2(...(opts.rough || [0, 1])) },
    uEyeK: { value: opts.eyeK ?? 0.95 }, uEmiK: { value: opts.emiK ?? 1.0 }, uVisorRough: { value: opts.visorRough ?? -1 },
  };
  mat.userData.u = P;
  const CL = opts.classes;   // optional: recolour by surface class (clay / toy palettes) instead of the scan texture
  if (CL) Object.assign(P, {
    uCW: { value: new THREE.Vector3(...CL.white) }, uCD: { value: new THREE.Vector3(...CL.dark) }, uCB: { value: new THREE.Vector3(...CL.blue) },
    uCV: { value: new THREE.Vector3(...CL.visor) }, uCL: { value: new THREE.Vector3(...(CL.logo || [0.05, 0.05, 0.08])) }, uLogo: rig.shared.logo,
  });
  mat.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, u, P);
    sh.vertexShader = sh.vertexShader
      .replace('#include <beginnormal_vertex>', opts.smoothN ? 'vec3 objectNormal = aSmoothN;\n#ifdef USE_TANGENT\nvec3 objectTangent = vec3( tangent.xyz );\n#endif' : '#include <beginnormal_vertex>')
      .replace('#include <common>', '#include <common>\nattribute vec3 aSmoothN;\nattribute vec3 _face;\nattribute vec3 aCls;\nvarying vec3 vFace;\nvarying vec3 vCls;\nvarying vec3 vRestP;\nvarying vec3 vRestN;')
      .replace('#include <begin_vertex>', '#include <begin_vertex>\nvFace = _face; vCls = aCls; vRestP = position; vRestN = normal;');
    sh.fragmentShader = sh.fragmentShader
      .replace('#include <common>', '#include <common>\nvarying vec3 vFace; varying vec3 vCls; varying vec3 vRestP; varying vec3 vRestN;\nuniform vec3 uTint; uniform vec3 uDarkTint; uniform vec3 uEmiCol; uniform vec3 uEyeCol; uniform vec3 uEyeAlb; uniform vec2 uRough; uniform float uEyeK; uniform float uEmiK; uniform float uVisorRough;\n' + FACE
        + (CL ? 'uniform vec3 uCW; uniform vec3 uCD; uniform vec3 uCB; uniform vec3 uCV; uniform vec3 uCL;\n' + LOGO : ''))
      .replace('#include <map_fragment>', `#include <map_fragment>
        float faceA = vFace.z > 0.01 ? screenFace(vFace.xy) * vFace.z : 0.0;
        float lumA = dot(diffuseColor.rgb, vec3(0.2126, 0.7152, 0.0722));
        float wht = smoothstep(0.10, 0.45, lumA);
        diffuseColor.rgb *= mix(uDarkTint, uTint, wht);
        float ellV = pow((vRestP.x - 0.078) / 0.27, 2.0) + pow((vRestP.y - 0.647) / 0.18, 2.0);
        float frV = step(0.1, vRestP.z) * step(0.0, vRestN.z);
        float visM = max(smoothstep(0.08, 0.3, vFace.z), (1.0 - smoothstep(1.17, 1.23, ellV)) * frV);
        ${CL ? `
        float cw = smoothstep(0.45, 0.55, vCls.x), cb = smoothstep(0.37, 0.47, vCls.y) * (1.0 - visM);
        cw = max(cw, (1.0 - smoothstep(1.55, 1.65, ellV)) * frV);
        vec3 cc = mix(uCD, uCW, cw); cc = mix(cc, uCB, cb); cc = mix(cc, uCV, visM);
        cc = mix(cc, uCL, smoothstep(0.35, 0.6, logoMask(vRestP, vRestN)) * cw * (1.0 - visM));
        diffuseColor.rgb = cc;` : ''}
        diffuseColor.rgb = mix(diffuseColor.rgb, uEyeAlb, faceA);`)
      .replace('#include <roughnessmap_fragment>', `#include <roughnessmap_fragment>
        roughnessFactor = clamp(roughnessFactor * uRough.y + uRough.x, 0.02, 1.0);
        if (uVisorRough >= 0.0) roughnessFactor = mix(roughnessFactor, uVisorRough, visM);
        roughnessFactor = mix(roughnessFactor, 0.35, faceA);`)
      .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
        totalEmissiveRadiance *= uEmiCol * uEmiK * uRing;
        totalEmissiveRadiance += uEyeCol * faceA * uEyeK * uEyeGlow;`);
  };
  mat.customProgramCacheKey = () => 'sb-litrobot-' + (opts.key || 'x') + (opts.physical ? 'p' : 's') + (opts.smoothN ? 'n' : '');
  return mat;
}

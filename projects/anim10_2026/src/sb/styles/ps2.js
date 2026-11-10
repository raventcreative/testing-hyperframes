// PS2 STYLE: early-2000s console 3D. Robot decimated to a low-poly model (vertex clustering, ~5k tris) with vertex
// colours, Gouraud (per-vertex) lighting, chrome sphere-map visor; set with small procedural textures (wallpaper +
// wainscot, carpet, wood, whiteboard, night-city window) sampled bilinear with a touch of affine warping on a
// tessellated set; vertex snapping to the low-res grid; distance fog. Rendered at ~1/2.75 res (about 298x356),
// quantised to 15-bit colour with 4x4 ordered dither, upscaled bilinear with faint interlace lines.
import * as THREE from 'three';
import { styleMat, makeRT, Pass, hash2 } from '../common.js';
import { PAL } from '../set.js';

const DIV = 2.75;

// vertex clustering decimation of the skinned robot (per dominant bone, so hands never merge into the body)
function decimate(geo, cell) {
  const A = geo.attributes, n = A.position.count;
  const si = A.skinIndex, sw = A.skinWeight;
  const map = new Int32Array(n), keys = new Map(), reps = [], sums = [];
  for (let i = 0; i < n; i++) {
    let b = si.getX(i); if (sw.getY(i) > sw.getX(i)) b = si.getY(i);
    const x = A.position.getX(i), y = A.position.getY(i), z = A.position.getZ(i);
    const k = b + '|' + Math.floor(x / cell) + '|' + Math.floor(y / cell) + '|' + Math.floor(z / cell);
    let j = keys.get(k);
    if (j === undefined) { j = reps.length; keys.set(k, j); reps.push(i); sums.push({ p: [0, 0, 0], f: [0, 0, 0], c: [0, 0, 0], k: 0 }); }
    map[i] = j; const s = sums[j]; s.k++;
    s.p[0] += x; s.p[1] += y; s.p[2] += z;
    s.f[0] += A._face.getX(i); s.f[1] += A._face.getY(i); s.f[2] += A._face.getZ(i);
    s.c[0] += A.aCls.getX(i); s.c[1] += A.aCls.getY(i); s.c[2] += A.aCls.getZ(i);
  }
  const m = reps.length;
  const pos = new Float32Array(m * 3), face = new Float32Array(m * 3), cls = new Float32Array(m * 3), uv = new Float32Array(m * 2);
  const sI = new Uint16Array(m * 4), sW = new Float32Array(m * 4);
  for (let j = 0; j < m; j++) {
    const s = sums[j], r = reps[j];
    for (let k = 0; k < 3; k++) { pos[3 * j + k] = s.p[k] / s.k; face[3 * j + k] = s.f[k] / s.k; cls[3 * j + k] = s.c[k] / s.k; }
    uv[2 * j] = A.uv.getX(r); uv[2 * j + 1] = A.uv.getY(r);
    sI[4 * j] = si.getX(r); sI[4 * j + 1] = si.getY(r); sI[4 * j + 2] = si.getZ(r); sI[4 * j + 3] = si.getW(r);
    sW[4 * j] = sw.getX(r); sW[4 * j + 1] = sw.getY(r); sW[4 * j + 2] = sw.getZ(r); sW[4 * j + 3] = sw.getW(r);
  }
  const src = geo.index.array, idx = [];
  for (let t = 0; t < src.length; t += 3) {
    const a = map[src[t]], b = map[src[t + 1]], c = map[src[t + 2]];
    if (a !== b && b !== c && a !== c) idx.push(a, b, c);
  }
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.BufferAttribute(pos, 3)); g.setAttribute('uv', new THREE.BufferAttribute(uv, 2));
  g.setAttribute('_face', new THREE.BufferAttribute(face, 3)); g.setAttribute('aCls', new THREE.BufferAttribute(cls, 3));
  g.setAttribute('skinIndex', new THREE.BufferAttribute(sI, 4)); g.setAttribute('skinWeight', new THREE.BufferAttribute(sW, 4));
  g.setIndex(idx); g.computeVertexNormals();
  g.setAttribute('aSmoothN', g.attributes.normal.clone()); g.setAttribute('aBlobN', g.attributes.normal.clone());
  return g;
}

// small deterministic textures (canvas 2D), bilinear, no mipmaps (shimmer like the real thing)
function canvasTex(w, h, draw) {
  const c = document.createElement('canvas'); c.width = w; c.height = h; const g = c.getContext('2d'); draw(g, w, h);
  const t = new THREE.CanvasTexture(c); t.wrapS = t.wrapT = THREE.RepeatWrapping; t.generateMipmaps = false;
  t.minFilter = THREE.LinearFilter; t.magFilter = THREE.LinearFilter; t.colorSpace = THREE.NoColorSpace; return t;
}
const noiseFill = (g, w, h, base, amp, seed, cell = 1) => {
  for (let y = 0; y < h; y += cell) for (let x = 0; x < w; x += cell) {
    const v = (hash2(x + seed, y * 1.3 + seed) - 0.5) * amp;
    g.fillStyle = `rgb(${Math.round(base[0] + v)},${Math.round(base[1] + v)},${Math.round(base[2] + v * 0.9)})`; g.fillRect(x, y, cell, cell);
  }
};
function makeTextures() {
  // wall: one tile spans the full wall height (3.4): wallpaper stripes above a wood wainscot (bottom 0.9) + dado rail
  const wall = canvasTex(64, 256, (g, w, h) => {
    noiseFill(g, w, h, [178, 162, 130], 12, 1);
    for (let x = 0; x < w; x += 16) { g.fillStyle = 'rgba(120,96,70,0.32)'; g.fillRect(x, 0, 3, h); g.fillStyle = 'rgba(255,240,210,0.16)'; g.fillRect(x + 8, 0, 2, h); }
    const wy = Math.round(h * (1 - 0.9 / 3.4));
    for (let y = wy; y < h; y++) for (let x = 0; x < w; x++) { const v = (hash2(x * 0.2, y * 3.1) - 0.5) * 26; g.fillStyle = `rgb(${110 + v},${72 + v * 0.7},${44 + v * 0.5})`; g.fillRect(x, y, 1, 1); }
    g.fillStyle = 'rgb(70,44,26)'; g.fillRect(0, wy - 3, w, 4); for (let x = 0; x < w; x += 32) g.fillRect(x, wy, 2, h - wy);
    g.fillStyle = 'rgb(150,110,70)'; g.fillRect(0, wy - 5, w, 2);
  });
  wall.wrapT = THREE.ClampToEdgeWrapping;
  const carpet = canvasTex(64, 64, (g, w, h) => { noiseFill(g, w, h, [78, 86, 108], 16, 7); g.fillStyle = 'rgba(40,46,66,0.5)'; g.fillRect(0, 0, w, 1); g.fillRect(0, 0, 1, h); for (let i = 0; i < 40; i++) { g.fillStyle = 'rgba(30,34,50,0.35)'; g.fillRect(Math.floor(hash2(i, 3) * w), Math.floor(hash2(i, 9) * h), 2, 1); } });
  const wood = canvasTex(64, 64, (g, w, h) => { for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) { const v = Math.sin(x * 0.45 + Math.sin(y * 0.15) * 2.5 + hash2(x, y) * 0.8) * 18 + (hash2(x * 3, y) - 0.5) * 12; g.fillStyle = `rgb(${132 + v},${84 + v * 0.7},${52 + v * 0.45})`; g.fillRect(x, y, 1, 1); } });
  const board = canvasTex(64, 64, (g, w, h) => { noiseFill(g, w, h, [226, 228, 224], 8, 11); for (let i = 0; i < 6; i++) { g.fillStyle = 'rgba(150,170,200,0.12)'; g.fillRect(hash2(i, 5) * w, hash2(i, 6) * h, 14, 5); } });
  const city = canvasTex(128, 64, (g, w, h) => {
    const gr = g.createLinearGradient(0, 0, 0, h); gr.addColorStop(0, '#0b1230'); gr.addColorStop(1, '#3a2d48'); g.fillStyle = gr; g.fillRect(0, 0, w, h);
    let x = 0, i = 0; while (x < w) { const bw = 8 + Math.floor(hash2(i, 1) * 14), bh = 14 + Math.floor(hash2(i, 2) * 36); g.fillStyle = `rgb(${18 + i % 3 * 6},${20 + i % 2 * 6},${34})`; g.fillRect(x, h - bh, bw, bh);
      for (let yy = h - bh + 3; yy < h - 2; yy += 4) for (let xx = x + 2; xx < x + bw - 2; xx += 3) if (hash2(xx * 1.7, yy * 2.3) > 0.55) { g.fillStyle = hash2(xx, yy) > 0.3 ? '#ffd27a' : '#9fd0ff'; g.fillRect(xx, yy, 1, 2); }
      x += bw + 1; i++; }
    for (let k = 0; k < 30; k++) { g.fillStyle = '#ffffff'; g.fillRect(Math.floor(hash2(k, 8) * w), Math.floor(hash2(k, 9) * h * 0.4), 1, 1); }
  });
  return { wall, carpet, wood, board, city };
}

const PS2V = /* glsl */ `
uniform vec3 uFogCol; uniform vec2 uFog;
float fogK() { return smoothstep(uFog.x, uFog.y, vDepth); }
`;

export default function createPs2(ctx) {
  const { W, H } = ctx;
  const Wl = Math.round(W / DIV), Hl = Math.round(H / DIV);
  const low = decimate(ctx.rig.mesh.geometry, 0.048);
  const tex = makeTextures();
  const L = { uKeyDir: { value: new THREE.Vector3(-0.5, 0.8, 0.62).normalize() }, uKeyCol: { value: new THREE.Vector3(1.12, 1.0, 0.85) },
    uAmbUp: { value: new THREE.Vector3(0.36, 0.36, 0.44) }, uAmbDn: { value: new THREE.Vector3(0.16, 0.13, 0.12) },
    uSnap: { value: new THREE.Vector2(Wl / 2, Hl / 2) }, uFogCol: { value: new THREE.Vector3(0.12, 0.1, 0.14) }, uFog: { value: new THREE.Vector2(4.4, 11.0) } };
  const robotMat = styleMat({ robot: true, rawNormals: true, shared: ctx.rig.shared, defines: { VLIGHT: '', SNAP: '' }, uniforms: { ...L }, side: THREE.DoubleSide,
    extra: 'varying vec3 vGouraud;\nuniform vec3 uKeyDir;\n' + PS2V, frag: /* glsl */ `
    void main() {
      RobotSurf s = robotSurf();
      vec3 white = vec3(0.8, 0.81, 0.84), dark = vec3(0.09, 0.095, 0.115), blue = vec3(0.25, 0.65, 1.0);
      vec3 base = white * s.white + dark * s.dark;
      vec3 c = base * vGouraud;
      // per-vertex-ish specular (shiny console plastic)
      vec3 V = normalize(cameraPosition - vW); vec3 Hh = normalize(normalize(uKeyDir) + V);
      c += vec3(0.32) * pow(max(dot(normalize(vN), Hh), 0.0), 16.0) * s.white;
      // chrome sphere-map visor (fake reflection from the view normal)
      vec3 n = normalize(vNV);
      float band = smoothstep(0.25, 0.5, n.y) * (1.0 - smoothstep(0.55, 0.85, n.y)) + 0.35 * smoothstep(0.6, 0.95, -n.x);
      vec3 vis = vec3(0.03, 0.035, 0.06) + vec3(0.35, 0.42, 0.55) * band;
      c = mix(c, vis, s.visor);
      c += blue * s.blue * 1.1;
      c = mix(c, vec3(0.75, 0.95, 1.0), s.eye);
      c = mix(c, vec3(0.08, 0.08, 0.1), smoothstep(0.35, 0.6, s.logo));
      c = mix(c, uFogCol, fogK());
      gl_FragColor = vec4(c, 1.0);
    }` });
  const setMat = styleMat({ robot: false, defines: { VLIGHT: '', SNAP: '', AFFINE: '' }, uniforms: { ...L, tWall: { value: tex.wall }, tCarpet: { value: tex.carpet }, tWood: { value: tex.wood }, tBoard: { value: tex.board }, tCity: { value: tex.city } },
    extra: 'varying vec3 vGouraud;\nvarying vec3 vAff;\nuniform sampler2D tWall; uniform sampler2D tCarpet; uniform sampler2D tWood; uniform sampler2D tBoard; uniform sampler2D tCity;\n' + PS2V, frag: /* glsl */ `
    // affine-ish texture coords (screen-linear interpolation, mixed 50% with perspective-correct)
    vec2 planar() { vec3 a = abs(vN); vec2 pc = a.y > 0.5 ? vW.xz : (a.z > 0.5 ? vW.xy : vW.zy); return mix(pc, vAff.xy / vAff.z, 0.5); }
    void main() {
      int p = vPal; vec2 uv = planar();
      vec3 c = vec3(0.4);
      if (p == ${PAL.wall}) c = texture2D(tWall, vec2(uv.x / 0.9, clamp(uv.y / 3.4, 0.002, 0.998))).rgb;
      else if (p == ${PAL.floor}) c = texture2D(tCarpet, uv / 0.7).rgb;
      else if (p == ${PAL.deskTop} || p == ${PAL.deskBody} || p == ${PAL.boardFrame} || p == ${PAL.winFrame}) c = texture2D(tWood, uv / 0.5).rgb * (p == ${PAL.deskBody} ? 0.8 : 1.0);
      else if (p == ${PAL.board}) c = texture2D(tBoard, uv / 0.6).rgb;
      else if (p == ${PAL.sky}) c = texture2D(tCity, vec2((uv.x + 1.6) / 1.4, (uv.y - 0.85) / 1.0)).rgb * 1.2;
      else if (p == ${PAL.city}) c = vec3(0.05, 0.05, 0.08);
      else if (p == ${PAL.monitor} || p == ${PAL.keyboard}) c = vec3(0.16, 0.16, 0.18);
      else if (p == ${PAL.screen}) c = vec3(0.1, 0.22, 0.42);
      else if (p == ${PAL.bar1} || p == ${PAL.leaf}) c = vec3(0.25, 0.62, 0.3);
      else if (p == ${PAL.bar2} || p == ${PAL.mug}) c = vec3(0.92, 0.72, 0.2);
      else if (p == ${PAL.bar3} || p == ${PAL.pot}) c = vec3(0.75, 0.25, 0.2);
      else if (p == ${PAL.bar4}) c = vec3(0.25, 0.5, 0.9);
      else if (p == ${PAL.clock}) c = vec3(0.85, 0.85, 0.8);
      else if (p == ${PAL.axis} || p == ${PAL.clockHand}) c = vec3(0.1);
      else if (p == ${PAL.trim}) c = vec3(0.3, 0.2, 0.12);
      else if (p == ${PAL.soil}) c = vec3(0.2, 0.13, 0.08);
      vec3 lit = (p == ${PAL.sky} || p == ${PAL.screen}) ? c : c * vGouraud * 1.1;
      lit = mix(lit, uFogCol, fogK());
      gl_FragColor = vec4(lit, 1.0);
    }` });
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0.12, 0.1, 0.14);
  const robot = ctx.robotMesh(robotMat, low); scene.add(robot);
  scene.add(new THREE.Mesh(ctx.tessSet(), setMat));
  const rt = makeRT(Wl, Hl, { type: THREE.UnsignedByteType });
  const rtQ = makeRT(Wl, Hl, { type: THREE.UnsignedByteType, depth: false });
  const quant = new Pass(/* glsl */ `uniform sampler2D tSrc; varying vec2 vUv;
    float bayer4(vec2 p) { ivec2 i = ivec2(mod(p, 4.0)); int k = i.x + i.y * 4;
      float m[16] = float[16](0.0, 8.0, 2.0, 10.0, 12.0, 4.0, 14.0, 6.0, 3.0, 11.0, 1.0, 9.0, 15.0, 7.0, 13.0, 5.0); return (m[k] + 0.5) / 16.0 - 0.5; }
    void main() {
      vec3 c = texture2D(tSrc, vUv).rgb;
      c = pow(c, vec3(1.0 / 2.2));
      c = mix(vec3(luma(c)), c, 1.12) * 1.04;                       // slightly punchy console colour
      c = floor(c * 31.0 + 0.5 + bayer4(gl_FragCoord.xy) * 1.0) / 31.0;  // 15-bit (5:5:5) with ordered dither
      gl_FragColor = vec4(clamp(c, 0.0, 1.0), 1.0);
    }`, { tSrc: { value: rt.texture } });
  const up = new Pass(/* glsl */ `uniform sampler2D tSrc; uniform vec2 uRes; varying vec2 vUv;
    void main() {
      vec3 c = texture2D(tSrc, vUv).rgb;
      float line = mod(floor(gl_FragCoord.y), 3.0) < 1.0 ? 0.94 : 1.0;   // faint interlace / TV lines
      c *= line;
      vec2 v = vUv - 0.5; c *= 1.0 - 0.25 * dot(v, v);
      gl_FragColor = vec4(c, 1.0);
    }`, { tSrc: { value: rtQ.texture }, uRes: { value: new THREE.Vector2(W, H) } });
  return {
    render(target) {
      const r = ctx.renderer;
      robot.visible = ctx.robotVisible;
      r.setRenderTarget(rt); r.clear(); r.render(scene, ctx.camera);
      quant.render(r, rtQ); up.render(r, target);
    },
  };
}

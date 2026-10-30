// POCKET UNIVERSE v2 — the showcase world for the Claude Opus 5.5 reel (Three.js, deterministic: render(t) is a pure
// function of t; seeded geometry; no clock, no randomness at render time).
// Story (world time t): astronaut reaches a glowing cube -> the cube unfolds -> a floating island grows out of it
// (grey and empty) -> comes alive in colour -> SHOWCASE: the camera dives into the city, flies down the main avenue,
// climbs out over the lake and the ferris wheel, goes over the edge of the waterfall, swings under the island while
// day turns to sunset and night (windows switch on, aurora) -> the island lifts off the cube on a beam of light and
// the camera pulls out to the whole pocket universe, which keeps living behind the presenter.
import * as THREE from 'three';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/examples/jsm/postprocessing/OutputPass.js';
import { mergeGeometries } from 'three/examples/jsm/utils/BufferGeometryUtils.js';
import { ShaderPass } from 'three/examples/jsm/postprocessing/ShaderPass.js';
import { City, GradeShader } from './city.js';

const clamp = (v, a = 0, b = 1) => Math.max(a, Math.min(b, v));
const ss = (a, b, t) => { const u = clamp((t - a) / (b - a)); return u * u * (3 - 2 * u); };
const eo = (u) => 1 - Math.pow(1 - clamp(u), 3);
const eio = (u) => { u = clamp(u); return u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2; };
const back = (u) => { u = clamp(u); const c = 1.6; return 1 + (c + 1) * Math.pow(u - 1, 3) + c * Math.pow(u - 1, 2); };
const lerp = (a, b, u) => a + (b - a) * u;
function rng(seed) { let s = seed >>> 0 || 1; return () => ((s = (Math.imul(s, 1664525) + 1013904223) >>> 0) / 4294967296); }
function hash2(x, y) { const s = Math.sin(x * 127.1 + y * 311.7) * 43758.5453; return s - Math.floor(s); }
function noise(x, y) {
  const xi = Math.floor(x), yi = Math.floor(y), xf = x - xi, yf = y - yi;
  const u = xf * xf * (3 - 2 * xf), v = yf * yf * (3 - 2 * yf);
  const a = hash2(xi, yi), b = hash2(xi + 1, yi), c = hash2(xi, yi + 1), d = hash2(xi + 1, yi + 1);
  return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
}
const fbm = (x, y) => 0.55 * noise(x, y) + 0.3 * noise(x * 2.1 + 5, y * 2.1 + 1) + 0.15 * noise(x * 4.3 + 9, y * 4.3 + 3);
const col3 = (h) => new THREE.Color(h);

// ------------------------------------------------------------------ island layout (local units, island radius RAD)
const RAD = 1.15;
const AVX = -0.45, AVW = 0.1;                       // main avenue (along z)
const CROSS = [-0.42, -0.21, 0.0, 0.21, 0.42], CW = 0.04;
const LAKE = [0.36, -0.12], LAKE_R = 0.23;
const MTN = [0.47, 0.55];
const WF_A = -0.4;                                   // waterfall angle at the rim
const RIVER = [[0.4, 0.36], [0.36, 0.12], [LAKE[0], LAKE[1]], [0.62, -0.27], [0.88, -0.38], [Math.cos(WF_A) * 1.17, Math.sin(WF_A) * 1.17]];
const HERO = [-0.29, -0.1];
const WHEEL = [0.05, -0.64];
function segDist(px, pz, ax, az, bx, bz) {
  const vx = bx - ax, vz = bz - az, l2 = vx * vx + vz * vz; const u = clamp(((px - ax) * vx + (pz - az) * vz) / l2);
  return Math.hypot(px - ax - vx * u, pz - az - vz * u);
}
const riverD = (x, z) => { let d = 9; for (let i = 0; i < RIVER.length - 1; i++) d = Math.min(d, segDist(x, z, ...RIVER[i], ...RIVER[i + 1])); return d; };
const cityMask = (x, z) => ss(-0.98, -0.88, x) * (1 - ss(-0.06, 0.04, x)) * ss(-0.64, -0.56, z) * (1 - ss(0.62, 0.7, z));
function H(x, z) {
  const r = Math.hypot(x, z) / RAD;
  let h = 0.05 + 0.11 * fbm(x * 1.7 + 3, z * 1.7 + 7);
  const dm = Math.hypot(x - MTN[0], z - MTN[1]);
  h += 0.46 * Math.exp(-(dm * dm) / 0.04) * (0.85 + 0.3 * noise(x * 11, z * 11));
  h = lerp(h, 0.05, cityMask(x, z));
  const dl = Math.hypot(x - LAKE[0], z - LAKE[1]);
  h = lerp(h, -0.012, 1 - ss(LAKE_R - 0.02, LAKE_R + 0.07, dl));
  h = lerp(h, 0.004, 1 - ss(0.022, 0.07, riverD(x, z)));
  h = lerp(h, 0.012, ss(0.84, 0.99, r));
  return h;
}

// polar grid (centre fan + rings), y from fy, faces up (or down with flip)
function polarGrid(NR, NS, R, fy, flip = false) {
  const pos = [0, fy(0, 0), 0], idx = [];
  for (let i = 1; i <= NR; i++) { const rr = R * Math.pow(i / NR, 0.85); for (let j = 0; j < NS; j++) { const a = (j / NS) * Math.PI * 2; const x = Math.cos(a) * rr, z = Math.sin(a) * rr; pos.push(x, fy(x, z), z); } }
  const tri = (a, b, c) => (flip ? idx.push(a, c, b) : idx.push(a, b, c));
  for (let j = 0; j < NS; j++) tri(0, 1 + ((j + 1) % NS), 1 + j);
  for (let i = 1; i < NR; i++) { const o = 1 + (i - 1) * NS, o2 = 1 + i * NS; for (let j = 0; j < NS; j++) { const j2 = (j + 1) % NS; tri(o + j, o + j2, o2 + j); tri(o + j2, o2 + j2, o2 + j); } }
  const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setIndex(idx); g.computeVertexNormals();
  return g;
}

// soft round sprite points (additive)
function sparkMat(size) {
  return new THREE.ShaderMaterial({
    transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false,
    uniforms: { uOp: { value: 0 }, uSize: { value: size }, uTime: { value: 0 } },
    vertexShader: `attribute float aSeed; attribute vec3 aCol; varying vec3 vC; varying float vA; uniform float uSize; uniform float uTime;
      void main(){ vec4 mv = modelViewMatrix * vec4(position,1.0); gl_Position = projectionMatrix * mv;
        float tw = 0.55 + 0.45 * sin(uTime * (2.0 + aSeed * 3.0) + aSeed * 40.0); vA = tw; vC = aCol;
        gl_PointSize = uSize * (0.6 + aSeed * 0.8) * (300.0 / -mv.z); }`,
    fragmentShader: `varying vec3 vC; varying float vA; uniform float uOp;
      void main(){ vec2 d = gl_PointCoord - 0.5; float r = length(d); float a = smoothstep(0.5, 0.0, r); a *= a; gl_FragColor = vec4(vC * a * vA * uOp, 1.0); }`,
  });
}

export class World {
  static async create(canvas, opts = {}) { const w = new World(); w.init(canvas, opts);
    if (opts.inner) w.city = await City.create(w.renderer, { width: w.W, height: w.H, base: opts.base, draco: opts.draco });
    return w; }
  init(canvas, { width = 1080, height = 1920, show = [5.15, 16.2], inner = null } = {}) {
    this.W = width; this.H = height; this.SHOW = show; this.IN = inner || [show[0] + 2.25, show[1] - 3.2];
    const r = (this.renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false, preserveDrawingBuffer: true }));
    r.setPixelRatio(1); r.setSize(width, height, false);
    r.outputColorSpace = THREE.SRGBColorSpace; r.toneMapping = THREE.ACESFilmicToneMapping; r.toneMappingExposure = 1.1;
    r.shadowMap.enabled = true; r.shadowMap.type = THREE.PCFSoftShadowMap;
    const scene = (this.scene = new THREE.Scene());
    scene.fog = new THREE.Fog(0x0d1d44, 10, 30);
    this.cam = new THREE.PerspectiveCamera(52, width / height, 0.004, 90);
    const pm = new THREE.PMREMGenerator(r); scene.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture; scene.environmentIntensity = 0.5;
    const R = rng(11);
    this.uNight = { value: 0 }; this.uGrow = { value: 0 }; this.uTime = { value: 0 };

    // ---------------- sky: stage navy -> day -> sunset -> night, sun/moon glow
    this.sky = new THREE.Mesh(new THREE.SphereGeometry(45, 48, 24), new THREE.ShaderMaterial({
      side: THREE.BackSide, depthWrite: false, fog: false,
      uniforms: { uLife: { value: 0 }, uTod: { value: 0 }, uSun: { value: new THREE.Vector3(-0.5, 0.6, 0.6).normalize() } },
      vertexShader: 'varying vec3 vP; void main(){ vP = normalize(position); gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }',
      fragmentShader: `varying vec3 vP; uniform float uLife; uniform float uTod; uniform vec3 uSun;
        vec3 grad(vec3 hor, vec3 mid, vec3 top, float h){ vec3 c = mix(hor, mid, smoothstep(-0.05, 0.22, h)); return mix(c, top, smoothstep(0.22, 0.85, h)); }
        void main(){ float h = vP.y;
          vec3 stage = grad(vec3(0.10,0.24,0.46), vec3(0.06,0.14,0.32), vec3(0.025,0.05,0.14), h);
          vec3 day = grad(vec3(0.46,0.66,0.88), vec3(0.22,0.46,0.82), vec3(0.07,0.22,0.56), h);
          vec3 dusk = grad(vec3(1.00,0.52,0.24), vec3(0.62,0.30,0.48), vec3(0.12,0.10,0.32), h);
          vec3 night = grad(vec3(0.05,0.11,0.24), vec3(0.025,0.05,0.14), vec3(0.008,0.015,0.05), h);
          float sd = smoothstep(0.0, 0.5, uTod) * (1.0 - smoothstep(0.5, 0.95, uTod));
          vec3 live = mix(day, dusk, sd); live = mix(live, night, smoothstep(0.55, 1.0, uTod));
          vec3 c = mix(stage, live, uLife);
          float sun = max(dot(vP, normalize(uSun)), 0.0);
          vec3 sunC = mix(vec3(1.0,0.95,0.8), vec3(1.0,0.55,0.25), sd);
          float sunAmt = uLife * (1.0 - smoothstep(0.6, 0.85, uTod));
          c += sunC * (pow(sun, 700.0) * 3.0 + pow(sun, 18.0) * 0.35 + pow(sun, 4.0) * 0.12 * sd) * sunAmt;
          c += vec3(0.0,0.45,0.6) * 0.14 * exp(-abs(h - 0.02) * 14.0) * (1.0 - uLife * 0.7);
          gl_FragColor = vec4(c, 1.0); }` }));
    scene.add(this.sky);
    const sp = [], sseed = [], scol = [];
    for (let i = 0; i < 900; i++) { const a = R() * Math.PI * 2, y = 0.05 + R() * 0.95, rr = Math.sqrt(1 - y * y); sp.push(Math.cos(a) * rr * 40, y * 40, Math.sin(a) * rr * 40); sseed.push(R()); const w = R(); scol.push(0.75 + 0.25 * w, 0.85 + 0.1 * w, 1); }
    const sg = new THREE.BufferGeometry(); sg.setAttribute('position', new THREE.Float32BufferAttribute(sp, 3));
    sg.setAttribute('aSeed', new THREE.Float32BufferAttribute(sseed, 1)); sg.setAttribute('aCol', new THREE.Float32BufferAttribute(scol, 3));
    this.starMat = sparkMat(0.5); scene.add(new THREE.Points(sg, this.starMat));
    // aurora curtains (night)
    this.aurora = new THREE.Mesh(new THREE.CylinderGeometry(32, 32, 16, 128, 1, true), new THREE.ShaderMaterial({
      side: THREE.BackSide, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false,
      uniforms: { uOp: { value: 0 }, uTime: { value: 0 } },
      vertexShader: 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }',
      fragmentShader: `varying vec2 vUv; uniform float uOp; uniform float uTime;
        float h1(float x){ return fract(sin(x * 91.7) * 43758.5); }
        float n1(float x){ float i = floor(x), f = fract(x); f = f*f*(3.0-2.0*f); return mix(h1(i), h1(i+1.0), f); }
        void main(){ float x = vUv.x * 6.2831; float y = vUv.y;
          float a = 0.0;
          for (int k = 0; k < 3; k++) { float fk = float(k);
            float c = 0.45 + 0.12 * sin(x * (3.0 + fk) + uTime * (0.25 + 0.1 * fk) + fk * 2.0) + 0.06 * sin(x * 11.0 - uTime * 0.6);
            float band = exp(-pow((y - c) * (9.0 - fk * 2.0), 2.0));
            float rays = 0.55 + 0.45 * n1(x * 60.0 + fk * 13.0 + uTime * 0.8);
            a += band * rays * (0.7 - fk * 0.15); }
          vec3 col = mix(vec3(0.1,1.0,0.65), vec3(0.0,0.75,1.0), smoothstep(0.35, 0.6, y)); col = mix(col, vec3(0.65,0.3,1.0), smoothstep(0.6, 0.85, y));
          float side = 0.35 + 0.65 * n1(x * 2.0 + 3.0);
          gl_FragColor = vec4(col * a * side * uOp * smoothstep(0.15, 0.4, y) * (1.0 - smoothstep(0.85, 1.0, y)), 1.0); }` }));
    this.aurora.position.y = 9; scene.add(this.aurora);
    this.moon = new THREE.Mesh(new THREE.SphereGeometry(0.9, 32, 16), new THREE.MeshBasicMaterial({ color: 0xeaf3ff, fog: false, transparent: true, opacity: 0 }));
    this.moon.position.set(14, 16, -26); scene.add(this.moon);

    // ---------------- light
    this.hemi = new THREE.HemisphereLight(0x9cc8ff, 0x1a2440, 1.0); scene.add(this.hemi);
    const key = (this.key = new THREE.DirectionalLight(0xfff1e0, 2.2)); key.castShadow = true;
    key.shadow.mapSize.set(2048, 2048); Object.assign(key.shadow.camera, { left: -1.6, right: 1.6, top: 1.6, bottom: -1.6, near: 0.5, far: 30 });
    key.shadow.bias = -0.0006; key.shadow.normalBias = 0.012; scene.add(key); scene.add(key.target);
    this.underL = new THREE.PointLight(0x5fdcff, 0, 3.5, 1.5); scene.add(this.underL);
    this.rim = new THREE.DirectionalLight(0x62d6ff, 1.1); this.rim.position.set(4, 3, -5); scene.add(this.rim);

    // ---------------- dais
    const metal = new THREE.MeshStandardMaterial({ color: 0x1f2c4c, metalness: 0.7, roughness: 0.38 });
    const dais = new THREE.Mesh(new THREE.CylinderGeometry(3.2, 3.35, 0.22, 128), metal); dais.position.y = -0.11; dais.receiveShadow = true; scene.add(dais);
    const top = new THREE.Mesh(new THREE.CircleGeometry(3.1, 128), new THREE.MeshStandardMaterial({ color: 0x2a3a60, metalness: 0.55, roughness: 0.42 }));
    top.rotation.x = -Math.PI / 2; top.position.y = 0.002; top.receiveShadow = true; scene.add(top);
    this.ringMat = new THREE.MeshBasicMaterial({ color: 0x00c9ff });
    const ring = new THREE.Mesh(new THREE.TorusGeometry(3.12, 0.018, 8, 200), this.ringMat); ring.rotation.x = Math.PI / 2; ring.position.y = 0.01; scene.add(ring);
    const grid = new THREE.GridHelper(6, 24, 0x2f6ea8, 0x23406e); grid.position.y = 0.006; grid.material.transparent = true; grid.material.opacity = 0.22; scene.add(grid);

    // ---------------- pedestal + cube
    const ped = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.5, 0.18, 64), new THREE.MeshStandardMaterial({ color: 0x8fa3c2, metalness: 0.85, roughness: 0.25 }));
    ped.position.y = 0.09; ped.castShadow = ped.receiveShadow = true; scene.add(ped);
    const C = (this.cube = new THREE.Group()); C.position.set(0, 0.18, 0); scene.add(C);
    const S = 0.56, T = 0.035;
    const panelMat = new THREE.MeshStandardMaterial({ color: 0x55627e, metalness: 0.55, roughness: 0.32 });
    const seamMat = (this.seamMat = new THREE.MeshBasicMaterial({ color: 0x5ee3ff }));
    const mkPanel = () => {
      const g = new THREE.Group();
      const p = new THREE.Mesh(new THREE.BoxGeometry(S, S, T), panelMat); p.castShadow = true; g.add(p);
      for (const [w, h, x, y] of [[S * 0.86, 0.008, 0, S * 0.43], [S * 0.86, 0.008, 0, -S * 0.43], [0.008, S * 0.86, S * 0.43, 0], [0.008, S * 0.86, -S * 0.43, 0], [S * 0.5, 0.006, 0, 0.06], [S * 0.3, 0.006, 0, -0.06]]) {
        for (const sgn of [1, -1]) { const l = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.004), seamMat); l.position.set(x, y, sgn * (T / 2 + 0.002)); g.add(l); }
      }
      const plate = new THREE.Mesh(new THREE.BoxGeometry(S * 0.62, S * 0.62, 0.012), new THREE.MeshStandardMaterial({ color: 0x8592ad, metalness: 0.7, roughness: 0.2 }));
      plate.position.z = T / 2 + 0.006; g.add(plate);
      return g;
    };
    const bottom = mkPanel(); bottom.rotation.x = -Math.PI / 2; bottom.position.y = T / 2; C.add(bottom);
    this.sides = [];
    for (let k = 0; k < 4; k++) {
      const hinge = new THREE.Group(); hinge.rotation.y = (k * Math.PI) / 2; C.add(hinge);
      const piv = new THREE.Group(); piv.position.set(0, 0, S / 2); hinge.add(piv);
      const pnl = mkPanel(); pnl.position.set(0, S / 2, 0); piv.add(pnl);
      this.sides.push(piv);
    }
    const topH = (this.topH = new THREE.Group()); topH.position.set(0, S, -S / 2); C.add(topH);
    const topP = mkPanel(); topP.rotation.x = -Math.PI / 2; topP.position.set(0, 0, S / 2); topH.add(topP);
    this.core = new THREE.Mesh(new THREE.SphereGeometry(0.11, 32, 16), new THREE.MeshBasicMaterial({ color: 0xc9f6ff })); this.core.position.y = S / 2; C.add(this.core);
    this.coreL = new THREE.PointLight(0x48d8ff, 2.5, 4, 1.6); this.coreL.position.y = S / 2 + 0.05; C.add(this.coreL);
    // light beam that carries the island up
    this.beam = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.16, 1, 48, 1, true), new THREE.ShaderMaterial({
      transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide, fog: false,
      uniforms: { uOp: { value: 0 }, uTime: { value: 0 } },
      vertexShader: 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }',
      fragmentShader: `varying vec2 vUv; uniform float uOp; uniform float uTime;
        void main(){ float s = 0.6 + 0.4 * sin(vUv.x * 62.83 + uTime * 1.5) * sin(vUv.x * 25.1 - uTime * 0.9);
          float st = 0.7 + 0.3 * sin(vUv.y * 40.0 - uTime * 6.0);
          float a = (1.0 - vUv.y * 0.35) * s * st; gl_FragColor = vec4(vec3(0.35,0.85,1.0) * a * uOp, 1.0); }` }));
    scene.add(this.beam);

    // ---------------- ISLAND (grows out of the cube; local units; scaled by WS)
    const Wg = (this.world = new THREE.Group()); scene.add(Wg); this.WS = 0.78;
    // terrain top
    const terr = polarGrid(80, 200, RAD, H);
    const tp = terr.attributes.position, nrm = terr.attributes.normal, n = tp.count;
    this.cEmpty = new Float32Array(n * 3); this.cLive = new Float32Array(n * 3);
    const tc = new THREE.Color();
    for (let i = 0; i < n; i++) {
      const x = tp.getX(i), z = tp.getZ(i), h = tp.getY(i), r = Math.hypot(x, z) / RAD, slope = 1 - nrm.getY(i), nz = fbm(x * 9, z * 9);
      const g = 0.24 + h * 1.2 + 0.05 * nz;
      this.cEmpty.set([g * 0.42, g * 0.47, g * 0.56], i * 3);
      tc.setHSL(0.26 + 0.07 * nz, 0.6, 0.2 + 0.1 * nz + h * 0.25);                               // meadow
      if (h > 0.2 || slope > 0.18) tc.lerp(col3(0x7d7469), clamp((h - 0.2) * 6 + (slope - 0.18) * 5));   // rock
      if (h > 0.36) tc.lerp(col3(0xf4f7fb), clamp((h - 0.36) * 14));                               // snow
      tc.lerp(col3(0x6f7480), cityMask(x, z) * 0.92);                                            // city ground
      const dl = Math.hypot(x - LAKE[0], z - LAKE[1]);
      tc.lerp(col3(0xd9c79a), clamp(1 - Math.abs(dl - LAKE_R - 0.03) / 0.035) * 0.8);            // lake beach
      tc.lerp(col3(0xe3d2a4), ss(0.9, 0.98, r) * (1 - cityMask(x, z)));                          // rim beach
      this.cLive.set([tc.r, tc.g, tc.b], i * 3);
    }
    terr.setAttribute('color', new THREE.BufferAttribute(new Float32Array(this.cEmpty), 3));
    this.terrCol = terr.attributes.color;
    const terrain = new THREE.Mesh(terr, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.9 }));
    terrain.receiveShadow = true; terrain.castShadow = true; Wg.add(terrain);
    // skirt + rock underside (strata) + glowing crystals
    const NS = 200, skirt = [], sidx = [];
    for (let j = 0; j <= NS; j++) { const a = (j / NS) * Math.PI * 2, x = Math.cos(a) * RAD, z = Math.sin(a) * RAD; skirt.push(x, H(x, z), z, x, -0.05, z); }
    for (let j = 0; j < NS; j++) { const o = j * 2; sidx.push(o, o + 1, o + 2, o + 1, o + 3, o + 2); }
    const skg = new THREE.BufferGeometry(); skg.setAttribute('position', new THREE.Float32BufferAttribute(skirt, 3)); skg.setIndex(sidx); skg.computeVertexNormals();
    const dirt = new THREE.MeshStandardMaterial({ color: 0x6b4a33, roughness: 0.95, side: THREE.DoubleSide });
    Wg.add(new THREE.Mesh(skg, dirt));
    const under = (this.under = new THREE.Group()); Wg.add(under);
    const ug = polarGrid(40, 120, RAD, (x, z) => { const rr = Math.hypot(x, z) / RAD; return -0.05 - 0.95 * Math.pow(Math.max(0, 1 - rr * rr), 0.8) * (0.65 + 0.5 * fbm(x * 3 + 2, z * 3 + 5)); }, true);
    const up = ug.attributes.position, ucol = [];
    for (let i = 0; i < up.count; i++) { const y = up.getY(i), b = 0.5 + 0.5 * Math.sin(y * 38 + fbm(up.getX(i) * 4, up.getZ(i) * 4) * 4); const c = col3(0x5a3d2b).lerp(col3(0x8a7563), b * 0.6).lerp(col3(0x3b3f4a), clamp(-y * 1.1)); ucol.push(c.r, c.g, c.b); }
    ug.setAttribute('color', new THREE.Float32BufferAttribute(ucol, 3));
    under.add(new THREE.Mesh(ug, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.95, flatShading: true })));
    this.crystalMat = new THREE.MeshBasicMaterial({ color: 0x7ff0ff });
    for (let k = 0; k < 9; k++) { const a = R() * 6.28, rr = R() * 0.45; const c = new THREE.Mesh(new THREE.OctahedronGeometry(0.03 + R() * 0.05, 0), this.crystalMat); c.scale.y = 2.2; c.position.set(Math.cos(a) * rr, -0.3 - (0.5 - rr) * 1.2 - R() * 0.1, Math.sin(a) * rr); under.add(c); }

    // water (lake + river + waterfall): custom unlit shader that follows the time of day
    this.waterU = { uTime: this.uTime, uTod: { value: 0 }, uLife: { value: 0 }, uFlow: { value: 0 } };
    const waterShader = (flow) => new THREE.ShaderMaterial({
      transparent: true, depthWrite: false, uniforms: Object.assign({}, this.waterU, { uFlow: { value: flow } }),
      vertexShader: 'varying vec2 vUv; varying vec3 vW; void main(){ vUv = uv; vec4 w = modelMatrix * vec4(position,1.0); vW = w.xyz; gl_Position = projectionMatrix * viewMatrix * w; }',
      fragmentShader: `varying vec2 vUv; varying vec3 vW; uniform float uTime; uniform float uTod; uniform float uLife; uniform float uFlow;
        void main(){ vec3 V = normalize(cameraPosition - vW); float fr = pow(1.0 - clamp(V.y, 0.0, 1.0), 3.0);
          float sd = smoothstep(0.0,0.5,uTod) * (1.0 - smoothstep(0.5,0.95,uTod)); float nt = smoothstep(0.55,1.0,uTod);
          vec3 deep = mix(mix(vec3(0.06,0.32,0.52), vec3(0.22,0.16,0.32), sd), vec3(0.01,0.04,0.10), nt);
          vec3 refl = mix(mix(vec3(0.62,0.82,0.98), vec3(1.0,0.58,0.32), sd), vec3(0.05,0.2,0.35), nt);
          float rip = (sin(dot(vW.xz, vec2(0.8,0.6)) * 150.0 + uTime * 2.0) + sin(dot(vW.xz, vec2(-0.5,0.86)) * 190.0 - uTime * 1.6) + sin(dot(vW.xz, vec2(0.95,-0.31)) * 120.0 + uTime * 1.1)) / 3.0;
          float flow = sin(vUv.y * 30.0 + sin(vUv.x * 9.0) * 2.0 - uTime * 5.0 * uFlow) * 0.5 + 0.5;
          vec3 c = mix(deep, refl, clamp(0.25 + fr * 0.8 + 0.06 * rip + 0.03 * uFlow * flow, 0.0, 1.0));
          c += vec3(1.0) * pow(max(rip, 0.0), 10.0) * 0.06 * (1.0 - nt) + vec3(0.2,0.8,1.0) * pow(max(rip,0.0), 14.0) * 0.12 * nt;
          vec3 empty = vec3(0.22,0.26,0.32);
          gl_FragColor = vec4(mix(empty, c, uLife), 0.92); }` });
    const lake = new THREE.Mesh(new THREE.CircleGeometry(LAKE_R + 0.035, 64), waterShader(0)); lake.rotation.x = -Math.PI / 2; lake.position.set(LAKE[0], 0.022, LAKE[1]); Wg.add(lake);
    const rv = [], ruv = [], ridx = []; let acc = 0; const RP = new THREE.CatmullRomCurve3(RIVER.map(([x, z]) => new THREE.Vector3(x, 0, z)), false, 'catmullrom', 0.2);
    const RN = 160; for (let i = 0; i <= RN; i++) {
      const u = i / RN, p = RP.getPointAt(u), tg = RP.getTangentAt(u), nx = -tg.z, nz = tg.x, w = 0.024 + 0.01 * u;
      if (i) acc += RP.getLength() / RN;
      rv.push(p.x + nx * w, 0.021, p.z + nz * w, p.x - nx * w, 0.021, p.z - nz * w); ruv.push(0, acc * 8, 1, acc * 8);
      if (i < RN) { const o = i * 2; ridx.push(o, o + 2, o + 1, o + 1, o + 2, o + 3); }
    }
    const rg = new THREE.BufferGeometry(); rg.setAttribute('position', new THREE.Float32BufferAttribute(rv, 3)); rg.setAttribute('uv', new THREE.Float32BufferAttribute(ruv, 2)); rg.setIndex(ridx);
    Wg.add(new THREE.Mesh(rg, waterShader(1)));
    // waterfall ribbon off the rim + mist
    const ex = Math.cos(WF_A), ez = Math.sin(WF_A), fv = [], fuv = [], fid = [], FN = 60;
    for (let i = 0; i <= FN; i++) { const s = i / FN, rr = RAD + 0.01 + 0.16 * Math.pow(s, 0.55), y = 0.02 - 1.15 * Math.pow(s, 1.35), w = 0.032 + 0.05 * s, nx = -ez, nz = ex;
      fv.push(ex * rr + nx * w, y, ez * rr + nz * w, ex * rr - nx * w, y, ez * rr - nz * w); fuv.push(0, s, 1, s); if (i < FN) { const o = i * 2; fid.push(o, o + 2, o + 1, o + 1, o + 2, o + 3); } }
    const fg = new THREE.BufferGeometry(); fg.setAttribute('position', new THREE.Float32BufferAttribute(fv, 3)); fg.setAttribute('uv', new THREE.Float32BufferAttribute(fuv, 2)); fg.setIndex(fid);
    this.fallMat = new THREE.ShaderMaterial({ transparent: true, depthWrite: false, side: THREE.DoubleSide, blending: THREE.AdditiveBlending,
      uniforms: { uTime: this.uTime, uOp: { value: 0 }, uTod: this.waterU.uTod },
      vertexShader: 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }',
      fragmentShader: `varying vec2 vUv; uniform float uTime; uniform float uOp; uniform float uTod;
        float h1(vec2 p){ return fract(sin(dot(p, vec2(12.9898,78.233))) * 43758.5453); }
        void main(){ float x = vUv.x; float st = 0.0;
          for (int k = 0; k < 4; k++) { float fk = float(k); float col = floor(x * (10.0 + fk * 7.0)); float sp = 0.8 + h1(vec2(col, fk));
            st += smoothstep(0.55, 1.0, sin((vUv.y * (8.0 + fk * 3.0) - uTime * 2.6 * sp) * 6.283 + h1(vec2(col, fk + 7.0)) * 6.0)) * 0.35; }
          float edge = smoothstep(0.0, 0.25, x) * smoothstep(1.0, 0.75, x);
          float a = (0.25 + st) * edge * (1.0 - smoothstep(0.55, 1.0, vUv.y));
          vec3 c = mix(vec3(0.75,0.92,1.0), vec3(0.35,0.75,1.0), smoothstep(0.6, 1.0, uTod));
          gl_FragColor = vec4(c * a * uOp, 1.0); }` });
    Wg.add(new THREE.Mesh(fg, this.fallMat));
    const mist = [], mseed = [], mcol = []; for (let i = 0; i < 160; i++) { const s = R(); mist.push(ex * (RAD + 0.1 + 0.12 * R()) + (R() - 0.5) * 0.12, -0.25 - s * 0.75, ez * (RAD + 0.1 + 0.12 * R()) + (R() - 0.5) * 0.12); mseed.push(R()); mcol.push(0.7, 0.85, 1); }
    const mg = new THREE.BufferGeometry(); mg.setAttribute('position', new THREE.Float32BufferAttribute(mist, 3)); mg.setAttribute('aSeed', new THREE.Float32BufferAttribute(mseed, 1)); mg.setAttribute('aCol', new THREE.Float32BufferAttribute(mcol, 3));
    this.mistMat = sparkMat(0.03); Wg.add(new THREE.Points(mg, this.mistMat));

    // ---------------- city: merged walls (facade map by day, lit windows at night) + roofs; grows from the ground
    const CELLS = 32, CP = 32;
    const mkCanvas = (fn) => { const c = document.createElement('canvas'); c.width = c.height = CELLS * CP; const x = c.getContext('2d'); fn(x); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = 4; t.generateMipmaps = true; return t; };
    const RW = rng(5); const lit = [];
    for (let i = 0; i < CELLS * CELLS; i++) lit.push(RW());
    const facade = mkCanvas((x) => { x.fillStyle = '#e4e9f0'; x.fillRect(0, 0, CELLS * CP, CELLS * CP);
      for (let cy = 0; cy < CELLS; cy++) for (let cx = 0; cx < CELLS; cx++) { const g = x.createLinearGradient(0, cy * CP + 5, 0, cy * CP + 27); g.addColorStop(0, '#5d86ad'); g.addColorStop(1, '#22405f'); x.fillStyle = g; x.fillRect(cx * CP + 6, cy * CP + 5, 20, 22); } });
    const winTex = mkCanvas((x) => { x.fillStyle = '#000'; x.fillRect(0, 0, CELLS * CP, CELLS * CP);
      for (let cy = 0; cy < CELLS; cy++) for (let cx = 0; cx < CELLS; cx++) { const v = lit[cy * CELLS + cx]; if (v < 0.42) continue; x.fillStyle = v > 0.86 ? '#9fe7ff' : v > 0.5 ? '#ffd28f' : '#ffb766'; x.fillRect(cx * CP + 6, cy * CP + 5, 20, 22); } });
    const growPatch = (mat, emissive) => {
      mat.onBeforeCompile = (sh) => {
        sh.uniforms.uNight = this.uNight; sh.uniforms.uGrow = this.uGrow;
        sh.vertexShader = 'attribute float aOn; attribute float aBase; attribute float aDel; uniform float uGrow; varying float vOn;\n' + sh.vertexShader.replace('#include <begin_vertex>', `#include <begin_vertex>
          float gk = clamp((uGrow - aDel) / 0.32, 0.0, 1.0); gk = 1.0 - pow(1.0 - gk, 3.0);
          transformed.y = aBase + (transformed.y - aBase) * max(0.002, gk); vOn = aOn;`);
        sh.fragmentShader = 'uniform float uNight; varying float vOn;\n' + sh.fragmentShader.replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
          ${emissive ? 'totalEmissiveRadiance *= smoothstep(vOn, vOn + 0.08, uNight);' : ''}`);
      };
      mat.customProgramCacheKey = () => 'grow' + (emissive ? 'E' : 'P');
      return mat;
    };
    const walls = { p: [], n: [], uv: [], c: [], on: [], base: [], del: [] }, roofs = { p: [], n: [], c: [], on: [], base: [], del: [] };
    const CWW = 0.0135, CHH = 0.017;
    const addQuad = (B, a, b, c, d, nn, uvs, color, on, base, del) => {
      for (const v of [a, b, c, a, c, d]) B.p.push(...v);
      for (let k = 0; k < 6; k++) { B.n.push(...nn); B.c.push(color.r, color.g, color.b); B.on.push(on); B.base.push(base); B.del.push(del); }
      if (uvs) for (const k of [0, 1, 2, 0, 2, 3]) B.uv.push(...uvs[k]);
    };
    const building = (cx, cz, w, d, h, base, color, on, del, rot = 0) => {
      const cs = Math.cos(rot), sn = Math.sin(rot), P2 = (x, z) => [cx + x * cs - z * sn, cz + x * sn + z * cs];
      const corners = [[-w / 2, -d / 2], [w / 2, -d / 2], [w / 2, d / 2], [-w / 2, d / 2]].map(([x, z]) => P2(x, z));
      const ou = Math.floor(RW() * CELLS) / CELLS, ov = Math.floor(RW() * CELLS) / CELLS;
      for (let k = 0; k < 4; k++) {
        const [ax, az] = corners[k], [bx, bz] = corners[(k + 1) % 4], len = Math.hypot(bx - ax, bz - az);
        const nx = (bz - az) / len, nz = -(bx - ax) / len;          // outward for CCW-from-above corners
        const U = len / CWW / CELLS, V = h / CHH / CELLS, u0 = ou + k * 0.37;
        addQuad(walls, [bx, base, bz], [ax, base, az], [ax, base + h, az], [bx, base + h, bz], [nx, 0, nz],
          [[u0 + U, ov], [u0, ov], [u0, ov + V], [u0 + U, ov + V]], color, on, base, del);
      }
      const y = base + h, rc = color.clone().multiplyScalar(0.72);
      addQuad(roofs, [corners[0][0], y, corners[0][1]], [corners[3][0], y, corners[3][1]], [corners[2][0], y, corners[2][1]], [corners[1][0], y, corners[1][1]], [0, 1, 0], null, rc, on, base, del);
    };
    // corners order check: (-w/2,-d/2)->(w/2,-d/2)->(w/2,d/2)->(-w/2,d/2) is clockwise seen from +y with z down; outward normal (dz, -dx)/len
    const tint = [0xe6eaf0, 0xc9d3df, 0x9fb7d3, 0xd9c6a8, 0xa9b4c2, 0xeee6d8, 0x8fb3d9].map(col3);
    const blocks = [];
    const zEdges = [-0.6, ...CROSS.flatMap((z) => [z - CW / 2, z + CW / 2]), 0.66];
    for (let k = 0; k < zEdges.length; k += 2) {
      const z0 = zEdges[k] + 0.006, z1 = zEdges[k + 1] - 0.006;
      blocks.push([-0.93, AVX - AVW / 2 - 0.006, z0, z1], [AVX + AVW / 2 + 0.006, -0.07, z0, z1]);
    }
    for (const [x0, x1, z0, z1] of blocks) {
      const nx = Math.max(1, Math.round((x1 - x0) / 0.072)), nz = Math.max(1, Math.round((z1 - z0) / 0.07));
      for (let i = 0; i < nx; i++) for (let j = 0; j < nz; j++) {
        const lx0 = x0 + ((x1 - x0) * i) / nx, lx1 = x0 + ((x1 - x0) * (i + 1)) / nx, lz0 = z0 + ((z1 - z0) * j) / nz, lz1 = z0 + ((z1 - z0) * (j + 1)) / nz;
        const cx = (lx0 + lx1) / 2, cz = (lz0 + lz1) / 2;
        if (Math.hypot(cx, cz) > 0.95 || Math.hypot(cx - HERO[0], cz - HERO[1]) < 0.09 || RW() < 0.07) continue;
        const centre = Math.exp(-((cz * cz) / 0.1 + ((cx - AVX) * (cx - AVX)) / 0.07));
        const h = 0.05 + 0.3 * centre * (0.55 + 0.7 * RW()) + 0.04 * RW();
        const w = lx1 - lx0 - 0.012 - RW() * 0.008, d = lz1 - lz0 - 0.012 - RW() * 0.008;
        const base = 0.05, del = clamp(0.2 + 0.35 * (1 - centre) + 0.1 * RW(), 0, 0.65);
        const c = tint[Math.floor(RW() * tint.length)];
        if (h > 0.2 && RW() < 0.5) {                                     // setback tower
          building(cx, cz, w, d, h * 0.62, base, c, 0.2 + 0.7 * RW(), del);
          building(cx, cz, w * 0.7, d * 0.7, h * 0.38, base + h * 0.62, c, 0.2 + 0.7 * RW(), del); walls.base.fill(base, walls.base.length - 24); roofs.base.fill(base, roofs.base.length - 6);
        } else building(cx, cz, w, d, h, base, c, 0.2 + 0.7 * RW(), del);
      }
    }
    // hero tower (setbacks) — its spire and hologram ring are separate
    const hc = col3(0xc6d8ec);
    for (const [w, h0, h1] of [[0.11, 0, 0.3], [0.085, 0.3, 0.46], [0.06, 0.46, 0.58]]) {
      building(HERO[0], HERO[1], w, w, h1 - h0, 0.05 + h0, hc, 0.25 + 0.5 * RW(), 0.1, 0.3);
      walls.base.fill(0.05, walls.base.length - 24); roofs.base.fill(0.05, roofs.base.length - 6);
    }
    // suburb houses (pitched roofs) on the meadow
    const houses = [];
    for (let i = 0; i < 400 && houses.length < 70; i++) {
      const a = RW() * Math.PI * 2, rr = 0.15 + RW() * 0.78, x = Math.cos(a) * rr, z = Math.sin(a) * rr;
      if (cityMask(x, z) > 0.02 || Math.hypot(x - LAKE[0], z - LAKE[1]) < LAKE_R + 0.08 || riverD(x, z) < 0.07 || Math.hypot(x - MTN[0], z - MTN[1]) < 0.3 || Math.hypot(x - WHEEL[0], z - WHEEL[1]) < 0.1) continue;
      if (houses.some(([hx, hz]) => Math.hypot(hx - x, hz - z) < 0.045) || (x > -0.6 && x < -0.3 && z > 0.5)) continue;
      houses.push([x, z]);
      const base = H(x, z) - 0.004, w = 0.026 + RW() * 0.012, d = 0.02 + RW() * 0.01, hh = 0.022 + RW() * 0.012, rot = RW() * Math.PI;
      building(x, z, w, d, hh, base, col3([0xf3ede2, 0xf6f1e8, 0xe9dfcf, 0xdfe7ee][Math.floor(RW() * 4)]), 0.3 + 0.6 * RW(), 0.35 + 0.3 * RW(), rot);
      roofs.p.splice(roofs.p.length - 18); roofs.n.splice(roofs.n.length - 18); roofs.c.splice(roofs.c.length - 18); roofs.on.splice(roofs.on.length - 6); roofs.base.splice(roofs.base.length - 6); roofs.del.splice(roofs.del.length - 6);
      // gable roof
      const cs = Math.cos(rot), sn = Math.sin(rot), P3 = (px, py, pz) => [x + px * cs - pz * sn, py, z + px * sn + pz * cs];
      const y0 = base + hh, y1 = y0 + 0.016, rcol = col3([0xb5523b, 0x8f3d2c, 0x4f5d73, 0x9a6a4b][Math.floor(RW() * 4)]), del = roofs.del.length ? 0.4 : 0.4;
      const ow = w / 2 + 0.004, od = d / 2 + 0.004;
      const q = (a, b, c, d2, nn) => addQuad(roofs, a, b, c, d2, nn, null, rcol, 0.9, base, 0.35 + 0.3 * RW());
      q(P3(-ow, y0, -od), P3(-ow, y1, 0), P3(ow, y1, 0), P3(ow, y0, -od), [-sn * 0, 0.7, 0]);
      q(P3(ow, y0, od), P3(ow, y1, 0), P3(-ow, y1, 0), P3(-ow, y0, od), [0, 0.7, 0]);
      for (const sx of [-1, 1]) { const a2 = P3(sx * w / 2, y0, -d / 2), b2 = P3(sx * w / 2, y0, d / 2), c2 = P3(sx * w / 2, y1, 0); for (const v of sx > 0 ? [a2, c2, b2] : [a2, b2, c2]) roofs.p.push(...v); for (let k = 0; k < 3; k++) { roofs.n.push(sx * cs, 0, sx * sn); roofs.c.push(0.9, 0.88, 0.84); roofs.on.push(0.9); roofs.base.push(base); roofs.del.push(0.5); } }
    }
    const mkGeo = (B, uv) => { const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(B.p, 3)); g.setAttribute('normal', new THREE.Float32BufferAttribute(B.n, 3)); g.setAttribute('color', new THREE.Float32BufferAttribute(B.c, 3)); if (uv) g.setAttribute('uv', new THREE.Float32BufferAttribute(B.uv, 2)); g.setAttribute('aOn', new THREE.Float32BufferAttribute(B.on, 1)); g.setAttribute('aBase', new THREE.Float32BufferAttribute(B.base, 1)); g.setAttribute('aDel', new THREE.Float32BufferAttribute(B.del, 1)); return g; };
    this.wallMat = growPatch(new THREE.MeshStandardMaterial({ map: facade, vertexColors: true, roughness: 0.45, metalness: 0.25, emissive: 0xffffff, emissiveMap: winTex, emissiveIntensity: 2.4 }), true);
    this.blds = new THREE.Mesh(mkGeo(walls, true), this.wallMat); this.blds.castShadow = true; this.blds.receiveShadow = true; Wg.add(this.blds);
    this.roofMat = growPatch(new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.7, metalness: 0.1, side: THREE.DoubleSide }), false);
    this.roofs = new THREE.Mesh(mkGeo(roofs, false), this.roofMat); this.roofs.castShadow = true; this.roofs.receiveShadow = true; Wg.add(this.roofs);
    // streets (dark asphalt with lane dashes) over the city ground
    const streetMat = new THREE.MeshStandardMaterial({ color: 0x2b3038, roughness: 0.8 });
    const sgs = [];
    const av = new THREE.PlaneGeometry(AVW, 1.3); av.rotateX(-Math.PI / 2); av.translate(AVX, 0.053, 0.03); sgs.push(av);
    for (const z of CROSS) { const g = new THREE.PlaneGeometry(0.9, CW); g.rotateX(-Math.PI / 2); g.translate(-0.5, 0.0518, z); sgs.push(g); }
    this.streets = new THREE.Mesh(mergeGeometries(sgs), streetMat); this.streets.receiveShadow = true; Wg.add(this.streets);
    const dashM = new THREE.MeshBasicMaterial({ color: 0xd8dde6 }); const dg = [];
    for (let z = -0.58; z < 0.64; z += 0.035) { const g = new THREE.PlaneGeometry(0.0025, 0.016); g.rotateX(-Math.PI / 2); g.translate(AVX, 0.0538, z); dg.push(g); }
    Wg.add(new THREE.Mesh(mergeGeometries(dg), dashM));
    // street lights along the avenue (poles + lamp heads that glow at dusk)
    const poles = [], lamps = [];
    for (let z = -0.56; z < 0.64; z += 0.06) for (const sx of [-1, 1]) {
      const x = AVX + sx * (AVW / 2 - 0.006);
      const p = new THREE.CylinderGeometry(0.0012, 0.0016, 0.03, 5); p.translate(x, 0.05 + 0.015, z); poles.push(p);
      const l = new THREE.SphereGeometry(0.0022, 8, 6); l.translate(x - sx * 0.004, 0.081, z); lamps.push(l);
    }
    Wg.add(new THREE.Mesh(mergeGeometries(poles), new THREE.MeshStandardMaterial({ color: 0x30343c, metalness: 0.6, roughness: 0.4 })));
    this.lampMat = new THREE.MeshBasicMaterial({ color: 0xffd9a0 }); Wg.add(new THREE.Mesh(mergeGeometries(lamps), this.lampMat));
    // hero spire + beacon + hologram ring
    const sx0 = HERO[0], sz0 = HERO[1];
    this.spire = new THREE.Group(); this.spire.position.set(sx0, 0.63, sz0); Wg.add(this.spire);
    const spm = new THREE.MeshStandardMaterial({ color: 0xdbe6f3, metalness: 0.8, roughness: 0.2 });
    const s1 = new THREE.Mesh(new THREE.CylinderGeometry(0.004, 0.012, 0.12, 12), spm); s1.position.y = 0.06; this.spire.add(s1);
    this.beacon = new THREE.Mesh(new THREE.SphereGeometry(0.006, 10, 8), new THREE.MeshBasicMaterial({ color: 0xff3b3b })); this.beacon.position.y = 0.125; this.spire.add(this.beacon);
    this.holo = new THREE.Group(); this.holo.position.y = 0.0; this.spire.add(this.holo);
    this.holoMat = new THREE.MeshBasicMaterial({ color: 0x00c9ff, transparent: true, opacity: 0.0, blending: THREE.AdditiveBlending, depthWrite: false });
    for (const [rr, y] of [[0.075, 0.0], [0.06, 0.03]]) { const t = new THREE.Mesh(new THREE.TorusGeometry(rr, 0.0022, 6, 96), this.holoMat); t.rotation.x = Math.PI / 2; t.position.y = y; this.holo.add(t); }
    // ferris wheel
    const FW = (this.wheel = new THREE.Group()); const wb = H(...WHEEL); FW.position.set(WHEEL[0], wb, WHEEL[1]); FW.rotation.y = 0.9; Wg.add(FW);
    const fwm = new THREE.MeshStandardMaterial({ color: 0xf2f5fa, metalness: 0.5, roughness: 0.3 });
    for (const sx of [-1, 1]) { const leg = new THREE.Mesh(new THREE.CylinderGeometry(0.003, 0.004, 0.16, 6), fwm); leg.position.set(0, 0.075, sx * 0.025); leg.rotation.x = sx * 0.2; FW.add(leg); }
    this.wheelRot = new THREE.Group(); this.wheelRot.position.y = 0.15; FW.add(this.wheelRot);
    for (const zz of [-0.012, 0.012]) { const rim = new THREE.Mesh(new THREE.TorusGeometry(0.11, 0.0022, 6, 64), fwm); rim.position.z = zz; this.wheelRot.add(rim); }
    this.cabins = []; this.bulbMat = new THREE.MeshBasicMaterial({ color: 0xffe2a8 });
    const cabC = [0xff6b6b, 0x4dabf7, 0xffd43b, 0x69db7c, 0xb197fc, 0xff922b];
    for (let k = 0; k < 12; k++) {
      const a = (k / 12) * Math.PI * 2;
      const sp2 = new THREE.Mesh(new THREE.CylinderGeometry(0.0009, 0.0009, 0.11, 4), fwm); sp2.rotation.z = a; sp2.position.set(Math.cos(a + Math.PI / 2) * 0.055, Math.sin(a + Math.PI / 2) * 0.055, 0); this.wheelRot.add(sp2);
      const cab = new THREE.Mesh(new THREE.BoxGeometry(0.014, 0.013, 0.016), new THREE.MeshStandardMaterial({ color: cabC[k % 6], roughness: 0.5 })); cab.userData.a = a; cab.castShadow = true; FW.add(cab); this.cabins.push(cab);
      for (const j of [0, 0.5]) { const b = new THREE.Mesh(new THREE.SphereGeometry(0.0022, 6, 4), this.bulbMat); const aa = a + j * (Math.PI / 6); b.position.set(Math.cos(aa) * 0.11, Math.sin(aa) * 0.11, 0.014); this.wheelRot.add(b); }
    }
    // trees (instanced pines + round trees + trunks)
    const pineG = mergeGeometries([new THREE.ConeGeometry(0.022, 0.05, 8).translate(0, 0.045, 0), new THREE.ConeGeometry(0.017, 0.042, 8).translate(0, 0.072, 0)]);
    const roundG = new THREE.IcosahedronGeometry(0.024, 1).translate(0, 0.05, 0);
    const trunkG = new THREE.CylinderGeometry(0.0025, 0.0035, 0.03, 5).translate(0, 0.015, 0);
    const spots = [];
    for (let i = 0; i < 3000 && spots.length < 620; i++) {
      const a = R() * Math.PI * 2, rr = Math.sqrt(R()) * 0.98 * RAD, x = Math.cos(a) * rr, z = Math.sin(a) * rr, h = H(x, z);
      if (cityMask(x, z) > 0.05 || Math.hypot(x - LAKE[0], z - LAKE[1]) < LAKE_R + 0.05 || riverD(x, z) < 0.045 || h > 0.3 || rr > RAD * 0.9) continue;
      if (fbm(x * 3.5 + 11, z * 3.5 + 4) < 0.4 && R() > 0.15) continue;
      if (houses.some(([hx, hz]) => Math.hypot(hx - x, hz - z) < 0.03) || Math.hypot(x - WHEEL[0], z - WHEEL[1]) < 0.09 || (x > -0.6 && x < -0.3 && z > 0.5)) continue;
      spots.push([x, h - 0.003, z, R(), R() < 0.55 + h, 0.7 + R() * 0.7, R()]);
    }
    const pines = spots.filter((s) => s[4]), rounds = spots.filter((s) => !s[4]);
    const tMat = new THREE.MeshStandardMaterial({ roughness: 0.85, flatShading: true });
    this.pineI = new THREE.InstancedMesh(pineG, tMat, pines.length); this.roundI = new THREE.InstancedMesh(roundG, tMat.clone(), rounds.length);
    this.trunkI = new THREE.InstancedMesh(trunkG, new THREE.MeshStandardMaterial({ color: 0x5a3e2b, roughness: 0.9 }), spots.length);
    const cc = new THREE.Color();
    pines.forEach((s, k) => this.pineI.setColorAt(k, cc.setHSL(0.37 + 0.05 * s[6], 0.55, 0.13 + 0.07 * s[6])));
    rounds.forEach((s, k) => this.roundI.setColorAt(k, cc.setHSL(0.22 + 0.11 * s[6], 0.62, 0.2 + 0.09 * s[6])));
    for (const m of [this.pineI, this.roundI, this.trunkI]) { m.castShadow = true; m.receiveShadow = true; Wg.add(m); }
    this.pines = pines; this.rounds = rounds; this.spots = spots;
    // windmills on the hills
    this.mills = [];
    for (const [x, z] of [[0.8, 0.22], [0.66, 0.78], [0.12, 0.86], [-0.2, -0.86]]) {
      const g = new THREE.Group(); g.position.set(x, H(x, z) - 0.004, z); g.rotation.y = Math.atan2(x, z) + Math.PI; Wg.add(g);
      const tw = new THREE.Mesh(new THREE.CylinderGeometry(0.004, 0.008, 0.12, 8), fwm); tw.position.y = 0.06; tw.castShadow = true; g.add(tw);
      const hub = new THREE.Group(); hub.position.set(0, 0.12, 0.008); g.add(hub);
      for (let k = 0; k < 3; k++) { const bl = new THREE.Mesh(new THREE.BoxGeometry(0.006, 0.07, 0.0015), fwm); bl.position.y = 0.035; const p2 = new THREE.Group(); p2.rotation.z = (k * Math.PI * 2) / 3; p2.add(bl); hub.add(p2); }
      g.userData.hub = hub; this.mills.push(g);
    }
    // cars (instanced bodies + head/tail lights)
    const lanes = [];
    for (const s of [-1, 1]) lanes.push({ a: [AVX + s * 0.022, -0.6], b: [AVX + s * 0.022, 0.66], n: 11, sp: 0.085 * s });
    for (const z of CROSS) for (const s of [-1, 1]) lanes.push({ a: [-0.93, z + s * 0.009], b: [-0.07, z + s * 0.009], n: 3, sp: 0.06 * s });
    this.carList = [];
    lanes.forEach((L, li) => { for (let k = 0; k < L.n; k++) this.carList.push({ L, o: (k + R() * 0.6) / L.n, li }); });
    const NC = this.carList.length;
    this.carI = new THREE.InstancedMesh(new THREE.BoxGeometry(0.008, 0.0065, 0.016).translate(0, 0.0035, 0), new THREE.MeshStandardMaterial({ roughness: 0.35, metalness: 0.5 }), NC);
    const carC = [0xe03131, 0xf8f9fa, 0x1c7ed6, 0x212529, 0xfab005, 0x868e96];
    this.carList.forEach((c, k) => this.carI.setColorAt(k, col3(carC[k % carC.length])));
    this.headI = new THREE.InstancedMesh(new THREE.BoxGeometry(0.007, 0.0022, 0.0012), (this.headMat = new THREE.MeshBasicMaterial({ color: 0xfff6d8 })), NC);
    this.tailI = new THREE.InstancedMesh(new THREE.BoxGeometry(0.007, 0.0022, 0.0012), (this.tailMat = new THREE.MeshBasicMaterial({ color: 0xff3030 })), NC);
    this.carI.castShadow = true; Wg.add(this.carI, this.headI, this.tailI);
    // elevated train loop (bridge over the waterfall)
    const TR = 1.03, TY = 0.21;
    const trk = []; for (let k = 0; k < 160; k++) { const a = (k / 160) * Math.PI * 2; trk.push(new THREE.Vector3(Math.cos(a) * TR, TY, Math.sin(a) * TR)); }
    this.track = new THREE.CatmullRomCurve3(trk, true);
    const trackMat = new THREE.MeshStandardMaterial({ color: 0xd5dde8, metalness: 0.6, roughness: 0.3 });
    const tube = new THREE.TubeGeometry(this.track, 320, 0.006, 6, true); tube.scale(1, 0.6, 1); tube.translate(0, TY * 0.4, 0); Wg.add(new THREE.Mesh(tube, trackMat));
    const pil = []; for (let k = 0; k < 36; k++) { const a = (k / 36) * Math.PI * 2, x = Math.cos(a) * TR, z = Math.sin(a) * TR; const gy = Math.min(H(x, z), 0.02); const hh = TY - gy; const g = new THREE.CylinderGeometry(0.0025, 0.0035, hh, 6); g.translate(x, gy + hh / 2, z); pil.push(g); }
    Wg.add(new THREE.Mesh(mergeGeometries(pil), trackMat));
    this.train = [];
    const trainBody = new THREE.MeshStandardMaterial({ color: 0xf5f7fb, metalness: 0.3, roughness: 0.25 });
    this.trainWin = new THREE.MeshStandardMaterial({ color: 0x1b2a3f, emissive: 0x9fe7ff, emissiveIntensity: 0.2, roughness: 0.2 });
    const stripe = new THREE.MeshBasicMaterial({ color: 0x00c9ff });
    for (let k = 0; k < 6; k++) {
      const g = new THREE.Group();
      const b = new THREE.Mesh(new THREE.CapsuleGeometry(0.0085, 0.036, 4, 10), trainBody); b.rotation.z = Math.PI / 2; b.castShadow = true; g.add(b);
      const w = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.0045, 0.0172), this.trainWin); w.position.y = 0.002; g.add(w);
      const st = new THREE.Mesh(new THREE.BoxGeometry(0.044, 0.0015, 0.0174), stripe); st.position.y = -0.003; g.add(st);
      Wg.add(g); this.train.push(g);
    }
    // hot air balloons
    const balTex = (cA, cB) => { const c = document.createElement('canvas'); c.width = 128; c.height = 64; const x = c.getContext('2d'); for (let i = 0; i < 8; i++) { x.fillStyle = i % 2 ? cA : cB; x.fillRect(i * 16, 0, 16, 64); } const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t; };
    this.balloons = [];
    [[0.15, 0.25, ['#ff6b6b', '#fff3bf']], [0.62, -0.62, ['#4dabf7', '#ffffff']], [-0.15, 0.55, ['#ffd43b', '#e8590c']]].forEach(([x, z, [a, b]], k) => {
      const g = new THREE.Group(); const env = new THREE.Mesh(new THREE.SphereGeometry(0.035, 24, 16), new THREE.MeshStandardMaterial({ map: balTex(a, b), roughness: 0.6 }));
      env.scale.y = 1.18; env.castShadow = true; g.add(env);
      const bk = new THREE.Mesh(new THREE.BoxGeometry(0.012, 0.01, 0.012), new THREE.MeshStandardMaterial({ color: 0x8a5a35 })); bk.position.y = -0.058; g.add(bk);
      const fl = new THREE.Mesh(new THREE.SphereGeometry(0.004, 8, 6), new THREE.MeshBasicMaterial({ color: 0xffb35c })); fl.position.y = -0.045; g.add(fl);
      g.userData = { x, z, k }; Wg.add(g); this.balloons.push(g);
    });
    // birds (instanced V that flaps by flipping its y scale)
    const bv = new Float32Array([-1, 0.35, 0.1, 0, 0, 0.35, 0, 0, -0.25, 1, 0.35, 0.1, 0, 0, -0.25, 0, 0, 0.35]);
    const bgeo = new THREE.BufferGeometry(); bgeo.setAttribute('position', new THREE.BufferAttribute(bv, 3)); bgeo.computeVertexNormals();
    this.birdI = new THREE.InstancedMesh(bgeo, new THREE.MeshBasicMaterial({ color: 0x1d2433, side: THREE.DoubleSide }), 14); Wg.add(this.birdI);
    this.birdSeed = Array.from({ length: 14 }, () => [R(), R(), R()]);
    // clouds
    this.cloudMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 1, transparent: true, opacity: 0 });
    this.clouds = [];
    for (let i = 0; i < 8; i++) {
      const g = new THREE.Group(); const m = 4 + Math.floor(R() * 4);
      for (let j = 0; j < m; j++) { const s = new THREE.Mesh(new THREE.SphereGeometry(0.035 + R() * 0.035, 16, 12), this.cloudMat); s.position.set((j - m / 2) * 0.04 + R() * 0.01, R() * 0.025, (R() - 0.5) * 0.05); s.scale.y = 0.75; g.add(s); }
      g.userData = { a: (i / 8) * Math.PI * 2 + R() * 0.4, r: 0.5 + R() * 0.55, y: 0.48 + R() * 0.2 }; Wg.add(g); this.clouds.push(g);
    }
    // floating rocks orbiting the island (pocket-universe debris)
    this.rocks = [];
    const rockM = new THREE.MeshStandardMaterial({ color: 0x6d5a4a, roughness: 0.95, flatShading: true });
    for (let i = 0; i < 12; i++) { const m = new THREE.Mesh(new THREE.DodecahedronGeometry(0.02 + R() * 0.05, 0), rockM); m.userData = { a: R() * 6.28, r: 1.35 + R() * 0.6, y: -0.6 + R() * 0.8, s: 0.05 + R() * 0.08, sp: R() }; m.castShadow = true; Wg.add(m); this.rocks.push(m); }
    // sparkles (life burst) + fireflies (night)
    const spk = [], spSeed = [], spCol = [];
    for (let i = 0; i < 360; i++) { spk.push(0, 0, 0); spSeed.push(R()); const c = R() > 0.5 ? [0.45, 0.9, 1] : [1, 0.86, 0.55]; spCol.push(...c); }
    const spg = new THREE.BufferGeometry(); spg.setAttribute('position', new THREE.Float32BufferAttribute(spk, 3)); spg.setAttribute('aSeed', new THREE.Float32BufferAttribute(spSeed, 1)); spg.setAttribute('aCol', new THREE.Float32BufferAttribute(spCol, 3));
    this.spkMat = sparkMat(0.05); this.spkPts = new THREE.Points(spg, this.spkMat); scene.add(this.spkPts); this.spkSeed = spSeed;
    const ff = [], ffs = [], ffc = [];
    for (let i = 0; i < 220; i++) { const s = this.spots[Math.floor(R() * this.spots.length)]; ff.push(s[0] + (R() - 0.5) * 0.06, s[1] + 0.02 + R() * 0.06, s[2] + (R() - 0.5) * 0.06); ffs.push(R()); ffc.push(0.75, 1, 0.45); }
    const ffg = new THREE.BufferGeometry(); ffg.setAttribute('position', new THREE.Float32BufferAttribute(ff, 3)); ffg.setAttribute('aSeed', new THREE.Float32BufferAttribute(ffs, 1)); ffg.setAttribute('aCol', new THREE.Float32BufferAttribute(ffc, 3));
    this.ffMat = sparkMat(0.012); Wg.add(new THREE.Points(ffg, this.ffMat));

    // ---------------- astronaut (white suit, gold visor, backpack lights, knee/elbow rings, boots)
    const A = (this.astro = new THREE.Group()); scene.add(A);
    const suit = new THREE.MeshStandardMaterial({ color: 0xf3f5f9, roughness: 0.5 });
    const joint = new THREE.MeshStandardMaterial({ color: 0xaab6c8, roughness: 0.45, metalness: 0.3 });
    const dark = new THREE.MeshStandardMaterial({ color: 0x5b6577, roughness: 0.6 });
    const visor = new THREE.MeshStandardMaterial({ color: 0xffc46b, metalness: 1.0, roughness: 0.06, envMapIntensity: 1.6 });
    const cap = (r, l, m) => { const x = new THREE.Mesh(new THREE.CapsuleGeometry(r, l, 6, 16), m); x.castShadow = true; return x; };
    const body = cap(0.17, 0.2, suit); body.position.y = 0.52; A.add(body);
    const belt = new THREE.Mesh(new THREE.TorusGeometry(0.168, 0.018, 8, 40), joint); belt.rotation.x = Math.PI / 2; belt.position.y = 0.42; A.add(belt);
    const pack = new THREE.Mesh(new THREE.BoxGeometry(0.27, 0.32, 0.13), joint); pack.position.set(0, 0.57, -0.18); pack.castShadow = true; A.add(pack);
    this.packL = new THREE.MeshBasicMaterial({ color: 0x00c9ff });
    for (const x of [-0.08, 0, 0.08]) { const l = new THREE.Mesh(new THREE.BoxGeometry(0.035, 0.012, 0.01), this.packL); l.position.set(x, 0.66, -0.247); A.add(l); }
    const chest = new THREE.Mesh(new THREE.BoxGeometry(0.13, 0.08, 0.03), dark); chest.position.set(0, 0.6, 0.162); A.add(chest);
    for (const [x, c] of [[-0.035, 0xff4d4d], [0, 0x00c9ff], [0.035, 0x51cf66]]) { const b = new THREE.Mesh(new THREE.CylinderGeometry(0.009, 0.009, 0.01, 10), new THREE.MeshBasicMaterial({ color: c })); b.rotation.x = Math.PI / 2; b.position.set(x, 0.6, 0.18); A.add(b); }
    const head = (this.aHead = new THREE.Group()); head.position.y = 0.86; A.add(head);
    const helm = new THREE.Mesh(new THREE.SphereGeometry(0.235, 48, 32), suit); helm.castShadow = true; head.add(helm);
    const rimH = new THREE.Mesh(new THREE.TorusGeometry(0.17, 0.014, 10, 48), joint); rimH.position.z = 0.12; head.add(rimH);
    const vis = new THREE.Mesh(new THREE.SphereGeometry(0.205, 48, 32, -Math.PI * 0.4, Math.PI * 0.8, Math.PI * 0.27, Math.PI * 0.4), visor); vis.position.z = 0.045; head.add(vis);
    const ant = new THREE.Mesh(new THREE.CylinderGeometry(0.004, 0.004, 0.12, 6), joint); ant.position.set(0.15, 0.17, -0.05); ant.rotation.z = -0.3; head.add(ant);
    this.antTip = new THREE.Mesh(new THREE.SphereGeometry(0.014, 10, 8), new THREE.MeshBasicMaterial({ color: 0xff5252 })); this.antTip.position.set(0.168, 0.225, -0.05); head.add(this.antTip);
    const lamp = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 0.03, 16), joint); lamp.rotation.z = Math.PI / 2; lamp.position.set(-0.235, 0.02, 0); head.add(lamp);
    const neck = new THREE.Mesh(new THREE.TorusGeometry(0.15, 0.032, 12, 40), joint); neck.rotation.x = Math.PI / 2; neck.position.y = 0.7; A.add(neck);
    const limb = (x, y, upper, lower, r, endM, ring) => {
      const sh = new THREE.Group(); sh.position.set(x, y, 0); A.add(sh);
      const u = cap(r, upper, suit); u.position.y = -upper / 2 - r * 0.6; sh.add(u);
      const el = new THREE.Group(); el.position.y = -upper - r; sh.add(el);
      const rg2 = new THREE.Mesh(new THREE.TorusGeometry(r * 1.02, r * 0.28, 8, 24), joint); rg2.rotation.x = Math.PI / 2; el.add(rg2);
      const l = cap(r * 0.92, lower, suit); l.position.y = -lower / 2 - r * 0.5; el.add(l);
      const end = new THREE.Mesh(ring ? new THREE.BoxGeometry(r * 2.1, r * 1.3, r * 2.8) : new THREE.SphereGeometry(r * 1.15, 16, 12), endM); end.position.set(0, -lower - r * (ring ? 1.1 : 1), ring ? r * 0.35 : 0); end.castShadow = true; el.add(end);
      return { sh, el };
    };
    this.armL = limb(-0.22, 0.66, 0.11, 0.1, 0.055, dark, false); this.armR = limb(0.22, 0.66, 0.11, 0.1, 0.055, dark, false);
    this.legL = limb(-0.09, 0.36, 0.1, 0.1, 0.07, dark, true); this.legR = limb(0.09, 0.36, 0.1, 0.1, 0.07, dark, true);
    this.armL.sh.rotation.z = 0.25; this.armR.sh.rotation.z = -0.25;

    // ---------------- post: bloom
    const comp = (this.composer = new EffectComposer(r)); comp.setPixelRatio(1); comp.setSize(width, height);
    comp.addPass(new RenderPass(scene, this.cam));
    this.bloom = new UnrealBloomPass(new THREE.Vector2(width / 2, height / 2), 0.45, 0.55, 0.86); comp.addPass(this.bloom);
    comp.addPass(new OutputPass());
    this.grade = new ShaderPass(GradeShader); Object.assign(this.grade.uniforms.uSat, { value: 1.05 }); this.grade.uniforms.uVig.value = 0.22; this.grade.uniforms.uGrain.value = 0.025; comp.addPass(this.grade);
    this._lastLife = -1; this._lastGrowTrees = -1;
    this._v = [new THREE.Vector3(), new THREE.Vector3(), new THREE.Vector3(), new THREE.Vector3()];
    r.compile(scene, this.cam);
  }

  // ---------------------------------------------------------------- camera
  preCam(t) {   // the original S5 camera (world space)
    const orbit = 0.95 - 0.55 * eo((t - 1.6) / 3.2) - 0.035 * Math.max(0, t - 4.8);
    const rad = 3.9 - 0.9 * eo(t / 2.2) - 0.25 * eo((t - 2.4) / 2.4) + 0.02 * Math.sin(t * 0.7);
    const hgt = 1.15 + 0.55 * eo((t - 2.2) / 2.2) + 0.015 * Math.sin(t * 1.1);
    const grow = eo((t - 2.35) / 1.3);
    return [new THREE.Vector3(Math.sin(orbit) * rad, hgt, Math.cos(orbit) * rad), new THREE.Vector3(-0.15 * (1 - grow), 0.38 + 0.1 * grow, -0.2 * (1 - grow))];
  }
  postCam(t) {  // after the showcase: slow orbit around the floating island (world space)
    const Wy = this.world.position.y, a = 0.62 + 0.045 * (t - this.SHOW[1]);
    return [new THREE.Vector3(Math.sin(a) * 3.15, Wy + 0.38 + 0.03 * Math.sin(t * 0.5), Math.cos(a) * 3.15), new THREE.Vector3(0, Wy - 0.08, 0)];
  }
  showKeys() {   // [time, space, pos, target, fov] ; 'L' = island-local, 'W' = world. The city (inner) plays between IN0 and IN1.
    const [s0, s1] = this.SHOW, [i0, i1] = this.IN;
    return [
      [s0, 'P'],
      [s0 + 0.55 * (i0 - s0), 'L', [-0.1, 0.72, 1.4], [-0.45, 0.05, 0.2], 50],
      [i0, 'L', [-0.45, 0.2, 0.3], [-0.45, 0.02, -0.15], 58],
      [i1, 'L', [-0.32, 0.45, 0.6], [-0.3, 0.1, 0.0], 56],
      [i1 + 0.5 * (s1 - i1), 'W', [3.3, 1.0, 2.2], [0, 0.98, 0], 52],
      [s1, 'Q'],
    ];
  }
  camAt(t) {
    const [s0, s1] = this.SHOW;
    if (t <= s0) { const [p, q] = this.preCam(t); return [p, q, 52]; }
    if (t >= s1) { const [p, q] = this.postCam(t); return [p, q, 52]; }
    const W = this.world; W.updateMatrixWorld(true);
    const K = this.showKeys().map((k) => {
      if (k[1] === 'P') { const [p, q] = this.preCam(k[0]); const [p2, q2] = this.preCam(k[0] + 0.02); return { t: k[0], p, q, f: 52, vp: p2.sub(p).multiplyScalar(50), vq: q2.sub(q).multiplyScalar(50) }; }
      if (k[1] === 'Q') { const [p, q] = this.postCam(k[0]); const [p2, q2] = this.postCam(k[0] + 0.02); return { t: k[0], p, q, f: 52, vp: p2.sub(p).multiplyScalar(50), vq: q2.sub(q).multiplyScalar(50) }; }
      const p = new THREE.Vector3(...k[2]), q = new THREE.Vector3(...k[3]);
      if (k[1] === 'L') { W.localToWorld(p); W.localToWorld(q); }
      return { t: k[0], p, q, f: k[4] };
    });
    for (let i = 1; i < K.length - 1; i++) {
      const dt = K[i + 1].t - K[i - 1].t;
      K[i].vp = K[i].vp || K[i + 1].p.clone().sub(K[i - 1].p).divideScalar(dt);
      K[i].vq = K[i].vq || K[i + 1].q.clone().sub(K[i - 1].q).divideScalar(dt);
    }
    let i = 0; while (i < K.length - 2 && t > K[i + 1].t) i++;
    const a = K[i], b = K[i + 1], dt = b.t - a.t, u = clamp((t - a.t) / dt);
    const h00 = 2 * u * u * u - 3 * u * u + 1, h10 = u * u * u - 2 * u * u + u, h01 = -2 * u * u * u + 3 * u * u, h11 = u * u * u - u * u;
    const herm = (P0, V0, P1, V1) => P0.clone().multiplyScalar(h00).addScaledVector(V0, h10 * dt).addScaledVector(P1, h01).addScaledVector(V1, h11 * dt);
    return [herm(a.p, a.vp, b.p, b.vp), herm(a.q, a.vq, b.q, b.vq), lerp(a.f, b.f, u * u * (3 - 2 * u))];
  }

  // ---------------------------------------------------------------- render(t)
  render(t) {
    const [S0, S1] = this.SHOW, sd = S1 - S0, [I0, I1] = this.IN;
    if (this.city && t >= I0 && t < I1) { this.city.render(t - I0, (1 - ss(I0, I0 + 0.6, t)) + ss(I1 - 0.5, I1, t)); return; }
    this.grade.uniforms.uFlash.value = t < I0 ? ss(I0 - 0.45, I0, t) : t >= I1 ? 1 - ss(I1, I1 + 0.6, t) : 0; this.grade.uniforms.uTime.value = t;
    const life = ss(3.3, 4.9, t), grow = eo((t - 2.35) / 1.3);
    const tod = this.city ? ss(I0, I1 - 0.5, t) : ss(S0 + 0.3 * sd, S0 + 0.6 * sd, t) * 0.5 + ss(S0 + 0.6 * sd, S0 + 0.8 * sd, t) * 0.5;   // 0 day -> .5 sunset -> 1 night
    const night = ss(0.45, 0.95, tod), dusk = ss(0, 0.5, tod) * (1 - ss(0.5, 0.95, tod));
    const lift = this.city ? eio((t - (I1 - 4)) / 4.6) : eio((t - (S0 + 0.6 * sd)) / (0.3 * sd));
    this.uTime.value = t; this.uNight.value = night * 1.05; this.uGrow.value = grow;
    // astronaut: walk in, reach, awe; later looks up at the rising island
    const wk = ss(0, 1.45, t), walking = t < 1.45 ? Math.sin(t * Math.PI * 2 * 1.6) : 0;
    const A = this.astro; A.visible = this.city ? !(t > I0 - 0.5 && t < I1 + 1.2) : !(t > S0 + 0.12 * sd && t < S0 + 0.83 * sd); A.position.set(-1.45 + 0.4 * wk, t < 1.45 ? Math.abs(Math.sin(t * Math.PI * 1.6 * 2)) * 0.02 : 0, -1.45 + 0.45 * wk); A.rotation.y = 0.8;
    this.legL.sh.rotation.x = 0.45 * walking * (1 - ss(1.2, 1.45, t)); this.legR.sh.rotation.x = -0.45 * walking * (1 - ss(1.2, 1.45, t));
    this.legL.el.rotation.x = Math.max(0, -walking) * 0.4; this.legR.el.rotation.x = Math.max(0, walking) * 0.4;
    const reach = ss(1.35, 1.95, t) * (1 - ss(2.25, 2.8, t)), awe = ss(2.2, 3.0, t), look = lift;
    this.armR.sh.rotation.x = -0.35 * walking - 1.15 * reach - 0.35 * awe * (1 - reach) + 0.04 * Math.sin(t * 1.3) - 0.5 * look;
    this.armR.el.rotation.x = -0.35 * reach - 0.3 * look;
    this.armL.sh.rotation.x = 0.35 * walking - 0.25 * awe + 0.03 * Math.sin(t * 1.1 + 1);
    this.armL.sh.rotation.z = 0.25 + 0.2 * awe;
    this.aHead.rotation.x = 0.18 * reach - 0.22 * awe + 0.03 * Math.sin(t * 0.9) - 0.35 * look;
    this.aHead.rotation.y = 0.12 * Math.sin(t * 0.45) * ss(4.5, 6, t);
    A.rotation.x = -0.06 * awe;
    this.packL.color.setHSL(0.53, 1, 0.45 + 0.15 * Math.sin(t * 3));
    this.antTip.material.color.setRGB(1, 0.25 + 0.2 * (Math.sin(t * 4) > 0.6 ? 1 : 0), 0.25);
    // cube
    const hum = 0.6 + 0.4 * Math.sin(t * 5.5);
    this.coreL.intensity = 1.6 + 1.6 * hum * (1 - life * 0.4) + 3 * ss(1.9, 2.2, t) * (1 - ss(2.6, 3.4, t)) + 0.8 * lift;
    this.core.scale.setScalar(1 + 0.1 * hum + 0.35 * ss(1.95, 2.4, t) * (1 - ss(2.6, 3.2, t)));
    this.core.visible = t < 3.25;
    this.seamMat.color.setHSL(0.53, 1, (0.62 + 0.15 * hum) * (1 - 0.35 * night));
    this.topH.rotation.x = -1.7 * back((t - 2.0) / 0.45); this.topH.position.y = 0.56 + 0.55 * eo((t - 2.3) / 0.6);
    this.topH.scale.setScalar(Math.max(0.001, 1 - ss(2.45, 2.95, t)));
    this.sides.forEach((p, k) => { p.rotation.x = (Math.PI / 2) * back((t - 2.12 - k * 0.08) / 0.55); });
    // island transform: grows out of the cube, slowly turns, lifts off on a beam
    const W = this.world, WS = this.WS;
    W.scale.setScalar(Math.max(0.001, grow * WS));
    W.position.y = 0.2 + 0.08 * (1 - grow) + 1.0 * lift + 0.02 * Math.sin(t * 0.8) * lift;
    W.rotation.y = t * 0.06;
    this.under.scale.y = Math.max(0.001, clamp((lift - 0.01) / 0.72)); this.under.visible = lift > 0.001;
    const bh = W.position.y - 0.05 * WS - 0.4 - 0.95 * WS * this.under.scale.y * 0.5;
    this.underL.position.set(0, W.position.y - 0.95 * WS, 0); this.underL.intensity = 3 * lift;
    this.beam.visible = lift > 0.01; this.beam.scale.set(1, Math.max(0.01, bh), 1); this.beam.position.y = 0.4 + bh / 2;
    this.beam.material.uniforms.uOp.value = 0.2 * ss(0, 0.25, lift); this.beam.material.uniforms.uTime.value = t;
    // empty -> alive terrain colours
    if (life !== this._lastLife) {
      const col = this.terrCol.array, E = this.cEmpty, L = this.cLive;
      for (let i = 0; i < E.length; i++) col[i] = E[i] + (L[i] - E[i]) * life;
      this.terrCol.needsUpdate = true; this._lastLife = life;
    }
    // trees pop in with life (instanced)
    const m4 = new THREE.Matrix4(), q4 = new THREE.Quaternion(), s4 = new THREE.Vector3(), p4 = new THREE.Vector3(), yAx = new THREE.Vector3(0, 1, 0);
    if (life !== this._lastGrowTrees) {
      let k = 0, kp = 0, kr = 0;
      for (const s of this.spots) {
        const g = Math.max(0.001, back((life - s[3] * 0.55) / 0.35)) * s[5];
        q4.setFromAxisAngle(yAx, s[6] * 6.28); p4.set(s[0], s[1], s[2]); s4.set(g, g * (0.85 + 0.3 * s[6]), g); m4.compose(p4, q4, s4);
        this.trunkI.setMatrixAt(k++, m4);
        if (s[4]) this.pineI.setMatrixAt(kp++, m4); else this.roundI.setMatrixAt(kr++, m4);
      }
      this.trunkI.instanceMatrix.needsUpdate = this.pineI.instanceMatrix.needsUpdate = this.roundI.instanceMatrix.needsUpdate = true;
      this._lastGrowTrees = life;
    }
    // city life
    this.blds.castShadow = this.roofs.castShadow = grow >= 1;
    this.wallMat.emissiveIntensity = 1.5;
    this.lampMat.color.setRGB(1, 0.85, 0.62).multiplyScalar(0.12 + 2.6 * ss(0.15, 0.55, tod));
    this.spire.scale.setScalar(Math.max(0.001, eo((grow - 0.6) / 0.4)));
    this.holo.rotation.y = t * 0.9; this.holoMat.opacity = 0.35 * life + 0.55 * night;
    this.beacon.material.color.setRGB(1, 0.2, 0.2).multiplyScalar(Math.sin(t * 5) > 0.4 ? 2.2 : 0.35);
    this.wheel.scale.setScalar(Math.max(0.001, eo((life - 0.2) / 0.5)));
    this.wheelRot.rotation.z = t * 0.35;
    this.cabins.forEach((c) => { const a = c.userData.a + t * 0.35; c.position.set(Math.cos(a) * 0.11, 0.15 + Math.sin(a) * 0.11 - 0.012, 0); });
    this.bulbMat.color.setHSL((t * 0.08) % 1, 0.7, 0.62).multiplyScalar(0.6 + 2.2 * night);
    this.mills.forEach((g, k) => { g.scale.setScalar(Math.max(0.001, eo((life - 0.3 - k * 0.08) / 0.4))); g.userData.hub.rotation.z = t * (1.4 + k * 0.2); });
    // cars
    const carOn = ss(3.9, 4.6, t), lightK = 0.4 + 2.2 * ss(0.2, 0.7, tod);
    this.headMat.color.setRGB(1, 0.97, 0.85).multiplyScalar(lightK); this.tailMat.color.setRGB(1, 0.12, 0.12).multiplyScalar(lightK);
    this.carList.forEach((c, k) => {
      const L = c.L, u = (((c.o + (t * L.sp) / Math.hypot(L.b[0] - L.a[0], L.b[1] - L.a[1])) % 1) + 1) % 1;
      const x = lerp(L.a[0], L.b[0], u), z = lerp(L.a[1], L.b[1], u), ang = Math.atan2(L.b[0] - L.a[0], L.b[1] - L.a[1]) + (L.sp < 0 ? Math.PI : 0);
      const sc = carOn * (Math.hypot(x, z) < 0.96 ? 1 : 0) + 0.0001;
      q4.setFromAxisAngle(yAx, ang); p4.set(x, 0.0535, z); s4.set(sc, sc, sc); m4.compose(p4, q4, s4); this.carI.setMatrixAt(k, m4);
      const fx = Math.sin(ang), fz = Math.cos(ang);
      p4.set(x + fx * 0.0082, 0.057, z + fz * 0.0082); m4.compose(p4, q4, s4); this.headI.setMatrixAt(k, m4);
      p4.set(x - fx * 0.0082, 0.057, z - fz * 0.0082); m4.compose(p4, q4, s4); this.tailI.setMatrixAt(k, m4);
    });
    this.carI.instanceMatrix.needsUpdate = this.headI.instanceMatrix.needsUpdate = this.tailI.instanceMatrix.needsUpdate = true;
    // train
    const trOn = ss(4.0, 4.8, t);
    this.train.forEach((g, k) => {
      const u = ((0.12 + t * 0.052 - k * 0.0082) % 1 + 1) % 1, p = this.track.getPointAt(u), tg = this.track.getTangentAt(u);
      g.position.set(p.x, 0.21 + 0.0095, p.z); g.rotation.y = Math.atan2(-tg.z, tg.x); g.scale.setScalar(Math.max(0.001, trOn));
    });
    this.trainWin.emissiveIntensity = 0.15 + 2.2 * night;
    // balloons rise, birds circle, clouds drift, rocks orbit
    this.balloons.forEach((g) => { const { x, z, k } = g.userData; const rise = Math.max(0, t - 4.2 - k * 0.6); g.position.set(x + 0.02 * Math.sin(t * 0.3 + k), H(x, z) + 0.06 + 0.035 * rise, z + 0.015 * rise); g.scale.setScalar(Math.max(0.001, eo((t - 4.0 - k * 0.5) / 0.6))); g.rotation.y = t * 0.2; });
    const birdOn = ss(4.2, 5.0, t);
    this.birdSeed.forEach(([a, b, c], k) => {
      const ang = a * 6.28 + t * (0.35 + 0.1 * b), rr = 0.3 + 0.12 * c, y = 0.42 + 0.06 * Math.sin(t * 0.7 + k);
      p4.set(0.15 + Math.cos(ang) * rr, y, 0.05 + Math.sin(ang) * rr); q4.setFromAxisAngle(yAx, -ang);
      const fl = Math.cos(t * (9 + 4 * b) + k * 1.7), sc = 0.012 * birdOn + 0.00001; s4.set(sc, sc * fl, sc); m4.compose(p4, q4, s4); this.birdI.setMatrixAt(k, m4);
    });
    this.birdI.instanceMatrix.needsUpdate = true;
    this.cloudMat.opacity = 0.92 * ss(3.6, 4.6, t) * (1 - 0.45 * night);
    this.cloudMat.color.setRGB(1, 1, 1).lerp(col3(0xffb38a), dusk * 0.8).lerp(col3(0x4a5878), night);
    this.clouds.forEach((g) => { const a = g.userData.a + t * 0.04; g.position.set(Math.cos(a) * g.userData.r, g.userData.y, Math.sin(a) * g.userData.r); });
    this.rocks.forEach((m) => { const u = m.userData, a = u.a + t * u.s; m.position.set(Math.cos(a) * u.r, u.y + 0.04 * Math.sin(t * 0.6 + u.a), Math.sin(a) * u.r); m.rotation.set(t * 0.3 * u.sp, t * 0.2, 0); m.visible = lift > 0.05; m.scale.setScalar(Math.max(0.001, lift)); });
    // water
    this.waterU.uTod.value = tod; this.waterU.uLife.value = life; this.fallMat.uniforms.uOp.value = 0.85 * ss(4.0, 4.8, t);
    this.mistMat.uniforms.uOp.value = 0.6 * ss(4.0, 4.8, t) * this.under.scale.y; this.mistMat.uniforms.uTime.value = t;
    // sparkles: spiral up out of the cube as the world comes alive
    const sp = this.spkPts.geometry.attributes.position, burst = ss(3.0, 3.6, t) * (1 - ss(6.5, 8.0, t));
    for (let i = 0; i < sp.count; i++) {
      const s = this.spkSeed[i], ph = ((t - 3.0) * (0.12 + 0.1 * s) + s) % 1, a = s * 40 + ph * 9, rr = 0.25 + ph * 1.2 * (0.6 + 0.6 * s);
      sp.setXYZ(i, Math.cos(a) * rr, 0.3 + ph * 1.8, Math.sin(a) * rr);
    }
    sp.needsUpdate = true; this.spkMat.uniforms.uOp.value = 1.4 * burst; this.spkMat.uniforms.uTime.value = t;
    this.ffMat.uniforms.uOp.value = 1.3 * night; this.ffMat.uniforms.uTime.value = t;
    this.starMat.uniforms.uOp.value = 0.9 * (1 - life * (1 - night)) + 0.2 * night; this.starMat.uniforms.uTime.value = t;
    this.aurora.material.uniforms.uOp.value = 0.85 * ss(0.7, 1.0, tod); this.aurora.material.uniforms.uTime.value = t;
    this.moon.material.opacity = ss(0.6, 0.95, tod) * 1.0;
    // sky, fog, lights by time of day
    const sk = this.sky.material.uniforms; sk.uLife.value = life; sk.uTod.value = tod;
    const sunEl = lerp(0.62, 0.04, ss(0, 0.5, tod)), sunAz = -0.9 + 0.5 * tod;
    sk.uSun.value.set(Math.cos(sunAz) * Math.cos(Math.asin(sunEl)), sunEl, Math.sin(sunAz) * Math.cos(Math.asin(sunEl)));
    const fogDay = col3(0x9fc4e8), fogDusk = col3(0xd9845a), fogNight = col3(0x06122a), fogStage = col3(0x0d1d44);
    this.scene.fog.color.copy(fogStage).lerp(fogDay, life).lerp(fogDusk, dusk).lerp(fogNight, night);
    const key = this.key, sunDir = sk.uSun.value;
    const moonDir = new THREE.Vector3(14, 16, -26).normalize();
    const kd = new THREE.Vector3().copy(sunDir).lerp(moonDir, night).normalize();
    key.position.copy(W.position).addScaledVector(kd, 8); key.target.position.copy(W.position); key.target.updateMatrixWorld();
    key.color.set(0xfff1e0).lerp(col3(0xffa060), dusk).lerp(col3(0x8fb4ff), night);
    key.intensity = lerp(2.2, 2.7, life) * (1 - 0.35 * dusk) * (1 - 0.82 * night);
    this.hemi.color.set(0x9cc8ff).lerp(col3(0xffb08a), dusk * 0.7).lerp(col3(0x2a3f78), night);
    this.hemi.groundColor.set(0x1a2440).lerp(col3(0x3a2a40), dusk).lerp(col3(0x050a18), night);
    this.hemi.intensity = lerp(1.0, 0.72, life) * (1 - 0.5 * night);
    this.scene.environmentIntensity = 0.5 * (1 - 0.6 * night);
    this.rim.intensity = 1.1 + 0.6 * night;
    this.ringMat.color.setHSL(0.53, 1, 0.45 + 0.1 * Math.sin(t * 2));
    this.crystalMat.color.setRGB(0.5, 0.94, 1).multiplyScalar(1 + 1.5 * night);
    this.bloom.strength = 0.22 + 0.3 * burst + 0.4 * night; this.bloom.threshold = lerp(0.95, 0.72, night);
    this.renderer.toneMappingExposure = lerp(1.1, 0.92, life) * (1 + 0.25 * night);
    // camera
    const [cp, cq, fov] = this.camAt(t);
    this.cam.position.copy(cp); this.cam.lookAt(cq);
    const near = this.city ? (t > I0 - 0.9 && t < I1 + 1.0 ? 0.003 : 0.03) : t > S0 + 0.18 * sd && t < S0 + 0.62 * sd ? 0.003 : 0.03;
    if (this.cam.fov !== fov || this.cam.near !== near) { this.cam.fov = fov; this.cam.near = near; this.cam.updateProjectionMatrix(); }
    this.composer.render();
  }
}
window.World3D = { World };

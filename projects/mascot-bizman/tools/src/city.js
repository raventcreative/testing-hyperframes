// INNER CITY — the real-scale world the camera dives into (inside the pocket universe). Deterministic: render(ti) is a pure
// function of ti. Assets (free/open): Poly Haven CC0 HDRI (venice_sunset), three.js example models (Ferrari 458 —
// see assets/3d/CREDITS.md; Mixamo-rigged Michelle / Ready Player Me avatar driven by the Soldier mocap walk),
// three.js water normals, EZ-Tree procedural trees (MIT). Everything else (streets, buildings, shops, lamps) is built here.
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/examples/jsm/loaders/DRACOLoader.js';
import { RGBELoader } from 'three/examples/jsm/loaders/RGBELoader.js';
import { Sky } from 'three/examples/jsm/objects/Sky.js';
import { Water } from 'three/examples/jsm/objects/Water.js';
import * as SkeletonUtils from 'three/examples/jsm/utils/SkeletonUtils.js';
import { mergeGeometries } from 'three/examples/jsm/utils/BufferGeometryUtils.js';
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/examples/jsm/postprocessing/OutputPass.js';
import { ShaderPass } from 'three/examples/jsm/postprocessing/ShaderPass.js';
import { Tree } from '@dgreenheck/ez-tree';

const clamp = (v, a = 0, b = 1) => Math.max(a, Math.min(b, v));
const ss = (a, b, t) => { const u = clamp((t - a) / (b - a)); return u * u * (3 - 2 * u); };
const lerp = (a, b, u) => a + (b - a) * u;
function rng(seed) { let s = seed >>> 0 || 1; return () => ((s = (Math.imul(s, 1664525) + 1013904223) >>> 0) / 4294967296); }

// ------------------------------------------------------------------ cinematic grade (shared with the outer world)
export const GradeShader = {
  uniforms: { tDiffuse: { value: null }, uTime: { value: 0 }, uFlash: { value: 0 }, uSat: { value: 1.08 }, uContrast: { value: 1.06 },
    uShadow: { value: new THREE.Vector3(-0.012, 0.004, 0.02) }, uHigh: { value: new THREE.Vector3(0.025, 0.01, -0.02) }, uVig: { value: 0.32 }, uGrain: { value: 0.035 }, uRes: { value: new THREE.Vector2(1080, 1920) } },
  vertexShader: 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }',
  fragmentShader: `uniform sampler2D tDiffuse; uniform float uTime, uFlash, uSat, uContrast, uVig, uGrain; uniform vec3 uShadow, uHigh; uniform vec2 uRes; varying vec2 vUv;
    float h(vec2 p){ return fract(sin(dot(p, vec2(12.9898,78.233))) * 43758.5453); }
    float n2(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f); return mix(mix(h(i), h(i+vec2(1,0)), f.x), mix(h(i+vec2(0,1)), h(i+vec2(1,1)), f.x), f.y); }
    void main(){ vec3 c = texture2D(tDiffuse, vUv).rgb;
      float l = dot(c, vec3(0.2126,0.7152,0.0722));
      c = mix(vec3(l), c, uSat); c = (c - 0.5) * uContrast + 0.5;
      c += uShadow * (1.0 - smoothstep(0.0, 0.45, l)) + uHigh * smoothstep(0.45, 1.0, l);
      vec2 q = vUv - 0.5; q.x *= uRes.x / uRes.y; c *= 1.0 - uVig * smoothstep(0.25, 0.85, length(q) * 1.25);
      c += (h(vUv * uRes + fract(uTime * 7.13) * 91.7) - 0.5) * uGrain;
      float cl = n2(vUv * vec2(3.0, 5.0) + uTime * 0.6) * 0.6 + n2(vUv * vec2(9.0, 15.0) - uTime) * 0.4;   // cloud-like whiteout
      c = mix(c, vec3(0.93,0.96,1.0), clamp(uFlash * (0.75 + 0.5 * cl) * 1.2 - 0.1, 0.0, 1.0));
      gl_FragColor = vec4(clamp(c, 0.0, 1.0), 1.0); }`,
};

// ------------------------------------------------------------------ layout (metres). Boulevard along z; park + lake east.
const ROAD_W = 14, SIDE = 5, FRONT = ROAD_W / 2 + SIDE;            // building frontage at |x| = 12
const PARK = { x0: FRONT + 2, x1: 175, z0: -45, z1: 130 };          // open park on the east side
const LAKE = { x: 82, z: 35, w: 120, d: 90 };
const LANES = [[-5.25, 1], [-1.75, 1], [1.75, -1], [5.25, -1]];

export class City {
  static async create(renderer, opts = {}) { const c = new City(); await c.init(renderer, opts); return c; }
  async init(renderer, { width = 1080, height = 1920, base = 'assets/3d/', draco = 'vendor/draco/' } = {}) {
    this.r = renderer; const R = rng(77);
    const scene = (this.scene = new THREE.Scene());
    this.cam = new THREE.PerspectiveCamera(45, width / height, 0.3, 3000);
    const dl = new DRACOLoader().setDecoderPath(draco);
    const gl = new GLTFLoader().setDRACOLoader(dl);
    const tl = new THREE.TextureLoader();
    const [hdr, ferrari, aoTex, michelle, rpm, soldier, waterN, grassT] = await Promise.all([
      new RGBELoader().loadAsync(base + 'hdr/venice_sunset_1k.hdr'),
      gl.loadAsync(base + 'models/ferrari.glb'), tl.loadAsync(base + 'models/ferrari_ao.png'),
      gl.loadAsync(base + 'models/Michelle.glb'), gl.loadAsync(base + 'models/readyplayer.me.glb'), gl.loadAsync(base + 'models/Soldier.glb'),
      tl.loadAsync(base + 'tex/waternormals.jpg'), tl.loadAsync(base + 'tex/grasslight-big.jpg'),
    ]);
    const pm = new THREE.PMREMGenerator(renderer);
    hdr.mapping = THREE.EquirectangularReflectionMapping;
    scene.environment = pm.fromEquirectangular(hdr).texture; scene.environmentIntensity = 0.85;

    // ---------------- sky (physical atmosphere) + sun + fog
    const sky = (this.sky = new Sky()); sky.scale.setScalar(4000); scene.add(sky);
    const su = sky.material.uniforms; su.turbidity.value = 5.5; su.rayleigh.value = 1.4; su.mieCoefficient.value = 0.006; su.mieDirectionalG.value = 0.82;
    this.sun = new THREE.Vector3();
    const key = (this.key = new THREE.DirectionalLight(0xffc890, 3.2)); key.castShadow = true;
    key.shadow.mapSize.set(4096, 4096); Object.assign(key.shadow.camera, { left: -70, right: 70, top: 70, bottom: -70, near: 1, far: 600 });
    key.shadow.bias = -0.00025; key.shadow.normalBias = 0.04; scene.add(key, key.target);
    this.hemi = new THREE.HemisphereLight(0xbfd6ff, 0x3a2f28, 0.35); scene.add(this.hemi);
    scene.fog = new THREE.FogExp2(0xd8b48f, 0.0016);

    // ---------------- procedural textures
    const canvasTex = (w, h, fn, srgb = true, rep = true) => { const c = document.createElement('canvas'); c.width = w; c.height = h; fn(c.getContext('2d'), w, h); const t = new THREE.CanvasTexture(c); if (srgb) t.colorSpace = THREE.SRGBColorSpace; if (rep) t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = 8; return t; };
    const noiseFill = (x, w, h, base, amp, n, sz = 2) => { x.fillStyle = base; x.fillRect(0, 0, w, h); const RR = rng(n); for (let i = 0; i < w * h / 6; i++) { const v = Math.floor(RR() * amp); x.fillStyle = `rgba(${v},${v},${v},${0.06 + RR() * 0.08})`; x.fillRect(RR() * w, RR() * h, sz, sz); } };
    const asphalt = canvasTex(512, 512, (x, w, h) => { noiseFill(x, w, h, '#3b3d40', 255, 3); const RR = rng(9); for (let i = 0; i < 40; i++) { x.strokeStyle = 'rgba(20,20,22,0.25)'; x.lineWidth = 1 + RR() * 2; x.beginPath(); x.moveTo(RR() * w, RR() * h); x.bezierCurveTo(RR() * w, RR() * h, RR() * w, RR() * h, RR() * w, RR() * h); x.stroke(); } });
    asphalt.repeat.set(3, 140);
    const asphaltR = canvasTex(256, 256, (x, w, h) => noiseFill(x, w, h, '#d0d0d0', 255, 4), false); asphaltR.repeat.set(3, 140);
    const paving = canvasTex(512, 512, (x, w, h) => { noiseFill(x, w, h, '#a39d93', 200, 5); x.strokeStyle = 'rgba(60,55,50,0.55)'; x.lineWidth = 3; for (let i = 0; i <= 8; i++) { x.beginPath(); x.moveTo(0, i * 64); x.lineTo(w, i * 64); x.stroke(); x.beginPath(); x.moveTo(i * 64, 0); x.lineTo(i * 64, h); x.stroke(); } });
    paving.repeat.set(1.2, 140);

    // ---------------- ground: road, markings, sidewalks + curbs, park
    const roadM = new THREE.MeshStandardMaterial({ map: asphalt, roughnessMap: asphaltR, roughness: 0.92, metalness: 0.0 });
    const road = new THREE.Mesh(new THREE.PlaneGeometry(ROAD_W, 700), roadM); road.rotation.x = -Math.PI / 2; road.receiveShadow = true; scene.add(road);
    const markM = new THREE.MeshStandardMaterial({ color: 0xe9e6dc, roughness: 0.6 }), yel = new THREE.MeshStandardMaterial({ color: 0xd9a52b, roughness: 0.6 });
    const dashes = [], yl = [];
    for (let z = -345; z < 345; z += 9) for (const x of [-3.5, 3.5]) { const g = new THREE.PlaneGeometry(0.15, 3); g.rotateX(-Math.PI / 2); g.translate(x, 0.012, z); dashes.push(g); }
    for (const x of [-0.12, 0.12]) { const g = new THREE.PlaneGeometry(0.12, 700); g.rotateX(-Math.PI / 2); g.translate(x, 0.012, 0); yl.push(g); }
    for (const x of [-6.9, 6.9]) { const g = new THREE.PlaneGeometry(0.15, 700); g.rotateX(-Math.PI / 2); g.translate(x, 0.012, 0); dashes.push(g); }
    for (let k = 0; k < 9; k++) { const g = new THREE.PlaneGeometry(0.55, 4); g.rotateX(-Math.PI / 2); g.translate(-6 + k * 1.5, 0.013, -52); dashes.push(g); }   // crosswalk
    scene.add(new THREE.Mesh(mergeGeometries(dashes), markM), new THREE.Mesh(mergeGeometries(yl), yel));
    const swM = new THREE.MeshStandardMaterial({ map: paving, roughness: 0.85 }), curbM = new THREE.MeshStandardMaterial({ color: 0x9a958d, roughness: 0.8 });
    for (const s of [-1, 1]) {
      const sw = new THREE.Mesh(new THREE.BoxGeometry(SIDE, 0.16, 700), swM); sw.position.set(s * (ROAD_W / 2 + SIDE / 2), 0.08, 0); sw.receiveShadow = true; scene.add(sw);
      const cb = new THREE.Mesh(new THREE.BoxGeometry(0.22, 0.18, 700), curbM); cb.position.set(s * (ROAD_W / 2 + 0.11), 0.09, 0); cb.receiveShadow = true; scene.add(cb);
    }
    grassT.colorSpace = THREE.SRGBColorSpace; grassT.wrapS = grassT.wrapT = THREE.RepeatWrapping; grassT.repeat.set(40, 40); grassT.anisotropy = 8;
    const parkG = new THREE.Mesh(new THREE.PlaneGeometry(PARK.x1 - PARK.x0, PARK.z1 - PARK.z0), new THREE.MeshStandardMaterial({ map: grassT, color: 0x9fb07a, roughness: 0.95 }));
    parkG.rotation.x = -Math.PI / 2; parkG.position.set((PARK.x0 + PARK.x1) / 2, 0.05, (PARK.z0 + PARK.z1) / 2); parkG.receiveShadow = true; scene.add(parkG);
    const far = new THREE.Mesh(new THREE.PlaneGeometry(6000, 6000), new THREE.MeshStandardMaterial({ color: 0x5c5a55, roughness: 1 })); far.rotation.x = -Math.PI / 2; far.position.y = -0.02; scene.add(far);
    // lake (reflective water)
    waterN.wrapS = waterN.wrapT = THREE.RepeatWrapping;
    this.water = new Water(new THREE.CircleGeometry(LAKE.w / 2, 96), { textureWidth: 512, textureHeight: 512, waterNormals: waterN, sunDirection: new THREE.Vector3(), sunColor: 0xffe0b0, waterColor: 0x0c2a3a, distortionScale: 2.2, fog: true });
    this.water.rotation.x = -Math.PI / 2; this.water.scale.y = LAKE.d / LAKE.w; this.water.position.set(LAKE.x, 0.12, LAKE.z); scene.add(this.water);
    const rim = new THREE.Mesh(new THREE.RingGeometry(1, 1.06, 64), new THREE.MeshStandardMaterial({ color: 0xb8b0a2, roughness: 0.8 }));
    rim.scale.set(LAKE.w / 2, LAKE.d / 2, 1); rim.rotation.x = -Math.PI / 2; rim.position.set(LAKE.x, 0.13, LAKE.z); scene.add(rim);

    // ---------------- buildings (merged walls with facade / glass / lit-window maps + shop bands + roofs)
    const CELL = 32, FW = 1.6, FH = 3.6;                                   // window module (m)
    const lit = []; const RL = rng(21); for (let i = 0; i < CELL * CELL; i++) lit.push(RL());
    const facadeGlass = canvasTex(512, 512, (x) => { x.fillStyle = '#b9c2cc'; x.fillRect(0, 0, 512, 512); for (let cy = 0; cy < 32; cy++) for (let cx = 0; cx < 32; cx++) { const v = lit[cy * 32 + cx]; x.fillStyle = `rgb(${18 + v * 14},${28 + v * 16},${40 + v * 18})`; x.fillRect(cx * 16 + 1, cy * 16 + 1, 15, 13); } });
    const glassMR = canvasTex(512, 512, (x) => { x.fillStyle = 'rgb(0,170,90)'; x.fillRect(0, 0, 512, 512); for (let cy = 0; cy < 32; cy++) for (let cx = 0; cx < 32; cx++) { x.fillStyle = `rgb(0,${12 + lit[cy * 32 + cx] * 20},${230})`; x.fillRect(cx * 16 + 1, cy * 16 + 1, 15, 13); } }, false);
    const facadeStone = canvasTex(512, 512, (x) => { noiseFill(x, 512, 512, '#cdbfa8', 255, 12, 1); for (let cy = 0; cy < 32; cy++) for (let cx = 0; cx < 32; cx++) { const v = lit[cy * 32 + cx]; x.fillStyle = '#8f8270'; x.fillRect(cx * 16 + 3, cy * 16 + 2, 10, 11); x.fillStyle = `rgb(${24 + v * 20},${32 + v * 20},${42 + v * 22})`; x.fillRect(cx * 16 + 4, cy * 16 + 3, 8, 9); } });
    const stoneMR = canvasTex(512, 512, (x) => { x.fillStyle = 'rgb(0,220,0)'; x.fillRect(0, 0, 512, 512); for (let cy = 0; cy < 32; cy++) for (let cx = 0; cx < 32; cx++) { x.fillStyle = 'rgb(0,20,200)'; x.fillRect(cx * 16 + 4, cy * 16 + 3, 8, 9); } }, false);
    const winLit = (pad) => canvasTex(512, 512, (x) => { x.fillStyle = '#000'; x.fillRect(0, 0, 512, 512); for (let cy = 0; cy < 32; cy++) for (let cx = 0; cx < 32; cx++) { const v = lit[(cy * 32 + cx + 7) % 1024]; if (v < 0.58) continue; x.fillStyle = v > 0.9 ? '#cfe8ff' : v > 0.62 ? '#ffd9a6' : '#ffbf7a'; pad ? x.fillRect(cx * 16 + 4, cy * 16 + 3, 8, 9) : x.fillRect(cx * 16 + 1, cy * 16 + 1, 15, 13); } });
    const shopTex = canvasTex(1024, 256, (x) => {
      x.fillStyle = '#26221f'; x.fillRect(0, 0, 1024, 256); const RR = rng(31);
      for (let i = 0; i < 4; i++) { const x0 = i * 256 + 10; const g = x.createLinearGradient(0, 80, 0, 250); g.addColorStop(0, '#f4d9ac'); g.addColorStop(1, '#8a6a45'); x.fillStyle = g; x.fillRect(x0, 78, 236, 170);
        for (let k = 0; k < 6; k++) { x.fillStyle = `rgba(${60 + RR() * 120},${50 + RR() * 90},${40 + RR() * 60},0.85)`; x.fillRect(x0 + 10 + RR() * 200, 150 + RR() * 60, 18 + RR() * 30, 40 + RR() * 50); }
        x.fillStyle = ['#c43b2e', '#1f5e8c', '#2f6b3a', '#7a4f2a'][i]; x.fillRect(x0, 22, 236, 44); x.fillStyle = '#f2ecdf'; for (let k = 0; k < 5; k++) x.fillRect(x0 + 30 + k * 34, 38, 22, 10);
        x.fillStyle = '#111'; x.fillRect(x0 + 116, 78, 4, 170); }
    });
    const shopEm = canvasTex(1024, 256, (x) => { x.fillStyle = '#000'; x.fillRect(0, 0, 1024, 256); for (let i = 0; i < 4; i++) { const x0 = i * 256 + 10; x.fillStyle = '#ffcf94'; x.fillRect(x0, 78, 236, 170); x.fillStyle = '#ffffff'; for (let k = 0; k < 5; k++) x.fillRect(x0 + 30 + k * 34, 38, 22, 10); } });
    this.uNight = { value: 0 };
    const nightPatch = (m, key) => { m.onBeforeCompile = (sh) => { sh.uniforms.uNight = this.uNight;
      sh.vertexShader = 'attribute float aOn; varying float vOn;\n' + sh.vertexShader.replace('#include <begin_vertex>', '#include <begin_vertex>\n vOn = aOn;');
      sh.fragmentShader = 'uniform float uNight; varying float vOn;\n' + sh.fragmentShader.replace('#include <emissivemap_fragment>', '#include <emissivemap_fragment>\n totalEmissiveRadiance *= smoothstep(vOn, vOn + 0.12, uNight);'); };
      m.customProgramCacheKey = () => 'night' + key; return m; };
    const glassM = nightPatch(new THREE.MeshStandardMaterial({ map: facadeGlass, metalnessMap: glassMR, roughnessMap: glassMR, metalness: 1, roughness: 1, envMapIntensity: 1.25, emissive: 0xffffff, emissiveMap: winLit(false), emissiveIntensity: 0.85 }), 'g');
    const stoneM = nightPatch(new THREE.MeshStandardMaterial({ map: facadeStone, metalnessMap: stoneMR, roughnessMap: stoneMR, metalness: 1, roughness: 1, emissive: 0xffffff, emissiveMap: winLit(true), emissiveIntensity: 0.85 }), 's');
    const shopM = nightPatch(new THREE.MeshStandardMaterial({ map: shopTex, roughness: 0.35, metalness: 0.1, emissive: 0xffffff, emissiveMap: shopEm, emissiveIntensity: 1.3 }), 'p');
    const roofM = new THREE.MeshStandardMaterial({ color: 0x55575b, roughness: 0.9 });
    const B = { g: { p: [], n: [], uv: [], on: [] }, s: { p: [], n: [], uv: [], on: [] }, shop: { p: [], n: [], uv: [], on: [] }, roof: [] };
    const quad = (T, a, b, c, d, n, uv, on) => { for (const v of [a, b, c, a, c, d]) T.p.push(...v); for (let k = 0; k < 6; k++) { T.n.push(...n); T.on.push(on); } for (const k of [0, 1, 2, 0, 2, 3]) T.uv.push(...uv[k]); };
    const box = (cx, cz, w, d, h, kind, on) => {      // w along x, d along z; podium shop band facing the boulevard
      const C = [[cx - w / 2, cz - d / 2], [cx + w / 2, cz - d / 2], [cx + w / 2, cz + d / 2], [cx - w / 2, cz + d / 2]];
      const ou = Math.floor(R() * 32) / 32, ov = Math.floor(R() * 32) / 32;
      for (let k = 0; k < 4; k++) {
        const [ax, az] = C[k], [bx, bz] = C[(k + 1) % 4], len = Math.hypot(bx - ax, bz - az), nx = (bz - az) / len, nz = -(bx - ax) / len;
        const facesRoad = Math.abs(nx) > 0.5 && Math.sign(nx) === -Math.sign(cx);
        const y0 = facesRoad ? 5 : 0;
        if (facesRoad) quad(B.shop, [bx, 0, bz], [ax, 0, az], [ax, 5, az], [bx, 5, bz], [nx, 0, nz], [[len / 26, 0], [0, 0], [0, 1], [len / 26, 1]], 0.25 + R() * 0.3);
        const U = len / FW / 32, V = (h - y0) / FH / 32, T = kind === 'g' ? B.g : B.s;
        quad(T, [bx, y0, bz], [ax, y0, az], [ax, h, az], [bx, h, bz], [nx, 0, nz], [[ou + U, ov], [ou, ov], [ou, ov + V], [ou + U, ov + V]], on);
      }
      const g = new THREE.BoxGeometry(w, 0.4, d); g.translate(cx, h + 0.2, cz); B.roof.push(g);
      if (h > 30) for (let k = 0; k < 3; k++) { const u = new THREE.BoxGeometry(2 + R() * 4, 1.5 + R() * 2, 2 + R() * 4); u.translate(cx + (R() - 0.5) * w * 0.6, h + 1.2, cz + (R() - 0.5) * d * 0.6); B.roof.push(u); }
    };
    // boulevard frontage both sides
    for (const s of [-1, 1]) {
      let z = -340;
      while (z < 340) {
        const w = 16 + R() * 18, cz = z + w / 2; z += w + 3 + R() * 4;
        if (s > 0 && cz > PARK.z0 - 4 && cz < PARK.z1 + 4) continue;
        const centre = Math.exp(-((cz - 40) * (cz - 40)) / 26000);
        const h = 16 + 120 * centre * (0.45 + 0.7 * R()) + 10 * R(), d = 18 + R() * 14;
        box(s * (FRONT + d / 2), cz, d, w - 1.5, h, h > 55 || R() < 0.35 ? 'g' : 's', 0.15 + R() * 0.75);
      }
    }
    // skyline behind the park and far blocks (depth through the haze)
    for (let i = 0; i < 70; i++) {
      const x = 235 + R() * 300, z = -160 + R() * 420, w = 18 + R() * 26, d = 18 + R() * 26, h = 30 + Math.pow(R(), 1.8) * 150;
      box(x, z, w, d, h, R() < 0.6 ? 'g' : 's', 0.15 + R() * 0.75);
    }
    for (let i = 0; i < 90; i++) { const s = R() < 0.5 ? -1 : 1; const x = s * (FRONT + 45 + R() * 260), z = -340 + R() * 680; if (s > 0 && z > -80 && z < 200 && x < 190) continue; const w = 18 + R() * 24, h = 20 + Math.pow(R(), 1.5) * 150; box(x, z, w, w, h, R() < 0.55 ? 'g' : 's', 0.15 + R() * 0.75); }
    const mk = (T) => { const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(T.p, 3)); g.setAttribute('normal', new THREE.Float32BufferAttribute(T.n, 3)); g.setAttribute('uv', new THREE.Float32BufferAttribute(T.uv, 2)); g.setAttribute('aOn', new THREE.Float32BufferAttribute(T.on, 1)); return g; };
    for (const [T, M] of [[B.g, glassM], [B.s, stoneM], [B.shop, shopM]]) { const m = new THREE.Mesh(mk(T), M); m.castShadow = m.receiveShadow = true; scene.add(m); }
    const roofs = new THREE.Mesh(mergeGeometries(B.roof), roofM); roofs.castShadow = roofs.receiveShadow = true; scene.add(roofs);

    // ---------------- street lamps
    const poleM = new THREE.MeshStandardMaterial({ color: 0x2c2f33, metalness: 0.7, roughness: 0.4 });
    this.lampM = new THREE.MeshStandardMaterial({ color: 0x222222, emissive: 0xffd9a0, emissiveIntensity: 0 });
    const pg = [], lg = [];
    for (let z = -330; z < 340; z += 28) for (const s of [-1, 1]) {
      const x = s * (ROAD_W / 2 + 0.7);
      const p = new THREE.CylinderGeometry(0.09, 0.13, 8, 10); p.translate(x, 4, z); pg.push(p);
      const a = new THREE.CylinderGeometry(0.05, 0.05, 1.6, 6); a.rotateZ(Math.PI / 2); a.translate(x - s * 0.8, 7.9, z); pg.push(a);
      const l = new THREE.BoxGeometry(0.7, 0.14, 0.32); l.translate(x - s * 1.5, 7.8, z); lg.push(l);
    }
    const poles = new THREE.Mesh(mergeGeometries(pg), poleM); poles.castShadow = true; scene.add(poles, new THREE.Mesh(mergeGeometries(lg), this.lampM));

    // ---------------- trees (EZ-Tree, 3 species, cloned)
    const variants = [];
    for (const [preset, seed] of [['Ash Medium', 11], ['Oak Medium', 23], ['Aspen Medium', 37], ['Oak Large', 51]]) {
      const t = new Tree(); t.loadPreset(preset); t.options.seed = seed; t.generate();
      const bb = new THREE.Box3().setFromObject(t), hgt = bb.max.y - bb.min.y; t.userData.k = 1 / hgt;
      t.traverse((o) => { if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; } });
      variants.push(t);
    }
    const plant = (x, z, h, vi) => { const v = variants[vi % variants.length]; const t = v.clone(); t.scale.setScalar(h * v.userData.k); t.position.set(x, 0.16, z); t.rotation.y = R() * 6.28; scene.add(t); };
    for (let z = -320; z < 330; z += 14) for (const s of [-1, 1]) { if (s > 0 && z > PARK.z0 && z < PARK.z1) continue; if (Math.abs(((z + 330) % 28) - 0) < 3) continue; plant(s * (ROAD_W / 2 + 2.2), z + R() * 2, 7 + R() * 2.5, Math.floor(R() * 3)); }
    for (let i = 0; i < 60; i++) {
      const x = PARK.x0 + 4 + R() * (PARK.x1 - PARK.x0 - 8), z = PARK.z0 + 4 + R() * (PARK.z1 - PARK.z0 - 8);
      if (((x - LAKE.x) / (LAKE.w / 2 + 6)) ** 2 + ((z - LAKE.z) / (LAKE.d / 2 + 6)) ** 2 < 1) continue;
      plant(x, z, 9 + R() * 6, Math.floor(R() * 4));
    }

    // ---------------- cars (Ferrari 458 clones, repainted; contact-shadow plane; head/tail lights)
    const car0 = ferrari.scene.children[0];
    const bodyMs = [0x9b1111, 0x0d0d0f, 0xe8e8ea, 0x123d7a, 0x7d8288, 0xcfa21b, 0x1d4d2e].map((c) => new THREE.MeshPhysicalMaterial({ color: c, metalness: 1.0, roughness: 0.45, clearcoat: 1.0, clearcoatRoughness: 0.03 }));
    const glassM2 = new THREE.MeshPhysicalMaterial({ color: 0x0c0f12, metalness: 0.4, roughness: 0.0, transparent: true, opacity: 0.55 });
    aoTex.colorSpace = THREE.NoColorSpace;
    const aoM = new THREE.MeshBasicMaterial({ map: aoTex, blending: THREE.MultiplyBlending, toneMapped: false, transparent: true, premultipliedAlpha: true, depthWrite: false });
    this.headM = new THREE.MeshBasicMaterial({ color: 0xfff3d6 }); this.tailM = new THREE.MeshBasicMaterial({ color: 0xff2a1a });
    this.cars = [];
    const NC = 26;
    for (let i = 0; i < NC; i++) {
      const c = car0.clone(true);
      const bm = bodyMs[i % bodyMs.length];
      c.traverse((o) => { if (!o.isMesh) return; o.castShadow = true; o.receiveShadow = true; const nm = (o.material && o.material.name) || '';
        if (o.name === 'body' || /paint|body/i.test(nm)) o.material = bm; else if (/glass/i.test(o.name) || /Glass/.test(nm)) o.material = glassM2; });
      const ao = new THREE.Mesh(new THREE.PlaneGeometry(0.655 * 4, 1.3 * 4), aoM); ao.rotation.x = -Math.PI / 2; ao.renderOrder = 2; ao.position.y = 0.01; c.add(ao);
      for (const sx of [-0.6, 0.6]) { const hl = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.08, 0.04), this.headM); hl.position.set(sx, 0.72, 2.2); c.add(hl); const tlm = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.07, 0.04), this.tailM); tlm.position.set(sx, 0.85, -2.25); c.add(tlm); }
      const [lx, dir] = LANES[i % 4];
      c.userData = { lx, dir, sp: 9 + R() * 5, z0: -340 + R() * 680, wheels: ['wheel_fl', 'wheel_fr', 'wheel_rl', 'wheel_rr'].map((n) => c.getObjectByName(n)).filter(Boolean) };
      scene.add(c); this.cars.push(c);
    }
    // parked cars along the curb (stationary)
    for (let i = 0; i < 10; i++) { const c = this.cars[i].clone(true); c.userData = { parked: true }; c.position.set((i % 2 ? 1 : -1) * 6.2, 0, -300 + i * 61 + R() * 10); c.rotation.y = i % 2 ? Math.PI : 0; if (i % 2 && c.position.z > PARK.z0 && c.position.z < PARK.z1) c.position.z += 200; scene.add(c); }

    // ---------------- people: Michelle + Ready Player Me avatar walking with the Soldier mocap walk (in place, moved here)
    const walk = soldier.animations.find((a) => a.name === 'Walk');
    const idle = soldier.animations.find((a) => a.name === 'Idle');
    const skinned = (root) => { let m = null; root.traverse((o) => { if (!m && o.isSkinnedMesh) m = o; }); return m; };
    const scratch = [SkeletonUtils.clone(michelle.scene), SkeletonUtils.clone(rpm.scene)];   // retarget on throwaway copies (it poses the target)
    for (const g of [soldier.scene, ...scratch]) g.updateMatrixWorld(true);
    const src = skinned(soldier.scene), tM = skinned(scratch[0]), tR = skinned(scratch[1]);
    const rtc = (tgt, clip, pre) => { const c = SkeletonUtils.retargetClip(tgt, src, clip, { hip: 'mixamorigHips', fps: 30, hipInfluence: new THREE.Vector3(0, 0, 0), getBoneName: (b) => pre + b.name }); c.tracks = c.tracks.filter((t) => t.name.endsWith('.quaternion')); return c; };
    const wM = rtc(tM, walk, ''), wR = rtc(tR, walk, 'mixamorig'), iM = rtc(tM, idle, ''), iR = rtc(tR, idle, 'mixamorig');
    const topCols = [0x2f4f7f, 0x8c2f39, 0x3c6e47, 0x222222, 0x6b4c9a, 0x1f6f8b, 0x9c4a1a], botCols = [0x1f2633, 0x3a3a3a, 0x283c5a, 0x4a4036];
    this.people = [];
    const NP = 34;
    for (let i = 0; i < NP; i++) {
      const isM = i % 2 === 0, src = isM ? michelle.scene : rpm.scene;
      const p = SkeletonUtils.clone(src);
      p.traverse((o) => { if (!o.isMesh) return; o.castShadow = true; o.receiveShadow = true; o.frustumCulled = false;
        if (!isM) { const n = o.material.name; if (/Outfit_Top/.test(n)) { o.material = o.material.clone(); o.material.color.setHex(topCols[i % topCols.length]); } if (/Outfit_Bottom/.test(n)) { o.material = o.material.clone(); o.material.color.setHex(botCols[i % botCols.length]); } }
        else if (i % 4 === 2) { o.material = o.material.clone(); o.material.color.setHSL(R(), 0.25, 0.8); } });
      p.scale.setScalar(isM ? 0.96 + R() * 0.08 : (1.66 + R() * 0.16) / 1.87);
      const mixer = new THREE.AnimationMixer(skinned(p));
      const standing = i % 9 === 4;
      const act = mixer.clipAction(standing ? (isM ? iM : iR) : (isM ? wM : wR)); act.play();
      const hero = i < 14, side = hero ? 1 : R() < 0.5 ? -1 : 1, dir = R() < 0.5 ? -1 : 1, sp = 1.2 + R() * 0.3;
      const lane = hero ? 8.7 + R() * 2.9 : side * (ROAD_W / 2 + 1.8 + R() * 3.0);
      const z0 = hero ? 52 + R() * 44 - dir * sp * 5.2 : -300 + R() * 600;
      p.userData = { mixer, act, lane, dir, sp, z0, ph: R() * 5, standing };
      scene.add(p); this.people.push(p);
    }

    // ---------------- post
    const rt = new THREE.WebGLRenderTarget(width, height, { type: THREE.HalfFloatType, samples: 4 });
    const comp = (this.composer = new EffectComposer(renderer, rt)); comp.setPixelRatio(1); comp.setSize(width, height);
    comp.addPass(new RenderPass(scene, this.cam));
    this.bloom = new UnrealBloomPass(new THREE.Vector2(width / 2, height / 2), 0.25, 0.6, 0.92); comp.addPass(this.bloom);
    comp.addPass(new OutputPass());
    this.grade = new ShaderPass(GradeShader); comp.addPass(this.grade);
    renderer.compile(scene, this.cam);
  }

  // ---------------------------------------------------------------- camera path (ti seconds inside the city; 0..DUR)
  camKeys() {
    return [
      [0.0, [30, 170, 270], [0, 20, 80], 42],
      [2.6, [0, 42, 150], [0, 12, 60], 42],
      [4.0, [10.7, 1.7, 106], [8.6, 2.6, 60], 40],
      [6.6, [10.6, 1.62, 97], [7.4, 2.9, 60], 40],
      [8.2, [12.5, 10, 86], [60, 3, 40], 44],
      [9.8, [30, 18, 84], [100, 6, 20], 46],
      [11.6, [60, 40, 76], [150, 30, -30], 48],
    ];
  }
  camAt(ti) {
    const K = this.camKeys().map(([t, p, q, f]) => ({ t, p: new THREE.Vector3(...p), q: new THREE.Vector3(...q), f }));
    // monotone (Fritsch-Carlson) tangents per axis: no overshoot below the street or through facades
    const mono = (key) => { for (let i = 0; i < K.length; i++) { const v = new THREE.Vector3();
      for (const ax of ['x', 'y', 'z']) {
        const dL = i > 0 ? (K[i][key][ax] - K[i - 1][key][ax]) / (K[i].t - K[i - 1].t) : null, dR = i < K.length - 1 ? (K[i + 1][key][ax] - K[i][key][ax]) / (K[i + 1].t - K[i].t) : null;
        if (dL === null) v[ax] = dR * 0.5; else if (dR === null) v[ax] = dL * 0.5; else v[ax] = dL * dR <= 0 ? 0 : (2 * dL * dR) / (dL + dR);
      } K[i]['v' + key] = v; } };
    mono('p'); mono('q');
    let i = 0; while (i < K.length - 2 && ti > K[i + 1].t) i++;
    const a = K[i], b = K[i + 1], dt = b.t - a.t, u = clamp((ti - a.t) / dt);
    const h00 = 2 * u ** 3 - 3 * u * u + 1, h10 = u ** 3 - 2 * u * u + u, h01 = -2 * u ** 3 + 3 * u * u, h11 = u ** 3 - u * u;
    const H = (P0, V0, P1, V1) => P0.clone().multiplyScalar(h00).addScaledVector(V0, h10 * dt).addScaledVector(P1, h01).addScaledVector(V1, h11 * dt);
    return [H(a.p, a.vp, b.p, b.vp), H(a.q, a.vq, b.q, b.vq), lerp(a.f, b.f, u * u * (3 - 2 * u))];
  }

  // ---------------------------------------------------------------- render(ti): ti = seconds inside the city, flash 0..1
  render(ti, flash = 0, t = ti) {
    // sun: golden hour -> sunset -> blue hour
    const el = lerp(9, -4.5, ss(0.0, 11.6, ti)), az = 168;
    const phi = THREE.MathUtils.degToRad(90 - el), th = THREE.MathUtils.degToRad(az);
    this.sun.setFromSphericalCoords(1, phi, th);
    this.sky.material.uniforms.sunPosition.value.copy(this.sun);
    this.water.material.uniforms.sunDirection.value.copy(this.sun).normalize();
    const day = ss(-3, 6, el), dusk = 1 - day, night = ss(1.5, -3.5, el);
    this.uNight.value = night * 1.1;
    this.key.color.setRGB(1, lerp(0.62, 0.8, ss(2, 9, el)), lerp(0.38, 0.6, ss(2, 9, el)));
    this.key.intensity = 3.4 * ss(-2.5, 3, el) + 0.15;
    this.hemi.intensity = lerp(0.12, 0.38, day);
    this.hemi.color.setRGB(lerp(0.35, 0.75, day), lerp(0.45, 0.82, day), lerp(0.8, 1.0, day));
    this.scene.environmentIntensity = lerp(0.18, 0.85, day);
    this.sky.material.uniforms.rayleigh.value = lerp(2.6, 1.4, day);
    this.scene.fog.color.setRGB(lerp(0.2, 0.86, day), lerp(0.24, 0.66, day), lerp(0.36, 0.5, day));
    this.scene.fog.density = lerp(0.0019, 0.0015, day);
    this.lampM.emissiveIntensity = 3.5 * ss(4.5, 0.5, el);
    this.headM.color.setRGB(1, 0.95, 0.85).multiplyScalar(0.6 + 2.5 * dusk); this.tailM.color.setRGB(1, 0.12, 0.08).multiplyScalar(0.6 + 2.5 * dusk);
    this.r.toneMappingExposure = lerp(1.35, 0.95, day);
    // cars
    for (const c of this.cars) {
      const u = c.userData; let z = u.z0 + u.dir * u.sp * t; z = ((((z + 340) % 680) + 680) % 680) - 340;
      c.position.set(u.lx, 0, z); c.rotation.y = u.dir > 0 ? 0 : Math.PI;
      for (const w of u.wheels) w.rotation.x = (u.sp * t) / 0.34;
    }
    // people
    for (const p of this.people) {
      const u = p.userData; let z = u.standing ? u.z0 : u.z0 + u.dir * u.sp * t; z = ((((z + 340) % 680) + 680) % 680) - 340;
      p.position.set(u.lane, 0.16, z); p.rotation.y = u.standing ? (u.dir > 0 ? 0.6 : 2.4) : (u.dir > 0 ? 0 : Math.PI);
      u.mixer.setTime(u.ph + t * (u.standing ? 1 : u.sp / 1.3));
    }
    this.water.material.uniforms.time.value = t * 0.6;
    // camera
    const [cp, cq, fov] = this.camAt(ti);
    this.cam.position.copy(cp); this.cam.lookAt(cq); if (this.cam.fov !== fov) { this.cam.fov = fov; this.cam.updateProjectionMatrix(); }
    // shadow box follows what the camera looks at (texel-snapped)
    const tgt = cq.clone().lerp(cp, 0.35); tgt.y = 0; tgt.x = Math.round(tgt.x); tgt.z = Math.round(tgt.z);
    this.key.target.position.copy(tgt); this.key.position.copy(tgt).addScaledVector(this.sun, 300); this.key.target.updateMatrixWorld();
    // grade
    const g = this.grade.uniforms; g.uTime.value = t; g.uFlash.value = flash;
    g.uShadow.value.set(lerp(-0.02, -0.012, day), lerp(0.0, 0.004, day), lerp(0.035, 0.02, day)); g.uHigh.value.set(lerp(0.01, 0.03, day), 0.01, lerp(0.0, -0.025, day));
    this.bloom.strength = lerp(0.55, 0.22, day); this.bloom.threshold = lerp(0.75, 0.92, day);
    this.composer.render();
  }
}

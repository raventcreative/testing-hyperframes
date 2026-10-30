// POCKET UNIVERSE — original 3D demo for the Claude Opus 5.5 reel (Three.js, deterministic: render(t) is a pure
// function of t, seeded geometry, no clock). A small astronaut walks to a glowing mechanical cube on a dais; the cube's
// panels hinge open and a miniature world rises out of it: terrain, lake, trees, a lit skyline, roads with moving
// lights, drifting clouds. "Empty -> alive": the world starts as grey wire-like land and blooms into colour and light.
import * as THREE from 'three';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';

const ss = (a, b, t) => { const u = Math.max(0, Math.min(1, (t - a) / (b - a))); return u * u * (3 - 2 * u); };
const eo = (u) => 1 - Math.pow(1 - Math.max(0, Math.min(1, u)), 3);
const back = (u) => { u = Math.max(0, Math.min(1, u)); const c = 1.6; return 1 + (c + 1) * Math.pow(u - 1, 3) + c * Math.pow(u - 1, 2); };
function rng(seed) { let s = seed >>> 0 || 1; return () => ((s = (Math.imul(s, 1664525) + 1013904223) >>> 0) / 4294967296); }
function hash2(x, y) { const s = Math.sin(x * 127.1 + y * 311.7) * 43758.5453; return s - Math.floor(s); }
function noise(x, y) {
  const xi = Math.floor(x), yi = Math.floor(y), xf = x - xi, yf = y - yi;
  const u = xf * xf * (3 - 2 * xf), v = yf * yf * (3 - 2 * yf);
  const a = hash2(xi, yi), b = hash2(xi + 1, yi), c = hash2(xi, yi + 1), d = hash2(xi + 1, yi + 1);
  return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
}

export class World {
  static async create(canvas, opts) { const w = new World(); w.init(canvas, opts); return w; }
  init(canvas, { width = 1080, height = 1920 } = {}) {
    this.W = width; this.H = height;
    const r = (this.renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false, preserveDrawingBuffer: true }));
    r.setPixelRatio(1); r.setSize(width, height, false);
    r.outputColorSpace = THREE.SRGBColorSpace; r.toneMapping = THREE.ACESFilmicToneMapping; r.toneMappingExposure = 1.15;
    r.shadowMap.enabled = true; r.shadowMap.type = THREE.PCFSoftShadowMap;
    const scene = (this.scene = new THREE.Scene());
    scene.fog = new THREE.Fog(0x0d1d44, 9, 22);
    this.cam = new THREE.PerspectiveCamera(52, width / height, 0.05, 80);
    const pm = new THREE.PMREMGenerator(r); scene.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture; scene.environmentIntensity = 0.55;
    const R = rng(11);

    // ---------------- sky dome (gradient + soft horizon glow) and stars
    const sky = new THREE.Mesh(new THREE.SphereGeometry(40, 32, 16), new THREE.ShaderMaterial({
      side: THREE.BackSide, depthWrite: false, fog: false,
      uniforms: { uLife: { value: 0 } },
      vertexShader: 'varying vec3 vP; void main(){ vP = normalize(position); gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }',
      fragmentShader: `varying vec3 vP; uniform float uLife;
        void main(){ float h = vP.y;
          vec3 top = vec3(0.03,0.06,0.17), mid = vec3(0.07,0.17,0.38), hor = mix(vec3(0.12,0.30,0.55), vec3(0.20,0.55,0.80), uLife);
          vec3 c = mix(hor, mid, smoothstep(0.0,0.25,h)); c = mix(c, top, smoothstep(0.25,0.8,h));
          c += vec3(0.0,0.45,0.6) * 0.18 * exp(-abs(h-0.02)*14.0) * (0.5+0.5*uLife);
          gl_FragColor = vec4(c,1.0); }` }));
    scene.add(sky); this.sky = sky;
    const sp = []; for (let i = 0; i < 420; i++) { const a = R() * Math.PI * 2, y = 0.15 + R() * 0.85, rr = Math.sqrt(1 - y * y); sp.push(Math.cos(a) * rr * 35, y * 35, Math.sin(a) * rr * 35); }
    const sg = new THREE.BufferGeometry(); sg.setAttribute('position', new THREE.Float32BufferAttribute(sp, 3));
    scene.add(new THREE.Points(sg, new THREE.PointsMaterial({ color: 0xcfe6ff, size: 0.09, sizeAttenuation: true, fog: false, transparent: true, opacity: 0.8 })));

    // ---------------- light
    scene.add(new THREE.HemisphereLight(0x9cc8ff, 0x1a2440, 1.0));
    const key = new THREE.DirectionalLight(0xfff1e0, 2.2); key.position.set(-3.5, 6, 4); key.castShadow = true;
    key.shadow.mapSize.set(1024, 1024); key.shadow.camera.left = -4; key.shadow.camera.right = 4; key.shadow.camera.top = 4; key.shadow.camera.bottom = -4;
    key.shadow.bias = -0.0008; key.shadow.normalBias = 0.02; scene.add(key);
    const rim = new THREE.DirectionalLight(0x62d6ff, 1.2); rim.position.set(4, 3, -5); scene.add(rim);

    // ---------------- dais (brushed metal disc, chamfer ring, cyan light ring, faint floor grid)
    const metal = new THREE.MeshStandardMaterial({ color: 0x1f2c4c, metalness: 0.7, roughness: 0.38 });
    const dais = new THREE.Mesh(new THREE.CylinderGeometry(3.2, 3.35, 0.22, 96), metal); dais.position.y = -0.11; dais.receiveShadow = true; scene.add(dais);
    const top = new THREE.Mesh(new THREE.CircleGeometry(3.1, 96), new THREE.MeshStandardMaterial({ color: 0x2a3a60, metalness: 0.55, roughness: 0.42 }));
    top.rotation.x = -Math.PI / 2; top.position.y = 0.002; top.receiveShadow = true; scene.add(top);
    const ringMat = new THREE.MeshBasicMaterial({ color: 0x00c9ff });
    const ring = new THREE.Mesh(new THREE.TorusGeometry(3.12, 0.018, 8, 160), ringMat); ring.rotation.x = Math.PI / 2; ring.position.y = 0.01; scene.add(ring); this.ringMat = ringMat;
    const grid = new THREE.GridHelper(6, 24, 0x2f6ea8, 0x23406e); grid.position.y = 0.006; grid.material.transparent = true; grid.material.opacity = 0.22; scene.add(grid);

    // ---------------- pedestal + cube
    const ped = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.5, 0.18, 48), new THREE.MeshStandardMaterial({ color: 0x8fa3c2, metalness: 0.85, roughness: 0.25 }));
    ped.position.y = 0.09; ped.castShadow = ped.receiveShadow = true; scene.add(ped);
    const C = (this.cube = new THREE.Group()); C.position.set(0, 0.18, 0); scene.add(C);
    const S = 0.56, T = 0.035;
    const panelMat = new THREE.MeshStandardMaterial({ color: 0x55627e, metalness: 0.55, roughness: 0.32 });
    const seamMat = (this.seamMat = new THREE.MeshBasicMaterial({ color: 0x5ee3ff }));
    const mkPanel = () => {
      const g = new THREE.Group();
      const p = new THREE.Mesh(new THREE.BoxGeometry(S, S, T), panelMat); p.castShadow = true; g.add(p);
      // inset seams (cyan light lines) + a raised centre plate with micro detail
      for (const [w, h, x, y] of [[S * 0.86, 0.008, 0, S * 0.43], [S * 0.86, 0.008, 0, -S * 0.43], [0.008, S * 0.86, S * 0.43, 0], [0.008, S * 0.86, -S * 0.43, 0], [S * 0.5, 0.006, 0, 0.06], [S * 0.3, 0.006, 0, -0.06]]) {
        for (const sgn of [1, -1]) { const l = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.004), seamMat); l.position.set(x, y, sgn * (T / 2 + 0.002)); g.add(l); }
      }
      const plate = new THREE.Mesh(new THREE.BoxGeometry(S * 0.62, S * 0.62, 0.012), new THREE.MeshStandardMaterial({ color: 0x8592ad, metalness: 0.7, roughness: 0.2 }));
      plate.position.z = T / 2 + 0.006; g.add(plate);
      return g;
    };
    // hinge groups: bottom stays; four sides hinge outward about their bottom edges; top hinges back about its rear edge
    const bottom = mkPanel(); bottom.rotation.x = -Math.PI / 2; bottom.position.y = T / 2; C.add(bottom);
    this.sides = [];
    for (let k = 0; k < 4; k++) {
      const hinge = new THREE.Group(); hinge.rotation.y = (k * Math.PI) / 2; C.add(hinge);
      const piv = new THREE.Group(); piv.position.set(0, 0, S / 2); hinge.add(piv);
      const pnl = mkPanel(); pnl.position.set(0, S / 2, 0); piv.add(pnl);
      this.sides.push(piv);
    }
    const topH = new THREE.Group(); topH.position.set(0, S, -S / 2); C.add(topH);
    const topP = mkPanel(); topP.rotation.x = -Math.PI / 2; topP.position.set(0, 0, S / 2); topH.add(topP); this.topH = topH;
    const core = new THREE.Mesh(new THREE.SphereGeometry(0.11, 32, 16), new THREE.MeshBasicMaterial({ color: 0xc9f6ff }));
    core.position.y = S / 2; C.add(core); this.core = core;
    const coreL = (this.coreL = new THREE.PointLight(0x48d8ff, 2.5, 4, 1.6)); coreL.position.y = S / 2 + 0.05; C.add(coreL);

    // ---------------- miniature world (grows out of the opened cube)
    const Wg = (this.world = new THREE.Group()); Wg.position.set(0, 0.2, 0); scene.add(Wg); this.WS = 0.78;
    const RAD = 1.15, terr = new THREE.CircleGeometry(RAD, 96, 0, Math.PI * 2);
    terr.rotateX(-Math.PI / 2);
    const tp = terr.attributes.position, n = tp.count;
    const hgt = new Float32Array(n);
    for (let i = 0; i < n; i++) {
      const x = tp.getX(i), z = tp.getZ(i), d = Math.hypot(x, z) / RAD;
      let h = 0.18 * noise(x * 2.2 + 3, z * 2.2 + 7) + 0.07 * noise(x * 6 + 1, z * 6 + 2);
      h = h * (1 - d * d) - 0.03 * d;
      if (Math.hypot(x - 0.35, z + 0.28) < 0.3) h = Math.min(h, 0.015);                 // lake bed
      tp.setY(i, h); hgt[i] = h;
    }
    terr.computeVertexNormals();
    this.cEmpty = []; this.cLive = []; const cols = new Float32Array(n * 3);
    for (let i = 0; i < n; i++) {
      const h = hgt[i], g = 0.22 + h * 1.6;
      this.cEmpty.push(g * 0.42, g * 0.46, g * 0.55);
      const lush = new THREE.Color().setHSL(0.37 - h * 0.5, 0.62, 0.17 + h * 0.75);
      if (h > 0.15) lush.setHSL(0.08, 0.15, 0.55 + h);                                  // rocky peaks
      this.cLive.push(lush.r, lush.g, lush.b);
    }
    terr.setAttribute('color', new THREE.BufferAttribute(cols, 3));
    this.terrCol = terr.attributes.color;
    const terrain = new THREE.Mesh(terr, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.85, metalness: 0.0, flatShading: true }));
    terrain.receiveShadow = terrain.castShadow = true; Wg.add(terrain);
    const rim2 = new THREE.Mesh(new THREE.CylinderGeometry(RAD, RAD * 0.92, 0.12, 96, 1, true), new THREE.MeshStandardMaterial({ color: 0x3b2f2a, roughness: 0.9 }));
    rim2.position.y = -0.06; Wg.add(rim2);
    const lakeMat = (this.lakeMat = new THREE.MeshStandardMaterial({ color: 0x3a5a7a, metalness: 0.2, roughness: 0.15, emissive: 0x0a3a66, emissiveIntensity: 0 }));
    const lake = new THREE.Mesh(new THREE.CircleGeometry(0.27, 48), lakeMat); lake.rotation.x = -Math.PI / 2; lake.position.set(0.35, 0.03, -0.28); Wg.add(lake);
    const hAt = (x, z) => { const d = Math.hypot(x, z) / RAD; let h = 0.18 * noise(x * 2.2 + 3, z * 2.2 + 7) + 0.07 * noise(x * 6 + 1, z * 6 + 2); return h * (1 - d * d) - 0.03 * d; };
    // trees
    this.trees = [];
    const trunkM = new THREE.MeshStandardMaterial({ color: 0x5a3e2b, roughness: 0.9 });
    for (let i = 0; i < 46; i++) {
      const a = R() * Math.PI * 2, rr = 0.25 + R() * 0.75; const x = Math.cos(a) * rr * RAD * 0.9, z = Math.sin(a) * rr * RAD * 0.9;
      if (Math.hypot(x - 0.35, z + 0.28) < 0.34 || (x < -0.05 && x > -0.75 && z > -0.2 && z < 0.45)) continue;
      const g = new THREE.Group(); g.position.set(x, hAt(x, z), z);
      const tr = new THREE.Mesh(new THREE.CylinderGeometry(0.008, 0.012, 0.05, 6), trunkM); tr.position.y = 0.025; g.add(tr);
      const hue = 0.3 + R() * 0.08, col = new THREE.Color().setHSL(hue, 0.5, 0.3 + R() * 0.1);
      const cone = new THREE.Mesh(new THREE.ConeGeometry(0.035 + R() * 0.02, 0.1 + R() * 0.06, 7), new THREE.MeshStandardMaterial({ color: col, roughness: 0.8, flatShading: true }));
      cone.position.y = 0.09; cone.castShadow = true; g.add(cone);
      g.userData.d = R(); Wg.add(g); this.trees.push(g);
    }
    // skyline (window glow comes on with life)
    const wc = document.createElement('canvas'); wc.width = 32; wc.height = 64; const wx = wc.getContext('2d');
    wx.fillStyle = '#000'; wx.fillRect(0, 0, 32, 64);
    const RW = rng(5); for (let y = 4; y < 64; y += 7) for (let x = 3; x < 32; x += 7) if (RW() > 0.35) { wx.fillStyle = RW() > 0.5 ? '#ffd9a0' : '#9fe7ff'; wx.fillRect(x, y, 4, 4); }
    const wt = new THREE.CanvasTexture(wc); wt.colorSpace = THREE.SRGBColorSpace; wt.magFilter = THREE.NearestFilter;
    this.bldMat = new THREE.MeshStandardMaterial({ color: 0xd7dfeb, roughness: 0.4, metalness: 0.3, emissive: 0xffffff, emissiveMap: wt, emissiveIntensity: 0 });
    this.blds = [];
    for (let i = 0; i < 26; i++) {
      const x = -0.12 - R() * 0.58, z = -0.15 + R() * 0.55, h = 0.06 + Math.pow(R(), 2) * 0.3, w = 0.05 + R() * 0.04;
      const b = new THREE.Mesh(new THREE.BoxGeometry(w, h, w), this.bldMat); b.position.set(x, hAt(x, z) + h / 2, z); b.castShadow = true;
      b.userData.h = h; b.userData.d = R(); Wg.add(b); this.blds.push(b);
    }
    // roads: a loop around the city with travelling lights
    const pts = []; for (let k = 0; k < 64; k++) { const a = (k / 64) * Math.PI * 2; const rr = 0.78 + 0.08 * Math.sin(a * 3); const x = Math.cos(a) * rr, z = Math.sin(a) * rr; pts.push(new THREE.Vector3(x, hAt(x, z) + 0.012, z)); }
    this.road = new THREE.CatmullRomCurve3(pts, true);
    this.roadMat = new THREE.MeshBasicMaterial({ color: 0x00c9ff, transparent: true, opacity: 0 });
    Wg.add(new THREE.Mesh(new THREE.TubeGeometry(this.road, 256, 0.006, 6, true), this.roadMat));
    this.cars = []; const carM = new THREE.MeshBasicMaterial({ color: 0xfff3c4 });
    for (let i = 0; i < 14; i++) { const c = new THREE.Mesh(new THREE.SphereGeometry(0.011, 8, 6), carM); c.userData.o = i / 14; Wg.add(c); this.cars.push(c); }
    // clouds
    this.clouds = []; const cM = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 1, transparent: true, opacity: 0.0 });
    this.cloudMat = cM;
    for (let i = 0; i < 6; i++) {
      const g = new THREE.Group(); for (let j = 0; j < 4; j++) { const s = new THREE.Mesh(new THREE.SphereGeometry(0.05 + R() * 0.04, 12, 8), cM); s.position.set(j * 0.06 - 0.09, R() * 0.02, R() * 0.04); g.add(s); }
      g.userData.a = (i / 6) * Math.PI * 2; g.userData.r = 0.55 + R() * 0.45; g.userData.y = 0.55 + R() * 0.15; Wg.add(g); this.clouds.push(g);
    }

    // ---------------- astronaut (chibi proportions, white suit, glass visor, backpack, chest light)
    const A = (this.astro = new THREE.Group()); scene.add(A);
    const suit = new THREE.MeshStandardMaterial({ color: 0xf1f3f7, roughness: 0.55 });
    const joint = new THREE.MeshStandardMaterial({ color: 0xb9c3d3, roughness: 0.5, metalness: 0.2 });
    const visor = new THREE.MeshStandardMaterial({ color: 0x10234a, metalness: 0.95, roughness: 0.08, emissive: 0x0b3a6e, emissiveIntensity: 0.35 });
    const cap = (r, l, m) => { const x = new THREE.Mesh(new THREE.CapsuleGeometry(r, l, 6, 14), m); x.castShadow = true; return x; };
    const body = cap(0.17, 0.2, suit); body.position.y = 0.52; A.add(body);
    const pack = new THREE.Mesh(new THREE.BoxGeometry(0.26, 0.3, 0.12), joint); pack.position.set(0, 0.56, -0.17); pack.castShadow = true; A.add(pack);
    const chest = new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.07, 0.03), new THREE.MeshStandardMaterial({ color: 0x223355, emissive: 0x00c9ff, emissiveIntensity: 0.9 })); chest.position.set(0, 0.6, 0.16); A.add(chest);
    const head = (this.aHead = new THREE.Group()); head.position.y = 0.86; A.add(head);
    const helm = new THREE.Mesh(new THREE.SphereGeometry(0.23, 40, 24), suit); helm.castShadow = true; head.add(helm);
    const vis = new THREE.Mesh(new THREE.SphereGeometry(0.2, 40, 24, -Math.PI * 0.42, Math.PI * 0.84, Math.PI * 0.26, Math.PI * 0.42), visor);
    vis.position.z = 0.045; head.add(vis);
    const neck = new THREE.Mesh(new THREE.TorusGeometry(0.15, 0.03, 10, 32), joint); neck.rotation.x = Math.PI / 2; neck.position.y = 0.7; A.add(neck);
    const limb = (x, y, upper, lower, r) => {
      const sh = new THREE.Group(); sh.position.set(x, y, 0); A.add(sh);
      const u = cap(r, upper, suit); u.position.y = -upper / 2 - r * 0.6; sh.add(u);
      const el = new THREE.Group(); el.position.y = -upper - r; sh.add(el);
      const l = cap(r * 0.92, lower, suit); l.position.y = -lower / 2 - r * 0.5; el.add(l);
      const end = new THREE.Mesh(new THREE.SphereGeometry(r * 1.15, 14, 10), joint); end.position.y = -lower - r; end.castShadow = true; el.add(end);
      return { sh, el };
    };
    this.armL = limb(-0.22, 0.66, 0.11, 0.1, 0.055); this.armR = limb(0.22, 0.66, 0.11, 0.1, 0.055);
    this.legL = limb(-0.09, 0.36, 0.1, 0.1, 0.07); this.legR = limb(0.09, 0.36, 0.1, 0.1, 0.07);
    this.armL.sh.rotation.z = 0.25; this.armR.sh.rotation.z = -0.25;
    r.compile(scene, this.cam);
  }

  // t = world time (s). 0-1.4 walk in, 1.4-2.0 reach, 2.0-3.3 cube unfolds, 2.4-3.8 world rises, 3.4-4.8 comes alive, then lives.
  render(t) {
    const life = ss(3.3, 4.9, t), open = t, grow = eo((t - 2.35) / 1.3);
    // astronaut walk to the cube
    const wk = ss(0, 1.45, t), walking = t < 1.45 ? Math.sin(t * Math.PI * 2 * 1.6) : 0;
    const A = this.astro; A.position.set(-1.45 + 0.4 * wk, 0, -1.45 + 0.45 * wk); A.rotation.y = 0.8;
    A.position.y = t < 1.45 ? Math.abs(Math.sin(t * Math.PI * 1.6 * 2)) * 0.02 : 0;
    this.legL.sh.rotation.x = 0.45 * walking * (1 - ss(1.2, 1.45, t)); this.legR.sh.rotation.x = -0.45 * walking * (1 - ss(1.2, 1.45, t));
    this.legL.el.rotation.x = Math.max(0, -walking) * 0.4; this.legR.el.rotation.x = Math.max(0, walking) * 0.4;
    const reach = ss(1.35, 1.95, t) * (1 - ss(2.25, 2.8, t)) , awe = ss(2.2, 3.0, t);
    this.armR.sh.rotation.x = -0.35 * walking - 1.15 * reach - 0.35 * awe * (1 - reach) + 0.04 * Math.sin(t * 1.3);
    this.armR.el.rotation.x = -0.35 * reach;
    this.armL.sh.rotation.x = 0.35 * walking - 0.25 * awe + 0.03 * Math.sin(t * 1.1 + 1);
    this.armL.sh.rotation.z = 0.25 + 0.2 * awe;
    this.aHead.rotation.x = 0.18 * reach - 0.22 * awe + 0.03 * Math.sin(t * 0.9);
    this.aHead.rotation.y = 0.12 * Math.sin(t * 0.45) * ss(4.5, 6, t);
    A.rotation.x = -0.06 * awe;
    // cube: hum, then unfold (top back, sides out, staggered with a little overshoot)
    const hum = 0.6 + 0.4 * Math.sin(t * 5.5);
    this.coreL.intensity = 1.6 + 1.6 * hum * (1 - life * 0.4) + 3 * ss(1.9, 2.2, t) * (1 - ss(2.6, 3.4, t));
    this.core.scale.setScalar(1 + 0.1 * hum + 0.35 * ss(1.95, 2.4, t) * (1 - ss(2.6, 3.2, t)));
    this.core.visible = t < 3.25;
    this.seamMat.color.setHSL(0.53, 1, 0.62 + 0.15 * hum);
    // top panel: hinges open, lifts off and folds away into the light (no floating slab)
    this.topH.rotation.x = -1.7 * back((t - 2.0) / 0.45); this.topH.position.y = 0.56 + 0.55 * eo((t - 2.3) / 0.6);
    this.topH.scale.setScalar(Math.max(0.001, 1 - ss(2.45, 2.95, t)));
    this.sides.forEach((p, k) => { p.rotation.x = (Math.PI / 2) * back((t - 2.12 - k * 0.08) / 0.55); });
    // world rises out of the open cube and comes alive
    const W = this.world; W.scale.setScalar(Math.max(0.001, grow * this.WS)); W.position.y = 0.2 + 0.08 * (1 - grow);
    W.rotation.y = t * 0.06;
    const col = this.terrCol.array;
    for (let i = 0; i < this.cEmpty.length; i++) col[i] = this.cEmpty[i] + (this.cLive[i] - this.cEmpty[i]) * life;
    this.terrCol.needsUpdate = true;
    this.trees.forEach((g) => g.scale.setScalar(Math.max(0.001, eo((life - g.userData.d * 0.5) / 0.4))));
    this.blds.forEach((b) => { const k = Math.max(0.001, eo((grow - 0.3 - b.userData.d * 0.4) / 0.4)); b.scale.set(1, k, 1); b.position.y = b.userData.base ?? (b.userData.base = b.position.y - b.userData.h / 2) ; b.position.y = b.userData.base + (b.userData.h * k) / 2; });
    this.bldMat.emissiveIntensity = 1.4 * ss(3.9, 4.7, t);
    this.roadMat.opacity = 0.85 * ss(3.7, 4.5, t);
    this.cars.forEach((c) => { const p = this.road.getPointAt((c.userData.o + t * 0.035) % 1); c.position.copy(p); c.visible = t > 4.2; });
    this.cloudMat.opacity = 0.92 * ss(3.6, 4.6, t);
    this.clouds.forEach((g) => { const a = g.userData.a + t * 0.05; g.position.set(Math.cos(a) * g.userData.r, g.userData.y, Math.sin(a) * g.userData.r); });
    this.lakeMat.color.setRGB(0.23 + 0.0 * life, 0.35 + 0.15 * life, 0.48 + 0.3 * life); this.lakeMat.emissiveIntensity = 0.5 * life;
    this.sky.material.uniforms.uLife.value = life;
    this.ringMat.color.setHSL(0.53, 1, 0.45 + 0.1 * Math.sin(t * 2));
    // camera: over-the-shoulder push, then a partial orbit around the reveal, then a slow living orbit
    const orbit = 0.95 - 0.55 * eo((t - 1.6) / 3.2) - 0.035 * Math.max(0, t - 4.8);
    const rad = 3.9 - 0.9 * eo(t / 2.2) - 0.25 * eo((t - 2.4) / 2.4) + 0.02 * Math.sin(t * 0.7);
    const hgt = 1.15 + 0.55 * eo((t - 2.2) / 2.2) + 0.015 * Math.sin(t * 1.1);
    this.cam.position.set(Math.sin(orbit) * rad, hgt, Math.cos(orbit) * rad);
    this.cam.lookAt(-0.15 * (1 - grow), 0.38 + 0.1 * grow, -0.2 * (1 - grow));
    this.renderer.render(this.scene, this.cam);
  }
}
window.World3D = { World };

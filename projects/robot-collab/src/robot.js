// AI PRENEUR ROBOT runtime: loads the rigged robot GLB (body / head / hand_L / hand_R + _FACE visor coordinates),
// draws a procedural screen face on the visor (eyes: blink, gaze, happy; talk bars driven by the voice), pulses the blue
// lights, and renders from a pure state object (deterministic: no clock, no randomness). Bundled to vendor/robot3d.js.
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';

const FACE_PARS = /* glsl */ `
varying vec3 vFace;
uniform float uBlink; uniform vec2 uGaze; uniform float uHappy; uniform float uTalk; uniform vec4 uBars; uniform float uBar5;
uniform float uEyeGlow; uniform float uSquint;
float sdEll(vec2 p, vec2 r) { float k0 = length(p / r); float k1 = length(p / (r * r)); return k0 * (k0 - 1.0) / max(k1, 1e-5); }
float sdRound(vec2 p, vec2 b, float rr) { vec2 q = abs(p) - b + rr; return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - rr; }
float screenFace(vec2 p) {
  float a = 0.0;
  for (int i = 0; i < 2; i++) {
    float sx = i == 0 ? -1.0 : 1.0;
    vec2 c = vec2(sx, 0.02) + uGaze;
    float open = max(0.07, 1.0 - uBlink);
    vec2 r = vec2(0.39 * (1.0 + 0.08 * uBlink), 0.58 * open * (1.0 - 0.25 * uSquint));
    float d = sdEll(p - c, r);
    // happy: upper arc only (a crescent "^")
    float dh = max(d, -sdEll(p - c - vec2(0.0, -0.34), vec2(0.46, 0.62)));
    d = mix(d, dh, uHappy);
    a = max(a, 1.0 - smoothstep(-0.03, 0.03, d));
  }
  // talk bars under the eyes (voice visualiser), centred at t = -1.0
  float bars[5]; bars[0] = uBars.x; bars[1] = uBars.y; bars[2] = uBars.z; bars[3] = uBars.w; bars[4] = uBar5;
  for (int k = 0; k < 5; k++) {
    float h = 0.035 + 0.20 * bars[k];
    float d = sdRound(p - vec2(-0.36 + 0.18 * float(k), -1.0), vec2(0.045, h), 0.045);
    a = max(a, (1.0 - smoothstep(-0.025, 0.025, d)) * uTalk);
  }
  return a;
}
`;

export class Robot {
  static async create(canvas, opts) { const m = new Robot(); await m.init(canvas, opts); return m; }
  async init(canvas, { url, width = 1080, height = 1920, envIntensity = 0.55 }) {
    this.W = width; this.H = height;
    const r = (this.renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, preserveDrawingBuffer: true, premultipliedAlpha: true }));
    r.setPixelRatio(1); r.setSize(width, height, false);
    r.outputColorSpace = THREE.SRGBColorSpace; r.toneMapping = THREE.NoToneMapping; r.setClearColor(0x000000, 0);
    const scene = (this.scene = new THREE.Scene());
    scene.environment = new THREE.PMREMGenerator(r).fromScene(new RoomEnvironment(), 0.04).texture;
    scene.environmentIntensity = envIntensity;
    // same light rig as the mascot so both characters sit in one world
    scene.add(new THREE.HemisphereLight(0xf4f8ff, 0x9fb0cc, 1.15));
    const key = new THREE.DirectionalLight(0xfff6ee, 1.9); key.position.set(-1.2, 2.2, 2.0); scene.add(key);
    const rim = (this.rim = new THREE.DirectionalLight(0xcfe0ff, 1.1)); rim.position.set(1.4, 1.2, -1.6); scene.add(rim);
    const fill = new THREE.DirectionalLight(0xffffff, 0.35); fill.position.set(1.5, 0.6, 2.0); scene.add(fill);
    this.cam = new THREE.OrthographicCamera(-1, 1, 1, -1, -10, 10);
    const gltf = await new GLTFLoader().loadAsync(url);
    this.root = gltf.scene; scene.add(this.root);
    this.rigRoot = this.root.getObjectByName('rig_root');
    this.bones = {}; this.root.traverse((o) => { if (o.isBone) this.bones[o.name] = o; if (o.isSkinnedMesh) this.mesh = o; });
    this.rest = {}; for (const [n, b] of Object.entries(this.bones)) this.rest[n] = b.position.clone();
    this.mesh.frustumCulled = false;
    const mat = this.mesh.material;
    if (mat.roughness !== undefined) { mat.metalness = Math.min(mat.metalness, 1); }
    mat.emissiveIntensity = 1.0;
    const u = (this.u = {
      uBlink: { value: 0 }, uGaze: { value: new THREE.Vector2() }, uHappy: { value: 0 }, uTalk: { value: 0 },
      uBars: { value: new THREE.Vector4() }, uBar5: { value: 0 }, uEyeGlow: { value: 1 }, uSquint: { value: 0 },
    });
    mat.onBeforeCompile = (sh) => {
      Object.assign(sh.uniforms, u);
      sh.vertexShader = sh.vertexShader
        .replace('#include <common>', '#include <common>\nattribute vec3 _face;\nvarying vec3 vFace;')
        .replace('#include <begin_vertex>', '#include <begin_vertex>\nvFace = _face;');
      sh.fragmentShader = sh.fragmentShader
        .replace('#include <common>', '#include <common>\n' + FACE_PARS)
        .replace('#include <map_fragment>', `#include <map_fragment>
          float faceA = vFace.z > 0.01 ? screenFace(vFace.xy) * vFace.z : 0.0;
          diffuseColor.rgb = mix(diffuseColor.rgb, vec3(0.93, 0.97, 1.0), faceA);`)
        .replace('#include <roughnessmap_fragment>', `#include <roughnessmap_fragment>
          roughnessFactor = mix(roughnessFactor, 0.35, faceA);`)
        .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
          totalEmissiveRadiance += vec3(0.82, 0.92, 1.0) * faceA * 0.95 * uEyeGlow;`);
    };
    mat.customProgramCacheKey = () => 'robot-face-v3';
    mat.needsUpdate = true;
    // soft contact shadow (only when the floor is in frame)
    const sc = document.createElement('canvas'); sc.width = sc.height = 128;
    const g = sc.getContext('2d'); const grd = g.createRadialGradient(64, 64, 0, 64, 64, 64);
    grd.addColorStop(0, 'rgba(10,13,44,0.36)'); grd.addColorStop(0.5, 'rgba(10,13,44,0.13)'); grd.addColorStop(1, 'rgba(10,13,44,0)');
    g.fillStyle = grd; g.fillRect(0, 0, 128, 128);
    const st = new THREE.CanvasTexture(sc); st.colorSpace = THREE.SRGBColorSpace;
    this.shadow = new THREE.Mesh(new THREE.PlaneGeometry(0.62, 0.42), new THREE.MeshBasicMaterial({ map: st, transparent: true, depthWrite: false }));
    this.shadow.rotation.x = -Math.PI / 2; this.shadow.position.y = 0.002; this.shadow.renderOrder = -1; this.shadow.visible = false;
    scene.add(this.shadow);
    r.compile(scene, this.cam);
  }
  // framing: base of the robot at (fx, fy) px, robot height h px (0.90 model units), camera yaw/pitch in degrees
  setView({ fx, fy, h, yaw = 0, pitch = 6 }) {
    const k = h / 0.9, c = this.cam;
    c.left = -fx / k; c.right = (this.W - fx) / k; c.top = fy / k; c.bottom = -(this.H - fy) / k;
    const a = (yaw * Math.PI) / 180, p = (pitch * Math.PI) / 180;
    c.position.set(Math.sin(a) * Math.cos(p) * 4, Math.sin(p) * 4, Math.cos(a) * Math.cos(p) * 4);
    c.up.set(0, 1, 0); c.lookAt(0, 0, 0); c.updateProjectionMatrix();
  }
  // state: root {x,y,z,rx,ry,rz,s}, bones {name:[rx,ry,rz]}, offs {name:[dx,dy,dz]} (bone translation offsets),
  // face {blink, gaze:[x,y], happy, squint, talk, bars:[5], glow}, ring (blue light intensity), shadow, visible
  setState(s) {
    const R = s.root || {}, rr = this.rigRoot;
    rr.position.set(R.x || 0, R.y || 0, R.z || 0); rr.rotation.set(R.rx || 0, R.ry || 0, R.rz || 0, 'YXZ');
    const sc = R.s == null ? 1 : R.s; rr.scale.set(sc, sc, sc);
    for (const [n, b] of Object.entries(this.bones)) {
      const v = (s.bones && s.bones[n]) || [0, 0, 0]; b.rotation.set(v[0], v[1], v[2], 'XYZ');
      const o = (s.offs && s.offs[n]) || [0, 0, 0]; b.position.set(this.rest[n].x + o[0], this.rest[n].y + o[1], this.rest[n].z + o[2]);
    }
    const f = s.face || {}, u = this.u;
    u.uBlink.value = f.blink || 0; u.uGaze.value.set(...(f.gaze || [0, 0])); u.uHappy.value = f.happy || 0; u.uSquint.value = f.squint || 0;
    u.uTalk.value = f.talk || 0; const b = f.bars || [0, 0, 0, 0, 0]; u.uBars.value.set(b[0], b[1], b[2], b[3]); u.uBar5.value = b[4];
    u.uEyeGlow.value = f.glow == null ? 1 : f.glow;
    this.mesh.material.emissiveIntensity = s.ring == null ? 1 : s.ring;
    this.shadow.visible = !!s.shadow; this.shadow.position.x = R.x || 0; this.shadow.position.z = (R.z || 0);
    const lift = Math.max(0, (R.y || 0)); this.shadow.scale.setScalar(Math.max(0.5, 1 - lift * 1.6) * sc); this.shadow.material.opacity = Math.max(0.25, 1 - lift * 2.2);
    this.visible = s.visible !== false;
  }
  render() { this.renderer.clear(); if (this.visible) this.renderer.render(this.scene, this.cam); }
}
window.Robot3D = { Robot };

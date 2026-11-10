// CGI MOTION: the premium cinematic look. Full PBR robot (clearcoat shell) lit by a procedural studio environment,
// warm key spot with soft shadows, strong cyan / cool rim lights from behind, dark sleek office with emissive data
// screens + LED strip, glossy mirror floor (planar reflection, blurred), holographic floor ring under the robot,
// soft light shaft from above, HDR bloom on the lights and eyes, shallow depth of field, ACES tonemap + grade,
// vignette, subtle chromatic fringe and film grain.
import * as THREE from 'three';
import { makeRT, Pass, Blur, lc } from '../common.js';
import { PAL, NPAL } from '../set.js';
import { litRobotMaterial } from '../robot.js';
import { litSetMaterial, makeEnv, FloorMirror } from '../lit.js';

const DEF = { c: 0x30343c, r: 0.6, m: 0.0, e: 0x000000, k: 0 };
function palette(o) {
  const cols = [], rm = [], em = [];
  for (let i = 0; i < NPAL; i++) {
    const name = Object.keys(PAL).find((k) => PAL[k] === i); const p = { ...DEF, ...(o[name] || {}) };
    cols.push(lc(p.c)); rm.push([p.r, p.m]); em.push(lc(p.e).multiplyScalar(p.k));
  }
  return { cols, rm, em };
}
const PALETTE = palette({
  floor: { c: 0x07090c, r: 0.22 }, wall: { c: 0x1b2330, r: 0.85 }, trim: { c: 0x0a0c10, e: 0x2fd6ff, k: 0.55 },
  deskTop: { c: 0x3a2618, r: 0.32 }, deskBody: { c: 0x101216, r: 0.45 }, monitor: { c: 0x0b0c0f, r: 0.25, m: 0.3 },
  screen: { c: 0x02040a, r: 0.2, e: 0x0b2c5a, k: 1.4 }, bar1: { c: 0x02040a, e: 0x23e0c5, k: 3.2 }, bar2: { c: 0x02040a, e: 0xffb43c, k: 3.0 },
  bar3: { c: 0x02040a, e: 0xff4f7a, k: 3.0 }, bar4: { c: 0x02040a, e: 0x3cc8ff, k: 3.6 }, board: { c: 0x0b1118, r: 0.12, m: 0.2, e: 0x07182a, k: 0.6 },
  boardFrame: { c: 0x9aa3ad, r: 0.32, m: 1.0 }, leaf: { c: 0x1d4a2c, r: 0.55 }, pot: { c: 0x23262c, r: 0.4 }, soil: { c: 0x120c08, r: 1 },
  winFrame: { c: 0x15171b, r: 0.4, m: 0.6 }, sky: { c: 0x000000, e: 0x0b1a33, k: 1.0 }, city: { c: 0x05070b, r: 0.9, e: 0xffc070, k: 0.0 },
  clock: { c: 0xb8c0c8, r: 0.25, m: 1.0 }, clockHand: { c: 0xffffff, e: 0xffffff, k: 0.4 }, keyboard: { c: 0x1a1c20, r: 0.5 }, mug: { c: 0xe8e8e8, r: 0.3 },
  axis: { c: 0x02040a, e: 0xbfefff, k: 1.6 },
});

const COMP = /* glsl */ `
uniform sampler2D tC; uniform sampler2D tD; uniform sampler2D tB1; uniform sampler2D tB2; uniform sampler2D tB3; uniform sampler2D tDof;
uniform vec2 uRes; uniform float uT; uniform vec2 uNF; uniform float uFocus; uniform float uExp;
varying vec2 vUv;
float viewZ(float d) { return uNF.x * uNF.y / ((uNF.y - uNF.x) * d - uNF.y); }
vec3 aces(vec3 x) { const float a = 2.51, b = 0.03, c = 2.43, d = 0.59, e = 0.14; return clamp((x * (a * x + b)) / (x * (c * x + d) + e), 0.0, 1.0); }
void main() {
  vec2 uv = vUv;
  // chromatic fringe towards the corners
  vec2 cc = uv - 0.5; float r2 = dot(cc, cc);
  vec3 sharp = vec3(texture2D(tC, uv - cc * r2 * 0.006).r, texture2D(tC, uv).g, texture2D(tC, uv + cc * r2 * 0.006).b);
  float z = -viewZ(texture2D(tD, uv).r);
  float coc = clamp(abs(1.0 / uFocus - 1.0 / z) * uFocus * 2.0, 0.0, 1.0);
  coc = smoothstep(0.08, 0.6, coc);
  vec3 blurred = texture2D(tDof, uv).rgb;
  vec3 col = mix(sharp, blurred, coc);
  col += texture2D(tB1, uv).rgb * 0.40 + texture2D(tB2, uv).rgb * 0.32 + texture2D(tB3, uv).rgb * 0.24;
  col *= uExp;
  col = aces(col);
  // grade: teal shadows, warm highlights
  float l = luma(col);
  col = mix(col * vec3(0.92, 1.02, 1.06), col * vec3(1.05, 1.0, 0.94), smoothstep(0.25, 0.8, l));
  col = pow(col, vec3(1.0 / 2.2));
  col *= 1.0 - 0.9 * r2;
  col += (h12(uv * uRes + floor(uT * 24.0) * 17.31) - 0.5) * 0.028;
  gl_FragColor = vec4(col, 1.0);
}`;
const BRIGHT = /* glsl */ `uniform sampler2D tSrc; uniform vec2 uTexel; uniform float uTh; varying vec2 vUv;
void main() { vec3 s = (texture2D(tSrc, vUv + uTexel * vec2(-0.5)) + texture2D(tSrc, vUv + uTexel * vec2(0.5)) + texture2D(tSrc, vUv + uTexel * vec2(0.5, -0.5)) + texture2D(tSrc, vUv + uTexel * vec2(-0.5, 0.5))).rgb * 0.25;
  float l = luma(s); gl_FragColor = vec4(s * smoothstep(uTh, uTh * 2.2, l), 1.0); }`;
const DOWN = /* glsl */ `uniform sampler2D tSrc; uniform vec2 uTexel; varying vec2 vUv;
void main() { gl_FragColor = (texture2D(tSrc, vUv + uTexel * vec2(-1.0)) + texture2D(tSrc, vUv + uTexel * vec2(1.0)) + texture2D(tSrc, vUv + uTexel * vec2(1.0, -1.0)) + texture2D(tSrc, vUv + uTexel * vec2(-1.0, 1.0))) * 0.25; }`;

export default function createCgi(ctx) {
  const { W, H, renderer } = ctx;
  const scene = new THREE.Scene();
  scene.background = lc(0x05070a);
  scene.environment = makeEnv(renderer, { bg: 0x020306, panels: [
    { pos: [-1.5, 4.2, 2.0], size: [3.2, 1.6], look: [0, 0.6, 0], color: 0xfff1e2, intensity: 7.0 },
    { pos: [0.4, 1.2, 4.2], size: [3.0, 1.6], look: [0, 0.6, 0], color: 0xf2f6ff, intensity: 2.2 },
    { pos: [-3.4, 1.4, -1.2], size: [0.6, 3.0], look: [0, 1, 0], color: 0x34d6ff, intensity: 7.0 },
    { pos: [3.2, 1.6, -1.8], size: [0.8, 3.0], look: [0, 1, 0], color: 0xc8dcff, intensity: 5.0 },
    { pos: [2.6, 1.2, 3.0], size: [2.0, 1.4], look: [0, 1, 0], color: 0xffd2a8, intensity: 1.0 },
  ] });
  scene.environmentIntensity = 0.9;
  const robotMat = litRobotMaterial(ctx.rig, { physical: true, key: 'cgi', clearcoat: 0.8, clearcoatRoughness: 0.08, emiK: 3.6, eyeK: 2.4, emi: [0.25, 0.65, 1.0], eye: [0.75, 0.92, 1.0], visorRough: 0.06 });
  const robot = ctx.robotMesh(robotMat); robot.castShadow = true; scene.add(robot);
  const mirror = new FloorMirror();
  const rtRefl = makeRT(Math.ceil(W / 2), Math.ceil(H / 2), { type: THREE.HalfFloatType });
  const reflBlur = new Blur(Math.ceil(W / 2), Math.ceil(H / 2), THREE.HalfFloatType);
  const uRefl = { tRefl: { value: null }, uTexMat: { value: mirror.texMat }, uReflK: { value: 1.0 } };
  const setMat = litSetMaterial({ ...PALETTE, physical: false, key: 'cgi', uniforms: uRefl, hooks: {
    pars: 'uniform sampler2D tRefl; uniform mat4 uTexMat; uniform float uReflK;\n',
    albedo: /* glsl */ `
      if (vPal == ${PAL.wall}) { float pn = abs(fract(vWPos.x / 0.62) - 0.5); diffuseColor.rgb *= 1.0 - 0.35 * smoothstep(0.485, 0.495, pn); }
      if (vPal == ${PAL.floor}) { float t = abs(fract(vWPos.x / 0.9) - 0.5); diffuseColor.rgb *= 1.0 - 0.5 * smoothstep(0.494, 0.498, t); }`,
    emissive: /* glsl */ `
      if (vPal == ${PAL.city}) { vec2 q = vec2(vWPos.x * 13.0, vWPos.y * 10.0); vec2 g = floor(q); vec2 f = fract(q) - 0.5;
        float lw = 1.0 - smoothstep(0.18, 0.3, max(abs(f.x), abs(f.y) * 0.8));
        totalEmissiveRadiance += vec3(1.0, 0.72, 0.42) * 1.6 * step(0.6, h12(g)) * lw; }
      if (vPal == ${PAL.sky}) totalEmissiveRadiance *= 0.6 + 0.8 * smoothstep(0.9, 1.8, vWPos.y);
      if (vPal == ${PAL.floor}) {
        vec4 rp = uTexMat * vec4(vWPos, 1.0);
        vec3 refl = texture2DProj(tRefl, rp).rgb;
        vec3 V = normalize(cameraPosition - vWPos);
        float fr = 0.06 + 0.94 * pow(1.0 - max(V.y, 0.0), 5.0);
        totalEmissiveRadiance += refl * mix(0.3, 0.85, fr) * uReflK;
      }`,
  } });
  const setMesh = new THREE.Mesh(ctx.setGeo.sharp, setMat); setMesh.receiveShadow = true; scene.add(setMesh);
  // holographic floor ring + glow under the robot
  const ringG = new THREE.Group(); scene.add(ringG);
  const ringMat = (k, col) => new THREE.MeshBasicMaterial({ color: lc(col).multiplyScalar(k), transparent: true, blending: THREE.AdditiveBlending, depthWrite: false, toneMapped: false });
  const r1 = new THREE.Mesh(new THREE.RingGeometry(0.43, 0.452, 96), ringMat(3.0, 0x2fd6ff)); r1.rotation.x = -Math.PI / 2; r1.position.y = 0.004; ringG.add(r1);
  const r2 = new THREE.Mesh(new THREE.RingGeometry(0.5, 0.507, 96), ringMat(1.2, 0x2fd6ff)); r2.rotation.x = -Math.PI / 2; r2.position.y = 0.004; ringG.add(r2);
  const glowMat = new THREE.ShaderMaterial({ transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, uniforms: {},
    vertexShader: 'varying vec2 vU; void main(){ vU = uv * 2.0 - 1.0; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',
    fragmentShader: 'varying vec2 vU; void main(){ float r = length(vU); float g = exp(-pow((r - 0.73) / 0.08, 2.0)) * 0.6 + (1.0 - smoothstep(0.0, 0.75, r)) * 0.18; gl_FragColor = vec4(vec3(0.05, 0.45, 0.8) * g, 1.0); }' });
  const glow = new THREE.Mesh(new THREE.PlaneGeometry(1.25, 1.25), glowMat); glow.rotation.x = -Math.PI / 2; glow.position.y = 0.003; ringG.add(glow);
  // light shaft from above
  const shaftMat = new THREE.ShaderMaterial({ transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide,
    vertexShader: 'varying vec3 vN; varying vec3 vV; varying float vY; void main(){ vec4 w = modelMatrix * vec4(position,1.0); vY = position.y; vN = normalize(mat3(modelMatrix) * normal); vV = normalize(cameraPosition - w.xyz); gl_Position = projectionMatrix * viewMatrix * w; }',
    fragmentShader: 'varying vec3 vN; varying vec3 vV; varying float vY; void main(){ float f = pow(abs(dot(normalize(vN), normalize(vV))), 2.5); float h = smoothstep(-1.3, 0.6, vY) * (1.0 - smoothstep(0.9, 1.3, vY)); gl_FragColor = vec4(vec3(0.9, 0.85, 0.75) * f * h * 0.05, 1.0); }' });
  const shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.75, 2.6, 48, 1, true), shaftMat); shaft.position.set(-0.05, 1.3, 0.05); scene.add(shaft);
  // lights
  const key = new THREE.SpotLight(0xfff0de, 48, 0, 0.55, 0.65, 2); key.position.set(-1.6, 3.0, 2.4); key.target.position.set(0, 0.45, 0);
  key.castShadow = true; key.shadow.mapSize.set(1024, 1024); key.shadow.bias = -0.0004; key.shadow.normalBias = 0.01; key.shadow.radius = 6; key.shadow.camera.near = 1; key.shadow.camera.far = 8;
  scene.add(key, key.target);
  const rimA = new THREE.SpotLight(0x37d4ff, 55, 0, 0.6, 0.6, 2); rimA.position.set(-1.7, 2.2, -1.9); rimA.target.position.set(0, 0.55, 0); scene.add(rimA, rimA.target);
  const rimB = new THREE.SpotLight(0xd2e2ff, 40, 0, 0.6, 0.6, 2); rimB.position.set(1.9, 1.8, -1.6); rimB.target.position.set(0, 0.5, 0); scene.add(rimB, rimB.target);
  const fill = new THREE.HemisphereLight(0x8fb4d8, 0x0a0c10, 0.12); scene.add(fill);
  // wall wash: soft cool gradient on the back wall behind the robot (separates it from the background)
  const wash = new THREE.SpotLight(0x6f9bd6, 14, 0, 0.9, 0.9, 2); wash.position.set(0.3, 2.9, -0.4); wash.target.position.set(0.1, 0.9, -1.3); scene.add(wash, wash.target);
  // targets + post
  const rt = makeRT(W, H, { type: THREE.HalfFloatType, samples: 4, depthTexture: true });
  const hw = Math.ceil(W / 2), hh = Math.ceil(H / 2), qw = Math.ceil(W / 4), qh = Math.ceil(H / 4);
  const rtHalf = makeRT(hw, hh, { depth: false, type: THREE.HalfFloatType });
  const rtQ = makeRT(qw, qh, { depth: false, type: THREE.HalfFloatType });
  const bright = new Pass(BRIGHT, { tSrc: { value: rt.texture }, uTexel: { value: new THREE.Vector2(1 / W, 1 / H) }, uTh: { value: 1.3 } });
  const down = new Pass(DOWN, { tSrc: { value: null }, uTexel: { value: new THREE.Vector2(1 / hw, 1 / hh) } });
  const bl1 = new Blur(hw, hh, THREE.HalfFloatType), bl2 = new Blur(qw, qh, THREE.HalfFloatType), bl3 = new Blur(Math.ceil(qw / 2), Math.ceil(qh / 2), THREE.HalfFloatType);
  const dofDown = new Pass(DOWN, { tSrc: { value: rt.texture }, uTexel: { value: new THREE.Vector2(1 / W, 1 / H) } });
  const rtDofH = makeRT(hw, hh, { depth: false, type: THREE.HalfFloatType });
  const dofBlur = new Blur(qw, qh, THREE.HalfFloatType);
  const comp = new Pass(COMP, { tC: { value: rt.texture }, tD: { value: rt.depthTexture }, tB1: { value: null }, tB2: { value: null }, tB3: { value: null }, tDof: { value: null },
    uRes: { value: new THREE.Vector2(W, H) }, uT: { value: 0 }, uNF: { value: new THREE.Vector2() }, uFocus: { value: 4.5 }, uExp: { value: 0.95 } });
  return {
    render(target) {
      const r = ctx.renderer, cam = ctx.camera, rr = ctx.rig.rigRoot;
      robot.visible = ctx.robotVisible;
      ringG.position.set(rr.position.x, 0, rr.position.z); shaft.position.x = rr.position.x - 0.05; shaft.position.z = rr.position.z + 0.05;
      r.shadowMap.enabled = true; r.shadowMap.needsUpdate = true;
      // mirror pass (floor reflection), blurred = glossy
      const vc = mirror.update(cam);
      setMat.userData.u.uReflK.value = 0.0; ringG.visible = true;
      r.setRenderTarget(rtRefl); r.clear(); r.render(scene, vc);
      setMat.userData.u.uReflK.value = 1.0;
      setMat.userData.u.tRefl.value = reflBlur.run(r, rtRefl.texture, 1.0, 1);
      // main
      r.setRenderTarget(rt); r.clear(); r.render(scene, cam);
      // bloom ladder
      bright.render(r, rtHalf);
      comp.u.tB1.value = bl1.run(r, rtHalf.texture, 1.0, 1);
      down.u.tSrc.value = bl1.out.texture; down.u.uTexel.value.set(1 / hw, 1 / hh); down.render(r, rtQ);
      comp.u.tB2.value = bl2.run(r, rtQ.texture, 1.5, 1);
      comp.u.tB3.value = bl3.run(r, bl2.out.texture, 2.0, 2);
      // depth of field source (quarter-res blur of the frame)
      dofDown.render(r, rtDofH);
      comp.u.tDof.value = dofBlur.run(r, rtDofH.texture, 1.6, 2);
      const dist = cam.position.distanceTo(new THREE.Vector3(rr.position.x, 0.5 + rr.position.y, rr.position.z));
      comp.u.uFocus.value = dist; comp.u.uNF.value.set(cam.near, cam.far); comp.u.uT.value = ctx.t;
      comp.render(r, target);
    },
  };
}

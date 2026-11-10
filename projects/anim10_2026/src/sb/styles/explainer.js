// EXPLAINER 3D: soft clay / pastel product-explainer look. Rounded set (bevelled boxes), matte clay materials in a
// beige + pastel palette, sunny window, big soft key light with soft shadows, warm sky / ground ambient, the robot
// re-coloured as a satin clay toy (warm white shell, soft navy parts, glossy visor, gentle sky-blue lights).
import * as THREE from 'three';
import { makeRT, Pass, lc } from '../common.js';
import { PAL, NPAL } from '../set.js';
import { litRobotMaterial } from '../robot.js';
import { litSetMaterial, makeEnv } from '../lit.js';

function palette(o) {
  const cols = [], rm = [], em = [];
  for (let i = 0; i < NPAL; i++) {
    const name = Object.keys(PAL).find((k) => PAL[k] === i); const p = { c: 0xd8cfc4, r: 0.85, m: 0, e: 0, k: 0, ...(o[name] || {}) };
    cols.push(lc(p.c)); rm.push([p.r, p.m]); em.push(lc(p.e).multiplyScalar(p.k));
  }
  return { cols, rm, em };
}
const PALETTE = palette({
  floor: { c: 0xe6cfb4, r: 0.9 }, wall: { c: 0xf4e7d7, r: 0.95 }, trim: { c: 0xead6bf }, deskTop: { c: 0xf6ae92, r: 0.7 }, deskBody: { c: 0xf9d8c3, r: 0.8 },
  monitor: { c: 0x8f9cb8, r: 0.55 }, screen: { c: 0xd6ebff, r: 0.4, e: 0xd6ebff, k: 0.35 }, bar1: { c: 0x8fdcb9, r: 0.6 }, bar2: { c: 0xffd87a, r: 0.6 },
  bar3: { c: 0xff9a8a, r: 0.6 }, bar4: { c: 0x86c3ff, r: 0.6 }, board: { c: 0xfffaf2, r: 0.8 }, boardFrame: { c: 0xb4c3e6, r: 0.6 },
  leaf: { c: 0x86c995, r: 0.75 }, pot: { c: 0xe5946f, r: 0.8 }, soil: { c: 0x8a6550 }, winFrame: { c: 0xffffff, r: 0.6 },
  sky: { c: 0x000000, e: 0xbfe2ff, k: 1.25 }, city: { c: 0xd9ebfa, r: 0.9, e: 0xd9ebfa, k: 0.55 }, clock: { c: 0xfff8ee, r: 0.6 },
  clockHand: { c: 0x6b7385 }, keyboard: { c: 0xf6f4f1, r: 0.6 }, mug: { c: 0xffc4b2, r: 0.5 }, axis: { c: 0x7b88a6, r: 0.7 },
});

const COMP = /* glsl */ `
uniform sampler2D tC; uniform vec2 uRes; varying vec2 vUv;
vec3 filmic(vec3 x) { x *= 0.92; return clamp((x * (2.2 * x + 0.04)) / (x * (2.05 * x + 0.62) + 0.16), 0.0, 1.0); }
void main() {
  vec3 c = texture2D(tC, vUv).rgb;
  c = filmic(c);
  c = pow(c, vec3(1.0 / 2.2));
  c = mix(c, c * vec3(1.03, 1.0, 0.96), 0.6);
  vec2 v = vUv - 0.5; c *= 1.0 - 0.28 * dot(v, v);
  gl_FragColor = vec4(c, 1.0);
}`;

export default function createExplainer(ctx) {
  const { W, H, renderer } = ctx;
  const scene = new THREE.Scene();
  scene.background = lc(0xf4e7d7);
  scene.environment = makeEnv(renderer, { bg: 0xcdbca8, bgK: 0.6, panels: [
    { pos: [-2.2, 3.6, 2.8], size: [3.5, 2.5], look: [0, 0.6, 0], color: 0xfff4e6, intensity: 2.2 },
    { pos: [3.0, 1.8, 2.0], size: [2.0, 2.0], look: [0, 0.6, 0], color: 0xe6efff, intensity: 1.0 },
  ] });
  scene.environmentIntensity = 0.45;
  const robotMat = litRobotMaterial(ctx.rig, { key: 'explainer', noNormal: true, smoothN: true, rough: [0.5, 0.0], visorRough: 0.18, emiK: 0.9, eyeK: 1.4,
    emi: [0.5, 0.8, 1.0], eye: [0.85, 0.95, 1.0], eyeAlb: [0.95, 0.98, 1.0],
    classes: { white: [0.86, 0.82, 0.77], dark: [0.055, 0.066, 0.13], blue: [0.22, 0.58, 1.0], visor: [0.02, 0.025, 0.06], logo: [0.06, 0.07, 0.15] } });
  const robot = ctx.robotMesh(robotMat); robot.castShadow = true; robot.receiveShadow = true; scene.add(robot);
  const setMat = litSetMaterial({ ...PALETTE, key: 'explainer', hooks: {
    albedo: /* glsl */ `
      if (vPal == ${PAL.floor}) { float t = abs(fract(vWPos.x / 0.5) - 0.5); diffuseColor.rgb *= 1.0 - 0.06 * smoothstep(0.47, 0.49, t); }
      if (vPal == ${PAL.sky}) { float cl = smoothstep(0.55, 0.8, fbm(vWPos.xy * vec2(2.2, 4.0) + 3.0)); diffuseColor.rgb = vec3(0.0); }`,
    emissive: /* glsl */ `
      if (vPal == ${PAL.sky}) { float cl = smoothstep(0.55, 0.75, fbm(vWPos.xy * vec2(2.0, 4.2) + 3.0)); totalEmissiveRadiance = mix(totalEmissiveRadiance, vec3(1.25), cl * 0.8); }`,
  } });
  const setMesh = new THREE.Mesh(ctx.softSet(), setMat); setMesh.receiveShadow = true; setMesh.castShadow = true; scene.add(setMesh);
  scene.add(new THREE.HemisphereLight(0xfff3e6, 0xd8c3ac, 1.35));
  const key = new THREE.DirectionalLight(0xfff1e0, 2.4); key.position.set(-2.2, 3.4, 2.6); key.target.position.set(0, 0.4, -0.3);
  key.castShadow = true; key.shadow.mapSize.set(1024, 1024); key.shadow.bias = -0.0005; key.shadow.normalBias = 0.02;
  Object.assign(key.shadow.camera, { left: -2.2, right: 2.2, top: 2.4, bottom: -1.2, near: 0.5, far: 9 }); key.shadow.camera.updateProjectionMatrix();
  scene.add(key, key.target);
  const fill = new THREE.DirectionalLight(0xdfe9ff, 0.7); fill.position.set(2.5, 1.5, 2.0); scene.add(fill);
  const rt = makeRT(W, H, { type: THREE.HalfFloatType, samples: 4 });
  const comp = new Pass(COMP, { tC: { value: rt.texture }, uRes: { value: new THREE.Vector2(W, H) } });
  return {
    render(target) {
      const r = ctx.renderer;
      robot.visible = ctx.robotVisible;
      r.shadowMap.needsUpdate = true;
      r.setRenderTarget(rt); r.clear(); r.render(scene, ctx.camera);
      comp.render(r, target);
    },
  };
}

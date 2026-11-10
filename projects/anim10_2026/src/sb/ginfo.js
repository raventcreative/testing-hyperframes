// Info + G-buffer materials for the line-based styles (glow, line, chalk):
//   out0 (info): r = key-light lambert (0..1), g = eye / screen glow mask, b = blue-light mask, a = wordmark (robot) | floor pool (set)
//   out1 (G):    view normal xy, inverse depth, surface id (set: palette + 1, robot: 30..34)
import * as THREE from 'three';
import { styleMat, makeRT, ROBOT_ID } from './common.js';
import { PAL } from './set.js';

export function gInfoScene(ctx, { keyDir = [-0.6, 0.7, 0.45], smooth = true, poolR = 0.75, hideCity = false, simpleIds = false } = {}) {
  const uKey = { value: new THREE.Vector3(...keyDir).normalize() };
  const uPool = { value: new THREE.Vector3(0, 0, poolR) };
  const robotMat = styleMat({ robot: true, rawNormals: !smooth, shared: ctx.rig.shared, defines: { MRT: '' }, uniforms: { uKey }, extra: ROBOT_ID + 'uniform vec3 uKey;\n', frag: /* glsl */ `
    void main() {
      RobotSurf s = robotSurf();
      float ndl = clamp(dot(normalize(vN), uKey) * 0.5 + 0.5, 0.0, 1.0);
      gl_FragColor = vec4(ndl, s.eye, s.blue * uRing, s.logo);
      ${simpleIds ? `
      // minimal ids: shell / visor (geometric ellipse -> one clean visor contour) / eyes
      float ell = pow((vRest.x - 0.078) / 0.27, 2.0) + pow((vRest.y - 0.647) / 0.18, 2.0);
      float fr = step(0.1, vRest.z) * step(0.0, vRestN.z);
      float vis = step(ell, 1.18) * fr, bez = step(ell, 1.6) * fr;
      writeG(s.eye > 0.5 ? 34.0 : (vis > 0.5 ? 33.0 : (s.blue > 0.5 ? 32.0 : (s.white > 0.5 || bez > 0.5 ? 30.0 : 31.0))));` : 'writeG(robotId(s));'}
    }` });
  const setMat = styleMat({ robot: false, defines: { MRT: '' }, uniforms: { uKey, uPool }, extra: 'uniform vec3 uKey; uniform vec3 uPool;\n', frag: /* glsl */ `
    void main() {
      float ndl = clamp(dot(normalize(vN), uKey) * 0.5 + 0.5, 0.0, 1.0);
      float pool = vPal == ${PAL.floor} ? 1.0 - smoothstep(0.0, uPool.z, length(vW.xz - uPool.xy)) : 0.0;
      float glow = vPal == ${PAL.screen} ? 1.0 : 0.0;
      // floor dot grid (world space, anti-aliased): used by the minimal-line style
      float dots = 0.0;
      if (vPal == ${PAL.floor}) { vec2 gp = vW.xz / 0.22; vec2 f = fract(gp) - 0.5; float d = length(f) * 0.22; float w = fwidth(d) + 1e-4;
        dots = 1.0 - smoothstep(0.006 - w, 0.006 + w, d); }
      gl_FragColor = vec4(ndl, glow, dots, pool);
      writeG(float(vPal) + 1.0);
      ${hideCity ? `if (vPal == ${PAL.sky} || vPal == ${PAL.city}) { gl_FragColor = vec4(0.0); gOut1 = vec4(0.5, 0.5, 0.0, 0.0); }` : ''}
    }` });
  const scene = new THREE.Scene();
  const robot = ctx.robotMesh(robotMat); scene.add(robot);
  scene.add(new THREE.Mesh(ctx.setGeo.sharp, setMat));
  return {
    scene, robot, uKey, uPool,
    // render into an MRT target (count 2): textures[0] = info, textures[1] = G
    render(rt) {
      const r = ctx.renderer;
      robot.visible = ctx.robotVisible;
      const rr = ctx.rig.rigRoot; uPool.value.x = rr.position.x; uPool.value.y = rr.position.z;
      r.setRenderTarget(rt); r.setClearColor(new THREE.Color(0.5, 0.5, 0.0), 0.0); r.clear(); r.render(scene, ctx.camera);
      r.setClearColor(0x000000, 1);
    },
  };
}

export function makeGTarget(w, h, samples = 0) { return makeRT(w, h, { count: 2, type: THREE.HalfFloatType, samples }); }

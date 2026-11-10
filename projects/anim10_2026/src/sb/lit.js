// Helpers for the lit (PBR) styles: palette-driven MeshStandard/Physical set material with GLSL hooks, procedural
// studio environments (PMREM from emissive panels), planar mirror camera for glossy floors.
import * as THREE from 'three';
import { NOISE } from './common.js';
import { NPAL } from './set.js';

// cols: THREE.Color[] (linear), rm: [rough, metal][], em: THREE.Color[] (linear emissive)
// hooks: { pars, albedo, rough, emissive } GLSL snippets (have vPal, vWPos, vViewN available)
export function litSetMaterial({ cols, rm, em, physical = false, hooks = {}, uniforms = {}, key = 'x', side = THREE.FrontSide, phys = {} }) {
  const mat = new (physical ? THREE.MeshPhysicalMaterial : THREE.MeshStandardMaterial)({ color: 0xffffff, roughness: 1, metalness: 0, side, ...phys });
  const U = {
    uCol: { value: cols }, uRM: { value: rm.map((v) => new THREE.Vector2(v[0], v[1])) },
    uEm: { value: em || cols.map(() => new THREE.Color(0, 0, 0)) }, ...uniforms,
  };
  mat.userData.u = U;
  mat.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, U);
    sh.vertexShader = sh.vertexShader
      .replace('#include <common>', '#include <common>\nattribute float aPal;\nflat varying int vPal;\nvarying vec3 vWPos;\n' + (hooks.vpars || ''))
      .replace('#include <begin_vertex>', '#include <begin_vertex>\nvPal = int(aPal + 0.5);\nvWPos = (modelMatrix * vec4(transformed, 1.0)).xyz;\n' + (hooks.vertex || ''));
    sh.fragmentShader = sh.fragmentShader
      .replace('#include <common>', `#include <common>\nflat varying int vPal;\nvarying vec3 vWPos;\nuniform vec3 uCol[${NPAL}]; uniform vec2 uRM[${NPAL}]; uniform vec3 uEm[${NPAL}];\n` + NOISE + (hooks.pars || ''))
      .replace('#include <map_fragment>', '#include <map_fragment>\ndiffuseColor.rgb = uCol[vPal];\n' + (hooks.albedo || ''))
      .replace('#include <roughnessmap_fragment>', '#include <roughnessmap_fragment>\nroughnessFactor = uRM[vPal].x;\n' + (hooks.rough || ''))
      .replace('#include <metalnessmap_fragment>', '#include <metalnessmap_fragment>\nmetalnessFactor = uRM[vPal].y;\n')
      .replace('#include <normal_fragment_maps>', '#include <normal_fragment_maps>\n' + (hooks.normal || ''))
      .replace('#include <emissivemap_fragment>', '#include <emissivemap_fragment>\ntotalEmissiveRadiance = uEm[vPal];\n' + (hooks.emissive || ''))
      .replace('#include <opaque_fragment>', (hooks.final || '') + '\n#include <opaque_fragment>');
  };
  mat.customProgramCacheKey = () => 'sb-litset-' + key;
  return mat;
}

// studio environment: a dark box with emissive panels -> PMREM (for reflections / IBL)
// panels: [{ pos:[x,y,z], size:[w,h], look:[x,y,z], color:hex, intensity }]
export function makeEnv(renderer, { bg = 0x000000, bgK = 1, panels = [] } = {}) {
  const sc = new THREE.Scene();
  const room = new THREE.Mesh(new THREE.BoxGeometry(14, 8, 14), new THREE.MeshBasicMaterial({ color: new THREE.Color(bg).multiplyScalar(bgK), side: THREE.BackSide }));
  room.position.y = 3; sc.add(room);
  for (const p of panels) {
    const m = new THREE.Mesh(new THREE.PlaneGeometry(p.size[0], p.size[1]), new THREE.MeshBasicMaterial({ color: new THREE.Color(p.color).multiplyScalar(p.intensity), side: THREE.DoubleSide }));
    m.position.set(...p.pos); m.lookAt(...(p.look || [0, 1, 0])); sc.add(m);
  }
  const pm = new THREE.PMREMGenerator(renderer);
  const tex = pm.fromScene(sc, 0.0, 0.1, 30).texture;
  pm.dispose();
  return tex;
}

// planar mirror (y = 0 plane): virtual camera + texture matrix (same math as three's Reflector)
export class FloorMirror {
  constructor() { this.cam = new THREE.PerspectiveCamera(); this.texMat = new THREE.Matrix4(); }
  update(camera) {
    const normal = new THREE.Vector3(0, 1, 0), pos = new THREE.Vector3(0, 0, 0);
    const camPos = new THREE.Vector3().setFromMatrixPosition(camera.matrixWorld);
    const rot = new THREE.Matrix4().extractRotation(camera.matrixWorld);
    const view = pos.clone().sub(camPos).reflect(normal).negate().add(pos);
    const look = new THREE.Vector3(0, 0, -1).applyMatrix4(rot).add(camPos);
    const target = pos.clone().sub(look).reflect(normal).negate().add(pos);
    const vc = this.cam;
    vc.position.copy(view); vc.up.set(0, 1, 0).applyMatrix4(rot).reflect(normal); vc.lookAt(target);
    vc.far = camera.far; vc.updateMatrixWorld(); vc.projectionMatrix.copy(camera.projectionMatrix); vc.projectionMatrixInverse.copy(camera.projectionMatrixInverse);
    this.texMat.set(0.5, 0, 0, 0.5, 0, 0.5, 0, 0.5, 0, 0, 0.5, 0.5, 0, 0, 0, 1).multiply(vc.projectionMatrix).multiply(vc.matrixWorldInverse);
    // oblique near plane = the floor (nothing below it gets into the reflection)
    const plane = new THREE.Plane().setFromNormalAndCoplanarPoint(normal, pos).applyMatrix4(vc.matrixWorldInverse);
    const clip = new THREE.Vector4(plane.normal.x, plane.normal.y, plane.normal.z, plane.constant), pm = vc.projectionMatrix, q = new THREE.Vector4();
    q.x = (Math.sign(clip.x) + pm.elements[8]) / pm.elements[0]; q.y = (Math.sign(clip.y) + pm.elements[9]) / pm.elements[5]; q.z = -1; q.w = (1 + pm.elements[10]) / pm.elements[14];
    clip.multiplyScalar(2 / clip.dot(q));
    pm.elements[2] = clip.x; pm.elements[6] = clip.y; pm.elements[10] = clip.z + 1 - 0.003; pm.elements[14] = clip.w;
    return vc;
  }
}

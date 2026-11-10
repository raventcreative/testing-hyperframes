// Robot loading + pose state (same state shape as src/robot_base.js) + PBR face injection for lit styles.
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { FACE, LOGO } from './common.js';

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
  return rig;
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
  mat.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, u, P);
    sh.vertexShader = sh.vertexShader
      .replace('#include <common>', '#include <common>\nattribute vec3 _face;\nvarying vec3 vFace;')
      .replace('#include <begin_vertex>', '#include <begin_vertex>\nvFace = _face;');
    sh.fragmentShader = sh.fragmentShader
      .replace('#include <common>', '#include <common>\nvarying vec3 vFace;\nuniform vec3 uTint; uniform vec3 uDarkTint; uniform vec3 uEmiCol; uniform vec3 uEyeCol; uniform vec3 uEyeAlb; uniform vec2 uRough; uniform float uEyeK; uniform float uEmiK; uniform float uVisorRough;\n' + FACE)
      .replace('#include <map_fragment>', `#include <map_fragment>
        float faceA = vFace.z > 0.01 ? screenFace(vFace.xy) * vFace.z : 0.0;
        float lumA = dot(diffuseColor.rgb, vec3(0.2126, 0.7152, 0.0722));
        float wht = smoothstep(0.10, 0.45, lumA);
        diffuseColor.rgb *= mix(uDarkTint, uTint, wht);
        diffuseColor.rgb = mix(diffuseColor.rgb, uEyeAlb, faceA);`)
      .replace('#include <roughnessmap_fragment>', `#include <roughnessmap_fragment>
        roughnessFactor = clamp(roughnessFactor * uRough.y + uRough.x, 0.02, 1.0);
        if (uVisorRough >= 0.0) roughnessFactor = mix(roughnessFactor, uVisorRough, smoothstep(0.4, 0.7, vFace.z));
        roughnessFactor = mix(roughnessFactor, 0.35, faceA);`)
      .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
        totalEmissiveRadiance *= uEmiCol * uEmiK * uRing;
        totalEmissiveRadiance += uEyeCol * faceA * uEyeK * uEyeGlow;`);
  };
  mat.customProgramCacheKey = () => 'sb-litrobot-' + (opts.key || 'x') + (opts.physical ? 'p' : 's');
  return mat;
}

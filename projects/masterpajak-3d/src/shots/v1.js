// VIDEO 1 — STEP 1A: floating 3D receipt (RESI). 7.0 s @ 60 fps, 1080x1080.
import * as THREE from 'three';
import { createReceipt } from '../lib/documents.js';
import { curl } from '../lib/PaperSheet.js';
import { EASE, track, spring, springTo, drift, envelope, remap, lerp, DEG } from '../lib/motion.js';

export const TIMING = {
  duration: 7.0,
  enter: [0.0, 1.5],      // entrance from lower depth plane
  turn: [0.05, 1.85],       // rotation lags position -> follow-through
  curlSettle: 0.95,        // page-curl spring starts relaxing
  floatIn: [1.7, 3.0],
  marker: [3.05, 3.6],     // PPN line highlight
  hero: [4.45, 6.25],      // rotate to near-front pose
  floatOut: [4.9, 6.6],
};

export function createShot(stage, quality) {
  const T = TIMING;
  const sheet = createReceipt(stage, quality);
  const rig = new THREE.Group();
  rig.rotation.order = 'YXZ';
  rig.add(sheet);
  stage.scene.add(rig);
  const cam = stage.camera;
  const regions = sheet.art.regions;

  // entrance path: from a low, deep plane, sweeping up and forward
  const path = new THREE.CatmullRomCurve3([
    new THREE.Vector3(0.55, -2.8, -3.4),
    new THREE.Vector3(0.22, -0.78, -1.05),
    new THREE.Vector3(0.04, -0.06, -0.12),
    new THREE.Vector3(0.0, 0.0, 0.0),
  ], false, 'centripetal');

  // rotation keys (deg): pitch(X), yaw(Y), roll(Z)
  const rotEnter = track([
    [T.turn[0], [-64, 30, -16]],
    [T.turn[1], [-5, -21, 2.6], EASE.glide],
  ]);
  const rotHero = track([
    [T.hero[0], [0, 0, 0]],
    [T.hero[1], [1.6, 12.5, -2.6], EASE.inOut], // delta applied on top -> ends near-front (-5.5 yaw)
  ]);

  const update = (t) => {
    // --- object position ---
    const u = EASE.arrive(remap(t, T.enter[0], T.enter[1]));
    const p = path.getPointAt(u);
    const fl = envelope(t, T.floatIn[0], T.floatIn[1]) * (1 - 0.82 * envelope(t, T.floatOut[0], T.floatOut[1]));
    const tail = 0.18 * envelope(t, T.floatOut[0], T.floatOut[1]); // keeps a breath of life in the hold
    const amp = fl + tail;
    rig.position.set(
      p.x + drift(t, 1.3, 0.010 * amp, 0.13),
      p.y + drift(t, 0.2, 0.028 * amp, 0.19),
      p.z + drift(t, 2.7, 0.018 * amp, 0.11),
    );

    // --- rotation: entrance turn + inertia wobble + float + hero settle ---
    const r = rotEnter(t);
    const h = rotHero(t);
    // yaw inertia: when the turn finishes, a damped spring adds a soft overshoot
    const wob = (1 - spring(t - 1.15, 0.9, 0.42)) * (t > 1.15 ? 1 : 0);
    const yawWob = -3.2 * wob * Math.sin(Math.min(1, (t - 1.15) * 3));
    rig.rotation.set(
      (r[0] + h[0] + drift(t, 4.1, 1.5 * amp, 0.16)) * DEG,
      (r[1] + h[1] + yawWob + drift(t, 5.3, 2.2 * amp, 0.12)) * DEG,
      (r[2] + h[2] + drift(t, 6.7, 0.7 * amp, 0.14)) * DEG,
    );

    // --- paper behaviour: air-drag curl during the rise, spring settle, slight lengthwise bow ---
    const curlAmt = -46 * (1 - springTo(t, T.curlSettle, 1.9, 1.05, 0.38)); // back-curl, overshoots forward
    const breathe = 2.2 * drift(t, 8.8, amp, 0.17);
    sheet.deform = {
      axis: [0.24, 0.97],
      anchor: -0.1,
      theta: (s) => curl(s, 0.26, 0.69, (curlAmt + breathe) * DEG),
      bowX: 0.13,
      bowY: 0.035,
    };
    sheet.update();

    // --- detail animation: yellow marker on the tax (PPN) line ---
    sheet.setRegions([
      { rect: regions.vat, mode: 'marker', progress: EASE.marker(remap(t, T.marker[0], T.marker[1])), strength: 0.92, tint: '#FFE14D' },
    ]);

    // --- camera: push in with the entrance, then a barely perceptible drift ---
    const push = EASE.arrive(remap(t, 0, 1.7));
    const slow = remap(t, 1.7, T.duration);
    const z = lerp(4.75, 4.22, push) - 0.12 * slow;
    cam.position.set(
      0.05 * (1 - push) + drift(t, 9.1, 0.018, 0.07),
      -0.12 * (1 - push) + drift(t, 3.3, 0.012, 0.06),
      z,
    );
    cam.lookAt(0, lerp(-0.18, 0.0, push), 0);
  };

  return { duration: T.duration, update };
}

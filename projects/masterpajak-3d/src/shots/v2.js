// VIDEO 2 — STEP 1B: floating 3D bank statement (REKENING KORAN). 7.0 s @ 60 fps, 1080x1080.
import * as THREE from 'three';
import { createStatement, createStatementPage2 } from '../lib/documents.js';
import { zFold } from '../lib/folds.js';
import { HIGHLIGHT_ROWS } from '../docs/statement.js';
import { DOC } from '../tokens.js';
import { EASE, track, springTo, drift, envelope, remap, lerp, DEG } from '../lib/motion.js';

export const TIMING = {
  duration: 7.0,
  arrive: [0.0, 1.5],
  unfold1: 0.95,     // first crease opens (spring)
  unfold2: 1.13,     // second crease follows
  page2Out: [1.85, 2.95],  // page 2 slides out from fully behind the opened sheet
  page2Tuck: [3.4, 5.4],
  rows: 2.55,        // first credit row lights; others follow
  rowGap: 0.42,
  orbit: [1.6, 6.4], // subtle camera orbit
  hero: [4.4, 6.3],
};

export function createShot(stage, quality) {
  const T = TIMING;
  const { h } = DOC.statement;
  const main = createStatement(stage, quality);
  const p2 = createStatementPage2(stage, quality);
  const rig = new THREE.Group();
  rig.rotation.order = 'YXZ';
  rig.add(main, p2);
  stage.scene.add(rig);
  const cam = stage.camera;
  const regions = main.art.regions;

  const path = new THREE.CatmullRomCurve3([
    new THREE.Vector3(2.55, 0.42, -2.6),
    new THREE.Vector3(1.1, 0.2, -0.9),
    new THREE.Vector3(0.18, 0.03, -0.12),
    new THREE.Vector3(0, 0, 0),
  ], false, 'centripetal');
  const rotArrive = track([
    [0.0, [9, -58, 7]],
    [1.6, [-4, -15, -1.5], EASE.glide],
  ]);
  const rotHero = track([
    [T.hero[0], [0, 0, 0]],
    [T.hero[1], [1.6, 11.0, 1.2], EASE.inOut],
  ]);
  // [x, y, z, rollDeg, scale]
  const p2Offset = track([
    [T.page2Out[0], [0, -0.01, -0.12, 0, 0.95]],
    [T.page2Out[1], [0.085, 0.06, -0.055, 3.2, 1], EASE.soft],
    [T.page2Tuck[0], [0.085, 0.06, -0.055, 3.2, 1]],
    [T.page2Tuck[1], [0.03, 0.026, -0.045, 1.4, 1], EASE.inOut],
  ]);

  const update = (t) => {
    // --- fold state (1 = folded, 0 = flat) with spring overshoot & crease memory ---
    const o1 = springTo(t, T.unfold1, 1.5, 1.15, 0.5);
    const o2 = springTo(t, T.unfold2, 1.5, 1.15, 0.5);
    const a1 = lerp(178, 7, o1) * DEG;   // residual 7deg: paper remembers its crease
    const a2 = lerp(178, 6, o2) * DEG;
    const theta = zFold(h, a1, a2);
    main.deform = { axis: [0, 1], anchor: h / 3, theta, bowX: 0.05, bowY: 0 };
    main.update();
    // page 2: flat, parked exactly behind the opened sheet (fully occluded) -> slides out
    p2.deform = { axis: [0, 1], anchor: h / 3, theta: zFold(h, 4 * DEG, 3 * DEG), bowX: 0.04 };
    p2.update();
    p2.visible = t >= T.page2Out[0] - 0.05;
    const po = p2Offset(t);
    p2.position.set(po[0], po[1], po[2]);
    p2.scale.setScalar(po[4]);
    p2.rotation.z = po[3] * DEG;

    // lock the sheet's visual mass centre on the rig origin: it unfolds around its own centre
    main.position.y = -main.centroid.y;
    const centreY = 0;

    // --- rig motion ---
    const u = EASE.arrive(remap(t, T.arrive[0], T.arrive[1]));
    const p = path.getPointAt(u);
    const fl = envelope(t, 1.9, 3.0) * (1 - 0.8 * envelope(t, 4.8, 6.6)) + 0.2 * envelope(t, 4.8, 6.6);
    rig.position.set(
      p.x + drift(t, 2.2, 0.01 * fl, 0.12),
      p.y - centreY + drift(t, 0.7, 0.024 * fl, 0.18),
      p.z + drift(t, 3.9, 0.016 * fl, 0.1),
    );
    const r = rotArrive(t);
    const hr = rotHero(t);
    rig.rotation.set(
      (r[0] + hr[0] + drift(t, 5.1, 1.3 * fl, 0.15)) * DEG,
      (r[1] + hr[1] + drift(t, 6.2, 1.8 * fl, 0.11)) * DEG,
      (r[2] + hr[2] + drift(t, 7.4, 0.6 * fl, 0.13)) * DEG,
    );

    // --- credit rows light up in sequence (restrained marker, navy ink stays crisp) ---
    main.setRegions(HIGHLIGHT_ROWS.map((ri, k) => ({
      rect: regions[`row${ri}`],
      mode: 'marker',
      progress: EASE.marker(remap(t, T.rows + k * T.rowGap, T.rows + k * T.rowGap + 0.5)),
      strength: 0.62,
      tint: '#FFE14D',
    })));

    // --- camera: approach + subtle orbit around the document ---
    const push = EASE.arrive(remap(t, 0, 1.8));
    const orb = EASE.inOut(remap(t, T.orbit[0], T.orbit[1]));
    const ang = lerp(9, -5, orb) * DEG;
    const dist = lerp(4.6, 4.02, push) - 0.1 * remap(t, 1.8, T.duration);
    const camY = lerp(0.1, 0.05, push) + drift(t, 8.3, 0.012, 0.06);
    cam.position.set(Math.sin(ang) * dist, camY, Math.cos(ang) * dist);
    cam.lookAt(0.0, lerp(0.12, 0.0, push), 0);
  };

  return { duration: T.duration, update };
}

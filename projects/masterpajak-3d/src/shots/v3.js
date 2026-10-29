// VIDEO 3 — STEP 2: receipt + bank statement -> financial report. 11.0 s @ 60 fps, 1080x1080.
//
// Story beats (all object-driven, no symbols):
//  1. RESI enters from the left, REKENING KORAN from the right, both through depth.
//  2. They begin to revolve around a shared centre: ~1 revolution with real acceleration,
//     a stable cruise and controlled deceleration (velocity-profile integrator).
//  3. Reconciliation: the receipt TOTAL and the matching statement debit line are marked,
//     and a yellow thread links them -> "the AI matched these".
//  4. Both documents fold into compact packets and slide into one stack.
//  5. The stack turns over; on its far side it is a folded report with a navy cover
//     (swap happens exactly edge-on, hidden by the motion blur and the thin profile).
//  6. The report unfolds (letter fold) -> LAPORAN KEUANGAN; data reveals; hero push-in; hold.
import * as THREE from 'three';
import { createReceipt, createStatement, createReport } from '../lib/documents.js';
import { zFold, letterFold } from '../lib/folds.js';
import { MATCH_ROW } from '../docs/statement.js';
import { DOC } from '../tokens.js';
import { EASE, track, smoothTrack, springTo, cruise, drift, envelope, remap, lerp, smoother, bezier, DEG } from '../lib/motion.js';

export const TIMING = {
  duration: 11.0,
  enter: [0.0, 1.55],
  orbit: [1.35, 5.6],          // one revolution
  marks: [5.7, 5.86],          // receipt TOTAL / statement debit markers start
  thread: [6.02, 6.5],         // connector draws
  threadOut: [6.62, 6.95],     // connector retracts into the statement line
  fold: [6.7, 7.3],            // both documents fold in place
  stack: [6.92, 7.78],         // slide together into one stack (overlaps the fold: one gesture)
  flip: [7.5, 8.26],           // stack turns over -> report cover
  unfoldTop: 8.22,             // report top panel opens (spring)
  unfoldBottom: 8.42,          // bottom panel follows
  reveal: 9.05,                // title marker, chart growth, profit marker
  hold: 10.25,
};

export function createShot(stage, quality) {
  const T = TIMING;
  const cam = stage.camera;
  const receipt = createReceipt(stage, quality);
  const statement = createStatement(stage, quality);
  const report = createReport(stage, quality);
  const rRig = new THREE.Group(); rRig.rotation.order = 'YXZ'; rRig.add(receipt);
  const sRig = new THREE.Group(); sRig.rotation.order = 'YXZ'; sRig.add(statement);
  const stack = new THREE.Group(); stack.add(rRig, sRig);
  const repRig = new THREE.Group(); repRig.rotation.order = 'YXZ'; repRig.add(report);
  const repPivot = new THREE.Group(); repPivot.add(repRig);
  stage.scene.add(stack, repPivot);

  // --- reconciliation thread ---
  const threadMat = new THREE.MeshStandardMaterial({ color: '#FED111', emissive: '#FED111', emissiveIntensity: 0.32, roughness: 0.38, metalness: 0 });
  const thread = new THREE.Mesh(new THREE.BufferGeometry(), threadMat);
  const dotGeo = new THREE.SphereGeometry(0.0105, 24, 16);
  const dotA = new THREE.Mesh(dotGeo, threadMat);
  const dotB = new THREE.Mesh(dotGeo, threadMat);
  stage.scene.add(thread, dotA, dotB);
  const SEG = 90, RAD = 8;

  const rReg = receipt.art.regions;
  const sReg = statement.art.regions;
  const pReg = report.art.regions;
  const hR = DOC.receipt.h, hS = DOC.statement.h, hP = DOC.report.h;

  // --- entrances ---
  const rPath = new THREE.CatmullRomCurve3([
    new THREE.Vector3(-2.75, -0.55, -2.7), new THREE.Vector3(-1.35, -0.16, -0.85),
    new THREE.Vector3(-0.62, -0.01, -0.08), new THREE.Vector3(-0.52, 0, 0),
  ], false, 'centripetal');
  const sPath = new THREE.CatmullRomCurve3([
    new THREE.Vector3(2.85, 0.5, -3.0), new THREE.Vector3(1.42, 0.16, -0.95),
    new THREE.Vector3(0.62, 0.01, -0.08), new THREE.Vector3(0.52, 0, 0),
  ], false, 'centripetal');
  const rRotIn = track([[0, [12, 58, -9]], [1.75, [-2, 9, 0.5], EASE.glide]]);
  const sRotIn = track([[0.12, [7, -60, 8]], [1.85, [-2, -9, -0.5], EASE.glide]]);

  // --- orbit ---
  const phi = cruise(T.orbit[0], T.orbit[1], Math.PI * 2, 0.32, 0.4);
  const omega = (t) => (phi(t + 0.004) - phi(t - 0.004)) / 0.008;
  const omegaMax = (Math.PI * 2) / ((T.orbit[1] - T.orbit[0]) * (1 - 0.36));
  const radius = track([[T.orbit[0], 0.52], [3.3, 0.62, EASE.inOut], [T.orbit[1], 0.47, EASE.inOut]]);

  // --- stacking ---
  const stackK = (t) => EASE.inOut(remap(t, T.stack[0], T.stack[1]));
  const flipEase = bezier(0.58, 0.0, 0.3, 1.0);
  // camera dolly: one continuous spline (no stop-start between beats)
  const dolly = smoothTrack([
    [0, 6.2], [1.6, 5.72], [3.4, 5.8], [5.5, 5.25], [6.5, 5.12],
    [7.85, 3.72], [8.3, 3.74], [9.25, 4.1], [11.0, 3.88],
  ]);

  const update = (t) => {
    // ===== orbit / entrance positions for both source documents =====
    const uR = EASE.arrive(remap(t, T.enter[0], T.enter[1] - 0.1));
    const uS = EASE.arrive(remap(t, T.enter[0] + 0.12, T.enter[1]));
    const pR = rPath.getPointAt(uR), pS = sPath.getPointAt(uS);
    const f = phi(t);
    const w = omega(t) / omegaMax;               // 0..~1 normalised angular speed
    const R = radius(t);
    const tilt = 15 * DEG * envelope(t, T.orbit[0] + 0.1, 2.7, 4.6, T.orbit[1]);
    const orbitPos = (ang) => {
      const x = R * Math.cos(ang), z = -R * Math.sin(ang);
      return new THREE.Vector3(x, -z * Math.sin(tilt), z * Math.cos(tilt));
    };
    const oS = orbitPos(f), oR = orbitPos(f + Math.PI);
    // orbit displacement is ADDED to the entrance path (which ends on the orbit) -> C1-continuous hand-off
    const posR = pR.clone().add(oR).add(new THREE.Vector3(0.52, 0, 0));
    const posS = pS.clone().add(oS).sub(new THREE.Vector3(0.52, 0, 0));

    // floats (layered, non-repeating), quieter while orbiting
    const fl = envelope(t, 1.0, 1.9) * (1 - 0.6 * envelope(t, 2.0, 2.8, 5.2, 5.8));
    const flR = fl * (1 - stackK(t));

    // ===== stacking: both folded packets slide to the centre, receipt in front =====
    const k = stackK(t);
    rRig.position.set(
      lerp(posR.x, -0.015, k) + drift(t, 1.1, 0.008 * flR, 0.14),
      lerp(posR.y, 0.0, k) + drift(t, 2.1, 0.022 * flR, 0.19),
      lerp(posR.z, 0.062, k),
    );
    sRig.position.set(
      lerp(posS.x, 0.0, k) + drift(t, 3.4, 0.008 * flR, 0.12),
      lerp(posS.y, 0.0, k) + drift(t, 4.6, 0.02 * flR, 0.17),
      lerp(posS.z, 0.0, k),
    );

    // orientation: entrance turn, then orbit-coupled yaw + banking (secondary motion)
    const rIn = rRotIn(t), sIn = sRotIn(t);
    const orbitYawR = -24 * Math.sin(f + Math.PI) * envelope(t, T.orbit[0], 2.4, 4.8, T.orbit[1]);
    const orbitYawS = -24 * Math.sin(f) * envelope(t, T.orbit[0], 2.4, 4.8, T.orbit[1]);
    const bankR = -5 * w * Math.cos(f + Math.PI);
    const bankS = -5 * w * Math.cos(f);
    const settle = EASE.glide(remap(t, T.orbit[1] - 0.4, T.fold[1]));
    rRig.rotation.set(
      (lerp(rIn[0], -1.5, settle) + drift(t, 5.2, 1.2 * flR, 0.15)) * DEG,
      (lerp(rIn[1] + orbitYawR, 4, settle) * (1 - k) + drift(t, 6.6, 1.6 * flR, 0.12)) * DEG,
      (lerp(rIn[2] + bankR, 0, settle) * (1 - k)) * DEG,
    );
    sRig.rotation.set(
      (lerp(sIn[0], -1.5, settle) + drift(t, 7.7, 1.1 * flR, 0.14)) * DEG,
      (lerp(sIn[1] + orbitYawS, -4, settle) * (1 - k) + drift(t, 8.1, 1.5 * flR, 0.11)) * DEG,
      (lerp(sIn[2] + bankS, 0, settle) * (1 - k)) * DEG,
    );

    // ===== paper behaviour: air flex during the orbit, then folding =====
    const foldR1 = EASE.inOut(remap(t, T.fold[0] + 0.04, T.fold[1] - 0.04));
    const foldR2 = EASE.inOut(remap(t, T.fold[0] + 0.12, T.fold[1]));
    const foldS1 = EASE.inOut(remap(t, T.fold[0], T.fold[1] - 0.08));
    const foldS2 = EASE.inOut(remap(t, T.fold[0] + 0.08, T.fold[1] - 0.02));
    const flex = 6 * w * DEG;
    receipt.deform = {
      axis: [0, 1], anchor: hR / 3,
      theta: zFold(hR, lerp(2 * DEG + flex, 178 * DEG, foldR1), lerp(1.5 * DEG, 178 * DEG, foldR2)),
      bowX: 0.11 * (1 - foldR1), bowY: 0.02 * (1 - foldR1),
    };
    receipt.update();
    statement.deform = {
      axis: [0, 1], anchor: hS / 3,
      theta: zFold(hS, lerp(7 * DEG + flex, 178 * DEG, foldS1), lerp(6 * DEG, 178 * DEG, foldS2)),
      bowX: 0.05 * (1 - foldS1),
    };
    statement.update();
    // each document folds around its own visual mass centre (no competing translations)
    receipt.position.x = -receipt.centroid.x; receipt.position.y = -receipt.centroid.y;
    statement.position.x = -statement.centroid.x; statement.position.y = -statement.centroid.y;

    // ===== reconciliation markers =====
    receipt.setRegions([{ rect: rReg.total, mode: 'marker', progress: EASE.marker(remap(t, T.marks[0], T.marks[0] + 0.42)), strength: 0.9, tint: '#FFE14D' }]);
    statement.setRegions([{ rect: sReg[`row${MATCH_ROW}`], mode: 'marker', progress: EASE.marker(remap(t, T.marks[1], T.marks[1] + 0.42)), strength: 0.75, tint: '#FFE14D' }]);

    // ===== flip: the stack turns over, the report takes its place edge-on =====
    const fp = flipEase(remap(t, T.flip[0], T.flip[1]));
    const alpha = Math.PI * fp;
    const lift = Math.sin(Math.PI * fp);
    stack.rotation.set(0.06 * lift, alpha, 0);
    stack.position.set(0, 0.03 * lift, 0.16 * lift);
    repPivot.rotation.set(0.06 * lift, alpha - Math.PI, 0);
    repPivot.position.copy(stack.position);
    const swapped = alpha >= Math.PI / 2;
    stack.visible = !swapped;
    repPivot.visible = swapped;

    // ===== report: letter fold opens with spring; content reveals =====
    const o1 = springTo(t, T.unfoldTop, 1.25, 1.05, 0.52);
    const o3 = springTo(t, T.unfoldBottom, 1.25, 1.1, 0.55);
    report.deform = {
      axis: [0, 1], anchor: 0,
      theta: letterFold(hP, lerp(178, 5, o1) * DEG, lerp(178, 4, o3) * DEG),
      bowX: 0.04 * smoother(remap(t, 8.6, 9.6)),
    };
    report.update();
    report.position.set(-report.centroid.x, -report.centroid.y, 0.012);
    const rv = T.reveal;
    report.setRegions([
      { rect: pReg.titleMarker, mode: 'marker', progress: EASE.marker(remap(t, rv, rv + 0.5)), strength: 0.95, tint: '#FFE14D' },
      ...[0, 1, 2].map((i) => ({ rect: pReg[`col${i}`], mode: 'grow', progress: EASE.soft(remap(t, rv + 0.12 + i * 0.13, rv + 0.72 + i * 0.13)), strength: 1, tint: '#FFFFFF' })),
      { rect: pReg.profitMarker, mode: 'marker', progress: EASE.marker(remap(t, rv + 0.55, rv + 1.05)), strength: 0.9, tint: '#FFE14D' },
    ]);
    // report hero pose: settles from the flip into a gentle 3/4 then near-front
    const repFloat = envelope(t, 8.9, 9.8) * (1 - 0.75 * envelope(t, 9.9, T.hold + 0.4));
    const heroK = EASE.inOut(remap(t, 8.6, T.hold));
    repRig.rotation.set(
      (lerp(0, -2.5, heroK) + drift(t, 9.3, 1.0 * repFloat, 0.15)) * DEG,
      (lerp(0, -7, heroK) + drift(t, 10.2, 1.4 * repFloat, 0.12)) * DEG,
      drift(t, 11.4, 0.4 * repFloat, 0.13) * DEG,
    );
    repRig.position.set(0, drift(t, 12.6, 0.02 * repFloat, 0.18), 0);

    // ===== thread between the matched lines =====
    const grow = EASE.soft(remap(t, T.thread[0], T.thread[1]));
    const shrink = EASE.inOut(remap(t, T.threadOut[0], T.threadOut[1]));
    const showThread = grow > 0.001 && shrink < 0.999 && !swapped;
    thread.visible = showThread;
    dotA.visible = dotB.visible = showThread;
    if (showThread) {
      stage.scene.updateMatrixWorld(true);
      const tr = rReg.total, sr = sReg[`row${MATCH_ROW}`];
      const a = receipt.surfacePoint(0.995, (tr[1] + tr[3]) / 2);   // leaves from the receipt's edge
      const b = statement.surfacePoint(0.005, (sr[1] + sr[3]) / 2); // lands on the statement's edge
      a.z += 0.008; b.z += 0.008;
      const curve = new THREE.CubicBezierCurve3(a, a.clone().add(new THREE.Vector3(0.16, 0.05, 0.24)), b.clone().add(new THREE.Vector3(-0.16, 0.05, 0.24)), b);
      thread.geometry.dispose();
      thread.geometry = new THREE.TubeGeometry(curve, SEG, 0.0046, RAD, false);
      const per = RAD * 6;
      const s0 = Math.floor(shrink * SEG), s1 = Math.ceil(grow * SEG);
      thread.geometry.setDrawRange(s0 * per, Math.max(0, s1 - s0) * per);
      dotA.position.copy(a); dotB.position.copy(b);
      dotA.scale.setScalar(smoother(remap(t, T.thread[0] - 0.05, T.thread[0] + 0.15)) * (1 - smoother(remap(t, T.threadOut[0], T.threadOut[0] + 0.15))));
      dotB.scale.setScalar(smoother(remap(t, T.thread[1] - 0.12, T.thread[1] + 0.05)) * (1 - smoother(remap(t, T.threadOut[1] - 0.1, T.threadOut[1]))));
    }

    // ===== camera =====
    const orbK = EASE.inOut(remap(t, T.orbit[0], T.orbit[1]));
    const dist = dolly(t);
    const elev = 0.5 * envelope(t, 1.5, 3.4, 4.2, 5.8);
    const camYaw = (lerp(-4, 4, orbK) * (1 - EASE.inOut(remap(t, 5.4, 7.4)))) * DEG;
    cam.position.set(Math.sin(camYaw) * dist + drift(t, 13.1, 0.015, 0.07), elev + drift(t, 14.2, 0.012, 0.06), Math.cos(camYaw) * dist);
    cam.lookAt(0, elev * 0.25, 0);
  };

  return { duration: T.duration, update };
}

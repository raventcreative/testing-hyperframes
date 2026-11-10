// Procedural "creator's office" set (simple readable geometry): floor, back wall with a window (sky + skyline outside),
// a desk with a monitor whose screen shows a bar chart, a standing chart board with 4 bars, a snake plant, a wall clock.
// Every part carries a palette index (aPal) so each style recolours / re-renders the whole set from one geometry.
import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/examples/jsm/geometries/RoundedBoxGeometry.js';
import { mergeGeometries } from 'three/examples/jsm/utils/BufferGeometryUtils.js';

export const PAL = {
  floor: 0, wall: 1, trim: 2, deskTop: 3, deskBody: 4, monitor: 5, screen: 6, bar1: 7, bar2: 8, bar3: 9, bar4: 10,
  board: 11, boardFrame: 12, leaf: 13, pot: 14, winFrame: 15, sky: 16, city: 17, clock: 18, clockHand: 19, keyboard: 20, mug: 21,
  axis: 22, soil: 23,
};
export const NPAL = 24;

// layout (world units; robot = 0.9 tall, standing at the origin, facing +z)
export const LAYOUT = {
  wallZ: -1.3,
  win: { x0: -1.25, x1: -0.35, y0: 1.0, y1: 1.72 },
  desk: { x: -1.0, z: -0.78, w: 1.05, d: 0.5, h: 0.6 },
  board: { x: 0.92, z: -0.72, w: 0.64, h: 0.5, y0: 0.86 },
  plant: { x: 0.78, z: 0.42 },
  clock: { x: 0.25, y: 1.8 },
};

export function buildSet({ round = 0 } = {}) {
  const parts = [];
  const box = (w, h, d, r = round) => (r > 0 ? new RoundedBoxGeometry(w, h, d, 3, Math.min(r, w / 2.01, h / 2.01, d / 2.01)) : new THREE.BoxGeometry(w, h, d));
  const add = (geo, pal, p = [0, 0, 0], rot = [0, 0, 0], s) => {
    const g = geo.index ? geo.toNonIndexed() : geo;
    if (!g.attributes.uv) g.setAttribute('uv', new THREE.Float32BufferAttribute(new Float32Array(g.attributes.position.count * 2), 2));
    const m = new THREE.Matrix4().compose(new THREE.Vector3(...p), new THREE.Quaternion().setFromEuler(new THREE.Euler(...rot)), new THREE.Vector3(...(s || [1, 1, 1])));
    g.applyMatrix4(m);
    g.setAttribute('aPal', new THREE.Float32BufferAttribute(new Float32Array(g.attributes.position.count).fill(pal), 1));
    for (const k of Object.keys(g.attributes)) if (!['position', 'normal', 'uv', 'aPal'].includes(k)) g.deleteAttribute(k);
    parts.push(g);
  };
  const L = LAYOUT, WZ = L.wallZ, W = L.win;
  // floor + back wall with a window hole
  add(new THREE.PlaneGeometry(9, 7), PAL.floor, [0, 0, 0.6], [-Math.PI / 2, 0, 0]);
  const wall = (x0, x1, y0, y1) => add(new THREE.PlaneGeometry(x1 - x0, y1 - y0), PAL.wall, [(x0 + x1) / 2, (y0 + y1) / 2, WZ]);
  wall(-4.5, W.x0, 0, 3.4); wall(W.x1, 4.5, 0, 3.4); wall(W.x0, W.x1, 0, W.y0); wall(W.x0, W.x1, W.y1, 3.4);
  add(box(9, 0.07, 0.025, 0), PAL.trim, [0, 0.035, WZ + 0.012]);
  // window: frame, mullions, sill, sky + skyline outside
  const fw = 0.05, fd = 0.07, cx = (W.x0 + W.x1) / 2, cy = (W.y0 + W.y1) / 2, ww = W.x1 - W.x0, wh = W.y1 - W.y0;
  add(box(ww + 2 * fw, fw, fd), PAL.winFrame, [cx, W.y1 + fw / 2, WZ]);
  add(box(ww + 2 * fw, fw, fd), PAL.winFrame, [cx, W.y0 - fw / 2, WZ]);
  add(box(fw, wh, fd), PAL.winFrame, [W.x0 - fw / 2, cy, WZ]);
  add(box(fw, wh, fd), PAL.winFrame, [W.x1 + fw / 2, cy, WZ]);
  add(box(0.025, wh, 0.04), PAL.winFrame, [cx, cy, WZ]);
  add(box(ww, 0.025, 0.04), PAL.winFrame, [cx, cy, WZ]);
  add(box(ww + 0.2, 0.03, 0.13), PAL.winFrame, [cx, W.y0 - fw - 0.012, WZ + 0.05]);
  add(new THREE.PlaneGeometry(6, 3.2), PAL.sky, [cx, 1.4, WZ - 1.6]);
  const city = [[-0.42, 0.34, 0.16], [-0.25, 0.52, 0.12], [-0.1, 0.28, 0.14], [0.06, 0.62, 0.15], [0.22, 0.4, 0.13], [0.36, 0.5, 0.12], [-0.55, 0.45, 0.13], [0.5, 0.3, 0.15]];
  for (const [dx, h, w] of city) add(box(w, h, 0.1, 0), PAL.city, [cx + dx * 1.6, W.y0 - 0.12 + h / 2, WZ - 1.1]);
  // desk (left, behind the robot) + monitor with a bar chart + keyboard + mug
  const D = L.desk, top = D.h;
  add(box(D.w, 0.045, D.d), PAL.deskTop, [D.x, top - 0.022, D.z]);
  add(box(0.04, top - 0.045, D.d - 0.04), PAL.deskBody, [D.x - D.w / 2 + 0.05, (top - 0.045) / 2, D.z]);
  add(box(0.3, top - 0.045, D.d - 0.04), PAL.deskBody, [D.x + D.w / 2 - 0.18, (top - 0.045) / 2, D.z]);
  for (let i = 0; i < 3; i++) add(box(0.24, 0.008, 0.01, 0), PAL.trim, [D.x + D.w / 2 - 0.18, 0.12 + i * 0.17, D.z + D.d / 2 - 0.015]);
  const mx = D.x + 0.02, mz = D.z - 0.06, sw = 0.52, sh = 0.32, my = top + 0.07 + sh / 2;
  add(box(0.18, 0.015, 0.11), PAL.monitor, [mx, top + 0.008, mz]);
  add(box(0.04, 0.09, 0.025), PAL.monitor, [mx, top + 0.05, mz - 0.01]);
  add(box(sw, sh, 0.028), PAL.monitor, [mx, my, mz]);
  add(new THREE.PlaneGeometry(sw - 0.04, sh - 0.04), PAL.screen, [mx, my, mz + 0.0145]);
  const sbars = [0.3, 0.52, 0.42, 0.8], spal = [PAL.bar1, PAL.bar2, PAL.bar3, PAL.bar4];
  for (let i = 0; i < 4; i++) { const h = sbars[i] * (sh - 0.1); add(box(0.06, h, 0.004, 0), spal[i], [mx - 0.15 + i * 0.1, my - (sh - 0.1) / 2 + h / 2 - 0.01, mz + 0.017]); }
  add(box(0.4, 0.004, 0.004, 0), PAL.axis, [mx, my - (sh - 0.1) / 2 - 0.012, mz + 0.017]);
  add(box(0.36, 0.018, 0.12), PAL.keyboard, [mx + 0.02, top + 0.01, D.z + 0.13]);
  add(new THREE.CylinderGeometry(0.035, 0.032, 0.09, 16), PAL.mug, [D.x + D.w / 2 - 0.12, top + 0.045, D.z + 0.08]);
  // standing chart board (right): board + frame + legs + 4 rising bars + axes
  const B = L.board, by = B.y0 + B.h / 2;
  add(box(B.w, B.h, 0.025), PAL.board, [B.x, by, B.z]);
  add(box(B.w + 0.05, 0.03, 0.04), PAL.boardFrame, [B.x, B.y0 + B.h + 0.012, B.z]);
  add(box(B.w + 0.05, 0.03, 0.04), PAL.boardFrame, [B.x, B.y0 - 0.012, B.z]);
  add(box(0.03, B.h + 0.05, 0.04), PAL.boardFrame, [B.x - B.w / 2 - 0.012, by, B.z]);
  add(box(0.03, B.h + 0.05, 0.04), PAL.boardFrame, [B.x + B.w / 2 + 0.012, by, B.z]);
  for (const sx of [-1, 1]) {
    add(box(0.03, B.y0, 0.03), PAL.boardFrame, [B.x + sx * (B.w / 2 - 0.06), B.y0 / 2, B.z - 0.02]);
    add(box(0.05, 0.02, 0.3), PAL.boardFrame, [B.x + sx * (B.w / 2 - 0.06), 0.01, B.z - 0.02]);
  }
  add(box(0.02, B.y0 * 0.9, 0.02), PAL.boardFrame, [B.x, B.y0 * 0.55, B.z - 0.2], [-0.35, 0, 0]);
  const bh = [0.13, 0.2, 0.27, 0.36], bx0 = B.x - B.w / 2 + 0.14, base = B.y0 + 0.06;
  for (let i = 0; i < 4; i++) add(box(0.075, bh[i], 0.012, 0), spal[i], [bx0 + i * 0.12, base + bh[i] / 2, B.z + 0.018]);
  add(box(B.w - 0.12, 0.008, 0.01, 0), PAL.axis, [B.x + 0.02, base - 0.004, B.z + 0.016]);
  add(box(0.008, B.h - 0.1, 0.01, 0), PAL.axis, [B.x - B.w / 2 + 0.07, B.y0 + B.h / 2, B.z + 0.016]);
  // trend arrow over the bars
  const pts = [[bx0 - 0.03, base + 0.16], [bx0 + 0.12, base + 0.22], [bx0 + 0.24, base + 0.26], [bx0 + 0.38, base + 0.39]];
  for (let i = 0; i < 3; i++) {
    const [x0, y0] = pts[i], [x1, y1] = pts[i + 1], len = Math.hypot(x1 - x0, y1 - y0);
    add(box(len + 0.01, 0.012, 0.008, 0), PAL.axis, [(x0 + x1) / 2, (y0 + y1) / 2, B.z + 0.03], [0, 0, Math.atan2(y1 - y0, x1 - x0)]);
  }
  add(new THREE.ConeGeometry(0.025, 0.05, 3), PAL.axis, [pts[3][0] + 0.01, pts[3][1] + 0.012, B.z + 0.03], [0, 0, -0.72]);
  // snake plant in a pot (front right)
  const Pl = L.plant;
  add(new THREE.CylinderGeometry(0.12, 0.09, 0.24, 24), PAL.pot, [Pl.x, 0.12, Pl.z]);
  add(new THREE.CylinderGeometry(0.128, 0.128, 0.035, 24), PAL.pot, [Pl.x, 0.24, Pl.z]);
  add(new THREE.CylinderGeometry(0.11, 0.11, 0.01, 24), PAL.soil, [Pl.x, 0.252, Pl.z]);
  const leaves = [[0, 0.62, 0.0, 0.05], [1.1, 0.5, 0.22, 0.045], [2.3, 0.56, 0.18, 0.05], [3.4, 0.44, 0.28, 0.042], [4.5, 0.52, 0.2, 0.048], [5.5, 0.4, 0.3, 0.04], [0.55, 0.36, 0.34, 0.038]];
  for (const [a, h, tilt, w] of leaves) {
    const g = new THREE.CylinderGeometry(0.0, w, h, 6, 4); g.scale(1, 1, 0.28); g.translate(0, h / 2, 0);
    add(g, PAL.leaf, [Pl.x + Math.cos(a) * 0.03, 0.25, Pl.z + Math.sin(a) * 0.03], [Math.sin(a) * tilt, -a, Math.cos(a) * tilt]);
  }
  // wall clock
  const C = L.clock;
  add(new THREE.CylinderGeometry(0.13, 0.13, 0.035, 32), PAL.clock, [C.x, C.y, WZ + 0.02], [Math.PI / 2, 0, 0]);
  add(new THREE.CylinderGeometry(0.112, 0.112, 0.01, 32), PAL.board, [C.x, C.y, WZ + 0.04], [Math.PI / 2, 0, 0]);
  add(box(0.012, 0.085, 0.006, 0), PAL.clockHand, [C.x, C.y + 0.035, WZ + 0.048]);
  add(box(0.06, 0.012, 0.006, 0), PAL.clockHand, [C.x + 0.026, C.y, WZ + 0.048]);
  const geo = mergeGeometries(parts, false);
  geo.computeBoundingSphere();
  return geo;
}

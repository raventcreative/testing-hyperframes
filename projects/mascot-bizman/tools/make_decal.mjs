// Chest logo decal: samples the front jacket surface z on a grid (rest pose) for a box, writes decals.json.
// Usage: node make_decal.mjs <work dir> <logo url (as the page sees it)> <x0> <x1> <yc> <aspect w/h> <out.json>
import fs from 'fs';
const [dir, url, X0, X1, YC, ASP, out] = process.argv.slice(2);
const P = new Float32Array(fs.readFileSync(`${dir}/biz_pos.f32`).buffer.slice(0));
const I = new Uint32Array(fs.readFileSync(`${dir}/biz_idx.u32`).buffer.slice(0));
const x0 = +X0, x1 = +X1, yc = +YC, h = (x1 - x0) / +ASP, y0 = yc - h / 2, y1 = yc + h / 2;
// triangles near the box, front-facing region only
const tris = [];
for (let t = 0; t < I.length; t += 3) {
  const a = I[t], b = I[t + 1], c = I[t + 2];
  const xs = [P[3*a], P[3*b], P[3*c]], ys = [P[3*a+1], P[3*b+1], P[3*c+1]], zs = [P[3*a+2], P[3*b+2], P[3*c+2]];
  if (Math.max(...xs) < x0 - 0.01 || Math.min(...xs) > x1 + 0.01 || Math.max(...ys) < y0 - 0.01 || Math.min(...ys) > y1 + 0.01 || Math.min(...zs) < 0.02) continue;
  tris.push([a, b, c]);
}
function zAt(x, y) {
  let best = -9;
  for (const [a, b, c] of tris) {
    const ax = P[3*a], ay = P[3*a+1], bx = P[3*b], by = P[3*b+1], cx = P[3*c], cy = P[3*c+1];
    const den = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy); if (Math.abs(den) < 1e-14) continue;
    const l1 = ((by - cy) * (x - cx) + (cx - bx) * (y - cy)) / den, l2 = ((cy - ay) * (x - cx) + (ax - cx) * (y - cy)) / den, l3 = 1 - l1 - l2;
    if (l1 < -1e-6 || l2 < -1e-6 || l3 < -1e-6) continue;
    const z = l1 * P[3*a+2] + l2 * P[3*b+2] + l3 * P[3*c+2]; if (z > best) best = z;
  }
  return best;
}
const nx = 56, ny = 9, Z = [];
for (let j = 0; j < ny; j++) { const row = []; for (let i = 0; i < nx; i++) row.push(+zAt(x0 + (x1 - x0) * i / (nx - 1), y1 - (y1 - y0) * j / (ny - 1)).toFixed(5)); Z.push(row); }
// exact front surface (no smoothing: averaging a curved surface sinks the print into the cloth at the sides)
const Zs = Z;
const dec = [{ url, bone: 'chest', box: [x0, x1, +y0.toFixed(5), +y1.toFixed(5)], zgrid: Zs, offset: 0.0011, emissive: 0.55, roughness: 0.6, skinned: true }];
fs.writeFileSync(out, JSON.stringify(dec));
console.log('box', dec[0].box, 'z range', Math.min(...Zs.flat()), Math.max(...Zs.flat()));

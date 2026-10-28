// Least-squares local UV Jacobian around each eye / brow on the face-mask islands (for gaze + brow shifts).
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import fs from 'fs';
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS);
const doc = await io.read(process.argv[2]);
const prim = doc.getRoot().listMeshes()[0].listPrimitives()[0];
const P = prim.getAttribute('POSITION').getArray(), UV = prim.getAttribute('TEXCOORD_0').getArray(), FM = prim.getAttribute('_FACEMASK').getArray();
function fit(cx, cy, r) {
  const rows = [];
  for (let v = 0; v < FM.length; v++) if (FM[v] > 0.5) { const dx = P[3*v]-cx, dy = P[3*v+1]-cy; if (dx*dx+dy*dy < r*r) rows.push([dx, dy, UV[2*v], UV[2*v+1]]); }
  // keep the dominant UV chart only (eye / brow regions can straddle an atlas seam)
  { const us = rows.map(r => r[2]).sort((a,b)=>a-b), vs = rows.map(r => r[3]).sort((a,b)=>a-b);
    const mu = us[us.length >> 1], mv = vs[vs.length >> 1];
    for (let i = rows.length - 1; i >= 0; i--) if (Math.hypot(rows[i][2] - mu, rows[i][3] - mv) > 0.06) rows.splice(i, 1); }
  // solve [dx dy 1] * M = [u v]
  const A = [[0,0,0],[0,0,0],[0,0,0]], bu = [0,0,0], bv = [0,0,0];
  for (const [x,y,u,v] of rows) { const r_ = [x,y,1]; for (let i=0;i<3;i++){ for(let j=0;j<3;j++) A[i][j]+=r_[i]*r_[j]; bu[i]+=r_[i]*u; bv[i]+=r_[i]*v; } }
  const solve = (A,b)=>{ const m=A.map((r,i)=>[...r,b[i]]); for(let i=0;i<3;i++){ let p=i; for(let k=i+1;k<3;k++) if(Math.abs(m[k][i])>Math.abs(m[p][i])) p=k; [m[i],m[p]]=[m[p],m[i]]; for(let k=0;k<3;k++) if(k!==i){ const f=m[k][i]/m[i][i]; for(let j=i;j<4;j++) m[k][j]-=f*m[i][j]; } } return m.map((r,i)=>r[3]/r[i]); };
  const cu = solve(A,bu), cv = solve(A,bv);
  let err = 0; for (const [x,y,u,v] of rows) err = Math.max(err, Math.hypot(cu[0]*x+cu[1]*y+cu[2]-u, cv[0]*x+cv[1]*y+cv[2]-v));
  return { n: rows.length, J: [cu[0], cu[1], cv[0], cv[1]], uv0: [cu[2], cv[2]], maxErr: err };
}
const cfg = {
  eyeA: { c: [-0.092, 0.61], r: [0.046, 0.043], ...fit(-0.092, 0.61, 0.05) },  // screen-left eye (character's right)
  eyeB: { c: [0.09, 0.61], r: [0.046, 0.043], ...fit(0.09, 0.61, 0.05) },   // screen-right eye (character's left)
  browA: { c: [-0.1, 0.685], ...fit(-0.1, 0.675, 0.035) },
  browB: { c: [0.1, 0.685], ...fit(0.1, 0.675, 0.035) },
  mouth: { c: [0.0, 0.549], r: [0.026, 0.016] },
  skin: [243, 207, 186], skinEye: [246, 214, 195],
};
console.log(JSON.stringify(cfg, null, 1));
fs.writeFileSync(process.argv[3], JSON.stringify(cfg, null, 1));

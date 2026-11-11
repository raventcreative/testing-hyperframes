"""Remove the fused arms + hands from the Tripo robot and patch the body where they were attached.
Inputs: rt_pos.f32 rt_uv.f32 rt_idx.u32 vcol.npy   Outputs: cut_pos.f32 cut_uv.f32 cut_idx.u32 cut_nrm.f32 + cut_info.json"""
import json, numpy as np
P = np.fromfile('rt_pos.f32', np.float32).reshape(-1,3).astype(np.float64); UV = np.fromfile('rt_uv.f32', np.float32).reshape(-1,2)
I = np.fromfile('rt_idx.u32', np.uint32).reshape(-1,3).astype(np.int64); C = np.load('vcol.npy')
RA = 0.047; SH = np.array([0.267, 0.358, 0.033]); WR = np.array([0.272, 0.152, 0.042]); HC = np.array([0.279, 0.111, 0.062]); RH = 0.046
def seg_d(p, a, b):
    ab = b - a; t = np.clip(((p - a) @ ab) / (ab @ ab), 0, 1); return np.linalg.norm(p - (a + t[:, None] * ab), axis=1)
arm = np.zeros(len(P), bool)
for sg in (1, -1):
    m = np.array([sg, 1, 1])
    q = P * m   # mirror right side onto left
    d = seg_d(q, SH, WR); dh = np.linalg.norm(q - HC, axis=1)
    arm |= ((d < RA + 0.016) & (q[:,0] > 0.212)) | (dh < RH + 0.018)
print('arm verts', arm.sum())
# drop triangles touching an arm vertex
keep = ~arm[I].any(1); I2 = I[keep]; print('tris', len(I), '->', len(I2))
_k = np.round(P * 1e5).astype(np.int64); _, _c = np.unique(_k, axis=0, return_inverse=True); _c = _c.ravel()
par = np.arange(_c.max() + 1)
def fr(x):
    r = x
    while par[r] != r: r = par[r]
    while par[x] != r: par[x], x = r, par[x]
    return r
for a, b, c in _c[I2]:
    ra = fr(a); par[fr(b)] = ra; par[fr(c)] = ra
roots = np.array([fr(x) for x in range(len(par))]); tri_root = roots[_c[I2[:, 0]]]
u, cnt = np.unique(tri_root, return_counts=True); big = u[np.argmax(cnt)]
print('islands', len(u), 'dropped tris', (tri_root != big).sum()); I2 = I2[tri_root == big]
# weld by position to find the true boundary (UV seams duplicate vertices)
key = np.round(P * 1e5).astype(np.int64); _, canon_of = np.unique(key, axis=0, return_inverse=True); canon_of = canon_of.ravel()
rep = np.zeros(canon_of.max() + 1, np.int64); rep[canon_of] = np.arange(len(P))   # one representative vertex per welded point
E = np.concatenate([I2[:, [0, 1]], I2[:, [1, 2]], I2[:, [2, 0]]]); Ec = canon_of[E]
Es = np.sort(Ec, 1); _, inv, cnt = np.unique(Es, axis=0, return_inverse=True, return_counts=True); inv = inv.ravel()
bnd = Ec[cnt[inv] == 1]   # directed boundary edges (orientation of the remaining triangle)
print('boundary edges', len(bnd))
nxt = {}
for a, b in bnd: nxt.setdefault(a, []).append(b)
loops, seen = [], set()
for a0 in list(nxt):
    if a0 in seen: continue
    loop = [a0]; seen.add(a0); a = a0
    for _ in range(100000):
        bs = [b for b in nxt.get(a, []) if b not in seen or b == a0]
        if not bs: break
        b = bs[0]
        if b == a0: break
        loop.append(b); seen.add(b); a = b
    loops.append(loop)
loops = [l for l in loops if len(l) >= 3]
print('loops', [(len(l), P[rep[l]].mean(0).round(3).tolist()) for l in loops])
newP, newUV, newT = [], [], []
nv = len(P)
# a navy body texel for the patch (median body uv of navy back verts)
navy = (np.abs(P[:,0]) < 0.08) & (P[:,1] < 0.35) & (P[:,1] > 0.15) & (P[:,2] < -0.12)
uv_navy = np.median(UV[navy], 0)
for l in loops:
    pts = P[rep[l]]; c = pts.mean(0)
    if abs(c[0]) < 0.12 or c[1] > 0.47: continue   # only the side patches
    # Newell normal; orient outward (away from body axis)
    n = np.zeros(3)
    for i in range(len(pts)): a, b = pts[i], pts[(i + 1) % len(pts)]; n += np.cross(a, b)
    n /= np.linalg.norm(n)
    out = np.array([np.sign(c[0]), 0, 0.0])
    # concentric rings toward the centre, bulged outward a little so the patch follows the rounded wall
    R = 4; ring_prev = []
    for k in l:   # duplicate the rim with the navy UV so no patch triangle interpolates across texture islands
        ring_prev.append(nv); newP.append(P[rep[k]]); newUV.append(uv_navy); nv += 1
    for r in range(1, R + 1):
        s = 1 - r / (R + 0.0001) if r < R else 0
        if r == R:
            cen = c + out * 0.010
            ci = nv; newP.append(cen); newUV.append(uv_navy); nv += 1
            for i in range(len(ring_prev)): newT.append([ring_prev[i], ring_prev[(i + 1) % len(ring_prev)], ci])
            break
        ring = []
        for i, k in enumerate(l):
            p = c + (P[rep[k]] - c) * s + out * 0.010 * (1 - s * s)
            ring.append(nv); newP.append(p); newUV.append(uv_navy); nv += 1
        for i in range(len(l)):
            a, b, a2, b2 = ring_prev[i], ring_prev[(i + 1) % len(l)], ring[i], ring[(i + 1) % len(l)]
            newT.append([a, b, b2]); newT.append([a, b2, a2])
        ring_prev = ring
newT = np.array(newT, np.int64)
# orientation: boundary edges a->b belong to the kept triangle; the patch must use b->a. Ring triangles above use a->b, so flip them.
newT = newT[:, [0, 2, 1]]
P3 = np.vstack([P, np.array(newP)]); UV3 = np.vstack([UV, np.array(newUV, np.float32)]); I3 = np.vstack([I2, newT])
# drop now-unreferenced vertices
used = np.zeros(len(P3), bool); used[I3.ravel()] = True; remap = -np.ones(len(P3), np.int64); remap[used] = np.arange(used.sum())
P4 = P3[used]; UV4 = UV3[used]; I4 = remap[I3]
# ---- SIDE REBUILD: the torso wall where the arms were fused is re-shaped onto the torso's own rounded profile
# (outer-wall radius per height x angle, measured away from the arms, interpolated across the arm zone, smoothed), so
# the old junction (stitched, wrinkled) disappears. _SIDE = band weight: the shader paints that band plain navy and
# drops the normal map there, so no baked white streaks / wrinkles survive.
P0 = np.fromfile('rt_pos.f32', np.float32).reshape(-1,3).astype(np.float64)
armBig = np.zeros(len(P0), bool)
for sg in (1, -1):
    q = P0 * np.array([sg, 1, 1]); armBig |= ((seg_d(q, SH, WR) < RA + 0.03) & (q[:,0] > 0.19)) | (np.linalg.norm(q - HC, axis=1) < RH + 0.03)
tor = (~armBig) & (P0[:,1] < 0.44)
r0 = np.hypot(P0[:,0], P0[:,2]); t0 = np.degrees(np.arctan2(np.abs(P0[:,0]), P0[:,2]))
YB = np.arange(0.0, 0.445, 0.01); TB = np.arange(0, 181, 5.0)
prof = np.full((len(YB), len(TB)), np.nan)
for i, y in enumerate(YB):
    m = tor & (np.abs(P0[:,1] - y) < 0.007)
    for j, t in enumerate(TB):
        mm = m & (np.abs(t0 - t) < 4.0)
        if mm.sum() >= 3: prof[i, j] = np.percentile(r0[mm], 90)
    row = prof[i]; ok = ~np.isnan(row)
    if ok.sum() >= 2: prof[i] = np.interp(TB, TB[ok], row[ok])
from math import exp
def gsmooth(a, s, axis):
    k = np.array([exp(-0.5 * (d / s) ** 2) for d in range(-3, 4)]); k /= k.sum()
    pad = np.pad(a, [(3, 3) if ax == axis else (0, 0) for ax in range(a.ndim)], mode='edge')
    out = np.zeros_like(a)
    for d in range(7):
        sl = [slice(None)] * a.ndim; sl[axis] = slice(d, d + a.shape[axis]); out += k[d] * pad[tuple(sl)]
    return out
prof = gsmooth(gsmooth(prof, 1.6, 0), 1.2, 1)
def prof_at(y, t):
    fy = np.clip(y / 0.01, 0, len(YB) - 1.001); iy = fy.astype(int); wy = fy - iy
    ft = np.clip(t / 5.0, 0, len(TB) - 1.001); it = ft.astype(int); wt = ft - it
    a = prof[iy, it] * (1 - wt) + prof[iy, it + 1] * wt; b = prof[iy + 1, it] * (1 - wt) + prof[iy + 1, it + 1] * wt
    return a * (1 - wy) + b * wy
def sstep(a, b, x): u = np.clip((x - a) / (b - a), 0, 1); return u * u * (3 - 2 * u)
# ---- VISOR: Tripo modelled the eyes + smile ~1 cm proud of the glass; flatten the screen to a smooth fitted surface
# (the face is drawn procedurally in the shader, so the old bumps only made ghost reflections)
def rbox(x, y, cx, cy, hx, hy, r):
    qx = np.abs(x - cx) - hx + r; qy = np.abs(y - cy) - hy + r
    return np.hypot(np.maximum(qx, 0), np.maximum(qy, 0)) + np.minimum(np.maximum(qx, qy), 0) - r
dv = rbox(P4[:,0], P4[:,1], 0.0, 0.6425, 0.201, 0.117, 0.082)
front = (P4[:,2] > 0.06) & (P4[:,1] > 0.5) & (P4[:,1] < 0.8)
C0 = np.load('vcol.npy'); Lv = C0.mean(1)
# fit z = quadratic(x, y) on the dark glass (original verts only, inside the screen, not the eyes)
orig = np.arange(len(P4)) < 0   # placeholder (patch verts are not on the face)
key0 = np.round(np.fromfile('rt_pos.f32', np.float32).reshape(-1,3).astype(np.float64) * 1e5).astype(np.int64)
glass = front & (dv < -0.012)
Pv = P4[glass]
# use the lowest z per small xy cell (the glass under the bumps)
cell = np.floor(Pv[:,:2] / 0.012).astype(int); order = np.lexsort((Pv[:,2], cell[:,1], cell[:,0])); seen = set(); pick = []
for i in order:
    k = (cell[i,0], cell[i,1])
    if k not in seen: seen.add(k); pick.append(i)
Q = Pv[pick]; X, Y = Q[:,0], Q[:,1] - 0.6425
A = np.stack([np.ones_like(X), X, Y, X*X, Y*Y, X*Y, X**4, Y**4], 1); coef, *_ = np.linalg.lstsq(A, Q[:,2], rcond=None)
def zfit(x, y):
    y = y - 0.6425; return np.stack([np.ones_like(x), x, y, x*x, y*y, x*y, x**4, y**4], 1) @ coef
wv = (1 - sstep(-0.012, 0.0, dv)) * front
P4[:,2] = np.where(wv > 0, P4[:,2] * (1 - wv) + zfit(P4[:,0], P4[:,1]) * wv, P4[:,2])
print('visor flattened verts', (wv > 0.01).sum(), 'fit rms', np.sqrt(np.mean((A @ coef - Q[:,2])**2)).round(4))
# ---- JUNCTION SMOOTHING: Laplacian smoothing around the old arm attachment removes the creases at the shoulder top
dj0 = np.full(len(P4), 9.0)
for sg in (1, -1):
    q = P4 * np.array([sg, 1, 1]); dj0 = np.minimum(dj0, seg_d(q, SH + np.array([0, 0.02, 0]), WR))
wj = (1 - sstep(RA + 0.035, RA + 0.075, dj0)) * (1 - sstep(0.43, 0.445, P4[:,1])) * sstep(0.15, 0.19, np.abs(P4[:,0]))
kw = np.round(P4 * 1e5).astype(np.int64); _, cw = np.unique(kw, axis=0, return_inverse=True); cw = cw.ravel(); nW = cw.max() + 1
E2 = np.concatenate([I4[:, [0, 1]], I4[:, [1, 2]], I4[:, [2, 0]]]); E2 = cw[E2]; E2 = np.concatenate([E2, E2[:, ::-1]])
Pw = np.zeros((nW, 3)); Pw[cw] = P4; ww = np.zeros(nW); np.maximum.at(ww, cw, wj)
deg = np.bincount(E2[:,0], minlength=nW).astype(float)
for it in range(20):
    acc = np.zeros((nW, 3)); np.add.at(acc, E2[:,0], Pw[E2[:,1]])
    avg = acc / np.maximum(deg, 1)[:, None]
    Pw = Pw + (0.5 * ww)[:, None] * (avg - Pw)
P4 = Pw[cw]
print('junction smoothed verts', (wj > 0.01).sum())
rr = np.hypot(P4[:,0], P4[:,2]); tt = np.degrees(np.arctan2(np.abs(P4[:,0]), P4[:,2])); yy = P4[:,1]
rp = prof_at(yy, tt)
wband = sstep(42, 58, tt) * (1 - sstep(124, 148, tt)) * sstep(0.03, 0.07, yy) * (1 - sstep(0.385, 0.425, yy))
wouter = sstep(0.78, 0.9, rr / np.maximum(rp, 1e-6))
W = wband * wouter
newr = rr * (1 - W) + rp * W
scale = np.where(rr > 1e-6, newr / np.maximum(rr, 1e-6), 1.0)
P4[:,0] *= scale; P4[:,2] *= scale
# texture/normal-map clean-up zone also covers the whole old junction (shoulder top, armpit, back of the arm)
dj = np.full(len(P4), 9.0)
for sg in (1, -1):
    q = P4 * np.array([sg, 1, 1]); dj = np.minimum(dj, seg_d(q, SH + np.array([0, 0.02, 0]), WR))
junction = (1 - sstep(RA + 0.03, RA + 0.065, dj)) * (1 - sstep(0.425, 0.44, P4[:,1])) * sstep(0.17, 0.2, np.abs(P4[:,0]))
SIDE = np.clip(np.maximum(W * 1.15, junction), 0, 1)
print('side band verts', (W > 0.01).sum(), 'max move', np.abs(newr - rr).max().round(4))
# vertex normals (area weighted), then for original verts keep smooth normals from geometry too (consistent)
fn = np.cross(P4[I4[:,1]] - P4[I4[:,0]], P4[I4[:,2]] - P4[I4[:,0]]); Nn = np.zeros_like(P4)
for k in range(3): np.add.at(Nn, I4[:, k], fn)
# share normals across welded duplicates
key4 = np.round(P4 * 1e5).astype(np.int64); _, c4 = np.unique(key4, axis=0, return_inverse=True); c4 = c4.ravel()
acc = np.zeros((c4.max() + 1, 3)); np.add.at(acc, c4, Nn); Nn = acc[c4]; Nn /= np.linalg.norm(Nn, axis=1, keepdims=True) + 1e-12
P4.astype(np.float32).tofile('cut_pos.f32'); UV4.astype(np.float32).tofile('cut_uv.f32'); I4.astype(np.uint32).tofile('cut_idx.u32'); Nn.astype(np.float32).tofile('cut_nrm.f32'); SIDE.astype(np.float32).tofile('cut_side.f32')
print('out verts', len(P4), 'tris', len(I4), 'patch tris', len(newT))
json.dump({'arm_radius': RA, 'shoulder': SH.tolist(), 'wrist': WR.tolist(), 'hand_centre': HC.tolist(), 'hand_radius': RH}, open('cut_info.json', 'w'))

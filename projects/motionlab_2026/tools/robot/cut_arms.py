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
# vertex normals (area weighted), then for original verts keep smooth normals from geometry too (consistent)
fn = np.cross(P4[I4[:,1]] - P4[I4[:,0]], P4[I4[:,2]] - P4[I4[:,0]]); Nn = np.zeros_like(P4)
for k in range(3): np.add.at(Nn, I4[:, k], fn)
# share normals across welded duplicates
key4 = np.round(P4 * 1e5).astype(np.int64); _, c4 = np.unique(key4, axis=0, return_inverse=True); c4 = c4.ravel()
acc = np.zeros((c4.max() + 1, 3)); np.add.at(acc, c4, Nn); Nn = acc[c4]; Nn /= np.linalg.norm(Nn, axis=1, keepdims=True) + 1e-12
P4.astype(np.float32).tofile('cut_pos.f32'); UV4.astype(np.float32).tofile('cut_uv.f32'); I4.astype(np.uint32).tofile('cut_idx.u32'); Nn.astype(np.float32).tofile('cut_nrm.f32')
print('out verts', len(P4), 'tris', len(I4), 'patch tris', len(newT))
json.dump({'arm_radius': RA, 'shoulder': SH.tolist(), 'wrist': WR.tolist(), 'hand_centre': HC.tolist(), 'hand_radius': RH}, open('cut_info.json', 'w'))

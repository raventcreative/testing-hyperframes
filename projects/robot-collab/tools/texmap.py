"""texel -> 3D position / normal / component maps for the robot texture (2048), z-buffer free (each texel belongs to one triangle in UV)."""
import numpy as np, time
S = 2048
P = np.fromfile('pos.f32', np.float32).reshape(-1, 3); Nn = np.fromfile('nrm.f32', np.float32).reshape(-1, 3)
UV = np.fromfile('uv.f32', np.float32).reshape(-1, 2); I = np.fromfile('idx.u32', np.uint32).reshape(-1, 3)
vl = np.load('vlab.npy')
pos = np.zeros((S, S, 3), np.float32); nrm = np.zeros((S, S, 3), np.float32); comp = np.full((S, S), -1, np.int8)
t0 = time.time()
uvp = UV[I] * (S - 1)            # (T,3,2) ; glTF uv: v down = image row
for k in range(len(I)):
    uv = uvp[k]
    x0, y0 = np.floor(uv.min(0)).astype(int); x1, y1 = np.ceil(uv.max(0)).astype(int)
    x0 = max(x0, 0); y0 = max(y0, 0); x1 = min(x1, S - 1); y1 = min(y1, S - 1)
    if x1 < x0 or y1 < y0 or (x1 - x0) * (y1 - y0) > 40000: continue
    gx, gy = np.meshgrid(np.arange(x0, x1 + 1), np.arange(y0, y1 + 1)); gx = gx.ravel(); gy = gy.ravel()
    (ax, ay), (bx, by), (cx, cy) = uv
    den = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)
    if abs(den) < 1e-12: continue
    l1 = ((by - cy) * (gx - cx) + (cx - bx) * (gy - cy)) / den
    l2 = ((cy - ay) * (gx - cx) + (ax - cx) * (gy - cy)) / den
    l3 = 1 - l1 - l2
    m = (l1 >= -0.01) & (l2 >= -0.01) & (l3 >= -0.01)
    if not m.any(): continue
    t = I[k]; L = np.stack([l1[m], l2[m], l3[m]], 1)
    pos[gy[m], gx[m]] = L @ P[t]; nrm[gy[m], gx[m]] = L @ Nn[t]; comp[gy[m], gx[m]] = vl[t[0]]
print('raster', round(time.time() - t0, 1), 's, covered', (comp >= 0).mean())
nrm /= np.maximum(np.linalg.norm(nrm, axis=2, keepdims=True), 1e-6)
np.save('tex_pos.npy', pos); np.save('tex_nrm.npy', nrm); np.save('tex_comp.npy', comp)

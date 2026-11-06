"""Bakes the AI PRENEUR wordmark into the robot's base colour (4096) + roughness, wrapped around the collar front with a
cylindrical projection (constant letter width along the curved shell) -> printed-on look, lit by the PBR material."""
import numpy as np, sys
from PIL import Image
S = 4096
P = np.fromfile('pos.f32', np.float32).reshape(-1, 3); Nn = np.fromfile('nrm.f32', np.float32).reshape(-1, 3)
UV = np.fromfile('uv.f32', np.float32).reshape(-1, 2); I = np.fromfile('idx.u32', np.uint32).reshape(-1, 3)
AX, AZ, RREF = 0.023, 0.005, 0.215          # collar axis (x, z) and reference radius for the arc length
W, YC = float(sys.argv[1]) if len(sys.argv) > 1 else 0.27, float(sys.argv[2]) if len(sys.argv) > 2 else 0.385
TH0 = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0     # centre angle (rad), 0 = collar front (+z)
lg = Image.open('logo_src.png').convert('RGBA'); lg = lg.crop(lg.getbbox())
H = W * lg.height / lg.width
# texture-space raster of the collar-front triangles only (4096)
c = P[I].mean(1); th = np.arctan2(c[:, 0] - AX, c[:, 2] - AZ)
sel = (c[:, 1] > YC - H * 2.5) & (c[:, 1] < YC + H * 2.5) & (np.abs(th - TH0) < (W / 2) / RREF + 0.12) & (c[:, 2] > -0.05)
T = I[sel]; print('triangles', len(T), 'logo', W, 'x', round(H, 4))
TX, TY, XYZ, NRM = [], [], [], []
for t in T:
    uv = UV[t] * (S - 1)
    x0, y0 = np.floor(uv.min(0)).astype(int); x1, y1 = np.ceil(uv.max(0)).astype(int)
    gx, gy = np.meshgrid(np.arange(x0, x1 + 1), np.arange(y0, y1 + 1)); gx = gx.ravel(); gy = gy.ravel()
    (ax, ay), (bx, by), (cx, cy) = uv
    den = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)
    if abs(den) < 1e-12: continue
    l1 = ((by - cy) * (gx - cx) + (cx - bx) * (gy - cy)) / den; l2 = ((cy - ay) * (gx - cx) + (ax - cx) * (gy - cy)) / den; l3 = 1 - l1 - l2
    m = (l1 >= -0.02) & (l2 >= -0.02) & (l3 >= -0.02)
    if not m.any(): continue
    L = np.stack([l1[m], l2[m], l3[m]], 1)
    TX.append(gx[m]); TY.append(gy[m]); XYZ.append(L @ P[t]); NRM.append(L @ Nn[t])
TX = np.concatenate(TX); TY = np.concatenate(TY); XYZ = np.concatenate(XYZ); NRM = np.concatenate(NRM)
th = np.arctan2(XYZ[:, 0] - AX, XYZ[:, 2] - AZ)
s = (th - TH0) * RREF
lu = (s + W / 2) / W; lv = (YC + H / 2 - XYZ[:, 1]) / H
# outward-facing only (skip the inner side / back faces of the shell)
rad = np.stack([XYZ[:, 0] - AX, np.zeros(len(XYZ)), XYZ[:, 2] - AZ], 1); rad /= np.linalg.norm(rad, axis=1, keepdims=True) + 1e-9
facing = (NRM * rad).sum(1) / (np.linalg.norm(NRM, axis=1) + 1e-9)
ok = (lu >= 0) & (lu <= 1) & (lv >= 0) & (lv <= 1) & (facing > 0.35)
print('logo texels', ok.sum())
# logo sampled at the texture's own resolution (pre-filtered) -> clean anti-aliased edges
dens = 2360.0                                  # texels per unit at 4096 on the collar front
lw = int(W * dens * 2); lh = max(8, int(H * dens * 2))
L = np.asarray(lg.resize((lw, lh), Image.LANCZOS)).astype(np.float32) / 255
def bil(img, u, v):
    x = np.clip(u * (img.shape[1] - 1), 0, img.shape[1] - 1.001); y = np.clip(v * (img.shape[0] - 1), 0, img.shape[0] - 1.001)
    x0 = np.floor(x).astype(int); y0 = np.floor(y).astype(int); fx = (x - x0)[:, None]; fy = (y - y0)[:, None]
    return (img[y0, x0] * (1 - fx) * (1 - fy) + img[y0, x0 + 1] * fx * (1 - fy) + img[y0 + 1, x0] * (1 - fx) * fy + img[y0 + 1, x0 + 1] * fx * fy)
smp = bil(L, lu[ok], lv[ok]); a = smp[:, 3:4]
# fade the print slightly where the shell turns away (natural, no hard cut)
a = a * np.clip((facing[ok] - 0.35) / 0.25, 0, 1)[:, None]
base = Image.open('tex_base_noeyes_fix.png').convert('RGB').resize((S, S), Image.LANCZOS)
B = np.asarray(base).astype(np.float32)
alb = B[TY[ok], TX[ok]]
ink = np.array([46, 46, 46], np.float32)
shade = (alb.mean(1, keepdims=True) / 245.0).clip(0.6, 1.05)          # keep the shell's baked shading under the ink
B[TY[ok], TX[ok]] = alb * (1 - a) + ink * shade * a
import gutter
C4 = np.load('cov4096.npy')
B = gutter.dilate(B, C4, 10)
Image.fromarray(np.clip(B, 0, 255).astype(np.uint8)).save('tex_base_logo_4096.png')
# roughness: ink is satin (less glossy than the white shell)
MR = np.asarray(Image.open('tex_mr_noeyes_fix.png').convert('RGB').resize((S, S), Image.LANCZOS)).astype(np.float32)
mr = MR[TY[ok], TX[ok]]; mr[:, 1] = mr[:, 1] * (1 - a[:, 0]) + np.maximum(mr[:, 1], 95) * a[:, 0]; mr[:, 2] = mr[:, 2] * (1 - a[:, 0])
MR[TY[ok], TX[ok]] = mr
MR = gutter.dilate(MR, C4, 10)
Image.fromarray(np.clip(MR, 0, 255).astype(np.uint8)).resize((2048, 2048), Image.LANCZOS).save('tex_mr_logo.png')
print('baked')

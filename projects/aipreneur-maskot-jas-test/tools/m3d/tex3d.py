"""Helpers: mesh arrays exported by export.mjs + UV-space rasterisation (texel -> 3D surface point)."""
import numpy as np
from pathlib import Path
from PIL import Image
SRC = Path(__file__).resolve().parents[2] / "mascot3d_src"
P = np.fromfile(SRC / "jas_pos.bin", np.float32).reshape(-1, 3)
UV = np.fromfile(SRC / "jas_uv.bin", np.float32).reshape(-1, 2)
IDX = np.fromfile(SRC / "jas_idx.bin", np.uint32).reshape(-1, 3)


def tris_in_box(x0, x1, y0, y1, zmin=-9):
    c = P[IDX].mean(1)
    m = (c[:, 0] > x0) & (c[:, 0] < x1) & (c[:, 1] > y0) & (c[:, 1] < y1) & (c[:, 2] > zmin)
    return IDX[m]


def raster_uv(tris, S):
    """for every texel covered by `tris` (UV space, SxS texture, v down) -> (tx, ty, xyz)."""
    TX, TY, XYZ = [], [], []
    for t in tris:
        uv = UV[t] * (S - 1); p = P[t]
        x0, y0 = np.floor(uv.min(0)).astype(int); x1, y1 = np.ceil(uv.max(0)).astype(int)
        if x1 - x0 > 200 or y1 - y0 > 200:
            continue
        gx, gy = np.meshgrid(np.arange(x0, x1 + 1), np.arange(y0, y1 + 1))
        gx = gx.ravel(); gy = gy.ravel()
        (ax, ay), (bx, by), (cx, cy) = uv
        den = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)
        if abs(den) < 1e-9:
            continue
        l1 = ((by - cy) * (gx - cx) + (cx - bx) * (gy - cy)) / den
        l2 = ((cy - ay) * (gx - cx) + (ax - cx) * (gy - cy)) / den
        l3 = 1 - l1 - l2
        m = (l1 >= -0.02) & (l2 >= -0.02) & (l3 >= -0.02)
        if not m.any():
            continue
        TX.append(gx[m]); TY.append(gy[m])
        XYZ.append(l1[m, None] * p[0] + l2[m, None] * p[1] + l3[m, None] * p[2])
    return np.concatenate(TX), np.concatenate(TY), np.concatenate(XYZ)


def front_view(tex, x0, x1, y0, y1, scale=4000, zmin=0.0):
    """orthographic front render of a box region (via texel splats, nearest z wins)."""
    tris = tris_in_box(x0, x1, y0, y1, zmin)
    S = tex.shape[0]
    tx, ty, xyz = raster_uv(tris, S)
    W = int((x1 - x0) * scale); H = int((y1 - y0) * scale)
    img = np.zeros((H, W, 3), np.uint8); zb = np.full((H, W), -9.0)
    px = ((xyz[:, 0] - x0) * scale).astype(int); py = ((y1 - xyz[:, 1]) * scale).astype(int)
    ok = (px >= 0) & (px < W) & (py >= 0) & (py < H)
    order = np.argsort(xyz[ok, 2])
    px, py, col = px[ok][order], py[ok][order], tex[ty[ok], tx[ok]][order]
    img[py, px] = col
    return img

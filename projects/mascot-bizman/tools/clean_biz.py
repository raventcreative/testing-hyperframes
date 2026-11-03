#!/usr/bin/env python3
"""Base-colour clean-up for the chibi businessman mascot (original GLB untouched):
 - paints out the baked smile (the runtime draws a talking mouth on clean skin)
 - pads every UV chart border (no foreign colours bleeding in at chart edges)
Fill = harmonic diffusion in a front-projected grid of the region, sampled back to the texels (atlas-safe).
Usage: python3 clean_biz.py <out.png>"""
import sys
import numpy as np
from PIL import Image
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
import tex3d
tex = np.asarray(Image.open(tex3d.BASE).convert("RGB")).astype(np.float32)
S = tex.shape[0]


def clean(box, zmin, is_bad, grid=0.0004, dil=3, iters=600):
    x0, x1, y0, y1 = box
    tx, ty, xyz = tex3d.raster_uv(tex3d.tris_in_box(x0 - 0.01, x1 + 0.01, y0 - 0.01, y1 + 0.01, zmin), S)
    k = (xyz[:, 0] > x0) & (xyz[:, 0] < x1) & (xyz[:, 1] > y0) & (xyz[:, 1] < y1) & (xyz[:, 2] > zmin)
    tx, ty, xyz = tx[k], ty[k], xyz[k]
    col = tex[ty, tx]
    bad = is_bad(col, xyz)
    W = int((x1 - x0) / grid) + 1; H = int((y1 - y0) / grid) + 1
    gx = ((xyz[:, 0] - x0) / grid).astype(int); gy = ((y1 - xyz[:, 1]) / grid).astype(int)
    acc = np.zeros((H, W, 3)); cnt = np.zeros((H, W)); badg = np.zeros((H, W), bool)
    np.add.at(acc, (gy[~bad], gx[~bad]), col[~bad]); np.add.at(cnt, (gy[~bad], gx[~bad]), 1)
    badg[gy[bad], gx[bad]] = True
    for _ in range(dil):
        b = badg.copy(); b[1:] |= badg[:-1]; b[:-1] |= badg[1:]; b[:, 1:] |= badg[:, :-1]; b[:, :-1] |= badg[:, 1:]; badg = b
    known = (cnt > 0) & ~badg
    img = np.where(known[..., None], acc / np.maximum(cnt, 1)[..., None], 0)
    fill = img.copy(); fill[~known] = img[known].mean(0)
    for _ in range(iters):
        f = fill.copy()
        f[1:-1, 1:-1] = (fill[:-2, 1:-1] + fill[2:, 1:-1] + fill[1:-1, :-2] + fill[1:-1, 2:]) / 4
        fill = np.where(known[..., None], img, f)
    sel = badg[gy, gx]
    tex[ty[sel], tx[sel]] = fill[gy[sel], gx[sel]]
    print("box", box, "texels", len(tx), "replaced", int(sel.sum()))


# skin reference: a ring around the mouth (nose-to-chin), excluding the mouth itself
t0 = tex3d.tris_in_box(-0.07, 0.07, 0.515, 0.585, 0.17); _tx, _ty, _xyz = tex3d.raster_uv(t0, S)
ring = ((_xyz[:, 0] / 0.06) ** 2 + ((_xyz[:, 1] - 0.547) / 0.03) ** 2) > 1
skin = np.median(tex[_ty[ring], _tx[ring]], 0); print("mouth-area skin", skin)
# the red smile + its grey crease shading + spiky bake specks at the corners
clean((-0.05, 0.05, 0.527, 0.567), 0.17,
      lambda c, p: (np.abs(c - skin).sum(1) > 34) & (((p[:, 0] / 0.045) ** 2 + ((p[:, 1] - 0.547) / 0.017) ** 2) < 1))

# ---- seam padding (push-pull dilation outside the UV charts)
cov = np.zeros((S, S), bool)
uvp = tex3d.UV * (S - 1)
tri = uvp[tex3d.IDX]
mn = np.floor(tri.min(1)).astype(int); mx = np.ceil(tri.max(1)).astype(int)
for t in range(len(tri)):
    x0, y0 = np.clip(mn[t], 0, S - 1); x1, y1 = np.clip(mx[t], 0, S - 1)
    gx, gy = np.meshgrid(np.arange(x0, x1 + 1), np.arange(y0, y1 + 1))
    (ax_, ay), (bx, by), (cx, cy) = tri[t]
    den = (by - cy) * (ax_ - cx) + (cx - bx) * (ay - cy)
    if abs(den) < 1e-12: continue
    l1 = ((by - cy) * (gx - cx) + (cx - bx) * (gy - cy)) / den
    l2 = ((cy - ay) * (gx - cx) + (ax_ - cx) * (gy - cy)) / den
    m = (l1 >= -0.01) & (l2 >= -0.01) & (1 - l1 - l2 >= -0.01)
    cov[gy[m], gx[m]] = True
print("chart coverage", round(cov.mean(), 3))
known = cov.copy(); out = tex.copy()
for it in range(16):
    acc = np.zeros_like(out); cnt = np.zeros((S, S))
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)):
        sh_k = np.roll(np.roll(known, dy, 0), dx, 1); sh_c = np.roll(np.roll(out, dy, 0), dx, 1)
        acc += sh_c * sh_k[..., None]; cnt += sh_k
    grow = (~known) & (cnt > 0)
    out[grow] = acc[grow] / cnt[grow][:, None]
    known |= grow
Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(sys.argv[1])
print("saved", sys.argv[1])

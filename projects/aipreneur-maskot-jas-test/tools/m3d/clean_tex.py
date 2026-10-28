#!/usr/bin/env python3
"""Base-colour clean-up for the new suit mascot (originals untouched):
 - paints out the misprinted jacket text "AII FRENEUR" (a crisp AI PRENEUR logo decal replaces it at runtime)
 - paints out the baked smile (the runtime draws a talking mouth on clean skin)
Fill = diffusion in a front-projected grid of the region, sampled back to the texels (atlas-safe)."""
import sys, json
import numpy as np
from PIL import Image
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
import tex3d
OUT = tex3d.SRC.parent / "assets/mascot3d"
tex = np.asarray(Image.open(tex3d.SRC / "jas_chibi_businessperson_3d_model_basecolor.webp").convert("RGB")).astype(np.float32)
S = tex.shape[0]


def clean(box, zmin, is_bad, grid=0.0004, dil=2, iters=400):
    x0, x1, y0, y1 = box
    tx, ty, xyz = tex3d.raster_uv(tex3d.tris_in_box(x0 - 0.01, x1 + 0.01, y0 - 0.01, y1 + 0.01, zmin), S)
    k = (xyz[:, 0] > x0) & (xyz[:, 0] < x1) & (xyz[:, 1] > y0) & (xyz[:, 1] < y1) & (xyz[:, 2] > zmin)
    tx, ty, xyz = tx[k], ty[k], xyz[k]
    col = tex[ty, tx]
    bad = is_bad(col)
    W = int((x1 - x0) / grid) + 1; H = int((y1 - y0) / grid) + 1
    gx = ((xyz[:, 0] - x0) / grid).astype(int); gy = ((y1 - xyz[:, 1]) / grid).astype(int)
    acc = np.zeros((H, W, 3)); cnt = np.zeros((H, W)); badg = np.zeros((H, W), bool)
    np.add.at(acc, (gy[~bad], gx[~bad]), col[~bad]); np.add.at(cnt, (gy[~bad], gx[~bad]), 1)
    badg[gy[bad], gx[bad]] = True
    for _ in range(dil):   # grow the bad mask (anti-aliased glyph edges)
        b = badg.copy(); b[1:] |= badg[:-1]; b[:-1] |= badg[1:]; b[:, 1:] |= badg[:, :-1]; b[:, :-1] |= badg[:, 1:]; badg = b
    known = (cnt > 0) & ~badg
    img = np.where(known[..., None], acc / np.maximum(cnt, 1)[..., None], 0)
    fill = img.copy(); m = known.astype(float)
    mean = img[known].mean(0); fill[~known] = mean
    for _ in range(iters):   # harmonic fill of the unknown cells (known cells fixed)
        f = fill.copy()
        f[1:-1, 1:-1] = (fill[:-2, 1:-1] + fill[2:, 1:-1] + fill[1:-1, :-2] + fill[1:-1, 2:]) / 4
        fill = np.where(known[..., None], img, f)
    sel = badg[gy, gx]
    tex[ty[sel], tx[sel]] = fill[gy[sel], gx[sel]]
    print("box", box, "texels", len(tx), "replaced", int(sel.sum()))


lum = lambda c: c @ np.array([0.299, 0.587, 0.114])
clean((-0.118, -0.012, 0.364, 0.399), 0.04, lambda c: lum(c) > 62)                      # jacket text
skin = np.array([250, 222, 205.0])
clean((-0.045, 0.045, 0.532, 0.566), 0.12, lambda c: np.abs(c - skin).sum(1) > 70)       # baked smile
Image.fromarray(np.clip(tex, 0, 255).astype(np.uint8)).save(OUT / "basecolor_clean.png")

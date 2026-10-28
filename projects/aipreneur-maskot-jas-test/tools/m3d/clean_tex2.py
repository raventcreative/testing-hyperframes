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
tex = np.asarray(Image.open(tex3d.BASE).convert("RGB")).astype(np.float32)
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


# v2 model: jacket is blank (logo decal is added at runtime); only the baked smile is painted out
t0 = tex3d.tris_in_box(-0.06, 0.06, 0.52, 0.575, 0.12); _tx, _ty, _ = tex3d.raster_uv(t0, S)
skin = np.median(tex[_ty, _tx], 0); print("mouth-area skin", skin)
clean((-0.045, 0.045, 0.53, 0.566), 0.12, lambda c: np.abs(c - skin).sum(1) > 55)
# hands: the baked texture has a white "glove" highlight on the back of the hand and orange fingers.
# Every hand texel past the shirt cuff (measured along the wrist->fingertip axis) is re-coloured to one skin tone
# that matches the face; only the luminance (shading) of the original is kept, compressed so nothing goes white.
W0 = np.array([0.188, 0.296]); TIP = np.array([0.232, 0.215]); AXD = (TIP - W0) / np.linalg.norm(TIP - W0)
SKIN_HAND = np.array([247, 214, 197.0])
for sgn in (1, -1):
    tx, ty, xyz = tex3d.raster_uv(tex3d.tris_in_box(min(sgn * 0.12, sgn * 0.3), max(sgn * 0.12, sgn * 0.3), 0.17, 0.33, -1), S)
    t = (np.stack([np.abs(xyz[:, 0]), xyz[:, 1]], 1) - W0) @ AXD
    c0 = tex[ty, tx]; mx, mn = c0.max(1), c0.min(1); sat = (mx - mn) / np.maximum(mx, 1)
    k = (t > 0.018) | ((t > 0.0) & (sat > 0.16))           # + skin-coloured texels tucked inside the cuff
    tx, ty, t = tx[k], ty[k], np.where(t[k] > 0.018, t[k], 0.03)
    c = tex[ty, tx]
    L = c @ np.array([0.299, 0.587, 0.114])
    lo, hi = np.percentile(L, 5), np.percentile(L, 97)
    sh = np.clip((L - lo) / max(1, hi - lo), 0, 1)
    new = SKIN_HAND * (0.74 + 0.3 * sh)[:, None]
    w = np.clip((t - 0.018) / 0.008, 0, 1)[:, None]          # feather into the cuff edge
    tex[ty, tx] = c * (1 - w) + np.clip(new, 0, 255) * w
    print("hand texels recoloured", len(tx))
Image.fromarray(np.clip(tex, 0, 255).astype(np.uint8)).save(OUT / "basecolor_v2_clean.png")

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
SKIN_HAND = np.array([244, 205, 186.0])
for sgn in (1, -1):
    tx, ty, xyz = tex3d.raster_uv(tex3d.tris_in_box(min(sgn * 0.12, sgn * 0.3), max(sgn * 0.12, sgn * 0.3), 0.17, 0.33, -1), S)
    t = (np.stack([np.abs(xyz[:, 0]), xyz[:, 1]], 1) - W0) @ AXD
    c0 = tex[ty, tx]; mx, mn = c0.max(1), c0.min(1); sat = (mx - mn) / np.maximum(mx, 1)
    # orange bake specks on the cuff / sleeve end (not hand): each takes the MAJORITY class (white cuff or dark
    # sleeve) of its 12 nearest neutral neighbours on the surface and that class's median colour -> no grey mix
    Lc = c0 @ np.array([0.299, 0.587, 0.114])
    band = (t > -0.02) & (t <= 0.013) & (sat > 0.12)
    neu = (t > -0.03) & (t <= 0.02) & (sat < 0.1) & ((Lc > 150) | (Lc < 90))
    pn, cn, wn = xyz[neu], c0[neu], Lc[neu] > 150
    bi = np.where(band)[0]; nfix = 0
    for a in range(0, len(bi), 512):
        ch = bi[a:a + 512]
        d = np.linalg.norm(xyz[ch][:, None, :] - pn[None, :, :], axis=2)
        nn = np.argsort(d, 1)[:, :12]
        for r, i in enumerate(ch):
            ids = nn[r]; isw = wn[ids]
            pick = ids[isw] if isw.mean() >= 0.5 else ids[~isw]
            tex[ty[i], tx[i]] = np.median(cn[pick], 0); nfix += 1
    print("cuff specks fixed", nfix)
    k = t > 0.013
    tx, ty, t = tx[k], ty[k], t[k]
    c = tex[ty, tx]
    L = c @ np.array([0.299, 0.587, 0.114])
    lo, hi = np.percentile(L, 5), np.percentile(L, 97)
    sh = np.clip((L - lo) / max(1, hi - lo), 0, 1)
    new = SKIN_HAND * (0.8 + 0.22 * sh)[:, None]
    w = np.clip((t - 0.013) / 0.005, 0, 1)[:, None]          # feather into the cuff edge
    tex[ty, tx] = c * (1 - w) + np.clip(new, 0, 255) * w
    print("hand texels recoloured", len(tx))
# ---- jacket speck removal (3D-aware): a bright texel on the jacket counts as a bake fleck when, on the SURFACE
# around it (3D radius ~1 cm, 3x3x3 voxel neighbourhood), almost everything is dark jacket. Shirt, pants and cuffs
# are large bright areas, so they are never touched. Flecks take the mean colour of the dark texels around them.
lumf = lambda c: c @ np.array([0.299, 0.587, 0.114])
tx, ty, xyz = tex3d.raster_uv(tex3d.tris_in_box(-0.3, 0.3, 0.22, 0.48, -1), S)
col = tex[ty, tx]; L = lumf(col)
lo = np.array([-0.3, 0.22, -0.2]); cell = 0.004
ci = np.floor((xyz - lo) / cell).astype(int); dims = ci.max(0) + 3; ci += 1
dark = L < 75
cnt = np.zeros(dims); drk = np.zeros(dims); acc = np.zeros(tuple(dims) + (3,))
np.add.at(cnt, tuple(ci.T), 1); np.add.at(drk, tuple(ci.T), dark)
np.add.at(acc, tuple(ci.T), col * dark[:, None])
def box3(a):
    o = a.copy()
    for ax in range(3): o = np.roll(o, 1, ax) + o + np.roll(o, -1, ax)
    return o
C, Dk, A = box3(cnt), box3(drk), box3(acc)
k = tuple(ci.T)
fleck = (L > 100) & (Dk[k] / np.maximum(C[k], 1) > 0.8)
tex[ty[fleck], tx[fleck]] = A[k][fleck] / np.maximum(Dk[k][fleck], 1)[:, None]
print("jacket flecks removed", int(fleck.sum()))
# ---- seam padding: every texel outside the UV charts is filled from the nearest chart colour (push-pull dilation),
# so bilinear / mip sampling at chart borders never pulls in foreign colours (white specks on the jacket, red lines
# on the hands, "torn" sleeve edges)
cov = np.zeros((S, S), bool)
uvp = tex3d.UV * (S - 1)
tri = uvp[tex3d.IDX]                                  # (T,3,2)
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
for it in range(24):
    acc = np.zeros_like(out); cnt = np.zeros((S, S))
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)):
        sh_k = np.roll(np.roll(known, dy, 0), dx, 1); sh_c = np.roll(np.roll(out, dy, 0), dx, 1)
        acc += sh_c * sh_k[..., None]; cnt += sh_k
    grow = (~known) & (cnt > 0)
    out[grow] = acc[grow] / cnt[grow][:, None]
    known |= grow
tex = out
Image.fromarray(np.clip(tex, 0, 255).astype(np.uint8)).save(OUT / "basecolor_v2_clean.png")

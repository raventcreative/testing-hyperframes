"""Rebuilds the open (left-of-frame) hand under the removed subtitle in frame 115.83 s from its real geometry.
The finger layout was read from the pixels visible between the subtitle letters (skin / dark gap map):
  - middle finger: lower edge ~y1150 (x250-290), tip (327,1120)            -> real, untouched
  - ring finger:   DIAGONAL, base ~(236,1199) on the palm -> tip ~(322,1158) -> rebuilt: the middle finger's own pixels
                   mapped (similarity transform) from its axis onto the ring finger's axis, so skin, shading and nail are real
  - dark gaps:     middle/ring above the ring finger, ring/little below it  -> shirt-dark sampled from the visible gap
  - little finger: top edge ~y1216, real below that                         -> untouched
  - palm (under "b", "a"): smooth skin from the LaMa pass
Only pixels under the subtitle strokes (+ their dark outline) are replaced, so everything visible stays the original.
Usage: python3 -I tools/fix_hand.py <frame_115.83.png> <clean.png> <out.png>"""
import sys
import cv2
import numpy as np

src, clean_p, out = sys.argv[1:4]
im = cv2.imread(src)
cl = cv2.imread(clean_p)
H, W = im.shape[:2]
f = im.astype(np.float32)
mn = im.min(axis=2)
K = lambda r: cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))

BX0, BX1, BY0, BY1 = 172, 350, 1140, 1222                 # hand box (left hand only)
st = np.zeros((H, W), np.uint8)
band = (slice(1150, 1232), slice(BX0, BX1))
st[band][mn[band] > 185] = 255
hole = cv2.dilate(st, K(4))
hole[1206:1217, 240:350][f[1206:1217, 240:350, 2] < 80] = 255        # dark outline band under the word
hole[1146:1220, 172:194] = 255                                      # grey edge of the subtitle plate left of the "b"
hole[:BY0] = 0; hole[BY1:] = 0; hole[:, :BX0] = 0; hole[:, BX1:] = 0

# ---- model of the hand inside the box
res = cl.astype(np.float32)                                         # palm: LaMa (smooth skin)
# finger zone right of the palm: dark gaps everywhere, then the ring finger on top, real little finger below y1216
M = np.zeros((H, W), np.uint8)
cv2.fillPoly(M, [np.array([[264, 1148], [342, 1146], [342, 1216], [246, 1216], [252, 1204], [262, 1170]], np.int32)], 255)
gm = cv2.GaussianBlur(M, (0, 0), 2.2).astype(np.float32) / 255     # gaps close into the palm like a real finger web
vis = np.zeros((H, W), bool); vis[1150:1240, 345:385] = True                  # plain shirt right of the fingertips
vis &= (hole == 0) & (f[..., 2] < 70)
dark = np.median(f[vis], axis=0) if vis.sum() > 15 else np.array([26, 26, 28], np.float32)
rng = np.random.default_rng(5)
# local dark field: normalised blur of the real, visible dark pixels around (follows the shirt's own shading)
dm = ((hole == 0) & (f[..., 2] < 60)).astype(np.float32)
dm[:1090] = 0; dm[1260:] = 0; dm[:, :200] = 0; dm[:, 420:] = 0
num = cv2.GaussianBlur(f * dm[..., None], (0, 0), 10); den = cv2.GaussianBlur(dm, (0, 0), 10)[..., None]
dfield = np.where(den > 1e-3, num / np.maximum(den, 1e-3), dark[None, None, :])
res = res * (1 - gm[..., None]) + (dfield + rng.normal(0, 1.4, (H, W, 1)).astype(np.float32)) * gm[..., None]
pk = np.zeros((H, W), np.float32); pk[1216:1240, 236:350] = 1; pk = cv2.GaussianBlur(pk, (0, 0), 1.2)[..., None]
res = res * (1 - pk) + f * pk                                       # little finger: its real pixels

# ring finger: middle finger axis (base Bm -> tip Tm) mapped onto the ring finger axis (Br -> Tr)
Bm, Tm = np.array([238.0, 1127.0]), np.array([322.0, 1122.0])
Br, Tr = np.array([236.0, 1199.0]), np.array([322.0, 1158.0])
vm, vr = Tm - Bm, Tr - Br
s = np.linalg.norm(vr) / np.linalg.norm(vm) * 0.97
ang = np.arctan2(vr[1], vr[0]) - np.arctan2(vm[1], vm[0])
c, si = s * np.cos(ang), s * np.sin(ang)
A = np.array([[c, -si, 0], [si, c, 0]], np.float32)
A[:, 2] = Br - A[:, :2] @ Bm
patch = cv2.warpAffine(f, A, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
patch = patch * 0.96                                                # ring finger sits a touch deeper in shadow
# finger mask: the middle finger's own skin, carried by the same transform (exact silhouette incl. rounded tip)
skin = ((f[..., 2] > 95) & (f[..., 2] > f[..., 0] + 20)).astype(np.uint8) * 255
mzone = np.zeros((H, W), np.uint8)
cv2.fillPoly(mzone, [np.array([[226, 1100], [334, 1100], [334, 1146], [226, 1150]], np.int32)], 255)
fm = cv2.warpAffine(cv2.morphologyEx(skin & mzone, cv2.MORPH_OPEN, K(1)), A, (W, H), flags=cv2.INTER_LINEAR)
fm = cv2.GaussianBlur(fm, (0, 0), 1.2).astype(np.float32) / 255
fade = np.clip((np.arange(W) - 236) / 14, 0, 1)[None, :]           # melt the finger base into the palm
fm = fm * fade
res = res * (1 - fm[..., None]) + patch * fm[..., None]

# ---- composite: a smooth region around what the subtitle covered (letter-shaped cuts leave ghosts / ragged edges)
hm = np.maximum(cv2.GaussianBlur(cv2.dilate(hole, K(5)), (0, 0), 2.5).astype(np.float32) / 255, (hole > 0).astype(np.float32))[..., None]
hand = f * (1 - hm) + res * hm
box = np.zeros((H, W), np.float32); box[BY0:BY1, BX0:BX1] = 1
box = cv2.GaussianBlur(box, (0, 0), 1.5)[..., None]
outf = cl.astype(np.float32) * (1 - box) + hand * box
cv2.imwrite(out, np.clip(outf, 0, 255).astype(np.uint8))
print("hand fixed", out, "gap colour", dark, "scale %.3f angle %.1f deg" % (s, np.degrees(ang)))

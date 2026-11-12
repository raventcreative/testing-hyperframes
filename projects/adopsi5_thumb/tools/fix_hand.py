"""Rebuilds the open (left-of-frame) hand under the removed subtitle in frame 115.83 s by hand-structure instead of LaMa,
which had smeared the ring finger into a blob:
  - ring finger: the visible middle finger, shifted down/right onto the ring finger's visible top edge and tip (fingers are
    near-parallel here), pasted only where the subtitle was
  - gap between ring finger and little finger: the dark shirt colour sampled from the visible part of that gap
  - palm under the "b" and the little finger's top edge: Navier-Stokes inpaint over the thin stroke mask (smooth skin)
Everything outside the hand box is taken from the LaMa-cleaned frame unchanged.
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

BX0, BX1, BY0, BY1 = 172, 346, 1138, 1240                 # hand box
st = np.zeros((H, W), np.uint8)
band = (slice(1150, 1232), slice(BX0, BX1))
st[band][mn[band] > 185] = 255
sh = np.zeros_like(st); sh[7:, 2:] = st[:-7, :-2]                 # the subtitle's drop shadow (offset down-right)
hole = cv2.dilate(st | sh, K(7))
hole[1146:1220, 172:194] = 255                                     # grey edge of the subtitle plate left of the "b"
hole[:BY0] = 0; hole[BY1:] = 0; hole[:, :BX0] = 0; hole[:, BX1:] = 0

# 1. base: the LaMa result (smooth palm and little finger)
res = cl.astype(np.float32)

# 2. dark gap between ring finger and little finger: a soft wedge, closed toward the palm
gap = np.zeros((H, W), np.uint8)
cv2.fillPoly(gap, [np.array([[244, 1192], [300, 1190], [336, 1188], [336, 1228], [316, 1222], [300, 1213], [283, 1207], [252, 1203], [244, 1199]], np.int32)], 255)
gap = cv2.GaussianBlur(gap, (0, 0), 3.0).astype(np.float32) / 255
vis = np.zeros((H, W), bool); vis[1150:1240, 338:380] = True                 # shirt just right of the fingertips
vis &= (hole == 0) & (f[..., 2] < 75)
dark = np.median(f[vis], axis=0) if vis.sum() > 20 else np.array([18, 18, 26], np.float32)
rng = np.random.default_rng(5)
gfill = dark[None, None, :] + rng.normal(0, 1.8, (H, W, 1)).astype(np.float32)
res = res * (1 - gap[..., None]) + gfill * gap[..., None]

# 2b. little finger's top band: its own visible body (just below the subtitle) moved up 10 px
pz = np.zeros((H, W), np.uint8)
cv2.fillPoly(pz, [np.array([[236, 1200], [283, 1205], [300, 1212], [314, 1219], [314, 1230], [236, 1230]], np.int32)], 255)
pz = cv2.GaussianBlur(pz, (0, 0), 1.5).astype(np.float32) / 255
pp = np.zeros_like(f); pp[:-10] = f[10:]
res = res * (1 - pz[..., None]) + pp * pz[..., None]

# 3. ring finger = the middle finger shifted onto the ring finger's visible top edge and tip
DY, DX = 44, 3
patch = np.zeros_like(f)
patch[DY:, DX:] = f[:-DY, :-DX]
cap = np.zeros((H, W), np.uint8)
cv2.rectangle(cap, (232, 1146), (318, 1190), 255, -1)
cv2.circle(cap, (318, 1168), 22, 255, -1)                    # rounded tip
cap = cv2.GaussianBlur(cap, (0, 0), 1.8).astype(np.float32) / 255
res = res * (1 - cap[..., None]) + patch * cap[..., None]

# 4. real pixels everywhere except under the subtitle strokes + shadow; only inside the hand box
# smooth replacement region around the strokes (a letter-shaped cut would leave ragged finger edges)
hm = cv2.GaussianBlur(cv2.dilate(hole, K(5)), (0, 0), 2.5).astype(np.float32) / 255
hm = np.maximum(hm, (hole > 0).astype(np.float32))[..., None]
hand = f * (1 - hm) + res * hm
box = np.zeros((H, W), np.float32); box[BY0:BY1, BX0:BX1] = 1
box = cv2.GaussianBlur(box, (0, 0), 2)[..., None]
outf = cl.astype(np.float32) * (1 - box) + hand * box
cv2.imwrite(out, np.clip(outf, 0, 255).astype(np.uint8))
print("hand fixed", out, "gap colour", dark)

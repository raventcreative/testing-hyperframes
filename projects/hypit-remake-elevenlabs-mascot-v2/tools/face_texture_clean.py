"""v4 texture clean-up for the mascot (run with a Python that has opencv + numpy).

  python face_texture_clean.py <texdir_in> <mouth_uvmask.raw> <texdir_out>

texdir_in: basecolor.png / normal.png / rm.png extracted from assets/mascot3d/mascot_rigged.glb
1. Hair: the Tripo texture has light, flat, roundish "highlight" blobs painted on the hair charts
   (they read as brown/pink circles on screen). Detect them (flat L 100-150, slightly pink, mostly
   surrounded by hair, compact shape) and inpaint them from the surrounding hair.
2. Mouth: the baked open mouth (lips/teeth/tongue + cavity charts) is replaced by the surrounding
   skin tone so the procedural, lip-synced mouth sits on clean skin (no cover patch, no dark ring).
   Normal map flattened and roughness set to skin there.
"""
import sys
from pathlib import Path
import cv2
import numpy as np

src, mask_raw, dst = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
dst.mkdir(parents=True, exist_ok=True)
base = cv2.imread(str(src / "basecolor.png"))
nrm = cv2.imread(str(src / "normal.png"))
rm = cv2.imread(str(src / "rm.png"))
S = base.shape[0]

# ---------------------------------------------------------------- 1) hair blobs
lab = cv2.cvtColor(base, cv2.COLOR_BGR2LAB).astype(np.float32)
L, A, B = lab[:, :, 0], lab[:, :, 1] - 128, lab[:, :, 2] - 128
cand = ((L > 100) & (L < 150) & (A > 6) & (A < 16) & (B > 3) & (B < 13)).astype(np.uint8)
cand = cv2.morphologyEx(cand, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
hair = ((L > 45) & (L < 102) & (A > 2) & (A < 14)).astype(np.uint8)
n, lab_, st, cen = cv2.connectedComponentsWithStats(cand)
blobs = np.zeros_like(cand)
EXCL = [(1780, 0, 2048, 300), (1780, 850, 2048, 1100)]  # shirt print ("AI PRENEUR") charts
count = 0
for i in range(1, n):
    x, y, w, h, a = st[i]
    if a < 120 or a > 9000:
        continue
    cx, cy = cen[i]
    if any(x0 <= cx <= x1 and y0 <= cy <= y1 for x0, y0, x1, y1 in EXCL):
        continue
    comp = (lab_ == i).astype(np.uint8)
    ring = cv2.dilate(comp, np.ones((15, 15), np.uint8)) - comp
    if hair[ring > 0].mean() < 0.55:
        continue
    cnts, _ = cv2.findContours(comp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cnts, key=cv2.contourArea)
    area, per = cv2.contourArea(c), cv2.arcLength(c, True)
    circ = 4 * np.pi * area / (per * per) if per else 0
    (_, _), (rw, rh), _ = cv2.minAreaRect(c)
    ar = max(rw, rh) / max(1, min(rw, rh))
    if circ > 0.5 and ar < 3.2:
        blobs |= comp
        count += 1
blobs = cv2.dilate(blobs, np.ones((7, 7), np.uint8))
base = cv2.inpaint(base, blobs * 255, 9, cv2.INPAINT_TELEA)
print("hair blobs painted out:", count)

# ---------------------------------------------------------------- 2) mouth
mm = np.fromfile(mask_raw, dtype=np.uint8).reshape(S, S)
mm = cv2.morphologyEx(mm, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
inner = cv2.dilate(mm, np.ones((9, 9), np.uint8))
ring = cv2.dilate(mm, np.ones((41, 41), np.uint8)) & ~inner
lab = cv2.cvtColor(base, cv2.COLOR_BGR2LAB)
skinlike = (lab[:, :, 0] > 170) & ((lab[:, :, 1].astype(int) - 128) > 4)
sel = (ring > 0) & skinlike
skin = np.median(base[sel], axis=0) if sel.sum() > 50 else np.array([186, 207, 243])
skin_rm = np.median(rm[sel], axis=0) if sel.sum() > 50 else rm[inner > 0].mean(axis=0)
print("mouth skin BGR", skin, "ring px", int(sel.sum()))
fill = base.copy()
fill[inner > 0] = skin
# soft blend: inside fully skin, outer 8 px feathered (the feather only touches the skin ring)
alpha = cv2.GaussianBlur((inner > 0).astype(np.float32), (0, 0), 3)
alpha = np.clip(alpha * 1.6, 0, 1)[:, :, None]
base = (base * (1 - alpha) + fill * alpha).astype(np.uint8)
flat = np.zeros_like(nrm); flat[:] = (255, 128, 128)  # BGR of (128,128,255)
nrm = (nrm * (1 - alpha) + flat * alpha).astype(np.uint8)
rmf = rm.copy(); rmf[inner > 0] = skin_rm
rm = (rm * (1 - alpha) + rmf * alpha).astype(np.uint8)

cv2.imwrite(str(dst / "basecolor.png"), base)
cv2.imwrite(str(dst / "normal.png"), nrm)
cv2.imwrite(str(dst / "rm.png"), rm)
print("written", dst)

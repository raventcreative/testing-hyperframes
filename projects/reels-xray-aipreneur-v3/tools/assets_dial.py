"""Split the user's navy dial photo (assets/elements/user/dial_navy.webp) into animatable parts for S08.

The dial is a circle seen at an angle -> an ellipse in the photo. Fitted face ellipse: axes 688.9 x 798.4,
first axis at 6 deg (cv2.fitEllipse on the navy face). Affine A = R(6 deg) . diag(0.8628, 1) maps the dial's
own plane (a circle) onto the photo. Parts that must turn (needle, window gears) are re-sampled into that
circle plane ("rectified"), so CSS can rotate them inside a wrapper carrying A and they stay on the dial.

Outputs (assets/elements/xray/dial/):
  base_win.png  the gear window area of the dial with the turning gold painted dark (sits under the gears)
  plate.png     full dial, needle painted out (opencv inpaint), gear window cut out  [photo space, 1254 px]
  hub.png       the ivory hub cap (drawn over the needle)                  [photo space]
  needle.png    needle, rectified, 760 px square centred on the pivot    [circle space]
  gear_a/b/c/d.png  window gears, rectified, square crops centred on their axles
  dial.json     pivot, affine, gear centres/radii, needle angle
Run: <venv>/bin/python -I tools/assets_dial.py
"""
import json, math
from pathlib import Path
import numpy as np, cv2

P = Path(__file__).resolve().parents[1]
OUT = P / "assets/elements/xray/dial"
OUT.mkdir(parents=True, exist_ok=True)
im = cv2.imread(str(P / "assets/elements/user/dial_navy.webp"), cv2.IMREAD_UNCHANGED)
H, W = im.shape[:2]
bgr, alpha = im[..., :3].copy(), im[..., 3].copy()

PIV = np.array([739.0, 607.0])          # hub centre (needle line extended through the hub)
TH, SX = math.radians(6.0), 688.9 / 798.4
R = np.array([[math.cos(TH), -math.sin(TH)], [math.sin(TH), math.cos(TH)]])
A = R @ np.diag([SX, 1.0])              # circle plane -> photo
Ai = np.linalg.inv(A)

def aff(M, c=PIV):                       # 2x3 cv2 matrix for p' = M (p - c) + c
    t = c - M @ c
    return np.hstack([M, t[:, None]])

rect = cv2.warpAffine(np.dstack([bgr, alpha]), aff(Ai), (W, H), flags=cv2.INTER_CUBIC, borderValue=(0, 0, 0, 0))
cv2.imwrite(str(P / "tools/.dial_rect_debug.png"), rect) if False else None

# ---------------------------------------------------------------- needle (rectified)
tip = np.array([975.0, 382.0])
v = Ai @ (tip - PIV)
ang = math.degrees(math.atan2(v[1], v[0]))   # -45.x deg (screen coords, y down)
L = float(np.hypot(*v))
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
dx, dy = xx - PIV[0], yy - PIV[1]
u = np.array([math.cos(math.radians(ang)), math.sin(math.radians(ang))])
along = dx * u[0] + dy * u[1]
perp = np.abs(-dx * u[1] + dy * u[0])
hsv = cv2.cvtColor(rect[..., :3], cv2.COLOR_BGR2HSV)
bright = (hsv[..., 2] > 95) | (hsv[..., 1] < 80)
half_w = np.clip(13 - 9 * (along / L), 3.5, 13)            # tapered needle
strip = (along > 30) & (along < L + 10) & (perp < half_w + 3)
nmask = (strip & bright & (rect[..., 3] > 0)).astype(np.uint8) * 255
nmask = cv2.morphologyEx(nmask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
nmask = cv2.GaussianBlur(nmask, (3, 3), 0)
needle = rect.copy()
needle[..., 3] = (needle[..., 3].astype(np.float32) * nmask / 255).astype(np.uint8)
N = 760
needle_sq = np.zeros((N, N, 4), np.uint8)
x0, y0 = int(PIV[0] - N / 2), int(PIV[1] - N / 2)
needle_sq[:, :] = needle[y0:y0 + N, x0:x0 + N]
cv2.imwrite(str(OUT / "needle.png"), needle_sq)

# ---------------------------------------------------------------- base: needle inpainted (photo space)
shadow_strip = ((along > 40) & (along < L + 6) & (perp < half_w + 15)).astype(np.uint8) * 255
nm_photo = cv2.warpAffine(np.maximum(nmask, shadow_strip), aff(A), (W, H), flags=cv2.INTER_LINEAR)
nm_photo = (nm_photo > 20).astype(np.uint8) * 255
nm_photo = cv2.dilate(nm_photo, np.ones((5, 5), np.uint8))
hub_r = 78
hub_disc = ((xx - PIV[0]) ** 2 / (66 * SX) ** 2 + (yy - PIV[1]) ** 2 / 66 ** 2) < 1
nm_photo[hub_disc] = 0                                       # the hub stays as photographed
base = cv2.inpaint(bgr, nm_photo, 9, cv2.INPAINT_TELEA)

# hub cap sprite (ellipse in photo space, soft edge)
hub = np.zeros((H, W), np.float32)
hub_m = (((xx - PIV[0]) / (hub_r * SX)) ** 2 + ((yy - PIV[1]) / hub_r) ** 2)
hub = np.clip((1.06 - hub_m) / 0.06, 0, 1)
hx0, hy0, HS = int(PIV[0] - 100), int(PIV[1] - 100), 200
hub_img = np.dstack([bgr, (hub * 255).astype(np.uint8)])[hy0:hy0 + HS, hx0:hx0 + HS]
cv2.imwrite(str(OUT / "hub.png"), hub_img)

# ---------------------------------------------------------------- gear window (photo space eye shape)
Lt, Rt, Top, Bot = np.array([516, 834.0]), np.array([972, 802.0]), np.array([712, 700.0]), np.array([705, 932.0])
def bez(p0, c, p1, t):
    return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * c + t ** 2 * p1
cu = (Top - 0.25 * (Lt + Rt)) / 0.5
cl = (Bot - 0.25 * (Lt + Rt)) / 0.5
ts = np.linspace(0, 1, 80)[:, None]
poly_r = np.vstack([bez(Lt, cu, Rt, ts), bez(Rt, cl, Lt, ts)])
poly = ((A @ (poly_r - PIV).T).T + PIV).astype(np.int32)
win = np.zeros((H, W), np.uint8)
cv2.fillPoly(win, [poly], 255)
win = cv2.GaussianBlur(win, (5, 5), 0)
plate = np.dstack([base, (alpha.astype(np.float32) * (1 - win / 255.0)).astype(np.uint8)])
cv2.imwrite(str(OUT / "plate.png"), plate)

# ---------------------------------------------------------------- gears (rectified square crops)
GEARS = {"gear_a": ((656, 818.5), 128, True), "gear_b": ((857.5, 840), 62, False), "gear_c": ((820, 729), 50, False), "gear_d": ((927.5, 837.5), 24, True)}
meta_g = {}
hsv_r = cv2.cvtColor(rect[..., :3], cv2.COLOR_BGR2HSV)
gold = ((hsv_r[..., 0] >= 10) & (hsv_r[..., 0] <= 32) & (hsv_r[..., 1] > 70) & (hsv_r[..., 2] > 60)).astype(np.uint8) * 255
gold = cv2.GaussianBlur(cv2.morphologyEx(gold, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8)), (3, 3), 0)
gold_fill = np.zeros((H, W), np.uint8)
for name, (c, r, is_gold) in GEARS.items():
    cr = np.array(c, float)
    s = int(2 * r + 8)
    gx0, gy0 = int(round(cr[0] - s / 2)), int(round(cr[1] - s / 2))
    crop = rect[gy0:gy0 + s, gx0:gx0 + s].copy()
    yy2, xx2 = np.mgrid[0:s, 0:s]
    d = np.hypot(xx2 - s / 2, yy2 - s / 2)
    circ = np.clip((r - d) / 2.0, 0, 1)
    if is_gold:   # only the gold wheel turns; bridge, jewel and the dark gaps stay with the plate
        sect = np.ones_like(d)
        if name == "gear_a":   # leave out the lower-left sector where a second (static) gold wheel shows
            angd = np.degrees(np.arctan2(yy2 - s / 2, xx2 - s / 2)) % 360
            sect = np.clip(np.minimum(np.abs(angd - 98), np.abs(angd - 212)) / 6.0, 0, 1) * ((angd < 98) | (angd > 212)) + 0
        circ = ((circ * sect * gold[gy0:gy0 + s, gx0:gx0 + s] / 255.0) > 0.5).astype(np.float32)   # binary: sprite == hole
        fill = np.zeros((H, W), np.uint8)
        fill[gy0:gy0 + s, gx0:gx0 + s] = (circ > 0.5).astype(np.uint8) * 255
        gold_fill = np.maximum(gold_fill, fill)
    crop[..., 3] = (crop[..., 3] * circ).astype(np.uint8)
    cv2.imwrite(str(OUT / f"{name}.png"), crop)
    meta_g[name] = {"c_rect": [round(float(cr[0]), 2), round(float(cr[1]), 2)], "size": s, "r": r, "photo": list(c)}

gm = cv2.warpAffine(gold_fill, aff(A), (W, H), flags=cv2.INTER_LINEAR)
gm = (gm > 127).astype(np.uint8) * 255
dark = cv2.GaussianBlur(base, (0, 0), 6)
dark = (dark.astype(np.float32) * 0.28 + np.array([26, 24, 22])).clip(0, 255).astype(np.uint8)
base2 = base.copy(); base2[gm > 0] = dark[gm > 0]
bx0, by0 = poly[:, 0].min() - 24, poly[:, 1].min() - 24
bx1, by1 = poly[:, 0].max() + 24, poly[:, 1].max() + 24
cv2.imwrite(str(OUT / "base_win.png"), np.dstack([base2, alpha])[by0:by1, bx0:bx1])   # only the window is ever visible
(OUT / "base.png").unlink(missing_ok=True)
json.dump({"base_win_box": [int(bx0), int(by0), int(bx1 - bx0), int(by1 - by0)], "pivot": PIV.tolist(), "rot_deg": 6.0, "scale_x": SX, "needle_angle_deg": round(ang, 2), "needle_len": round(L, 1),
           "needle_sq": N, "hub_box": [hx0, hy0, HS], "gears": meta_g, "window_poly": poly.tolist()[::8]},
          open(OUT / "dial.json", "w"), indent=1)
print("needle angle", round(ang, 2), "len", round(L, 1), "needle px", int((nmask > 128).sum()), "inpaint px", int((nm_photo > 0).sum()))
for k, m in meta_g.items():
    print(k, m)

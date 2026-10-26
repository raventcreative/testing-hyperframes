"""Dissect the user's mechanical phone photo (assets/elements/user/phone_mech.webp) into animatable layers.

Outputs (assets/elements/xray/phone/):
  body.webp     the phone body only (floating glass removed, its rim line over the gears inpainted)
  gear_*.webp   circular gear sprites cut from the RECTIFIED face (so they rotate as true circles in-plane)
  phone.json    geometry: face quad, CSS matrix3d that maps face-local px -> photo px (exact homography columns
                + a unit normal), rig perspective, glass size + closed/open poses in face-local coordinates.
Method: line fits on the silhouette / navy rim give the face and glass quads; the face homography is decomposed
with K (f = 5900, principal point = image centre; the photo is near-orthographic) into a 3D plane pose, so CSS
can place a real 3D plane over the photo (rig with perspective f). The floating glass is parallel to the face,
so its open pose is a lift along the normal + a small in-plane shift (least-squares fit to the photo's glass).
Run: <venv>/bin/python -I tools/assets_phone.py <project>
"""
import json, sys
from pathlib import Path
import cv2
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
OUT = P / "assets/elements/xray/phone"; OUT.mkdir(parents=True, exist_ok=True)
im = cv2.imread(str(P / "assets/elements/user/phone_mech.webp"), cv2.IMREAD_UNCHANGED)   # BGRA
IH, IW = im.shape[:2]
A = im[..., 3]; B, G, R = (im[..., i].astype(int) for i in range(3))

# ------------------------------------------------------------------ silhouettes + quads
op = (A > 200).astype(np.uint8)
body = cv2.morphologyEx(op, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31)))
n, lab, st, _ = cv2.connectedComponentsWithStats(body)
body = (lab == 1 + np.argmax(st[1:, 4])).astype(np.uint8)
rim = ((A > 150) & (cv2.dilate(body, np.ones((5, 5), np.uint8)) == 0)).astype(np.uint8)
navy = (B > R + 25) & (B > 60) & (R < 130) & (body > 0)

def fitx(pts):
    p = np.array(pts, float); a, b = np.polyfit(p[:, 1], p[:, 0], 1); return ("x", a, b)
def fity(pts):
    p = np.array(pts, float); a, b = np.polyfit(p[:, 0], p[:, 1], 1); return ("y", a, b)
def inter(L1, L2):
    def abc(L):
        t, a, b = L
        return (1, -a, b) if t == "x" else (-a, 1, b)
    a1, b1, c1 = abc(L1); a2, b2, c2 = abc(L2); d = a1 * b2 - a2 * b1
    return [(c1 * b2 - c2 * b1) / d, (a1 * c2 - a2 * c1) / d]

fr = fitx([(np.nonzero(body[y])[0].max(), y) for y in range(380, 1060, 4)])
ft = fity([(x, np.nonzero(body[:, x])[0].min()) for x in range(150, 430, 4)])
fl = fitx([(np.nonzero(navy[y])[0].min(), y) for y in range(340, 1000, 4) if navy[y].any()])
fb = fity([(x, np.nonzero(navy[:, x])[0].max()) for x in range(620, 940, 4) if navy[:, x].any()])
FACE = [inter(ft, fl), inter(ft, fr), inter(fb, fr), inter(fb, fl)]           # tl tr br bl
gl = fitx([(np.nonzero(rim[y])[0].min(), y) for y in range(110, 240, 3) if rim[y].any()])
gt = fity([(x, np.nonzero(rim[:, x])[0].min()) for x in range(300, 540, 3) if rim[:, x].any()])
gr = fitx([(np.nonzero(rim[y])[0].max(), y) for y in range(180, 820, 3) if rim[y].any()])
gb = fity([(x, np.nonzero(rim[:, x])[0].max()) for x in range(900, 1060, 3) if rim[:, x].any()])
GLASS = [inter(gt, gl), inter(gt, gr), inter(gb, gr), inter(gb, gl)]

# ------------------------------------------------------------------ face plane pose (CSS 3D)
FW, FH = 494, 1002                       # face-local size (aspect measured 0.493)
f, cx, cy = 5900.0, IW / 2, IH / 2
K = np.array([[f, 0, cx], [0, f, cy], [0, 0, 1]])
Hf = cv2.getPerspectiveTransform(np.float32([[0, 0], [FW, 0], [FW, FH], [0, FH]]), np.float32(FACE)).astype(float)
M = np.linalg.inv(K) @ Hf
lam = (np.linalg.norm(M[:, 0]) + np.linalg.norm(M[:, 1])) / 2
r1, r2, t = M[:, 0] / lam, M[:, 1] / lam, M[:, 2] / lam
if t[2] < 0:
    r1, r2, t = -r1, -r2, -t
c1 = np.array([r1[0], r1[1], -r1[2]]); c2 = np.array([r2[0], r2[1], -r2[2]])
c3 = np.cross(c1 / np.linalg.norm(c1), c2 / np.linalg.norm(c2)); c3 /= np.linalg.norm(c3)
if c3[2] < 0:
    c3 = -c3                              # local +z = toward the viewer
T = np.array([cx + t[0], cy + t[1], f - t[2]])
M4 = np.eye(4); M4[:3, 0], M4[:3, 1], M4[:3, 2], M4[:3, 3] = c1, c2, c3, T

def proj(p):                              # rig 3D -> photo px (rig perspective f at (cx, cy))
    s = f / (f - p[2]); return np.array([cx + (p[0] - cx) * s, cy + (p[1] - cy) * s])
def local_to_photo(u, v, w=0.0):
    return proj(M4 @ np.array([u, v, w, 1.0]))
err = max(np.linalg.norm(local_to_photo(*uv) - np.array(q)) for uv, q in zip([(0, 0), (FW, 0), (FW, FH), (0, FH)], FACE))

# ------------------------------------------------------------------ glass: size + open pose (fit)
def glass_corners(p):
    x, y, h, w, hh = p
    return [local_to_photo(x, y, h), local_to_photo(x + w, y, h), local_to_photo(x + w, y + hh, h), local_to_photo(x, y + hh, h)]
LIFT = 260.0                               # lift along the normal (ambiguous in a near-ortho photo -> fixed)
p = np.array([80.0, -10.0, LIFT, 448.0, 990.0])
tgt = np.array(GLASS).ravel()
free = [0, 1, 3, 4]
for _ in range(30):                       # Gauss-Newton on x, y, w, h (8 equations)
    base = np.array(glass_corners(p)).ravel(); r = base - tgt
    J = np.zeros((8, 4))
    for j, k in enumerate(free):
        dp = np.zeros(5); dp[k] = 1e-2
        J[:, j] = (np.array(glass_corners(p + dp)).ravel() - base) / 1e-2
    step = np.linalg.lstsq(J, -r, rcond=None)[0]
    for j, k in enumerate(free):
        p[k] += step[j]
gx, gy, gh, gw, ghh = p
gerr = np.abs(np.array(glass_corners(p)).ravel() - tgt).max()
closed = [(FW - gw) / 2, (FH - ghh) / 2]

# ------------------------------------------------------------------ rectified face (2x) + rim inpaint
S = 2
Hs = Hf @ np.diag([1 / S, 1 / S, 1])
tex = cv2.warpPerspective(im, np.linalg.inv(Hs), (FW * S, FH * S), flags=cv2.INTER_CUBIC)
# rim band of the floating glass as it crosses the body (glass outline in face-local coords, z = 0 reading)
Hi = np.linalg.inv(Hf)
gloc = [(Hi @ np.array([*q, 1.0])) for q in GLASS]; gloc = [g[:2] / g[2] for g in gloc]
mask = np.zeros((FH * S, FW * S), np.uint8)
rad, IN, TH = 36 * S, 9 * S, 36 * S       # the rim band sits just inside the glass outline
lx0, ly0 = gloc[0][0] * S + IN, gloc[0][1] * S
lx1, ly1 = gloc[3][0] * S + IN, gloc[3][1] * S - IN
cv2.line(mask, (int(lx0), int(ly0)), (int(lx1), int(ly1 - rad)), 255, TH)
cv2.line(mask, (int(lx1 + rad), int(ly1)), (int(gloc[2][0] * S), int(gloc[2][1] * S - IN)), 255, TH)
cv2.ellipse(mask, (int(lx1 + rad), int(ly1 - rad)), (rad, rad), 0, 90, 180, 255, TH)
mask[:, :] = np.where(tex[..., 3] > 0, mask, 0)
bgr = tex[..., :3].copy()
fixed = cv2.inpaint(bgr, mask, 5, cv2.INPAINT_NS).astype(float)
# tone the repaired band toward the local navy so it reads as a dark channel, not a pale smear
navy_bgr = np.array([84.0, 46.0, 24.0])
lum = fixed.mean(axis=2, keepdims=True)
fixed = np.clip(fixed * 0.22 + navy_bgr * 0.78 + (lum - 120) * 0.05, 0, 255)
soft = cv2.GaussianBlur(mask, (15, 15), 0).astype(float)[..., None] / 255
tex[..., :3] = (bgr * (1 - soft) + fixed * soft).astype(np.uint8)
cv2.imwrite("/tmp/claude-0/-home-user-testing-hyperframes/20e5da73-b3b2-5061-a447-ad53371b0e44/scratchpad/ph/tex_fixed.jpg", cv2.resize(cv2.cvtColor(tex, cv2.COLOR_BGRA2BGR), (FW, FH)))

# patch the photo: warp the repaired texture back and composite inside the warped rim mask
back = cv2.warpPerspective(tex, Hs, (IW, IH), flags=cv2.INTER_CUBIC)
mback = cv2.warpPerspective(mask, Hs, (IW, IH), flags=cv2.INTER_LINEAR)
mback = cv2.GaussianBlur(cv2.dilate(mback, np.ones((3, 3), np.uint8)), (5, 5), 0).astype(float)[..., None] / 255
out = im.copy()
out[..., :3] = (im[..., :3] * (1 - mback) + back[..., :3] * mback).astype(np.uint8)
# keep only the body (drop the floating glass + its faint alpha outside the body)
keep = cv2.dilate(body, np.ones((5, 5), np.uint8))
out[..., 3] = np.where(keep > 0, im[..., 3], 0).astype(np.uint8)
ys, xs = np.nonzero(out[..., 3] > 8)
cv2.imwrite(str(OUT / "body.webp"), out, [cv2.IMWRITE_WEBP_QUALITY, 92])

# ------------------------------------------------------------------ gear sprites (face-local centre, radius)
GEARS = {"g1": (258, 311, 77), "g2": (252, 500, 80), "g3": (226, 742, 128), "g4": (126, 588, 33), "g5": (356, 712, 40)}
for name, (gxc, gyc, gr_) in GEARS.items():
    cxp, cyp, rp = gxc * S, gyc * S, gr_ * S
    crop = tex[cyp - rp: cyp + rp, cxp - rp: cxp + rp].copy()
    yy, xx = np.mgrid[0:2 * rp, 0:2 * rp]
    d = np.sqrt((xx - rp + 0.5) ** 2 + (yy - rp + 0.5) ** 2)
    a = np.clip((rp - d) / 2.5, 0, 1)
    crop[..., 3] = (crop[..., 3] * a).astype(np.uint8)
    cv2.imwrite(str(OUT / f"gear_{name}.webp"), crop, [cv2.IMWRITE_WEBP_QUALITY, 92])

meta = {
    "image": [IW, IH], "f": f, "cx": cx, "cy": cy, "face_quad": [[round(float(a), 2) for a in q] for q in FACE],
    "glass_quad": [[round(float(a), 2) for a in q] for q in GLASS], "FW": FW, "FH": FH,
    "matrix3d": [round(float(v), 6) for v in M4.T.ravel()],          # column-major for CSS
    "face_fit_err_px": round(float(err), 3),
    "glass": {"w": round(float(gw), 2), "h": round(float(ghh), 2), "closed": [round(float(closed[0]), 2), round(float(closed[1]), 2)],
              "open": [round(float(gx), 2), round(float(gy), 2), round(float(gh), 2)], "fit_err_px": round(float(gerr), 2)},
    "normal_in_photo": [round(float(c3[0]), 4), round(float(c3[1]), 4)], "col_scale": [round(float(np.linalg.norm(c1)), 4), round(float(np.linalg.norm(c2)), 4)],
    "c1": [round(float(v), 6) for v in c1], "c2": [round(float(v), 6) for v in c2], "c3": [round(float(v), 6) for v in c3],
    "gears": {k: list(v) for k, v in GEARS.items()}, "texture_scale": S,
    "body_bbox": [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())],
}
(OUT / "phone.json").write_text(json.dumps(meta, indent=1))
print("face err px", meta["face_fit_err_px"], "| glass", meta["glass"], "| body bbox", meta["body_bbox"])

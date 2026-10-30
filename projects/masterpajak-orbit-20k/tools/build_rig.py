"""Split the supplied MasterPajak mascot PNG into puppet layers (2.5D rig).

Input : assets/mascot/masterpajak_mascot_original.webp (user-supplied, already alpha-cut)
Output: assets/mascot/layer_{body,armR,armL,head}.png  (original pixels, only masked — no repaint of the logo)
        vendor/masterpajak-rig.js                    (pivots, seams, offsets for the WebGL puppet)

armR = the character's RIGHT arm (screen-left), armL = character's LEFT arm (screen-right).
The logo is never redrawn: the head layer is the original head pixels cut on its circle.
"""
import json
import numpy as np
from PIL import Image

SRC = "assets/mascot/masterpajak_mascot_original.webp"
img = np.asarray(Image.open(SRC).convert("RGBA")).astype(np.float32)
H, W = img.shape[:2]
alpha = img[..., 3] / 255.0
lum = img[..., :3].mean(2)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)

# ---------------- head circle (least squares on the silhouette) ----------------
pts = []
for y in range(110, 430):
    xs = np.where(alpha[y] > 0.5)[0]
    pts += [(xs[0], y), (xs[-1], y)]
for x in range(380, 640):
    ys = np.where(alpha[:, x] > 0.5)[0]
    pts.append((x, ys[0]))
P = np.array(pts, float)
A = np.c_[2 * P, np.ones(len(P))]
sol = np.linalg.lstsq(A, (P ** 2).sum(1), rcond=None)[0]
hcx, hcy = sol[0], sol[1]
hr = float(np.sqrt(sol[2] + hcx ** 2 + hcy ** 2))


def clip01(v):
    return np.clip(v, 0.0, 1.0)


# ---------------- arm seams ----------------
def crease_curve(lo, hi, y0, y1, side):
    """x of the arm/torso boundary per row: the dark crease while touching, the alpha gap's middle once separated."""
    xs = {}
    for y in range(y0, y1 + 1):
        row_a = alpha[y, lo:hi]
        on = row_a > 0.5
        # alpha gap inside the window?
        gap = np.where(~on)[0]
        if len(gap) and on[: gap[0]].any() and on[gap[-1]:].any():
            xs[y] = lo + (gap[0] + gap[-1]) / 2.0
        else:
            v = np.where(row_a > 0.9, lum[y, lo:hi], 1e9)
            xs[y] = lo + float(np.argmin(v))
    ys = np.array(sorted(xs))
    vals = np.array([xs[y] for y in ys])
    # smooth (moving average, 15 rows)
    k = 15
    pad = np.pad(vals, (k // 2, k // 2), mode="edge")
    sm = np.convolve(pad, np.ones(k) / k, mode="valid")
    return {int(y): float(v) for y, v in zip(ys, sm)}


def silhouette_x(y, side):
    xs = np.where(alpha[y] > 0.5)[0]
    return float(xs[0] if side < 0 else xs[-1])


rig = {"src": {"w": W, "h": H}}
YA = 655          # armpit row (crease starts)
YB = 585          # outer shoulder row where the seam meets the silhouette
Y_END = 990
masks = {}
for name, side, lo, hi in (("armR", -1, 325, 392), ("armL", 1, 632, 700)):
    cut = crease_curve(lo, hi, YA, Y_END, side)
    Ax, Ay = cut[YA], YA
    Bx, By = silhouette_x(YB, side) + (-6 if side < 0 else 6), YB
    # signed distance, positive on the arm side
    # rows >= YA: horizontal distance to the crease
    cut_arr = np.full(H, np.nan, np.float32)
    for y, v in cut.items():
        cut_arr[y] = v
    cut_arr[Y_END + 1:] = cut[Y_END]
    d_crease = (cut_arr[:, None] - xx) * (-side)  # side -1: arm where x < cut
    # rows < YA: distance to line A->B, arm side = outward/below
    nx, ny = (By - Ay), -(Bx - Ax)  # normal of AB
    nl = np.hypot(nx, ny)
    nx, ny = nx / nl, ny / nl
    # orient normal so a known arm point (outer shoulder low) is positive
    probe = (Bx + side * -0 + (-30 if side < 0 else 30) * 0, YA)  # point below B on the outer side
    probe = (silhouette_x(YA, side) - side * 20, YA - 5)
    if (probe[0] - Ax) * nx + (probe[1] - Ay) * ny < 0:
        nx, ny = -nx, -ny
    d_line = (xx - Ax) * nx + (yy - Ay) * ny
    d = np.where(yy >= YA, d_crease, d_line)
    # outside the arm's vertical span / far side of the body -> not arm
    d = np.where(yy < YB - 40, -50.0, d)
    d = np.where(yy > Y_END, -50.0, d)
    core = (d > 6) & (alpha > 0.5)
    arm_bottom = int(np.where(core.any(1))[0].max())
    d = np.where(yy > arm_bottom + 2, -50.0, d)
    masks[name] = d
    # pivot = seam midpoint pulled slightly into the arm; hand tip = lowest arm pixel
    arm_px = (d > 0) & (alpha > 0.5)
    ys_a, xs_a = np.where(arm_px)
    tip_y = int(ys_a.max())
    tip_x = float(xs_a[ys_a >= tip_y - 6].mean())
    # hinge near the outer shoulder: the top silhouette barely moves (no fold), the armpit side stretches like fabric
    px, py = Ax * 0.15 + Bx * 0.85 - side * 4, By + 30
    rig[name] = {
        "side": side,
        "A": [float(Ax), float(Ay)],
        "B": [float(Bx), float(By)],
        "n": [float(nx), float(ny)],
        "pivot": [float(px), float(py)],
        "tip": [tip_x, float(tip_y)],
        "crease": [[int(y), round(v, 2)] for y, v in sorted(cut.items()) if y % 5 == 0],
    }

# ---------------- layers ----------------
dist_head = np.sqrt((xx - hcx) ** 2 + (yy - hcy) ** 2)
FE = 1.2  # feather px

# head: original pixels inside the fitted circle (+2 px to keep the soft edge), nothing redrawn
hm = clip01((hr + 8.0 - dist_head) / FE)
head_a = alpha * hm
# body: original minus head disk (exact complement under "over": a_h + a_b(1-a_h) = a), minus arms (3 px underlap)
body_a = np.where(hm >= 0.999, 0.0, alpha * (1 - hm) / np.maximum(1 - alpha * hm, 1e-4))
for name in ("armR", "armL"):
    body_a = body_a * clip01((3.0 - masks[name]) / FE)
def keep_component(mask, seed):
    """binary flood fill from seed inside mask (numpy dilation until stable)"""
    reg = np.zeros_like(mask)
    reg[seed[1], seed[0]] = True
    while True:
        g = reg.copy()
        g[1:] |= reg[:-1]; g[:-1] |= reg[1:]; g[:, 1:] |= reg[:, :-1]; g[:, :-1] |= reg[:, 1:]
        g &= mask
        if (g == reg).all():
            return reg
        reg = g


arm_a = {}
for n in ("armR", "armL"):
    a_ = alpha * clip01(masks[n] / FE + 0.5)
    piv = rig[n]["pivot"]; tip = rig[n]["tip"]
    seed = (int((piv[0] + tip[0]) / 2), int((piv[1] + tip[1]) / 2))
    k_ = keep_component(a_ > 0.15, seed)
    for _ in range(2):
        g = k_.copy(); g[1:] |= k_[:-1]; g[:-1] |= k_[1:]; g[:, 1:] |= k_[:, :-1]; g[:, :-1] |= k_[:, 1:]; k_ = g
    arm_a[n] = np.where(k_, a_, 0.0)

# neck stub under the head (only ever visible as a sliver when the head tilts):
# copy the first neck row below the head upward inside the disk, column by column.
body_rgb = img[..., :3].copy()
y0 = int(round(hcy + hr + 10))
neck_cols = np.where(alpha[y0] > 0.02)[0]
for y in range(int(hcy + hr * 0.55), y0):
    for x in neck_cols:
        if dist_head[y, x] < hr - 2.5:
            body_rgb[y, x] = img[y0, x, :3]
            body_a[y, x] = max(body_a[y, x], alpha[y0, x])


def save(name, rgb, a):
    ys, xs = np.where(a > 0.004)
    x0, x1 = max(0, xs.min() - 4), min(W, xs.max() + 5)
    y0_, y1 = max(0, ys.min() - 4), min(H, ys.max() + 5)
    out = np.dstack([rgb, np.clip(a * 255.0 + 0.5, 0, 255)]).astype(np.uint8)[y0_:y1, x0:x1]
    Image.fromarray(out, "RGBA").save(f"assets/mascot/layer_{name}.png", optimize=True)
    return {"x": int(x0), "y": int(y0_), "w": int(x1 - x0), "h": int(y1 - y0_)}


rig["layers"] = {
    "body": save("body", body_rgb, body_a),
    "armR": save("armR", img[..., :3], arm_a["armR"]),
    "armL": save("armL", img[..., :3], arm_a["armL"]),
    "head": save("head", img[..., :3], head_a),
}
ys, xs = np.where(alpha > 0.5)
rig["bbox"] = [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]
rig["feet"] = [float((xs.min() + xs.max()) / 2), float(ys.max())]
rig["head"] = {"c": [float(hcx), float(hcy)], "r": hr, "neck": [float(hcx), float(hcy + hr - 8)]}
rig["hip"] = [float(hcx), 1000.0]
rig["waist"] = [760.0, 1000.0]  # rows where the upper-body weight fades from 1 (above) to 0 (legs)

with open("vendor/masterpajak-rig.js", "w") as f:
    f.write("// generated by tools/build_rig.py — pivots/seams of the MasterPajak puppet (source px)\n")
    f.write("window.MP_RIG = " + json.dumps(rig) + ";\n")

# QA: recomposite at rest must equal the original
comp = np.zeros((H, W, 4), np.float32)


def over(rgb, a):
    global comp
    a = a[..., None]
    comp[..., :3] = rgb * a + comp[..., :3] * (1 - a)
    comp[..., 3:] = a + comp[..., 3:] * (1 - a)


over(body_rgb, body_a)
over(img[..., :3], arm_a["armR"])
over(img[..., :3], arm_a["armL"])
over(img[..., :3], head_a)
diff_a = np.abs(comp[..., 3] - alpha).max()
m = alpha > 0.98
diff_c = np.abs(comp[..., :3][m] - img[..., :3][m]).max()
print("head", hcx, hcy, hr)
print("rest recomposite: max alpha diff %.3f, max colour diff on opaque px %.1f" % (diff_a, diff_c))


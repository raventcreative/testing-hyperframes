"""Removes the edit's burned-in overlays from frame 115.83 s of "5 level adopsi AI" (1080x1920):
  - hook box "MAU GUA BONGKAR?": rebuilt geometrically. Every pixel of the box is re-lit from the clean pixel at the box edge in
    its own column (dark ceiling above the LED strip, lit wood panels below it) times the wall's brightness profile versus the
    distance from the strip (measured on clean columns outside the box); the strip itself is redrawn from its own cross-section.
  - subtitle "bahas tentang business": LaMa (ONNX, CPU) in native-resolution 512x512 crops, generous stroke mask (outline +
    drop shadow included, else the shadow bleeds back in)
  - clideo.com watermark: LaMa
  - (f11823) the two keyword chips "BUSINESS KNOWLEDGE" / "FUNDAMENTAL THINKING" over the TV and the hair top: LaMa
Usage: python3 -I tools/clean_frame.py <frame.png> <lama_fp32.onnx> <out.png> [cfg]   cfg: f11583 (default) | f11560 | f11823"""
import sys
import cv2
import numpy as np
import onnxruntime as ort

src, model, out = sys.argv[1:4]
CFG = sys.argv[4] if len(sys.argv) > 4 else "f11583"
C = {"f11583": dict(line=(-0.1702, 403.7), sub_band=(1150, 1232, 180, 905), sub_crops=(150, 420), chips=[]),
     "f11560": dict(line=(-0.1691, 404.4), sub_band=(1115, 1265, 340, 740), sub_crops=(300,), chips=[]),
     "f11823": dict(line=(-0.2082, 446.2), sub_band=(1150, 1235, 380, 720), sub_crops=(300,),
                    chips=[(418, 545, 910, 620), (378, 653, 910, 728)])}[CFG]
im = cv2.imread(src)
H, W = im.shape[:2]
mn = im.min(axis=2)
K = lambda r: cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))

# ---------------------------------------------------------------- hook box (geometric)
f = im.astype(np.float32)
LA, LB = C["line"]                                        # LED strip centre line: y = LA*x + LB (fitted per frame)
line_y = lambda x: LA * x + LB
X0, X1, Y0, Y1 = 166, 918, 230, 368
BAND = 9
CLEAN = list(range(30, 150)) + list(range(930, 1070))
offs = np.arange(-BAND - 6, BAND + 7)
prof = np.median(np.array([[f[int(round(line_y(x) + o)), x] for o in offs] for x in CLEAN]), axis=0)
# Coons-style fill: blend, at equal offset from the strip, the clean columns just left and right of the box; then pull each
# column toward its own clean pixel at the box's top / bottom edge (top: short decay; bottom: long decay, so the vertical wood
# panel lines continue up to the strip).
XL, XR = X0 - 4, X1 + 4
def col_at(xc, d):                                        # median of 7 columns around xc, at offset d from the strip
    v = [f[int(np.clip(round(line_y(xx) + d), 0, H - 1)), xx] for xx in range(xc - 6, xc + 1)] if xc < W // 2 else \
        [f[int(np.clip(round(line_y(xx) + d), 0, H - 1)), xx] for xx in range(xc, xc + 7)]
    return np.median(np.array(v), axis=0)
def hfill(x, y):
    d = y - line_y(x)
    t = (x - XL) / (XR - XL)
    return col_at(XL, d) * (1 - t) + col_at(XR, d) * t
o = f.copy()
ctop = np.array([f[Y0 - 2, x] - hfill(x, Y0 - 2) for x in range(X0, X1)])
cbot = np.array([f[Y1 + 2, x] - hfill(x, Y1 + 2) for x in range(X0, X1)])
ctop = cv2.GaussianBlur(ctop[None], (0, 0), sigmaX=5, sigmaY=0.1)[0]
for i, x in enumerate(range(X0, X1)):
    yc = line_y(x)
    bot_above = (Y1 + 2) < yc - BAND - 2                  # strip passes below the box in this column
    for y in range(Y0, Y1):
        if y < yc - BAND - 2:
            o[y, x] = hfill(x, y) + ctop[i] * np.exp(-(y - Y0) / 16) + (cbot[i] * np.exp(-(Y1 - y) / 16) if bot_above else 0)
        elif y > yc + BAND + 2:
            o[y, x] = hfill(x, y) + cbot[i] * np.exp(-(Y1 - y) / 45)
    for k, off in enumerate(offs):
        y = int(round(yc + off))
        if Y0 <= y < Y1:
            o[y, x] = prof[k]
strip = np.zeros((H, W), bool)
for x in range(W):
    yc = line_y(x)
    strip[max(0, int(yc - BAND - 5)):int(yc + BAND + 6), x] = True
sm = cv2.GaussianBlur(o, (0, 0), sigmaX=1.4, sigmaY=2.4)            # keeps vertical panel lines, removes column noise
o = np.where(strip[..., None], o, sm)
box = np.zeros((H, W), np.float32); box[Y0:Y1, X0:X1] = 1
fb = cv2.GaussianBlur(box, (0, 0), 2.5)[..., None]
f = f * (1 - fb) + o * fb
# re-grain the rebuilt area so it matches the compressed video texture
rng = np.random.default_rng(3)
f = f + rng.normal(0, 2.2, f.shape).astype(np.float32) * fb
res = np.clip(f, 0, 255).astype(np.uint8)

# ---------------------------------------------------------------- LaMa
sess = ort.InferenceSession(model, providers=["CPUExecutionProvider"])
def lama(img, mask, x0, y0):
    c = img[y0:y0 + 512, x0:x0 + 512]
    m = mask[y0:y0 + 512, x0:x0 + 512]
    if m.max() == 0:
        return img
    mm = (m > 127).astype(np.float32)
    rgb = cv2.cvtColor(c, cv2.COLOR_BGR2RGB).astype(np.float32) / 255 * (1 - mm[..., None])
    y = sess.run(None, {"image": rgb.transpose(2, 0, 1)[None], "mask": mm[None, None]})[0][0].transpose(1, 2, 0)
    y = cv2.cvtColor(np.clip(y, 0, 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
    a = np.maximum(cv2.GaussianBlur(m, (0, 0), 1.5).astype(np.float32) / 255, mm)[..., None]
    r = img.copy()
    r[y0:y0 + 512, x0:x0 + 512] = (c * (1 - a) + y * a).astype(np.uint8)
    return r

for (cx0, cy0, cx1, cy1) in C["chips"]:                    # rounded pills (+ glow), filled in two overlapping crops
    cm = np.zeros((H, W), np.uint8)
    r = (cy1 - cy0) // 2
    cv2.rectangle(cm, (cx0 + r, cy0), (cx1 - r, cy1), 255, -1)
    cv2.circle(cm, (cx0 + r, cy0 + r), r, 255, -1); cv2.circle(cm, (cx1 - r, cy0 + r), r, 255, -1)
    cm = cv2.dilate(cm, K(8))
    for x0 in (cx0 - 60, W - 512):
        res = lama(res, cm, max(0, min(x0, W - 512)), max(0, cy0 - 240))
sub = np.zeros((H, W), np.uint8)
y0_, y1_, x0_, x1_ = C["sub_band"]
band = (slice(y0_, y1_), slice(x0_, x1_))
sub[band][mn[band] > 185] = 255
sub = cv2.dilate(sub, K(16))
for x0 in C["sub_crops"]:
    res = lama(res, sub, x0, 940)
wm = np.zeros((H, W), np.uint8)
reg = (slice(1840, 1915), slice(760, 1075))
wm[reg][mn[reg] > 120] = 255
wm = cv2.dilate(wm, K(12))
res = lama(res, wm, W - 512, H - 512)
cv2.imwrite(out, res)
print("clean", out)

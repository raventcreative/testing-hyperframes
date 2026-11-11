"""Builds assets/bg_depth.jpg (the thumbnail background) from one video frame, fully local:
1. remove the burned-in titles / subtitle / watermark (OpenCV inpaint + smooth fill), repaint the mic cube
2. Real-ESRGAN x2 over the whole frame (tiled, ONNX on CPU) -> cleans compression artifacts, adds detail
3. GFPGAN 1.4 face restoration (aligned 512 crop from 5 landmarks), blended back at FACE_W so identity stays
4. supersample back to 1080x1920 (Lanczos), navy split-tone, subtle portrait-mode depth (subject matte)
Usage: python3 -I tools/build_bg.py <frame.png> <matte.png> <models_dir> <out.jpg> [face_weight] [cfg]
cfg: "f5083" (5.08 s, hand gesture; default) or "f4667" (4.67 s, pointing at the HUMAN AGENT box)"""
import sys
import cv2
import numpy as np
import onnxruntime as ort

src, matte_p, MD, out_p = sys.argv[1:5]
FACE_W = float(sys.argv[5]) if len(sys.argv) > 5 else 0.7
CFG = sys.argv[6] if len(sys.argv) > 6 else "f5083"
im = cv2.imread(src)
H, W = im.shape[:2]

# ---------------------------------------------------------------- 1. text removal
b, g, r = [im[..., i].astype(int) for i in range(3)]
lum = (r + g + b) / 3
sat = np.max(im, axis=2).astype(int) - np.min(im, axis=2).astype(int)
def rect(x0, y0, x1, y1):
    m = np.zeros((H, W), np.uint8); m[y0:y1, x0:x1] = 255; return m
def cond(x0, y0, x1, y1, c, dil):
    m = np.zeros((H, W), np.uint8); m[y0:y1, x0:x1][c[y0:y1, x0:x1]] = 255
    return cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * dil + 1, 2 * dil + 1)))
mask = np.zeros((H, W), np.uint8)
if CFG == "f5083":
    parts = (rect(255, 262, 835, 352),                                   # "1 HUMAN AGENT" + glow
             rect(0, 682, 692, 750), cond(690, 702, 737, 748, (lum > 170) & (sat < 90), 3),   # slide title row + "SETARA 10 ORANG"
             cond(395, 1148, 495, 1230, (b > 140) & (b > r + 35), 6),    # "10" over the mic cube
             rect(486, 1150, 690, 1230),                                 # "orang" over the shirt
             rect(765, 1828, 1058, 1900))                                # watermark
    CUBE = (409, 1142, 483, 1213)
    STICK = None
    HAZE = (484, 1140, 530, 1215)
    LM = [[426.7, 896.0], [499.3, 901.7], [455.0, 946.7], [428.3, 981.7], [488.3, 982.7]]
else:   # f4667
    parts = (rect(255, 262, 835, 352),                                   # "1 HUMAN AGENT" + glow
             rect(262, 1152, 815, 1228),                                 # "itu setara dengan" band (text + dark outline)
             rect(765, 1828, 1058, 1900))
    CUBE = (430, 1137, 506, 1184)
    STICK = (451, 1184, 467, 1222)
    HAZE = None
    LM = [[485.0, 905.0], [555.0, 914.0], [516.7, 960.0], [483.3, 988.3], [540.0, 991.7]]
for m in parts:
    mask |= m
fill = cv2.inpaint(im, mask, 9, cv2.INPAINT_TELEA)
smooth = cv2.GaussianBlur(fill, (0, 0), 6)
fm = (cv2.GaussianBlur(mask, (0, 0), 2.5).astype(np.float32) / 255)[..., None]
cl = im * (1 - fm) + (fill * 0.25 + smooth * 0.75) * fm
if CFG == "f4667":
    # column-wise refill per region: inside each masked run, interpolate between the nearest clean pixels above and below
    # that belong to the SAME region (body vs screen, from a matte made on a pre-cleaned frame) -> keeps the shirt's lighting
    subj = cv2.imread(matte_p, cv2.IMREAD_UNCHANGED)[..., 3] > 127
    imf = im.astype(np.float32); out_ = cl.copy()
    ys, xs = np.nonzero(mask)
    for x in np.unique(xs):
        col = mask[:, x] > 0
        yy = np.nonzero(col)[0]
        for reg in (True, False):
            ok = (~col) & (subj[:, x] == reg)
            okidx = np.nonzero(ok)[0]
            tgt = yy[subj[yy, x] == reg]
            if len(tgt) == 0 or len(okidx) == 0: continue
            for y in tgt:
                up = okidx[okidx < y]; dn = okidx[okidx > y]
                up = up[-1] if len(up) and y - up[-1] < 90 else None
                dn = dn[0] if len(dn) and dn[0] - y < 90 else None
                if up is None and dn is None: continue
                if up is None: out_[y, x] = imf[min(dn + 2, H - 1), x]
                elif dn is None: out_[y, x] = imf[max(up - 2, 0), x]
                else:
                    t = (y - up) / (dn - up)
                    out_[y, x] = imf[max(up - 2, 0), x] * (1 - t) + imf[min(dn + 2, H - 1), x] * t
    sm2 = cv2.GaussianBlur(out_, (0, 0), sigmaX=3.0, sigmaY=1.2)
    mk = (mask > 0).astype(np.float32)[..., None]
    out_ = out_ * (1 - mk) + sm2 * mk
    fm2 = (cv2.GaussianBlur(mask, (0, 0), 1.5).astype(np.float32) / 255)[..., None]
    cl = im * (1 - fm2) + out_ * fm2
# mic cube face: clean vertical gradient sampled from its own clean top edge (+ a darker bottom)
x0, y0, x1, y1 = CUBE
if CFG == "f5083":
    top = np.median(im[y0 + 1:y0 + 4, x0 + 4:x0 + 40].reshape(-1, 3), axis=0).astype(np.float32)
    bot = np.median(im[y1 - 6:y1 - 2, x0 + 3:x0 + 22].reshape(-1, 3), axis=0).astype(np.float32)
else:   # only the cube's top strip is visible above the subtitle: take its bright silver, darken toward the bottom
    strip = im[y0 + 3:y0 + 20, x0 + 6:x1 - 6].reshape(-1, 3).astype(np.float32)
    lum_s = strip.mean(axis=1)
    top = np.median(strip[lum_s >= np.percentile(lum_s, 70)], axis=0)
    bot = top * 0.72
t = np.linspace(0, 1, y1 - y0)[:, None, None]
grad = np.repeat(top * (1 - t) + bot * t, x1 - x0, axis=1) * np.linspace(1.02, 0.95, x1 - x0)[None, :, None]
cm = np.zeros((H, W), np.float32); cm[y0:y1, x0:x1] = 1; cm = cv2.GaussianBlur(cm, (0, 0), 1.6)[..., None]
cf = cl.copy(); cf[y0:y1, x0:x1] = grad
cl = cl * (1 - cm) + cf * cm
if STICK:   # the mic handle under the cube, rebuilt from its visible lower part
    sx0, sy0, sx1, sy1 = STICK
    col = np.median(im[sy1 + 4:sy1 + 20, sx0:sx1].reshape(-1, 3), axis=0).astype(np.float32)
    prof = np.median(im[sy1 + 4:sy1 + 20, sx0:sx1].astype(np.float32), axis=0)      # left-right shading of the handle
    sm_ = np.zeros((H, W), np.float32); sm_[sy0:sy1, sx0:sx1] = 1; sm_ = cv2.GaussianBlur(sm_, (0, 0), 1.0)[..., None]
    sf = cl.copy(); sf[sy0:sy1, sx0:sx1] = prof[None, :, :]
    cl = cl * (1 - sm_) + sf * sm_
if HAZE:    # shirt right of the cube: refill with surrounding shirt colour (no light haze)
    hx0, hy0, hx1, hy1 = HAZE
    L2 = cl.mean(axis=2)
    box = np.zeros((H, W), bool); box[hy0:hy1, hx0:hx1] = True
    valid = (~box) & (L2 < 45); valid[:hy0 - 30] = False; valid[hy1 + 30:] = False; valid[:, :hx0 - 10] = False; valid[:, hx1 + 40:] = False
    num = cv2.GaussianBlur(cl * valid[..., None], (0, 0), 10); den = cv2.GaussianBlur(valid.astype(np.float32), (0, 0), 10)[..., None]
    hm = cv2.GaussianBlur((box & (L2 > 38)).astype(np.float32), (0, 0), 2.5)[..., None]
    cl = cl * (1 - hm) + (num / np.maximum(den, 1e-3)) * hm
cl = np.clip(cl, 0, 255).astype(np.uint8)

# ---------------------------------------------------------------- 2. Real-ESRGAN x2 (tiled)
sr = ort.InferenceSession(MD + "/real_esrgan_x2.onnx", providers=["CPUExecutionProvider"])
T, P = 240, 16
rgb = cv2.cvtColor(cl, cv2.COLOR_BGR2RGB).astype(np.float32) / 255
up = np.zeros((H * 2, W * 2, 3), np.float32)
for ty in range(0, H, T):
    for tx in range(0, W, T):
        ya, yb, xa, xb = max(0, ty - P), min(H, ty + T + P), max(0, tx - P), min(W, tx + T + P)
        tile = rgb[ya:yb, xa:xb].transpose(2, 0, 1)[None]
        o = sr.run(None, {"input": tile})[0][0].transpose(1, 2, 0)
        oy, ox = (ty - ya) * 2, (tx - xa) * 2
        hh, ww = min(T, H - ty) * 2, min(T, W - tx) * 2
        up[ty * 2:ty * 2 + hh, tx * 2:tx * 2 + ww] = o[oy:oy + hh, ox:ox + ww]
up = (np.clip(up, 0, 1) * 255).astype(np.uint8)
up = cv2.cvtColor(up, cv2.COLOR_RGB2BGR)
print("esrgan done", up.shape, flush=True)

# ---------------------------------------------------------------- 3. GFPGAN on the face (landmarks measured on the 1080 frame)
lm = np.array(LM, np.float32) * 2
tpl = np.array([[192.98138, 239.94708], [318.90277, 240.1936], [256.63416, 314.01935], [201.26117, 371.41043], [313.08905, 371.15118]], np.float32)
M, _ = cv2.estimateAffinePartial2D(lm, tpl, method=cv2.LMEDS)
crop = cv2.warpAffine(up, M, (512, 512), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
fr = ort.InferenceSession(MD + "/gfpgan_1.4.onnx", providers=["CPUExecutionProvider"])
x = (cv2.cvtColor(crop, cv2.COLOR_BGR2RGB).astype(np.float32) / 255 - 0.5) / 0.5
y = fr.run(None, {"input": x.transpose(2, 0, 1)[None]})[0][0].transpose(1, 2, 0)
rest = cv2.cvtColor(((np.clip(y, -1, 1) + 1) / 2 * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
# soft oval over the face only (keeps hair, sunglasses, ears from the real photo)
fmask = np.zeros((512, 512), np.float32)
cv2.ellipse(fmask, (256, 300), (176, 214), 0, 0, 360, 1, -1)
fmask = cv2.GaussianBlur(fmask, (0, 0), 22)
Mi = cv2.invertAffineTransform(M)
rest_b = cv2.warpAffine(rest, Mi, (W * 2, H * 2), flags=cv2.INTER_CUBIC)
mask_b = cv2.warpAffine(fmask, Mi, (W * 2, H * 2))[..., None] * FACE_W
up = (up * (1 - mask_b) + rest_b * mask_b).astype(np.uint8)
cv2.imwrite(out_p.replace(".jpg", "_2x.png"), up)

# ---------------------------------------------------------------- 4. supersample, grade, depth
f = cv2.resize(up, (W, H), interpolation=cv2.INTER_LANCZOS4).astype(np.float32) / 255
Lm = f.mean(axis=2, keepdims=True); sh = np.clip(1 - Lm * 1.6, 0, 1) ** 1.5
navy = np.array([0.29, 0.12, 0.04], np.float32)[None, None, :]          # BGR of a deep navy
f = f * (1 - 0.35 * sh) + navy * 0.35 * sh
f = np.clip((f - 0.5) * 1.05 + 0.5, 0, 1) * 255
a = cv2.imread(matte_p, cv2.IMREAD_UNCHANGED)[..., 3].astype(np.float32) / 255
a = cv2.GaussianBlur(a, (0, 0), 2.0)[..., None]
out = np.clip((f - 128) * 1.04 + 132, 0, 255) * a + cv2.GaussianBlur(f, (0, 0), 2.4) * 0.88 * (1 - a)
cv2.imwrite(out_p, np.clip(out, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 96])
print("done", out_p)

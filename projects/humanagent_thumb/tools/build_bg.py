"""Builds assets/bg_depth.jpg (the thumbnail background) from one video frame, fully local:
1. remove the burned-in titles / subtitle / watermark (OpenCV inpaint + smooth fill), repaint the mic cube
2. Real-ESRGAN x2 over the whole frame (tiled, ONNX on CPU) -> cleans compression artifacts, adds detail
3. GFPGAN 1.4 face restoration (aligned 512 crop from 5 landmarks), blended back at FACE_W so identity stays
4. supersample back to 1080x1920 (Lanczos), navy split-tone, subtle portrait-mode depth (subject matte)
Usage: python3 -I tools/build_bg.py <frame.png> <matte.png> <models_dir> <out.jpg> [face_weight]"""
import sys
import cv2
import numpy as np
import onnxruntime as ort

src, matte_p, MD, out_p = sys.argv[1:5]
FACE_W = float(sys.argv[5]) if len(sys.argv) > 5 else 0.7
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
for m in (rect(255, 262, 835, 352),                                   # "1 HUMAN AGENT" + glow
          rect(0, 682, 692, 750), cond(690, 702, 737, 748, (lum > 170) & (sat < 90), 3),   # slide title row + "SETARA 10 ORANG"
          cond(395, 1148, 495, 1230, (b > 140) & (b > r + 35), 6),    # "10" over the mic cube
          rect(486, 1150, 690, 1230),                                 # "orang" over the shirt
          rect(765, 1828, 1058, 1900)):                               # watermark
    mask |= m
fill = cv2.inpaint(im, mask, 9, cv2.INPAINT_TELEA)
smooth = cv2.GaussianBlur(fill, (0, 0), 6)
fm = (cv2.GaussianBlur(mask, (0, 0), 2.5).astype(np.float32) / 255)[..., None]
cl = im * (1 - fm) + (fill * 0.25 + smooth * 0.75) * fm
# mic cube face: clean vertical gradient sampled from its own clean edges
x0, y0, x1, y1 = 409, 1142, 483, 1213
top = np.median(im[y0 + 1:y0 + 4, x0 + 4:x0 + 40].reshape(-1, 3), axis=0).astype(np.float32)
bot = np.median(im[y1 - 6:y1 - 2, x0 + 3:x0 + 22].reshape(-1, 3), axis=0).astype(np.float32)
t = np.linspace(0, 1, y1 - y0)[:, None, None]
grad = np.repeat(top * (1 - t) + bot * t, x1 - x0, axis=1) * np.linspace(1.02, 0.95, x1 - x0)[None, :, None]
cm = np.zeros((H, W), np.float32); cm[y0:y1, x0:x1] = 1; cm = cv2.GaussianBlur(cm, (0, 0), 1.6)[..., None]
cf = cl.copy(); cf[y0:y1, x0:x1] = grad
cl = cl * (1 - cm) + cf * cm
# shirt right of the cube: refill with surrounding shirt colour (no light haze)
L2 = cl.mean(axis=2)
box = np.zeros((H, W), bool); box[1140:1215, 484:530] = True
valid = (~box) & (L2 < 45); valid[:1110] = False; valid[1245:] = False; valid[:, :474] = False; valid[:, 570:] = False
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
lm = np.array([[426.7, 896.0], [499.3, 901.7], [455.0, 946.7], [428.3, 981.7], [488.3, 982.7]], np.float32) * 2
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

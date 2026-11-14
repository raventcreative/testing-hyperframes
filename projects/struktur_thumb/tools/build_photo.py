"""Cover background from the client's 399x667 screenshot (Struktur Manusia + AI; copied from adopsi5_thumb): Real-ESRGAN x2 (tiled ONNX)
-> GFPGAN 1.4 on the face -> subject matte (u2net_human_seg) -> navy split-tone + subtle portrait depth -> placed on the
1080x1920 canvas with a slight zoom so the head clears the headline. Writes the background and the grid mask (grid only
behind the subject, fading out toward the bottom).
Usage: python3 -I tools/build_photo.py <photo.png> <models_dir> <u2net.onnx> <out_bg.jpg> <out_gridmask.png> [zoom] [face_w]"""
import sys
import cv2
import numpy as np
import onnxruntime as ort

src, MD, U2, out_bg, out_grid = sys.argv[1:6]
Z = float(sys.argv[6]) if len(sys.argv) > 6 else 1.12
FACE_W = float(sys.argv[7]) if len(sys.argv) > 7 else 0.7
im = cv2.imread(src)
im = cv2.copyMakeBorder(im, 0, im.shape[0] % 2, 0, im.shape[1] % 2, cv2.BORDER_REFLECT)   # the x2 model needs even sizes
h, w = im.shape[:2]
LM = [[193.5, 261.5], [213.5, 256.0], [203.0, 269.5], [200.0, 281.5], [215.0, 278.0]]   # eyes, nose tip, mouth corners

# 1. Real-ESRGAN x2
sr = ort.InferenceSession(MD + "/real_esrgan_x2.onnx", providers=["CPUExecutionProvider"])
T, P = 240, 16
rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB).astype(np.float32) / 255
up = np.zeros((h * 2, w * 2, 3), np.float32)
for ty in range(0, h, T):
    for tx in range(0, w, T):
        ya, yb, xa, xb = max(0, ty - P), min(h, ty + T + P), max(0, tx - P), min(w, tx + T + P)
        o = sr.run(None, {"input": rgb[ya:yb, xa:xb].transpose(2, 0, 1)[None]})[0][0].transpose(1, 2, 0)
        oy, ox = (ty - ya) * 2, (tx - xa) * 2
        hh, ww = min(T, h - ty) * 2, min(T, w - tx) * 2
        up[ty * 2:ty * 2 + hh, tx * 2:tx * 2 + ww] = o[oy:oy + hh, ox:ox + ww]
up = cv2.cvtColor((np.clip(up, 0, 1) * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
H2, W2 = up.shape[:2]
print("esrgan done", up.shape, flush=True)

# 2. GFPGAN on the face
lm = np.array(LM, np.float32) * 2
tpl = np.array([[192.98138, 239.94708], [318.90277, 240.1936], [256.63416, 314.01935], [201.26117, 371.41043], [313.08905, 371.15118]], np.float32)
M, _ = cv2.estimateAffinePartial2D(lm, tpl, method=cv2.LMEDS)
crop = cv2.warpAffine(up, M, (512, 512), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
fr = ort.InferenceSession(MD + "/gfpgan_1.4.onnx", providers=["CPUExecutionProvider"])
x = (cv2.cvtColor(crop, cv2.COLOR_BGR2RGB).astype(np.float32) / 255 - 0.5) / 0.5
y = fr.run(None, {"input": x.transpose(2, 0, 1)[None]})[0][0].transpose(1, 2, 0)
rest = cv2.cvtColor(((np.clip(y, -1, 1) + 1) / 2 * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
fmask = np.zeros((512, 512), np.float32)
cv2.ellipse(fmask, (256, 300), (176, 214), 0, 0, 360, 1, -1)
fmask = cv2.GaussianBlur(fmask, (0, 0), 22)
Mi = cv2.invertAffineTransform(M)
rest_b = cv2.warpAffine(rest, Mi, (W2, H2), flags=cv2.INTER_CUBIC)
mask_b = cv2.warpAffine(fmask, Mi, (W2, H2))[..., None] * FACE_W
up = (up * (1 - mask_b) + rest_b * mask_b).astype(np.uint8)
print("gfpgan done", flush=True)

# 3. matte on the upscaled photo
s = ort.InferenceSession(U2, providers=["CPUExecutionProvider"])
xm = cv2.resize(cv2.cvtColor(up, cv2.COLOR_BGR2RGB), (320, 320), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
xm = (xm / xm.max() - np.array([0.485, 0.456, 0.406])) / np.array([0.229, 0.224, 0.225])
am = s.run(None, {s.get_inputs()[0].name: xm.transpose(2, 0, 1)[None].astype(np.float32)})[0][0, 0]
am = (am - am.min()) / (am.max() - am.min() + 1e-9)
a = cv2.resize(am, (W2, H2), interpolation=cv2.INTER_CUBIC)
try:
    a = cv2.ximgproc.guidedFilter(up, a.astype(np.float32), 8, 1e-3)
except Exception:
    a = cv2.bilateralFilter(a.astype(np.float32), 9, 0.2, 7)
a = np.clip((a - 0.25) / 0.5, 0, 1).astype(np.float32)

# 4. place on the canvas (1080x1920): canvas px per photo px = (1920/h) * Z, face centred
CW, CH = 1080, 1920
sc = CH / h * Z                                   # per original-photo px
k = sc / 2                                        # per upscaled px
ox = 540 - 205 * sc
oy = 765 - 228 * sc                               # head top (photo y~228) at canvas y~765
A = np.array([[k, 0, ox], [0, k, oy]], np.float32)
img = cv2.warpAffine(up, A, (CW, CH), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT).astype(np.float32) / 255
al = cv2.warpAffine(a, A, (CW, CH), flags=cv2.INTER_LINEAR)
# subject sharpening (gentle) + navy split-tone + portrait depth, as in the other covers
Lm = img.mean(axis=2, keepdims=True); sh = np.clip(1 - Lm * 1.6, 0, 1) ** 1.5
navy = np.array([0.29, 0.12, 0.04], np.float32)[None, None, :]
img = img * (1 - 0.35 * sh) + navy * 0.35 * sh
img = np.clip((img - 0.5) * 1.05 + 0.5, 0, 1) * 255
ab = cv2.GaussianBlur(al, (0, 0), 2.0)[..., None]
subj = np.clip((img - 128) * 1.04 + 132, 0, 255)
subj = np.clip(subj + 0.35 * (subj - cv2.GaussianBlur(subj, (0, 0), 1.6)), 0, 255)
out = subj * ab + cv2.GaussianBlur(img, (0, 0), 2.4) * 0.88 * (1 - ab)
cv2.imwrite(out_bg, np.clip(out, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 96])
amk = cv2.dilate(cv2.GaussianBlur(al, (0, 0), 2.0), np.ones((7, 7), np.uint8))
fade = np.clip((1650 - np.arange(CH)) / 500, 0, 1)[:, None]
g = (1 - amk) * fade
cv2.imwrite(out_grid, np.dstack([np.full((CH, CW, 3), 255, np.uint8), (np.clip(g, 0, 1) * 255).astype(np.uint8)]))
print("done", out_bg, "scale %.3f" % sc)

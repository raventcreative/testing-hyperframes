"""Testimonial cover background (white theme) from the client's 410x733 screenshot.
1. LaMa removes the burned-in caption "YANG BETUL-BETUL" and the "AIPRENEUR" watermark (inpainted at native size, image
   reflect-padded to the model's 512 px).
2. Real-ESRGAN x2 -> GFPGAN 1.4 on the face (blended) -> Real-ESRGAN x2 again (=> 4x).
3. u2net_human_seg matte -> placed on the 1080x1920 canvas (head lowered so the headline sits above it), background lifted
   toward white (high-key) so the white gradients blend in; subject kept natural with a gentle sharpen.
Writes the background JPG, the grid mask (grid only behind the subject) and the cleaned 4x source.
Usage: python3 -I tools/build_testi.py <screenshot.png> <models_dir> <u2net.onnx> <out_bg.jpg> <out_gridmask.png> <out_clean4x.png> [scale] [head_y]"""
import sys
import cv2
import numpy as np
import onnxruntime as ort

src, MD, U2, out_bg, out_grid, out_clean = sys.argv[1:7]
SC = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0       # extra zoom on top of "fit width"
HEAD_Y = float(sys.argv[8]) if len(sys.argv) > 8 else 560   # canvas y of the glasses' top (photo y ~115)
im = cv2.imread(src, cv2.IMREAD_UNCHANGED)
if im.shape[2] == 4:
    im = im[..., :3]
H0, W0 = im.shape[:2]
K = lambda r: cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))

# ---------------------------------------------------------------- 1. LaMa at native size
mn = im.min(axis=2)
mask = np.zeros((H0, W0), np.uint8)
cap = (slice(449, 482), slice(84, 330))                     # caption band
mask[cap][mn[cap] > 150] = 255
mask = cv2.dilate(mask, K(4))
cv2.rectangle(mask, (156, 38), (257, 61), 255, -1)          # watermark (blue "AI" + white "PRENEUR"), whole box
mask = cv2.dilate(mask, K(2))
sess = ort.InferenceSession(MD + "/lama_fp32.onnx", providers=["CPUExecutionProvider"])
pad = 512 - W0
padded = cv2.copyMakeBorder(im, 0, 0, 0, pad, cv2.BORDER_REFLECT)
pmask = cv2.copyMakeBorder(mask, 0, 0, 0, pad, cv2.BORDER_CONSTANT, value=0)
def lama(img, m, y0):
    c, mm = img[y0:y0 + 512], (m[y0:y0 + 512] > 127).astype(np.float32)
    rgb = cv2.cvtColor(c, cv2.COLOR_BGR2RGB).astype(np.float32) / 255 * (1 - mm[..., None])
    y = sess.run(None, {"image": rgb.transpose(2, 0, 1)[None], "mask": mm[None, None]})[0][0].transpose(1, 2, 0)
    y = cv2.cvtColor(np.clip(y, 0, 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
    a = np.maximum(cv2.GaussianBlur(m[y0:y0 + 512], (0, 0), 1.2).astype(np.float32) / 255, mm)[..., None]
    r = img.copy(); r[y0:y0 + 512] = (c * (1 - a) + y * a).astype(np.uint8)
    return r
padded = lama(padded, pmask, 0)                             # top window: watermark
padded = lama(padded, pmask, H0 - 512)                      # bottom window: caption
clean = padded[:, :W0]
print("lama done", flush=True)

# ---------------------------------------------------------------- 2. upscale + face
sr = ort.InferenceSession(MD + "/real_esrgan_x2.onnx", providers=["CPUExecutionProvider"])
def esrgan(img):
    img = cv2.copyMakeBorder(img, 0, img.shape[0] % 2, 0, img.shape[1] % 2, cv2.BORDER_REFLECT)
    h, w = img.shape[:2]; T, P = 240, 16
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float32) / 255
    up = np.zeros((h * 2, w * 2, 3), np.float32)
    for ty in range(0, h, T):
        for tx in range(0, w, T):
            ya, yb, xa, xb = max(0, ty - P), min(h, ty + T + P), max(0, tx - P), min(w, tx + T + P)
            o = sr.run(None, {"input": rgb[ya:yb, xa:xb].transpose(2, 0, 1)[None]})[0][0].transpose(1, 2, 0)
            oy, ox = (ty - ya) * 2, (tx - xa) * 2
            hh, ww = min(T, h - ty) * 2, min(T, w - tx) * 2
            up[ty * 2:ty * 2 + hh, tx * 2:tx * 2 + ww] = o[oy:oy + hh, ox:ox + ww]
    return cv2.cvtColor((np.clip(up, 0, 1) * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
up = esrgan(clean)
LM = np.array([[175.0, 213.8], [241.3, 214.5], [205.0, 248.8], [181.3, 283.8], [226.3, 285.0]], np.float32) * 2
tpl = np.array([[192.98138, 239.94708], [318.90277, 240.1936], [256.63416, 314.01935], [201.26117, 371.41043], [313.08905, 371.15118]], np.float32)
M, _ = cv2.estimateAffinePartial2D(LM, tpl, method=cv2.LMEDS)
crop = cv2.warpAffine(up, M, (512, 512), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
fr = ort.InferenceSession(MD + "/gfpgan_1.4.onnx", providers=["CPUExecutionProvider"])
x = (cv2.cvtColor(crop, cv2.COLOR_BGR2RGB).astype(np.float32) / 255 - 0.5) / 0.5
y = fr.run(None, {"input": x.transpose(2, 0, 1)[None]})[0][0].transpose(1, 2, 0)
rest = cv2.cvtColor(((np.clip(y, -1, 1) + 1) / 2 * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
fmask = np.zeros((512, 512), np.float32)
cv2.ellipse(fmask, (256, 300), (170, 205), 0, 0, 360, 1, -1)
fmask = cv2.GaussianBlur(fmask, (0, 0), 22)
H2, W2 = up.shape[:2]
Mi = cv2.invertAffineTransform(M)
rest_b = cv2.warpAffine(rest, Mi, (W2, H2), flags=cv2.INTER_CUBIC)
mask_b = cv2.warpAffine(fmask, Mi, (W2, H2))[..., None] * 0.62
up = (up * (1 - mask_b) + rest_b * mask_b).astype(np.uint8)
cv2.imwrite(out_clean.replace(".png", "_face2x.png"), crop)
up = esrgan(up)
cv2.imwrite(out_clean, up)
H4, W4 = up.shape[:2]
print("upscale done", up.shape, flush=True)

# ---------------------------------------------------------------- 3. matte + canvas
s = ort.InferenceSession(U2, providers=["CPUExecutionProvider"])
xm = cv2.resize(cv2.cvtColor(up, cv2.COLOR_BGR2RGB), (320, 320), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
xm = (xm / xm.max() - np.array([0.485, 0.456, 0.406])) / np.array([0.229, 0.224, 0.225])
am = s.run(None, {s.get_inputs()[0].name: xm.transpose(2, 0, 1)[None].astype(np.float32)})[0][0, 0]
am = (am - am.min()) / (am.max() - am.min() + 1e-9)
a = cv2.resize(am, (W4, H4), interpolation=cv2.INTER_CUBIC)
a = cv2.bilateralFilter(a.astype(np.float32), 9, 0.2, 7)
a = np.clip((a - 0.25) / 0.5, 0, 1).astype(np.float32)
CW, CH = 1080, 1920
k = CW / W4 * SC                                            # canvas px per 4x px
ox = 540 - (W4 / 2) * k
oy = HEAD_Y - 115 * 4 * k
A = np.array([[k, 0, ox], [0, k, oy]], np.float32)
img = cv2.warpAffine(up, A, (CW, CH), flags=cv2.INTER_AREA, borderMode=cv2.BORDER_REPLICATE).astype(np.float32)
al = cv2.warpAffine(a, A, (CW, CH), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
ab = cv2.GaussianBlur(al, (0, 0), 2.0)[..., None]
subj = np.clip(img + 0.30 * (img - cv2.GaussianBlur(img, (0, 0), 1.4)), 0, 255)
subj = np.clip((subj - 128) * 1.05 + 131, 0, 255)
bgd = cv2.GaussianBlur(img, (0, 0), 3.0)
bgd = bgd * 0.72 + 255 * 0.28                               # high-key: lift the room toward white
out = subj * ab + bgd * (1 - ab)
cv2.imwrite(out_bg, np.clip(out, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 96])
amk = cv2.dilate(cv2.GaussianBlur(al, (0, 0), 2.0), np.ones((7, 7), np.uint8))
fade = np.clip((1650 - np.arange(CH)) / 500, 0, 1)[:, None]
g = (1 - amk) * fade
cv2.imwrite(out_grid, np.dstack([np.full((CH, CW, 3), 255, np.uint8), (np.clip(g, 0, 1) * 255).astype(np.uint8)]))
print("done", out_bg, "k=%.4f oy=%.1f" % (k, oy))

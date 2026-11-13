"""Step 3 of build_testi.py only (matte + canvas), from the cleaned 4x source after manual touch-ups.
Usage: python3 -I tools/canvas_testi.py <clean4x.png> <u2net.onnx> <out_bg.jpg> <out_gridmask.png> [scale] [head_y]"""
import sys
import cv2
import numpy as np
import onnxruntime as ort
src, U2, out_bg, out_grid = sys.argv[1:5]
SC = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
HEAD_Y = float(sys.argv[6]) if len(sys.argv) > 6 else 560
up = cv2.imread(src)
H4, W4 = up.shape[:2]
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

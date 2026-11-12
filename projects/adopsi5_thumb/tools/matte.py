"""Subject matte (u2net_human_seg, ONNX) for the cleaned frame -> RGBA png whose alpha is the person (+ mic).
Usage: python3 -I tools/matte.py <clean.png> <u2net_human_seg.onnx> <out_matte.png>"""
import sys
import cv2
import numpy as np
import onnxruntime as ort
src, model, out = sys.argv[1:4]
im = cv2.imread(src); H, W = im.shape[:2]
s = ort.InferenceSession(model, providers=["CPUExecutionProvider"])
x = cv2.resize(cv2.cvtColor(im, cv2.COLOR_BGR2RGB), (320, 320), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
x = (x / x.max() - np.array([0.485, 0.456, 0.406])) / np.array([0.229, 0.224, 0.225])
y = s.run(None, {s.get_inputs()[0].name: x.transpose(2, 0, 1)[None].astype(np.float32)})[0][0, 0]
y = (y - y.min()) / (y.max() - y.min() + 1e-9)
a = cv2.resize(y, (W, H), interpolation=cv2.INTER_CUBIC)
# refine the upscaled edge against the full-res frame (guided filter if available, else a light bilateral)
try:
    a = cv2.ximgproc.guidedFilter(im, a.astype(np.float32), 8, 1e-3)
except Exception:
    a = cv2.bilateralFilter(a.astype(np.float32), 9, 0.2, 7)
a = np.clip((a - 0.25) / 0.5, 0, 1)
rgba = np.dstack([im, (a * 255).astype(np.uint8)])
cv2.imwrite(out, rgba)
print("matte", out, a.mean())

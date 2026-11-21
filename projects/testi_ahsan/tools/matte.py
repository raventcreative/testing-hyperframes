"""Person matte for the Ahsan photo with u2net_human_seg (no client cut-out this time) -> source/matte.png (photo size)."""
import cv2, numpy as np, onnxruntime as ort, sys
M = "/root/.cache/hyperframes/background-removal/models/u2net_human_seg.onnx"
im = cv2.imread("source/foto.webp"); H, W = im.shape[:2]
x = cv2.resize(cv2.cvtColor(im, cv2.COLOR_BGR2RGB), (320, 320), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
x = (x - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
s = ort.InferenceSession(M, providers=["CPUExecutionProvider"])
o = s.run(None, {s.get_inputs()[0].name: x.transpose(2, 0, 1)[None].astype(np.float32)})[0][0, 0]
o = (o - o.min()) / (o.max() - o.min() + 1e-6)
m = cv2.resize(o, (W, H), interpolation=cv2.INTER_CUBIC)
# refine with a guided-style edge snap: joint bilateral on the photo
g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255
m = np.clip((m - 0.35) / 0.3, 0, 1)
try:
    m = cv2.ximgproc.guidedFilter(g, m.astype(np.float32), 6, 1e-3)
except AttributeError:
    m = cv2.GaussianBlur(m, (0, 0), 1.2)
m = cv2.erode(np.clip(m, 0, 1).astype(np.float32), np.ones((5, 5), np.uint8))  # pull the edge in ~2 px: no lifted-background halo on the hair
cv2.imwrite("source/matte.png", (np.clip(m, 0, 1) * 255).astype(np.uint8)); print("ok", W, H)

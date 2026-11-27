"""White-theme cover background from the event photo: subject matte (u2net_human_seg), person brightened, room softened +
lifted toward white, placed on 1080x1920 with the head at y~700 (headline above). Writes assets/bg.jpg + assets/gridmask.png.
Usage: python3 -I tools/build_bg.py source/photo.jpg /root/.cache/hyperframes/background-removal/models/u2net_human_seg.onnx"""
import sys, cv2, numpy as np, onnxruntime as ort
src, U2 = sys.argv[1:3]
im = cv2.imread(src); h, w = im.shape[:2]
s = ort.InferenceSession(U2, providers=["CPUExecutionProvider"])
x = cv2.resize(cv2.cvtColor(im, cv2.COLOR_BGR2RGB), (320, 320), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
x = (x / x.max() - np.array([0.485, 0.456, 0.406])) / np.array([0.229, 0.224, 0.225])
m = s.run(None, {s.get_inputs()[0].name: x.transpose(2, 0, 1)[None].astype(np.float32)})[0][0, 0]
m = (m - m.min()) / (m.max() - m.min() + 1e-9)
a = cv2.resize(m, (w, h), interpolation=cv2.INTER_CUBIC)
a = np.clip((a - 0.12) / 0.3, 0, 1).astype(np.float32)
a = cv2.GaussianBlur(cv2.dilate(a, np.ones((15, 15), np.uint8)), (0, 0), 12)          # soft: only steers the brightening, never cuts
# keep only the presenter (largest blob near the centre)
n, l, st, _ = cv2.connectedComponentsWithStats((a > 0.5).astype(np.uint8))
keep = 1 + int(np.argmax(st[1:, 4])); a = a * cv2.dilate((l == keep).astype(np.float32), np.ones((25, 25), np.uint8))
f = im.astype(np.float32) / 255
# person: lift shadows/midtones, gentle warmth, local contrast
p = np.power(f, 0.78) * 1.06; p = np.clip(p + 0.25 * (p - cv2.GaussianBlur(p, (0, 0), 2.0)), 0, 1)
# room: brighter, softer, slightly desaturated so the white theme reads clean
r = f.copy(); g = r.mean(axis=2, keepdims=True); r = g + (r - g) * 0.8                   # room: no blur (no cut-out look)
r = np.clip(np.power(r, 0.75) * 1.06, 0, 1) * 0.88 + 0.12
A = a[..., None]; out = p * A + r * (1 - A)
CW, CH, SC, HX, HY, HEAD = 1080, 1920, 1.62, 985, 230, 690
M = np.float32([[SC, 0, 540 - HX * SC], [0, SC, HEAD - HY * SC]])
plate = cv2.resize(cv2.imread("assets/bg-light.png"), (CW, CH), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255
img = cv2.warpAffine(out, M, (CW, CH), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_CONSTANT, borderValue=(1, 1, 1))
cov = cv2.warpAffine(np.ones((h, w), np.float32), M, (CW, CH), borderValue=0)[..., None]
img = img * cov + plate * (1 - cov)
al = cv2.warpAffine(a, M, (CW, CH))
cv2.imwrite("assets/bg.jpg", np.clip(img * 255, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 96])
amk = cv2.dilate(cv2.GaussianBlur(al, (0, 0), 2.0), np.ones((7, 7), np.uint8))
fade = np.clip((1650 - np.arange(CH)) / 500, 0, 1)[:, None]
cv2.imwrite("assets/gridmask.png", np.dstack([np.full((CH, CW, 3), 255, np.uint8), (np.clip((1 - amk) * fade, 0, 1) * 255).astype(np.uint8)]))
print("done")

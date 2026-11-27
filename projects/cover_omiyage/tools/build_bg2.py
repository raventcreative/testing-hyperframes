"""Room background (person removed with LaMa) + the client's clean cutout placed exactly where he stood.
Usage: python3 -I tools/build_bg2.py <lama_fp32.onnx> <u2net_human_seg.onnx>"""
import sys, cv2, numpy as np, onnxruntime as ort
from PIL import Image
LAMA, U2 = sys.argv[1:3]
ph = cv2.imread("source/photo.jpg"); H0, W0 = ph.shape[:2]
cu = np.array(Image.open("source/cutout.webp").convert("RGBA")).astype(np.float32) / 255
M = np.load("source/cut2photo.npy")                                   # cutout -> photo (SIFT)
# person mask in the photo: u2net matte + the aligned cutout, generously dilated
s = ort.InferenceSession(U2, providers=["CPUExecutionProvider"])
x = cv2.resize(cv2.cvtColor(ph, cv2.COLOR_BGR2RGB), (320, 320), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
x = (x / x.max() - np.array([0.485, 0.456, 0.406])) / np.array([0.229, 0.224, 0.225])
m = s.run(None, {s.get_inputs()[0].name: x.transpose(2, 0, 1)[None].astype(np.float32)})[0][0, 0]
m = cv2.resize((m - m.min()) / (m.max() - m.min() + 1e-9), (W0, H0))
n, l, st, _ = cv2.connectedComponentsWithStats((m > 0.3).astype(np.uint8)); m = (l == 1 + int(np.argmax(st[1:, 4]))).astype(np.uint8)
ca = cv2.warpAffine(cu[..., 3], M.astype(np.float32), (W0, H0))
mask = cv2.dilate(((m > 0) | (ca > 0.1)).astype(np.uint8) * 255, np.ones((31, 31), np.uint8))
for dy in range(10, 130, 10): mask[:-dy] = np.maximum(mask[:-dy], mask[dy:])          # also clear the original head/hair sitting above the cutout
# LaMa on a square crop around the person, at 512
ys, xs = np.nonzero(mask); cx, cy = (xs.min() + xs.max()) // 2, (ys.min() + ys.max()) // 2
S = min(int(max(xs.max() - xs.min(), ys.max() - ys.min()) * 1.15), H0, W0); x0 = int(np.clip(cx - S // 2, 0, W0 - S)); y0 = int(np.clip(cy - S // 2, 0, H0 - S))
crop = ph[y0:y0 + S, x0:x0 + S]; mc = mask[y0:y0 + S, x0:x0 + S]
c5 = cv2.resize(crop, (512, 512), interpolation=cv2.INTER_AREA); m5 = (cv2.resize(mc, (512, 512)) > 127).astype(np.float32)
sess = ort.InferenceSession(LAMA, providers=["CPUExecutionProvider"])
rgb = cv2.cvtColor(c5, cv2.COLOR_BGR2RGB).astype(np.float32) / 255 * (1 - m5[..., None])
y = sess.run(None, {"image": rgb.transpose(2, 0, 1)[None], "mask": m5[None, None]})[0][0].transpose(1, 2, 0)
y = cv2.resize(cv2.cvtColor(np.clip(y, 0, 255).astype(np.uint8), cv2.COLOR_RGB2BGR), (S, S), interpolation=cv2.INTER_CUBIC)
a = cv2.GaussianBlur(mc, (0, 0), 4).astype(np.float32)[..., None] / 255
room = ph.copy(); room[y0:y0 + S, x0:x0 + S] = (crop * (1 - a) + y * a).astype(np.uint8)
cv2.imwrite("source/room_clean.jpg", room)
# room look: brighter, a touch desaturated, soft depth blur
r = room.astype(np.float32) / 255; g = r.mean(axis=2, keepdims=True); r = g + (r - g) * 0.8
r = np.clip(np.power(r, 0.75) * 1.06, 0, 1) * 0.88 + 0.12
r = cv2.GaussianBlur(r, (0, 0), 2.6)
navy = np.array([0x4f, 0x28, 0x13], np.float32)[None, None, :] / 255           # #13284f (BGR)
r = r * 0.42 + navy * 0.58 * (0.55 + 0.45 * r.mean(axis=2, keepdims=True))    # navy grade, room recedes
# canvas: same framing as before (photo head at y~690)
CW, CH, SC, HX, HY, HEAD = 1080, 1920, 1.75, 727, 792, 650
A = np.float32([[SC, 0, 540 - HX * SC], [0, SC, HEAD - HY * SC]])
plate = cv2.resize(cv2.imread("assets/plate_navy.png"), (CW, CH)).astype(np.float32) / 255
img = cv2.warpAffine(r, A, (CW, CH), flags=cv2.INTER_LANCZOS4, borderValue=(1, 1, 1))
cov = cv2.warpAffine(np.ones((H0, W0), np.float32), A, (CW, CH)); top = int(np.argmax(cov[:, 540] > 0.5))
cov = (cov * np.clip((np.arange(CH)[:, None] - top) / 260, 0, 1))[..., None]; img = img * cov + plate * (1 - cov)   # feathered top edge
cv2.imwrite("assets/room.jpg", np.clip(img * 255, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 96])
# person layer: cutout -> photo -> canvas, brightened
A3 = np.vstack([A, [0, 0, 1]]) @ np.vstack([M, [0, 0, 1]])
p = np.power(cu[..., :3], 0.85) * 1.04; p = np.clip(p + 0.22 * (p - cv2.GaussianBlur(p, (0, 0), 1.6)), 0, 1)
P = cv2.warpAffine(np.dstack([p, cu[..., 3]]), A3[:2].astype(np.float32), (CW, CH), flags=cv2.INTER_LANCZOS4)
Image.fromarray((np.clip(P, 0, 1) * 255).astype(np.uint8)).save("assets/person_c.png")
amk = cv2.dilate(cv2.GaussianBlur(P[..., 3], (0, 0), 2.0), np.ones((7, 7), np.uint8))
fade = np.clip((1650 - np.arange(CH)) / 500, 0, 1)[:, None]
cv2.imwrite("assets/gridmask3.png", np.dstack([np.full((CH, CW, 3), 255, np.uint8), (np.clip((1 - amk) * fade, 0, 1) * 255).astype(np.uint8)]))
print("crop", x0, y0, S, "person scale", round(float(np.sqrt(abs(np.linalg.det(A3[:2, :2])))), 3))

"""HD background for the cover, fully local: Real-ESRGAN x2 (tiled ONNX) -> GFPGAN 1.4 on the face (5 landmarks measured on the
1080 frame, blended back at FACE_W so identity stays) -> Lanczos back to 1080x1920 -> navy split-tone + subtle portrait depth
(subject matte) -> shifted down SHIFT px (top filled from the dark ceiling) so the head clears the headline.
Also writes the grid mask (grid only behind the subject, fading out toward the bottom).
Usage: python3 -I tools/enhance.py <clean.png> <matte.png> <models_dir> <out.jpg> <gridmask.png> [face_weight] [shift] [landmarks]
landmarks: "x,y;x,y;x,y;x,y;x,y" (eyes L/R, nose tip, mouth corners L/R on the 1080 frame); default = frame 115.83"""
import sys
import cv2
import numpy as np
import onnxruntime as ort
src, matte_p, MD, out_p, grid_p = sys.argv[1:6]
FACE_W = float(sys.argv[6]) if len(sys.argv) > 6 else 0.6
SHIFT = int(sys.argv[7]) if len(sys.argv) > 7 else 150
cl = cv2.imread(src); H, W = cl.shape[:2]
LM = [[405.0, 781.7], [490.0, 770.0], [441.7, 826.7], [424.3, 875.7], [486.0, 869.3]]
if len(sys.argv) > 8:
    LM = [[float(v) for v in pt.split(",")] for pt in sys.argv[8].split(";")]

sr = ort.InferenceSession(MD + "/real_esrgan_x2.onnx", providers=["CPUExecutionProvider"])
T, P = 240, 16
rgb = cv2.cvtColor(cl, cv2.COLOR_BGR2RGB).astype(np.float32) / 255
up = np.zeros((H * 2, W * 2, 3), np.float32)
for ty in range(0, H, T):
    for tx in range(0, W, T):
        ya, yb, xa, xb = max(0, ty - P), min(H, ty + T + P), max(0, tx - P), min(W, tx + T + P)
        o = sr.run(None, {"input": rgb[ya:yb, xa:xb].transpose(2, 0, 1)[None]})[0][0].transpose(1, 2, 0)
        oy, ox = (ty - ya) * 2, (tx - xa) * 2
        hh, ww = min(T, H - ty) * 2, min(T, W - tx) * 2
        up[ty * 2:ty * 2 + hh, tx * 2:tx * 2 + ww] = o[oy:oy + hh, ox:ox + ww]
up = cv2.cvtColor((np.clip(up, 0, 1) * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
print("esrgan done", flush=True)

lm = np.array(LM, np.float32) * 2
tpl = np.array([[192.98138, 239.94708], [318.90277, 240.1936], [256.63416, 314.01935], [201.26117, 371.41043], [313.08905, 371.15118]], np.float32)
M, _ = cv2.estimateAffinePartial2D(lm, tpl, method=cv2.LMEDS)
crop = cv2.warpAffine(up, M, (512, 512), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
fr = ort.InferenceSession(MD + "/gfpgan_1.4.onnx", providers=["CPUExecutionProvider"])
x = (cv2.cvtColor(crop, cv2.COLOR_BGR2RGB).astype(np.float32) / 255 - 0.5) / 0.5
y = fr.run(None, {"input": x.transpose(2, 0, 1)[None]})[0][0].transpose(1, 2, 0)
rest = cv2.cvtColor(((np.clip(y, -1, 1) + 1) / 2 * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
cv2.imwrite(out_p.replace(".jpg", "_facecrop.png"), np.hstack([crop, rest]))
fmask = np.zeros((512, 512), np.float32)
cv2.ellipse(fmask, (256, 300), (176, 214), 0, 0, 360, 1, -1)
fmask = cv2.GaussianBlur(fmask, (0, 0), 22)
Mi = cv2.invertAffineTransform(M)
rest_b = cv2.warpAffine(rest, Mi, (W * 2, H * 2), flags=cv2.INTER_CUBIC)
mask_b = cv2.warpAffine(fmask, Mi, (W * 2, H * 2))[..., None] * FACE_W
up = (up * (1 - mask_b) + rest_b * mask_b).astype(np.uint8)

f = cv2.resize(up, (W, H), interpolation=cv2.INTER_LANCZOS4).astype(np.float32) / 255
Lm = f.mean(axis=2, keepdims=True); sh = np.clip(1 - Lm * 1.6, 0, 1) ** 1.5
navy = np.array([0.29, 0.12, 0.04], np.float32)[None, None, :]
f = f * (1 - 0.35 * sh) + navy * 0.35 * sh
f = np.clip((f - 0.5) * 1.05 + 0.5, 0, 1) * 255
a = cv2.imread(matte_p, cv2.IMREAD_UNCHANGED)[..., 3].astype(np.float32) / 255
a = cv2.GaussianBlur(a, (0, 0), 2.0)[..., None]
img = np.clip((f - 128) * 1.04 + 132, 0, 255) * a + cv2.GaussianBlur(f, (0, 0), 2.4) * 0.88 * (1 - a)

def shift(arr):
    o = np.empty_like(arr)
    o[SHIFT:] = arr[:H - SHIFT]
    top = arr[:24].mean(axis=0, keepdims=True)                     # dark ceiling, extended upward
    o[:SHIFT] = np.repeat(top, SHIFT, axis=0)
    return o
img = shift(img)
img[:SHIFT + 30] = cv2.GaussianBlur(img[:SHIFT + 30], (0, 0), 6) * (np.linspace(0, 1, SHIFT + 30)[:, None, None] ** 0) 
cv2.imwrite(out_p, np.clip(img, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 96])
# grid mask: transparent where the subject is, fading out from y=1150 to y=1650 (after the shift)
am = shift(cv2.dilate(a[..., 0], np.ones((7, 7), np.uint8))[..., None])[..., 0]
fade = np.clip((1650 - np.arange(H)) / 500, 0, 1)[:, None]
g = (1 - am) * fade
cv2.imwrite(grid_p, np.dstack([np.full((H, W, 3), 255, np.uint8), (g * 255).astype(np.uint8)]))
print("done", out_p, grid_p)

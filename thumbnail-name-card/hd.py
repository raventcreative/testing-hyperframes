# HD pipeline: Real-ESRGAN x4 (tiled) + GFPGAN v1.4 face restore (blended to keep identity).
# usage: hd.py models_dir in.png out.png [face_weight]
import onnxruntime as ort, numpy as np, cv2, sys, time
M, src, out = sys.argv[1:4]; fw = float(sys.argv[4]) if len(sys.argv) > 4 else 0.6
import os
cache = out.replace('.png', '_sr.png')
img = cv2.imread(src)[..., ::-1].astype(np.float32) / 255.0            # RGB 0..1
H, W, _ = img.shape
sr = ort.InferenceSession(M + '/realesrgan_x4.onnx', providers=['CPUExecutionProvider'])
T, O = 64, 12; S = T - 2 * O
pad = np.pad(img, ((O, O + T), (O, O + T), (0, 0)), mode='reflect')
up = np.zeros((H * 4, W * 4, 3), np.float32); t0 = time.time()
for y in (range(0, H, S) if not os.path.exists(cache) else []):
    for x in range(0, W, S):
        tile = pad[y:y + T, x:x + T].transpose(2, 0, 1)[None]
        o = sr.run(None, {'input.1': tile})[0][0].transpose(1, 2, 0)
        core = o[O * 4:(O + S) * 4, O * 4:(O + S) * 4]
        hh, ww = min(S, H - y) * 4, min(S, W - x) * 4
        up[y * 4:y * 4 + hh, x * 4:x * 4 + ww] = core[:hh, :ww]
up = np.clip(up, 0, 1); print('sr done', up.shape, round(time.time() - t0, 1), 's')
bgr = cv2.imread(cache) if os.path.exists(cache) else (up[..., ::-1] * 255).round().astype(np.uint8)
cv2.imwrite(cache, bgr)

# ---- face restore ----
det = cv2.FaceDetectorYN.create(M + '/yunet.onnx', '', (bgr.shape[1], bgr.shape[0]), 0.7)
_, faces = det.detect(bgr)
if faces is not None and len(faces):
    f = max(faces, key=lambda f: f[2] * f[3]); fx, fy, fw_, fh = [int(v) for v in f[:4]]; eyes = [0, 0]
    src5 = np.float32(f[4:14]).reshape(5, 2)
    tmpl = np.float32([[192.98, 239.94], [318.90, 240.19], [256.63, 314.01], [201.26, 371.41], [313.09, 371.15]])
    A = cv2.estimateAffinePartial2D(src5, tmpl, method=cv2.LMEDS)[0].astype(np.float32)
    crop = cv2.warpAffine(bgr, A, (512, 512), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    x = (crop[..., ::-1].astype(np.float32) / 255 - .5) / .5
    gf = ort.InferenceSession(M + '/gfpgan14.onnx', providers=['CPUExecutionProvider'])
    o = gf.run(None, {'input': x.transpose(2, 0, 1)[None]})[0][0].transpose(1, 2, 0)
    rest = ((np.clip(o, -1, 1) * .5 + .5) * 255)[..., ::-1].astype(np.float32)
    rest = rest * fw + crop.astype(np.float32) * (1 - fw)            # keep identity
    Ai = cv2.invertAffineTransform(A)
    back = cv2.warpAffine(rest, Ai, (bgr.shape[1], bgr.shape[0]), flags=cv2.INTER_LANCZOS4)
    m = np.zeros((512, 512), np.float32); cv2.ellipse(m, (256, 270), (190, 235), 0, 0, 360, 1, -1)
    m = cv2.GaussianBlur(m, (0, 0), 28)
    mb = cv2.warpAffine(m, Ai, (bgr.shape[1], bgr.shape[0]))[..., None]
    bgr = (back * mb + bgr.astype(np.float32) * (1 - mb)).round().clip(0, 255).astype(np.uint8)
    cv2.imwrite(out.replace('.png', '_facecrop.png'), np.hstack([crop, rest.astype(np.uint8)]))
    print('face', (fx, fy, fw_, fh), 'eyes', len(eyes))
else: print('no face found')
cv2.imwrite(out, bgr); print('saved', bgr.shape)

"""v2 from the second (cleaner) recording source/earth_rec2.mp4 (no clideo, 8.7 Mbps).
The recorder duplicated ~3 of every 4 frames (stutter). We keep only the unique frames, measure the camera move between
each pair (similarity transform: zoom + pan), and rebuild a perfectly smooth virtual camera: constant-feel log-zoom with
easing, always centred on Bundaran HI (target propagated back through the transforms). Google's label + pin on the
fountain are inpainted. Output: raw upscaled picture -> tools/post.py adds zoom-blur punches, title, SFX.
Usage: python3 tools/build2.py preview|final out.mp4"""
import sys, json, subprocess, numpy as np, cv2

MODE = sys.argv[1]; OUT = sys.argv[2]
SRC = "source/earth_rec3.mp4"; FPS = 30; W, H = 1080, 1920
BX0, BY0, BX1, BY1 = 0, 172, 1540, 1002         # map only (right info panel x>1548 cut)
XMIN = 400                                       # keep clear of the top-left "Temukan…" popup
CW, CH = 468, 830                                # 9:16 crop at native zoom (full band height)
PILL = (0, 740, 90, 830)                         # minimap tile bottom-left (never in crop)
T_A, T_C, T_B = 1.0, 6.2, 8.2

# ---- frames + unique frames ----
cap = cv2.VideoCapture(SRC); SF = cap.get(cv2.CAP_PROP_FPS); frames = []
while True:
    ok, f = cap.read()
    if not ok: break
    frames.append(f[BY0:BY1, BX0:BX1].copy())
tr = json.load(open("out/track3.json"))
END_T = 10.9
U = [i for i, r in enumerate(tr) if r[0] <= END_T and (r[1] > 0.1)]
U = [i for i in U if tr[i][0] >= 7.2]
start = max(i for i, r in enumerate(tr) if r[0] < 7.2)
U = [start] + U
print("unique frames used:", len(U))

# ---- pairwise similarity transforms (frame k -> frame k+1) ----
det = cv2.SIFT_create(nfeatures=3000)
def feats(img):
    g = cv2.cvtColor(cv2.resize(img, None, fx=0.5, fy=0.5), cv2.COLOR_BGR2GRAY)
    m = np.full(g.shape, 255, np.uint8); m[:50, :35] = 0; m[PILL[1]//2-4:PILL[3]//2+4, PILL[0]//2-4:PILL[2]//2+4] = 0
    return det.detectAndCompute(g, m)
bf = cv2.BFMatcher(cv2.NORM_L2)
F = [feats(frames[i]) for i in U]
Ms, logs = [], []
for k in range(len(U) - 1):
    (ka, da), (kb, db) = F[k], F[k + 1]; M = None
    if da is not None and db is not None and len(ka) > 20 and len(kb) > 20:
        mm = [m for m, n in (p for p in bf.knnMatch(da, db, k=2) if len(p) == 2) if m.distance < 0.8 * n.distance]
        if len(mm) >= 12:
            A = np.float32([ka[m.queryIdx].pt for m in mm]) * 2; B = np.float32([kb[m.trainIdx].pt for m in mm]) * 2
            M, inl = cv2.estimateAffinePartial2D(A, B, method=cv2.RANSAC, ransacReprojThreshold=4, maxIters=4000, confidence=0.999)
            if M is not None and inl.sum() < 10: M = None
    if M is None:                                                              # fallback: radial-flow zoom about view centre
        z = np.exp(sum(tr[j][2] for j in range(U[k] + 1, U[k + 1] + 1)))
        c = np.array([(BX1 - BX0) / 2, (BY1 - BY0) / 2])
        M = np.float32([[z, 0, c[0] - z * c[0]], [0, z, c[1] - z * c[1]]]); print("fallback", k, round(tr[U[k]][0], 2), round(z, 3))
    s = float(np.sqrt(abs(np.linalg.det(M[:, :2]))))
    Ms.append(M); logs.append(np.log(max(s, 1e-3)))
Lam = np.concatenate([[0], np.cumsum(logs)])
print("total zoom x%.0f" % np.exp(Lam[-1]))

# ---- target (Bundaran HI) propagated back from the last frame ----
end = tr[U[-1]]; P = [None] * len(U)
P[-1] = np.array([944.6 - BX0, 459.2 - BY0])
for k in range(len(U) - 2, -1, -1):
    M3 = np.vstack([Ms[k], [0, 0, 1]]); P[k] = (np.linalg.inv(M3) @ np.array([*P[k + 1], 1]))[:2]
P = np.array(P)
# smooth the path a little in log-zoom space so the camera never jitters
# (no smoothing: pure propagation keeps consecutive frames geometrically consistent for the dissolves)

# ---- keep one frame per zoom level (Google pans without zooming for ~2 s before landing: keep the last of each plateau) ----
KI = []
for k in range(len(U)):
    x, y = P[k]
    if Lam[k] > Lam[0] + np.log(4) and k != len(U) - 1 and not (60 < y < 610 and 120 < x < BX1 - BX0 - 120): continue   # target off-screen in this frame
    if KI and Lam[k] - Lam[KI[-1]] < 0.012: KI[-1] = k
    else: KI.append(k)
KI = np.array(KI); LK = Lam[KI]
print("zoom levels kept:", len(KI))

# ---- extra zoom where Google left the target near a frame edge (so the camera never dips/clamps) ----
LO, HI = 0.36, 0.64
ek = []
for k in KI:
    if Lam[k] < Lam[0] + np.log(4): ek.append(1.0); continue
    x, y = P[k]; hb = BY1 - BY0; wl, wr = XMIN - BX0, BX1 - BX0
    hmax = min(y / LO, (hb - y) / (1 - HI), (x - wl) / LO * CH / CW, (wr - x) / (1 - HI) * CH / CW, hb)
    ek.append(float(np.clip(CH / max(hmax, 1), 1.0, 1.6)))
ek = np.array(ek)
for _ in range(6): ek[1:-1] = np.maximum(ek[1:-1], 0.5 * (ek[:-2] + ek[2:]))   # spread so it eases in/out
ek = np.convolve(np.pad(ek, 4, mode="edge"), np.ones(9) / 9, mode="valid")
print("extra zoom max %.2f end %.2f" % (ek.max(), ek[-1]))
def E(v): return float(np.interp(v, LK, ek))

# ---- label / pin removal on the fountain (Google's "Bundaran Hotel Indonesia" + red marker) ----
_c = cv2.VideoCapture("source/earth_rec.mp4"); _c.set(cv2.CAP_PROP_POS_FRAMES, int(20 * 30000 / 1001)); _, _f20 = _c.read()
TPL = _f20[489:513, 950:968].astype(np.float32)                     # mouse-cursor template (same Chrome arrow)
_g = cv2.cvtColor(_f20[489:513, 950:968], cv2.COLOR_BGR2GRAY); TM = cv2.dilate(((_g > 215) | (_g < 45)).astype(np.uint8), np.ones((3, 3), np.uint8))
def decursor(img):
    r = cv2.matchTemplate(img.astype(np.float32), TPL, cv2.TM_CCORR_NORMED, mask=np.dstack([TM] * 3).astype(np.float32))
    _, mv, _, (x, y) = cv2.minMaxLoc(r)
    if mv < 0.95: return img
    sub = cv2.cvtColor(img[y:y + 24, x:x + 18], cv2.COLOR_BGR2GRAY)
    m = (((sub > 190) | (sub < 70)) & (TM > 0)).astype(np.uint8)
    M = np.zeros(img.shape[:2], np.uint8); M[y:y + 24, x:x + 18] = cv2.dilate(m, np.ones((3, 3), np.uint8), iterations=2) * 255
    return cv2.inpaint(img, M, 4, cv2.INPAINT_TELEA)
def clean(img, k):                                              # remove Google's red pin + "Jakarta" label around the target
    img = decursor(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV); px, py = int(P[k][0]), int(P[k][1])
    box = np.zeros(img.shape[:2], np.uint8)
    box[max(py - 30, 0):py + 22, max(px - 18, 0):px + 18] = 1
    box[max(py - 62, 0):py - 14, max(px - 70, 0):px + 70] = 1
    red = ((hsv[..., 0] < 10) | (hsv[..., 0] > 168)) & (hsv[..., 1] > 110) & (hsv[..., 2] > 100)
    wht = (hsv[..., 2] > 200) & (hsv[..., 1] < 50)
    m = ((red | wht) & (box > 0)).astype(np.uint8)
    if m.sum() < 8: return img
    m = cv2.dilate(m, np.ones((3, 3), np.uint8), iterations=2) * 255
    return cv2.inpaint(img, m, 5, cv2.INPAINT_TELEA)
def chain(j, k):                                               # transform frame j -> frame k (j < k)
    A = np.eye(3)
    for q in range(j, k): A = np.vstack([Ms[q], [0, 0, 1]]) @ A
    return A
def fill_pill(k):
    img = frames[U[k]].copy(); x0, y0, x1, y1 = PILL
    for j in range(k - 1, -1, -1):
        A = chain(j, k); Ai = np.linalg.inv(A)
        cs = np.array([[x0, y0, 1], [x1, y0, 1], [x0, y1, 1], [x1, y1, 1]], float) @ Ai.T
        bx0, by0 = cs[:, 0].min(), cs[:, 1].min(); bx1, by1 = cs[:, 0].max(), cs[:, 1].max()
        inside = bx0 > 2 and by0 > 2 and bx1 < img.shape[1] - 2 and by1 < img.shape[0] - 2
        clear = bx1 < x0 - 4 or bx0 > x1 + 4 or by1 < y0 - 4 or by0 > y1 + 4
        if inside and clear:
            wj = cv2.warpAffine(frames[U[j]], A[:2].astype(np.float32), (img.shape[1], img.shape[0]), flags=cv2.INTER_CUBIC)
            img[y0:y1, x0:x1] = wj[y0:y1, x0:x1]
            return img
    m = np.zeros(img.shape[:2], np.uint8); m[y0:y1, x0:x1] = 255
    return cv2.inpaint(img, m, 8, cv2.INPAINT_TELEA)
CL = {}
def frame(k):
    if k not in CL: CL[k] = clean(frames[U[k]].copy(), k)
    return CL[k]

# ---- virtual camera ----
L0, L1 = Lam[0], Lam[-1]
def V(t):                                                       # wanted log-zoom
    if t < T_A: return L0 - np.log(1.75) + np.log(1.75) * (1 - (1 - t / T_A) ** 2) * 0.12
    if t < T_C:
        x = (t - T_A) / (T_C - T_A); e = x * x * (3 - 2 * x) * 0.8 + 0.2 * x
        a = L0 - np.log(1.75) + np.log(1.75) * 0.12
        return a + (L1 - a) * e
    x = (t - T_C) / (T_B - T_C); return L1 + np.log(1.04) * (1 - (1 - x) ** 2)
def render_k(k, v, want_mask=False):
    e = E(v); w, h = CW * np.exp(Lam[k] - v) / e, CH * np.exp(Lam[k] - v) / e
    cx, cy = P[k]
    if w < (BX1 - XMIN): cx = float(np.clip(cx, XMIN - BX0 + w / 2, BX1 - BX0 - w / 2))
    if h < (BY1 - BY0): cy = float(np.clip(cy, h / 2, BY1 - BY0 - h / 2))
    M = np.float32([[CW / w, 0, CW / 2 - cx * CW / w], [0, CH / h, CH / 2 - cy * CH / h]])
    bm = cv2.BORDER_CONSTANT if (v < Lam[0] + np.log(4) or want_mask) else cv2.BORDER_REPLICATE
    out = cv2.warpAffine(frame(k), M, (CW, CH), flags=cv2.INTER_CUBIC, borderMode=bm, borderValue=(0, 0, 0)).astype(np.float32)
    if want_mask:
        mk = cv2.warpAffine(np.ones(frame(k).shape[:2], np.float32), M, (CW, CH), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        return out, cv2.erode(mk, np.ones((5, 5), np.uint8))[..., None]
    return out
def view(v):
    j = int(np.searchsorted(LK, v, side="right") - 1); j = min(max(j, 0), len(KI) - 1)
    if j == len(KI) - 1 or v <= LK[0]: return render_k(KI[j], v)
    f = (v - LK[j]) / max(LK[j + 1] - LK[j], 1e-6)
    if f < 0.8 or v < Lam[0] + np.log(4): return render_k(KI[j], v)
    w = (f - 0.8) / 0.2; w = w * w * (3 - 2 * w)                # short dissolve into the next real frame
    a = render_k(KI[j], v); b, m = render_k(KI[j + 1], v, True); w = w * m
    return a * (1 - w) + b * w

# ---- upscaler ----
if MODE == "final":
    import onnxruntime as ort
    so = ort.SessionOptions(); so.intra_op_num_threads = 4
    sess = ort.InferenceSession("/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/models/real_esrgan_x2.onnx", so, providers=["CPUExecutionProvider"])
    iname = sess.get_inputs()[0].name
    def up(img):
        x = (img[:, :, ::-1].astype(np.float32) / 255).transpose(2, 0, 1)[None]
        y = (np.clip(sess.run(None, {iname: x})[0][0].transpose(1, 2, 0), 0, 1) * 255).astype(np.uint8)[:, :, ::-1]
        return cv2.resize(y, (W, H), interpolation=cv2.INTER_CUBIC)
else:
    up = lambda img: cv2.resize(img, (W, H), interpolation=cv2.INTER_LANCZOS4)

ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                       "-c:v", "libx264", "-preset", "slow", "-crf", "8", "-pix_fmt", "yuv444p", OUT], stdin=subprocess.PIPE)
N = int(round(T_B * FPS))
for i in range(N):
    t = i / FPS
    acc = sum(view(V(max(t + d / FPS, 0))) for d in (-0.25, 0, 0.25)) / 3      # 3-subframe motion blur
    ff.stdin.write(up(np.clip(acc, 0, 255).astype(np.uint8)).tobytes())
    if i % 30 == 0: print(f"frame {i}/{N}", flush=True)
ff.stdin.close(); ff.wait(); print("done", OUT)

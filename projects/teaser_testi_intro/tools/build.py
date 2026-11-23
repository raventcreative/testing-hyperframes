"""Teaser testimoni intro: Google Earth screen recording -> clean 9:16 fly-in (1080x1920, 30 fps).
Usage: python3 tools/build.py preview|final [out.mp4]
 - crops the map only (no browser UI, side panel, clideo watermark), tracks the target to Bundaran HI
 - time-remap with smooth speed ramp (PCHIP), 3-subframe motion blur, continuous digital push-in
 - removes the mouse cursor (template match + inpaint)
 - final: Real-ESRGAN x2 upscale per frame; preview: Lanczos
 - overlays: JAKARTA title + coordinates at the end, small "Google Earth" attribution
"""
import sys, subprocess, numpy as np, cv2
from scipy.interpolate import PchipInterpolator as P
from PIL import Image, ImageDraw, ImageFont

MODE = sys.argv[1] if len(sys.argv) > 1 else "preview"
OUT = sys.argv[2] if len(sys.argv) > 2 else f"out/teaser_intro_{MODE}.mp4"
TEXT = "--clean" not in sys.argv
SRC = "source/earth_rec.mp4"; SFPS = 30000 / 1001; FPS = 30; W, H = 1080, 1920
BX0, BX1, BY0, BY1 = 420, 1540, 172, 1002          # source band; crop kept inside x 410..1370 (watermark x>1380, panel x>1548)
CW, CH = 468, 830                                   # 9:16 crop at zoom 1

# ---- timeline (output seconds) ----
import json
TR = json.load(open("out/track.json"))                      # per-frame optical-flow magnitude (tools: track step in NOTES)
T_A, T_C, T_B = 1.6, 7.8, 9.6                               # globe until 1.6 s, travel until 7.8 s, hold until 9.6 s
S0, S1, SG = 11.0, 25.0, 3.0                                # travel source range, still-globe source time
fl = np.array(TR["flow"]); k0, k1 = int(S0 * SFPS), int(S1 * SFPS)
cum = np.concatenate([[0], np.cumsum(fl[k0:k1] + 0.05)]); cum /= cum[-1]   # motion-equalised progress (skips Google's pauses)
ks = np.arange(k0, k1 + 1) / SFPS
def prog(u):                                                 # ease-in from the still globe, ease-out into the hold
    x = min(max((u - T_A) / (T_C - T_A), 0), 1)
    return x * x * (3 - 2 * x) * 0.85 + x * 0.15
def src_t(t):
    if t < T_A: return SG
    if t < T_C: return float(np.interp(prog(t), cum, ks))
    return S1
zs = P([S0, 12.3, S1], [0.62, 1.0, 1.08])
def z_t(t):
    if t < T_A: return 0.56 + 0.06 * (1 - (1 - t / T_A) ** 2)
    if t < T_C: return float(zs(src_t(t)))
    x = (t - T_C) / (T_B - T_C); return 1.08 + 0.14 * (1 - (1 - x) ** 2)
cxf = P([0, 14, 18, 19, 20, 21.5, 22.5, 23.25, 24.25, 24.75, 25.0], [955, 950, 938, 911, 841, 690, 700, 726, 730, 784, 800])
cyf = P([0, 11.0, 14, 23.0, 25.0], [552, 552, 520, 620, 694])

# ---- read source frames ----
N = int(round(T_B * FPS))
cap = cv2.VideoCapture(SRC); frames = {}; k = 0
while True:
    ok, f = cap.read()
    if not ok: break
    frames[k] = f[BY0:BY1, BX0:BX1].copy(); k += 1
last = max(frames)

# ---- cursor removal ----
full20 = None
cap = cv2.VideoCapture(SRC); cap.set(cv2.CAP_PROP_POS_FRAMES, int(20 * SFPS)); _, full20 = cap.read()
tpl = full20[489:513, 950:968].astype(np.float32)
g = cv2.cvtColor(full20[489:513, 950:968], cv2.COLOR_BGR2GRAY)
tmask = ((g > 215) | (g < 45)).astype(np.uint8)
tmask[:, :] = cv2.dilate(tmask, np.ones((3, 3), np.uint8))
def decursor(img):
    r = cv2.matchTemplate(img.astype(np.float32), tpl, cv2.TM_CCORR_NORMED, mask=np.dstack([tmask]*3).astype(np.float32))
    _, mv, _, ml = cv2.minMaxLoc(r)
    if mv < 0.97: return img
    x, y = ml; sub = img[y:y+24, x:x+18]
    sg = cv2.cvtColor(sub, cv2.COLOR_BGR2GRAY)
    m = (((sg > 200) | (sg < 60)) & (tmask > 0)).astype(np.uint8)
    if m.sum() < 40: return img
    M = np.zeros(img.shape[:2], np.uint8); M[y:y+24, x:x+18] = cv2.dilate(m, np.ones((3, 3), np.uint8)) * 255
    return cv2.inpaint(img, M, 4, cv2.INPAINT_TELEA)
clean = {}
def getf(k):
    k = min(k, last)
    if k not in clean: clean[k] = decursor(frames[k])
    return clean[k]
def sample(s):                                      # linear blend between source frames
    x = s * SFPS; a = int(np.floor(x)); w = x - a
    fa = getf(a).astype(np.float32)
    return fa if w < 1e-3 else fa * (1 - w) + getf(a + 1).astype(np.float32) * w

def crop(img, s, z):
    w, h = CW / z, CH / z
    cx = float(np.clip(cxf(s), 410 + w/2, 1370 - w/2)) if w < 960 else 890.0
    cy = float(np.clip(cyf(s), BY0 + h/2, BY1 - h/2)) if h < 830 else 587.0
    cx -= BX0; cy -= BY0
    M = np.float32([[CW / w, 0, CW/2 - cx * CW / w], [0, CH / h, CH/2 - cy * CH / h]])
    return cv2.warpAffine(img, M, (CW, CH), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))

# ---- upscaler ----
if MODE == "final":
    import onnxruntime as ort
    so = ort.SessionOptions(); so.intra_op_num_threads = 4
    sess = ort.InferenceSession("/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/models/real_esrgan_x2.onnx", so, providers=["CPUExecutionProvider"])
    iname = sess.get_inputs()[0].name
    def up(img):
        x = (img[:, :, ::-1].astype(np.float32) / 255).transpose(2, 0, 1)[None]
        y = sess.run(None, {iname: x})[0][0].transpose(1, 2, 0)
        y = (np.clip(y, 0, 1) * 255).astype(np.uint8)[:, :, ::-1]
        return cv2.resize(y, (W, H), interpolation=cv2.INTER_CUBIC)
else:
    up = lambda img: cv2.resize(img, (W, H), interpolation=cv2.INTER_LANCZOS4)

# ---- overlays ----
FB = ImageFont.truetype("tools/Poppins-Bold.ttf", 132); FR = ImageFont.truetype("tools/Poppins-Regular.ttf", 34)
FS = ImageFont.truetype("tools/Poppins-SemiBold.ttf", 30); FA = ImageFont.truetype("tools/Poppins-Regular.ttf", 22)
ease = lambda x: 1 - (1 - min(max(x, 0), 1)) ** 3
yy = np.linspace(0, 1, H)[:, None, None]
grad = np.clip((yy - 0.55) / 0.45, 0, 1) ** 1.6 * 0.62            # bottom shade for title
vig = None
def spaced(d, xy, text, font, sp, fill):
    x, y = xy; tw = sum(d.textlength(c, font=font) for c in text) + sp * (len(text) - 1)
    x -= tw / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill); x += d.textlength(c, font=font) + sp
def overlay(img, t):
    global vig
    if vig is None:
        Y, X = np.mgrid[0:H, 0:W]; r = np.sqrt(((X - W/2) / (W * 0.75))**2 + ((Y - H/2) / (H * 0.75))**2)
        vig = (1 - np.clip(r - 0.35, 0, 1) * 0.55)[:, :, None]
    f = img.astype(np.float32) * vig
    a = ease((t - 7.5) / 0.8) if TEXT else 0
    if a > 0: f = f * (1 - grad * a)
    f = np.clip(f, 0, 255).astype(np.uint8)
    im = Image.fromarray(f[:, :, ::-1]).convert("RGBA"); lay = Image.new("RGBA", im.size); d = ImageDraw.Draw(lay)
    if TEXT:
        a1 = ease((t - 7.7) / 0.7); a2 = ease((t - 8.15) / 0.6); a3 = ease((t - 8.0) / 0.7)
        if a1 > 0:
            spaced(d, (W/2, 1430 + 30 * (1 - a1)), "JAKARTA", FB, 34 - 16 * a1, (255, 255, 255, int(255 * a1)))
        if a3 > 0:
            L = 260 * a3; d.rounded_rectangle((W/2 - L, 1606, W/2 + L, 1610), 2, fill=(1, 204, 247, int(255 * a3)))
        if a2 > 0:
            spaced(d, (W/2, 1636 + 16 * (1 - a2)), "6.1950° S  ·  106.8230° E", FR, 3, (255, 255, 255, int(235 * a2)))
            spaced(d, (W/2, 1700 + 16 * (1 - a2)), "BUNDARAN HI · INDONESIA", FS, 6, (1, 204, 247, int(255 * a2)))
    d.text((40, H - 62), "Google Earth", font=FA, fill=(255, 255, 255, 150))
    return np.array(Image.alpha_composite(im, lay).convert("RGB"))[:, :, ::-1]

# ---- render (text version + clean version in one pass) ----
def pipe(path):
    return subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                             "-c:v", "libx264", "-preset", "slow", "-crf", "14", "-pix_fmt", "yuv420p", "-movflags", "+faststart", path], stdin=subprocess.PIPE)
outs = [(pipe(OUT), True), (pipe(OUT.replace(".mp4", "_CLEAN.mp4")), False)]
for i in range(N):
    t = i / FPS; acc = 0
    for d in (-0.22, 0, 0.22):                                      # 3-subframe motion blur (short shutter)
        tt = t + d / FPS; s = src_t(max(tt, 0))
        acc = acc + crop(sample(s), s, z_t(max(tt, 0)))
    fr = up(np.clip(acc / 3, 0, 255).astype(np.uint8))
    fr = (fr.astype(np.float32) * ease(t / 0.5)).astype(np.uint8)  # fade in from black
    for p_, txt in outs:
        TEXT = txt; p_.stdin.write(overlay(fr, t).tobytes())
    if i % 15 == 0: print(f"frame {i}/{N}", flush=True)
for p_, _ in outs: p_.stdin.close(); p_.wait()
print("done", OUT)

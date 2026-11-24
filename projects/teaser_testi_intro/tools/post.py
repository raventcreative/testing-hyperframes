"""Post pass: raw upscaled fly-in -> videographer zoom blur + vignette + fade + title + SFX.
Usage: python3 tools/post.py out/raw_upscaled.mp4 out/TEASER_INTRO_JAKARTA_9x16.mp4
Writes <out>.mp4 (title), <out>_CLEAN.mp4 (no title), <out>_SFX.wav (sound effects only, for CapCut).
Zoom blur strength follows the measured zoom speed of the picture (optical flow), so it peaks on the fast pushes."""
import sys, subprocess, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

IN, OUT = sys.argv[1], sys.argv[2]
W, H, FPS = 1080, 1920, 30
CLEAN = OUT.replace(".mp4", "_CLEAN.mp4"); SFXW = OUT.replace(".mp4", "_SFX.wav")

# ---- read frames + measure zoom speed ----
cap = cv2.VideoCapture(IN); frames = []
while True:
    ok, f = cap.read()
    if not ok: break
    frames.append(f)
N = len(frames)
Y, X = np.mgrid[0:240, 0:135].astype(np.float32); rx, ry = X - 67.5, Y - 120; rr = np.sqrt(rx**2 + ry**2) + 1e-3
v = [0.0]
for i in range(1, N):
    a = cv2.cvtColor(cv2.resize(frames[i-1], (135, 240)), cv2.COLOR_BGR2GRAY)
    b = cv2.cvtColor(cv2.resize(frames[i], (135, 240)), cv2.COLOR_BGR2GRAY)
    fl = cv2.calcOpticalFlowFarneback(a, b, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    radial = (fl[..., 0] * rx + fl[..., 1] * ry) / rr                 # outward = zoom in
    v.append(float(np.median(radial / rr)))                           # relative scale change per frame
v = np.array(v); v[0] = v[1]
vs = np.convolve(v, np.ones(5) / 5, mode="same")
base = 0.03 * np.clip(vs / 0.08, 0, 1)                               # mild continuous blur while zooming
PULSES = [1.75]                                                       # videographer zoom-blur punches: launch + strongest pushes
for i in np.argsort(-vs):
    t = i / FPS
    if vs[i] < 0.065 or t > 6.0: break
    if all(abs(t - q) > 1.0 for q in PULSES): PULSES.append(t)
PULSES.sort()
pulse = np.zeros(N)
for q in PULSES:
    for i in range(N):
        dt = i / FPS - q
        pulse[i] = max(pulse[i], np.exp(-(dt / 0.09) ** 2) if dt < 0 else np.exp(-(dt / 0.22) ** 2))
amt = base + 0.13 * pulse
np.save(OUT.replace(".mp4", "_speed.npy"), np.stack([v, amt]))

_gy, _gx = np.mgrid[0:H, 0:W].astype(np.float32)
CMASK = np.clip((np.sqrt(((_gx - W/2) / (W * 0.5))**2 + ((_gy - H/2) / (H * 0.5))**2) - 0.08) / 0.35, 0, 1)[..., None]
def zoom_blur(img, a, cx=W/2, cy=H/2, n=14):
    if a < 0.006: return img
    acc = np.zeros(img.shape, np.float32)
    for k in range(n):
        s = 1 + a * k / (n - 1)
        M = np.float32([[s, 0, cx - s * cx], [0, s, cy - s * cy]])
        acc += cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    out = acc / n; m = CMASK
    # keep the very centre crisp (where the eye is), blur grows to the edges
    return (img * (1 - m) + out * m).astype(np.uint8)

# ---- overlays ----
FB = ImageFont.truetype("tools/Poppins-Bold.ttf", 132); FR = ImageFont.truetype("tools/Poppins-Regular.ttf", 34)
FS = ImageFont.truetype("tools/Poppins-SemiBold.ttf", 30); FA = ImageFont.truetype("tools/Poppins-Regular.ttf", 22)
ease = lambda x: 1 - (1 - min(max(x, 0), 1)) ** 3
yy = np.linspace(0, 1, H)[:, None, None]; grad = np.clip((yy - 0.55) / 0.45, 0, 1) ** 1.6 * 0.62
Yg, Xg = np.mgrid[0:H, 0:W]; r = np.sqrt(((Xg - W/2) / (W * 0.75))**2 + ((Yg - H/2) / (H * 0.75))**2)
vig = (1 - np.clip(r - 0.35, 0, 1) * 0.55)[:, :, None]; del Yg, Xg, r
def spaced(d, xy, text, font, sp, fill):
    x, y = xy; tw = sum(d.textlength(c, font=font) for c in text) + sp * (len(text) - 1); x -= tw / 2
    for c in text: d.text((x, y), c, font=font, fill=fill); x += d.textlength(c, font=font) + sp
T_LAND = 7.7
def overlay(img, t, text):
    f = img.astype(np.float32) * vig * ease(t / 0.5)
    a = ease((t - T_LAND + 0.2) / 0.8) if text else 0
    if a > 0: f = f * (1 - grad * a)
    im = Image.fromarray(np.clip(f, 0, 255).astype(np.uint8)[:, :, ::-1]).convert("RGBA"); lay = Image.new("RGBA", im.size); d = ImageDraw.Draw(lay)
    if text:
        a1 = ease((t - T_LAND) / 0.7); a2 = ease((t - T_LAND - 0.45) / 0.6); a3 = ease((t - T_LAND - 0.3) / 0.7)
        if a1 > 0: spaced(d, (W/2, 1430 + 30 * (1 - a1)), "JAKARTA", FB, 34 - 16 * a1, (255, 255, 255, int(255 * a1)))
        if a3 > 0: L = 260 * a3; d.rounded_rectangle((W/2 - L, 1606, W/2 + L, 1610), 2, fill=(1, 204, 247, int(255 * a3)))
        if a2 > 0:
            spaced(d, (W/2, 1636 + 16 * (1 - a2)), "6.1950° S  ·  106.8230° E", FR, 3, (255, 255, 255, int(235 * a2)))
            spaced(d, (W/2, 1700 + 16 * (1 - a2)), "BUNDARAN HI · INDONESIA", FS, 6, (1, 204, 247, int(255 * a2)))
    d.text((40, H - 62), "Google Earth", font=FA, fill=(255, 255, 255, 150))
    return np.array(Image.alpha_composite(im, lay).convert("RGB"))[:, :, ::-1]

# ---- SFX (Pixabay Content License, from the HyperFrames media skill) ----
SR = 48000; D = N / FPS
def load(name):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f"assets/sfx/{name}.mp3", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).copy()
mix = np.zeros(int((D + 3) * SR), np.float32)
def put(name, t, gain_db, align_peak=False):
    x = load(name) * 10 ** (gain_db / 20)
    off = int(np.argmax(np.abs(x))) if align_peak else 0
    s = max(int(t * SR) - off, 0); e = min(s + len(x), len(mix)); mix[s:e] += x[:e - s]
events = []
put("riser", 0.15, -9); events.append((0.15, "riser"))
put("whoosh-cinematic", 1.55, -4, align_peak=True); events.append((1.55, "whoosh-cinematic"))
for j, q in enumerate(PULSES[1:]):                                   # whoosh on every punch
    put("whoosh" if j % 2 == 0 else "whoosh-short", q, -6, align_peak=True); events.append((q, "whoosh"))
put("impact-bass-1", T_LAND, -3, align_peak=True); events.append((T_LAND, "impact-bass-1"))
put("sparkle", T_LAND + 0.4, -12); events.append((T_LAND + 0.4, "sparkle"))
mix = mix[:int(D * SR)]
fo = int(0.6 * SR); mix[-fo:] *= np.linspace(1, 0, fo)
mix *= 10 ** (-1.0 / 20) / max(np.abs(mix).max(), 1e-6)              # peak -1 dBFS
st = np.repeat(mix[:, None], 2, 1)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s16le", SFXW], input=st.tobytes(), check=True)
print("sfx events:", [(round(t, 2), n) for t, n in events])

# ---- render both versions with audio ----
def pipe(path):
    return subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                             "-i", SFXW, "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "slow", "-crf", "14", "-pix_fmt", "yuv420p",
                             "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", path], stdin=subprocess.PIPE)
pa, pc = pipe(OUT), pipe(CLEAN)
for i, f in enumerate(frames):
    t = i / FPS; b = zoom_blur(f, float(amt[i]))
    pa.stdin.write(overlay(b, t, True).tobytes()); pc.stdin.write(overlay(b, t, False).tobytes())
for p in (pa, pc): p.stdin.close(); p.wait()
print("done", OUT, CLEAN, SFXW, "max blur", round(float(amt.max()), 3))

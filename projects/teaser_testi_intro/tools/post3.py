"""V3 teaser intro: typed search "AI Preneur Coaching to Jakarta" -> Enter -> the page shrinks away into space (zoom out to Earth)
-> the Google Earth fly-in (out/raw3_upscaled.mp4 from tools/build3.py) -> cyan AIpreneur pin drops on Jakarta + title.
Usage: python3 tools/post3.py out/raw3_upscaled.mp4 out/TEASER_INTRO_AIPRENEUR_JAKARTA_9x16.mp4
Writes <out>.mp4 (title), <out>_CLEAN.mp4 (no title text, pin kept), <out>_SFX.wav."""
import sys, json, subprocess, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

IN, OUT = sys.argv[1], sys.argv[2]
W, H, FPS = 1080, 1920, 30
CLEAN = OUT.replace(".mp4", "_CLEAN.mp4"); SFXW = OUT.replace(".mp4", "_SFX.wav")
QUERY = "AI Preneur Coaching to Jakarta"
T_TYPE0, T_TYPE1, T_ENTER, T_SHRINK0, T_SHRINK1 = 0.55, 2.15, 2.5, 2.7, 3.35
OFF = T_SHRINK0                                   # flight video starts (globe) under the shrinking page
NAVY, NAVY2, CYAN = (10, 13, 44), (41, 75, 119), (1, 204, 247)

# ---- flight frames + target screen path ----
cap = cv2.VideoCapture(IN); FL = []
while True:
    ok, f = cap.read()
    if not ok: break
    FL.append(f)
TGT = json.load(open("out/target3_screen.json"))
T_LAND = OFF + 6.2                                 # build3 T_C
N = int(round((OFF + len(FL) / FPS) * FPS))
D = N / FPS

# ---- opening page (PIL, crisp 1080x1920) ----
F_TXT = ImageFont.truetype("tools/Poppins-Regular.ttf", 39); F_PH = ImageFont.truetype("tools/Poppins-Regular.ttf", 39)
F_KEY = ImageFont.truetype("tools/Poppins-SemiBold.ttf", 23); F_SM = ImageFont.truetype("tools/Poppins-SemiBold.ttf", 28)
BG = Image.open("assets/brand/bg_light_1080x1920.png").convert("RGB").resize((W, H))
LOGO = Image.open("assets/brand/logo_dark_trim.png").convert("RGBA"); LOGO = LOGO.resize((420, int(420 * LOGO.size[1] / LOGO.size[0])), Image.LANCZOS)
BX, BY, BW, BH = 70, 880, 940, 124                 # search bar
rng = np.random.default_rng(7)
gaps = rng.uniform(0.7, 1.35, len(QUERY)); gaps[QUERY.index(" ") if " " in QUERY else 0] *= 1.0
KT = T_TYPE0 + np.cumsum(gaps) / gaps.sum() * (T_TYPE1 - T_TYPE0)   # time each character lands
ease = lambda x: 1 - (1 - min(max(x, 0), 1)) ** 3
def shadow_layer():
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
    d.rounded_rectangle((BX, BY + 14, BX + BW, BY + BH + 14), BH // 2, fill=(10, 13, 44, 60))
    return sh.filter(ImageFilter.GaussianBlur(22))
SH = shadow_layer()
def page(t):
    im = BG.copy().convert("RGBA")
    a_in = ease(t / 0.45)
    lg = LOGO.copy(); lg.putalpha(lg.getchannel("A").point(lambda v: int(v * a_in)))
    im.alpha_composite(lg, ((W - lg.size[0]) // 2, int(560 - 20 * (1 - a_in))))
    press = 1 - 0.025 * np.exp(-((t - T_ENTER - 0.05) / 0.07) ** 2)          # bar dips on Enter
    bar = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(bar)
    bar.alpha_composite(SH)
    cx, cy = BX + BW / 2, BY + BH / 2; bw, bh = BW * press, BH * press
    x0, y0 = cx - bw / 2, cy - bh / 2
    focus = ease((t - 0.25) / 0.3)
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), bh / 2, fill=(255, 255, 255, 255),
                        outline=tuple(int(a + (b - a) * focus) for a, b in zip((214, 222, 234), NAVY2)) + (255,), width=3)
    # magnifier icon
    mx, my = x0 + 62, cy - 4; d.ellipse((mx - 17, my - 17, mx + 17, my + 17), outline=NAVY2 + (255,), width=5)
    d.line((mx + 12, my + 12, mx + 26, my + 26), fill=NAVY2 + (255,), width=6)
    n = int(np.sum(KT <= t)); txt = QUERY[:n]; tx = x0 + 110
    if n == 0: d.text((tx, cy), "Cari tujuan…", font=F_PH, fill=(140, 152, 172, int(255 * a_in)), anchor="lm")
    else: d.text((tx, cy), txt, font=F_TXT, fill=NAVY + (255,), anchor="lm")
    tw = d.textlength(txt, font=F_TXT) if n else 0
    blink = (t < T_TYPE0 or t > T_TYPE1 + 0.05) and (int(t * 2.4) % 2 == 1)
    if t < T_ENTER + 0.1 and not blink and t > 0.2:
        d.rounded_rectangle((tx + tw + 4, cy - 28, tx + tw + 8, cy + 28), 2, fill=NAVY2 + (255,))
    # Enter keycap on the right: appears when typing ends, pressed at T_ENTER
    ka = ease((t - T_TYPE1 - 0.05) / 0.25)
    if ka > 0:
        pr = np.exp(-((t - T_ENTER) / 0.08) ** 2); kx1, ky = x0 + bw - 26, cy
        kw, kh = 132, 60; kx0 = kx1 - kw
        on = t >= T_ENTER - 0.03
        fill = NAVY2 + (int(255 * ka),) if on else (238, 243, 250, int(255 * ka))
        d.rounded_rectangle((kx0, ky - kh / 2 + 4 * pr, kx1, ky + kh / 2 + 4 * pr), 16, fill=fill,
                            outline=(NAVY2 + (int(255 * ka),)), width=2)
        d.text(((kx0 + kx1) / 2, ky + 4 * pr), "Enter ↵", font=F_KEY, fill=((255, 255, 255) if on else NAVY2) + (int(255 * ka),), anchor="mm")
    im.alpha_composite(bar)
    # loading line after Enter
    if t > T_ENTER:
        p = ease((t - T_ENTER) / 0.35); d2 = ImageDraw.Draw(im)
        d2.rounded_rectangle((BX + 60, BY + BH + 34, BX + 60 + (BW - 120) * p, BY + BH + 40), 3, fill=CYAN + (255,))
        d2.text((W / 2, BY + BH + 92), "Menuju Jakarta…", font=F_SM, fill=NAVY2 + (int(255 * ease((t - T_ENTER) / 0.25)),), anchor="mm")
    return cv2.cvtColor(np.array(im.convert("RGB")), cv2.COLOR_RGB2BGR)

# ---- zoom blur ----
_gy, _gx = np.mgrid[0:H, 0:W].astype(np.float32)
CM = np.clip((np.sqrt(((_gx - W/2) / (W * 0.5))**2 + ((_gy - H/2) / (H * 0.5))**2) - 0.08) / 0.35, 0, 1)[..., None]
def zoom_blur(img, a, n=14, outward=True):
    if a < 0.006: return img
    acc = np.zeros(img.shape, np.float32)
    for k in range(n):
        s = 1 + a * k / (n - 1) if outward else 1 / (1 + a * k / (n - 1))
        M = np.float32([[s, 0, W/2 - s * W/2], [0, s, H/2 - s * H/2]])
        acc += cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return (img * (1 - CM) + acc / n * CM).astype(np.uint8)

# flight zoom speed -> blur punches (same recipe as v1/v2)
Yq, Xq = np.mgrid[0:240, 0:135].astype(np.float32); rx, ry = Xq - 67.5, Yq - 120; rr = np.sqrt(rx**2 + ry**2) + 1e-3
v = [0.0]
for i in range(1, len(FL)):
    a = cv2.cvtColor(cv2.resize(FL[i-1], (135, 240)), cv2.COLOR_BGR2GRAY); b = cv2.cvtColor(cv2.resize(FL[i], (135, 240)), cv2.COLOR_BGR2GRAY)
    fl = cv2.calcOpticalFlowFarneback(a, b, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    v.append(float(np.median(((fl[..., 0] * rx + fl[..., 1] * ry) / rr) / rr)))
vs = np.convolve(np.array(v), np.ones(5) / 5, mode="same")
PULSES = []
for i in np.argsort(-vs):
    t = OFF + i / FPS
    if vs[i] < 0.05 or t > T_LAND - 1.0: break
    if t > OFF + 1.4 and all(abs(t - q) > 1.0 for q in PULSES): PULSES.append(t)
PULSES = sorted(PULSES)[:3]
def amt(t):
    a = 0.0
    if T_SHRINK0 - 0.05 < t < T_SHRINK1 + 0.25:                                 # the page flying away: inward blur
        a = 0.16 * np.sin(np.pi * min(max((t - T_SHRINK0 + 0.05) / (T_SHRINK1 - T_SHRINK0 + 0.3), 0), 1))
    i = int(round((t - OFF) * FPS))
    if 0 <= i < len(vs): a = max(a, 0.03 * float(np.clip(vs[i] / 0.08, 0, 1)))
    for q in PULSES:
        dt = t - q; a = max(a, 0.13 * (np.exp(-(dt / 0.09) ** 2) if dt < 0 else np.exp(-(dt / 0.22) ** 2)))
    return a

# ---- title + pin overlays ----
FB = ImageFont.truetype("tools/Poppins-Bold.ttf", 132); FR = ImageFont.truetype("tools/Poppins-Regular.ttf", 34)
FS = ImageFont.truetype("tools/Poppins-SemiBold.ttf", 30); FA = ImageFont.truetype("tools/Poppins-Regular.ttf", 22)
yy = np.linspace(0, 1, H)[:, None, None]; grad = np.clip((yy - 0.55) / 0.45, 0, 1) ** 1.6 * 0.62
r_ = np.sqrt(((_gx - W/2) / (W * 0.75))**2 + ((_gy - H/2) / (H * 0.75))**2); VIG = (1 - np.clip(r_ - 0.35, 0, 1) * 0.55)[:, :, None]
def spaced(d, xy, text, font, sp, fill):
    x, y = xy; tw = sum(d.textlength(c, font=font) for c in text) + sp * (len(text) - 1); x -= tw / 2
    for c in text: d.text((x, y), c, font=font, fill=fill); x += d.textlength(c, font=font) + sp
def pin(d, x, y, s, a):                                                      # cyan map pin, tip at (x, y)
    R = 30 * s; cyc = y - 52 * s
    d.polygon([(x - R * 0.72, cyc + R * 0.62), (x + R * 0.72, cyc + R * 0.62), (x, y)], fill=CYAN + (int(255 * a),))
    d.ellipse((x - R, cyc - R, x + R, cyc + R), fill=CYAN + (int(255 * a),), outline=(255, 255, 255, int(255 * a)), width=max(int(4 * s), 1))
    d.ellipse((x - R * 0.38, cyc - R * 0.38, x + R * 0.38, cyc + R * 0.38), fill=(255, 255, 255, int(255 * a)))
def overlay(img, t, text):
    f = img.astype(np.float32)
    if t >= OFF: f = f * VIG
    f = f * ease(t / 0.3)
    a = ease((t - T_LAND + 0.2) / 0.8) if text else 0
    if a > 0: f = f * (1 - grad * a)
    im = Image.fromarray(np.clip(f, 0, 255).astype(np.uint8)[:, :, ::-1]).convert("RGBA"); lay = Image.new("RGBA", im.size); d = ImageDraw.Draw(lay)
    if t > T_LAND - 0.35:                                                   # pin drop + ripples on Jakarta
        i = min(int(round((t - OFF) * FPS)), len(TGT) - 1); px, py = TGT[i]
        u = (t - (T_LAND - 0.35)) / 0.35
        if u < 1: yoff = -260 * (1 - u) ** 2; sc = 1.0
        else:
            w_ = t - T_LAND; yoff = -18 * np.exp(-w_ * 7) * abs(np.sin(w_ * 16)); sc = 1 + 0.12 * np.exp(-w_ * 6) * np.sin(w_ * 18)
        for kq in range(3):
            w_ = t - T_LAND - kq * 0.35
            if 0 < w_ < 1.4:
                rr_ = 20 + 170 * ease(w_ / 1.4); al = int(200 * (1 - w_ / 1.4))
                d.ellipse((px - rr_, py - rr_ * 0.45, px + rr_, py + rr_ * 0.45), outline=CYAN + (al,), width=4)
        d.ellipse((px - 16, py - 6, px + 16, py + 6), fill=(0, 0, 0, int(90 * min(max(u, 0), 1))))
        pin(d, px, py + yoff, 1.15 * sc, min(1, max(u, 0) * 3))
    if text:
        a1 = ease((t - T_LAND - 0.1) / 0.7); a2 = ease((t - T_LAND - 0.55) / 0.6); a3 = ease((t - T_LAND - 0.4) / 0.7)
        if a1 > 0: spaced(d, (W/2, 1430 + 30 * (1 - a1)), "JAKARTA", FB, 34 - 16 * a1, (255, 255, 255, int(255 * a1)))
        if a3 > 0: L = 260 * a3; d.rounded_rectangle((W/2 - L, 1606, W/2 + L, 1610), 2, fill=CYAN + (int(255 * a3),))
        if a2 > 0:
            spaced(d, (W/2, 1636 + 16 * (1 - a2)), "6.2088° S  ·  106.8456° E", FR, 3, (255, 255, 255, int(235 * a2)))
            spaced(d, (W/2, 1700 + 16 * (1 - a2)), "AI PRENEUR COACHING · INDONESIA", FS, 5, CYAN + (int(255 * a2),))
    if t >= OFF: d.text((40, H - 62), "Google Earth", font=FA, fill=(255, 255, 255, 150))
    return np.array(Image.alpha_composite(im, lay).convert("RGB"))[:, :, ::-1]

def flight(t):
    i = int(round((t - OFF) * FPS)); return FL[min(max(i, 0), len(FL) - 1)]
def frame(t):
    if t < T_SHRINK0: return zoom_blur(page(t), amt(t))
    bg = flight(t)
    if t >= T_SHRINK1: return zoom_blur(bg, amt(t))
    u = (t - T_SHRINK0) / (T_SHRINK1 - T_SHRINK0); s = np.exp(np.log(0.015) * u ** 1.6)   # page shrinks away (camera pulls back)
    pg = page(t)
    M = np.float32([[s, 0, W/2 - s * W/2], [0, s, H/2 - s * H/2]])
    warped = cv2.warpAffine(pg, M, (W, H), flags=cv2.INTER_AREA)
    mask = np.zeros((H, W), np.uint8); r = int(70 * s) + 1
    x0, y0, x1, y1 = int(W/2 - s * W/2), int(H/2 - s * H/2), int(W/2 + s * W/2), int(H/2 + s * H/2)
    cv2.rectangle(mask, (x0 + r, y0), (x1 - r, y1), 255, -1); cv2.rectangle(mask, (x0, y0 + r), (x1, y1 - r), 255, -1)
    for cx_, cy_ in ((x0 + r, y0 + r), (x1 - r, y0 + r), (x0 + r, y1 - r), (x1 - r, y1 - r)): cv2.circle(mask, (cx_, cy_), r, 255, -1)
    sh = cv2.GaussianBlur(mask, (0, 0), 30 * s + 2).astype(np.float32)[..., None] / 255 * 0.55
    m = cv2.GaussianBlur(mask, (3, 3), 0).astype(np.float32)[..., None] / 255
    out = bg.astype(np.float32) * (1 - sh) ; out = out * (1 - m) + warped.astype(np.float32) * m
    fade = ease((u - 0.75) / 0.25); out = out * (1 - fade * m) + bg.astype(np.float32) * fade * m
    return zoom_blur(out.astype(np.uint8), amt(t), outward=False)

# ---- SFX (Pixabay Content License) ----
SR = 48000
def load(name):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f"assets/sfx/{name}.mp3", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).copy()
mix = np.zeros(int((D + 3) * SR), np.float32); EV = []
def put(name, t, db, peak=False, rate=1.0):
    x = load(name) * 10 ** (db / 20)
    if rate != 1.0: x = np.interp(np.arange(0, len(x), rate), np.arange(len(x)), x).astype(np.float32)
    off = int(np.argmax(np.abs(x))) if peak else 0
    s = max(int(t * SR) - off, 0); e = min(s + len(x), len(mix)); mix[s:e] += x[:e - s]; EV.append((round(float(t), 2), name))
for i, kt in enumerate(KT):
    if QUERY[i] != " ": put("key-press", kt - 0.01, -14 + rng.uniform(-2, 1), rate=rng.uniform(0.9, 1.12))
put("click-soft", T_ENTER - 0.02, -6)
put("whoosh-cinematic", T_SHRINK0 + 0.25, -4, peak=True)
put("riser", OFF + 0.6, -12)
for j, q in enumerate(PULSES): put("whoosh" if j % 2 == 0 else "whoosh-short", q, -6, peak=True)
put("impact-bass-1", T_LAND, -3, peak=True); put("pop", T_LAND - 0.02, -8); put("sparkle", T_LAND + 0.55, -12)
mix = mix[:int(D * SR)]; fo = int(0.6 * SR); mix[-fo:] *= np.linspace(1, 0, fo)
mix *= 10 ** (-1.0 / 20) / max(np.abs(mix).max(), 1e-6)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s16le", SFXW],
               input=np.repeat(mix[:, None], 2, 1).tobytes(), check=True)
print("pulses", [round(q, 2) for q in PULSES], "land", round(T_LAND, 2), "dur", round(D, 2))

def pipe(path):
    return subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                             "-i", SFXW, "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "slow", "-crf", "14", "-pix_fmt", "yuv420p",
                             "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", path], stdin=subprocess.PIPE)
pa, pc = pipe(OUT), pipe(CLEAN)
for i in range(N):
    t = i / FPS; fr = frame(t)
    pa.stdin.write(overlay(fr, t, True).tobytes()); pc.stdin.write(overlay(fr, t, False).tobytes())
for p in (pa, pc): p.stdin.close(); p.wait()
print("done", OUT, CLEAN, SFXW)

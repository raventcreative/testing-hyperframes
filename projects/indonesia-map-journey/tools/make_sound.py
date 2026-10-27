"""Motion-driven sound design (deterministic, seeded) -> assets/sfx/*.wav

bed_air.wav   82 s stereo bed computed from the camera path (data/camera_frames.json):
              deep air that grows with altitude, a filtered rush whose brightness follows camera speed
              (pans with the direction of travel), soft gusts while the camera passes the cloud layer.
swish_*.wav   paper-card unfold (3 takes), swish_back.wav retract, trace.wav boundary pen-trace,
              tick_*.wav pitched variants of the bundled key-press for connector lines.
Usage: python3 -I tools/make_sound.py
"""
import json, math, os, wave
import numpy as np
from scipy.signal import butter, sosfilt, sosfilt_zi

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "sfx")
SR = 48000
FPS = 30


def write(name, x):
    x = np.asarray(x, np.float32)
    if x.ndim == 1:
        x = np.stack([x, x], 1)
    peak = np.max(np.abs(x))
    if peak > 0.89:  # keep true peak under about -1 dBFS
        x = x * (0.89 / peak)
    pcm = (x * 32767).astype("<i2")
    with wave.open(os.path.join(OUT, name), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())


def band(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], "band", fs=SR, output="sos"), x)


def lp(x, f, order=2):
    return sosfilt(butter(order, f, "low", fs=SR, output="sos"), x)


def hp(x, f, order=2):
    return sosfilt(butter(order, f, "high", fs=SR, output="sos"), x)


def brown(rng, n):
    w = rng.standard_normal(n)
    b = np.zeros(n); acc = 0.0
    b = np.cumsum(w) ; b = b - lp(b, 8)  # remove DC drift
    return b / (np.std(b) + 1e-9)


def varband(x, centers, q=0.9, block=512):
    """time-varying band-pass: per-block coefficients, filter state carried across blocks"""
    y = np.zeros_like(x); zi = None; prev = None
    for i in range(0, len(x), block):
        c = float(centers[min(i // block, len(centers) - 1)])
        lo, hi = max(40, c / (1 + q)), min(SR / 2 - 100, c * (1 + q))
        sos = butter(2, [lo, hi], "band", fs=SR, output="sos")
        if zi is None:
            zi = sosfilt_zi(sos) * 0
        seg, zi = sosfilt(sos, x[i:i + block], zi=zi)
        y[i:i + block] = seg
    return y


def env_from_frames(vals, n):
    t = np.arange(n) / SR
    return np.interp(t, np.arange(len(vals)) / FPS, vals)


def bed():
    cams = json.load(open(os.path.join(ROOT, "data", "camera_frames.json")))
    ux = np.array([c[0] for c in cams]); uy = np.array([c[1] for c in cams]); w = np.array([c[2] for c in cams])
    k = 1920 / w
    A = 1000 / k
    alt = np.clip(np.log(A / 8) / np.log(1100 / 8), 0, 1)
    # screen speed in px/frame (pan + zoom)
    dk = np.abs(np.diff(np.log(k), prepend=np.log(k[0]))) * 900
    dp = np.hypot(np.diff(ux, prepend=ux[0]), np.diff(uy, prepend=uy[0])) * k
    sp = np.clip((dk + dp) / 70, 0, 1)
    sp = np.convolve(sp, np.ones(5) / 5, mode="same")
    pan = np.clip(np.diff(ux, prepend=ux[0]) * k / 25, -1, 1)
    pan = np.convolve(pan, np.ones(9) / 9, mode="same")
    cloud = np.exp(-((np.log(A) - np.log(300)) / 0.45) ** 2) * (sp > 0.05)
    n = int(82 * SR)
    rng = np.random.default_rng(82)
    ALT, SP, PAN, CL = (env_from_frames(v, n) for v in (alt, sp, pan, cloud))
    out = np.zeros((n, 2))
    for ch in range(2):
        r = np.random.default_rng(100 + ch)
        deep = lp(brown(r, n), 260, 4) * (0.10 + 0.22 * ALT + 0.30 * SP)
        rush_src = r.standard_normal(n)
        centers = 350 + 2600 * SP[::512] ** 1.4
        rush = varband(rush_src, centers, q=0.8) * (0.55 * SP ** 1.3)
        gust_src = lp(r.standard_normal(n), 1400, 2)
        g_mod = 0.6 + 0.4 * np.sin(2 * np.pi * (0.7 + 0.13 * ch) * np.arange(n) / SR + ch)
        gust = gust_src * CL * g_mod * 0.35
        side = (1 - PAN) / 2 if ch == 0 else (1 + PAN) / 2
        out[:, ch] = deep + rush * (0.55 + 0.9 * side) + gust
    # fade in / gentle tail under the final still
    t = np.arange(n) / SR
    out *= np.clip(t / 0.35, 0, 1)[:, None] * np.clip((82 - t) / 1.6, 0, 1)[:, None]
    out = out / (np.max(np.abs(out)) + 1e-9) * 0.6
    write("bed_air.wav", out)


def swish(seed, f0, f1, dur, attack, rev=False):
    rng = np.random.default_rng(seed)
    n = int(dur * SR); t = np.arange(n) / SR
    src = rng.standard_normal(n)
    centers = np.geomspace(f0, f1, n // 256 + 1)
    x = varband(src, centers, q=1.3, block=256)
    grain = hp(rng.standard_normal(n), 3500) * (rng.random(n) < 0.02) * 0.6  # paper fibres
    env = np.minimum(t / attack, 1) * np.exp(-np.maximum(t - attack, 0) / (dur * 0.33))
    x = (x + grain) * env
    if rev:
        x = x[::-1]
    l = x * (0.9 + 0.1 * np.sin(t * 7 + seed)); r = np.concatenate([np.zeros(24), x[:-24]])
    return np.stack([l, r], 1)


def trace(seed, dur=1.15):
    rng = np.random.default_rng(seed)
    n = int(dur * SR); t = np.arange(n) / SR
    x = band(rng.standard_normal(n), 1800, 5200, 2)
    rough = lp(np.abs(rng.standard_normal(n)), 30)  # pen pressure flutter
    env = np.clip(t / 0.08, 0, 1) * np.clip((dur - t) / 0.25, 0, 1) * (1 - 0.35 * t / dur)
    return x * (0.55 + 0.45 * rough / (rough.max() + 1e-9)) * env


def pitched(src, ratio):
    with wave.open(src, "rb") as w:
        n = w.getnframes(); ch = w.getnchannels(); sr = w.getframerate()
        a = np.frombuffer(w.readframes(n), "<i2").astype(np.float32).reshape(-1, ch) / 32768
    idx = np.arange(0, len(a), ratio * sr / SR)
    return np.stack([np.interp(idx, np.arange(len(a)), a[:, c]) for c in range(ch)], 1)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    bed()
    write("swish_a.wav", swish(1, 2600, 700, 0.55, 0.035) * 0.8)
    write("swish_b.wav", swish(2, 3200, 900, 0.5, 0.03) * 0.8)
    write("swish_c.wav", swish(3, 2200, 600, 0.6, 0.04) * 0.8)
    write("swish_back.wav", swish(4, 2400, 650, 0.45, 0.03, rev=True) * 0.8)
    write("trace.wav", trace(5) * 0.8)
    # key-press variants for connector ticks (bundled file decoded once by ffmpeg to wav)
    kp = os.path.join(OUT, "_key.wav")
    os.system(f"ffmpeg -v error -y -i {os.path.join(OUT, 'key-press.mp3')} -ar {SR} -ac 2 {kp}")
    for name, r in (("tick_a.wav", 1.0), ("tick_b.wav", 1.12), ("tick_c.wav", 0.9)):
        write(name, pitched(kp, r) * 0.9)
    os.remove(kp)
    print("sound assets written:", sorted(f for f in os.listdir(OUT) if f.endswith(".wav")))

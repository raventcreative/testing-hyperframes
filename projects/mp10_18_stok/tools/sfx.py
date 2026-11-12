"""Synthesised SFX for MasterPajak AI Video 18 (Stok Itu Uang yang Lagi Diam) — sits under the VO (no samples, no music, per the
client's rule). Beat times are parsed from window.TM in index.html (real VO word times), so a re-voice only needs
`python3 tools/sfx.py` again. Deterministic.
Sounds: warehouse air, stabilo marker, the saldo card turning edge-on, box hop + flip + cardboard knocks (one hero flip, then a
domino of eleven), a soft till "ching" on the money reveal, the pause badge, depth-of-field swell, sticker slaps + red-X buzzes +
falls, the MODAL tag clink and swing, card whooshes, LAKU stamps, money chips (whoosh + landing ticks + counter clicks), the
"jeblok" drop, the padahal hop + shimmer, band sweep, hologram fx, the pembukuan chips, the laba rugi card, stamp chime, shine,
beam/iris boom, end pops + chime. Writes assets/audio/sfx.wav (48 kHz mono, TM.total s). Run: python3 tools/sfx.py [project dir]"""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(18)
def put(t, x, g=1.0):
    i = int(t * SR); j = min(N, i + len(x))
    if i < 0 or i >= N: return
    out[i:j] += g * x[: j - i]

def svf_bp(x, f, q=1.2):
    """state-variable band-pass with a per-sample centre frequency"""
    y = np.zeros_like(x); lo = bp = 0.0
    fs = 2 * np.sin(np.pi * np.clip(f, 20, SR / 6) / SR); d = 1.0 / q
    for n in range(len(x)):
        hp = x[n] - lo - d * bp; bp += fs[n] * hp; lo += fs[n] * bp; y[n] = bp
    return y

def env(n, a=0.35, shape=2.0):
    k = int(n * a); e = np.ones(n)
    e[:k] = np.sin(np.linspace(0, np.pi / 2, k)) ** shape; e[k:] = np.cos(np.linspace(0, np.pi / 2, n - k)) ** shape
    return e

def whoosh(dur=0.6, f0=300, f1=2600, q=1.1, a=0.45):
    n = int(dur * SR); u = np.linspace(0, 1, n)
    f = f0 * (f1 / f0) ** (np.sin(np.pi * u * 0.5) ** 1.3)
    x = svf_bp(rng.standard_normal(n), f, q) * env(n, a)
    return x / (np.abs(x).max() + 1e-9)

def boom(dur=1.4, f0=95, f1=38):
    n = int(dur * SR); t = np.arange(n) / SR
    ph = 2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR
    x = np.sin(ph) * np.exp(-t * 3.2)
    nb = svf_bp(rng.standard_normal(n), np.full(n, 180.0), 0.8) * np.exp(-t * 9) * 0.6
    x = np.tanh(1.8 * (x + nb)); return x / np.abs(x).max()

def pop(f0=900, f1=320, dur=0.09):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * np.exp(-t * 38)
    return x / np.abs(x).max()

def tick(dur=0.025, f=4200):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.full(n, f), 2.0) * np.exp(-t * 260)
    return x / (np.abs(x).max() + 1e-9)

def square_blips(notes, step=0.055):
    o = []
    for f in notes:
        n = int(step * SR); t = np.arange(n) / SR
        o.append(np.sign(np.sin(2 * np.pi * f * t)) * 0.6 * np.exp(-t * 18))
    return np.concatenate(o)

def zap(dur=0.5):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(120 * (2400 / 120) ** (t / dur)) / SR) * env(n, 0.15) * 0.6
    x += np.sin(2 * np.pi * 60 * t) * 0.35 * np.exp(-t * 4) + 0.15 * np.sin(2 * np.pi * 15734 / 4 * t) * np.exp(-t * 10)
    return x / np.abs(x).max()

def chime(freqs=(1318.5, 1760, 2637), dur=1.4):
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for k, f in enumerate(freqs):
        d = int(k * 0.06 * SR); tt = t[: n - d]
        x[d:] += np.sin(2 * np.pi * f * tt) * np.exp(-tt * 3.5) * (0.8 ** k)
    return x / np.abs(x).max()

def ding(f=2093, dur=0.5):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 7) + 0.35 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 14)
    return x / np.abs(x).max()

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def knock(f=150, dur=0.22):
    """cardboard box knock: low damped body + a papery click"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 26) + 0.5 * np.sin(2 * np.pi * f * 1.9 * t) * np.exp(-t * 40)
    x += svf_bp(rng.standard_normal(n), np.full(n, 1300.0), 1.0) * np.exp(-t * 70) * 0.5
    return x / np.abs(x).max()

def paper(dur=0.3):
    """sticker / paper slap: soft noise burst with a fast low-mid body"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(2200, 900, n), 0.9) * np.exp(-t * 22)
    x += np.sin(2 * np.pi * 110 * t) * np.exp(-t * 30) * 0.6
    return x / np.abs(x).max()

def buzz(dur=0.24, f=150):
    """soft "nope" buzzer for the red X: two detuned square tones, low-passed, short"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sign(np.sin(2 * np.pi * f * t)) + np.sign(np.sin(2 * np.pi * f * 1.012 * t))
    x = svf_bp(x * 0.5, np.full(n, 700.0), 0.7) * np.minimum(1, t / 0.01) * np.minimum(1, (dur - t) / 0.05)
    return x / np.abs(x).max()

def clink(f=2400, dur=0.35):
    """metal hook clink: inharmonic partials, quick decay"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = sum(np.sin(2 * np.pi * f * r * t) * np.exp(-t * d) * g for r, d, g in ((1, 16, 1), (1.47, 22, .6), (2.09, 30, .4), (2.76, 40, .25)))
    return x / np.abs(x).max()

def till(dur=0.9):
    """soft cash-till "ching": a bright bell pair over a tiny mechanical click"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.zeros(n); d = int(0.05 * SR)
    for f, k in ((2637, 0), (3520, d)):
        tt = t[: n - k]; x[k:] += np.sin(2 * np.pi * f * tt) * np.exp(-tt * 5) + 0.3 * np.sin(2 * np.pi * f * 2.4 * tt) * np.exp(-tt * 11)
    x[: len(tick(0.02, 3000))] += tick(0.02, 3000) * 0.8
    return x / np.abs(x).max()

def drop(dur=0.75, f0=520, f1=70):
    """the "jeblok" drop: a falling sine glide into a low thud"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** ((t / dur) ** 0.8)) / SR) * env(n, 0.1, 1.0)
    return x / np.abs(x).max()

def shimmer(dur=0.8):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(4000, 9000, n), 3.0) * env(n, 0.4)
    return x / np.abs(x).max()

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

# S1 · hook: warehouse air with a slow dolly, text pops, the saldo card swings in and turns edge-on, stabilo on "tipis?"
wh(0.0, 3.2, 180, 800, 0.9, 0.5, 0.35)
put(0.3, pop(500, 900, 0.08), 0.07); put(TM['saldo'] - 0.28, pop(560, 1000, 0.08), 0.08)
wh(TM['saldo'] - 0.32, 0.55, 2400, 600, 1.2, 0.3, 0.45)
wh(TM['tipis'] + 0.1, 0.45, 600, 3600, 2.2, 0.5, 0.4); put(TM['tipis'] + 0.55, tick(0.02, 5200), 0.05)
put(TM['tipis'] + 0.2, marker(0.42), MK)
wh(TM['balik'] - 0.15, 0.45, 1800, 500, 1.1, 0.4, 0.35)
# S2 · "balik": the hero hops, flips, lands; "uang": a domino of eleven flips + a soft till ching; "diam": pause badge, stillness
put(TM['balik'] + 0.22, pop(500, 950, 0.08), 0.08); put(TM['balik'] + 0.55, marker(0.32), MK * 0.9)
wh(TM['balik'] + 0.42, 0.7, 400, 2200, 1.3, 0.5, 0.55); put(TM['balik'] + 1.1, knock(160, 0.22), 0.16)
put(TM['isi'] - 0.04, pop(600, 1100, 0.08), 0.08)
for k in range(11):
    t0 = TM['uang'] - 0.05 + k * 0.045
    put(t0, whoosh(0.32, 700, 2400, 1.3, 0.5), W * 0.16); put(t0 + 0.55, knock(150 + 12 * (k % 4), 0.16), 0.07)
put(TM['uang'] + 0.35, till(0.9), 0.07)
put(TM['diam'] - 0.05, pop(420, 840, 0.1), 0.13); put(TM['diam'] + 0.05, marker(0.38), MK)
for k in range(4): put(TM['diam'] + 0.1 + k * 0.07, tick(0.015, 3000 + 400 * k), 0.035)
# S3 · the box floats out (depth swell), two stickers slap on, get the red X + buzz, and fall away
wh(TM['bel'] - 0.05, 0.9, 250, 1600, 0.9, 0.6, 0.55)
for tHit, tX, tFall, dirg in ((TM['hangus'] - 0.32, TM['hangus'] + 0.12, TM['hangus'] + 0.85, 1.0), (TM['untung'] - 0.28, TM['untung'] + 0.14, TM['untung'] + 0.62, 1.0)):
    wh(tHit - 0.45, 0.45, 600, 2600, 1.3, 0.6, 0.5); put(tHit - 0.02, paper(0.3), 0.15)
    put(tX, marker(0.22), MK * 0.7); put(tX + 0.06, buzz(0.24, 150), 0.07); put(tX + 0.06, pop(700, 350, 0.09), 0.09)
    wh(tFall, 0.75, 2000, 300, 1.0, 0.25, 0.4)
put(TM['hangus'] - 0.55, pop(520, 980, 0.08), 0.06); put(TM['untung'] - 0.8, pop(540, 1000, 0.08), 0.06)
# S4 · back into its slot, the MODAL tag clinks onto the hook and swings, stabilo on "modal"
wh(TM['modal'] - 0.08, 0.7, 1800, 300, 1.0, 0.35, 0.5); put(TM['modal'] + 0.52, knock(140, 0.22), 0.15)
wh(TM['modal'] + 0.2, 0.5, 500, 2200, 1.2, 0.6, 0.4); put(TM['modal'] + 0.68, clink(2400, 0.35), 0.06)
for k, dt in enumerate((0.9, 1.3, 1.7)): put(TM['modal'] + dt, tick(0.02, 2800 - 300 * k), 0.025)
put(TM['modal'] + 0.25, marker(0.34), MK); put(TM['nyangkut'] + 0.05, pop(480, 900, 0.08), 0.06)
# "baru jadi biaya pas barangnya laku": BIAYA card in, two LAKU stamps, chips fly to BIAYA, counter clicks, boxes leave
wh(TM['biaya'] - 0.05, 0.6, 2200, 500, 1.1, 0.35, 0.45); put(TM['biaya'] + 0.95, marker(0.32), MK)
for i in range(2):
    t0 = TM['laku'] + 0.05 + i * 0.22
    wh(t0 + 0.02, 0.45, 500, 1800, 1.2, 0.5, 0.25)
    put(t0 + 0.64, knock(120, 0.25), 0.18); put(t0 + 0.66, pop(320, 160, 0.12), 0.1)
    wh(t0 + 0.07, 0.75, 800, 2600, 1.3, 0.5, 0.25); put(t0 + 0.8, tick(0.02, 3600), 0.08)
    wh(t0 + 0.88, 0.7, 1800, 300, 1.0, 0.3, 0.4)
put(TM['laku'] + 0.8, tick(0.016, 2600), 0.08); put(TM['laku'] + 1.02, tick(0.016, 2900), 0.08)
# S5 · "dianggap biaya": all chips stream into BIAYA (ticks), the MODAL tag drops, BIAYA shakes; LABA card; "jeblok" drop
for k in range(10):
    t0 = TM['semua'] + 0.1 + k * 0.06
    put(t0, whoosh(0.4, 900, 2800, 1.4, 0.5), W * 0.12); put(t0 + 0.68, tick(0.014, 3200 + 150 * (k % 4)), 0.05)
wh(TM['semua'] + 0.2, 0.7, 1600, 250, 1.0, 0.3, 0.3)
put(TM['semua'] + 0.75, tick(0.016, 2400), 0.09); put(TM['semua'] + 0.8, buzz(0.3, 110), 0.06)
wh(TM['jeblok'] - 0.1, 0.6, 2200, 500, 1.1, 0.35, 0.45)
put(TM['jeblok'] + 0.72, drop(0.75, 520, 70), 0.14); put(TM['jeblok'] + 1.12, knock(90, 0.35), 0.2); put(TM['jeblok'] + 1.14, boom(0.6, 120, 45), 0.08)
# "padahal barangnya masih ada": cards swish out, the camera swings back, ten soft hops, a shimmer, MASIH DI RAK card
wh(TM['padahal'] - 0.05, 0.6, 600, 2400, 1.1, 0.5, 0.45); wh(TM['padahal'] + 0.1, 0.9, 300, 1200, 0.9, 0.5, 0.3)
for k in range(10): put(TM['padahal'] + 0.73 + k * 0.045, knock(170 + 10 * (k % 3), 0.12), 0.05)
put(TM['padahal'] + 0.6, shimmer(0.9), 0.04)
wh(TM['padahal'] + 0.75, 0.55, 2200, 500, 1.1, 0.35, 0.35); put(TM['padahal'] + 1.12, marker(0.3), MK)
# band sweep -> brand
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
# S6 · brand: the pembukuan card rises, hologram, three chips arc in, captions, the laba rugi lifts out, stamp + chime, shine
wh(TM['sol'] + 0.3, 0.8, 250, 2000, 1.0, 0.45, 0.5)
holo_fx(TM['sol'] + 0.55)
for k in range(3):
    t = TM['catat'] - 0.1 + k * 0.28
    put(t, whoosh(0.45, 900, 2600, 1.4, 0.5), W * 0.35); put(t + 0.58, pop(520 + 90 * k, 1050 + 120 * k, 0.08), 0.12)
put(TM['pemb'] + 0.5, marker(0.42), MK)
for g0 in (TM['pemb'] + 0.9, TM['lr'] + 1.7, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
wh(TM['lr'], 0.8, 1600, 300, 0.9, 0.5, 0.35); wh(TM['lr'] + 0.18, 0.8, 250, 2400, 1.0, 0.45, 0.6)
put(TM['bener'] - 0.1, marker(0.42), MK); put(TM['bener'] + 0.36, pop(600, 1300, 0.09), 0.14); put(TM['bener'] + 0.42, chime((1568, 2093, 2637), 1.1), 0.06)
put(TM['bener'] + 0.5, marker(0.42), MK * 0.8); put(TM['bener'] + 0.6, shimmer(0.8), 0.03)
# beam + iris -> end
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 1.2, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")

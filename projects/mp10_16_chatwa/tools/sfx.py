"""Synthesised SFX for MasterPajak AI Video 16 (Dari Chat ke Catatan Rapi) — sits under the VO (no samples, no music, per the client's rule).
Beat times are parsed from window.TM in index.html (real VO word times), so a re-time only needs `python3 tools/sfx.py` again.
Deterministic. Sounds: chat message blips (generic two-tone, no app's notification sound), spill pops, unread-badge ticks, stabilo
marker strokes, text pops, the three read-out bubbles lifting (rising air + soft ding), the sigh drop (falling air + papery thuds),
the pile (soft landings), the lost bubble (teeter ticks, slide, long falling whoosh), the sheet flying in, each order bubble peeling
off and landing as a row (flutter + whoosh + pop/ding up the scale), cell ticks on "tanggal, pesanan, nominal", total row, five check
pops on "dicek", band sweep, hologram fx, card flip, trace zip + source chip chime, beam/iris boom, end pops + chime.
Writes assets/audio/sfx.wav (48 kHz mono, TM.total s). Run: python3 tools/sfx.py [project dir]"""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(16)
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
    """bright check-mark ding: a sine + soft inharmonic partial, fast decay"""
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
    """paper slap / settle: soft noise burst with a fast low-mid body"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(2200, 900, n), 0.9) * np.exp(-t * 22)
    x += np.sin(2 * np.pi * 110 * t) * np.exp(-t * 30) * 0.6
    return x / np.abs(x).max()

def flutter(dur=0.5):
    """paper flutter: AM-chopped band noise"""
    n = int(dur * SR); t = np.arange(n) / SR
    am = 0.55 + 0.45 * np.sign(np.sin(2 * np.pi * (16 + 8 * t / dur) * t))
    x = svf_bp(rng.standard_normal(n), 2400 + 700 * np.sin(2 * np.pi * 5 * t), 1.3) * am * env(n, 0.25)
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

def blip(f0=1320, f1=1760, dur=0.11):
    """generic chat 'message in' blip: two short sine tones (not any app's notification sound)"""
    n = int(dur * SR); t = np.arange(n) / SR; h = n // 2
    x = np.zeros(n); x[:h] = np.sin(2 * np.pi * f0 * t[:h]); x[h:] = np.sin(2 * np.pi * f1 * t[h:])
    x *= np.exp(-((t % (dur / 2)) * 28)); return x / np.abs(x).max()

BM = 0.15   # this film's beam/iris runs 0.15 s later than the series default
# ---- S1 · hook: the chat floods, bubbles spill out, the unread badge climbs ----
wh(0.0, 2.4, 200, 900, 0.9, 0.5, 0.3)
for i, t in enumerate([0.5, 0.86, 1.22, 1.75, 2.32, 2.92]): put(t + 0.04, blip(1250 + 40 * i, 1700 + 40 * i), 0.07)
for k, t in enumerate([0.42, 0.78, 1.12, 1.46, 1.8, 2.14, 2.48, 2.82]):
    put(t, pop(600 + 50 * (k % 4), 1150 + 60 * (k % 3), 0.07), 0.06); put(t + 0.02, whoosh(0.45, 700, 2600, 1.4, 0.4), W * 0.18)
for t in (0.62, 1.5, 2.4, 3.2, TM['numpukw']): put(t, tick(0.018, 3600), 0.06)
put(TM['hook'] + 0.55, pop(500, 900, 0.08), 0.08); put(TM['chatw'] + 0.05, marker(0.38), MK)
put(TM['dicatat'] + 0.1, pop(520, 980, 0.08), 0.08); put(TM['mana'], marker(0.38), MK)
# ---- S2 · the three read-out bubbles lift toward the lens ----
wh(TM['b1'] - 0.15, 0.9, 300, 1200, 1.0, 0.5, 0.35)
for k, t in enumerate([TM['b1'], TM['b2'], TM['b3']]):
    wh(t, 0.55, 400 + 80 * k, 2400 + 200 * k, 1.2, 0.35, 0.55); put(t + 0.12, ding(1568 * (1.0595 ** (3 * k)), 0.5), 0.05)
    put(t + 0.05, pop(700, 1300, 0.07), 0.07)
# ---- S3 · sigh: they drop back onto the screen; the pile; the lost bubble ----
wh(TM['sigh'] + 0.05, 0.5, 2200, 400, 1.0, 0.3, 0.5)
for k in range(3): put(TM['sigh'] + 0.47 + k * 0.07, paper(0.25), 0.11)
for k, t in enumerate([8.6, 8.78, 8.96, 9.14, 9.32, 9.52]):
    t = t - 8.567 + TM['numpuk']; put(t, whoosh(0.3, 2400, 700, 1.1, 0.3), W * 0.25); put(t + 0.29, paper(0.22), 0.1); put(t + 0.3, pop(380 + 40 * k, 700 + 60 * k, 0.07), 0.07)
put(TM['numpuk'] + 0.3, pop(500, 900, 0.08), 0.07); put(TM['numpukw'] + 0.05, marker(0.33), MK)
put(TM['numpukw'], pop(800, 1500, 0.08), 0.09)
for dt in (0.02, 0.28, 0.52): put(TM['lost'] + dt, tick(0.02, 2400), 0.07)
put(TM['lostw'] - 0.02, tick(0.02, 2200), 0.08)
wh(TM['lostw'], 0.35, 600, 1800, 1.0, 0.5, 0.35); wh(TM['lostw'] + 0.3, 1.1, 1800, 160, 0.9, 0.2, 0.7)
put(TM['lost'] + 0.02, pop(480, 880, 0.08), 0.07); put(TM['lostw'] + 0.3, marker(0.38), MK)
# ---- S4 · the phone sinks, the sheet flies in; the first order bubble peels off and lands as row 1 ----
wh(TM['catat'], 0.95, 300, 1400, 1.0, 0.6, 0.6); wh(TM['catat'] + 0.12, 0.85, 2400, 500, 1.0, 0.25, 0.5)
put(TM['catat'] + 1.0, paper(0.3), 0.14); put(TM['catat'] + 0.5, pop(500, 950, 0.08), 0.08)
put(TM['baris'] + 0.1, marker(0.42), MK)
FT = [TM['baris'] - 0.05, TM['satu'] - 0.12, TM['satu'] + 0.2, TM['satu'] + 0.52, TM['satu'] + 0.84]; D = 0.62
for k, t in enumerate(FT):
    put(t, flutter(0.3), 0.05); wh(t, D, 500, 2600 + 150 * k, 1.2, 0.5, 0.55)
    put(t + D - 0.03, pop(620 + 70 * k, 1250 + 120 * k, 0.08), 0.12); put(t + D, ding(1760 * (1.0595 ** (2 * k)), 0.45), 0.05)
for k, t in enumerate([TM['tgl'], TM['psn'], TM['nom']]): put(t, marker(0.28), MK * 0.75); put(t + 0.05, tick(0.02, 3000 + 400 * k), 0.08)
# ---- S5 · satu pesanan, satu baris; rapi (total row); dicek (five checks) ----
put(TM['satu'] + 0.05, pop(520, 980, 0.08), 0.07); put(TM['satu2'] + 0.3, marker(0.35), MK)
wh(TM['rapi'] + 0.02, 0.4, 1500, 500, 1.0, 0.4, 0.3); wh(TM['rapi'] + 0.12, 0.45, 400, 1600, 1.0, 0.5, 0.3); put(TM['rapi'] + 0.4, knock(140, 0.2), 0.08)
put(TM['cek'], marker(0.4), MK)
for k in range(5): put(TM['cek'] + k * 0.08, pop(700 + 80 * k, 1400 + 140 * k, 0.07), 0.1)
put(TM['cek'] + 0.45, chime((1568, 2093, 2637), 1.0), 0.05)
# ---- band sweep -> brand ----
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.15)
wh(TM['sol'] + 0.05, 0.9, 2000, 400, 1.0, 0.35, 0.45); put(TM['sol'] + 0.9, knock(130, 0.2), 0.1)
put(TM['sol'] + 0.75, pop(500, 900, 0.08), 0.06)
# the flip into "Pembukuan", underline, then the trace: link pop, zip along the line, chip pop + chime
wh(TM['pemb'] - 0.62, 0.66, 300, 2600, 1.3, 0.6, 0.6); put(TM['pemb'] + 0.04, knock(120, 0.2), 0.12); put(TM['pemb'], pop(520, 980, 0.08), 0.08)
put(TM['pemb'] + 0.4, marker(0.4), MK)
put(TM['bisa'] + 0.1, pop(900, 1600, 0.07), 0.1); put(TM['bisa'] + 0.22, shimmer(0.55), 0.05); wh(TM['bisa'] + 0.22, 0.5, 900, 3400, 1.8, 0.6, 0.3)
put(TM['telusur'] - 0.1, pop(600, 1200, 0.09), 0.12); put(TM['telusur'] + 0.05, chime((1318.5, 1760, 2637), 1.1), 0.06)
put(TM['telusur'] + 0.3, marker(0.35), MK)
for g0 in (TM['sol'] + 2.6, TM['telusur'] + 0.2, TM['cta'] + 1.2, TM['bio'] + 1.2): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# ---- beam + iris -> end card ----
put(TM['end'] - 0.5 + BM, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45 + BM, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02 + BM, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.1 + 0.55)
put(TM['urus'] - 0.05, pop(480, 900, 0.08), 0.06)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 1.0, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")

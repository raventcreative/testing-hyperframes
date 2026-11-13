"""Synthesised SFX for MasterPajak AI Video 30 (Usahamu Untung Berapa?) — sits under the VO (no samples, no music, per the client's rule).
Beat times are parsed from window.TM in index.html, so a VO re-time only needs `python3 tools/sfx.py` again. Deterministic.
Sounds: quiet meeting-room air, camera push, caption pops, the question bubble + stabilo strokes, the split panels sliding in
(whoosh pair + clack), divider slides, question-mark boings + sweat drips, the paper burst (flutter), hero paper slaps, papers
raining onto the table, the "Rp ???" wobble, a calm sparkle + chime, tablet lift / tap / push, report-row ticks, "jelas" ding,
badges (ding / soft nope), band sweep, hologram fx, notes flying into the brand tablet, report build + chime, answer ding,
beam/iris boom, end pops + chime. Writes assets/audio/sfx.wav (48 kHz mono, TM.total s).
Run: python3 tools/sfx.py [project dir]"""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(30)
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


def boing(f0=520, f1=980, dur=0.22):
    """cartoon question-mark pop: a short upward glide with a wobble"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 * (f1 / f0) ** (t / dur) * (1 + 0.06 * np.sin(2 * np.pi * 22 * t))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 11)
    return x / np.abs(x).max()

def drip(dur=0.18):
    """sweat drop: a falling water blip"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(1500 * (500 / 1500) ** (t / dur)) / SR) * np.exp(-t * 20)
    return x / np.abs(x).max()

def nope(dur=0.34):
    """soft two-tone 'nope' for the ✕ badge (low, rounded, not harsh)"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = np.where(t < dur / 2, 392.0, 311.0)
    x = (np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.3 * np.sin(2 * np.pi * np.cumsum(2 * f) / SR)) * env(n, 0.08, 1.0)
    return x / np.abs(x).max()

def tap(f=900, dur=0.07):
    """glass tablet tap"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 70) + 0.4 * svf_bp(rng.standard_normal(n), np.full(n, 3500.0), 2.0) * np.exp(-t * 120)
    return x / np.abs(x).max()

def room(dur):
    """quiet meeting-room air: low band noise, very soft"""
    n = int(dur * SR)
    x = svf_bp(rng.standard_normal(n), np.full(n, 260.0), 0.7)
    x *= np.minimum(1, np.arange(n) / (0.4 * SR)) * np.minimum(1, (n - np.arange(n)) / (0.5 * SR))
    return x / (np.abs(x).max() + 1e-9)

# S1 · hook: room air, camera push, caption pops, the question bubble + its words, two stabilo strokes, the pen tick
put(0.0, room(TM['sigh'] + 0.3), 0.05)
wh(0.0, 3.4, 180, 700, 0.9, 0.5, 0.3)
put(TM['hook'] - 0.1, pop(480, 900, 0.08), 0.07)
put(TM['nanya'] - 0.15, tick(0.02, 3000), 0.05)
put(TM['usaha'] - 0.3, pop(380, 820, 0.12), 0.13); wh(TM['usaha'] - 0.32, 0.35, 700, 2200, 1.2, 0.4, 0.25)
for k in ('usaha', 'untung', 'berapa', 'sebulan'): put(TM[k] - 0.08, pop(560, 1050, 0.07), 0.07)
put(TM['berapa'] - 0.05, marker(0.3), MK * 0.9); put(TM['sebulan'] + 0.05, marker(0.3), MK * 0.9)
# split: two panels slide in (left + right whoosh), they meet with a soft clack, the divider draws (same cut times as index.html)
tS = max(TM['sebulan'] + 0.45, TM['a'] - 0.98); tS4 = TM['beda'] - 0.3
wh(tS - 0.04, 0.5, 300, 2400, 1.1, 0.6, 0.55); wh(tS, 0.5, 350, 2600, 1.1, 0.6, 0.5)
put(tS + 0.4, knock(170, 0.18), 0.12); put(tS + 0.32, tick(0.02, 3600), 0.06)
# divider slides (A focus / B focus / both)
for t in (TM['a'] - 0.13, TM['b'] - 0.2, tS4): wh(t, 0.6, 500, 1800, 1.0, 0.5, 0.35)
# S2 · Penjual A
put(TM['a'] - 0.12, pop(460, 880, 0.08), 0.07); put(TM['bingung'] - 0.1, pop(520, 980, 0.08), 0.08)
for k in range(3): put(TM['bingung'] + 0.06 + k * 0.13, boing(520 + 90 * k, 980 + 120 * k, 0.22), 0.09)
put(TM['bingung'] + 0.35, drip(0.18), 0.08)
# "bongkar": the pile bursts (flutter + upward whoosh), each hero paper slaps into place, "kececer": papers rain down onto the table
wh(TM['bongkar'], 0.55, 400, 3200, 1.0, 0.35, 0.6); put(TM['bongkar'] + 0.02, flutter(0.9), 0.09)
for k in ('nota', 'chat', 'catatan'): wh(TM[k] - 0.2, 0.35, 900, 2600, 1.3, 0.5, 0.35); put(TM[k] + 0.2, paper(0.25), 0.1); put(TM[k] - 0.1, pop(520, 1000, 0.07), 0.06)
wh(TM['kececer'], 0.6, 2400, 500, 1.0, 0.3, 0.45); put(TM['kececer'] + 0.05, flutter(0.7), 0.07)
for k in range(7): put(TM['kececer'] + 0.55 + k * 0.06 + 0.02 * (k % 3), paper(0.22), 0.07 + 0.01 * (k % 2))
put(TM['kececer'] + 0.35, marker(0.34), MK)
# "Jawabnya: kira-kira" — bubble pop, the "Rp ???" pill wobble, a second drip
put(TM['jawab'] + 0.35, pop(400, 860, 0.12), 0.12)
put(TM['kira'] + 0.3, boing(600, 1100, 0.2), 0.08)
for j in range(3): put(TM['kira'] + 0.5 + j * 0.15, tick(0.02, 2600 + 300 * j), 0.04)
put(TM['kira'] + 0.25, drip(0.18), 0.07)
# S3 · Penjual B: calm sparkle, the tablet lifts (whoosh + tap), pushes in, rows fill, "jelas" ding
put(TM['b'] - 0.1, pop(460, 880, 0.08), 0.07); put(TM['tenang'] - 0.1, pop(520, 980, 0.08), 0.07)
put(TM['tenang'], shimmer(0.7), 0.04); put(TM['tenang'] + 0.05, chime((1568, 2093, 2637), 1.0), 0.04)
put(TM['tenang'] + 0.3, marker(0.34), MK * 0.9)
wh(TM['buka'] - 0.12, 0.5, 300, 1500, 1.0, 0.6, 0.35); put(TM['buka'] + 0.33, tap(880, 0.07), 0.08)
wh(TM['lap'] - 0.05, 0.6, 250, 1200, 0.9, 0.5, 0.3)
for k, t in enumerate((TM['pj'] - 0.05, TM['by'] - 0.08, TM['by'] + 0.12, TM['laba'] - 0.05)): put(t, tick(0.02, 3000 + 250 * k), 0.07); put(t + 0.02, pop(560 + 60 * k, 1100 + 80 * k, 0.07), 0.07)
put(TM['jelas'] - 0.05, pop(700, 1400, 0.07), 0.1); put(TM['jelas'], ding(2349, 0.55), 0.07)
# S4 · both: caption pops, stabilo, badges (✓ ding / ✕ soft nope)
put(TM['beda'] - 0.1, pop(480, 900, 0.08), 0.07); put(TM['gede'] - 0.1, pop(520, 980, 0.08), 0.07)
put(TM['tapi'] - 0.05, pop(480, 900, 0.08), 0.07); put(TM['ada'] - 0.1, pop(540, 1000, 0.08), 0.06)
put(TM['data'] + 0.3, marker(0.34), MK)
put(TM['ada'], pop(700, 1400, 0.08), 0.11); put(TM['ada'] + 0.04, ding(2093, 0.5), 0.07)
put(TM['nggak'] - 0.05, pop(500, 800, 0.08), 0.09); put(TM['nggak'], nope(0.34), 0.05)
# band sweep -> brand
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
# S5 · brand: tablet swings up, hologram, notes fly in and dive into the tablet, the report builds, the question + answer
wh(TM['sol'] + 0.2, 0.8, 250, 2200, 1.0, 0.45, 0.55)
holo_fx(TM['sol'] + 0.55)
for t in (TM['cat'] - 0.25, TM['jual'] - 0.15, TM['biaya'] - 0.25, TM['biaya'] + 0.05): wh(t, 0.45, 600, 2600, 1.2, 0.5, 0.4); put(t + 0.45, paper(0.2), 0.06)
put(TM['lr'] - 0.5, flutter(0.6), 0.07)
for k in range(4): put(TM['lr'] - 0.08 + k * 0.06, whoosh(0.3, 2400, 700, 1.4, 0.4), W * 0.25)
for k in range(4): put(TM['lr'] + 0.05 + k * 0.13, pop(520 + 90 * k, 1050 + 120 * k, 0.08), 0.1); put(TM['lr'] + 0.05 + k * 0.13, tick(0.016, 3600), 0.05)
put(TM['lr'] + 0.55, chime((1318.5, 1760, 2637), 1.2), 0.06)
put(TM['cat'] - 0.1, pop(480, 900, 0.08), 0.06); put(TM['biaya'] + 0.35, marker(0.42), MK)
put(TM['biar'] - 0.05, pop(400, 860, 0.12), 0.12); put(TM['pakai'] - 0.05, pop(700, 1400, 0.08), 0.1); put(TM['pakai'], ding(2093, 0.5), 0.06)
put(TM['dat'] + 0.05, marker(0.38), MK)
for g0 in (TM['sol'] + 2.9, TM['lr'] + 1.1, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# beam + iris -> end
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['cta'] - 0.1, pop(500, 1000, 0.12), P_); put(TM['bio'] - 0.05, pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 1.2, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")

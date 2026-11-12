"""Synthesised SFX for MasterPajak AI Video 23 (Utang ke Supplier Jangan Cuma di Kepala) — sits under the VO (no samples, no music, per the client's rule).
Beat times are parsed from window.TM in index.html, so a VO re-time only needs `python3 tools/sfx.py` again. Deterministic.
Sounds: studio air + orbiting paper flutters, stabilo marker strokes, hero-note swings (whoosh + paper slap + ding), the orbit
speeding up (rising whirl + dizzy wobble), the slipping note (slide whistle), whip pan, the bill flying in and slapping down,
"kaget" (boing + pop), the cash drawer sliding open + stop knock + dust, the bar card swing, "BELUM DICATAT" stamp thump, bar
growth tone, the chunk peeling off, strike-through scratch, band sweep, hologram fx, notes flying into the ledger rows (flutter +
landing pops), column clicks, check pops with rising dings, the riwayat pop, beam/iris boom, end pops + chime.
Writes assets/audio/sfx.wav (48 kHz mono, TM.total s).
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
rng = np.random.default_rng(23)
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

def slide_whistle(dur=0.9, f0=1500, f1=320):
    """cartoon slide whistle (falling note): a gliding sine with a little vibrato and breath noise"""
    n = int(dur * SR); t = np.arange(n) / SR; u = t / dur
    f = f0 * (f1 / f0) ** (u ** 1.4) * (1 + 0.012 * np.sin(2 * np.pi * 7 * t))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.12, 1.2)
    x += svf_bp(rng.standard_normal(n), f * 1.0, 3.0) * 0.18 * env(n, 0.12, 1.2)
    return x / np.abs(x).max()

def dizzy(dur=1.4, f0=420, f1=900):
    """dizzy swirl: two detuned rising wobbles (cartoon spinning stars)"""
    n = int(dur * SR); t = np.arange(n) / SR; u = t / dur
    f = f0 * (f1 / f0) ** u
    wob = 1 + 0.06 * np.sin(2 * np.pi * (5 + 6 * u) * t)
    x = np.sin(2 * np.pi * np.cumsum(f * wob) / SR) + 0.6 * np.sin(2 * np.pi * np.cumsum(f * 1.5 * wob) / SR + 1.0)
    return x * env(n, 0.6, 1.5) / 1.6

def boing(dur=0.45, f0=180, f1=520):
    """surprise boing: a springy pitch bounce"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 + (f1 - f0) * np.abs(np.sin(2 * np.pi * 6 * t)) * np.exp(-t * 5)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 6)
    return x / np.abs(x).max()

def drawer(dur=0.42):
    """drawer slide: rolling rumble (low band noise with a slow AM) ending in a stop knock"""
    n = int(dur * SR); t = np.arange(n) / SR
    am = 0.6 + 0.4 * np.sin(2 * np.pi * 38 * t)
    x = svf_bp(rng.standard_normal(n), np.linspace(420, 260, n), 1.4) * am * env(n, 0.2, 1.0)
    return x / np.abs(x).max()

def stamp(dur=0.3):
    """rubber stamp thump: a dull low hit with a papery smack"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * 85 * t) * np.exp(-t * 22) + 0.8 * svf_bp(rng.standard_normal(n), np.full(n, 900.0), 0.8) * np.exp(-t * 45)
    return x / np.abs(x).max()

def scratch(dur=0.3):
    """pen strike-through: a quick scratchy stroke"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(1800, 3200, n), 2.2) * np.minimum(1, t / 0.02) * np.minimum(1, (dur - t) / 0.05)
    x *= 0.7 + 0.3 * np.sign(np.sin(2 * np.pi * 60 * t))
    return x / np.abs(x).max()

def rise(dur=0.7, f0=220, f1=660):
    """bar growth: a soft rising tone with a little shimmer"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 * (f1 / f0) ** (t / dur)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.75, 1.2) + 0.3 * svf_bp(rng.standard_normal(n), f * 6, 4.0) * env(n, 0.7, 1.2)
    return x / np.abs(x).max()

WH = TM['pas'] - 0.16
ACC = TM['dibayar'] + 0.75
# S1 · hook: studio air, the notes orbit (paper flutter swells), text pops, stabilo on "di kepala?"
wh(0.0, 2.8, 200, 900, 0.9, 0.5, 0.35)
for j in range(4): put(0.2 + j * 0.8, flutter(0.6), 0.035)
put(TM['hook'] + 0.05, pop(500, 900, 0.08), 0.07); put(TM['masih'] + 0.1, pop(560, 1000, 0.08), 0.07)
put(TM['kepala'] + 0.3, marker(0.42), MK)
# S2 · each named note swings forward: whoosh + paper slap + a little ding
for k, t in enumerate([TM['kain'] - 0.12, TM['kemas'] - 0.1, TM['sablon'] - 0.1]):
    wh(t - 0.05, 0.45, 400, 1800, 1.2, 0.5, 0.45); put(t + 0.32, paper(0.25), 0.11); put(t + 0.36, ding(1760 * (1.0595 ** (3 * k)), 0.45), 0.045)
for t in [TM['kemas'] - 0.45, TM['sablon'] - 0.45]: put(t, flutter(0.55), 0.05)
# S3 · "lama-lama": the orbit accelerates (rising whirl + dizzy wobble), "lupa": the sablon note slips (slide whistle down), stabilo
wh(ACC, TM['lupa'] - ACC + 0.2, 200, 1600, 1.0, 0.85, 0.45)
put(TM['lama'] + 0.1, dizzy(TM['lupa'] - TM['lama'] + 0.6), 0.05)
for j in range(6): put(ACC + 0.6 + j * 0.28, flutter(0.35), 0.03 + 0.006 * j)
put(TM['lupa'] - 0.02, pop(900, 500, 0.08), 0.1); put(TM['lupa'] + 0.02, slide_whistle(1.0), 0.07)
put(TM['lupa'] + 0.05, marker(0.35), MK); put(TM['lupa'] + 0.3, whoosh(0.9, 1200, 300, 1.0, 0.3), W * 0.25)
# whip pan to the counter
wh(WH - 0.04, 0.55, 250, 3200, 0.9, 0.55, 1.1)
# S4 · "pas ditagih": the bill flies in and slaps down; the lost note flutters back; "kaget": boing + "!" pop; drawer opens empty, dust
wh(TM['tagih'] - 0.08, 0.6, 2200, 500, 1.1, 0.35, 0.6); put(TM['tagih'] + 0.5, paper(0.3), 0.15)
put(TM['kaget'] - 0.4, flutter(0.45), 0.06); put(TM['kaget'] + 0.08, pop(600, 1200, 0.08), 0.09)
put(TM['kaget'] - 0.06, boing(0.5), 0.13); put(TM['kaget'] - 0.04, pop(500, 1100, 0.1), 0.12)
for j in range(4): put(TM['kaget'] + j * 0.07, tick(0.018, 2400 + 200 * j), 0.05)
put(TM['uang'], drawer(0.42), 0.16); put(TM['uang'] + 0.38, knock(160, 0.2), 0.12)
put(TM['uang'] + 0.3, whoosh(0.8, 900, 300, 0.8, 0.3), W * 0.25)
put(TM['pakai'] + 0.05, marker(0.42), MK)
# S5 · the studio blurs, the bar card swings up; stamp "BELUM DICATAT"; the bar grows; the chunk peels; strike + stabilo
wh(TM['utang2'] - 0.05, 0.9, 1500, 300, 0.9, 0.4, 0.35); wh(TM['utang2'] + 0.05, 0.85, 250, 2400, 1.0, 0.45, 0.6)
put(TM['utang2'] + 0.42, whoosh(0.35, 800, 2200, 1.4, 0.5), W * 0.25)
put(TM['catat'] + 0.24, stamp(0.3), 0.18)
put(TM['untung'], rise(0.75), 0.06); put(TM['untung'] + 0.32, pop(560, 1100, 0.08), 0.08)
put(TM['lihat'] + 0.45, tick(0.02, 3000), 0.06); put(TM['gede'], marker(0.38), MK); put(TM['gede'] + 0.02, pop(700, 1300, 0.07), 0.07)
wh(TM['dari'] - 0.04, 0.55, 400, 2800, 1.2, 0.5, 0.55); put(TM['dari'] + 0.48, pop(500, 900, 0.09), 0.09)
put(TM['asli'] - 0.15, scratch(0.3), 0.07); put(TM['asli'] + 0.05, marker(0.38), MK); put(TM['asli'] + 0.1, ding(2093, 0.5), 0.05)
# band sweep -> brand
BS = TM['sol'] - 0.32
for k in range(3): wh(BS - 0.05 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
# S6 · brand: card swings up, avatar pops, hologram; three notes leave the head and land in the rows; the avatar smiles
wh(TM['sol'] + 0.25, 0.9, 250, 2200, 1.0, 0.45, 0.5); put(TM['sol'] + 0.4, pop(600, 1200, 0.09), 0.1)
holo_fx(TM['sol'] + 0.55)
for k in range(3):
    t = TM['pindah'] + 0.2 + k * 0.3
    put(t, pop(900, 1500, 0.06), 0.06); put(t + 0.02, flutter(0.6), 0.05); put(t, whoosh(0.8, 800, 2400, 1.3, 0.5), W * 0.3)
    put(t + 0.82, pop(520 + 90 * k, 1050 + 120 * k, 0.08), 0.12); put(t + 0.86, tick(0.016, 4200), 0.05)
put(TM['pemb'] + 0.35, marker(0.45), MK); put(TM['pemb'] + 0.45, chime((1318.5, 1760, 2637), 1.0), 0.05)
for g0 in (TM['sol'] + 2.9, TM['semua'] + 0.6, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# "ke siapa, berapa, sisanya berapa": column flashes (soft clicks), stabilo on sisa + total
for t in (TM['siapa'] - 0.05, TM['berapa'] - 0.05, TM['sisa']): put(t, tick(0.02, 2600), 0.08); put(t + 0.01, pop(700, 1000, 0.05), 0.04)
put(TM['sisa'] + 0.05, marker(0.32), MK * 0.9); put(TM['sisab'], marker(0.36), MK)
# "semua kecatat": three check pops with rising dings
for k in range(3): t = TM['catat2'] - 0.1 + k * 0.12; put(t, pop(700, 1400, 0.07), 0.11); put(t + 0.04, ding(2093 * (1.0595 ** (2 * k)), 0.5), 0.05)
# "bisa ditelusuri": the trace runs, the riwayat pops; underline
put(TM['bisa'] - 0.15, whoosh(0.5, 1400, 3200, 1.6, 0.5), W * 0.3); put(TM['bisa'] - 0.05, pop(600, 1200, 0.09), 0.11)
put(TM['telusur'] + 0.35, marker(0.45), MK)
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

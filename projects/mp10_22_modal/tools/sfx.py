"""Synthesised SFX for MasterPajak AI Video 22 (Modal Masuk Bukan Penjualan) — sits under the VO (no samples, no music).
Beat times are parsed from window.TM in index.html, so a VO re-time only needs `python3 tools/sfx.py` again. Deterministic.
Sounds: conveyor motor hum + roller ticks, camera air, caption pops, stabilo marker, emergency-stop brake + token rattle, lane
whooshes + junction blips, board header knock, scan gate drop (clunk + bounces) + gate hum, scan beeps + flip whooshes on every
token, side boards rising (whoosh + knock), the sorter's jumps (boing + whoosh) and coin dings when a board counts, gauge ratchet
ticks, rubber stamps ("bukan hasil jualan", "tetap"), the false jump (coin dings + rising tones + a two-pulse warning), a soft
"huh?" droop on "padahal", band sweep, hologram fx, card swing + row pops + chip blips, beam/iris boom, end pops + chime.
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
rng = np.random.default_rng(20)
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
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def knock(f=150, dur=0.22):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 26) + 0.5 * np.sin(2 * np.pi * f * 1.9 * t) * np.exp(-t * 40)
    x += svf_bp(rng.standard_normal(n), np.full(n, 1300.0), 1.0) * np.exp(-t * 70) * 0.5
    return x / np.abs(x).max()

def shimmer(dur=0.8):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(4000, 9000, n), 3.0) * env(n, 0.4)
    return x / np.abs(x).max()

def clunk(dur=0.35):
    """studio lamp switching on: a heavy relay clunk + a short warm mains hum"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * 85 * t) * np.exp(-t * 30) + svf_bp(rng.standard_normal(n), np.full(n, 900.0), 1.5) * np.exp(-t * 90) * 0.8
    x += (np.sin(2 * np.pi * 100 * t) + 0.4 * np.sin(2 * np.pi * 200 * t)) * 0.18 * np.exp(-t * 6)
    return x / np.abs(x).max()

def buzzer(f=520, dur=0.32, bright=True):
    """quiz buzzer press: a bright square-ish two-tone beep (or a low raspy buzz for the wrong answer)"""
    n = int(dur * SR); t = np.arange(n) / SR
    if bright:
        x = np.tanh(3 * (np.sin(2 * np.pi * f * t) + 0.5 * np.sin(2 * np.pi * f * 1.5 * t)))
    else:
        x = np.sign(np.sin(2 * np.pi * f * t)) * (0.7 + 0.3 * np.sign(np.sin(2 * np.pi * 31 * t)))
        x = svf_bp(x, np.full(n, 600.0), 0.7)
    e = np.minimum(1, t / 0.006) * np.minimum(1, (dur - t) / 0.03)
    x = x * e; return x / np.abs(x).max()

def clock(dur=0.05, f=2400):
    """countdown clock tick: a dry wooden click"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.full(n, f), 3.0) * np.exp(-t * 180) + np.sin(2 * np.pi * 1100 * t) * np.exp(-t * 120) * 0.5
    return x / np.abs(x).max()

def snare(dur=0.12):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.full(n, 2600.0), 0.8) * np.exp(-t * 40) + np.sin(2 * np.pi * 190 * t) * np.exp(-t * 45) * 0.6
    return x / np.abs(x).max()

def wahwah(start=392.0, dur=1.25):
    """quiz 'fail' sting: three descending muted-brass notes, the last one bends and wobbles"""
    notes = [(start, 0.2), (start * 0.944, 0.2), (start * 0.891, 0.2), (start * 0.84, dur - 0.6)]
    o = []
    for k, (f, d) in enumerate(notes):
        n = int(d * SR); t = np.arange(n) / SR
        ff = f * (1 - (0.06 * t / d if k == 3 else 0)) * (1 + (0.025 * np.sin(2 * np.pi * 6 * t) if k == 3 else 0))
        ph = 2 * np.pi * np.cumsum(ff) / SR
        x = np.sin(ph) + 0.5 * np.sin(2 * ph) + 0.3 * np.sin(3 * ph) + 0.15 * np.sin(4 * ph)
        x = svf_bp(x, 700 + 500 * np.abs(np.sin(2 * np.pi * (3 if k == 3 else 1.5) * t)), 0.9)
        e = np.minimum(1, t / 0.02) * np.minimum(1, (d - t) / 0.04); o.append(x * e)
    x = np.concatenate(o); return x / np.abs(x).max()

def applause(dur=1.6, rate=90):
    """soft synthetic applause: many short filtered noise claps with a swell"""
    n = int(dur * SR); x = np.zeros(n); u = np.linspace(0, 1, n)
    for _ in range(int(rate * dur)):
        i = int(rng.random() * (n - 2000)); c = svf_bp(rng.standard_normal(900), np.full(900, 1200 + 1800 * rng.random()), 1.2) * np.exp(-np.arange(900) / 120)
        x[i:i + 900] += c * (0.5 + rng.random())
    x *= np.sin(np.pi * np.clip(u * 1.4, 0, 1) / 2) * np.cos(np.pi * u / 2) ** 0.6
    return x / np.abs(x).max()

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)


# ---- extra voices for the sorting line ----
def motor(dur, f=55.0):
    """conveyor motor: a low hum with a slow roller flutter (fades in / out)"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.5 * np.sin(2 * np.pi * 2 * f * t) + 0.25 * np.sin(2 * np.pi * 3.01 * f * t)
    x *= 0.75 + 0.25 * np.sin(2 * np.pi * 7.5 * t)
    x += svf_bp(rng.standard_normal(n), np.full(n, 420.0), 0.9) * 0.35
    e = np.minimum(1, t / 0.35) * np.minimum(1, (dur - t) / 0.12)
    return x * e / np.abs(x).max()

def brake(dur=0.32):
    """emergency stop: a heavy relay clunk plus a short gritty brake hiss"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * 70 * t) * np.exp(-t * 22) + svf_bp(rng.standard_normal(n), np.linspace(2600, 900, n), 1.4) * np.exp(-t * 11) * 0.7
    return x / np.abs(x).max()

def coin(f=2637, dur=0.55):
    """counted: a bright coin ding with a metallic partial"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 6) + 0.5 * np.sin(2 * np.pi * f * 1.5 * t) * np.exp(-t * 9) + 0.25 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 16)
    x[: int(0.004 * SR)] *= np.linspace(0, 1, int(0.004 * SR))
    return x / np.abs(x).max()

def boing(f0=260, f1=700, dur=0.28):
    """the token's jump off the belt: a quick upward springy sweep"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 + (f1 - f0) * (1 - np.exp(-t * 18)) + 25 * np.sin(2 * np.pi * 22 * t) * np.exp(-t * 8)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7)
    return x / np.abs(x).max()

def stamp(dur=0.3):
    """rubber stamp slam: a low thud with a papery slap"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * 95 * t) * np.exp(-t * 30) + svf_bp(rng.standard_normal(n), np.full(n, 1800.0), 0.9) * np.exp(-t * 60) * 0.8
    return x / np.abs(x).max()

def warn(f=330, dur=0.5):
    """the false jump: a two-pulse low warning tone"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.tanh(2.2 * (np.sin(2 * np.pi * f * t) + 0.4 * np.sin(2 * np.pi * f * 2 * t)))
    gate = ((t % 0.25) < 0.17).astype(float)
    e = np.minimum(1, t / 0.01) * np.minimum(1, (dur - t) / 0.03)
    x = svf_bp(x * gate * e, np.full(n, 900.0), 0.8)
    return x / np.abs(x).max()

def rise(f0=300, f1=1200, dur=0.5):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * env(n, 0.3)
    return x / np.abs(x).max()

# S1 · hook: motor hum + roller ticks while the belt runs, camera pull-back air, caption pops, marker on "omzet?", gauge flick
put(0.0, motor(TM['eh'] + 0.05), 0.07)
t = 0.12
while t < TM['eh']: put(t, tick(0.02, 1900 + 300 * ((int(t * 8)) % 2)), 0.025); t += 0.125
wh(0.15, 2.6, 180, 900, 0.9, 0.5, 0.45)
put(TM['hook'] - 0.1, pop(500, 900, 0.08), 0.06); put(TM['lang'] - 0.05, pop(540, 980, 0.08), 0.07); put(TM['omz'] - 0.1, pop(600, 1100, 0.08), 0.08)
put(TM['omz'] + 0.25, marker(0.4), MK)
put(TM['omz'] - 0.05, square_blips([660, 990], 0.05), 0.03); put(TM['omz'] + 0.15, knock(240, 0.14), 0.06)
# S2 · "Eh, tunggu!": emergency stop + token rattle; lanes draw back (soft whooshes), junction blips; penjualan header drop + marker
put(TM['eh'] + 0.0, brake(0.34), 0.16)
for k in range(4): put(TM['eh'] + 0.06 + k * 0.02, tick(0.02, 3000 + 200 * k), 0.05)
for k in range(4): put(TM['eh'] + 0.2 + k * 0.025, knock(420 + 30 * k, 0.08), 0.03)
wh(TM['eh'] + 0.05, 1.4, 1500, 400, 1.0, 0.4, 0.5)
put(TM['eh'] + 0.05, pop(480, 860, 0.08), 0.06); put(TM['ngk'] - 0.05, pop(520, 940, 0.08), 0.06)
for j in range(3): wh(TM['ngk'] + 0.2 + j * 0.12, 0.55, 400, 1800, 1.3, 0.3, 0.3)
for j in range(4): put(TM['ngk'] + 0.3 + j * 0.1, square_blips([1320 + 110 * j], 0.05), 0.025)
put(TM['jual'] + 0.15, knock(200, 0.2), 0.1); put(TM['jual'] + 0.55, marker(0.38), MK)
# S3 · the scan gate drops in (clunk + bounces), hums, slides; every flip = scan beep + flip whoosh; side boards rise
FLIP = [TM['ada2'] - 0.32, TM['pinj'], TM['tmod'], TM['prib']]
g0 = FLIP[0] - 0.62
wh(g0 - 0.1, 0.45, 2400, 500, 1.1, 0.3, 0.35); put(g0 + 0.3, clunk(0.3), 0.1); put(g0 + 0.38, knock(180, 0.12), 0.05); put(g0 + 0.43, knock(200, 0.1), 0.03)
n = int((FLIP[3] + 0.6 - g0) * SR); tt_ = np.arange(n) / SR
put(g0 + 0.3, (np.sin(2 * np.pi * 120 * tt_) * 0.6 + np.sin(2 * np.pi * 240 * tt_) * 0.3) * np.minimum(1, tt_ / 0.2) * np.minimum(1, (tt_[-1] - tt_) / 0.3), 0.025)
for i, f in enumerate(FLIP):
    put(f - 0.03, square_blips([1568, 2093], 0.045), 0.04)
    wh(f, 0.4, 600, 2800, 1.4, 0.35, 0.35)
    put(f + 0.3, pop(700 + 80 * i, 1300 + 100 * i, 0.07), 0.07)
    if i: wh(f + 0.02, 0.6, 250, 1200, 0.9, 0.5, 0.4); put(f + 0.5, knock(170, 0.22), 0.09)
for f in FLIP[1:]: wh(f - 0.6, 0.55, 300, 1600, 1.0, 0.5, 0.3)
wh(FLIP[3] + 0.45, 0.7, 500, 2200, 1.0, 0.6, 0.4)
# S4 · sorter fires: jump (boing + whoosh), glide, counted on the board (coin ding); gauge ratchet; markers; stamps
LEAP = [11.05, TM['pin2'] + 0.1, TM['tm2'] - 0.02, 13.3]
for i, tL in enumerate(LEAP):
    put(tL - 0.08, knock(300, 0.08), 0.06); put(tL, boing(240 + 30 * i, 680 + 40 * i, 0.3), 0.07)
    wh(tL + 0.3, 0.7, 400, 2400, 1.2, 0.7, 0.45)
    put(tL + 1.13, coin(2349 if i == 0 else 1976 + 120 * i, 0.6), 0.08); put(tL + 1.13, pop(500, 900, 0.07), 0.07)
t = LEAP[0] + 1.13
for j in range(10): put(t + j * 0.05, tick(0.012, 3200 + 100 * (j % 3)), 0.04)
put(TM['pin2'] - 0.05, pop(520, 960, 0.08), 0.06); put(TM['utang'] + 0.3, marker(0.32), MK)
put(TM['tm2'] - 0.05, pop(540, 980, 0.08), 0.06); put(TM['setor'] + 0.4, marker(0.34), MK)
put(TM['bukan'], pop(600, 1100, 0.08), 0.08); put(TM['hasil'] + 0.35, marker(0.44), MK)
for j in range(3): put(TM['bukan'] + 0.42 + j * 0.13, stamp(0.3), 0.12)
# S5 · tokens pop out of the side boards, arc across, land on the omzet board; gauge jumps; false-jump warning on "naik"; shrug; TETAP
WR = [TM['hit'] - 0.12, TM['hit'] + 0.12, TM['hit'] + 0.36]
wh(TM['kalau'], 1.1, 200, 1500, 0.9, 0.5, 0.5); put(TM['kalau'] - 0.05, pop(480, 860, 0.08), 0.06)
for j, t0 in enumerate(WR):
    land = t0 + 0.2 + 0.62 + j * 0.06
    put(t0, pop(900, 1600, 0.06), 0.08); wh(t0 + 0.2, land - t0 - 0.2, 600, 2400, 1.3, 0.5, 0.35)
    put(land, coin(2093 + 220 * j, 0.5), 0.07); put(land, rise(500 + 120 * j, 900 + 160 * j, 0.25), 0.04)
    for k in range(5): put(land + k * 0.04, tick(0.012, 3400), 0.035)
put(TM['angka'] - 0.05, pop(560, 1000, 0.08), 0.07)
put(TM['naik'], warn(330, 0.5), 0.09); put(TM['naik'] + 0.02, knock(140, 0.2), 0.1); put(TM['naik'] + 0.05, pop(600, 1300, 0.08), 0.08)
for j in range(5): put(TM['naik'] + j * 0.06, tick(0.015, 2200), 0.04)
put(TM['pdh'] - 0.02, pop(460, 820, 0.08), 0.06)
n = int(0.7 * SR); tt_ = np.arange(n) / SR
put(TM['pdh'] + 0.25, np.sin(2 * np.pi * np.cumsum(520 * (300 / 520) ** (tt_ / 0.7)) / SR) * env(n, 0.2) * 0.8, 0.035)   # a soft "huh?" droop
put(TM['jmu'] + 0.1, square_blips([1046, 1046], 0.06), 0.03)
put(TM['ngk2'] + 0.05, stamp(0.3), 0.12); put(TM['ngk2'] + 0.25, marker(0.4), MK)
# band sweep -> brand: hologram, card swing, minis into rows, kind chips, underline markers, footer, stabilo
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
wh(TM['sol'] + 0.3, 0.9, 250, 2000, 1.0, 0.45, 0.55)
put(TM['sol'] + 0.15, pop(480, 860, 0.08), 0.05)
for k in range(4):
    t = TM['umsk'] - 0.35 + k * 0.2
    wh(t, 0.5, 700, 2600, 1.3, 0.4, 0.25); put(t + 0.5, pop(520 + 90 * k, 1050 + 120 * k, 0.08), 0.1)
    put(TM['jenis'] + 0.1 + k * 0.14, square_blips([1568 + 130 * k], 0.04), 0.03)
put(TM['umsk'] - 0.05, pop(520, 940, 0.08), 0.05); put(TM['jenis'] + 0.6, marker(0.42), MK)
for g in (TM['mpai'] + 0.25, TM['biar'] + 0.5, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g, square_blips([1800, 900, 1500], 0.02), 0.02)
put(TM['omu'] - 0.1, pop(500, 900, 0.08), 0.08); put(TM['omu'] + 0.25, knock(260, 0.12), 0.05)
put(TM['asli'] + 0.05, marker(0.4), MK); put(TM['asli'] + 0.1, marker(0.42), MK * 0.8); put(TM['asli'] + 0.3, chime((1568, 2093, 2637), 0.9), 0.03)
# beam + iris -> end
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 1.0, chime((784, 1046, 1568), 1.3), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")

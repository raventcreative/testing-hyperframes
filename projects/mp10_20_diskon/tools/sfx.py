"""Synthesised SFX for MasterPajak AI Video 20 (Diskon Gede, Untung Ikut Gede?) — sits under the VO (no samples, no music).
Beat times are parsed from window.TM in index.html, so a VO re-time only needs `python3 tools/sfx.py` again. Deterministic.
Sounds: crane-in air, studio lamps (clunk + warm hum), bulb chase shimmer, promo-tag drop + swing creak-less flutter, stabilo
marker, quiz lozenge slides, buzzer presses (A / B), countdown clock ticks + time-up buzz, board switch, row pops + value
ticks, sticker slap, drum-roll + odometer ticks, "wah-wah" fail sting on the small result, bar-card whoosh + bar rises, whip
pan, correct "ding-ding" + soft synthetic applause + confetti, wrong-answer low buzz for A, equation card + box pops + stamp,
band sweep, hologram fx, card swing-in + row pops + underline marker, tag swing, beam/iris boom, end pops + chime.
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

# S1 · hook: crane-in air, five lamps clunk on, bulb shimmer, title pops, tag drop + swing, marker on "ikut gede?", "?" pop
wh(0.0, 2.8, 200, 900, 0.9, 0.5, 0.35)
for k in range(5): put(TM['hook'] + 0.05 + abs(k - 2) * 0.09, clunk(0.3), 0.07)
put(TM['hook'] + 0.3, shimmer(1.2), 0.025)
put(TM['hook'] - 0.1, pop(500, 900, 0.08), 0.07); put(TM['disk'], pop(560, 1000, 0.08), 0.08); put(TM['unt'], pop(520, 950, 0.08), 0.07)
wh(TM['disk'] - 0.05, 0.5, 2200, 500, 1.1, 0.25, 0.45); put(TM['disk'] + 0.45, knock(240, 0.16), 0.08)
put(TM['per'] + 0.02, pop(700, 1300, 0.07), 0.08)
put(TM['gede'] - 0.05, marker(0.42), MK)
put(TM['unt'] + 0.05, pop(380, 900, 0.12), 0.1)
# S2 · lozenges slide, buzzers A / B, countdown ticks + time-up buzz
for dt in (-0.14, 0.02): wh(TM["optA"] + dt, 0.42, 500, 2600, 1.2, 0.4, 0.4)
wh(TM['optB'] - 0.04, 0.42, 500, 2600, 1.2, 0.4, 0.4)
put(TM['aA'], buzzer(587, 0.26), 0.08); put(TM['bB'], buzzer(659, 0.26), 0.08)
t = TM['optA'] + 0.25
while t < TM['hit'] - 0.2: put(t, clock(0.05, 2400 if int((t - TM['optA']) * 2) % 2 else 1900), 0.07); t += 0.5
put(TM['hit'] - 0.12, buzzer(150, 0.42, False), 0.07)
for k in range(3): wh(TM['hit'] - 0.12 + k * 0.05, 0.35, 2400, 600, 1.2, 0.3, 0.3)
# S3 · push into the board, rows, the sticker slap, values
wh(TM['hit'] + 0.02, 0.95, 250, 1800, 0.9, 0.55, 0.6); put(TM['hit'] + 0.3, square_blips([880, 1320], 0.04), 0.025)
for k, (a, v) in enumerate([(TM['harga'] - 0.04, TM['harga'] + 0.32), (TM['disk2'] + 0.1, None), (TM['j70'] - 0.05, None), (TM['modal'] + 0.05, TM['m50']), (TM['ongkir'] + 0.3, TM['o10'])]):
    put(a, pop(520 + 60 * k, 1000 + 80 * k, 0.08), 0.1); put(a + 0.02, tick(0.02, 3600), 0.05)
    if v: put(v, pop(800, 1500, 0.06), 0.08)
wh(TM['disk2'] - 0.12, 0.42, 600, 2400, 1.1, 0.7, 0.45); put(TM['disk2'] + 0.3, knock(260, 0.14), 0.13); put(TM['disk2'] + 0.31, pop(300, 700, 0.08), 0.1)
# drum-roll -> odometer ticks -> the small result: a "wah-wah" sting
t = TM['o10'] + 0.3; k = 0
while t < TM['laba'] - 0.1: put(t, snare(0.1), 0.05 + 0.04 * (t - TM['o10']) / (TM['laba'] - TM['o10'])); t += max(0.045, 0.12 - 0.006 * k); k += 1
tt = TM['laba'] - 0.14
for j in range(12): put(tt, tick(0.012, 3600 + 120 * (j % 3)), 0.06); tt += 0.05 + 0.004 * j
put(TM['l10'] + 0.08, knock(120, 0.25), 0.12); put(TM['l10'] + 0.15, wahwah(392, 1.25), 0.09)
put(TM['l10'] + 0.2, shimmer(0.6), 0.02)
# S4 · "Padahal tadinya": bar card flies in, bars rise
wh(TM['tadi'] - 0.12, 0.6, 2400, 500, 1.1, 0.3, 0.55)
put(TM['tadi'] + 0.3, pop(500, 800, 0.08), 0.08)
n = int(0.6 * SR); tt_ = np.arange(n) / SR; rise = np.sin(2 * np.pi * np.cumsum(300 * (900 / 300) ** (tt_ / 0.6)) / SR) * env(n, 0.3)
put(TM['l40'] - 0.05, rise, 0.04); put(TM['l40'] + 0.55, pop(700, 1400, 0.07), 0.09)
put(TM['l40'] + 0.85, ding(1760, 0.4), 0.04)
# S5 · whip pan, correct buzzer + ding-ding, applause, confetti, A's wrong buzz
wh(TM['jwb'] - 0.22, 0.5, 2600, 300, 1.0, 0.35, 0.6); wh(TM['jwb'] + 0.02, 0.5, 300, 3200, 1.2, 0.6, 0.9)
for dt in (0.25, 0.31, 0.37): wh(TM['jwb'] + dt, 0.35, 500, 2400, 1.2, 0.4, 0.3)
put(TM['jB'] - 0.02, buzzer(659, 0.22), 0.09)
for j in range(3): put(TM['jB'] + 0.05 + j * 0.2, ding(1568 * (1.26 ** j), 0.5), 0.07)
put(TM['jB'] + 0.25, buzzer(140, 0.3, False), 0.05)
put(TM['jB'] + 0.1, applause(1.8, 110), 0.07)
for j in range(10): put(TM['jB'] + 0.1 + j * 0.13, pop(1200 + 200 * (j % 4), 2400, 0.04), 0.035)
# equation card, boxes, stamp
wh(TM['biar'] - 0.1, 0.4, 1600, 500, 1.0, 0.4, 0.3); wh(TM['biar'], 0.6, 250, 2000, 1.0, 0.45, 0.5)
put(TM['biar'] + 0.45, pop(600, 1100, 0.08), 0.1)
for k in range(4): put(TM['kamu'] + 0.1 + k * 0.16, pop(520 + 90 * k, 1050 + 120 * k, 0.08), 0.11)
put(TM['x4'] - 0.02, knock(200, 0.2), 0.12); put(TM['x4'], pop(600, 1300, 0.09), 0.13); put(TM['x4'] + 0.05, chime((1568, 2093, 2637), 1.0), 0.05)
# band sweep -> brand
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
wh(TM['sol'] + 0.25, 0.9, 250, 2000, 1.0, 0.45, 0.55)
for k in range(4): put(TM['lr'] + 0.5 + k * 0.32 - 0.04, pop(520 + 90 * k, 1050 + 120 * k, 0.08), 0.11)
put(TM['mpai'] - 0.2, marker(0.45), MK)
for g0 in (TM['mpai'] + 0.2, TM['asli'] + 1.2, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
put(TM['asli'] + 0.5, marker(0.35), MK * 0.9); put(TM['asli'] + 0.62, pop(700, 1300, 0.08), 0.1)
wh(TM['promo'] - 0.1, 0.5, 2200, 600, 1.1, 0.3, 0.4); put(TM['promo'] + 0.38, knock(260, 0.14), 0.08)
put(TM['promo'] + 0.55, marker(0.42), MK)
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

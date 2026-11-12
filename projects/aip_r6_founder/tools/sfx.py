"""Synthesised SFX bed for the FOUNDER reel (R6: tes ide bisnis ke 100 pembeli AI) (no samples, no downloads): idea card + scan,
the 100-avatar panel popping in (a wave of tiny pops + counter ticks), the Rp0 slam, 11 command chips flying out, board seats lighting,
CFO rows ticking + ring sweep + strike, persona cards, the pitch being sent, the two verdicts (chime / BELUM stamp), objection rows,
the TAHAN DULU stamp, the SIMULASI stamp, the CTA (FOUNDER typing, heart, plane, DM chime). Deterministic. Writes assets/audio/sfx.wav.
Run: python3 tools/sfx.py ."""
import json, sys, wave
from pathlib import Path
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
T = json.loads((P / "production/timing.json").read_text())
SR = 48000; N = int(T["total_sec"] * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(7)
S = {s["id"]: s for s in T["scenes"]}
def wt(txt, after=0.0):
    for w in T["words"]:
        if w["w"] == txt and w["s"] >= after: return w["s"]
    return None

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
    u = np.linspace(0, 1, n); k = int(n * a)
    e = np.ones(n); e[:k] = np.sin(np.linspace(0, np.pi / 2, k)) ** shape; e[k:] = np.cos(np.linspace(0, np.pi / 2, n - k)) ** shape
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
    x = np.tanh(1.8 * (x + nb))
    return x / np.abs(x).max()

def pop(f0=900, f1=320, dur=0.09):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * np.exp(-t * 38)
    return x / np.abs(x).max()

def tick(dur=0.025, f=4200):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.full(n, f), 2.0) * np.exp(-t * 260)
    return x / (np.abs(x).max() + 1e-9)

def square_blips(notes, step=0.055):
    out_ = []
    for f in notes:
        n = int(step * SR); t = np.arange(n) / SR
        out_.append(np.sign(np.sin(2 * np.pi * f * t)) * 0.6 * np.exp(-t * 18))
    return np.concatenate(out_)

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

def rip(dur=0.55):
    n = int(dur * SR); t = np.arange(n) / SR
    jit = np.repeat(rng.random(n // 240 + 1), 240)[:n] ** 3
    x = svf_bp(rng.standard_normal(n), np.linspace(1400, 3600, n), 1.4) * jit * env(n, 0.2)
    return x / np.abs(x).max()

def scribble(dur=0.6):
    n = int(dur * SR); t = np.arange(n) / SR
    am = 0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 13 * t))
    x = svf_bp(rng.standard_normal(n), 2600 + 900 * np.sin(2 * np.pi * 6.5 * t), 1.6) * am * env(n, 0.2)
    return x / np.abs(x).max()

def rumble(dur=1.5):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(70, 260, n), 0.7)
    x = x / np.abs(x).max() * env(n, 0.3, 1.0)
    return x


def flap():
    """split-flap clack: two quick clicks + a soft low knock"""
    x = np.zeros(int(0.22 * SR)); a = tick(0.02, 3000); b = tick(0.02, 2400)
    x[: len(a)] += a; i = int(0.11 * SR); x[i:i + len(b)] += 0.8 * b
    k = pop(180, 90, 0.08); x[: len(k)] += 0.35 * k
    return x / np.abs(x).max()

def rise(dur=0.6, f0=300, f1=1200):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * env(n, 0.8, 1.0) * (0.6 + 0.4 * np.sign(np.sin(2 * np.pi * 14 * t)))
    return x / np.abs(x).max()

def buzz(dur=0.35):
    n = int(dur * SR); t = np.arange(n) / SR
    x = (np.sign(np.sin(2 * np.pi * 110 * t)) * 0.5 + np.sign(np.sin(2 * np.pi * 116 * t)) * 0.5) * env(n, 0.05, 1.0)
    return x / np.abs(x).max()

def typing(t0, t1, gain=0.11, rate=16):
    k = 0; t = t0
    while t < t1:
        put(t, tick(0.02, 3600 + 500 * (k % 3)), gain * (0.8 + 0.2 * (k % 2))); k += 1; t += 1.0 / rate * (0.8 + 0.4 * ((k * 7) % 5) / 5)



W = 0.15
def bell(dur=0.9):
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for k, f in enumerate((1568, 2349, 3136)):
        x += np.sin(2 * np.pi * f * t) * np.exp(-t * (4 + 2 * k)) * (0.8 ** k)
    x *= 0.75 + 0.25 * np.sin(2 * np.pi * 11 * t)
    return x / np.abs(x).max()

st = lambda i: S[i]["start"]
def pops(t0, n, span, f0=900, f1=1500, g=0.05, dur=0.04):
    for k in range(n): put(t0 + span * k / max(1, n - 1), pop(f0 + (f1 - f0) * k / max(1, n - 1), f0 * 1.4 + (f1 - f0) * k / max(1, n - 1), dur), g)
def ticks(t0, n, span, f=2600, g=0.08):
    for k in range(n): put(t0 + span * k / max(1, n - 1), tick(0.02, f + 140 * (k % 4)), g)
# --- s01 hook: idea card, "dites" scan, connector, the panel pops in + counter, Rp0 slam, AMAN
put(0.02, pop(500, 760, 0.08), 0.08)
put(wt("dites") - 0.06, pop(800, 1300, 0.07), 0.12); put(wt("dites") - 0.02, whoosh(0.55, 700, 2600, 2.0, 0.5), W * 0.35)
put(wt("ke") - 0.02, tick(0.03, 2200), 0.12)
t100 = wt("100"); pops(t100 - 0.08, 14, 0.7, 700, 1700, 0.045); ticks(t100 - 0.04, 10, 0.8, 3000, 0.06)
put(wt("AI") - 0.02, chime((1318.5, 1760, 2637), 0.9), 0.05)
put(wt("sebelum") - 0.12, whoosh(0.4, 500, 1800, 1.3, 0.45), W * 0.45)
put(wt("sepeser") + 0.08, boom(0.45, 150, 60), 0.22); put(wt("sepeser") + 0.1, pop(420, 200, 0.12), 0.12)
put(wt("pun.") - 0.06, chime((1568, 2093, 2637), 0.9), 0.06); put(wt("pun.") - 0.04, pop(1000, 1600, 0.06), 0.1)
put(st("s02") - 0.3, whoosh(0.4, 2000, 600, 1.3, 0.35), W * 0.6)
# --- s02 the Founder pack: card up, title + glint, "11" slam, 11 chips fly out, Claude chime, badges, 3 featured rings
put(st("s02") + 0.02, whoosh(0.4, 500, 1800, 1.3, 0.45), W * 0.45)
put(wt("Founder:") - 0.12, pop(700, 1200, 0.08), 0.13); put(wt("Founder:") + 0.1, rise(0.5, 900, 2400), 0.025)
put(wt("11") - 0.0, boom(0.4, 160, 65), 0.2)
for k in range(11): put(wt("11") + 0.02 + k * 0.055, whoosh(0.18, 900, 2600, 1.6, 0.3), W * 0.18); put(wt("11") + 0.3 + k * 0.055, pop(800 + 50 * k, 1200 + 50 * k, 0.04), 0.06)
put(wt("Claude,") - 0.03, chime((1318.5, 1760, 2637), 0.9), 0.06)
put(wt("gratis") - 0.06, pop(900, 1400, 0.07), 0.13); put(wt("open") - 0.08, pop(1000, 1500, 0.07), 0.12)
for q in range(3): put(wt("source.") + 0.05 + q * 0.08, pop(1200 + 120 * q, 1800 + 120 * q, 0.05), 0.08)
put(st("s03") - 0.27, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.5)
# --- s03 the board: pill, title words, seats rise, chips, each seat lights on its name
put(st("s03") + 0.05, pop(600, 1000, 0.08), 0.1)
put(wt("dewan") - 0.1, pop(500, 800, 0.08), 0.1); put(wt("direksi,") - 0.1, pop(600, 950, 0.08), 0.1)
for k in range(3): put(wt("dewan") - 0.05 + k * 0.08, whoosh(0.35, 500, 1700, 1.3, 0.4), W * 0.3)
for q in range(3): put(wt("kerangka") - 0.06 + q * 0.12, pop(1000 + 100 * q, 1500 + 100 * q, 0.05), 0.08)
for k, w in enumerate(["Hormozi,", "Thiel,", "Steve"]):
    put(wt(w) - 0.08, flap(), 0.1); put(wt(w) - 0.02, pop(800 + 200 * k, 1300 + 200 * k, 0.07), 0.12)
put(st("s04") - 0.26, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.5)
# --- s04 CFO: card, title slam, rows tick, rule, rest per portion, ring sweep, strike
put(st("s04") + 0.03, whoosh(0.45, 500, 1700, 1.3, 0.45), W * 0.45)
put(wt("CFO,") - 0.0, boom(0.35, 160, 70), 0.17)
typing(wt("ngitung") - 0.3, wt("ngitung") + 0.15, 0.08, 22)
for k in range(4): put(wt("CFO,") + 0.22 + k * 0.13, tick(0.025, 2400 + 150 * k), 0.12)
put(wt("margin") - 0.32, whoosh(0.25, 1200, 3000, 1.6, 0.3), W * 0.25); put(wt("margin") - 0.1, pop(700, 1100, 0.08), 0.13)
put(wt("asli") - 0.1, rise(0.45, 500, 1600), 0.03); put(wt("asli") + 0.12, rip(0.22), 0.06)
put(wt("asli") + 0.3, buzz(0.16), 0.03); put(wt("asli") + 0.4, chime((1318.5, 1760), 0.6), 0.04)
put(st("s05") - 0.28, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.5)
# --- s05 panel: pill, PALING SERU, title slam, the 100 pop in, three persona cards fly out, three fields
put(st("s05") + 0.05, pop(600, 1000, 0.08), 0.1)
put(wt("seru:") - 0.1, pop(1100, 1700, 0.07), 0.13); put(wt("seru:"), chime((1568, 2093, 2637), 0.8), 0.05)
put(wt("panel", st("s05")) - 0.02, boom(0.4, 150, 65), 0.18)
pops(wt("100", st("s05")) - 0.1, 14, 0.62, 700, 1700, 0.045)
for k in range(3): put(wt("masing-masing") - 0.12 + k * 0.08, whoosh(0.4, 700, 2400, 1.4, 0.4), W * 0.3)
put(wt("masing-masing") + 0.3, pop(600, 950, 0.08), 0.1)
for w in ["penghasilan,", "kebiasaan,", "keraguan"]: put(wt(w) - 0.12, pop(900, 1400, 0.06), 0.11); put(wt(w) - 0.1, tick(0.02, 2600), 0.06)
put(wt("sendiri.") - 0.1, whoosh(0.3, 1200, 2400, 1.6, 0.3), W * 0.25)
put(st("s06") - 0.28, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.5)
# --- s06 pitch: card, CONTOH label, title words, price slam, chips, the send + panel ripple
put(st("s06") + 0.02, whoosh(0.45, 500, 1700, 1.3, 0.45), W * 0.45)
put(wt("Contohnya,") + 0.06, pop(900, 1500, 0.07), 0.1)
for w in ["katering", "makan", "kantor,"]: put(wt(w) - 0.1, tick(0.025, 2600), 0.1)
put(wt("Rp25.000") - 0.0, boom(0.4, 160, 65), 0.18); put(wt("Rp25.000") + 0.04, chime((2093, 2637, 3136), 0.6), 0.04)
for q in range(2): put(wt("Rp25.000") + 0.35 + q * 0.12, pop(1000 + 150 * q, 1500 + 150 * q, 0.05), 0.08)
put(wt("per", st("s06")) - 0.02, pop(800, 1300, 0.07), 0.1)
put(wt("porsi.") - 0.1, whoosh(0.32, 2400, 700, 1.4, 0.35), W * 0.45); put(wt("porsi.") + 0.2, pop(500, 800, 0.08), 0.12)
ticks(wt("porsi.") + 0.16, 9, 0.32, 3200, 0.04)
put(st("s07") - 0.26, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.5)
# --- s07 verdicts: two cards slide in, CFO rows, "masuk" chime, panel counts to 18, BELUM stamp
put(st("s07") + 0.0, whoosh(0.4, 500, 1800, 1.3, 0.45), W * 0.4); put(st("s07") + 0.1, whoosh(0.4, 600, 2000, 1.3, 0.45), W * 0.35)
for w, a in [("CFO-nya", 0.25), ("angkanya", -0.25), ("angkanya", 0.0)]: put(wt(w) + a, tick(0.025, 2500), 0.1)
put(wt("masuk.") - 0.16, whoosh(0.28, 900, 2600, 1.6, 0.3), W * 0.3); put(wt("masuk.") - 0.02, chime((1046, 1318, 1568, 2093), 1.0), 0.08)
put(wt("Tapi", st("s07")) - 0.05, whoosh(0.3, 1600, 700, 1.3, 0.3), W * 0.25)
ticks(wt("panelnya") - 0.05, 9, 0.55, 2800, 0.07)
put(wt("belum.") - 0.0, boom(0.45, 140, 55), 0.22); put(wt("belum.") + 0.02, buzz(0.25), 0.045); put(wt("belum.") + 0.05, pop(380, 180, 0.12), 0.12)
put(st("s08") - 0.26, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.5)
# --- s08 18 / 100: panel in, count + 18 green pops, the 82 dim, three objection rows
put(st("s08") + 0.02, whoosh(0.4, 500, 1600, 1.3, 0.45), W * 0.35)
ticks(wt("18") - 0.12, 9, 0.5, 2800, 0.07); pops(wt("18") - 0.1, 18, 0.5, 1100, 1900, 0.04, 0.035)
put(wt("dari", st("s08")) + 0.1, whoosh(0.5, 1800, 500, 1.2, 0.5), W * 0.3)
put(wt("beli.", st("s08")) - 0.1, pop(900, 1400, 0.06), 0.08)
for w, a in [("bawa", -0.1), ("warteg", -0.16), ("murah.", 0.02)]:
    put(wt(w) + a - 0.08, pop(420, 260, 0.1), 0.1); put(wt(w) + a, whoosh(0.3, 700, 2200, 1.5, 0.35), W * 0.3); put(wt(w) + a + 0.22, pop(800, 1200, 0.05), 0.08)
put(st("s09") - 0.26, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.5)
# --- s09 now vs later: green card + chip, "daripada" pill, cart rises, items, pay pulse, TAHAN DULU stamp
put(st("s09") + 0.02, whoosh(0.4, 500, 1800, 1.3, 0.45), W * 0.4)
put(wt("sekarang,", st("s09")) + 0.05, chime((1318.5, 1760, 2349), 0.8), 0.06); put(wt("sekarang,", st("s09")) + 0.06, pop(1000, 1600, 0.06), 0.1)
put(wt("daripada") - 0.1, pop(700, 1100, 0.07), 0.1); put(wt("daripada"), whoosh(0.4, 500, 1700, 1.3, 0.45), W * 0.35)
for k in range(4): put(wt("beli", st("s09")) - 0.2 + k * 0.1, tick(0.025, 2300 + 150 * k), 0.1)
put(wt("peralatan") - 0.05, pop(800, 1300, 0.07), 0.1)
put(wt("dapur.") - 0.0, boom(0.4, 150, 60), 0.2); put(wt("dapur.") + 0.02, pop(320, 160, 0.1), 0.12)
put(st("s10") - 0.24, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.5)
# --- s10 simulated → real: panel box, SIMULASI stamp, winner card, real-test card, real buyers pop + checks
put(st("s10") + 0.02, whoosh(0.45, 500, 1700, 1.3, 0.45), W * 0.4)
put(wt("simulasi.") - 0.02, boom(0.4, 150, 60), 0.18); put(wt("simulasi.") + 0.0, zap(0.35), 0.03)
put(wt("ide", st("s10")) - 0.1, tick(0.025, 2200), 0.1)
put(wt("menang,") - 0.22, pop(800, 1300, 0.08), 0.12); put(wt("menang,") - 0.1, chime((1568, 2093, 2637), 0.9), 0.06)
put(wt("tes", st("s10")) - 0.2, tick(0.025, 2200), 0.1); put(wt("tes", st("s10")) - 0.12, whoosh(0.4, 500, 1800, 1.3, 0.45), W * 0.35)
for k in range(4): put(wt("pembeli", st("s10")) - 0.1 + k * 0.07, pop(700 + 100 * k, 1100 + 100 * k, 0.06), 0.1)
for k in range(4): put(wt("beneran.") + 0.12 + k * 0.06, pop(1300 + 120 * k, 2000 + 120 * k, 0.04), 0.07)
put(wt("beneran.") + 0.15, chime((1318.5, 1760, 2349), 0.8), 0.05)
put(st("s11") - 0.24, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.5)
# --- s11 CTA: package + sheet, FOUNDER typing, heart, send + plane, DM, end chime
put(st("s11") + 0.0, whoosh(0.4, 400, 1800, 1.3, 0.45), W * 0.5); put(st("s11") + 0.1, pop(700, 1200, 0.08), 0.1)
tF = wt("FOUNDER,")
for k in range(7): put(tF - 0.2 + k * 0.46 / 6, tick(0.022, 4200), 0.14)
put(tF + 0.31, pop(900, 1600, 0.1), 0.15)
put(wt("aku", tF) - 0.01, tick(0.03, 2000), 0.2); put(wt("aku", tF) + 0.06, whoosh(0.5, 700, 3600, 1.2, 0.45), W * 0.9)
put(wt("DM.") - 0.12, pop(800, 1300, 0.07), 0.1); put(wt("DM.") + 0.08, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

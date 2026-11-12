"""Synthesised SFX bed for the R13 TRADER reel (adapted from the R9 YOUTUBE bed) (no samples, no downloads): candles climbing, pushy
bubble struck, Claude bubble + "Jangan dulu" lock, repo header + chip burst + three shelves, header flaps, scanner sweep + setups, news /
report cards, entry/stop/target zones, Time Machine paths + counter, waffle fill + coin flip, PASS/BLOCK stamps, three gates unlocking,
paper switch, note rows, paste + typing + send, the CTA. Deterministic.
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
st = lambda i: S[i]["start"]

def wt_(txt, after=0.0):
    v = wt(txt, after)
    if v is None: raise SystemExit("word not found " + txt)
    return v
def out_whoosh(sid): put(st(sid) - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s01 hook: candles climb, pushy bubble, cursor drift, strike + X, Claude bubble, "Jangan dulu." + lock
put(0.02, rise(0.6, 300, 1200), 0.05)
for k in range(7): put(wt_("Mau") - 0.1 + k * 0.2, tick(0.02, 2600 + 120 * k), 0.06)
put(wt_("AI") - 0.1, pop(700, 1200, 0.08), 0.12)
put(wt_("trading") - 0.05, whoosh(1.0, 400, 1400, 1.4, 0.5), W * 0.25)
put(wt_("Pilih") - 0.05, rip(0.22), 0.06); put(wt_("Pilih") + 0.05, buzz(0.18), 0.03)
put(wt_("berani") - 0.2, pop(500, 900, 0.09), 0.12); put(wt_("berani") - 0.1, chime((1046, 1318), 0.6), 0.04)
typing(wt_("jangan") - 0.1, wt_("jangan") + 0.45, 0.07, 20)
put(wt_("dulu.") - 0.06, boom(0.35, 140, 60), 0.2); put(wt_("dulu.") - 0.04, square_blips([660, 440]), 0.05)
out_whoosh("s02")
# --- s02 the pack: header drop, pack card, 11 chips burst, GRATIS, three shelves + the sort
put(wt_("Namanya") - 0.12, whoosh(0.45, 2400, 600, 1.4, 0.45), W * 0.6); put(wt_("Namanya") + 0.3, flap(), 0.1)
put(wt_("Day") - 0.18, pop(600, 1000, 0.09), 0.12); put(wt_("Claude") - 0.1, chime((1046, 1318, 1568), 0.9), 0.05)
for k in range(11): put(wt_("11") + 0.02 + k * 0.055, pop(800 + 50 * k, 1300 + 50 * k, 0.05), 0.07)
put(wt_("gratis,") - 0.04, pop(800, 1300, 0.08), 0.13)
for k in range(3): put(wt_("dibagi") + 0.02 + k * 0.16, whoosh(0.35, 500, 1800, 1.4, 0.4), W * 0.35)
for k in range(11): put(wt_("dibagi") + 0.5 + k * 0.05, tick(0.016, 3000 - 80 * k), 0.06)
put(wt_("lapis.") - 0.05, chime((1318.5, 1760, 2637), 0.8), 0.05)
out_whoosh("t1")
# --- t1 CARI: flap, scanner panel, tiles deal, beam sweep + counter, setups, news, report
put(st("t1") + 0.02, flap(), 0.12)
put(wt_("nyari:") - 0.22, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.5)
for k in range(14): put(wt_("nyari:") + 0.02 + k * 0.035, tick(0.014, 3400), 0.04)
put(wt_("ribuan") - 0.1, rise(0.95, 500, 1600), 0.03)
for k in range(5): put(wt_("ribuan") + 0.03 + k * 0.13, tick(0.02, 4200), 0.07)
for k in range(3): put(wt_("ribuan") + 0.15 + k * 0.32, pop(900 + 150 * k, 1500 + 150 * k, 0.06), 0.1)
put(wt_("berita,") - 0.24, whoosh(0.35, 600, 2000, 1.4, 0.4), W * 0.45); put(wt_("berita,") - 0.05, pop(600, 1000, 0.08), 0.11)
put(wt_("laporan") - 0.3, whoosh(0.35, 600, 2000, 1.4, 0.4), W * 0.45)
for k in range(3): put(wt_("laporan") - 0.1 + k * 0.14, tick(0.02, 2600 + 300 * k), 0.08)
out_whoosh("t2")
# --- t2 RENCANA: flap, chart rises, candles, entry line + dot, red zone, green zone, notes
put(st("t2") + 0.02, flap(), 0.12)
put(wt_("ngerencanain:") - 0.26, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.5)
for k in range(12): put(wt_("ngerencanain:") - 0.1 + k * 0.05, tick(0.014, 2800 + 60 * k), 0.04)
put(wt_("titik") - 0.12, scribble(0.35), 0.04); put(wt_("titik") - 0.04, pop(900, 1500, 0.07), 0.12)
put(wt_("stop", 16) - 0.1, boom(0.3, 160, 70), 0.14)
put(wt_("target.") - 0.18, rise(0.35, 700, 1600), 0.04); put(wt_("target.") - 0.04, chime((1568, 2093), 0.6), 0.05)
# --- s05 TIME MACHINE: flap, zones stretch, paths fan out + counter, axis, "0 order terkirim"
put(st("s05") + 0.1, flap(), 0.12)
put(wt_("Plus") + 0.2, whoosh(0.6, 400, 1600, 1.2, 0.5), W * 0.45)
put(wt_("Machine:") - 0.05, chime((1046, 1568, 2093), 1.0), 0.06)
put(wt_("10.000") - 0.12, rumble(1.8), 0.035); put(wt_("10.000") - 0.1, rise(1.6, 300, 1800), 0.03)
for k in range(24): put(wt_("10.000") - 0.1 + k * 0.07, tick(0.012, 3600 + 40 * (k % 6)), 0.035)
put(wt_("sisa") - 0.1, whoosh(0.4, 700, 2000, 1.4, 0.4), W * 0.3)
put(wt_("sepeser") - 0.1, pop(700, 1200, 0.09), 0.13); put(wt_("sepeser") - 0.05, square_blips([880, 660]), 0.04)
out_whoosh("s06")
# --- s06 RESULT: card, waffle fills (green, red, grey), difference chip, coin flip + verdict
put(wt_("Di") - 0.05, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.5)
for k in range(10): put(wt_("peluang") + 0.1 + k * 0.055, tick(0.014, 3000 + 40 * k), 0.05)
for k in range(9): put(wt_("sama", 25) + 0.02 + k * 0.055, tick(0.014, 2200 - 30 * k), 0.05)
for k in range(6): put(wt_("duluan", 26.3) + 0.2 + k * 0.06, tick(0.012, 1800), 0.03)
put(wt_("tipis:") - 0.1, pop(800, 1300, 0.08), 0.12)
for k in range(4): put(wt_("lempar") - 0.1 + k * 0.19, tick(0.03, 5200 - 300 * k), 0.12)
put(wt_("koin.") + 0.05, chime((1318.5, 1760), 0.7), 0.05)
out_whoosh("t3")
# --- t3 REM: flap, limit card, ticket 1 meter + PASS stamp, ticket 2 meter + BLOCK stamp + shake
put(st("t3") + 0.02, flap(), 0.12)
put(wt_("ngerem:") - 0.24, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.5)
put(wt_("batas", 30.5) - 0.28, whoosh(0.3, 600, 1800, 1.4, 0.4), W * 0.35)
put(wt_("rugi") - 0.15, rise(0.55, 400, 1100), 0.035); put(wt_("dijaga,") - 0.06, boom(0.25, 200, 90), 0.16); put(wt_("dijaga,"), square_blips([880, 1320]), 0.04)
put(wt_("trade") - 0.3, whoosh(0.3, 600, 1800, 1.4, 0.4), W * 0.35)
put(wt_("lewat") - 0.15, rise(0.7, 300, 1500), 0.04)
put(wt_("diblokir.") - 0.08, boom(0.3, 150, 60), 0.2); put(wt_("diblokir.") + 0.1, buzz(0.32), 0.05)
out_whoosh("s08")
# --- s08 BROKER: flap, order card, three gates (locked), unlock one by one, "siap dikirim", PAPER pulse
put(st("s08") + 0.02, flap(), 0.12)
put(wt_("Nggak") + 0.1, pop(600, 1000, 0.08), 0.12)
for k in range(3): put(wt_("Nggak") + 0.26 + k * 0.1, whoosh(0.25, 600, 1800, 1.4, 0.4), W * 0.25)
for k, (w, a) in enumerate((("tanpa", 0), ("persetujuan", 0), ("kamu,", 35))):
    t0 = wt_(w, a) + (-0.05, 0.12, -0.02)[k]
    put(t0, square_blips([660 + 220 * k, 990 + 220 * k]), 0.045); put(t0 + 0.02, tick(0.03, 1600), 0.12)
put(wt_("kamu,", 35) + 0.2, chime((1568, 2093), 0.6), 0.05)
put(wt_("dan", 35.9) - 0.2, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.45)
put(wt_("bawaannya") + 0.05, pop(600, 1100, 0.08), 0.1); put(wt_("latihan.") - 0.1, chime((1318.5, 1760, 2637), 0.8), 0.05)
out_whoosh("s09")
# --- s09 NOTES: flap, three rows, source chips, shield shake
put(st("s09") + 0.02, flap(), 0.12)
put(wt_("Datanya") + 0.06, whoosh(0.35, 500, 1800, 1.4, 0.45), W * 0.45)
for k in range(3): put(wt_("Amerika,") - 0.1 + k * 0.1, pop(900 + 100 * k, 1500 + 100 * k, 0.05), 0.08)
put(wt_("anggap") - 0.25, whoosh(0.35, 500, 1800, 1.4, 0.45), W * 0.45)
put(wt_("bukan", 40) - 0.28, whoosh(0.35, 500, 1800, 1.4, 0.45), W * 0.45)
put(wt_("jaminan."), buzz(0.25), 0.035)
put(st("s10") - 0.2, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.3)
# --- s10 INSTALL: flap, chat opens, paste, typing, send, hand-over to the link card
put(st("s10") + 0.02, flap(), 0.12)
put(wt_("Pasangnya:") + 0.15, whoosh(0.45, 500, 1800, 1.4, 0.45), W * 0.5)
put(wt_("tempel") - 0.05, tick(0.04, 1600), 0.2); put(wt_("tempel") + 0.05, pop(800, 1300, 0.07), 0.1)
typing(wt_("tulis") - 0.02, wt_("tulis") + 0.62, 0.09, 20)
put(wt_("skill.", 45) + 0.08, tick(0.04, 1500), 0.18); put(wt_("skill.", 45) + 0.12, chime((1318.5, 1760, 2637), 0.8), 0.05)
put(st("s11") - 0.42, whoosh(0.4, 2400, 700, 1.4, 0.4), W * 0.5); put(st("s11") - 0.32, pop(600, 1000, 0.08), 0.1)
# --- s11 CTA
put(wt_("Komen") - 0.06, whoosh(0.4, 600, 2000, 1.4, 0.5), W * 0.5)
for k in range(5): put(wt_("SAHAM,") - 0.08 + k * 0.06, tick(0.022, 4200), 0.15)
put(wt_("SAHAM,") + 0.4, pop(900, 1600, 0.1), 0.15)
put(wt_("aku", 46) - 0.08, whoosh(0.7, 700, 3600, 1.2, 0.5), W); put(wt_("kirim", 46) - 0.02, pop(600, 1000, 0.08), 0.1)
put(wt_("DM.") - 0.06, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.4, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))


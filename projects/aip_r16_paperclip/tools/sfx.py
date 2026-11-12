"""Synthesised SFX bed for the R16 PAPERCLIP reel (was: WEB3D kit) (jualan website 3D, 1 prompt jadi) — no samples, no downloads: hook pops + sparkle bell,
the fan whooshes, "1 prompt" slam, staircase pops + token hops, library window / tiles / prompt-chip flaps, cursor click + copy chime,
paste + send, the AI build (typing, scan rise, product drop), photo/text/colour swaps, theme wipes, "naik kelas" boom, price card
(flaps, scope pops, scribble, stamp), portfolio pops, paid buzz + gift box drop + "gratis", CTA (3D typing, plane, DM chime).
Deterministic. Writes assets/audio/sfx.wav. Run: python3 tools/sfx.py ."""
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
L = lambda txt, sid: wt(txt, st(sid) - 0.05)          # word time inside a given scene (duplicates-safe)
# --- s01 hook: the ID card, the team fans out, fields fill (pop/tick), the paperclip drops + clamps, the stamp
put(0.02, pop(500, 760, 0.08), 0.08)
tA = wt("AI"); put(tA - 0.1, whoosh(0.45, 1800, 600, 1.3, 0.35), W * 0.45); put(tA + 0.02, whoosh(0.45, 700, 2200, 1.4, 0.4), W * 0.3)
t = wt("agent"); put(t + 0.02, bell(0.7), 0.04)
for k in range(4): put(t + 0.05 + k * 0.08, tick(0.02, 3600 + 300 * k), 0.05)
for w in ["jabatan,", "atasan,", "gaji"]: put(wt(w) - 0.06, pop(800, 1300, 0.07), 0.12); put(wt(w) - 0.02, tick(0.02, 2600), 0.07)
put(wt("token,") - 0.1, rise(0.5, 400, 1200), 0.03)
put(wt("kayak") - 0.06, whoosh(0.35, 2400, 700, 1.4, 0.35), W * 0.4)
put(wt("karyawan") + 0.1, tick(0.03, 1800), 0.2); put(wt("karyawan") + 0.12, pop(300, 180, 0.08), 0.12)
put(wt("beneran.") - 0.02, boom(0.35, 170, 70), 0.18); put(wt("beneran.") + 0.0, pop(320, 160, 0.1), 0.1)
# --- s02 name: cards drop, clip flies, letters rise, chips, terminal typing, ✓
put(st("s02") + 0.02, whoosh(0.45, 1600, 400, 1.2, 0.4), W * 0.5)
put(wt("Paperclip:") - 0.12, whoosh(0.4, 500, 2400, 1.3, 0.4), W * 0.4); put(wt("Paperclip:") + 0.2, chime((1318.5, 1760, 2637), 0.9), 0.05)
for k in range(9): put(wt("Paperclip:") - 0.12 + k * 0.035, tick(0.015, 3000 + 120 * k), 0.035)
put(wt("open") - 0.06, pop(700, 1200, 0.08), 0.12); put(wt("gratis,") - 0.06, pop(900, 1500, 0.08), 0.13); put(wt("gratis,") + 0.05, bell(0.6), 0.04)
put(wt("dan", st("s02")) - 0.2, whoosh(0.4, 400, 1600, 1.2, 0.45), W * 0.4)
typing(wt("jalan") - 0.05, wt("komputer") + 0.12, 0.09, 20)
put(wt("komputer") + 0.3, chime((1568, 2093), 0.5), 0.05); put(wt("sendiri.") - 0.06, pop(600, 1000, 0.07), 0.1)
put(st("s03") - 0.25, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.35)
# --- s03 form: window grows, cursor click, field pulse, goal typing, save ✓, goal rises
put(st("s03") + 0.05, whoosh(0.45, 400, 1500, 1.2, 0.45), W * 0.4)
put(wt("tulis") + 0.1, tick(0.03, 2200), 0.18); put(wt("tulis") + 0.12, pop(900, 1400, 0.05), 0.06)
put(wt("toko") - 0.05, pop(600, 900, 0.07), 0.08)
typing(wt("tembus") - 0.04, wt("seminggu.") + 0.1, 0.09, 18)
tSv = wt("seminggu.") + 0.18
put(tSv, tick(0.03, 2000), 0.18); put(tSv + 0.08, chime((1568, 2093, 2637), 0.7), 0.05)
put(tSv + 0.16, whoosh(0.4, 600, 2400, 1.3, 0.4), W * 0.5)
# --- s04 org chart: line drop, CEO pop, doc writes, stamp, tickets fly, teams pop
put(wt("CEO-nya") - 0.1, pop(500, 900, 0.09), 0.14); put(wt("CEO-nya") + 0.0, bell(0.6), 0.035)
put(wt("nyusun") - 0.1, whoosh(0.3, 900, 2200, 1.4, 0.35), W * 0.3)
for k in range(3): put(wt("nyusun") + 0.15 + k * 0.3, scribble(0.22), 0.035)
put(wt("kamu", st("s04")) - 0.12, pop(700, 1100, 0.07), 0.1)
put(wt("setujui,") - 0.18, whoosh(0.3, 600, 2000, 1.4, 0.35), W * 0.3)
put(wt("setujui,") + 0.14, boom(0.35, 170, 70), 0.2); put(wt("setujui,") + 0.16, pop(300, 150, 0.1), 0.12); put(wt("setujui,") + 0.3, chime((1318.5, 1760), 0.6), 0.04)
put(wt("baru", st("s04")) + 0.05, rise(0.5, 300, 900), 0.025)
for k in range(3): t = wt("tugasnya") + 0.09 + k * 0.13; put(t, whoosh(0.3, 1800, 600, 1.4, 0.3), W * 0.25); put(t + 0.36, pop(900 + 100 * k, 600, 0.06), 0.09)
for w in ["web,", "konten,", "riset."]: put(wt(w) - 0.18, pop(600, 1100, 0.09), 0.14); put(wt(w) - 0.1, tick(0.02, 3000), 0.06)
# --- s05 hire: tickets tuck, teams slide, empty seat, request card, switch, new agent
put(st("s05") + 0.05, whoosh(0.35, 2000, 800, 1.3, 0.35), W * 0.35)
put(wt("anggota") - 0.08, whoosh(0.45, 500, 1400, 1.2, 0.4), W * 0.35)
put(wt("baru?") - 0.25, pop(500, 800, 0.08), 0.1)
for k in range(4): put(wt("baru?") + 0.12 + k * 0.09, tick(0.015, 2400), 0.04)
put(wt("CEO-nya", st("s05")) + 0.05, whoosh(0.4, 600, 2000, 1.3, 0.4), W * 0.4); put(wt("CEO-nya", st("s05")) + 0.3, pop(700, 1200, 0.07), 0.1)
put(wt("approve.") - 0.1, tick(0.03, 2200), 0.2); put(wt("approve.") - 0.06, flap(), 0.08); put(wt("approve.") + 0.02, chime((1568, 2093, 2637), 0.7), 0.05)
put(wt("approve.") + 0.1, whoosh(0.3, 2400, 800, 1.4, 0.3), W * 0.3); put(st("s06") - 0.08, pop(500, 900, 0.09), 0.13)
# --- s06 heartbeat: fold into the monitor, sleep, triggers, beeps on each spike, reports, sleep again
put(st("s06") + 0.12, whoosh(0.55, 1600, 500, 1.2, 0.4), W * 0.45)
def beep(f=1046.5, dur=0.12):
    n = int(dur * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * f * t) * np.exp(-t * 18)
put(wt("nggak") + 0.05, pop(400, 200, 0.12), 0.06)
put(wt("bangun") - 0.05, pop(800, 1200, 0.06), 0.08); put(wt("bangun") + 0.07, pop(900, 1300, 0.06), 0.08)
T6 = {"web": wt("tugas") + 0.05, "konten": wt("jadwal,") + 0.08, "ceo": wt("lapor,") + 0.14}
for k, t in T6.items(): put(t, beep(1046.5 if k != "ceo" else 1318.5), 0.12); put(t + 0.16, beep(1046.5 if k != "ceo" else 1318.5), 0.07)
put(wt("tugas") - 0.35, whoosh(0.4, 900, 2200, 1.4, 0.35), W * 0.3); put(wt("jadwal,") - 0.3, whoosh(0.4, 900, 2200, 1.4, 0.35), W * 0.3)
put(wt("kerja,") - 0.05, rise(0.6, 400, 900), 0.02)
put(wt("lapor,") - 0.02, whoosh(0.3, 800, 2400, 1.4, 0.3), W * 0.3); put(wt("lapor,") + 0.3, pop(900, 1400, 0.06), 0.09)
put(wt("tidur") - 0.02, pop(600, 300, 0.12), 0.07)
# --- s07 budget: flip, bars fill (ticks), warning, red stop, pause
put(st("s07") + 0.02, flap(), 0.08)
for k in range(10): put(wt("Token") + 0.3 + k * 0.08, tick(0.015, 2400 + 100 * k), 0.035)
put(wt("budget-nya") + 0.15, beep(880, 0.15), 0.1); put(wt("budget-nya") + 0.32, beep(880, 0.15), 0.08)
put(wt("habis,") - 0.04, rise(0.3, 600, 1400), 0.04); put(wt("habis,") + 0.26, buzz(0.25), 0.04)
put(wt("otomatis") - 0.04, boom(0.35, 160, 60), 0.18); put(wt("otomatis") - 0.02, pop(300, 150, 0.1), 0.12)
put(wt("dijeda.") + 0.05, pop(700, 400, 0.08), 0.08)
put(st("s08") - 0.3, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.45)
# --- s08 caveats: pill, cost card, chips, coin drop, start-small slider, supervisor ticks
put(wt("Catatannya:") - 0.08, pop(600, 1000, 0.08), 0.12)
put(wt("Catatannya:") + 0.35, whoosh(0.45, 400, 1500, 1.2, 0.45), W * 0.4)
put(wt("Catatannya:") + 0.65, pop(500, 900, 0.07), 0.08)
put(wt("agent-nya", st("s08")) - 0.05, whoosh(0.3, 600, 1800, 1.4, 0.35), W * 0.25)
put(wt("API") - 0.06, pop(800, 1300, 0.07), 0.11); put(wt("langganan") - 0.06, pop(900, 1400, 0.07), 0.11)
put(wt("biayanya.") - 0.3, whoosh(0.3, 2400, 900, 1.4, 0.3), W * 0.25)
coin = lambda: chime((2637, 3520), 0.35)
put(wt("biayanya.") + 0.02, coin(), 0.05); put(wt("biayanya.") + 0.08, pop(500, 300, 0.07), 0.08)
put(wt("Mulai") - 0.2, whoosh(0.4, 400, 1400, 1.2, 0.45), W * 0.35)
put(wt("kecil") - 0.05, rise(0.5, 900, 300), 0.03)
put(wt("kecil") + 0.35, pop(800, 1200, 0.06), 0.08); put(wt("kecil") + 0.5, pop(900, 1300, 0.06), 0.08)
put(wt("kamu", st("s08") + 6.5) - 0.2, whoosh(0.4, 400, 1400, 1.2, 0.45), W * 0.35)
tK8, tN8 = wt("kamu", st("s08") + 6.5), wt("ngawasin.")
for i in range(3): put(tK8 + 0.2 + i * ((tN8 + 0.3 - tK8 - 0.2) / 3), pop(1000 + 120 * i, 1500 + 120 * i, 0.06), 0.11)
put(st("s09") - 0.27, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.45)
# --- s09 CTA: package + comment sheet, TIM typing, heart, send, plane, DM, end logo
put(st("s09") + 0.0, whoosh(0.4, 400, 1800, 1.3, 0.45), W * 0.5); put(st("s09") + 0.12, pop(700, 1200, 0.08), 0.1)
tR = wt("TIM,"); ta = max(st("s09") + 0.22, tR - 0.1)
for k in range(3): put(ta + k * 0.12, tick(0.022, 4200), 0.16)
put(ta + 0.32, pop(900, 1600, 0.1), 0.15)
put(wt("aku", st("s09")) - 0.01, tick(0.03, 2000), 0.2); put(wt("aku", st("s09")) + 0.06, whoosh(0.5, 700, 3600, 1.2, 0.45), W * 0.9)
put(wt("DM.") - 0.12, pop(800, 1300, 0.07), 0.1); put(wt("DM.") + 0.08, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
out *= 1.33   # bed level: about 12 LU under the VO (kit balance)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

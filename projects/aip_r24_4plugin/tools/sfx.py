"""Synthesised SFX bed for R20 (Claude Code pakai model AI gratis — FreeLLMAPI) — no samples, no downloads: typing on the terminal,
paywall drop + lock jiggle, wallet drain, "?" pop, road scribble + box landing, LED blips, chips, laptop rise, request envelope,
"ngerti" chime, token arc, quota rows, ring move, drain + "habis" buzz, step cards + typed commands + keys, honest-note stamps,
file flight, magnifier sweep, red chips, stamps, CTA (LLM typing, plane, DM chime), end chime.
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
def ws(txt, sid):                                      # word time inside a given scene (duplicates-safe)
    t = wt(txt, st(sid) - 0.05); assert t is not None, (txt, sid); return t
def out_(sid): put(st(sid) - 0.3, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.45)
def card(t, g=1.0): put(t, whoosh(0.35, 500, 1600, 1.2, 0.45), W * 0.35 * g); put(t + 0.24, pop(420, 760, 0.09), 0.09 * g)
def chip(t, g=1.0): put(t, pop(700, 1150, 0.07), 0.1 * g); put(t + 0.1, tick(0.02, 2600), 0.05 * g)
def okck(t): put(t, pop(900, 1500, 0.06), 0.1); put(t + 0.04, chime((1568, 2093), 0.5), 0.035)
def stamp(t, bad=False): put(t, boom(0.35, 170, 70), 0.18); put(t + 0.02, pop(320, 160, 0.1), 0.1); (put(t + 0.04, buzz(0.18), 0.03) if bad else None)
# --- s01 hook: typing, paywall drop + lock jiggle, wallet rises + drains, "?"
put(0.02, pop(500, 760, 0.08), 0.07)
typing(max(0.12, wt("belajar") - 0.3), wt("Claude Code,") + 0.5, 0.075)
tt = wt("tapi"); put(tt - 0.2, whoosh(0.7, 300, 1800, 1.2, 0.5), W * 0.25)            # robot flies in
put(tt - 0.14, whoosh(0.3, 2200, 700, 1.4, 0.35), W * 0.4); put(tt + 0.12, boom(0.3, 170, 70), 0.13)
for k in range(4): put(tt + 0.22 + k * 0.07, tick(0.02, 1900 + 200 * (k % 2)), 0.07)
card(wt("belum") - 0.12, 0.8); put(wt("sanggup") - 0.05, rise(0.5, 900, 260), 0.025)
tq = wt("langganan?"); put(tq - 0.06, pop(500, 1100, 0.1), 0.14); put(tq + 0.36, tick(0.02, 2200), 0.05); put(tq + 0.5, tick(0.02, 1800), 0.05)
out_("s02")
# --- s02 window shrinks, road draws, signpost, box lands, repo card, LEDs, chips, underline
put(wt("Ada") - 0.05, whoosh(0.4, 1600, 500, 1.2, 0.4), W * 0.4)
put(wt("jalan") - 0.05, scribble(0.5), 0.05); chip(wt("tengahnya:") - 0.06)
tf = wt("FreeLLMAPI,"); put(tf - 0.3, whoosh(0.35, 1800, 500, 1.3, 0.4), W * 0.4); put(tf + 0.05, boom(0.4, 150, 60), 0.2); put(tf + 0.08, pop(320, 180, 0.1), 0.1)
card(tf - 0.1, 0.7); put(tf + 0.25, chime((1318.5, 1760, 2349), 0.7), 0.04)
put(wt("server") - 0.05, square_blips([1320, 1760, 1320, 1760, 2093], 0.09), 0.025); chip(wt("server") - 0.1)
put(wt("kecil") - 0.02, pop(600, 900, 0.07), 0.07)
chip(wt("gratis", 7) - 0.1); put(wt("gratis", 7), chime((1568, 2093, 2637), 0.6), 0.04)
put(wt("GitHub.") - 0.12, tick(0.03, 3000), 0.08); put(wt("GitHub.") - 0.1, whoosh(0.3, 900, 2600, 1.6, 0.3), W * 0.2)
put(st("s03") - 0.3, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.35)
# --- s03 laptop rises, box settles, chip, Claude Code pill + bubble, envelope, "ngerti" badge, OpenAI chip
put(ws("Dia", "s03") - 0.15, whoosh(0.5, 300, 1200, 1.1, 0.5), W * 0.45); put(ws("Dia", "s03") + 0.3, pop(380, 700, 0.09), 0.1)
tl3 = ws("laptopmu,", "s03"); chip(tl3 - 0.1); put(tl3, square_blips([1046, 1318.5, 1046, 1568], 0.1), 0.02)
tn = ws("ngerti", "s03"); chip(tn - 0.3); put(tn - 0.05, pop(600, 1000, 0.08), 0.1)
tfo = ws("format", "s03"); put(tfo - 0.1, whoosh(0.5, 600, 2400, 1.4, 0.4), W * 0.45); put(tfo + 0.4, pop(900, 1400, 0.06), 0.09)
okck(ws("API", "s03") + 0.05); chip(ws("Claude.", "s03") - 0.05)
out_("s04")
# --- s04 app card + typing, box, token arc, panel, rows on names, token drop into Google
put(st("s04") + 0.0, pop(500, 900, 0.08), 0.08); typing(st("s04") + 0.12, ws("Claude Code", "s04") + 0.2, 0.065)
chip(ws("Claude Code", "s04") - 0.12)
td = ws("dioper", "s04"); put(td - 0.12, whoosh(0.5, 600, 2600, 1.4, 0.4), W * 0.5); put(td + 0.36, pop(800, 1300, 0.07), 0.1)
put(td + 0.36, square_blips([1318.5, 1760, 1318.5], 0.09), 0.02)
card(ws("jatah", "s04") - 0.16)
for w_ in ["Google,", "Groq,", "Mistral,", "dan"]: t = ws(w_, "s04") - 0.14; put(t, pop(700, 1100, 0.06), 0.08); put(t + 0.1, rise(0.35, 500, 1100), 0.012)
tg = ws("Google,", "s04"); put(tg - 0.02, whoosh(0.3, 2000, 700, 1.4, 0.3), W * 0.3); okck(tg + 0.3)
out_("s05")
# --- s05 body rises, tag, brain drops + wires, BUKAN CLAUDE stamp, swap, footnote
put(st("s05") + 0.0, whoosh(0.45, 300, 1300, 1.1, 0.5), W * 0.4); put(st("s05") + 0.32, pop(400, 700, 0.09), 0.09)
chip(ws("Claude Code,", "s05") - 0.12)
th = ws("tapi", "s05"); put(th - 0.1, whoosh(0.3, 1800, 600, 1.3, 0.35), W * 0.35); put(th + 0.22, pop(300, 160, 0.1), 0.12)
for k in range(3): put(th + 0.2 + k * 0.05, tick(0.02, 2400 + 200 * k), 0.06)
stamp(ws("bukan", "s05") - 0.02 + 0.18, True)
put(min(ws("Claude.", "s05") - 0.1, ws("bukan", "s05") + 0.24) + 0.06, pop(900, 1400, 0.06), 0.08)
chip(ws("Claude Code,", "s05") + 0.25, 0.6)
out_("s06")
# --- s06 panel, drain + "habis", "otomatis" pill + spin, ring moves, tick
card(st("s06") + 0.0, 0.8)
ts6 = ws("satu", "s06"); put(ts6 - 0.05, rise(0.55, 900, 200), 0.03)
th6 = ws("habis,", "s06"); put(th6, buzz(0.22), 0.035); put(th6 + 0.02, pop(500, 250, 0.1), 0.1)
to = ws("otomatis", "s06"); chip(to - 0.1); put(to, whoosh(0.9, 500, 1700, 2.0, 0.5), W * 0.25)
tp = ws("pindah", "s06"); put(tp - 0.12, whoosh(0.32, 1400, 600, 1.4, 0.35), W * 0.4); put(tp + 0.2, pop(800, 1300, 0.07), 0.1)
okck(ws("lain.", "s06") - 0.08); chip(to + 0.15, 0.6)
out_("s07")
# --- s07 three step cards, typed commands, keys, ticks, result
card(st("s07") + 0.0); typing(ws("servernya,", "s07") - 0.1, ws("isi", "s07") - 0.2, 0.07); okck(ws("isi", "s07") - 0.12)
card(ws("isi", "s07") - 0.14)
for t in [ws("API", "s07"), ws("key", "s07") + 0.12, ws("layanan,", "s07")]: put(t - 0.1, pop(600, 1000, 0.07), 0.1); put(t + 0.22, tick(0.03, 2300), 0.09)
okck(ws("layanan,", "s07") + 0.3)
card(ws("lalu", "s07") - 0.14); typing(ws("satu", "s07") - 0.15, ws("perintah", "s07") + 0.25, 0.07)
tr = ws("perintah", "s07") + 0.42; chip(tr); okck(tr + 0.2); put(tr + 0.05, chime((1318.5, 1760, 2349), 0.8), 0.045)
out_("s08")
# --- s08 honest notes: chip + headline, card 1 tiles + "≠" slam, card 2 bar jumps
chip(st("s08") + 0.0); put(ws("Jujur", "s08") + 0.1, whoosh(0.3, 600, 1600, 1.2, 0.4), W * 0.3)
card(ws("kualitasnya", "s08") - 0.2)
for k, dt in enumerate([-0.05, 0.1]): put(ws("kualitasnya", "s08") + dt, pop(600 + 150 * k, 1000 + 150 * k, 0.07), 0.08)
stamp(ws("beda", "s08") + 0.1)
card(ws("limit", "s08") - 0.2); put(ws("limit", "s08"), rise(0.4, 400, 1000), 0.015); chip(ws("gratisnya", "s08") - 0.05)
for t in [ws("bisa", "s08") - 0.05, ws("berubah.", "s08") - 0.02, ws("berubah.", "s08") + 0.24, ws("berubah.", "s08") + 0.48]: put(t, tick(0.025, 2000), 0.09); put(t, pop(700, 450, 0.06), 0.06)
put(ws("berubah.", "s08") + 0.24, buzz(0.16), 0.025)
out_("s09")
# --- s09 nodes, file flight, eye, ToS + magnifier + highlight, red chips, tip
for k in range(3): put(st("s09") + 0.0 + k * 0.12, pop(500 + 120 * k, 900 + 120 * k, 0.07), 0.08)
tdk = ws("dikirim", "s09"); put(tdk - 0.05, whoosh(0.45, 600, 2200, 1.4, 0.4), W * 0.4); put(ws("server", "s09") - 0.05, whoosh(0.45, 700, 2400, 1.4, 0.4), W * 0.4)
tpn = ws("penyedia,", "s09"); put(tpn + 0.2, pop(900, 500, 0.08), 0.1); put(tpn + 0.24, buzz(0.12), 0.02)
card(ws("baca", "s09") - 0.4); put(ws("baca", "s09") - 0.08, whoosh(0.6, 800, 1800, 2.0, 0.5), W * 0.25)
put(ws("aturannya", "s09") - 0.1, scribble(0.35), 0.05); put(ws("aturannya", "s09"), chime((1318.5, 1760), 0.5), 0.03)
for w_ in ["jangan", "kirim", "data"]: put(ws(w_, "s09") - 0.08, pop(600, 350, 0.08), 0.11)
put(ws("sensitif.", "s09") + 0.02, buzz(0.2), 0.035); okck(ws("sensitif.", "s09") + 0.15)
out_("s10")
# --- s10 two cards, rows, COCOK + NANTI DULU stamps
card(st("s10") + 0.0)
for k in range(3): put(ws("belajar", "s10") - 0.1 + k * 0.12, tick(0.025, 2600 + 200 * k), 0.07)
stamp(ws("dulu,", "s10") - 0.05 + 0.15); put(ws("dulu,", "s10") + 0.1, chime((1568, 2093), 0.5), 0.035)
card(ws("bukan", "s10") - 0.15)
for k in range(2): put(ws("bukan", "s10") + 0.15 + k * 0.12, tick(0.025, 2000 + 150 * k), 0.07)
chip(ws("kerjaan", "s10") + 0.05, 0.7); stamp(ws("klien.", "s10") - 0.05 + 0.15, True)
put(st("s11") - 0.2, whoosh(0.3, 1800, 600, 1.3, 0.35), W * 0.4)
# --- s11 CTA: package card, comment "LLM", heart, send, plane, DM chime, end logo
s11 = st("s11")
put(s11 + 0.0, pop(500, 900, 0.09), 0.12); put(s11 + 0.02, whoosh(0.4, 400, 1800, 1.3, 0.45), W * 0.5)
tR = wt("LLM,"); ta = max(s11 + 0.2, tR - 0.1)
for k in range(3): put(ta + k * 0.15, tick(0.022, 4200), 0.16)
put(ta + 0.42, pop(900, 1600, 0.1), 0.15)
put(wt("aku", s11) - 0.01, tick(0.03, 2000), 0.2); put(wt("aku", s11) + 0.06, whoosh(0.5, 700, 3600, 1.2, 0.45), W * 0.9)
put(wt("DM.") - 0.12, pop(800, 1300, 0.07), 0.1); put(wt("DM.") + 0.08, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

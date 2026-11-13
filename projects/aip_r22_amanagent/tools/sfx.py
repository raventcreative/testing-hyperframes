"""Synthesised SFX bed for R22 (Agent AI di server klien: checklist AMAN) — no samples, no downloads: chat typing dots + message pop,
evidence card + KOSONG stamp, clipboard drop + column pops, phase-rail slide + ticks, badge swing + typed commands, key/ban, sudo
refusal, camera shutter + snapshot slide + pin + flag, selector slide + approval prompt + yolo strikes + JANGAN stamp, toll-gate arms
+ deny, receipt printer (motor + line feeds), vault padlock + eraser bounce + error buzz, diff handle + restore, sticky note flutter
+ wall bounce, CTA (AMAN typing, plane, DM chime), end chime.
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
def rail_tick(t): put(t, pop(1200, 1900, 0.05), 0.08); put(t + 0.03, chime((2093, 2637), 0.35), 0.025)
def shutter(t): put(t, tick(0.02, 5200), 0.22); put(t + 0.06, tick(0.03, 2600), 0.16); put(t + 0.02, whoosh(0.18, 3000, 1200, 1.5, 0.2), W * 0.3)
def printer(t0, t1, gain=0.05):
    n = int((t1 - t0) * SR); tt = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.full(n, 900.0), 3.0) * (0.55 + 0.45 * np.sign(np.sin(2 * np.pi * 38 * tt))) * env(n, 0.1, 1.0)
    put(t0, x / (np.abs(x).max() + 1e-9), gain)
def latch(t): put(t, pop(260, 120, 0.08), 0.16); put(t + 0.025, tick(0.02, 1800), 0.14)
# --- s01 hook: typing dots, question bubble, evidence card, KOSONG stamp
put(0.02, pop(500, 760, 0.08), 0.07)
for r in range(6): put(0.12 + r * 0.26, tick(0.018, 2600), 0.03)
tq = ws("\u201cKemarin", "s01"); put(tq - 0.14, pop(600, 1150, 0.1), 0.14); put(tq - 0.1, chime((1318.5, 1760), 0.4), 0.03)
tk = ws("Kamu", "s01"); card(tk - 0.18, 0.8); put(tk - 0.25, whoosh(0.7, 300, 1800, 1.2, 0.5), W * 0.25)   # robot flies in
stamp(ws("buktinya?", "s01") + 0.2, True)
out_("s02")
# --- s02 clipboard + three columns, rail slides in at the end
card(st("s02") + 0.0); put(ws("tiga", "s02") - 0.12, pop(700, 1200, 0.08), 0.1)
for w_ in ["sebelum,", "selama,", "sesudah"]:
    t = ws(w_, "s02") - 0.16; put(t, pop(520, 900, 0.08), 0.1); [put(t + 0.2 + j * 0.09, tick(0.02, 2400 + 150 * j), 0.05) for j in range(2)]
put(st("s03") - 0.42, whoosh(0.45, 1600, 600, 1.3, 0.4), W * 0.45)
for k in range(3): put(st("s03") - 0.36 + k * 0.06, pop(800 + 120 * k, 1200 + 120 * k, 0.05), 0.05)
# rail: phase changes + ticks (same times as index.html)
for sid in ["s03", "s07", "s09"]: put(st(sid) + 0.02, pop(900, 1400, 0.06), 0.06)
for w_, sid, dt in [("sudo.", "s03", 0.3), ("awal.", "s04", 0.2), ("yolo.", "s05", 0.3), ("ask.", "s06", 0.3), ("jamnya.", "s07", 0.2), ("jejaknya.", "s08", 0.3), ("ubah.", "s09", 0.3)]:
    rail_tick(ws(w_, sid) + dt)
# --- s03 badge swings in, command types, master key + ban, sudo group refusal
put(st("s03") + 0.1, whoosh(0.5, 500, 1400, 1.2, 0.5), W * 0.4); put(st("s03") + 0.5, tick(0.03, 1500), 0.08)
typing(ws("dapat", "s03") - 0.05, ws("sendiri,", "s03") + 0.2, 0.07)
card(ws("sendiri,", "s03") - 0.05, 0.7); put(ws("admin,", "s03") - 0.02, pop(420, 220, 0.09), 0.12); put(ws("admin,", "s03") + 0.18, buzz(0.14), 0.02)
card(ws("grup", "s03") - 0.5, 0.6); put(ws("sudo.", "s03") + 0.02, buzz(0.2), 0.035); put(ws("sudo.", "s03") + 0.06, pop(500, 250, 0.1), 0.1)
out_("s04")
# --- s04 folder, shutter + snapshot, pin, typed git commands, flag
card(st("s04") + 0.0, 0.7)
tc = ws("Commit", "s04"); shutter(tc + 0.1); put(tc + 0.18, whoosh(0.5, 400, 1600, 1.2, 0.45), W * 0.4); put(tc + 0.62, pop(300, 160, 0.09), 0.12)
typing(ws("folder", "s04") - 0.24, ws("git,", "s04") + 0.25, 0.065)
put(ws("titik", "s04") - 0.05, pop(260, 130, 0.1), 0.14); put(ws("titik", "s04"), tick(0.03, 1200), 0.08); put(ws("awal.", "s04"), chime((1568, 2093), 0.5), 0.035)
out_("s05")
# --- s05 selector card, typed command, knob slide, approval prompt, yolo strikes + stamp
card(st("s05") + 0.0, 0.7); typing(ws("set", "s05") - 0.18, ws("manual,", "s05") + 0.15, 0.065)
tm = ws("manual,", "s05"); put(tm - 0.12, whoosh(0.36, 700, 1500, 1.6, 0.4), W * 0.35); put(tm + 0.22, tick(0.03, 1700), 0.12); put(tm + 0.24, pop(600, 900, 0.06), 0.08)
card(tm + 0.18, 0.6)
for k in range(4): put(tm + 0.34 + k * 0.06, pop(700 + 80 * k, 1100 + 80 * k, 0.05), 0.05)
tn = ws("nyalain", "s05")
for k in range(3): put(tn + k * 0.08, scribble(0.16), 0.04)
stamp(ws("yolo.", "s05") + 0.2, True)
out_("s06")
# --- s06 lanes, allow pills, arms drop (ask), deny lane, typed config, footnote
card(st("s06") + 0.0, 0.7)
for k in range(3): put(st("s06") + 0.12 + k * 0.08, pop(500 + 90 * k, 800 + 90 * k, 0.05), 0.05)
for k in range(3): put(ws("serba", "s06") - 0.1 + k * 0.1, pop(900, 1400, 0.05), 0.06)
tp = ws("permission-nya", "s06")
for k in range(3): put(tp + 0.12 + k * 0.16, pop(240, 110, 0.08), 0.13); put(tp + 0.14 + k * 0.16, tick(0.02, 1500), 0.1)
typing(ws("ubah", "s06") - 0.22, ws("ask.", "s06") + 0.2, 0.06)
ta = ws("ask.", "s06"); put(ta + 0.3, pop(240, 110, 0.08), 0.14); put(ta + 0.38, buzz(0.16), 0.03); chip(ta + 0.3, 0.6)
out_("s07")
# --- s07 printer lands, REC blips, paper feeds, typed rule, ring
card(st("s07") + 0.05, 0.8)
tau = ws("auditd", "s07")
for k in range(8): put(tau + k * 0.45, tick(0.015, 3400), 0.025)
for w_, dt in [("merekam", -0.15), ("semua", -0.1), ("perintah", -0.1), ("akun", -0.1), ("akun", 0.2), ("plus", -0.2)]: printer(ws(w_, "s07") + dt, ws(w_, "s07") + dt + 0.26, 0.05)
typing(ws("semua", "s07") - 0.22, ws("akun", "s07") + 0.4, 0.055)
put(ws("akun", "s07") + 0.3, pop(700, 1100, 0.07), 0.08); put(ws("jamnya.", "s07") - 0.18, whoosh(0.3, 900, 2400, 1.6, 0.3), W * 0.25)
out_("s08")
# --- s08 vault, receipt slides in, owner chip, padlock, eraser hit + bounce, error, ok chip
card(st("s08") + 0.0, 0.7); put(ws("Log-nya", "s08"), whoosh(0.4, 1400, 500, 1.3, 0.35), W * 0.3)
chip(ws("milik", "s08") - 0.05); latch(ws("root,", "s08") - 0.06)
put(ws("agent", "s08") - 0.15, whoosh(0.35, 600, 1800, 1.3, 0.35), W * 0.35); typing(ws("agent", "s08") - 0.22, ws("hapus", "s08") - 0.05, 0.06)
th = ws("hapus", "s08"); put(th + 0.04, boom(0.3, 150, 60), 0.16); put(th + 0.06, pop(400, 200, 0.1), 0.12); put(th + 0.1, buzz(0.24), 0.04)
okck(ws("jejaknya.", "s08") + 0.05)
out_("s09")
# --- s09 status card + rows, diff card + panels + handle, rings, typed restore
card(st("s09") + 0.0, 0.7)
for k in range(2): put(ws("status", "s09") - 0.1 + k * 0.16, pop(600 + 150 * k, 950 + 150 * k, 0.06), 0.08)
card(ws("diff", "s09") - 0.3, 0.7); put(ws("diff", "s09") + 0.08, whoosh(0.3, 1800, 700, 1.4, 0.3), W * 0.3); put(ws("diff", "s09") + 0.3, tick(0.03, 1600), 0.1)
put(ws("file", "s09") - 0.1, pop(900, 1400, 0.06), 0.07); put(ws("baris", "s09") - 0.06, pop(900, 1400, 0.06), 0.07)
typing(ws("ubah.", "s09") - 0.22, ws("ubah.", "s09") + 0.5, 0.06)
out_("s10")
# --- s10 note flutters, action passes through, BUKAN PAGAR stamp, fence rises, action bounces off the wall
card(st("s10") + 0.0, 0.7); put(ws("larangan", "s10") - 0.15, whoosh(0.3, 900, 2000, 1.4, 0.3), W * 0.25)
tb = ws("bukan", "s10"); put(tb - 0.05, whoosh(0.45, 500, 2200, 1.4, 0.4), W * 0.4); put(tb + 0.1, rip(0.3), 0.025); put(tb + 0.42, pop(500, 250, 0.1), 0.1)
stamp(ws("pagar.", "s10") + 0.2, True)
card(ws("Pagarnya", "s10") - 0.3, 0.7)
for k in range(3): put(ws("Pagarnya", "s10") - 0.05 + k * 0.12, pop(240 + 40 * k, 130, 0.08), 0.1)
ts_ = ws("sistem.", "s10"); put(ts_ - 0.3, whoosh(0.25, 600, 1600, 1.4, 0.3), W * 0.3); put(ts_ - 0.06, boom(0.25, 160, 70), 0.14); okck(ts_ + 0.06)
put(st("s11") - 0.2, whoosh(0.3, 1800, 600, 1.3, 0.35), W * 0.4)
# --- s11 CTA: package card, comment "AMAN", heart, send, plane, DM chime, end logo
s11 = st("s11")
put(s11 + 0.0, pop(500, 900, 0.09), 0.12); put(s11 + 0.02, whoosh(0.4, 400, 1800, 1.3, 0.45), W * 0.5)
tR = wt("AMAN,"); ta2 = max(s11 + 0.2, tR - 0.1)
for k in range(4): put(ta2 + k * 0.1, tick(0.022, 4200), 0.16)
put(ta2 + 0.42, pop(900, 1600, 0.1), 0.15)
put(wt("aku", s11) - 0.01, tick(0.03, 2000), 0.2); put(wt("aku", s11) + 0.06, whoosh(0.5, 700, 3600, 1.2, 0.45), W * 0.9)
put(wt("DM.") - 0.12, pop(800, 1300, 0.07), 0.1); put(wt("DM.") + 0.08, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

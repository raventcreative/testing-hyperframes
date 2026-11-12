"""Synthesised SFX bed for R12 (5 alat gratis di GitHub jadi 5 menu jasa) — no samples, no downloads: recipe ticks + GRATIS stamp,
warung whoosh, "?" pop, flip + "gratis" ticks, menu board flaps, header drops / ticket rises per tool, schedule ticks + fly-outs,
strip unroll + snips, chat bubbles + typing, agent bell + code typing + review stamp, template pops, licence buzz + magnifier sweep,
headcount pops + WAJIB LISENSI boom, menu ring scribble + click, CTA (JASA typing, plane, DM chime), end chime.
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
# helpers for the repeated beats
def head_in(sid, name):
    t0 = st(sid); put(t0 + 0.0, whoosh(0.4, 500, 1600, 1.2, 0.45), W * 0.4); put(t0 + 0.28, pop(420, 760, 0.09), 0.1)
    tn = L(name, sid); put(tn - 0.04, pop(800, 1300, 0.07), 0.11); put(tn + 0.3, tick(0.025, 2600), 0.08); put(tn + 0.32, pop(900, 1400, 0.05), 0.06)
def ticket_in(t, tp):
    put(t, whoosh(0.35, 600, 1800, 1.3, 0.4), W * 0.35); put(t + 0.3, pop(520, 900, 0.08), 0.1); put(tp, chime((1318.5, 1760), 0.6), 0.04)
def out_(sid):
    put(st(sid) - 0.3, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.5)
# --- s01 hook: recipe on screen, ingredient ticks, GRATIS stamp, warung slides in, "Tetap dibeli", awning flap, "?"
put(0.02, pop(500, 760, 0.08), 0.08)
for i in range(5): put(wt("Resep") + i * 0.192, tick(0.02, 2600 + 200 * i), 0.08)
tg = wt("gratis,"); put(tg - 0.16, whoosh(0.22, 2400, 800, 1.4, 0.3), W * 0.3); put(tg + 0.03, boom(0.35, 170, 70), 0.2); put(tg + 0.03, pop(320, 160, 0.1), 0.12)
put(tg - 0.25, whoosh(0.7, 300, 1800, 1.2, 0.5), W * 0.3)                  # robot flies in
tt = wt("tapi"); put(tt - 0.16, whoosh(0.45, 600, 2200, 1.3, 0.4), W * 0.5); put(tt + 0.3, pop(500, 820, 0.08), 0.09)
tb = wt("beli"); put(tb - 0.1, pop(700, 1100, 0.08), 0.12); put(tb, chime((1318.5, 1760), 0.6), 0.04)
put(wt("warung,") - 0.06, flap(), 0.08)
tk = wt("kan?"); put(tk - 0.1, pop(500, 1100, 0.1), 0.14); put(tk + 0.16, tick(0.02, 2200), 0.06); put(tk + 0.28, tick(0.02, 1800), 0.06)
# --- s02 recipe flips to the 5 tools, "gratis" ticks, warung → menu board, "Klien bayar", "Kamu yang ngerjain"
tl_ = wt("Lima") - 0.16; put(tl_, whoosh(0.3, 900, 2400, 1.6, 0.4), W * 0.35); put(tl_ + 0.15, flap(), 0.08)
for i in range(5): put(tl_ + 0.32 + i * ((wt("GitHub") + 0.3 - tl_ - 0.32) / 5), pop(600 + 80 * i, 1000 + 80 * i, 0.06), 0.08)
tg2 = wt("gratis,", 5)
for i in range(5): put(tg2 - 0.22 + i * 0.07, tick(0.02, 3000 + 150 * i), 0.07)
put(tg2 + 0.1, chime((1568, 2093, 2637), 0.8), 0.05)
tw = wt("tapi", 5) - 0.16; put(tw, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.4)
for i in range(5): put(tw + 0.26 + i * 0.06, tick(0.02, 2000 + 120 * i), 0.06)
put(wt("klien") - 0.1, pop(700, 1200, 0.08), 0.12); put(wt("bayar"), chime((2093, 2637), 0.5), 0.05)
put(wt("yang", 6.5) - 0.14, pop(500, 900, 0.08), 0.1); put(wt("ngerjain.") + 0.1, boom(0.35, 170, 70), 0.18)
out_("s03")
# --- s03 Postiz: post card, schedule pill, accounts fan out, copies fly out, ticks
head_in("s03", "Postiz:")
put(wt("jadwalin") - 0.3, pop(600, 1000, 0.08), 0.1); put(wt("jadwalin") - 0.08, pop(900, 1400, 0.07), 0.11)
for k in range(4): put(wt("jadwalin") + k * 0.12, tick(0.02, 2200 if k % 2 else 1700), 0.08)
for k in range(6): put(wt("banyak") - 0.16 + k * 0.07, pop(700 + 70 * k, 1100 + 70 * k, 0.06), 0.09)
ts = wt("sekaligus,"); put(ts - 0.06, whoosh(0.4, 700, 2600, 1.4, 0.4), W * 0.6)
for k in range(6): put(ts + 0.28 + k * 0.03, tick(0.02, 3200 + 120 * k), 0.07)
put(ts + 0.32, chime((1568, 2093, 2637), 0.8), 0.05)
ticket_in(L("buat", "s03") - 0.16, wt("sosmed."))
out_("s04")
# --- s04 AutoClip: strip unrolls, playhead, highlights + snips, clips grow, subtitles, badges
head_in("s04", "AutoClip:")
put(wt("panjang") - 0.12, rise(0.5, 300, 900), 0.03); put(wt("panjang") - 0.12, whoosh(0.5, 400, 1400, 1.2, 0.5), W * 0.3)
tj = wt("jadi", st("s04"))
for k in range(3): put(tj - 0.12 + k * 0.1, pop(900, 1500, 0.05), 0.08); put(tj + 0.06 + k * 0.1, tick(0.03, 4200), 0.12); put(tj + 0.08 + k * 0.1, rip(0.12), 0.03)
tkl = wt("klip"); put(tkl, whoosh(0.4, 500, 2000, 1.3, 0.4), W * 0.5)
for k in range(3): put(tkl + 0.3 + k * 0.06, pop(500 + 100 * k, 900 + 100 * k, 0.07), 0.1)
for k in range(3): put(wt("bersubtitle,") - 0.1 + k * 0.12, tick(0.025, 2600 + 200 * k), 0.08)
for k in range(2): put(wt("podcaster") - 0.12 + k * 0.12, pop(800, 1300, 0.06), 0.09)
put(wt("seller") - 0.1, pop(900, 1400, 0.06), 0.1); put(wt("seller"), chime((1318.5, 1760), 0.5), 0.04)
ticket_in(L("buat", "s04") - 0.16, wt("seller") + 0.05)
out_("s05")
# --- s05 Chatwoot: inbox slides in, channel chips, bubbles fly into rows, "3 baru", typing reply, send, tick
head_in("s05", "Chatwoot:")
put(wt("chat") - 0.3, whoosh(0.35, 500, 1500, 1.2, 0.4), W * 0.3)
for tc, tf in [(wt("WhatsApp") - 0.14, wt("WhatsApp") + 0.12), (wt("Instagram") - 0.3, wt("Instagram") + 0.06), (wt("Instagram") - 0.08, wt("masuk") + 0.06)]:
    put(tc, pop(700, 1100, 0.07), 0.1); put(tc + 0.12, pop(1200, 1700, 0.05), 0.07); put(tf, whoosh(0.3, 900, 2400, 1.5, 0.35), W * 0.3); put(tf + 0.28, tick(0.02, 2400), 0.08)
put(wt("satu", st("s05")) - 0.06, pop(900, 1500, 0.07), 0.11); put(wt("inbox,") - 0.04, chime((1318.5, 1760, 2349), 0.8), 0.05)
typing(L("buat", "s05"), wt("admin") + 0.35, 0.09)
put(wt("chat.") + 0.02, tick(0.03, 2000), 0.14); put(wt("chat.") + 0.06, whoosh(0.3, 800, 2600, 1.4, 0.35), W * 0.3); put(wt("chat.") + 0.12, chime((1568, 2093), 0.6), 0.05)
ticket_in(L("buat", "s05") - 0.16, wt("admin"))
out_("s06")
# --- s06 OpenHands: instruction card, agent node, code streams, checklist, page slides up, review stamp
head_in("s06", "OpenHands:")
put(wt("OpenHands:") + 0.35, whoosh(0.35, 500, 1500, 1.2, 0.4), W * 0.3)
put(wt("agen") - 0.12, pop(500, 1000, 0.09), 0.12); put(wt("agen"), bell(0.6), 0.03); put(wt("agen") + 0.3, whoosh(0.35, 600, 1800, 1.3, 0.4), W * 0.25)
typing(wt("ngoding") - 0.05, L("buat", "s06") - 0.3, 0.08)
tse, tpe = wt("sesuai"), wt("perintahmu,")
for i in range(3): put(tse + 0.02 + i * ((tpe + 0.45 - tse) / 3), pop(1000 + 150 * i, 1500 + 150 * i, 0.05), 0.1)
put(L("buat", "s06") - 0.05, whoosh(0.4, 500, 1800, 1.3, 0.4), W * 0.4); put(L("buat", "s06") + 0.3, pop(600, 1000, 0.08), 0.1)
put(wt("UMKM.") - 0.04, boom(0.35, 170, 70), 0.18); put(wt("UMKM.") - 0.02, pop(320, 160, 0.1), 0.1)
ticket_in(L("buat", "s06") - 0.16, wt("UMKM.") + 0.1)
out_("s07")
# --- s07 Remotion: code card, lines, tokens, "reel ini" pill, template, six videos fly out, licence chip warning
head_in("s07", "Remotion:")
put(wt("video", st("s07")) - 0.3, whoosh(0.35, 500, 1500, 1.2, 0.4), W * 0.3)
typing(wt("video", st("s07")) - 0.05, wt("kode,") + 0.2, 0.07)
for i in range(3): put(wt("kode,") - 0.1 + i * 0.08, pop(1100 + 120 * i, 1600 + 120 * i, 0.05), 0.08)
put(wt("kayak") - 0.08, pop(700, 1200, 0.08), 0.12); put(wt("reel"), chime((1318.5, 1760, 2349), 0.7), 0.05)
put(wt("Satu", st("s07")) - 0.2, pop(500, 900, 0.09), 0.12); put(wt("template,"), tick(0.025, 2600), 0.08)
tba, tpr = wt("banyak", st("s07")), wt("produk.")
for k in range(6): t = tba - 0.12 + k * ((tpr - tba) / 6); put(t, whoosh(0.25, 900, 2400, 1.5, 0.3), W * 0.2); put(t + 0.22, pop(700 + 90 * k, 1100 + 90 * k, 0.06), 0.09)
put(tpr + 0.08, buzz(0.18), 0.03); put(tpr + 0.08, pop(600, 400, 0.08), 0.08)
ticket_in(tba - 0.3, tpr - 0.1)
out_("s08")
# --- s08 licence: heading words, labels, magnifier sweep, Remotion label lifts, panel, headcount, GRATIS / WAJIB LISENSI
s8 = st("s08")
put(s8 + 0.02, pop(500, 900, 0.09), 0.1)
for w_ in ["gratis", "belum", "bebas:"]: put(wt(w_, s8) - 0.1, pop(700, 1100, 0.07), 0.1)
for k in range(5): put(s8 + 0.12 + k * 0.07, pop(800 + 80 * k, 1200 + 80 * k, 0.05), 0.07)
tR = wt("Remotion", s8); tT = wt("Tapi")
put(tT + 0.3, whoosh(tR - 0.25 - tT - 0.3, 600, 1400, 1.0, 0.5), W * 0.25)
for k in range(5): put(tT + 0.3 + k * ((tR - 0.25 - tT - 0.3) / 5), tick(0.02, 2400 + 200 * k), 0.07)
put(tR - 0.08, buzz(0.22), 0.035); put(tR - 0.06, pop(600, 1000, 0.08), 0.1); put(tR + 0.02, whoosh(0.4, 500, 1600, 1.2, 0.45), W * 0.4)
tKa, tLe, tTi = wt("kalau"), wt("lebih"), wt("tiga.")
for k in range(3): put(tKa - 0.05 + k * 0.12, pop(900 + 100 * k, 1400 + 100 * k, 0.06), 0.1)
put(wt("karyawanmu") + 0.25, chime((1318.5, 1760), 0.6), 0.04)
for k in range(3): put(tLe - 0.1 + k * 0.1, pop(500 + 60 * k, 800 + 60 * k, 0.07), 0.1)
put(tLe + 0.38, boom(0.4, 150, 60), 0.2); put(tLe + 0.4, buzz(0.2), 0.03); put(tTi, pop(600, 1000, 0.06), 0.07)
put(st("s09") - 0.16, whoosh(0.3, 1800, 600, 1.3, 0.35), W * 0.4)
# --- s09 menu board returns, ticks, "pilih satu" ring + click, 3-step path
s9 = st("s09")
put(s9 + 0.0, whoosh(0.4, 500, 1600, 1.2, 0.45), W * 0.4); put(s9 + 0.3, pop(420, 760, 0.09), 0.1)
for k in range(5): put(max(s9 + 0.35, wt("Cek")) + k * ((wt("pilih") - 0.25 - wt("Cek")) / 5), tick(0.02, 3000 + 150 * k), 0.08)
put(wt("pilih"), scribble(0.4), 0.06); put(wt("jasa,", s9) - 0.02, tick(0.03, 2000), 0.16); put(wt("jasa,", s9), pop(900, 1500, 0.06), 0.1)
for k in range(3): t = wt("latihan") - 0.12 if k == 0 else wt("latihan") + 0.2 + k * ((wt("teman.") - wt("latihan") - 0.2) / 2.2); put(t, pop(600 + 120 * k, 1000 + 120 * k, 0.07), 0.11)
put(wt("latihan") + 0.02, chime((1318.5, 1760, 2349), 0.7), 0.04)
put(st("s10") - 0.26, whoosh(0.3, 1800, 600, 1.3, 0.35), W * 0.4)
# --- s10 CTA: package card, comment "JASA", heart, send, plane, DM chime, end logo
s10 = st("s10")
put(s10 + 0.0, pop(500, 900, 0.09), 0.12); put(s10 + 0.02, whoosh(0.4, 400, 1800, 1.3, 0.45), W * 0.5)
tR = wt("JASA,"); ta = max(s10 + 0.2, tR - 0.1)
for k in range(4): put(ta + k * 0.1, tick(0.022, 4200), 0.16)
put(ta + 0.42, pop(900, 1600, 0.1), 0.15)
put(wt("aku", s10) - 0.01, tick(0.03, 2000), 0.2); put(wt("aku", s10) + 0.06, whoosh(0.5, 700, 3600, 1.2, 0.45), W * 0.9)
put(wt("DM.") - 0.12, pop(800, 1300, 0.07), 0.1); put(wt("DM.") + 0.08, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

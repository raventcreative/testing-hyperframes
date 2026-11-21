"""SFX for R33 (assets/audio/sfx.wav, 48 kHz mono, 104.6 s) — client: "kasih sound effect biar gak suara VO aja".
Samples: the repo's vo_safe set (assets/sfx) + a few synthesised in code (message send/receive blips, soft impact, riser).
Levels are set relative to the VO peak (≈ -8…-10 dB under it for hits/whooshes, quieter for caption ticks/typing), fixed (the remix uses
no compressor on the SFX). Event times come from the VO alignment (production/words.json, +0.3 s); every sample is placed by its measured
PEAK and nudged (±150 ms max) so no transient lands within 70 ms of a word onset."""
import json, subprocess, wave
import numpy as np
SR, DUR, OFF = 48000, 104.6, 0.3
W = json.load(open("production/words.json")); ON = np.array([s + OFF for _, s, _ in W])
def wt(txt, after=0):
    for w, s, e in W:
        if w == txt and s + OFF >= after: return s + OFF
    raise SystemExit("sfx: word not found " + txt)
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", "assets/audio/vo.mp3", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout
VOPK = float(np.abs(np.frombuffer(pcm, np.int16) / 32768).max())
out = np.zeros(int(SR * DUR))
def load(n):
    w = wave.open(f"assets/sfx/{n}.wav"); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
    a = a.reshape(-1, w.getnchannels()).mean(axis=1); return a / np.abs(a).max()
S = {n: load(n) for n in ["click", "key", "ping", "pop", "sparkle", "type", "whoosh"]}
tt = lambda d: np.arange(int(SR * d)) / SR
def blip(f0, f1, d=0.16):   # message send (rising) / receive (falling) — two short sine notes
    t = tt(d); h = len(t) // 2; f = np.where(np.arange(len(t)) < h, f0, f1)
    env = np.minimum(1, t / 0.004) * np.exp(-((t % (d / 2)) / 0.05)); x = np.sin(2 * np.pi * np.cumsum(f) / SR) * env
    return x / np.abs(x).max()
def impact(d=0.7):          # soft low thump + air
    t = tt(d); rng = np.random.default_rng(3); x = np.sin(2 * np.pi * (55 + 40 * np.exp(-t * 18)) * t) * np.exp(-t * 6)
    x += 0.25 * rng.standard_normal(len(t)) * np.exp(-t * 14); x = np.convolve(x, np.ones(6) / 6, "same"); return x / np.abs(x).max()
def riser(d=0.7):           # filtered noise swelling into the hit (peak at the end)
    t = tt(d); rng = np.random.default_rng(5); n = rng.standard_normal(len(t)); y = np.zeros_like(n); a = 0.0
    for i in range(len(n)): k = 0.02 + 0.5 * (t[i] / d) ** 2; a += k * (n[i] - a); y[i] = a
    y *= (t / d) ** 2.2 * np.minimum(1, (d - t) / 0.02); return y / np.abs(y).max()
S.update({"send": blip(880, 1318), "recv": blip(1318, 988), "impact": impact(), "riser": riser()})
PK = {n: int(np.argmax(np.abs(x))) for n, x in S.items()}
def safe(t):
    for dt in (0, -0.03, 0.03, -0.06, 0.06, -0.09, 0.09, -0.12, 0.12, -0.15, 0.15):
        if np.all(np.abs(ON - (t + dt)) >= 0.07): return t + dt
    return None
LOG, SKIP = [], []
def put(t, n, db, rate=1.0):   # db relative to the VO peak
    x = S[n]; pk = PK[n] / rate
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    t = safe(t)
    if t is None: SKIP.append(n); return
    i = max(0, int(t * SR - pk)); j = min(len(out), i + len(x)); out[i:j] += VOPK * 10 ** (db / 20) * x[: j - i]; LOG.append((t, n))
L1, L2, L3, L4, KIR, CARA, TEMP, RIW, TAPI, KOM = wt("Laci"), wt("Laci", 24), wt("Laci", 31.5), wt("Laci", 37.6), wt("Kirain"), wt("Cara"), wt("Tempel"), wt("Riwayat"), wt("Tapi"), wt("Komen")
# ---- transitions: a whoosh on every one, riser + soft impact on the big reveals
for t, r in [(6.35, 0.75), (KIR - 0.3, 1.1), (L1 + 0.2, 1.2), (L2 - 0.05, 1.35), (L3 - 0.3, 0.7), (L4 - 0.05, 1.0), (41.05, 0.9), (CARA - 0.35, 1.25),
             (RIW - 0.4, 0.75), (TAPI - 0.55, 0.65), (90.1, 1.05), (94.55, 0.85), (KOM - 0.2, 0.9)]:
    put(t, "whoosh", -8, r)
for t in (5.55, KIR - 0.2, 41.42, KOM - 0.2): put(t - 0.02, "riser", -12); put(t, "impact", -9)
put(wt("Claude") - 0.05, "impact", -11)                                                   # Claude logo lands in the hook
# ---- hook: thumb swiping the list (soft ticks), the found message
for k in range(34): put(0.25 + k * 0.12, "key", -17, 1.35)
put(wt("nyariin") - 0.15, "recv", -10); put(wt("nyariin") + 0.2, "sparkle", -13)
# ---- titles + chips (UI pops)
for t in [7.0, KIR + 0.1, L1, L2, L3, L4, 41.65, CARA + 0.05, TEMP, RIW - 0.25, TAPI - 0.1, 90.6, 94.9]: put(t + 0.05, "click", -12, 0.9)
for t in [0.5, wt("dua") - 0.1, L1 + 0.05, wt("Siapin") - 0.1, wt("kira-kira") - 0.1]: put(t + 0.05, "pop", -11, 1.2)
# ---- caption-in ticks (one per caption chunk, very soft)
ch, a = [], 0
for i, (w, s, e) in enumerate(W):
    if w[-1] in ",.:?" or i - a == 3 or i == len(W) - 1: ch.append(a); a = i + 1
for i in ch: put(W[i][1] + OFF - 0.1, "key", -19, 1.6)
# ---- B: repo sign, planks, bubble crosses + dives
put(wt("open") - 0.1, "pop", -9, 0.9); put(wt("Luke"), "click", -13); put(wt("MIT.") + 0.05, "pop", -11, 1.1)
for i in range(6): put(wt("nyambungin") + i * 0.15 + 0.25, "click", -10, 0.75)
put(wt("Claude", 12) - 0.55, "send", -10)
# ---- K: tiles rain, drawers light, drawers open, every tool card pops
for i in range(12): put(wt("dua") + i * 0.06 + 0.42, "key", -14, 1.1)
for i in range(4): put(wt("empat") + i * 0.14, "pop", -12, 1.3)
for L in (L1, L2, L3, L4): put(L + 0.12, "click", -9, 0.7)
TOOLT = [wt("cari", 19), wt("lihat"), wt("buka"), wt("nemuin"), wt("tarik"), wt("lihat", 26), wt("cek"), wt("semua"), wt("pesan", 32.8), wt("file"), wt("plus"), wt("media")]
for t in TOOLT: put(t, "pop", -9, 1.0)
for i in range(2): put(wt("pesan", 32.8) + 0.05 + i * 0.55, "send", -11)                # messages to the phone and the group
for i in range(3): put(wt("file") + 0.15 + i * 0.42, "pop", -12, 0.8)                     # three files
for i in range(4): put(wt("media") + i * 0.32 + 0.4, "click", -12, 1.2)                    # media land in the laptop
put(wt("media") + 1.4, "sparkle", -11)                                                    # 12/12
# ---- A: click, typing, send, tools tick, answer arrives
put(wt("Misalnya,") - 0.15, "click", -9)
for i in range(15): put(wt("supplier") + i * 0.1, "type", -16, 1.5)
put(wt("Claude", 48) - 0.15, "send", -8)
for t in (wt("milih") + 0.05, wt("nyari", 49) - 0.1, wt("pesanmu,") + 0.2): put(t, "ping", -13, 1.25)
put(wt("lalu", 50) - 0.05, "recv", -9); put(wt("lengkap") - 0.3, "pop", -11, 0.9)
# ---- S: crates, terminal typing, QR scan, connected, config paste, restart, toggle
for t in (wt("Go,"), wt("Python,"), wt("UV,"), wt("Claude", 55)): put(t + 0.17, "impact", -13); put(t + 0.17, "pop", -11, 0.6)
put(wt("Claude", 55) + 0.75, "sparkle", -13)
for i in range(12): put(wt("Unduh", 56) + i * 0.06, "type", -15, 1.7)
for i in range(5): put(wt("jalankan") + i * 0.08, "type", -15, 1.7)
put(wt("scan") - 0.2, "pop", -11); put(wt("kode") + 0.1, "ping", -12); put(wt("ponselmu.") + 0.25, "recv", -10)
put(TEMP + 0.1, "click", -10)
for i in range(10): put(TEMP + 0.05 + i * 0.05, "key", -17, 1.4)
put(wt("restart,") + 0.05, "whoosh", -14, 1.6); put(wt("muncul") + 0.05, "click", -9); put(wt("muncul") + 0.15, "sparkle", -13)
# ---- L: messages flow into SQLite, the key, the bar, one bubble to Claude, the lever
for i in range(6): put(RIW + i * 0.45 + 0.3, "pop", -15, 1.3)
put(wt("komputermu", 68) - 0.2, "pop", -11)
put(wt("dikirim"), "click", -11, 0.8); put(wt("tool-nya") + 0.2, "click", -10, 0.6); put(wt("tool-nya") + 0.4, "send", -11)
put(wt("kamu", 73), "impact", -12); put(wt("kamu", 73), "click", -10, 0.5)
# ---- X: README board, line highlights, leak, trojan message, x-ray, checkpoint
put(TAPI + 0.2, "impact", -12)
for t in (wt("seperti", 78), wt("risiko"), wt("bocor.") - 0.5): put(t, "click", -12, 1.1)
for i in range(5): put(wt("risiko") + 0.9 + i * 0.32, "pop", -15, 1.5)
put(wt("pesan", 84) - 0.3, "recv", -10); put(wt("nyelipin"), "riser", -13); put(wt("nyelipin") + 0.1, "ping", -11, 0.8)
put(wt("cek", 87) + 0.05, "click", -9); put(wt("ngirim") + 0.15, "send", -10)
# ---- C: calendar flips, QR, scan
for i in range(0, 19, 2): put(wt("kira-kira") + i * 0.065, "key", -15)
put(wt("koneksinya") - 0.1, "pop", -11); put(wt("minta"), "ping", -12)
# ---- F + CTA: lever, typing WA, send, DM arrives
put(wt("kendali") + 0.1, "click", -9, 0.6); put(wt("kendali") + 0.2, "impact", -13)
for i in range(2): put(wt("WA,") + i * 0.12, "key", -11)
put(wt("aku", 98) + 0.05, "send", -8); put(wt("panduan") - 0.1, "recv", -8); put(wt("panduan") + 0.2, "sparkle", -13)
out = np.clip(out, -1, 1)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
near = [t for t, n in LOG if np.any(np.abs(ON - t) < 0.07)]
print(f"sfx: {len(LOG)} events, peak {np.abs(out).max():.3f} (VO peak {VOPK:.3f}), events still near a word onset: {len(near)}, skipped (no gap): {SKIP}")

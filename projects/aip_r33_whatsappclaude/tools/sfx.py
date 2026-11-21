"""SFX for R33 (assets/audio/sfx.wav, 48 kHz mono, 104.6 s) from the repo's vo_safe set (assets/sfx). Event times come from the VO
alignment (production/words.json, +0.3 s). Each sample is placed by its measured PEAK, at a fixed low level, and nudged so no
transient lands within 70 ms of a word onset."""
import json, wave
import numpy as np
SR, DUR, OFF = 48000, 104.6, 0.3
W = json.load(open("production/words.json")); ON = np.array([s + OFF for _, s, _ in W])
def wt(txt, after=0):
    for w, s, e in W:
        if w == txt and s + OFF >= after: return s + OFF
    raise SystemExit("sfx: word not found " + txt)
out = np.zeros(int(SR * DUR))
def load(n):
    w = wave.open(f"assets/sfx/{n}.wav"); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
    return a.reshape(-1, w.getnchannels()).mean(axis=1)
S = {n: load(n) for n in ["click", "key", "ping", "pop", "sparkle", "type", "whoosh"]}
PK = {n: int(np.argmax(np.abs(x))) for n, x in S.items()}
def put(t, n, g=1.0, rate=1.0):
    x = S[n]; pk = PK[n] / rate
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    d = ON - t; near = d[np.abs(d) < 0.07]
    if len(near): t = t - 0.08 if near[0] >= 0 else t + 0.08          # keep transients off word onsets
    i = int(t * SR - pk); i = max(0, i); j = min(len(out), i + len(x)); out[i:j] += g * x[: j - i]
G = 0.55                                                               # global SFX level (fixed, no ducking compressor)
L1, L2, L3, L4, KIR, CARA, TEMP, RIW, TAPI, KOM = wt("Laci"), wt("Laci", 24), wt("Laci", 31.5), wt("Laci", 37.6), wt("Kirain"), wt("Cara"), wt("Tempel"), wt("Riwayat"), wt("Tapi"), wt("Komen")
for k in range(0, 40): put(0.2 + k * 0.1, "key", 0.05 * G, 1.4)                         # thumb swiping the list
put(wt("Claude") - 0.1, "sparkle", 0.25 * G); put(wt("nyariin") - 0.2, "ping", 0.2 * G)  # Claude finds it
put(5.6, "whoosh", 0.25 * G, 0.8); put(6.35, "whoosh", 0.3 * G, 0.7)                     # reveal + island hop
put(7.0, "click", 0.15 * G); put(wt("open") - 0.1, "pop", 0.2 * G)
for i in range(6): put(wt("nyambungin") + i * 0.15 + 0.25, "click", 0.12 * G, 0.8)      # planks
put(KIR - 0.35, "whoosh", 0.3 * G, 1.2)                                                  # dive + flash
for i in range(12): put(wt("dua") + i * 0.06 + 0.4, "key", 0.06 * G, 1.1)               # tiles
for i in range(4): put(wt("empat") + i * 0.14, "pop", 0.12 * G, 1.2)
for L in (L1, L2, L3, L4): put(L + 0.1, "click", 0.18 * G, 0.7)                          # drawers open
put(L2 - 0.05, "whoosh", 0.25 * G, 1.3); put(L3 - 0.3, "whoosh", 0.3 * G, 0.6); put(L4 - 0.05, "whoosh", 0.22 * G, 1.0)
for t in [wt("cari", 19), wt("lihat"), wt("buka"), wt("nemuin"), wt("tarik"), wt("lihat", 26), wt("cek"), wt("semua"), wt("pesan", 32.8), wt("file"), wt("plus"), wt("media")]:
    put(t, "pop", 0.14 * G, 1.0)                                                         # each tool lands
put(wt("media") + 1.4, "sparkle", 0.2 * G)                                               # 12/12
put(41.0, "whoosh", 0.25 * G, 0.9)                                                       # iris
put(wt("Misalnya,") - 0.15, "click", 0.18 * G)
for i in range(14): put(wt("supplier") + i * 0.11, "type", 0.06 * G, 1.5)               # typing the question
put(wt("Claude", 48) - 0.15, "click", 0.2 * G)
for t in (wt("milih") + 0.05, wt("nyari", 49) - 0.1, wt("pesanmu,") + 0.2): put(t, "ping", 0.1 * G, 1.2)
put(wt("lengkap") + 0.2, "sparkle", 0.18 * G)
put(CARA - 0.4, "whoosh", 0.3 * G, 1.2)                                                  # whip tilt
for t in (wt("Go,"), wt("Python,"), wt("UV,"), wt("Claude", 55)): put(t + 0.17, "pop", 0.18 * G, 0.6)  # crates land
for i in range(10): put(wt("Unduh", 56) + i * 0.08, "type", 0.05 * G, 1.6)
put(wt("scan") + 0.1, "ping", 0.12 * G); put(wt("ponselmu.") + 0.25, "sparkle", 0.15 * G)
put(TEMP + 0.1, "click", 0.15 * G); put(wt("restart,") + 0.05, "whoosh", 0.15 * G, 1.4); put(wt("muncul") + 0.05, "click", 0.18 * G)
put(RIW - 0.45, "whoosh", 0.28 * G, 0.7)                                                 # dolly zoom
for i in range(6): put(RIW + i * 0.45 + 0.3, "pop", 0.06 * G, 1.3)
put(wt("dikirim"), "click", 0.16 * G, 0.8); put(wt("tool-nya") + 0.2, "click", 0.16 * G, 0.6); put(wt("kamu", 73), "click", 0.2 * G, 0.5)
put(TAPI - 0.7, "whoosh", 0.3 * G, 0.6)                                                  # orbit
put(wt("bocor.") - 0.4, "type", 0.08 * G, 0.8)
put(wt("nyelipin"), "ping", 0.12 * G, 0.8); put(wt("cek", 87) + 0.05, "click", 0.2 * G); put(wt("ngirim"), "pop", 0.14 * G)
put(90.05, "whoosh", 0.3 * G, 1.1)                                                       # shutter
for i in range(0, 19, 2): put(wt("kira-kira") + i * 0.06, "key", 0.05 * G)               # calendar flips
put(wt("scan", 93), "ping", 0.12 * G)
put(94.45, "whoosh", 0.28 * G, 0.8); put(wt("kendali") + 0.1, "click", 0.2 * G, 0.6)
put(KOM - 0.2, "pop", 0.22 * G, 0.6); put(KOM - 0.18, "whoosh", 0.2 * G, 0.9)           # ring
for i in range(2): put(wt("WA,") + i * 0.12, "key", 0.12 * G)
put(wt("aku", 98) + 0.05, "click", 0.2 * G); put(wt("panduan") - 0.1, "ping", 0.18 * G)
out = np.clip(out, -1, 1)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
print("sfx peak", round(float(np.abs(out).max()), 3))

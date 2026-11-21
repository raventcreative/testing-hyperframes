"""SFX for R32 (assets/audio/sfx.wav, 48 kHz mono, 55.6 s) — v2, client: "kasih sound effect biar gak suara VO aja".
Sources: the repo's vo_safe samples (assets/sfx) + a few sounds synthesised here in numpy (shutter, riser, hum, ding, chat blips,
caption ticks). Event times come from the VO word timings (production/words.json + 0.3 s), the same lookups the scenes use.
Levels are set RELATIVE TO THE VO PEAK as they will sound in the final remix (tools/remix_audio.sh plays this file at x0.6, fixed,
no sidechain): transitions/shutter ~-8 dB, UI pops/blips/ding ~-10 dB, risers -10 dB at their peak, typing/caption ticks -13..-15 dB.
No hit on a word onset: every event is placed by its measured PEAK and nudged off any onset closer than 60 ms."""
import json, wave, subprocess
import numpy as np
SR, DUR, OFF, REMIX_GAIN = 48000, 55.6, 0.3, 0.6
WORDS = json.load(open("production/words.json"))
ONSETS = np.array([s + OFF for _, s, _ in WORDS])
def W(txt, after=0.0):
    for w, s, e in WORDS:
        if w == txt and s + OFF >= after: return s + OFF
    raise KeyError(txt)
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", "assets/audio/vo.mp3", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout
VO_PEAK = float(np.abs(np.frombuffer(pcm, np.int16) / 32768).max())
out = np.zeros(int(SR * DUR))
def load(n):
    w = wave.open(f"assets/sfx/{n}.wav"); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
    return a.reshape(-1, w.getnchannels()).mean(axis=1)
S = {n: load(n) for n in ["click", "key", "ping", "pop", "sparkle", "type", "whoosh"]}
rng = np.random.default_rng(32)
tt = lambda d: np.arange(int(SR * d)) / SR
def hp(x, k=0.97):  # one-pole high-pass
    y = np.zeros_like(x); p = 0.0; px = 0.0
    for i, v in enumerate(x): p = k * (p + v - px); px = v; y[i] = p
    return y
def lp(x, a):       # one-pole low-pass (a may be an array, 0..1)
    y = np.zeros_like(x); p = 0.0; a = np.broadcast_to(a, x.shape)
    for i, v in enumerate(x): p += a[i] * (v - p); y[i] = p
    return y
# synthesised sounds
def shutter():
    def burst(d, k): t = tt(d); return hp(rng.standard_normal(len(t))) * np.exp(-t * k)
    x = np.zeros(int(SR * 0.16)); a = burst(0.03, 160); b = burst(0.045, 110); i = int(SR * 0.055)
    x[: len(a)] += a; x[i: i + len(b)] += 0.8 * b
    t = tt(0.16); x += 0.25 * np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 90)
    return x
def riser(d=0.9):
    t = tt(d); u = t / d; n = rng.standard_normal(len(t))
    x = lp(n, 0.02 + 0.5 * u ** 2) * (u ** 2.2) + 0.25 * np.sin(2 * np.pi * (300 + 900 * u ** 2) * t) * u ** 3
    x[-int(SR * 0.01):] *= np.linspace(1, 0, int(SR * 0.01)); return x
def hum(d=0.85):
    t = tt(d); env = np.minimum(1, t / 0.08) * np.minimum(1, (d - t) / 0.15)
    return env * (np.sin(2 * np.pi * 110 * t) + 0.5 * np.sin(2 * np.pi * 220 * t) + 0.2 * np.sin(2 * np.pi * 330 * t)) * (0.8 + 0.2 * np.sin(2 * np.pi * 9 * t))
def ding():
    t = tt(1.1); return sum(a * np.sin(2 * np.pi * f * t) * np.exp(-t * k) for f, a, k in [(1320, 1, 4.5), (2640, 0.45, 7), (3960, 0.2, 10)])
def blip(f0, f1, d=0.09):
    t = tt(d); f = f0 + (f1 - f0) * t / d; ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.minimum(1, t / 0.005) * np.exp(-t * 18)
def blip2(): a = blip(880, 900, 0.07); b = blip(1320, 1340, 0.09); x = np.zeros(int(SR * 0.17)); x[: len(a)] += a; x[int(SR * 0.075): int(SR * 0.075) + len(b)] += b; return x
def tick():
    t = tt(0.03); return np.sin(2 * np.pi * 2100 * t) * np.exp(-t * 220)
SY = {"shutter": shutter(), "riser": riser(), "riser_s": riser(0.6), "hum": hum(), "ding": ding(), "send": blip(620, 1250, 0.1), "recv": blip2(), "tick": tick()}
LOG = []
def put(t, n, rel_db, rate=1.0, gain_end=False):
    x = SY[n] if n in SY else S[n]
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    x = x / (np.abs(x).max() + 1e-9) * VO_PEAK * 10 ** (rel_db / 20) / REMIX_GAIN   # peak relative to the VO peak in the final mix
    pk = int(np.argmax(np.abs(x))) / SR
    for _ in range(3):                                                             # nudge the peak off any word onset (60 ms)
        d = ONSETS - t; near = d[np.abs(d) < 0.06]
        if not near.size: break
        t = t + (near[0] - 0.065 if near[0] > 0 else near[0] + 0.065)
    i = int((t - pk) * SR); i0 = max(0, i); j = min(len(out), i + len(x))
    if j > i0: out[i0:j] += x[i0 - i: j - i]
    LOG.append((round(t, 3), n, rel_db))
T = dict(produk=W("produk,"), ai=W("AI"), bikinin=W("bikinin"), video=W("video"), suara=W("suara"), ini=W("Ini"), cocok=W("cocok"), umkm=W("UMKM,"), online=W("online"), sampai=W("sampai"),
         satu=W("Satu."), terang=W("terang:"), depan=W("depan,"), samping=W("samping,"), detail=W("detail"), dua=W("Dua."), kirim=W("Kirim"), asisten=W("asisten"),
         nulis=W("nulis"), susunan=W("susunan"), adegan=W("adegan,"), detik=W("detik"), detik2=W("detik."), harga=W("harga,"), ukuran=W("ukuran,"), siapa=W("siapa"),
         hook=W("Hook"), manfaat=W("manfaat"), satu1=W("satu", 20), persatu=W("satu,", 20), ajakan=W("ajakan"), keranjang=W("keranjang"), tiga=W("Tiga."),
         naskah2=W("Naskah"), suara2=W("suara", 30), gaya=W("gaya"), jualan=W("jualan."), empat=W("Empat."), adegan2=W("Adegan,"), foto2=W("foto,", 30), suara3=W("suara", 36),
         dirender=W("dirender"), video2=W("video", 36), siap=W("siap"), video3=W("Video"), juga=W("juga", 40), dibikin=W("dibikin"), pakai=W("pakai"),
         tapi=W("Tapi"), alat=W("alat"), jaminan=W("jaminan"), klaim=W("klaim"), sebelum=W("sebelum"), posting=W("posting."), komen=W("Komen"), promo=W("promo,"), kirim2=W("kirim", 50))
# ---- transitions: whoosh on every one (+ soft risers into the reveals)
put(5.62, "riser", -10); put(5.75, "whoosh", -8, 0.6)                              # zoom-out reveal (map)
put(T["cocok"] - 0.05, "whoosh", -9, 0.9)                                          # pan to "who it's for"
put(10.55, "whoosh", -8, 0.8)                                                      # island-hop flight
put(T["dua"] - 0.05, "riser_s", -10); put(T["dua"] - 0.2, "whoosh", -8, 1.2)      # photo flies into the lens (match cut)
put(T["hook"] - 0.32, "whoosh", -8, 0.9)                                           # elevator doors
put(T["tiga"] - 0.16, "whoosh", -8, 1.3)                                           # whip tilt
put(T["jualan"] + 0.45, "whoosh", -8, 0.6)                                         # 180° orbit
put(T["video3"] + 0.1, "whoosh", -9, 0.5)                                          # dolly zoom
put(T["tapi"] - 0.42, "whoosh", -8, 0.9)                                           # iris
put(T["komen"] - 0.3, "riser_s", -12); put(T["komen"] - 0.2, "whoosh", -8, 0.8); put(T["komen"] - 0.12, "pop", -11, 0.5)   # shockwave into the CTA
# ---- hook
put(T["produk"], "shutter", -8)                                                    # camera shutter on the photo
put(T["ai"] - 0.02, "pop", -10, 0.8); put(T["ai"] + 0.1, "sparkle", -12)          # AI cube
put(T["video"] - 0.1, "riser_s", -10); put(T["video"], "pop", -9, 0.7)             # cube unfolds into the promo screen
put(T["suara"] + 0.12, "sparkle", -11)                                             # speaker rings
for i in range(4): put(T["ini"] - 0.1 + i * 0.28, "tick", -12)                     # the path lights the 4 islands
for k in ("umkm", "online", "sampai"): put(T[k] - 0.05, "pop", -10, 0.9)
# ---- step 1: lights + three photos
put(T["terang"], "click", -10, 0.6)
for k in ("depan", "samping", "detail"): put(T[k], "shutter", -8); put(T[k] + 0.5, "pop", -12, 1.2)
# ---- step 2: chat (typing ticks, send / receive blips, rows, chips)
TY0, TY1 = T["dua"] + 0.12, T["kirim"] + 0.45
for k in range(int((TY1 - TY0) / 0.07)): put(TY0 + k * 0.07, "key", -15, 1.1 + 0.08 * (k % 3))
put(T["asisten"] + 0.02, "send", -10)
put(T["nulis"] - 0.05, "recv", -10)
for k in ("susunan", "adegan", "detik", "detik2"): put(T[k] - 0.02, "tick", -13)
for k in ("harga", "ukuran", "siapa"): put(T[k] - 0.02, "pop", -10, 1.0)
for k in ("hook", "manfaat", "satu1", "persatu", "ajakan"): put(T[k] - 0.05, "click", -10, 0.6)   # script blocks land
for k in range(6): put(T["keranjang"] - 0.35 + k * 0.07, "key", -15, 0.8)                         # cart rolls in
put(T["keranjang"] + 0.15, "ping", -11, 1.1)
# ---- step 3: AI voice booth
put(T["naskah2"] - 0.25, "pop", -11, 0.9); put(T["suara2"], "sparkle", -11); put(T["gaya"], "pop", -10, 0.8); put(T["jualan"] + 0.05, "sparkle", -12, 1.2)
# ---- step 4: render machine (inputs, hum, ding, phone, upload)
for k in ("adegan2", "foto2", "suara3"): put(T[k] - 0.25, "tick", -13); put(T[k] + 0.42, "pop", -10, 0.85)
put(T["dirender"] + 0.4, "hum", -12)
for k in range(9): put(T["dirender"] + k * 0.085, "key", -16, 1.4)
put(T["dirender"] + 0.78, "ding", -9)
put(T["video2"] - 0.35, "riser_s", -11); put(T["video2"] - 0.1, "pop", -9, 0.7)
put(T["siap"], "send", -10)
for k in ("juga", "dibikin", "pakai"): put(T[k] + (0.2 if k == "dibikin" else 0.1 if k == "pakai" else 0), "tick", -12)
# ---- check board
put(T["alat"] + 0.05, "click", -10, 0.8); put(T["jaminan"] + 0.05, "click", -10, 0.5)
for k in ("klaim", "sebelum", "posting"): put(T[k] + 0.05, "tick", -11)
# ---- CTA
for k in range(5): put(T["promo"] - 0.05 + k * 0.07, "key", -13)
put(T["kirim2"], "send", -9); put(T["kirim2"] + 0.25, "recv", -9); put(T["kirim2"] + 0.45, "pop", -11, 0.9)
# ---- caption-in: a soft tick 70 ms before each caption chunk (chunking = tools/main_script.js)
a = 0; chunks = []
for i, (w, s, e) in enumerate(WORDS):
    if w[-1:] in ",.:?" or i - a == 3 or i == len(WORDS) - 1: chunks.append(a); a = i + 1
for c in chunks: put(WORDS[c][1] + OFF - 0.07, "tick", -16)
out = np.clip(out, -1, 1)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
json.dump(LOG, open("production/sfx_events.json", "w"))
print("VO peak", round(20 * np.log10(VO_PEAK), 1), "dBFS; sfx.wav peak", round(20 * np.log10(np.abs(out).max() + 1e-9), 1), "dBFS;", len(LOG), "events")

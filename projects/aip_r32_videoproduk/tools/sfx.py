"""SFX for R32 (assets/audio/sfx.wav, 48 kHz mono, 55.6 s) from the repo's vo_safe set (copied to assets/sfx).
Event times come from the VO word timings (production/words.json + 0.3 s offset), the same lookups the scenes use.
Mix rules (batch 8): one fixed, lower SFX level (no sidechain in the remix), and no SFX transient on a word onset:
each sample is placed by its measured PEAK, and a peak that would land within 45 ms of a word onset is nudged off it."""
import json, wave
import numpy as np
SR, DUR, OFF = 48000, 55.6, 0.3
WORDS = json.load(open("production/words.json"))
ONSETS = np.array([s + OFF for _, s, _ in WORDS])
def W(txt, after=0.0):
    for w, s, e in WORDS:
        if w == txt and s + OFF >= after: return s + OFF
    raise KeyError(txt)
out = np.zeros(int(SR * DUR))
def load(n):
    w = wave.open(f"assets/sfx/{n}.wav"); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
    return a.reshape(-1, w.getnchannels()).mean(axis=1)
S = {n: load(n) for n in ["click", "key", "ping", "pop", "sparkle", "type", "whoosh"]}
LOG = []
def put(t, n, g=1.0, rate=1.0):
    x = S[n]
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    pk = int(np.argmax(np.abs(x))) / SR                      # place by the measured peak
    d = ONSETS - t; near = d[np.abs(d) < 0.045]
    if near.size: t = t + (near[0] - 0.05 if near[0] > 0 else near[0] + 0.05)   # nudge off the onset
    i = int((t - pk) * SR); i0 = max(0, i); j = min(len(out), i + len(x))
    if j > i0: out[i0:j] += g * x[i0 - i: j - i]
    LOG.append((round(t, 3), n))
T = dict(produk=W("produk,"), ai=W("AI"), bikinin=W("bikinin"), suara=W("suara"), ini=W("Ini"), umkm=W("UMKM,"), online=W("online"), sampai=W("sampai"),
         satu=W("Satu."), terang=W("terang:"), depan=W("depan,"), samping=W("samping,"), detail=W("detail"), dua=W("Dua."), kirim=W("Kirim"), asisten=W("asisten"),
         nulis=W("nulis"), susunan=W("susunan"), adegan=W("adegan,"), detik=W("detik"), detik2=W("detik."), harga=W("harga,"), ukuran=W("ukuran,"), siapa=W("siapa"),
         hook=W("Hook"), manfaat=W("manfaat"), satu1=W("satu", 20), persatu=W("satu,", 20), ajakan=W("ajakan"), keranjang=W("keranjang"), tiga=W("Tiga."),
         naskah2=W("Naskah"), suara2=W("suara", 30), gaya=W("gaya"), jualan=W("jualan."), empat=W("Empat."), adegan2=W("Adegan,"), foto2=W("foto,", 30), suara3=W("suara", 36),
         dirender=W("dirender"), video2=W("video", 36), siap=W("siap"), video3=W("Video"), juga=W("juga", 40), dibikin=W("dibikin"), pakai=W("pakai"),
         tapi=W("Tapi"), alat=W("alat"), jaminan=W("jaminan"), klaim=W("klaim"), sebelum=W("sebelum"), posting=W("posting."), komen=W("Komen"), promo=W("promo,"), kirim2=W("kirim", 50))
G = 0.55   # one fixed SFX level (scaled in the remix too)
# hook
put(T["produk"], "click", 0.30 * G, 0.7)                          # shutter
put(T["ai"] - 0.02, "pop", 0.30 * G, 0.8)                         # AI cube
put(T["bikinin"] + 0.05, "whoosh", 0.22 * G, 1.1)                 # cube unfolds into the screen
put(T["suara"] + 0.12, "sparkle", 0.18 * G)                       # speaker rings
put(5.75, "whoosh", 0.28 * G, 0.6)                                # zoom-out reveal
for i in range(4): put(T["ini"] - 0.1 + i * 0.28, "key", 0.10 * G, 0.9)   # path lights the four islands
for k in ("umkm", "online", "sampai"): put(T[k] - 0.05, "pop", 0.22 * G, 0.9)
put(10.55, "whoosh", 0.26 * G, 0.8)                               # island-hop flight
put(T["terang"], "click", 0.22 * G, 0.6)                          # lights on
for k in ("depan", "samping", "detail"): put(T[k], "click", 0.28 * G, 0.7); put(T[k] + 0.5, "pop", 0.12 * G, 1.2)
put(T["dua"] - 0.22, "whoosh", 0.26 * G, 1.2)                     # dive into the photo
TY0, TY1 = T["dua"] + 0.12, T["kirim"] + 0.45
for k in range(int((TY1 - TY0) / 0.075)): put(TY0 + k * 0.075, "key", 0.05 * G, 1.1)
put(T["asisten"] + 0.02, "click", 0.26 * G, 0.9)                  # send
put(T["nulis"] - 0.05, "ping", 0.14 * G)
for k in ("susunan", "adegan", "detik", "detik2"): put(T[k] - 0.02, "pop", 0.10 * G, 1.2)
for k in ("harga", "ukuran", "siapa"): put(T[k] - 0.02, "pop", 0.16 * G, 1.0)
put(T["hook"] - 0.3, "whoosh", 0.24 * G, 0.9)                     # elevator doors
for k in ("hook", "manfaat", "satu1", "persatu", "ajakan"): put(T[k] + (0 if k != "hook" else -0.1), "click", 0.22 * G, 0.6)
for k in range(6): put(T["keranjang"] - 0.35 + k * 0.07, "key", 0.05 * G, 0.8)
put(T["keranjang"] + 0.15, "ping", 0.14 * G, 1.1)
put(T["tiga"] - 0.18, "whoosh", 0.30 * G, 1.3)                    # whip tilt
put(T["suara2"], "sparkle", 0.16 * G)
put(T["gaya"], "pop", 0.18 * G, 0.8)
put(T["jualan"] + 0.05, "sparkle", 0.12 * G, 1.2)
put(T["jualan"] + 0.45, "whoosh", 0.26 * G, 0.6)                  # 180° orbit
for k in ("adegan2", "foto2", "suara3"): put(T[k] + 0.42, "pop", 0.18 * G, 0.85)
for k in range(9): put(T["dirender"] + k * 0.085, "type", 0.05 * G, 1.4)
put(T["dirender"] + 0.78, "ping", 0.16 * G, 1.1)
put(T["video2"] - 0.1, "pop", 0.22 * G, 0.7)
put(T["siap"], "sparkle", 0.14 * G)
put(T["video3"] + 0.1, "whoosh", 0.18 * G, 0.5)                   # dolly zoom
for k in ("juga", "dibikin", "pakai"): put(T[k] + (0.2 if k == "dibikin" else 0.1 if k == "pakai" else 0), "pop", 0.12 * G, 1.1)
put(T["tapi"] - 0.4, "whoosh", 0.24 * G, 0.9)                     # iris
for k in ("alat", "jaminan", "klaim", "sebelum", "posting"): put(T[k] + 0.05, "click", 0.18 * G, 0.8)
put(T["komen"] - 0.22, "pop", 0.26 * G, 0.5); put(T["komen"] - 0.2, "whoosh", 0.18 * G, 0.8)   # shockwave
for k in range(5): put(T["promo"] - 0.05 + k * 0.07, "key", 0.10 * G)
put(T["kirim2"], "click", 0.22 * G); put(T["kirim2"] + 0.25, "ping", 0.18 * G)
out = np.clip(out, -1, 1)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
json.dump(LOG, open("production/sfx_events.json", "w"))
print("sfx peak", round(float(np.abs(out).max()), 3), len(LOG), "events")

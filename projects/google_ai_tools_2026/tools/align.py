"""VO word timing without network ASR (Hugging Face is blocked in this environment).
Speech segments (energy > -40 dB, gaps >= 90 ms) of the ORIGINAL VO are mapped to the LOCKED SCRIPT by hand
(SCENES below; every block reads at a plausible 5-8 syllables/s). Inside a block, word boundaries = syllable-weighted
split; a boundary snaps to a real gap (segment gap or a >= 50 ms dip below -55 dB) within 0.3 s, else to the
quietest 10 ms frame within 80 ms. Numbers are weighted by their spoken Indonesian form.
Outputs production/timing.json (words, scenes with global start/duration, caption chunks).
Run: python3 -I tools/align.py ."""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
VO = P / "assets/audio/ElevenLabs_2026-11-04T06_02_17_Dakocan - Expressive, Cheerful and Clear_pvc_sp100_s40_sb50_v4.mp3"
FPS = 30
# scene id, text (verbatim), segment range, caption chunks (split before word index), key words
SCENES = [
    ("s01", "Google punya lima AI tools viral.", [0, 0], [], ["lima"]),
    ("s02", "Tapi dua sedang dipensiunkan.", [1, 1], [], ["dua", "dipensiunkan."]),
    ("s03", "Yang masih layak kamu coba sekarang ada tiga.", [2, 3], [], ["tiga."]),
    ("s04", "Pertama, Pomelli.", [4, 5], [], ["Pomelli."]),
    ("s05", "Tempel website bisnismu, dia bisa membaca identitas brand kamu.", [6, 7], [3], ["website", "identitas", "brand"]),
    ("s06", "Lalu membantu bikin materi promosi dengan tampilan yang konsisten.", [8, 8], [5], ["konsisten."]),
    ("s07", "Kedua, Stitch.", [9, 10], [], ["Stitch."]),
    ("s08", "Tulis ide aplikasi, desain layarnya langsung disusun.", [11, 12], [3], ["disusun."]),
    ("s09", "Bahkan bisa dijadikan prototipe yang bisa diklik.", [13, 13], [], ["prototipe", "diklik."]),
    ("s10", "Ketiga, Antigravity.", [15, 16], [], ["Antigravity."]),
    ("s11", "AI agent bisa bantu coding lewat editor, terminal, sampai browser.", [18, 19], [5], ["editor,", "terminal,", "browser."]),
    ("s12", "Nah, ini bagian yang sering orang lewatkan.", [20, 22], [], ["lewatkan."]),
    ("s13", "Mixboard sudah ditutup sejak 28 September 2026.", [23, 23], [3], ["Mixboard", "ditutup", "28", "September", "2026."]),
    ("s14", "Opal juga dijadwalkan berhenti tanggal 17 November 2026.", [24, 24], [4], ["Opal", "dijadwalkan", "17", "November", "2026."]),
    ("s15", "Jadi, jangan asal simpan daftar AI yang sudah lama.", [25, 25], [4], ["jangan"]),
    ("s16", "Mau link tiga tools yang masih aktif, plus contoh promptnya?", [26, 28], [7], ["link", "contoh", "promptnya?"]),
    ("s17", "Komen GOOGLE.", [29, 29], [], ["GOOGLE."]),
]
PRON = {"google": "gugel", "ai": "eiai", "tools": "tuls", "website": "websait", "brand": "brend", "pomelli": "pomeli",
        "stitch": "stic", "antigravity": "entigraviti", "agent": "eijen", "coding": "koding", "browser": "brauser",
        "mixboard": "miksbord", "link": "link", "plus": "plas", "promptnya": "promnya",
        "28": "duapuluhdelapan", "17": "tujuhbelas", "2026": "duaribuduapuluhenam"}

raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(VO), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
a = np.frombuffer(raw, dtype=np.int16).astype(float) / 32768
hop = 160; n = len(a) // hop; DUR = len(a) / 16000
db = 20 * np.log10(np.sqrt(np.mean(a[: n * hop].reshape(n, hop) ** 2, axis=1)) + 1e-6)
sp = db > -40; segs = []; i = 0
while i < n:
    if sp[i]:
        j = i
        while j < n and (sp[j] or any(sp[j:j + 9])): j += 1
        segs.append((i / 100, j / 100)); i = j
    else: i += 1
assert len(segs) == 30, len(segs)
dips = []; i = 0
while i < n:
    if db[i] < -55:
        j = i
        while j < n and db[j] < -55: j += 1
        if j - i >= 5: dips.append((i + j) / 200)
        i = j
    else: i += 1

def spoken(w):
    k = re.sub(r"[^a-z0-9]", "", w.lower())
    s = PRON.get(k, k)
    return "".join(ch for ch in s if "a" <= ch <= "z")
syl = lambda s: max(1, len(re.findall(r"[aiueo]+", s)))

words, scenes = [], []
for sid, txt, (sa, sb), cuts, keys in SCENES:
    s0, e0 = segs[sa][0], segs[sb][1]
    ws = txt.split(); sps = [spoken(w) for w in ws]
    wt = np.array([syl(s) + 0.4 + (0.6 if re.search(r"[,.:?]$", w) else 0) for s, w in zip(sps, ws)])
    cum = np.concatenate([[0], np.cumsum(wt)]) / wt.sum()
    b = [s0 + c * (e0 - s0) for c in cum]
    gaps = [(segs[k][1] + segs[k + 1][0]) / 2 for k in range(sa, sb)] + [d for d in dips if s0 < d < e0]
    used = set()
    for k in range(1, len(b) - 1):
        lo = b[k - 1] + max(0.15, 0.075 * syl(sps[k - 1]))   # a word cannot be faster than ~13 syllables/s (min 150 ms)
        cand = [g for g in gaps if abs(g - b[k]) < 0.3 and g not in used and g > lo and (re.search(r"[,.:?]$", ws[k - 1]) or abs(g - b[k]) < 0.12)]
        if cand:
            g = min(cand, key=lambda g: abs(g - b[k])); used.add(g); b[k] = g
        else:
            f0 = int(max(b[k] - 0.08, lo) * 100); f1 = max(f0 + 2, int((b[k] + 0.08) * 100)); b[k] = (f0 + int(np.argmin(db[f0:f1 + 1]))) / 100
    for k in range(1, len(b)): b[k] = max(b[k], b[k - 1] + 0.06)
    first = len(words)
    for k, w in enumerate(ws):
        words.append({"w": w, "s": round(b[k], 3), "e": round(b[k + 1] - 0.01, 3), "key": w in keys, "scene": sid})
    scenes.append({"id": sid, "text": txt, "w0": first, "w1": len(words) - 1, "speech": [s0, e0], "cuts": [first + c for c in cuts]})

TOTAL = int(np.ceil(DUR * FPS)) / FPS
for k, sc in enumerate(scenes):
    st = 0.0 if k == 0 else round(round(((scenes[k - 1]["speech"][1] + sc["speech"][0]) / 2) * FPS) / FPS, 4)
    sc["start"] = st
for k, sc in enumerate(scenes):
    en = scenes[k + 1]["start"] if k + 1 < len(scenes) else TOTAL
    sc["dur"] = round(en - sc["start"], 4)
    sc["local"] = {w["w"]: round(w["s"] - sc["start"], 3) for w in words[sc["w0"]:sc["w1"] + 1]}
caps = []
for sc in scenes:
    bounds = [sc["w0"]] + sc["cuts"] + [sc["w1"] + 1]
    for c in range(len(bounds) - 1):
        a0, a1 = bounds[c], bounds[c + 1] - 1
        cs = sc["start"] if c == 0 else round(words[a0]["s"] - 0.12, 3)
        ce = sc["start"] + sc["dur"] if c == len(bounds) - 2 else round(words[bounds[c + 1]]["s"] - 0.12, 3)
        caps.append([round(cs, 3), round(ce, 3), a0, a1, [i for i in range(a0, a1 + 1) if words[i]["key"]]])
out = {"vo_sec": round(DUR, 5), "total_sec": round(TOTAL, 4), "frames": int(round(TOTAL * FPS)), "segments": segs, "words": words, "scenes": scenes, "caps": caps}
(P / "production/timing.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print("VO", round(DUR, 5), "total", round(TOTAL, 4), "frames", out["frames"])
for sc in scenes:
    print(f"{sc['id']} {sc['start']:6.2f} +{sc['dur']:5.2f}  speech {sc['speech'][0]:6.2f}-{sc['speech'][1]:6.2f}  {sc['text']}")
    print("      " + "  ".join(f"{w['w']}@{w['s']:.2f}" for w in words[sc['w0']:sc['w1'] + 1]))

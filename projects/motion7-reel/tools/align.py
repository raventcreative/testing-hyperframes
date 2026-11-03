"""VO timing without network ASR (Hugging Face is blocked here).
Speech segments (energy > -40 dB, gaps >= 90 ms) are mapped to script blocks by hand (MAP, checked against
syllable rates: every block reads at 6.4-7.5 syllables/s). Inside a block, word boundaries = syllable-weighted
split; a boundary snaps to a real gap (segment gap or a >= 50 ms dip below -55 dB) within 0.3 s, else to the
quietest 10 ms frame within 80 ms. Phones = letters spread over their word.
Outputs: production/word_timing.json, vendor/vo_words.js (VO_WORDS, VO_PHONES, VO_ENV, VO_PHR)"""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
AUDIO = P / "assets/audio/vo_tight.wav"
ITEMS = [("Satu,", "3D page flythrough.", "Satu landing page dimiringin, terus kamera terbang nembus semuanya.", [5], [6], [7, 7]),
         ("Dua,", "product tour promo.", "Satu kata tebal per fitur, dipotong pas sama beat.", [8], [9], [10, 12]),
         ("Tiga,", "dashboard launch film.", "Prompt-nya ngetik sendiri, terus dashboard-nya kebangun.", [13], [14], [15, 16]),
         ("Empat,", "AI food finder.", "Ketik lagi pengen makan apa, aplikasinya mikir di depan mata.", [17], [18], [19, 20]),
         ("Lima,", "weekday countdown.", "Tujuh hari muter cepet, terus ngunci di Jumat.", [21], [22], [23, 24]),
         ("Enam,", "UGC creator promo.", "Wajah, HP, dan video reaksi, dalam satu swipe.", [25], [26], [27, 30]),
         ("Tujuh,", "claymation music video.", "Karakter clay di langit penuh emoji dan drone.", [31], [32], [33, 35])]
BLOCKS = [([("hook", "Video kayak gini dulu butuh satu tim editor.")], [0, 0]),
          ([("hook", "Sekarang, cukup satu prompt.")], [1, 2]),
          ([("hook", "Ini tujuh prompt motion terbaik minggu ini, dan nomor tujuh paling gila.")], [3, 4])]
for lab, name, desc, a, b, c in ITEMS:
    BLOCKS += [([("label", lab)], [a[0], a[0]]), ([("name", name)], [b[0], b[0]]), ([("desc", desc)], c)]
BLOCKS += [([("cta", "Komen MOTION,"), ("cta", "gue kirim ketujuh prompt plus videonya langsung ke DM lu.")], [36, 37])]
PRON = {"3d": "tridi", "page": "peij", "flythrough": "flaitru", "product": "prodak", "tour": "tur", "promo": "promo", "beat": "bit",
        "dashboard": "desbord", "dashboardnya": "desbordnya", "launch": "lonc", "film": "film", "promptnya": "promnya", "prompt": "promt",
        "ai": "eiai", "food": "fud", "finder": "fainder", "weekday": "wikdei", "countdown": "kaundaun", "ugc": "yujisi", "creator": "krieitor",
        "hp": "hape", "swipe": "swaip", "claymation": "kleimeisyen", "music": "myusik", "video": "video", "clay": "klei", "drone": "dron",
        "motion": "mosyen", "dm": "diem", "gue": "gue", "editor": "editor", "landing": "lending", "plus": "plas", "videonya": "videonya"}
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(AUDIO), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
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
assert len(segs) == 38, len(segs)
dips = []; i = 0
while i < n:
    if db[i] < -55:
        j = i
        while j < n and db[j] < -55: j += 1
        if j - i >= 5: dips.append((i + j) / 200)
        i = j
    else: i += 1
def spoken(w):
    k = re.sub(r"[^a-z0-9\-]", "", w.lower()).strip("-")
    s = PRON.get(k, PRON.get(k.replace("-", ""), k))
    return "".join(ch for ch in s if "a" <= ch <= "z")
syl = lambda s: max(1, len(re.findall(r"[aiueo]+", s)))
words, phones, phr = [], [], []
for subs, (sa, sb) in BLOCKS:
    s0, e0 = segs[sa][0], segs[sb][1]
    ws, owner = [], []
    for si, (kind, txt) in enumerate(subs):
        for w in txt.split(): ws.append(w); owner.append(si)
    sps = [spoken(w) for w in ws]
    wt = np.array([syl(s) + 0.4 + (0.6 if re.search(r"[,.:?]$", w) else 0) for s, w in zip(sps, ws)])
    cum = np.concatenate([[0], np.cumsum(wt)]) / wt.sum()
    b = [s0 + c * (e0 - s0) for c in cum]
    gaps = [(segs[k][1] + segs[k + 1][0]) / 2 for k in range(sa, sb)] + [d for d in dips if s0 < d < e0]
    used = set()
    for k in range(1, len(b) - 1):
        cand = [g for g in gaps if abs(g - b[k]) < 0.3 and g not in used and (re.search(r"[,.:?]$", ws[k - 1]) or abs(g - b[k]) < 0.12)]
        if cand:
            g = min(cand, key=lambda g: abs(g - b[k])); used.add(g); b[k] = g
        else:
            f0, f1 = int((b[k] - 0.08) * 100), int((b[k] + 0.08) * 100); b[k] = (f0 + int(np.argmin(db[f0:f1 + 1]))) / 100
    for k in range(1, len(b)): b[k] = max(b[k], b[k - 1] + 0.06)
    first = len(words)
    for k, w in enumerate(ws):
        st, en = round(b[k], 3), round(b[k + 1] - 0.01, 3)
        words.append([w, st, en, 1 if subs[owner[k]][0] in ("name", "label") or w.startswith("PLUGIN") else 0, sps[k]])
        L = len(sps[k]); stp = (en - st) / max(1, L)
        for c, ch in enumerate(sps[k]): phones.append([ch, round(st + c * stp, 3), round(st + (c + 1) * stp, 3), len(words) - 1])
    for si, (kind, txt) in enumerate(subs):
        idx = [first + k for k in range(len(ws)) if owner[k] == si]
        phr.append({"kind": kind, "text": txt, "start": words[idx[0]][1], "end": words[idx[-1]][2], "w0": idx[0], "w1": idx[-1]})
items = []
k = 3
for _ in ITEMS:
    items.append({"label": phr[k], "name": phr[k + 1], "desc": phr[k + 2]}); k += 3
out = {"dur": round(DUR, 3), "hook": phr[:3], "items": items, "cta": phr[-2:]}
env = np.clip((db + 60) / 60, 0, 1)
(P / "production/word_timing.json").write_text(json.dumps({"segments": segs, "phrases": phr, "words": words}, indent=1, ensure_ascii=False))
(P / "vendor/vo_words.js").write_text("// generated by tools/align.py\nwindow.VO_WORDS = " + json.dumps(words, ensure_ascii=False, separators=(",", ":")) +
    ";\nwindow.VO_PHONES = " + json.dumps(phones, separators=(",", ":")) + ";\nwindow.VO_ENV = " + json.dumps([int(round(v * 99)) for v in env], separators=(",", ":")) +
    ";\nwindow.VO_PHR = " + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n")
for p in phr: print(f"{p['kind']:6s} {p['start']:6.2f}-{p['end']:6.2f} {p['text']}")

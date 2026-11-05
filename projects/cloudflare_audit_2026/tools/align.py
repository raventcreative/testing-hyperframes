"""VO word timing without network ASR (Hugging Face is blocked in this environment).
Speech segments (energy > -40 dB, gaps >= 90 ms) of the ORIGINAL VO are mapped to the locked script by hand (SCENES;
every block reads at a plausible 5-8 syllables/s; sentence ends fall on the longer pauses). Inside a block, word
boundaries = syllable-weighted split, snapped to real gaps/dips (never faster than ~13 syl/s, min 150 ms per word).
Outputs production/timing.json (words with caption style, scenes, caption chunks) and vendor/vo_words.js
(VO_WORDS, VO_PHONES, VO_ENV for the mascot lip sync).  Run: python3 -I tools/align.py ."""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
VO = P / "assets/audio/vo.mp3"
FPS = 30
# id, verbatim text, segment range, chunk cuts (word index inside the scene where a new caption chunk starts),
# cyan keywords, marker keyword (white rectangle + cyan bold, apex only)
SCENES = [
    ("s01", "Website buatan AI kamu keren. Tapi aman belum?", [0, 2], [5], ["keren."], ["aman"]),
    ("s02", "Ini ada skill open-source dari Cloudflare yang menarik banget.", [3, 3], [5], ["open-source", "Cloudflare"], []),
    ("s03", "Namanya Security Audit Skill.", [4, 4], [], [], ["Security", "Audit", "Skill."]),
    ("s04", "Kamu pasang di coding agent, lalu arahkan ke project milikmu.", [5, 6], [5], ["coding", "agent,", "project"], []),
    ("s05", "Pertama, dia memetakan kode dan jalur akses aplikasi.", [7, 7], [5], ["memetakan", "jalur", "akses"], []),
    ("s06", "Setelah itu, beberapa agent berburu potensi celah dari sisi berbeda.", [8, 8], [2, 7], ["berburu", "potensi", "celah"], []),
    ("s07", "Tapi tunggu, ini bagian yang paling keren.", [9, 11], [], ["keren."], ["tunggu,"]),
    ("s08", "Kalau satu agent merasa menemukan masalah,", [12, 12], [], ["satu", "masalah,"], []),
    ("s09", "agent lain justru ditugaskan untuk membantah temuannya.", [13, 13], [4], ["agent", "lain"], ["membantah"]),
    ("s10", "Bukan asal kasih peringatan.", [14, 14], [], ["peringatan."], ["Bukan"]),
    ("s11", "Hasilnya dipisah: terkonfirmasi, masih perlu diperiksa, atau ditolak.", [15, 18], [2], ["terkonfirmasi,", "diperiksa,", "ditolak."], []),
    ("s12", "Lalu disusun jadi laporan yang bisa kamu cek satu per satu.", [20, 20], [4], ["laporan", "satu", "per", "satu."], []),
    ("s13", "Perlu diingat, ini alat bantu audit, bukan jaminan website aman.", [21, 23], [2, 6], ["alat", "bantu", "audit,"], ["bukan", "jaminan"]),
    ("s14", "Mau link resmi, cara pasang, dan contoh prompt-nya?", [24, 24], [5], ["link", "resmi,", "cara", "pasang,", "contoh", "prompt-nya?"], []),
    ("s15", "Komen AMAN. Aku kirim panduannya.", [25, 26], [2], ["panduannya."], ["AMAN."]),
]
LIGHT = {"di", "ke", "dan", "yang", "dari", "ini", "itu", "ada", "lalu", "atau", "untuk", "jadi", "dia", "kamu", "aku", "kalau",
         "tapi", "setelah", "lain", "justru", "per", "mau", "nya", "bisa", "juga", "sejak", "masih", "perlu", "asal", "kasih"}
PRON = {"website": "websait", "ai": "eiai", "skill": "skil", "open-source": "opensors", "cloudflare": "klaudfler",
        "security": "sikyuriti", "audit": "odit", "coding": "koding", "agent": "eijen", "project": "projek",
        "prompt-nya": "promnya", "aman": "aman", "komen": "komen"}

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
assert len(segs) == 27, len(segs)
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
    s = PRON.get(k, PRON.get(re.sub(r"[^a-z]", "", k), k))
    return "".join(ch for ch in s if "a" <= ch <= "z")
syl = lambda s: max(1, len(re.findall(r"[aiueo]+", s)))

words, scenes = [], []
for sid, txt, (sa, sb), cuts, cyan, marker in SCENES:
    s0, e0 = segs[sa][0], segs[sb][1]
    ws = txt.split(); sps = [spoken(w) for w in ws]
    wt = np.array([syl(s) + 0.4 + (0.6 if re.search(r"[,.:?]$", w) else 0) for s, w in zip(sps, ws)])
    cum = np.concatenate([[0], np.cumsum(wt)]) / wt.sum()
    b = [s0 + c * (e0 - s0) for c in cum]
    gaps = [(segs[k][1] + segs[k + 1][0]) / 2 for k in range(sa, sb)] + [d for d in dips if s0 < d < e0]
    used = set()
    for k in range(1, len(b) - 1):
        lo = b[k - 1] + max(0.15, 0.075 * syl(sps[k - 1]))
        end = re.search(r"[.?!:]$", ws[k - 1])   # sentence end: snap to the real sentence pause, even if it is farther away
        win = 0.6 if end else 0.3
        cand = [g for g in gaps if abs(g - b[k]) < win and g not in used and g > lo and (re.search(r"[,.:?]$", ws[k - 1]) or abs(g - b[k]) < 0.12)]
        if cand:
            if end:
                seg_gaps = [g for g in cand if any(abs(g - (segs[q][1] + segs[q + 1][0]) / 2) < 1e-6 for q in range(sa, sb))]
                g = max(seg_gaps or cand, key=lambda g: (g in seg_gaps, -abs(g - b[k])))
            else:
                g = min(cand, key=lambda g: abs(g - b[k]))
            used.add(g)
            nxt = [segs[q + 1][0] for q in range(sa, sb) if abs(g - (segs[q][1] + segs[q + 1][0]) / 2) < 1e-6]
            b[k] = nxt[0] - 0.02 if nxt else g   # a word after a real pause starts where the voice resumes
        else:
            f0 = int(max(b[k] - 0.08, lo) * 100); f1 = max(f0 + 2, int((b[k] + 0.08) * 100)); b[k] = (f0 + int(np.argmin(db[f0:f1 + 1]))) / 100
    for k in range(1, len(b)): b[k] = max(b[k], b[k - 1] + 0.06)
    first = len(words)
    for k, w in enumerate(ws):
        bare = re.sub(r"[^a-z\-]", "", w.lower())
        style = "m" if w in marker else "c" if w in cyan else "r" if bare in LIGHT else "b"
        words.append({"w": w, "s": round(b[k], 3), "e": round(b[k + 1] - 0.01, 3), "st": style, "sp": sps[k], "scene": sid})
    scenes.append({"id": sid, "text": txt, "w0": first, "w1": len(words) - 1, "speech": [s0, e0], "cuts": [first + c for c in cuts]})

TOTAL = int(np.ceil(DUR * FPS)) / FPS
for k, sc in enumerate(scenes):
    sc["start"] = 0.0 if k == 0 else round(round(((scenes[k - 1]["speech"][1] + sc["speech"][0]) / 2) * FPS) / FPS, 4)
for k, sc in enumerate(scenes):
    en = scenes[k + 1]["start"] if k + 1 < len(scenes) else TOTAL
    sc["dur"] = round(en - sc["start"], 4)
caps = []
for sc in scenes:
    bounds = [sc["w0"]] + sc["cuts"] + [sc["w1"] + 1]
    for c in range(len(bounds) - 1):
        a0, a1 = bounds[c], bounds[c + 1] - 1
        cs = sc["start"] if c == 0 else round(words[a0]["s"] - 0.12, 3)
        ce = sc["start"] + sc["dur"] if c == len(bounds) - 2 else round(words[bounds[c + 1]]["s"] - 0.12, 3)
        caps.append([round(cs, 3), round(ce, 3), a0, a1])
out = {"vo_sec": round(DUR, 5), "total_sec": round(TOTAL, 4), "frames": int(round(TOTAL * FPS)), "segments": segs, "words": words, "scenes": scenes, "caps": caps}
(P / "production/timing.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
# mascot lip-sync data (same format as the earlier reels)
VW = [[w["w"], w["s"], w["e"], 1 if w["st"] in "cm" else 0, w["sp"]] for w in words]
PH = []
for i, w in enumerate(words):
    L = len(w["sp"]); stp = (w["e"] - w["s"]) / max(1, L)
    for c, ch in enumerate(w["sp"]): PH.append([ch, round(w["s"] + c * stp, 3), round(w["s"] + (c + 1) * stp, 3), i])
env = np.clip((db + 60) / 60, 0, 1)
(P / "vendor").mkdir(exist_ok=True)
(P / "vendor/vo_words.js").write_text("// generated by tools/align.py\nwindow.VO_WORDS = " + json.dumps(VW, ensure_ascii=False, separators=(",", ":")) +
    ";\nwindow.VO_PHONES = " + json.dumps(PH, separators=(",", ":")) + ";\nwindow.VO_ENV = " + json.dumps([int(round(v * 99)) for v in env], separators=(",", ":")) +
    ";\nwindow.VO_SCENES = " + json.dumps([{k: s[k] for k in ("id", "start", "dur", "w0", "w1")} for s in scenes], separators=(",", ":")) + ";\n")
print("VO", round(DUR, 5), "total", round(TOTAL, 4), "frames", out["frames"])
for sc in scenes:
    print(f"{sc['id']} {sc['start']:6.2f} +{sc['dur']:5.2f}  {sc['text']}")
    print("      " + "  ".join(f"{w['w']}@{w['s']:.2f}[{w['st']}]" for w in words[sc['w0']:sc['w1'] + 1]))

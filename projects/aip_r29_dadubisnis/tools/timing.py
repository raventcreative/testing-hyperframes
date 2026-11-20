"""R29 · dadu bisnis — production/timing.json + vendor/vo_words.js from production/vo_words_raw.json (ElevenLabs character
alignment via tools/align_words.py). Word starts inside a silence snap to the voice onset (energy > -40 dB). VO starts at OFFSET.
Scenes = word-index starts (45 beats); scene cuts at the middle of the gap between two phrases (frame-rounded).
Caption chunks: per scene, break after , . : ? or when the chunk would pass 21 characters / 4 words.
Run: python3 -I tools/timing.py ."""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
OFFSET, FPS, TAIL = 9 / 30, 30, 1.6
R = json.loads((P / "production/vo_words_raw.json").read_text())
raw = [w for s in R["segments"] for w in s["words"]]
TFIX = {}
for _i, (_s, _e) in TFIX.items(): raw[_i]["s"], raw[_i]["e"] = _s, _e

# merges: first raw index -> (last raw index, caption text, spoken spelling for lip sync)
MERGE = {9: (13, "16,7%.", "enambelaskomatujuhpersen"), 20: (25, "83,8%.", "delapanpuluhtigakomadelapanpersen"),
         30: (31, "100%.", "seratuspersen"), 148: (152, "0,02%.", "nolkomanolduapersen")}
FIXI = {7: "6", 15: "10", 27: "100", 79: "3", 99: "6.", 101: "1.000", 141: "6.", 142: "5", 342: "6.", 398: "DADU,"}
PRON = {"dm": "diem", "ai": "ei", "ainya": "einya", "shiny": "syaini", "object": "obyek", "syndrome": "sindrom", "online": "onlain",
        "prompt": "prom", "1000": "seribu", "10": "sepuluh", "100": "seratus", "3": "tiga", "6": "enam", "5": "lima", "dadu": "dadu"}

def spoken(w):
    k = re.sub(r"[^a-z0-9]", "", w.lower())
    s = PRON.get(k, k)
    return "".join(ch for ch in s if "a" <= ch <= "z") or "a"

pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", str(P / "assets/audio/vo.mp3"), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                     capture_output=True, check=True).stdout
a = np.frombuffer(pcm, np.int16).astype(float) / 32768
hop = 160; n = len(a) // hop; DUR = len(a) / 16000
db = 20 * np.log10(np.sqrt(np.mean(a[: n * hop].reshape(n, hop) ** 2, axis=1)) + 1e-6)
sp = db > -40; segs = []; i = 0
while i < n:
    if sp[i]:
        j = i
        while j < n and (sp[j] or any(sp[j:j + 9])): j += 1
        if j - i >= 6: segs.append((i / 100, j / 100))
        i = j
    else: i += 1

def snap(s, e):
    nxt = [a0 for a0, a1 in segs if s < a0 < e]
    for a0, a1 in segs:
        if a0 <= s < a1:
            return nxt[0] if nxt and (a1 - s) < 0.4 * (e - s) else s
    return nxt[0] if nxt else s

words = []; i = 0; rawidx = []
while i < len(raw):
    w = raw[i]
    if i in MERGE:
        j, txt, spk = MERGE[i]; e = raw[j]["e"]; i2 = j + 1
    else:
        txt = FIXI.get(i, w["w"]); spk = spoken(txt); e = w["e"]; i2 = i + 1
    s = w["s"] if i in MERGE else snap(w["s"], e)
    words.append({"w": txt, "s": round(s + OFFSET, 3), "s0": round(w["s"] + OFFSET, 3), "e": round(e + OFFSET, 3), "sp": spk})
    rawidx.append(i)
    i = i2
for k, w in enumerate(words):
    if w["s"] - w["s0"] > 0.02:
        m = k
        while m + 1 < len(words) and words[m + 1]["s0"] - words[m]["e"] < 0.05: m += 1
        S, E, o = w["s"], words[m]["e"], w["s0"]
        for q in range(k + 1, m + 1):
            words[q]["s"] = max(words[q]["s"], round(S + (words[q]["s0"] - o) * (E - S) / max(1e-3, E - o), 3))
for k in range(len(words) - 1): words[k]["e"] = min(words[k]["e"], round(words[k + 1]["s"] - 0.01, 3))
for w in words: w.pop("s0")

# scene starts as RAW word indices (see production/NOTES.md for the beat list)
SC_RAW = [0, 14, 26, 32, 42, 51, 65, 71, 81, 90, 100, 108, 116, 127, 142, 153, 157, 165, 170, 175, 184, 194, 197, 204, 214, 220,
          229, 237, 241, 253, 260, 268, 280, 288, 292, 307, 312, 318, 329, 339, 343, 363, 370, 384, 397]
KEY = {"6", "6.", "16,7%.", "83,8%.", "100%.", "0,02%.", "10", "100", "1.000", "5", "dadu", "dadunya", "nampan", "nampannya", "pasar.", "pasar",
       "pasar,", "ide", "idenya", "kegedean,", "kekecilan.", "salah.", "sempit,", "lantai.", "terbatas.", "acak,", "kunci", "variabelnya.",
       "pelajaran,", "naik.", "tepat,", "tumbuh.", "meleset", "shiny", "object", "syndrome.", "kinclong,", "nol", "kebalikannya.", "diteliti", "lemparan.", "banyak-banyakan",
       "produknya,", "penawarannya,", "harganya,", "jualannya.", "AI", "ulasan", "keluhan", "versi", "bukan", "tepat.", "lemparanmu,",
       "DADU,", "DM.", "sekaligus.", "sekaligus?", "lolos", "mental", "keluarga,", "3", "lembar", "kerja", "berulang,", "perintah"}
w2s = {r: k for k, r in enumerate(rawidx)}
starts = [w2s[r] for r in SC_RAW]
scenes = []
for q, w0 in enumerate(starts):
    w1 = (starts[q + 1] - 1) if q + 1 < len(starts) else len(words) - 1
    for wi in range(w0, w1 + 1): words[wi]["st"] = "k" if words[wi]["w"] in KEY else "b"; words[wi]["scene"] = q
    scenes.append({"id": f"s{q + 1:02d}", "text": " ".join(w["w"] for w in words[w0:w1 + 1]), "w0": w0, "w1": w1,
                   "speech": [words[w0]["s"], words[w1]["e"]]})
TOTAL = round(int(np.ceil((DUR + OFFSET + TAIL - 0.3) * FPS)) / FPS, 4)
for q, sc in enumerate(scenes):
    sc["start"] = 0.0 if q == 0 else round(round(((scenes[q - 1]["speech"][1] + sc["speech"][0]) / 2) * FPS) / FPS, 4)
for q, sc in enumerate(scenes):
    en = scenes[q + 1]["start"] if q + 1 < len(scenes) else TOTAL
    sc["dur"] = round(en - sc["start"], 4)
# caption chunks
caps = []
for sc in scenes:
    a0 = sc["w0"]; cur = []
    for wi in range(sc["w0"], sc["w1"] + 1):
        txt = " ".join(words[x]["w"] for x in cur + [wi])
        if cur and (len(txt) > 23 or len(cur) >= 4):
            caps.append(cur); cur = []
        cur.append(wi)
        if re.search(r"[,.:?]$", words[wi]["w"]) and wi < sc["w1"]:
            caps.append(cur); cur = []
    if cur: caps.append(cur)
CAPS = []
for k, c in enumerate(caps):
    s = max(0.05, round(words[c[0]]["s"] - 0.12, 3))
    nx = caps[k + 1] if k + 1 < len(caps) else None
    e = round(words[nx[0]]["s"] - 0.14, 3) if nx else round(TOTAL - 0.05, 3)
    e = min(e, round(words[c[-1]]["e"] + 1.0, 3)) if nx else e
    CAPS.append([s, e, c[0], c[-1]])
out = {"vo_offset": round(OFFSET, 4), "vo_sec": round(DUR, 5), "total_sec": TOTAL, "frames": int(round(TOTAL * FPS)),
       "segments": [[round(x + OFFSET, 2), round(y + OFFSET, 2)] for x, y in segs], "words": words, "scenes": scenes, "caps": CAPS}
(P / "production/timing.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
VW = [[w["w"], w["s"], w["e"], 1 if w["st"] == "k" else 0, w["sp"]] for w in words]
PH = []
for i, w in enumerate(words):
    L = len(w["sp"]); stp = (w["e"] - w["s"]) / max(1, L)
    for c, ch in enumerate(w["sp"]): PH.append([ch, round(w["s"] + c * stp, 3), round(w["s"] + (c + 1) * stp, 3), i])
env = np.clip((db + 60) / 60, 0, 1)
env = np.concatenate([np.zeros(int(round(OFFSET * 100))), env])
(P / "vendor/vo_words.js").write_text("// generated by tools/timing.py (times include the VO offset)\nwindow.TOTAL = " + json.dumps(TOTAL) +
    ";\nwindow.VO_WORDS = " + json.dumps(VW, ensure_ascii=False, separators=(",", ":")) + ";\nwindow.VO_PHONES = " + json.dumps(PH, separators=(",", ":")) +
    ";\nwindow.VO_ENV = " + json.dumps([int(round(v * 99)) for v in env], separators=(",", ":")) +
    ";\nwindow.VO_SCENES = " + json.dumps([{k: s[k] for k in ("id", "start", "dur", "w0", "w1")} for s in scenes], separators=(",", ":")) +
    ";\nwindow.VO_CAPS = " + json.dumps(CAPS, separators=(",", ":")) + ";\n")
print("VO", round(DUR, 3), "offset", OFFSET, "total", TOTAL, "frames", out["frames"], "caps", len(CAPS))
for sc in scenes:
    print(f"{sc['id']} {sc['start']:7.2f} +{sc['dur']:5.2f}  {sc['text']}")
for c in CAPS: print(f"  cap {c[0]:7.2f}-{c[1]:7.2f}  " + " ".join(words[x]["w"] for x in range(c[2], c[3] + 1)))

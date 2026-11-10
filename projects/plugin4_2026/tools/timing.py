"""Builds production/timing.json + vendor/vo_words.js for the PLUGIN4 reel (4 Claude Code plugins remake) from the faster-whisper word timestamps.
- display fixes (Higgsfield, Wan 2.2, ElevenLabs, GPT-SoVITS, Midjourney, ComfyUI, FLUX, ChatGPT, Ollama, ...)
- word starts that whisper put inside a silence are snapped to the real voice onset (energy > -40 dB)
- VO starts at OFFSET s (9 frames).   Run: python3 -I tools/timing.py ."""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
OFFSET, FPS, TAIL = 9 / 30, 30, 1.3
R = json.loads((P / "production/vo_words_raw.json").read_text())
raw = [w for s in R["segments"] for w in s["words"]]

# merges: (first index, last index, display text, spoken spelling for lip sync)
MERGE = {4: (5, "Claude Code,", "klodkod"), 40: (41, "CLAUDE.md", "klodemdi"), 61: (62, "basa-basi.", "basabasi")}
FIX = {"Cloud": "Claude", "Carpathi": "Karpathy", "sesimple": "sesimpel", "Comment": "Komen", "setup,": "SETUP,"}
FIXI = {}
PRON = {"claude": "klod", "superpowers": "superpawers", "github": "githab", "karpathy": "karpati", "skills": "skils", "caveman": "kefmen",
        "codex": "kodeks", "openai": "openei", "plugin": "plagin", "token": "token", "dm": "diem", "setup": "setap", "vibe": "faib", "coding": "koding"}

def spoken(w):
    k = re.sub(r"[^a-z0-9]", "", w.lower())
    s = PRON.get(k, k)
    return "".join(ch for ch in s if "a" <= ch <= "z") or "a"

# voice segments from energy
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
    """move a start that whisper placed in a silence (or that is mostly unvoiced) to the next voice onset"""
    nxt = [a0 for a0, a1 in segs if s < a0 < e]
    for a0, a1 in segs:
        if a0 <= s < a1:
            return nxt[0] if nxt and (a1 - s) < 0.4 * (e - s) else s
    return nxt[0] if nxt else s

words = []; i = 0
while i < len(raw):
    w = raw[i]
    if i in MERGE:
        j, txt, spk = MERGE[i]; e = raw[j]["e"]; i2 = j + 1
    else:
        txt = FIXI.get(i, FIX.get(w["w"], w["w"])); spk = spoken(txt); e = w["e"]; i2 = i + 1
    s = snap(w["s"], e)
    words.append({"w": txt, "s": round(s + OFFSET, 3), "s0": round(w["s"] + OFFSET, 3), "e": round(e + OFFSET, 3), "sp": spk})
    i = i2
# a snapped start compresses the rest of its phrase: re-spread the phrase between the new onset and the phrase end
for k, w in enumerate(words):
    if w["s"] - w["s0"] > 0.02:
        m = k
        while m + 1 < len(words) and words[m + 1]["s0"] - words[m]["e"] < 0.05: m += 1
        S, E, o = w["s"], words[m]["e"], w["s0"]
        for q in range(k + 1, m + 1):
            words[q]["s"] = max(words[q]["s"], round(S + (words[q]["s0"] - o) * (E - S) / max(1e-3, E - o), 3))
for k in range(len(words) - 1): words[k]["e"] = min(words[k]["e"], round(words[k + 1]["s"] - 0.01, 3))
for w in words: w.pop("s0")

# scenes: id, first word text (sequential match), caption chunk cuts (word offsets), cyan words, marker words
SC = [
    ("s01", "Sebelum", [3, 5], ["Claude Code,", "empat"], []),
    ("r1", "Satu,", [2, 6, 9, 13, 18], ["Superpowers.", "300", "ribu"], ["Satu,"]),
    ("r2", "Dua,", [3, 7, 10, 15, 17], ["Karpathy", "Skills.", "CLAUDE.md", "empat"], ["Dua,"]),
    ("r3", "Tiga,", [2, 5, 7, 13], ["Caveman.", "63", "20."], ["Tiga,"]),
    ("r4", "Empat,", [3, 6, 9, 11, 15], ["Codex,", "OpenAI."], ["Empat,"]),
    ("s06", "Mau", [5], ["DM."], ["SETUP,"]),
]
LIGHT = {"di", "ke", "dan", "yang", "ini", "itu", "aku", "sama", "kayak", "lewat", "jadi", "biar", "dalam", "ada", "dari", "lalu",
         "atau", "baru", "sampai", "lagi", "isinya", "cuma"}
starts = []; k = 0
for sid, first, *_ in SC:
    while words[k]["w"] != first: k += 1
    starts.append(k); k += 1
scenes = []
for q, (sid, first, cuts, cyan, marker) in enumerate(SC):
    w0 = starts[q]; w1 = (starts[q + 1] - 1) if q + 1 < len(SC) else len(words) - 1
    for wi in range(w0, w1 + 1):
        t = words[wi]["w"]; bare = re.sub(r"[^a-z]", "", t.lower())
        words[wi]["st"] = "m" if t in marker else "c" if t in cyan else "r" if bare in LIGHT or t.lower() in LIGHT else "b"
        words[wi]["scene"] = sid
    scenes.append({"id": sid, "text": " ".join(w["w"] for w in words[w0:w1 + 1]), "w0": w0, "w1": w1,
                   "speech": [words[w0]["s"], words[w1]["e"]], "cuts": [w0 + c for c in cuts]})
TOTAL = round(int(np.ceil((DUR + OFFSET + TAIL - 0.3) * FPS)) / FPS, 4)
for q, sc in enumerate(scenes):
    sc["start"] = 0.0 if q == 0 else round(round(((scenes[q - 1]["speech"][1] + sc["speech"][0]) / 2) * FPS) / FPS, 4)
for q, sc in enumerate(scenes):
    en = scenes[q + 1]["start"] if q + 1 < len(scenes) else TOTAL
    sc["dur"] = round(en - sc["start"], 4)
caps = []
for sc in scenes:
    bounds = [sc["w0"]] + sc["cuts"] + [sc["w1"] + 1]
    for c in range(len(bounds) - 1):
        a0, a1 = bounds[c], bounds[c + 1] - 1
        cs = (max(0.05, round(words[a0]["s"] - 0.25, 3)) if sc["id"] == "s01" else sc["start"]) if c == 0 else round(words[a0]["s"] - 0.1, 3)
        ce = sc["start"] + sc["dur"] if c == len(bounds) - 2 else round(words[bounds[c + 1]]["s"] - 0.1, 3)
        caps.append([round(cs, 3), round(ce, 3), a0, a1])
out = {"vo_offset": round(OFFSET, 4), "vo_sec": round(DUR, 5), "total_sec": TOTAL, "frames": int(round(TOTAL * FPS)),
       "segments": [[round(x + OFFSET, 2), round(y + OFFSET, 2)] for x, y in segs], "words": words, "scenes": scenes, "caps": caps}
(P / "production/timing.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
VW = [[w["w"], w["s"], w["e"], 1 if w["st"] in "cm" else 0, w["sp"]] for w in words]
PH = []
for i, w in enumerate(words):
    L = len(w["sp"]); stp = (w["e"] - w["s"]) / max(1, L)
    for c, ch in enumerate(w["sp"]): PH.append([ch, round(w["s"] + c * stp, 3), round(w["s"] + (c + 1) * stp, 3), i])
env = np.clip((db + 60) / 60, 0, 1)
pad = int(round(OFFSET * 100))
env = np.concatenate([np.zeros(pad), env])
(P / "vendor/vo_words.js").write_text("// generated by tools/timing.py (times include the VO offset)\nwindow.VO_WORDS = " +
    json.dumps(VW, ensure_ascii=False, separators=(",", ":")) + ";\nwindow.VO_PHONES = " + json.dumps(PH, separators=(",", ":")) +
    ";\nwindow.VO_ENV = " + json.dumps([int(round(v * 99)) for v in env], separators=(",", ":")) +
    ";\nwindow.VO_SCENES = " + json.dumps([{k: s[k] for k in ("id", "start", "dur", "w0", "w1")} for s in scenes], separators=(",", ":")) + ";\n")
print("VO", round(DUR, 3), "offset", OFFSET, "total", TOTAL, "frames", out["frames"])
for sc in scenes:
    print(f"{sc['id']} {sc['start']:6.2f} +{sc['dur']:5.2f}  {sc['text']}")
    print("      " + "  ".join(f"{w['w']}@{w['s']:.2f}[{w['st']}]" for w in words[sc['w0']:sc['w1'] + 1]))

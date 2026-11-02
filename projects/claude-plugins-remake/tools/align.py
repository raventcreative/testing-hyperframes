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
PL = json.loads((P / "production/plugins.json").read_text())
CAT = {"c1": ("Satu,", "biar ngoding kayak senior dev:"), "c2": ("Dua,", "riset dan memahami apa pun:"),
       "c3": ("Tiga,", "project gede, token hemat:"), "c4": ("Empat,", "desain dan visual:"), "c5": ("Lima,", "nulis dan bikin video:")}
NAMES = {c: [p["name"] for p in PL if p["cat"] == c] for c in CAT}
# block -> list of (kind, text) sub-phrases, segment range [a, b]
BLOCKS = [([("hook", "Jangan install plugin Claude asal comot.")], [0, 0]),
          ([("hook", "Ini 30 plugin terbaik di GitHub,")], [1, 1]),
          ([("hook", "udah gue kelompokin sesuai kerjaannya.")], [2, 2])]
def cat_blocks(c, lab, desc, names):
    out = [([("label", CAT[c][0])], lab), ([("desc", CAT[c][1])], desc)]
    if names[1] - names[0] == 5:
        out += [([("name", n)], [names[0] + k, names[0] + k]) for k, n in enumerate(NAMES[c])]
    else:
        out += [([("name", n) for n in NAMES[c]], names)]
    return out
BLOCKS += cat_blocks("c1", [3, 3], [4, 4], [5, 10])
BLOCKS += cat_blocks("c2", [11, 11], [12, 12], [13, 18])
BLOCKS += cat_blocks("c3", [19, 19], [20, 21], [22, 25])
BLOCKS += [([("label", CAT["c4"][0]), ("desc", CAT["c4"][1])] + [("name", n) for n in NAMES["c4"]], [27, 34])]
BLOCKS += cat_blocks("c5", [35, 35], [36, 36], [37, 42])
BLOCKS += [([("outro", "Tapi jangan install semuanya.")], [43, 43]),
           ([("outro", "Pilih satu baris yang paling lu butuhin,"), ("outro", "dan buka repo-nya dulu sebelum install.")], [44, 44]),
           ([("cta", "Komen PLUGIN,"), ("cta", "gue kirim 30 link-nya langsung ke DM lu.")], [45, 45])]
PRON = {"30": "tigapuluh", "github": "githab", "claude": "klod", "install": "instol", "plugin": "plagin", "senior": "sinior", "dev": "dep",
        "superpowers": "superpawers", "matt": "met", "pocock": "pokok", "skills": "skils", "ecc": "isisi", "karpathy": "karpati", "ponytail": "poniteil",
        "agent": "eijen", "graphify": "grafifai", "reach": "ric", "understand": "anderstend", "anything": "enitin", "last": "last", "days": "deis",
        "career": "karir", "ops": "ops", "rea": "erie", "gstack": "jistek", "caveman": "keivmen", "claudemem": "klodmem", "headroom": "hedrum",
        "gsd": "jiesdi", "bmad": "bimed", "method": "metod", "ui": "yuai", "ux": "yueks", "pro": "pro", "max": "meks", "taste": "teist",
        "archify": "arkifai", "impeccable": "impekebel", "ppt": "pipiti", "master": "master", "diagram": "daiagrem", "design": "disain",
        "by": "bai", "anthropic": "entropik", "openmontage": "openmontaj", "hyperframes": "haiperfreims", "humanizer": "humenaiser",
        "i": "ai", "have": "hev", "adhd": "eidieicdi", "marketing": "marketin", "repo": "ripo", "repo-nya": "riponya", "link-nya": "linknya", "plugin,": "plagin"}
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
assert len(segs) == 46, len(segs)
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
cats, k = [], 3
for c in CAT:
    lab, desc = phr[k], phr[k + 1]; names = phr[k + 2:k + 8]; k += 8
    cats.append({"id": c, "label": lab, "desc": desc, "names": names})
out = {"dur": round(DUR, 3), "hook": phr[:3], "cats": cats, "outro": phr[-4:-2], "outro0": phr[-5], "cta": phr[-2:]}
out["outro"] = [phr[-5], phr[-4], phr[-3]]
env = np.clip((db + 60) / 60, 0, 1)
(P / "production/word_timing.json").write_text(json.dumps({"segments": segs, "phrases": phr, "words": words}, indent=1, ensure_ascii=False))
(P / "vendor/vo_words.js").write_text("// generated by tools/align.py\nwindow.VO_WORDS = " + json.dumps(words, ensure_ascii=False, separators=(",", ":")) +
    ";\nwindow.VO_PHONES = " + json.dumps(phones, separators=(",", ":")) + ";\nwindow.VO_ENV = " + json.dumps([int(round(v * 99)) for v in env], separators=(",", ":")) +
    ";\nwindow.VO_PHR = " + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n")
for p in phr: print(f"{p['kind']:6s} {p['start']:6.2f}-{p['end']:6.2f} {p['text']}")

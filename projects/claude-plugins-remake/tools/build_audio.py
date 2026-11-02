"""Writes the <audio> tags between <!--AUDIO--> markers in index.html: VO + SFX on measured VO times."""
import json, re, sys
from pathlib import Path
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
WT = json.loads((P / "production/word_timing.json").read_text()); ph, words = WT["phrases"], WT["words"]
DUR = {"whoosh": 0.574, "key": 0.4, "type": 1.5, "pop": 0.72, "click": 0.365, "sparkle": 1.8, "ping": 1.32}
def wt(p, txt):
    for k in range(p["w0"], p["w1"] + 1):
        if re.sub(r"[.,?:]", "", words[k][0]) == txt: return words[k][1]
    raise KeyError(txt)
S = [("whoosh", 0.0, 0.08)]
H = [p for p in ph if p["kind"] == "hook"]; O = [p for p in ph if p["kind"] == "outro"]; CT = [p for p in ph if p["kind"] == "cta"]
S += [("pop", 0.25, 0.05), ("pop", 0.7, 0.05), ("pop", 1.1, 0.05), ("whoosh", wt(H[1], "30") - 0.12, 0.1), ("sparkle", wt(H[1], "GitHub"), 0.07), ("pop", wt(H[2], "kelompokin"), 0.08)]
labels = [p for p in ph if p["kind"] == "label"]
for i, l in enumerate(labels): S.append(("whoosh", l["start"] - 0.3, 0.1))
for p in ph:
    if p["kind"] == "name": S.append(("click", p["start"] - 0.08, 0.06))
S += [("whoosh", O[0]["start"] - 0.32, 0.1), ("pop", wt(O[0], "semuanya") + 0.2, 0.08), ("key", wt(O[1], "baris") + 0.05, 0.06), ("key", wt(O[1], "baris") + 0.33, 0.06),
      ("key", wt(O[1], "baris") + 0.61, 0.06), ("click", O[2]["start"] + 0.42, 0.1), ("whoosh", O[2]["start"] + 0.48, 0.07), ("click", O[2]["start"] + 1.2, 0.08),
      ("whoosh", CT[0]["start"] - 0.3, 0.09), ("pop", wt(CT[0], "PLUGIN") - 0.04, 0.1), ("type", wt(CT[0], "PLUGIN"), 0.04), ("click", CT[1]["start"] - 0.05, 0.08),
      ("ping", wt(CT[1], "kirim"), 0.1), ("sparkle", wt(CT[1], "DM"), 0.08)]
tags = ['      <audio id="vo" class="clip" src="assets/audio/vo_tight.wav" data-start="0" data-duration="47.75" data-track-index="8" data-volume="1"></audio>']
lanes = []
for k, (n, t, v) in enumerate(sorted(S, key=lambda x: x[1])):
    t = max(0.0, round(t, 3)); d = min(DUR[n], 48.4 - t)
    li = next((j for j, e in enumerate(lanes) if e <= t), None)
    if li is None: lanes.append(0); li = len(lanes) - 1
    lanes[li] = t + d + 0.01
    tags.append(f'      <audio id="sfx{k:02d}" class="clip" src="assets/sfx/vo_safe/{n}.wav" data-start="{t}" data-duration="{d:.3f}" data-track-index="{10 + li}" data-volume="{v}"></audio>')
f = P / "index.html"; s = f.read_text()
s = re.sub(r"<!--AUDIO-->.*?<!--/AUDIO-->", "<!--AUDIO-->\n" + "\n".join(tags) + "\n      <!--/AUDIO-->", s, flags=re.S)
f.write_text(s); print(len(tags), "audio tags,", len(lanes), "lanes")

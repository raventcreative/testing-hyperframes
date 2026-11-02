"""Writes the <audio> tags between <!--AUDIO--> markers in index.html: VO + SFX placed on measured VO times.
Run: python3 -I tools/build_audio.py <project>"""
import json, re, sys
from pathlib import Path
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
WT = json.loads((P / "production/word_timing.json").read_text())
ph, codes, words = WT["phrases"], WT["codes"], WT["words"]
DUR = {"whoosh": 0.574, "key": 0.4, "type": 1.5, "pop": 0.72, "click": 0.365, "sparkle": 1.8, "ping": 1.32}
def wt(p, txt):
    for k in range(p["w0"], p["w1"] + 1):
        if re.sub(r"[.,?]", "", words[k][0]) == txt: return words[k][1]
    raise KeyError(txt)
S = []
H, CT = ph[:4], ph[-2:]
S += [("whoosh", 0.0, 0.10), ("pop", H[1]["start"], 0.12), ("whoosh", H[1]["start"] + 0.02, 0.10)]
S += [("type", wt(H[1], "lima") - 0.05, 0.05), ("pop", wt(H[1], "kode") - 0.05, 0.10)]
S += [("whoosh", H[3]["start"] - 0.25, 0.08), ("sparkle", wt(H[3], "visual") - 0.05, 0.10), ("whoosh", codes[0]["name"] - 0.6, 0.09)]
for i, c in enumerate(codes):
    S.append(("key", c["name"] - 0.14, 0.07))
    S.append(("click", c["nameEnd"] - 0.04, 0.07))
    S.append(("pop" if i % 2 else "whoosh", c["nameEnd"], 0.06))
    if (i + 1) % 5 == 0: S.append(("sparkle", c["nameEnd"] + 0.05, 0.06))
S += [("whoosh", CT[0]["start"] - 0.35, 0.10), ("pop", wt(CT[0], "PROMPT") - 0.04, 0.12), ("type", wt(CT[0], "PROMPT"), 0.04),
      ("click", CT[1]["start"] - 0.05, 0.09), ("ping", wt(CT[1], "kirim"), 0.10), ("sparkle", wt(CT[1], "DM"), 0.09)]
tags = ['      <audio id="vo" class="clip" src="assets/audio/vo_tight.wav" data-start="0" data-duration="43.95" data-track-index="8" data-volume="1"></audio>']
for k, (n, t, v) in enumerate(sorted(S, key=lambda x: x[1])):
    t = max(0.0, round(t, 3)); d = min(DUR[n], 44.6 - t)
    tags.append(f'      <audio id="sfx{k:02d}" class="clip" src="assets/sfx/vo_safe/{n}.wav" data-start="{t}" data-duration="{d:.3f}" data-track-index="{10 + k % 6}" data-volume="{v}"></audio>')
f = P / "index.html"; s = f.read_text()
s = re.sub(r"<!--AUDIO-->.*?<!--/AUDIO-->", "<!--AUDIO-->\n" + "\n".join(tags) + "\n      <!--/AUDIO-->", s, flags=re.S)
f.write_text(s); print(len(tags), "audio tags")

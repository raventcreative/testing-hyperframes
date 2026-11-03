"""Fill the media markers in index.html from production/word_timing.json:
BGMEDIA (blurred example per item), FRAMEMEDIA (hook montage + example per item in the frame), AUDIO (VO + SFX).
Run: python3 -I tools/build_media.py <project>"""
import json, re, sys
from pathlib import Path
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
WT = json.loads((P / "production/word_timing.json").read_text()); ph, words = WT["phrases"], WT["words"]
H = [p for p in ph if p["kind"] == "hook"]; L = [p for p in ph if p["kind"] == "label"]; N = [p for p in ph if p["kind"] == "name"]
DS = [p for p in ph if p["kind"] == "desc"]; CT = [p for p in ph if p["kind"] == "cta"]
D = 41.2
CLIPS = ["assets/clips/ex01_aipreneur.mp4"] + [f"assets/clips/ex0{n}.mp4" for n in range(2, 8)]
WIN = [(L[k]["start"] - 0.2, (L[k + 1]["start"] - 0.2) if k < 6 else CT[0]["start"] - 0.25) for k in range(7)]
r = lambda x: round(x, 3)
bg, fr = [], []
for k, (a, b) in enumerate(WIN):
    d = r(b - a + (0.05 if k < 6 else 0.3))
    bg.append(f'      <video id="bg-ex{k+1}" class="clip bvid" src="{CLIPS[k]}" data-start="{r(a)}" data-duration="{d}" data-track-index="1" muted playsinline></video>')
    fr.append(f'            <video id="frame-ex{k+1}" class="clip fvid" src="{CLIPS[k]}" data-start="{r(a)}" data-duration="{d}" data-track-index="4" muted playsinline></video>')
for k in range(7):
    a = 0.08 + k * 0.28; ms = 1.2 if k == 0 else 2.5
    fr.append(f'            <video id="montage-{k+1}" class="clip mont" src="{CLIPS[k]}" data-start="{r(a)}" data-duration="0.28" data-media-start="{ms}" data-track-index="5" muted playsinline></video>')
bg.append(f'      <video id="bg-hook" class="clip bvid" src="{CLIPS[6]}" data-start="0" data-duration="{r(H[1]["start"])}" data-media-start="1" data-track-index="2" muted playsinline></video>')
def wt(p, txt, n=1):
    c = 0
    for k in range(p["w0"], p["w1"] + 1):
        if re.sub(r"[.,?:]", "", words[k][0]).lower() == txt.lower():
            c += 1
            if c == n: return words[k][1]
    raise KeyError(txt)
DUR = {"whoosh": 0.574, "key": 0.4, "type": 1.5, "pop": 0.72, "click": 0.365, "sparkle": 1.8, "ping": 1.32}
S = [("whoosh", 0.0, 0.08)] + [("key", 0.08 + k * 0.28, 0.035) for k in range(7)]
S += [("type", H[1]["start"] + 0.1, 0.05), ("click", H[1]["end"] - 0.2, 0.08), ("pop", wt(H[2], "tujuh"), 0.09), ("sparkle", wt(H[2], "paling"), 0.08)]
for k, (a, b) in enumerate(WIN):
    S += [("whoosh", a - 0.05, 0.09), ("pop", L[k]["start"] - 0.05, 0.07)]
S += [("whoosh", WIN[6][1] - 0.1, 0.09), ("pop", wt(CT[0], "motion") - 0.05, 0.11), ("type", wt(CT[0], "motion"), 0.04),
      ("click", CT[1]["start"] - 0.05, 0.08), ("ping", wt(CT[1], "kirim"), 0.1), ("sparkle", wt(CT[1], "dm"), 0.07)]
tags = ['      <audio id="vo" class="clip" src="assets/audio/vo_tight.wav" data-start="0" data-duration="40.71" data-track-index="8" data-volume="1"></audio>']
lanes = []
for k, (n, t, v) in enumerate(sorted(S, key=lambda x: x[1])):
    t = max(0.0, r(t)); d = min(DUR[n], D - t)
    li = next((j for j, e in enumerate(lanes) if e <= t), None)
    if li is None: lanes.append(0); li = len(lanes) - 1
    lanes[li] = t + d + 0.01
    tags.append(f'      <audio id="sfx{k:02d}" class="clip" src="assets/sfx/vo_safe/{n}.wav" data-start="{t}" data-duration="{d:.3f}" data-track-index="{10 + li}" data-volume="{v}"></audio>')
f = P / "index.html"; s = f.read_text()
for mk, body in (("BGMEDIA", bg), ("FRAMEMEDIA", fr), ("AUDIO", tags)):
    s = re.sub(rf"<!--{mk}-->.*?<!--/{mk}-->", f"<!--{mk}-->\n" + "\n".join(body) + f"\n      <!--/{mk}-->", s, flags=re.S)
f.write_text(s); print(len(bg), "bg,", len(fr), "frame,", len(tags), "audio; windows", [(r(a), r(b)) for a, b in WIN])

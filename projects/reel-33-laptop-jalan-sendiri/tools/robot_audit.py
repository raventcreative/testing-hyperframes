"""Replay the robot's pose track against the scheduled gestures and prove the hands alternate.

Mirrors brand/fx/reel_fx.js exactly:
  - go(pose, at, dur) registers the new pose at at + dur/2; enter(pose, at) at at
  - side(t) = poseAt(t).x > 300 ? "R" : "L"
  - point: the arm used is the one AWAY from the robot's side (R -> left arm, L -> right arm)
  - wave:  the arm on the robot's own side
  - runGestures skips any gesture that starts before the previous one has finished

Run: python3 -I tools/robot_audit.py
"""
import json, re, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
src = (P / "production/index.src.txt").read_text()
js = src.split("const FX = REEL_FX")[1]
T = json.loads((P / "production/word_timing.json").read_text())
W, PH = T["words"], T["phrases"]
ph = lambda s: next(p for p in PH if p["text"].startswith(s))


def wt(s, w):
    k = PH.index(ph(s))
    return next((x[1] for x in W if x[3] == k and x[0].lower().startswith(w.lower())), ph(s)["start"])


env = {"D": 59.6}
for m in re.finditer(r'(\bt[A-Za-z0-9]*) = ph\("([^"]+)"\)\.start', src):
    env[m.group(1)] = ph(m.group(2))["start"]
for m in re.finditer(r'(\bt[A-Za-z0-9]*) = wt\("([^"]+)", "([^"]+)"\)', src):
    env[m.group(1)] = wt(m.group(2), m.group(3))
for _ in range(3):
    for m in re.finditer(r"const (t[A-Za-z0-9]*) = (t[A-Za-z0-9]*) ([-+]) ([\d.]+);", src):
        if m.group(2) in env:
            env[m.group(1)] = env[m.group(2)] + (1 if m.group(3) == "+" else -1) * float(m.group(4))
ev = lambda e: eval(e.strip(), {"__builtins__": {}}, env)

POSE = {"home": 0, "center": 222, "right": 440, "up": 222, "upL": -110, "upR": 500, "peekL": -110, "peekR": 530}
track, gest = [(0.0, 0, "home")], []
for m in re.finditer(r"FX\.(enter|go|dip|point|wave|beat)\(([^;]*?)\);", js):
    k, a = m.group(1), [x.strip() for x in m.group(2).split(",")]
    if k in ("enter", "go", "dip"):
        d = ev(a[2]) if len(a) > 2 else 0.7
        at = ev(a[1])
        track.append((at if k == "enter" else at + d * 0.5, POSE[a[0].strip('"')], a[0].strip('"')))
    else:
        gest.append((ev(a[0]), k))
track.sort(key=lambda z: z[0])


def poseAt(t):
    p = track[0][1]
    for z in track:
        if z[0] <= t:
            p = z[1]
    return p


DUR = {"point": 1.7, "wave": 1.9, "beat": 0.7}
gest.sort()
busy, n, seq, skipped = -1, 0, [], 0
for t, k in gest:
    if t < busy + 0.05:
        print(f"{t:6.2f}  {k:6} SKIPPED (overlaps the previous gesture)")
        skipped += 1
        continue
    busy = t + DUR[k]
    R = poseAt(t + 0.2) > 300
    if k == "point":
        arm = "LEFT" if R else "RIGHT"
    elif k == "wave":
        arm = "RIGHT" if R else "LEFT"
    else:
        arm = "LEFT" if n % 2 else "RIGHT"
        n += 1
    print(f"{t:6.2f}  {k:6} robot on {'R' if R else 'L'}  ->  {arm} arm")
    seq.append(arm)

alt = all(seq[i] != seq[i + 1] for i in range(len(seq) - 1))
rises = [(round(z[0], 2), z[2]) for z in track if z[2] in ("upL", "upR", "up")]
print()
print("pose moves        :", len(track) - 1)
print("side rises        :", rises)
print("gestures played   :", len(seq), "| skipped:", skipped)
print("hands alternate   :", alt)
sys.exit(0 if (alt and not skipped and len(rises) >= 2) else 1)

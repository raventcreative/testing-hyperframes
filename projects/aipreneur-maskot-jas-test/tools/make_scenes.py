#!/usr/bin/env python3
"""production/scenes.json — 17 silent effect demos, SEG seconds each, one per PDF effect (cut later into 17 MP4s)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
SEG = 6.0
FX = ["orbit_maskot_jas"]
sc = [{"id": f"s{k + 1:02d}", "fx": k + 1, "label": n, "start": round(k * SEG, 4), "end": round((k + 1) * SEG, 4), "dur": SEG} for k, n in enumerate(FX)]
D = round(len(FX) * SEG, 4)
(P / "production/scenes.json").write_text(json.dumps({"fps": 30, "duration": D, "seg": SEG, "scenes": sc}, indent=1))
# no recorded voice: a demo "talk" track so the mouth shows speech shapes in two windows (seeded, deterministic)
import random
rng = random.Random(7)
TALK = [(0.55, 1.95), (2.7, 4.2)]
phones, env = [], [0] * (int(D * 100) + 4)
for a, b in TALK:
    t = a
    while t < b - 0.1:
        v = rng.choice("aeiou")
        d = rng.choice([0.1, 0.12, 0.14, 0.16])
        c = rng.choice("mbtsnkpd")
        phones.append([c, round(t, 3), round(t + 0.04, 3), 0]); phones.append([v, round(t + 0.04, 3), round(t + d, 3), 0])
        t += d + (0.06 if rng.random() < 0.25 else 0)
    for k in range(int(a * 100), int(b * 100)):
        env[k] = 70 + int(12 * rng.random())
(P / "vendor/vo_words.js").write_text("// demo talk track (no voice-over)\nwindow.VO_WORDS = [];\n"
                                      f"window.VO_PHONES = {json.dumps(phones)};\nwindow.VO_ENV = {json.dumps(env)};\n")
print("scenes", len(sc), "D", D)

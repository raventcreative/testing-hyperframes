#!/usr/bin/env python3
"""production/sfx_plan.json — subtle SFX under the voice (NO music).
Sources: production/sfx/sNN.json (S.fx cues written by every scene build).
  1. VO-safe files (tools/sfx_prep.py -> assets/sfx/vo_safe/, high-passed away from the voice).
  2. Peak on the visual apex: each cue starts so the sound's measured peak lands on its apex.
  3. Ducked by the real VO level (x0.5 above -22 dB, x0.7 above -32 dB).
  4. Typing ticks merge into one trimmed typing clip.  5. Density: max 2 non-typing cues per 0.45 s.
Library: HyperFrames bundled SFX (Pixabay Content License, assets/sfx/CREDITS.md)."""
import json, subprocess
from pathlib import Path
import numpy as np
P = Path(__file__).resolve().parents[1]
NAMES = ["click", "key", "type", "pop", "sparkle", "whoosh", "ping"]
DEFAULT_VOL = {"type": 0.04}

def pcm(path, sr=16000):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(float) / 32768
info = {}
for n in NAMES:
    a = np.abs(pcm(P / f"assets/sfx/vo_safe/{n}.wav"))
    env = np.convolve(a, np.ones(160) / 160, mode="same")
    info[n] = (round(float(np.argmax(env)) / 16000, 4), round(len(a) / 16000, 3))
vo = pcm(P / "assets/audio/vo_20effects_elevenlabs.mp3")
hop = 160
vdb = 20 * np.log10(np.sqrt(np.mean(vo[: len(vo) // hop * hop].reshape(-1, hop) ** 2, axis=1)) + 1e-6)
def vo_level(t0, t1):
    a, b = max(0, int(t0 * 100)), max(int(t0 * 100) + 1, int(t1 * 100))
    seg = vdb[a:b]
    return float(np.percentile(seg, 75)) if len(seg) else -90.0
D = json.loads((P / "production/scenes.json").read_text())["duration"]
cues = []
for f in sorted((P / "production/sfx").glob("s*.json")):
    for c in json.loads(f.read_text()):
        t, name = float(c[0]), c[1]
        if name not in NAMES:
            continue
        vol = float(c[2]) if len(c) > 2 and c[2] is not None else DEFAULT_VOL.get(name, 0.07)
        cues.append((f.stem, t, name, vol))
cues.sort(key=lambda x: x[1])
merged, span = [], None
for c in cues:
    if c[2] == "type":
        if span and c[1] - span[2] < 0.6:
            span[2] = c[1]
        else:
            if span:
                merged.append((span[0], span[1], "type", span[3], span[2] - span[1] + 0.45))
            span = [c[0], c[1], c[1], c[3]]
        continue
    merged.append((c[0], c[1], c[2], c[3], None))
if span:
    merged.append((span[0], span[1], "type", span[3], span[2] - span[1] + 0.45))
merged.sort(key=lambda x: x[1])
out = []
for (src, apex, name, vol, span_d) in merged:
    pk, full = info[name]
    if name == "type":
        t, d = apex, min(full, span_d)
    else:
        t, d = max(0.0, apex - pk), min(full, 1.2)
    if t >= D - 0.05:
        continue
    lvl = vo_level(t, t + min(d, 0.3))
    duck = 0.5 if lvl > -22 else 0.7 if lvl > -32 else 1.0
    out.append({"src": src, "cue": name, "apex": round(apex, 3), "t": round(t, 3), "file": f"vo_safe/{name}.wav",
                "dur": round(d, 3), "vol": round(min(vol, 0.12) * duck, 3), "vo_db": round(lvl, 1), "duck": duck})
final = []
for c in out:
    near = [x for x in final if x["cue"] != "type" and abs(x["apex"] - c["apex"]) < 0.45]
    if c["cue"] != "type" and len(near) >= 2:
        weakest = min(near + [c], key=lambda x: x["vol"])
        if weakest is c:
            continue
        final.remove(weakest)
    if any(x["cue"] == c["cue"] and abs(x["apex"] - c["apex"]) < 0.25 for x in final):
        continue
    final.append(c)
(P / "production/sfx_plan.json").write_text(json.dumps(final, indent=1))
d = sum(1 for c in final if c["duck"] < 1)
print(f"{len(final)} cues ({d} ducked under speech, {len(final) - d} in pauses)")

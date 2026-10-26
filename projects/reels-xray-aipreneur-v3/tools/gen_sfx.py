"""production/sfx_plan.json from the SFX lists in tools/scenes/sNN.py + director camera punches.
Each cue is placed so the sound's measured peak lands on its apex. Subtle, purposeful only (no music).
Files: Pixabay-licensed library SFX (assets/sfx/CREDITS.md)."""
import importlib.util, json, subprocess, sys
from pathlib import Path
import numpy as np
P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / "tools"))
FILES = {"click": "click-soft.mp3", "key": "key-press.mp3", "pop": "pop.mp3", "sparkle": "sparkle.mp3", "whoosh": "whoosh-short.mp3"}
info = {}
for k, f in FILES.items():
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(P / "assets/sfx" / f), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
    a = np.abs(np.frombuffer(raw, dtype=np.int16).astype(float))
    env = np.convolve(a, np.ones(160) / 160, mode="same")
    info[k] = (round(float(np.argmax(env)) / 16000, 4), round(min(len(a) / 16000, 1.4), 3))
cues = []
for p in sorted((P / "tools/scenes").glob("s[0-9][0-9].py")):
    spec = importlib.util.spec_from_file_location(p.stem, p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for (t, name, vol) in getattr(m, "SFX", [])[:3]:
        cues.append((p.stem, float(t), name, float(vol)))
for c in json.loads((P / "production/director_camera.json").read_text()):
    if c["fx"] == "snapZoom":
        cues.append(("director", c["opts"]["at"] + 0.02, "click", 0.06))
out, last = [], {}
for (src, apex, name, vol) in sorted(cues, key=lambda x: x[1]):
    if apex - last.get(name, -9) < 0.25:   # same sound twice within 250 ms -> keep one
        continue
    last[name] = apex
    pk, dur = info[name]
    t = round(max(0.0, apex - pk), 3)
    out.append({"src": src, "cue": name, "apex": round(apex, 3), "t": t, "file": FILES[name], "dur": dur, "vol": round(min(vol, 0.16), 3)})
(P / "production/sfx_plan.json").write_text(json.dumps(out, indent=1))
print(len(out), "sfx cues;", {k: v for k, v in info.items()})

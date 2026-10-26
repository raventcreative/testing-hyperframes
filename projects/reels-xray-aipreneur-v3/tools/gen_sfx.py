"""production/sfx_plan.json — subtle, purposeful SFX that never fight the voice.

Sources: the SFX lists in tools/scenes/sNN.py (module SFX, or filled inside build()) + director snap zooms.
Rules (user: "efek suara dikit-dikit … gak tabrakan sama suara orangnya"):
  1. VO-safe files: every sound is a high-passed variant (tools/sfx_prep.py -> assets/sfx/vo_safe/).
  2. Peak on the visual apex: the cue starts so the sound's measured peak lands on the apex.
  3. Ducking by the real VO: the VO level around each cue is measured; cues on loud speech are lowered
     (x0.5 above -22 dB, x0.7 above -32 dB), cues in pauses keep their level.
  4. Typing: per-character 'type' events are merged into one typing clip trimmed to the typing span.
  5. Density: at most 2 non-typing cues inside any 0.45 s window (the quieter one is dropped).
"""
import importlib.util, json, subprocess, sys
from pathlib import Path
import numpy as np
P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / "tools"))
import xk
NAMES = ["click", "key", "type", "pop", "sparkle", "whoosh", "ping"]
DEFAULT_VOL = {"type": 0.05}

def pcm(path, sr=16000):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(float) / 32768
info = {}
for n in NAMES:
    a = np.abs(pcm(P / f"assets/sfx/vo_safe/{n}.wav"))
    env = np.convolve(a, np.ones(160) / 160, mode="same")
    info[n] = (round(float(np.argmax(env)) / 16000, 4), round(len(a) / 16000, 3))
vo = pcm(P / "assets/audio/vo_xray_elevenlabs.mp3")
hop = 160
vdb = 20 * np.log10(np.sqrt(np.mean(vo[: len(vo) // hop * hop].reshape(-1, hop) ** 2, axis=1)) + 1e-6)
def vo_level(t0, t1):
    a, b = max(0, int(t0 * 100)), max(int(t0 * 100) + 1, int(t1 * 100))
    seg = vdb[a:b]
    return float(np.percentile(seg, 75)) if len(seg) else -90.0

cues = []
for p in sorted((P / "tools/scenes").glob("s[0-9][0-9].py")):
    spec = importlib.util.spec_from_file_location(p.stem, p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    if not getattr(m, "SFX", None) and hasattr(m, "build"):
        m.build(xk.Scene(p.stem))
    for c in getattr(m, "SFX", []):
        t, name = float(c[0]), c[1]
        vol = float(c[2]) if len(c) > 2 else DEFAULT_VOL.get(name, 0.08)
        cues.append((p.stem, t, name, vol))
for c in json.loads((P / "production/director_camera.json").read_text()):
    if c["fx"] == "snapZoom":
        cues.append(("director", c["opts"]["at"] + 0.02, "click", 0.06))

# 4. merge typing ticks into spans
cues.sort(key=lambda x: x[1])
merged, span = [], None
for c in cues:
    if c[2] == "type":
        if span and c[1] - span[2] < 0.14:
            span[2] = c[1]
        else:
            if span:
                merged.append(("typing", span[1], "type", span[3], span[2] - span[1] + 0.12))
            span = [c[0], c[1], c[1], c[3]]
        continue
    merged.append((c[0], c[1], c[2], c[3], None))
if span:
    merged.append(("typing", span[1], "type", span[3], span[2] - span[1] + 0.12))
merged.sort(key=lambda x: x[1])

out = []
for (src, apex, name, vol, span_d) in merged:
    pk, full = info[name]
    if name == "type":
        t, d = apex, min(full, span_d)
    else:
        t, d = max(0.0, apex - pk), min(full, 1.2)
    lvl = vo_level(t, t + min(d, 0.3))
    duck = 0.5 if lvl > -22 else 0.7 if lvl > -32 else 1.0
    out.append({"src": src, "cue": name, "apex": round(apex, 3), "t": round(t, 3), "file": f"vo_safe/{name}.wav",
                "dur": round(d, 3), "vol": round(min(vol, 0.14) * duck, 3), "vo_db": round(lvl, 1), "duck": duck})
# 5. density
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
print(f"{len(final)} cues ({d} ducked under speech, {len(final) - d} in pauses); typing spans: {sum(1 for c in final if c['cue'] == 'type')}")

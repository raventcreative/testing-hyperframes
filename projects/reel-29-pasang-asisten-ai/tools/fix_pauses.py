"""Cap the silent gaps in the ElevenLabs VO (client rule 2026-11-23: pauses between lines <= ~0.45 s — long gaps
sound dead). Reads assets/audio/vo.mp3 (TTS output, untouched), trims every inter-phrase silence down to MAXGAP and
writes assets/audio/vo.wav. Run: python3 -I tools/fix_pauses.py [project] [--dry]"""
import subprocess, sys, wave
from pathlib import Path
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else ".").resolve()
DRY = "--dry" in sys.argv
MAXGAP = 0.45          # seconds of silence allowed between phrases
KEEP_EDGE = 0.06       # keep a sliver of the natural decay either side of a trim
SR = 44100

raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(P / "assets/audio/vo.mp3"),
                      "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.int16).astype(np.float32)

win = int(0.02 * SR)
env = np.convolve(np.abs(x), np.ones(win) / win, mode="same")
thr = max(env.max() * 0.012, 60.0)
quiet = env < thr

# contiguous quiet runs
runs, i, n = [], 0, len(quiet)
while i < n:
    if quiet[i]:
        j = i
        while j < n and quiet[j]:
            j += 1
        runs.append((i, j))
        i = j
    else:
        i += 1

cuts = []
for a, b in runs:
    if a == 0 or b >= n:          # leading / trailing silence handled separately
        continue
    dur = (b - a) / SR
    if dur > MAXGAP:
        keep = int(MAXGAP * SR)
        drop_from = a + int(KEEP_EDGE * SR) + keep // 2
        drop_to = b - int(KEEP_EDGE * SR) - (keep - keep // 2)
        if drop_to > drop_from:
            cuts.append((drop_from, drop_to, dur))

print(f"raw {len(x)/SR:.2f}s, gaps > {MAXGAP}s: {len(cuts)}")
for a, b, dur in cuts:
    print(f"  gap {dur:.2f}s at {a/SR:7.2f}s -> trim {(b-a)/SR:.2f}s")

if DRY:
    sys.exit(0)

out, last = [], 0
for a, b, _ in cuts:
    out.append(x[last:a])
    last = b
out.append(x[last:])
y = np.concatenate(out)

# trim long head/tail silence to 0.12 s
lead = next((k for k in range(len(y)) if abs(y[k]) > thr), 0)
tail = next((k for k in range(len(y) - 1, -1, -1) if abs(y[k]) > thr), len(y) - 1)
pad = int(0.12 * SR)
y = y[max(0, lead - pad): min(len(y), tail + pad)]

y = y.astype(np.int16)
with wave.open(str(P / "assets/audio/vo.wav"), "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(y.tobytes())
print("vo.wav", round(len(y) / SR, 2), "s")

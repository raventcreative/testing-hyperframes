#!/usr/bin/env python3
"""Map Whisper large-v3 (id) words onto the locked canonical script and refine
word boundaries against the ElevenLabs waveform (silence gaps + energy valleys).
Usage: python3 -I tools/align_words.py <project_dir> <raw16k_s16le> <silences.txt>
Writes production/word_timing.json (single source of truth for captions + apex).
"""
import json, re, sys
from pathlib import Path
import numpy as np

P = Path(sys.argv[1]).resolve()
RAW, SIL = sys.argv[2], sys.argv[3]
machine = json.loads((P / "production/transcript_machine.json").read_text())
canon_txt = (P / "handoff/07_VO_ELEVENLABS_READY.txt").read_text()
canon = canon_txt.split()

# --- 1. explicit, reviewed mapping machine -> canonical (by position) -------
# machine idx 9  "perkataannya." -> canon "per" + "katanya."   (split, FLAGGED)
# machine idx 30 "Cloud"          -> canon "Claude"            (pronunciation, FLAGGED)
# machine idx 137/138 "pandu?" "Pertanyaannya," -> "panduan" "instalnya?" (re-pass confirmed)
# machine idx 140/141 "hype" "it." -> "HYPIT."                (merge, product name)
m = [dict(w) for w in machine]
out = []
i = 0
while i < len(m):
    w = m[i]
    if i == 9:
        out.append({"text": None, "start": w["start"], "end": None, "src": [i], "split": "a"})
        out.append({"text": None, "start": None, "end": w["end"], "src": [i], "split": "b"})
    elif i == 140:
        out.append({"text": None, "start": w["start"], "end": m[i + 1]["end"], "src": [i, i + 1]})
        i += 1
    else:
        out.append({"text": None, "start": w["start"], "end": w["end"], "src": [i]})
    i += 1
assert len(out) == len(canon), (len(out), len(canon))
for o, c in zip(out, canon):
    o["text"] = c

# --- 2. waveform refinement ------------------------------------------------
x = np.fromfile(RAW, dtype=np.int16).astype(float) / 32768
SR, HOP = 16000, 160  # 10 ms frames
n = len(x) // HOP
rms = np.sqrt((x[: n * HOP].reshape(n, HOP) ** 2).mean(1))
db = np.convolve(20 * np.log10(rms + 1e-6), np.ones(3) / 3, "same")
dur = len(x) / SR

sil = []
for line in Path(SIL).read_text().split("\n"):
    if line.strip():
        a, b = map(float, line.split())
        if sil and a - sil[-1][1] < 0.012:
            sil[-1][1] = b
        else:
            sil.append([a, b])


def valley(t, win=0.14):
    lo, hi = max(0, int((t - win) * 100)), min(n - 1, int((t + win) * 100))
    k = lo + int(np.argmin(db[lo:hi + 1]))
    return k / 100.0


# split word "per | katanya": find valley inside the machine span
w9 = out[9]
mid = valley(w9["start"] + 0.22, 0.12)
out[9]["end"] = mid
out[10]["start"] = mid

# Reviewed anchor table: canonical word index whose END sits at a measured
# silence (punctuation pause) -> (silence_start, silence_end). Built by matching
# every sentence/comma pause >=0.06 s to the script's punctuation, in order.
ANCHORS = {
    6: (2.428, 2.540), 10: (4.073, 4.297), 12: (5.361, 5.558), 20: (9.015, 9.331),
    32: (13.732, 13.886), 40: (16.668, 17.055), 48: (20.320, 20.645),
    49: (21.251, 21.334), 50: (21.973, 22.052), 53: (23.119, 23.424),
    57: (24.987, 25.254), 65: (27.746, 28.185), 70: (29.911, 30.292),
    73: (31.780, 31.954), 75: (32.834, 32.921), 76: (33.671, 33.835),
    81: (35.846, 36.025), 93: (40.515, 40.906), 99: (42.817, 42.946),
    102: (44.000, 44.108), 108: (46.698, 47.058), 110: (47.692, 47.996),
    116: (49.810, 49.898), 121: (51.661, 51.881), 124: (53.622, 53.695),
    133: (56.479, 56.898), 139: (58.544, 58.924), 141: (59.708, 60.066),
}
mach = [(o["start"], o["end"]) for o in out]
SYL_OVERRIDE = {"workflow": 2, "b-roll": 2, "github": 2, "claude": 1, "code": 1, "hypit": 2, "ai": 2,
                "skill": 1, "brief": 1, "source": 1, "open": 2, "footage": 2, "caption": 2, "repo": 2,
                "link": 1, "hook": 1, "framework-nya": 4, "stars": 1, "edit": 2, "presenter": 3}
def syl(t):
    import re as _re
    k = _re.sub(r"[^a-z\-]", "", t.lower())
    if k in SYL_OVERRIDE:
        return SYL_OVERRIDE[k]
    return max(1, len(_re.findall(r"[aeiou]+", k)))
seg_bounds = []  # (first_idx, last_idx, t0, t1)
first, t0 = 0, 0.04
for k in sorted(ANCHORS):
    seg_bounds.append((first, k, t0, ANCHORS[k][0]))
    first, t0 = k + 1, ANCHORS[k][1]
seg_bounds.append((first, len(out) - 1, t0, None))
last_sil = sil[-1]
method = ["valley"] * (len(out) - 1)
for k in ANCHORS:
    method[k] = "silence_anchor"
for a_i, b_i, t0, t1 in seg_bounds:
    if t1 is None:
        t1 = last_sil[0] if last_sil[1] >= dur - 0.02 else mach[b_i][1]
    # relative machine durations (min 0.08 s weight)
    idx = list(range(a_i, b_i + 1))
    ws = [syl(out[j]["text"]) for j in idx]
    tot = sum(ws)
    # evidence 1: syllable-proportional
    sb = [t0]
    for wv in ws:
        sb.append(sb[-1] + (t1 - t0) * wv / tot)
    # evidence 2: Whisper's own relative boundaries, linearly rescaled to [t0, t1]
    m0, m1 = mach[a_i][0], mach[b_i][1]
    wb = [t0] + [t0 + (t1 - t0) * ((mach[j][1] + mach[j + 1][0]) / 2 - m0) / max(1e-3, m1 - m0) for j in idx[:-1]] + [t1]
    bounds = [(x + y) / 2 for x, y in zip(sb, wb)]
    # snap only to a genuinely quiet frame (< -40 dB) within +-0.07 s
    for j in range(1, len(bounds) - 1):
        lo = max(bounds[j - 1] + 0.08, bounds[j] - 0.07)
        hi = min(bounds[j + 1] - 0.08, bounds[j] + 0.07)
        if hi > lo:
            v = valley((lo + hi) / 2, (hi - lo) / 2)
            if db[int(v * 100)] < -40:
                bounds[j] = v
    for n_, j in enumerate(range(a_i, b_i + 1)):
        out[j]["start"], out[j]["end"] = round(bounds[n_], 3), round(bounds[n_ + 1], 3)
# first onset / last offset from the waveform
first_sil_end = sil[0][1] if sil and sil[0][0] < 0.01 else 0.0


for k, o in enumerate(out):
    o["start"], o["end"] = round(o["start"], 3), round(o["end"], 3)
    o["id"] = f"w{k}"
    o["boundary_after"] = method[k] if k < len(method) else "file_tail_silence"
    o["machine"] = " ".join(m[j]["text"] for j in o["src"])
    del o["src"]
    o.pop("split", None)

# --- 3. flags ----------------------------------------------------------------
flags = {
    "w9": "Machine heard 'perkataannya' (2 Whisper passes). Canonical 'per katanya'. Needs Freddie's ear.",
    "w10": "Second half of canonical 'per katanya' (split from machine 'perkataannya').",
    "w30": "Machine heard 'Cloud' (id + en passes). Canonical 'Claude'. Likely TTS pronunciation; needs Freddie's ear.",
}
for o in out:
    if o["id"] in flags:
        o["flag"] = flags[o["id"]]

json.dump({"words": out}, open(P / "production/_words_tmp.json", "w"), indent=1, ensure_ascii=False)
print("aligned", len(out), "words; last end", out[-1]["end"], "dur", round(dur, 3))
for o in out:
    print(f'{o["id"]:>5} {o["start"]:7.3f} {o["end"]:7.3f}  {o["text"]:<16} ({o["machine"]}) {o["boundary_after"]}')

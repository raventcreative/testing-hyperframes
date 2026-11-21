"""Whisper listen-check: transcribe an audio/video file with faster-whisper and diff word by word against production/vo_lines.txt.
Usage: python3 tools/vo_check.py <audio|video> <model small|medium> [out.json]"""
import sys, json, re, subprocess, difflib
import numpy as np
from faster_whisper import WhisperModel
src, mname = sys.argv[1], sys.argv[2]
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
m = WhisperModel(mname, device="cpu", compute_type="int8", cpu_threads=4)
segs, info = m.transcribe(a, language="id", word_timestamps=True, beam_size=5, condition_on_previous_text=False, vad_filter=False)
words = []
for s in segs:
    for w in s.words or []: words.append([w.word.strip(), round(w.start, 2), round(w.end, 2), round(w.probability, 2)])
NUM = {"3": "tiga", "5": "lima", "100": "seratus", "10": "sepuluh", "30": "tiga puluh"}
def norm(t):
    t = t.lower().replace("-", " ")
    out = []
    for x in t.split():
        x = re.sub(r"[^a-z0-9]", "", x)
        if not x: continue
        out += NUM.get(x, x).split()
    return out
ref = norm(open("production/vo_lines.txt").read())
hyp, hyp_t = [], []
for w, s, e, p in words:
    for x in norm(w): hyp.append(x); hyp_t.append((s, p))
sm = difflib.SequenceMatcher(a=ref, b=hyp, autojunk=False)
print(f"model={mname} ref={len(ref)} hyp={len(hyp)} ratio={sm.ratio():.3f}")
nd = 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == "equal": continue
    nd += 1
    t = hyp_t[j1][0] if j1 < len(hyp_t) else -1
    print(f"  {op:7s} @{t:6.2f}s  ref: {' '.join(ref[i1:i2])!r:40s} heard: {' '.join(hyp[j1:j2])!r}")
print("diffs:", nd)
low = [w for w in words if w[3] < 0.5]
print("low-confidence words:", low)
if len(sys.argv) > 3: json.dump(words, open(sys.argv[3], "w"), ensure_ascii=False)

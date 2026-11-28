"""Whisper listen-check: transcribe <audio> with faster-whisper <model> (Indonesian) and diff word by word against
production/vo_lines.txt. Usage: python3 tools/vo_check.py <audio|mp4> <small|medium> [offset_s]"""
import json, re, subprocess, sys, difflib
import numpy as np
from faster_whisper import WhisperModel
audio, mname = sys.argv[1], sys.argv[2]
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
x = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
m = WhisperModel(mname, device="cpu", compute_type="int8", cpu_threads=4)
segs, _ = m.transcribe(x, language="id", word_timestamps=True, beam_size=5, condition_on_previous_text=False, vad_filter=False)
hyp = []
for s in segs:
    for w in s.words or []: hyp.append((w.word.strip(), round(w.start, 2), round(w.probability, 2)))
norm = lambda w: re.sub(r"[^a-z0-9]", "", w.lower())
ref = [w for l in open("production/vo_lines.txt") for w in l.split()]
R, Hn = [norm(w) for w in ref], [norm(w[0]) for w in hyp]
print("HYP:", " ".join(w[0] for w in hyp))
sm = difflib.SequenceMatcher(a=R, b=Hn, autojunk=False); n = 0
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op == "equal": continue
    n += 1; print(f"{op:8s} ref: {' '.join(ref[a0:a1])!r:45s} heard: {' '.join(w[0] for w in hyp[b0:b1])!r} @ {hyp[b0][1] if b0 < len(hyp) else '-'}")
low = [w for w in hyp if w[2] < 0.5]
print("diffs:", n, "| low-prob words:", low)
json.dump(hyp, open(f"production/whisper_{mname}.json", "w"), ensure_ascii=False)

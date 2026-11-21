"""Word diff between production/vo_lines.txt and a faster-whisper json (tools/fw_transcribe.py output).
Usage: python3 tools/vo_diff.py <whisper.json> [offset_s]"""
import json, re, sys, difflib
norm = lambda w: re.sub(r"[^a-z0-9]", "", w.lower())
ref = [norm(w) for w in open("production/vo_lines.txt").read().split()]
ref = [w for w in ref if w]
d = json.load(open(sys.argv[1]))
hyp = [(norm(w["w"]), w["s"]) for s in d["segments"] for w in s["words"]]
hyp = [h for h in hyp if h[0]]
sm = difflib.SequenceMatcher(a=ref, b=[h[0] for h in hyp], autojunk=False)
n = 0
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op == "equal": continue
    n += 1
    t = hyp[b0][1] if b0 < len(hyp) else -1
    print(f"{op:8s} @{t:7.2f}  script: {' '.join(ref[a0:a1])!r:45s} heard: {' '.join(h[0] for h in hyp[b0:b1])!r}")
print(f"ref {len(ref)} words, heard {len(hyp)}, {n} diff blocks, ratio {sm.ratio():.3f}")

"""Whisper-MEDIUM check of the final MP4: word-by-word diff against production/vo_lines.txt.
python3 -I tools/vo_diff.py <final.mp4> <whisper.json from fw_transcribe.py>"""
import json, re, sys, difflib
norm = lambda w: re.sub(r"[^a-z0-9]", "", w.lower())
ref = [norm(w) for w in open("production/vo_lines.txt").read().split() if norm(w)]
d = json.load(open(sys.argv[2]))
hyp = [norm(x["w"]) for s in d["segments"] for x in s["words"] if norm(x["w"])]
hw = [x for s in d["segments"] for x in s["words"] if norm(x["w"])]
sm = difflib.SequenceMatcher(a=ref, b=hyp, autojunk=False)
print("ref words", len(ref), "heard", len(hyp), "ratio", round(sm.ratio(), 4))
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op != "equal": print(op, "REF:", " ".join(ref[a0:a1]), "| HEARD:", " ".join(hyp[b0:b1]), "@", hw[b0]["s"] if b0 < len(hw) else "-")
# low-confidence first-word check (chopped onsets): words with probability < 0.5
low = [(x["w"], x["s"], x["p"]) for x in hw if x["p"] < 0.5]
print("low-confidence words:", low)

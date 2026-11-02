#!/usr/bin/env python3
"""render progress from a segmented HyperFrames render log (+ segments.json when present)."""
import re, json, glob, os, sys
L = sys.argv[1]; P = os.path.dirname(os.path.dirname(os.path.abspath(L)))
txt = open(L, errors="ignore").read()
m = re.findall(r"Streaming frame (\d+)/(\d+) \(segment (\d+)/(\d+)\)", txt)
if not m: print("menyiapkan render..."); sys.exit()
tot, nseg = int(m[-1][1]), int(m[-1][3]); sf = -(-tot // nseg)
best = {}
for n, _, k, _ in m: best[int(k) - 1] = max(best.get(int(k) - 1, 0), int(n))
done = set()
js = sorted(glob.glob(P + "/renders/.hf-segments/*/segments.json"), key=os.path.getmtime)
if js: done = {c["index"] for c in json.load(open(js[-1])).get("completed", [])}
f = sum(min(sf, tot - i * sf) for i in done) + sum(max(0, n - k * sf) for k, n in best.items() if k not in done)
print(f"{100 * f / tot:.0f}% ({f}/{tot} frame, {len(done)}/{nseg} bagian selesai)")

#!/usr/bin/env python3
"""Determinism + random-order seek test: snapshot the same times in sorted and shuffled (seeded) order, twice,
and compare the frames pixel-by-pixel. Run: python3 tools/qa_seek.py <outdir> t1,t2,..."""
import subprocess, sys, shutil
from pathlib import Path
import numpy as np
from PIL import Image
P = Path(__file__).resolve().parents[1]
out = Path(sys.argv[1]); times = [float(x) for x in sys.argv[2].split(",")]
order = sorted(times); shuf = [order[(i * 7 + 3) % len(order)] for i in range(len(order))]
assert sorted(shuf) == order, "choose a count not divisible by 7"
def shoot(ts, d):
    shutil.rmtree(d, ignore_errors=True)
    subprocess.run(["npx", "--yes", "hyperframes@0.8.186", "snapshot", "--at", ",".join(map(str, ts)), "--no-end", "-o", str(d)], cwd=P, check=True, capture_output=True)
    fs = sorted(d.glob("frame-*-at-*.png"), key=lambda f: int(f.name.split("-")[1]))
    return {t: f for t, f in zip(ts, fs)}
a = shoot(order, out / "sorted"); b = shoot(shuf, out / "shuffled")
worst = 0
for t in order:
    x = np.asarray(Image.open(a[t]).convert("RGB"), dtype=np.int16); y = np.asarray(Image.open(b[t]).convert("RGB"), dtype=np.int16)
    d = np.abs(x - y); m = float(d.mean()); p = float((d.max(axis=2) > 8).mean() * 100)
    worst = max(worst, p)
    print(f"t={t:6.3f}  mean|diff|={m:.3f}  px>8: {p:.3f}%")
print("WORST % pixels differing >8:", round(worst, 3))

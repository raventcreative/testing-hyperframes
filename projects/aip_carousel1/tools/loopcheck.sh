#!/usr/bin/env bash
# Seamless-loop check: snapshot every slide at t=0 and t=duration (state at the loop point) and diff the two frames.
# Usage: tools/loopcheck.sh <scratch dir>   -> prints mean / max pixel difference per slide (PNG dumps deleted)
set -euo pipefail
cd "$(dirname "$0")/.."
OUT="$1"; mkdir -p "$OUT"
python3 -I - "$OUT" <<'PY'
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageChops
out = Path(sys.argv[1])
for s in json.loads(Path("slides/manifest.json").read_text()):
    d = out / f"loop_s{s['slide']:02d}"
    d.mkdir(exist_ok=True)
    for p in d.glob("*"): p.unlink()
    D = s["duration"]
    subprocess.run(["npx", "--yes", "hyperframes@0.8.186", "snapshot", s["dir"], "--at", f"0,{D}", "--no-end", "--keep", "--timeout", "60000", "-o", str(d)],
                   check=True, capture_output=True)
    a = Image.open(d / "at-0s.png").convert("RGB"); b = Image.open(d / f"at-{D:g}s.png").convert("RGB")
    diff = ImageChops.difference(a, b).convert("L")
    hist = diff.histogram(); n = sum(hist)
    mean = sum(i * c for i, c in enumerate(hist)) / n
    big = sum(hist[24:]) / n * 100
    bbox = diff.point(lambda v: 255 if v > 24 else 0).getbbox()
    print(f"slide {s['slide']:02d} {s['kind']:7s} {str(s['effect'] or ''):15s} mean {mean:.3f}  px>24: {big:.3f}%  bbox {bbox}")
    for p in d.glob("*"): p.unlink()
    d.rmdir()
PY

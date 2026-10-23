#!/usr/bin/env bash
# Seek-safety check: snapshot the same instants in two different (non-monotonic) orders and diff the PNGs.
# Usage: tools/seek_determinism.sh  (from the project dir)
set -euo pipefail
OUT=.hyperframes/determinism
rm -rf "$OUT" && mkdir -p "$OUT/a" "$OUT/b"
npx hyperframes snapshot --at 68.4,12,87,43,5,94.2,31,57.5 --no-end -o "$OUT/a" >/dev/null 2>&1
npx hyperframes snapshot --at 31,94.2,5,57.5,43,87,12,68.4 --no-end -o "$OUT/b" >/dev/null 2>&1
python3 -I - "$OUT" <<'EOF'
import sys, os, re, glob
from PIL import Image, ImageChops
out = sys.argv[1]
def index(d):
    m = {}
    for p in glob.glob(os.path.join(out, d, 'frame-*-at-*s.png')):
        t = re.search(r'-at-([0-9.]+)s\.png$', p).group(1)
        m[float(t)] = p
    return m
a, b = index('a'), index('b')
worst = 0
for t in sorted(a):
    if t not in b: print(f't={t}: missing in run b'); continue
    ia, ib = Image.open(a[t]).convert('RGB'), Image.open(b[t]).convert('RGB')
    diff = ImageChops.difference(ia, ib)
    bbox = diff.getbbox()
    px = sum(1 for v in diff.convert('L').getdata() if v > 8) if bbox else 0
    worst = max(worst, px)
    print(f't={t:6.2f}s  differing pixels (>8/255): {px}')
print('RESULT', 'PASS' if worst == 0 else f'DIFF (max {worst} px)')
EOF

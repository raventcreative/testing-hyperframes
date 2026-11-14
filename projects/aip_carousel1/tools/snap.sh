#!/usr/bin/env bash
# Snapshot one slide with the real HyperFrames runtime and make a JPG contact sheet (PNG dumps deleted).
# Usage: tools/snap.sh <slide number> <comma times> <scratch dir> [cols] [thumb width]
set -euo pipefail
cd "$(dirname "$0")/.."
N=$(printf "%02d" "$((10#$1))"); AT="$2"; OUT="$3"; COLS="${4:-4}"; TW="${5:-360}"
mkdir -p "$OUT/s$N"
npx --yes hyperframes@0.8.186 snapshot "slides/s$N" --at "$AT" --no-end --keep --timeout 60000 -o "$OUT/s$N" > "$OUT/s$N.log" 2>&1 || { tail -20 "$OUT/s$N.log"; exit 1; }
python3 -I tools/sheet.py "$OUT/s$N" "$OUT/s${N}_sheet.jpg" "$COLS" "$TW"

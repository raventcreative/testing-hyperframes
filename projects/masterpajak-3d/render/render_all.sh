#!/usr/bin/env bash
# Final render of all three films (deterministic). Usage: bash render/render_all.sh [outdir]
set -euo pipefail
cd "$(dirname "$0")/.."
OUT="${1:-out/final}"
for s in v1 v2 v3; do
  echo "=== $s ==="
  node render/render.mjs "$s" --q final --out "$OUT"
done

#!/bin/bash
# Render every slide in scenes/ (s00..s04) to out/motion_pack_<id>_1080x1350.mp4
cd "$(dirname "$0")/.."
for s in "$@"; do python3 -I tools/build.py "$s" --render || exit 1; done

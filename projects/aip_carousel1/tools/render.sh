#!/usr/bin/env bash
# Render slides to out/<name>.mp4, ONE AT A TIME (house rule: under flock /tmp/claude-0/render.lock), then ffprobe-check each.
# Usage: tools/render.sh [slide numbers...]   (default: every slide in slides/manifest.json)
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
mkdir -p out/logs
SLIDES=("$@")
if [ ${#SLIDES[@]} -eq 0 ]; then mapfile -t SLIDES < <(python3 -I -c 'import json;[print(s["slide"]) for s in json.load(open("slides/manifest.json"))]'); fi
for n in "${SLIDES[@]}"; do
  NN=$(printf "%02d" "$((10#$n))")
  read -r OUTNAME DUR < <(python3 -I -c "import json;s=[x for x in json.load(open('slides/manifest.json')) if x['slide']==$((10#$n))][0];print(s['out'],s['duration'])")
  OUTF="$ROOT/out/$OUTNAME.mp4"
  echo "== slide $NN -> $OUTF"
  ( cd "slides/s$NN" && flock /tmp/claude-0/render.lock npx --yes hyperframes@0.8.186 render . -o "$OUTF" -q looks -f 30 -w 3 > "$ROOT/out/logs/render_s$NN.log" 2>&1 ) || { echo "RENDER FAILED s$NN"; tail -20 "$ROOT/out/logs/render_s$NN.log"; exit 1; }
  ffprobe -v error -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate,nb_frames:format=duration -of compact "$OUTF"
  python3 -I - "$OUTF" "$DUR" <<'PY'
import json, subprocess, sys
f, dur = sys.argv[1], float(sys.argv[2])
p = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", f], capture_output=True, text=True).stdout)
v = [s for s in p["streams"] if s["codec_type"] == "video"][0]
a = [s for s in p["streams"] if s["codec_type"] == "audio"]
ok = v["width"] == 1080 and v["height"] == 1350 and abs(float(p["format"]["duration"]) - dur) < 0.05 and v["r_frame_rate"] == "30/1"
print(("OK  " if ok else "BAD ") + f"{v['width']}x{v['height']} {v['r_frame_rate']} {float(p['format']['duration']):.3f}s frames={v.get('nb_frames')} audio_streams={len(a)}")
sys.exit(0 if ok else 2)
PY
done

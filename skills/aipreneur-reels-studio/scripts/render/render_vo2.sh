#!/bin/bash
# usage: render_vo2.sh <project dir> <final name> — one render at a time (lock); muxes VO + SFX ONLY if the render really succeeded
set -u
d="$1"; name="$2"; ML="$(cd "$(dirname "$0")" && pwd)"
exec 9>"$ML/render.lock"
while true; do
  while pgrep -f "hyperframes@0.8.186 render" > /dev/null; do sleep 10; done
  if flock -n 9; then
    if pgrep -f "hyperframes@0.8.186 render" > /dev/null; then flock -u 9; sleep 7; continue; fi
    break
  fi
  sleep 7
done
cd "$d" || exit 1
free=$(df -Pm . | awk 'NR==2{print $4}')
if [ "$free" -lt 3000 ]; then flock -u 9; echo "$(date +%T) SKIP $d: only ${free} MB free"; exit 1; fi
npx --yes hyperframes@0.8.186 render . -o out/video.mp4 -q looks -f 30 -w 3 > out/render.log 2>&1
flock -u 9
if ! tr '\r' '\n' < out/render.log | grep -q "rendered in" || [ out/video.mp4 -ot index.html ]; then echo "$(date +%T) FAILED $d (see out/render.log)"; exit 1; fi
"$ML/remux_vo.sh" "$d" "$name" > /dev/null
echo "$(date +%T) done $d -> out/$name  pageerrors=$(tr '\r' '\n' < out/render.log | grep -c PAGEERROR)"

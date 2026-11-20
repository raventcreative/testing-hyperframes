#!/bin/bash
# usage: render_aip.sh <project dir> <final name> — AIpreneur kit: VO + SFX are <audio> tracks inside the composition, so the
# render carries them; afterwards a synthesised music bed is added (ducked under that audio) and the mix is normalised to
# -14 LUFS (video stream copied). One render at a time (lock).
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
mkdir -p out
free=$(df -Pm . | awk 'NR==2{print $4}')
if [ "$free" -lt 3000 ]; then flock -u 9; echo "$(date +%T) SKIP $d: only ${free} MB free"; exit 1; fi
npx --yes hyperframes@0.8.186 render . -o out/video.mp4 -q looks -f 30 -w 3 > out/render.log 2>&1
flock -u 9
if ! tr '\r' '\n' < out/render.log | grep -q "rendered in" || [ out/video.mp4 -ot index.html ]; then echo "$(date +%T) FAILED $d (see out/render.log)"; exit 1; fi
"$ML/remix_aip.sh" "$d" "$name"
echo "$(date +%T) done $d -> out/$name  pageerrors=$(tr '\r' '\n' < out/render.log | grep -c PAGEERROR)"

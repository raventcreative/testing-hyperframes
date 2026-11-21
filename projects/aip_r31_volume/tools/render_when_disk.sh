#!/bin/bash
# Waits (up to 4 h) until the disk has >= 3050 MB free, then runs the shared locked render (render_aip.sh), then the R31 two-pass
# remix (tools/remix_audio.sh: untouched VO + fixed-level SFX + ducked bed, -14 LUFS) and the whisper-MEDIUM word diff on the FINAL
# MP4. Everything is logged to production/FINAL_CHECK.txt.
cd "$(dirname "$0")/.."; P=$PWD; LOG=$P/production/FINAL_CHECK.txt; ML=/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/ml
echo "$(date +%T) waiting for disk >= 3050 MB" >> $LOG
for i in $(seq 1 480); do
  f=$(df -Pm / | awk 'NR==2{print $4}')
  if [ "$f" -ge 3050 ]; then
    echo "$(date +%T) free $f MB -> render" >> $LOG
    "$ML/render_aip.sh" "$P" AIP_R31_VOLUME.mp4 >> $LOG 2>&1
    if [ -f out/video.mp4 ] && [ out/video.mp4 -nt index.html ] && tail -1 $LOG | grep -q "done "; then
      echo "$(date +%T) remix (two-pass loudnorm)" >> $LOG; bash tools/remix_audio.sh >> $LOG 2>&1
      ffprobe -v error -show_entries format=duration:stream=codec_name,width,height -of compact out/AIP_R31_VOLUME.mp4 >> $LOG 2>&1
      echo "$(date +%T) whisper MEDIUM on the final MP4:" >> $LOG; python3 tools/vo_check.py out/AIP_R31_VOLUME.mp4 medium production/whisper_medium_final.json 2>&1 | grep -v Warn >> $LOG
      echo "$(date +%T) ALL DONE" >> $LOG; exit 0
    fi
  fi
  sleep 30
done
echo "$(date +%T) gave up waiting for disk" >> $LOG

#!/bin/bash
# Rebuild the R30 mix without re-rendering: VO lead, SFX ducked hard under the voice (so "Modul" stays clear), music bed
# ducked under the voice, two-pass loudnorm to -14 LUFS; the rendered video stream is copied.
set -eu
IN=out/AIP_R30_TIM_MARKETING_AI.mp4; OUT=out/AIP_R30_TIM_MARKETING_AI_fix.mp4; D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $IN)
G="[0:a]aformat=sample_rates=48000:channel_layouts=mono,adelay=300,apad,atrim=end=$D,asplit=3[vo][k1][k2];\
[1:a]aformat=sample_rates=48000:channel_layouts=mono,volume=0.9,apad,atrim=end=$D[sfx];\
[2:a]aformat=sample_rates=48000:channel_layouts=mono,volume=0.35,apad,atrim=end=$D[bed];\
[sfx][k1]sidechaincompress=threshold=0.015:ratio=8:attack=5:release=250[sfxd];\
[bed][k2]sidechaincompress=threshold=0.02:ratio=4:attack=15:release=450[bedd];\
[vo][sfxd][bedd]amix=inputs=3:normalize=0:duration=first"
J=$(ffmpeg -hide_banner -i assets/audio/vo.mp3 -i assets/audio/sfx.wav -i assets/audio/bed.wav -filter_complex "$G,loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p')
v(){ echo "$J" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
ffmpeg -v error -y -i assets/audio/vo.mp3 -i assets/audio/sfx.wav -i assets/audio/bed.wav -i $IN -filter_complex \
 "$G,loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$(v input_i):measured_TP=$(v input_tp):measured_LRA=$(v input_lra):measured_thresh=$(v input_thresh):offset=$(v target_offset):linear=true,aformat=channel_layouts=stereo[a]" \
 -map 3:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart $OUT
ffmpeg -hide_banner -i $OUT -af ebur128 -f null - 2>&1 | grep -A1 "Integrated loudness" | tail -1

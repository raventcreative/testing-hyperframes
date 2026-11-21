#!/bin/bash
# R31 final mix without re-rendering the picture (pattern: projects/aip_r30_timmarketingai/tools/remix_audio.sh):
# VO = ONE untouched ElevenLabs take (only delayed 0.3 s to its place, no cut/pad/stretch) + SFX at a fixed lower level
# (no compressor on the SFX) + music bed ducked under the voice, two-pass loudnorm to -14 LUFS; video stream copied.
set -eu
cd "$(dirname "$0")/.."
IN=out/video.mp4; OUT=out/AIP_R31_VOLUME.mp4; D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $IN)
G="[0:a]aformat=sample_rates=48000:channel_layouts=mono,adelay=300,apad,atrim=end=$D,asplit=2[vo][k];\
[1:a]aformat=sample_rates=48000:channel_layouts=mono,volume=0.62,apad,atrim=end=$D[sfx];\
[2:a]aformat=sample_rates=48000:channel_layouts=mono,volume=0.32,apad,atrim=end=$D[bed];\
[bed][k]sidechaincompress=threshold=0.03:ratio=3:attack=40:release=600[bedd];\
[vo][sfx][bedd]amix=inputs=3:normalize=0:duration=first"
J=$(ffmpeg -hide_banner -i assets/audio/vo.mp3 -i assets/audio/sfx.wav -i assets/audio/bed.wav -filter_complex "$G,loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p')
v(){ echo "$J" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
ffmpeg -v error -y -i assets/audio/vo.mp3 -i assets/audio/sfx.wav -i assets/audio/bed.wav -i $IN -filter_complex \
 "$G,loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$(v input_i):measured_TP=$(v input_tp):measured_LRA=$(v input_lra):measured_thresh=$(v input_thresh):offset=$(v target_offset):linear=true,aformat=channel_layouts=stereo[a]" \
 -map 3:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart $OUT
ffmpeg -hide_banner -i $OUT -af ebur128=peak=true -f null - 2>&1 | grep -A12 "Summary" | grep -E "I:|LRA:|Peak:"

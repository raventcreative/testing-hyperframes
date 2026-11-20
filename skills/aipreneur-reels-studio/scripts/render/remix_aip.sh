#!/bin/bash
# usage: remix_aip.sh <project dir> <final name> — rendered audio (VO + SFX from the composition) + synthesised music bed
# ducked under it, normalised to -14 LUFS; video stream copied.
set -eu
TOOLS="${TOOLS:-$(git -C "$1" rev-parse --show-toplevel)/tools}"
cd "$1"
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 out/video.mp4)
SEED=$(( $(basename "$PWD" | cksum | cut -d' ' -f1) % 15 ))
[ -f assets/audio/bed.wav ] || python3 "$TOOLS/music_bed.py" "$D" assets/audio/bed.wav "$SEED" > /dev/null
ffmpeg -v error -y -i out/video.mp4 -i assets/audio/bed.wav -filter_complex "\
[0:a]aformat=sample_rates=48000:channel_layouts=mono,apad,asplit=2[main][key];\
[1:a]aformat=sample_rates=48000:channel_layouts=mono,apad,volume=0.35[bed];\
[bed][key]sidechaincompress=threshold=0.02:ratio=4:attack=15:release=450[bedd];\
[main][bedd]amix=inputs=2:normalize=0:duration=first,atrim=end=$D,loudnorm=I=-14:TP=-1.5:LRA=11,aformat=channel_layouts=stereo[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart "out/$2"
echo "$2 $(ffprobe -v error -show_entries format=duration -of csv=p=0 "out/$2")s"

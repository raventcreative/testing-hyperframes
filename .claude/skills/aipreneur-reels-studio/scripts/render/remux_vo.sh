#!/bin/bash
# usage: remux_vo.sh <project dir> <final name>
# Final audio for a reel: VO (lead) + SFX (ducked ~6 dB only while the VO speaks) + a synthesised music bed (ducked ~12 dB under
# speech), all padded to the film length, loudness-normalised to -14 LUFS; the rendered video stream is copied untouched.
set -eu
TOOLS=${TOOLS:-$(git -C "$1" rev-parse --show-toplevel)/tools}
cd "$1"
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 out/video.mp4)
SEED=$(( $(basename "$PWD" | cksum | cut -d' ' -f1) % 15 ))
[ -f assets/audio/bed.wav ] || python3 "$TOOLS/music_bed.py" "$D" assets/audio/bed.wav "$SEED" > /dev/null
ffmpeg -v error -y -i out/video.mp4 -i assets/audio/vo.wav -i assets/audio/sfx.wav -i assets/audio/bed.wav -filter_complex "\
[1:a]aformat=sample_rates=48000:channel_layouts=mono,apad,asplit=3[vo][k1][k2];\
[2:a]aformat=sample_rates=48000:channel_layouts=mono,apad,volume=1.0[sfx];\
[3:a]aformat=sample_rates=48000:channel_layouts=mono,apad,volume=0.35[bed];\
[sfx][k1]sidechaincompress=threshold=0.03:ratio=2:attack=8:release=220[sfxd];\
[bed][k2]sidechaincompress=threshold=0.02:ratio=4:attack=15:release=450[bedd];\
[vo][sfxd][bedd]amix=inputs=3:normalize=0:duration=first,atrim=end=$D,loudnorm=I=-14:TP=-1.5:LRA=11,aformat=channel_layouts=stereo[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart "out/$2"
echo "$2 $(ffprobe -v error -show_entries format=duration -of csv=p=0 "out/$2")s (video ${D}s)"

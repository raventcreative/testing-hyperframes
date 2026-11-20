#!/bin/bash
# Regenerate preview frames from the client's own AIpreneur reels (6 s @30fps)
cd "$(dirname "$0")" && R=..
mkdir -p assets/clip && ffmpeg -v error -y -t 6 -i $R/reel-22-konten-7-hari/out/reel-22-konten-7-hari-v1-robot3d_1080x1920.mp4 -vf fps=30,scale=360:640 -q:v 3 assets/clip/f_%03d.jpg
i=1; for spec in reel-10-tim-marketing-1-orang/out/reel-10-tim-marketing-1-orang-v3-robot3d_1080x1920.mp4:0 reel-14-ai-operating-system/out/reel-14-ai-operating-system-v1-robot3d_1080x1920.mp4:8 reel-03-closing-saat-tidur/out/reel-03-closing-saat-tidur-v2-robot3d_1080x1920.mp4:2 reel-06-ai-company-os/out/reel-06-ai-company-os-v3-robot3d_1080x1920.mp4:4 reel-18-analis-data-wa/out/reel-18-analis-data-wa-v2-robot3d_1080x1920.mp4:6 reel-09-7-langkah-tim-ai/out/reel-09-7-langkah-tim-ai-v3-robot3d_1080x1920.mp4:3 reel-12-ai-manager-resto/out/reel-12-ai-manager-resto-v1-robot3d_1080x1920.mp4:2 reel-05-framework-5-tahap/out/reel-05-framework-5-tahap-v2-robot3d_1080x1920.mp4:5; do
  mkdir -p assets/clips/c$i; ffmpeg -v error -y -ss ${spec##*:} -t 6 -i $R/${spec%:*} -vf fps=30,scale=240:426 -q:v 4 assets/clips/c$i/f_%03d.jpg; i=$((i+1)); done

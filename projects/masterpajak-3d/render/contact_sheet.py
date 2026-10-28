#!/usr/bin/env python3
"""Labelled contact sheet from a video (sampled at given times) or from PNG files.
usage:
  contact_sheet.py out.jpg --video file.mp4 --times 0,0.5,1 [--cols 4] [--tile 420]
  contact_sheet.py out.jpg --images a.png b.png ... [--cols 4]
"""
import argparse, subprocess, io
from PIL import Image, ImageDraw, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument('out')
ap.add_argument('--video')
ap.add_argument('--times')
ap.add_argument('--images', nargs='*')
ap.add_argument('--cols', type=int, default=4)
ap.add_argument('--tile', type=int, default=420)
ap.add_argument('--title', default='')
a = ap.parse_args()

frames = []
if a.video:
    for t in [float(x) for x in a.times.split(',')]:
        png = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.4f}', '-i', a.video, '-frames:v', '1', '-f', 'image2pipe', '-vcodec', 'png', '-'],
                             capture_output=True, check=True).stdout
        frames.append((f'{t:.2f}s', Image.open(io.BytesIO(png)).convert('RGB')))
else:
    for p in a.images:
        frames.append((p.split('/')[-1].rsplit('.', 1)[0], Image.open(p).convert('RGB')))

T = a.tile
cols = a.cols
rows = (len(frames) + cols - 1) // cols
head = 44 if a.title else 0
sheet = Image.new('RGB', (cols * T, rows * (T + 26) + head), (24, 28, 52))
d = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
    big = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 20)
except Exception:
    font = big = ImageFont.load_default()
if a.title:
    d.text((12, 10), a.title, fill=(254, 209, 17), font=big)
for i, (label, im) in enumerate(frames):
    x, y = (i % cols) * T, (i // cols) * (T + 26) + head
    sheet.paste(im.resize((T, T), Image.LANCZOS), (x, y))
    d.text((x + 8, y + T + 4), label, fill=(255, 255, 255), font=font)
sheet.save(a.out, quality=90)
print('wrote', a.out, sheet.size)

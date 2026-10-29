#!/usr/bin/env python3
"""Technical delivery verification for the final MP4s. Prints a Markdown report.
Checks: container/codec, 1080x1080, 60 fps, NO audio streams, frame count, full decode
(playable, no errors), pure-green background (corner/edge samples over many frames),
first frame clean green."""
import json, subprocess, sys, io
from PIL import Image

def probe(f):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-count_frames', '-of', 'json', f], capture_output=True, text=True, check=True).stdout
    return json.loads(out)

def frame(f, t):
    png = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.3f}', '-i', f, '-frames:v', '1', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(png)).convert('RGB')

size = '1080x1080'
files = sys.argv[1:]
if files and files[0].startswith('--size='):
    size = files[0].split('=', 1)[1]; files = files[1:]
SW, SH = map(int, size.split('x'))
rows = []
ok_all = True
for f in files:
    p = probe(f)
    v = [s for s in p['streams'] if s['codec_type'] == 'video']
    a = [s for s in p['streams'] if s['codec_type'] == 'audio']
    o = [s for s in p['streams'] if s['codec_type'] not in ('video',)]
    s = v[0]
    num, den = map(int, s['r_frame_rate'].split('/'))
    fps = num / den
    dur = float(p['format']['duration'])
    nb = int(s.get('nb_read_frames', 0))
    dec = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-f', 'null', '-'], capture_output=True, text=True)
    playable = dec.returncode == 0 and not dec.stderr.strip()
    # green purity: sample border pixels at 9 times
    worst = 0
    pts = [(4, 4), (SW - 5, 4), (4, SH - 5), (SW - 5, SH - 5), (SW // 2, 4), (4, SH // 2), (SW - 5, SH // 2), (SW // 2, SH - 5)]
    for k in range(9):
        im = frame(f, dur * k / 9)
        for (x, y) in pts:
            r, g, b = im.getpixel((x, y))
            worst = max(worst, abs(r - 0), abs(g - 255), abs(b - 0))
    f0 = frame(f, 0)
    f0_bad = sum(1 for px in f0.getdata() if max(px[0], 255 - px[1], px[2]) > 3)
    checks = {
        'mp4/h264': p['format']['format_name'].startswith('mov') and s['codec_name'] == 'h264',
        size: s['width'] == SW and s['height'] == SH,
        '60fps': abs(fps - 60) < 1e-6,
        'no audio': len(a) == 0 and len(o) == 0,
        'playable': playable,
        'green bg': worst <= 3,
        'frame0 clean': f0_bad == 0,
    }
    ok = all(checks.values())
    ok_all &= ok
    rows.append((f.split('/')[-1], s['codec_name'], s.get('profile', ''), s['pix_fmt'], f"{s['width']}x{s['height']}", f'{fps:g}', f'{dur:.3f}', nb, len(p['streams']), len(a), 'yes' if playable else 'NO', f'±{worst}', f0_bad, 'PASS' if ok else 'FAIL: ' + ','.join(k for k, v in checks.items() if not v)))

print('| File | Codec | Profile | Pixel fmt | Size | FPS | Duration (s) | Frames | Streams | Audio streams | Plays (full decode) | BG deviation from #00FF00 | Non-green px frame 0 | Result |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for r in rows:
    print('| ' + ' | '.join(str(x) for x in r) + ' |')
print()
print('ALL CHECKS PASSED' if ok_all else 'SOME CHECKS FAILED')
sys.exit(0 if ok_all else 1)

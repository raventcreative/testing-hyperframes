#!/usr/bin/env python3
"""Green-screen purity check for shots whose subject may touch the frame edges.
For sampled frames: every pixel that is fully transparent in the alpha master (eroded by 2 px
to ignore 4:2:0 chroma bleed and faint motion-blur tails at object edges) must be #00FF00
(+-tolerance) in the green MP4. Edge band = 12 px."""
import subprocess, sys, numpy as np
mp4, webm, W, H, N = sys.argv[1], sys.argv[2], 1920, 1080, 12
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4], capture_output=True, text=True).stdout)
def grab(args, ch):
    raw = subprocess.run(['ffmpeg', '-v', 'error'] + args + ['-frames:v', '1', '-f', 'rawvideo', '-pix_fmt', 'rgba' if ch == 4 else 'rgb24', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(H, W, ch)
worst, checked = 0, 0
frames = round(dur * 60)
for k in range(N):
    n = int(frames * (k + 0.5) / N)
    t = n / 60
    # exact frame index on both files (seeking can land on different frames while things move)
    rgb = grab(['-i', mp4, '-vf', f'select=eq(n\\,{n})'], 3).astype(int)
    a = grab(['-c:v', 'libvpx-vp9', '-i', webm, '-vf', f'select=eq(n\\,{n})'], 4)[:, :, 3]
    bg = a == 0
    m = bg.copy()
    for _ in range(12):  # erode the background mask by 12 px
        m = m & np.roll(m, 1, 0) & np.roll(m, -1, 0) & np.roll(m, 1, 1) & np.roll(m, -1, 1)
    if m.sum() == 0: continue
    dev = np.max(np.abs(rgb[m] - np.array([0, 255, 0])), axis=1)
    worst = max(worst, int(dev.max())); checked += int(m.sum())
    print(f't={t:5.2f}s  background px={int(m.sum()):8d}  max deviation from #00FF00 = {int(dev.max())}')
ok = worst <= 4
print(f'{"PASS" if ok else "FAIL"}: {checked} background pixels checked, worst deviation {worst}')
sys.exit(0 if ok else 1)

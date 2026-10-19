import subprocess, sys, numpy as np
sys.path.insert(0, "tools")
from key_black import key
SRC, OUT = "assets/source/Testing_Karakter_1.mp4", "assets/heygen/char-alpha.webm"
W, H = 720, 1280
dec = subprocess.Popen(["ffmpeg","-v","error","-i",SRC,"-f","rawvideo","-pix_fmt","rgb24","-"], stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","rgba","-s",f"{W}x{H}","-r","25","-i","-",
    "-c:v","libvpx-vp9","-pix_fmt","yuva420p","-auto-alt-ref","0","-b:v","0","-crf","24","-row-mt","1","-deadline","good","-cpu-used","4", OUT], stdin=subprocess.PIPE)
n = 0
while True:
    buf = dec.stdout.read(W*H*3)
    if len(buf) < W*H*3: break
    enc.stdin.write(key(np.frombuffer(buf, np.uint8).reshape(H, W, 3)).tobytes()); n += 1
    if n % 250 == 0: print("frames", n, flush=True)
enc.stdin.close(); enc.wait(); print("done", n)

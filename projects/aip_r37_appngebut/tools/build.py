"""tools/index.src.html -> index.html (fills TOTAL and the VO length). Run: python3 -I tools/build.py"""
import subprocess
TOTAL = 86.4
vo = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", "assets/audio/vo.mp3"], capture_output=True, text=True).stdout)
s = open("tools/index.src.html").read().replace("{{TOTAL}}", str(TOTAL)).replace("{{VOSEC}}", str(round(vo, 3)))
open("index.html", "w").write(s); print("index.html", TOTAL, "s, vo", round(vo, 3))

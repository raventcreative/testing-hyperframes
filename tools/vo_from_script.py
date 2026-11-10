"""Generate a reel VO with the client's ElevenLabs voice from the '## Naskah' section of production/VO_SCRIPT.md.
Usage: python3 tools/vo_from_script.py projects/<name>   → projects/<name>/assets/audio/vo.mp3"""
import subprocess, sys
from pathlib import Path
P = Path(sys.argv[1])
txt = (P / "production/VO_SCRIPT.md").read_text().split("## Naskah", 1)[1].split("\n", 1)[1]
lines = [l.strip() for l in txt.splitlines() if l.strip() and not l.startswith("#")]
text = "\n\n".join(lines)
(P / "production/vo_text_sent.txt").write_text(text)
out = P / "assets/audio/vo.mp3"
subprocess.run([sys.executable, str(Path(__file__).parent / "el_tts.py"), text, str(out)], check=True)
print(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)], capture_output=True, text=True).stdout.strip(), "s")

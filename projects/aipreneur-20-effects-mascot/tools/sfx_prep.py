"""VO-safe SFX variants (assets/sfx/vo_safe/): each library sound is high-passed above the speech fundamentals /
formant core, softened at the end, so it sits *around* the voice instead of on top of it.
Library: HyperFrames bundled SFX (Pixabay Content License, see assets/sfx/CREDITS.md)."""
import subprocess
from pathlib import Path
P = Path(__file__).resolve().parents[1]
SPEC = {  # name: (source, filter chain)
    "click": ("click-soft.mp3", "highpass=f=1400,afade=t=out:st=0.25:d=0.1"),
    "key": ("key-press.mp3", "highpass=f=1600,afade=t=out:st=0.25:d=0.12"),
    "type": ("typing.mp3", "highpass=f=1800,volume=0.9"),
    "pop": ("pop.mp3", "highpass=f=700,afade=t=out:st=0.45:d=0.25"),
    "sparkle": ("sparkle.mp3", "highpass=f=2600,afade=t=out:st=0.9:d=0.5"),
    "whoosh": ("whoosh-short.mp3", "highpass=f=450,lowpass=f=9000,afade=t=out:st=0.4:d=0.17"),
    "ping": ("ping.mp3", "highpass=f=1800,afade=t=out:st=0.5:d=0.6"),
}
for name, (src, af) in SPEC.items():
    out = P / f"assets/sfx/vo_safe/{name}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(P / "assets/sfx" / src), "-af", af, "-ac", "2", "-ar", "48000", str(out)], check=True)
    print(name, out.stat().st_size)

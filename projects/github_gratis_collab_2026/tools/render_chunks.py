"""Resumable chunked render (the cloud container restarts now and then; a 45-min render is too fragile).
Splits the reel at scene starts, renders each chunk as its own project copy (scene slots shifted, persistent layers time-offset
via window.__T0 / host-timeline offset, no audio), skips chunks already on disk, then concatenates the video and muxes a clean
audio mix (VO at its offset + intro SFX) normalised to -14 LUFS.
Usage: python3 tools/render_chunks.py <project_dir> <out.mp4> [quality]"""
import json, re, shutil, subprocess, sys
from pathlib import Path
P = Path(sys.argv[1]).resolve(); OUT = Path(sys.argv[2]).resolve(); Q = sys.argv[3] if len(sys.argv) > 3 else "looks"
T = json.loads((P / "production/timing.json").read_text()); TOTAL = T["total_sec"]
CUTS = [0.0] + [s["start"] for s in T["scenes"] if s["id"] in ("s05", "s09", "s13")] + [TOTAL]
WORK = OUT.parent / (OUT.stem + "_chunks"); WORK.mkdir(parents=True, exist_ok=True)
src = (P / "index.html").read_text()
def chunk_index(t0, t1):
    d = round(t1 - t0, 4); h = src
    h = re.sub(r'(<div id="main-root"[^>]*data-duration=")[0-9.]+"', rf'\g<1>{d}"', h)
    for lid in ("bg", "fx", "caps", "robot", "mascot"):
        h = re.sub(rf'(<div id="{lid}"[^>]*data-duration=")[0-9.]+"', rf'\g<1>{d}"', h)
    def slot(m):
        st = float(m.group(2))
        if st < t0 - 1e-6 or st >= t1 - 1e-6: return ""
        return m.group(1) + f'{round(st - t0, 4)}' + m.group(3)
    h = re.sub(r'(      <div id="s\d\d" class="scene"[^>]*data-start=")([0-9.]+)("[^\n]*\n)', slot, h)
    h = re.sub(r'\s*<audio [^>]*></audio>', '', h)
    h = h.replace('<script src="vendor/gsap/dist/gsap.min.js"></script>', f'<script>window.__T0 = {t0};</script>\n    <script src="vendor/gsap/dist/gsap.min.js"></script>', 1)
    seek = '(function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);'
    assert seek in h
    h = h.replace(seek, seek + f'\n        (function (t) {{ const r = t.render; t.render = function (tt, se, f) {{ return r.call(this, tt + {t0}, se, f); }}; }})(tl);', 1)
    return h
parts = []
for k in range(len(CUTS) - 1):
    t0, t1 = CUTS[k], CUTS[k + 1]
    part = WORK / f"part{k}.mp4"; parts.append(part)
    if part.exists() and part.stat().st_size > 100000: print("skip", part.name, flush=True); continue
    cp = WORK / f"proj{k}"
    if cp.exists(): shutil.rmtree(cp)
    shutil.copytree(P, cp, ignore=shutil.ignore_patterns("out", ".hyperframes", "thumbnail", "renders"))
    (cp / "index.html").write_text(chunk_index(t0, t1))
    print(f"render chunk {k}: {t0} -> {t1}", flush=True)
    tmp = WORK / f"part{k}.tmp.mp4"
    subprocess.run(["npx", "--yes", "hyperframes@0.8.186", "render", str(cp), "-o", str(tmp), "-q", Q, "-f", "30", "-w", "3"], check=True,
                   stdout=open(WORK / f"part{k}.log", "w"), stderr=subprocess.STDOUT)
    tmp.rename(part); shutil.rmtree(cp)
lst = WORK / "list.txt"; lst.write_text("".join(f"file '{p}'\n" for p in parts))
video = WORK / "video.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-an", "-c", "copy", str(video)], check=True)
# audio: VO at its offset + intro SFX (same volumes as the composition), -14 LUFS
off = int(round(T["vo_offset"] * 1000))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-i", str(P / "assets/audio/vo.mp3"), "-i", str(P / "assets/audio/sfx_intro.wav"),
                "-filter_complex", f"[1:a]adelay={off}|{off},aresample=48000[v];[2:a]volume=0.85,aresample=48000[s];[v][s]amix=inputs=2:normalize=0:duration=longest,apad,atrim=0:{TOTAL},loudnorm=I=-14:TP=-1:LRA=11[a]",
                "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", str(OUT)], check=True)
print("done", OUT, flush=True)

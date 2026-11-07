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
    # host timeline: shift its own data by -t0 (a render-patch offset is not honoured by the producer's render path)
    if t0 > 0:
        def shift_block(h, start_marker, fn):
            i = h.index(start_marker) + len(start_marker); j = h.index("\n        ];", i)
            rows = [r.strip().rstrip(",") for r in h[i:j].strip().split("\n")]
            out = [json.dumps(fn(json.loads(r)), ensure_ascii=False) for r in rows if r]
            out = [o for o in out if o != "null"]
            return h[:i] + "\n          " + ",\n          ".join(out) + h[j:]
        h = shift_block(h, "const W = [", lambda r: [r[0], round(r[1] - t0, 3), r[2]])
        h = shift_block(h, "const CAPS = [", lambda r: None if r[1] <= t0 + 0.02 else [round(max(0.0, r[0] - t0), 3), round(r[1] - t0, 3), r[2], r[3], r[4]])
        m = re.search(r"const HW = (\[.*?\]);\n", h); HW = json.loads(m.group(1))
        HW = [[round(a - t0, 4), round(b - t0, 4), lab] for a, b, lab in HW if b > t0 + 1e-6]
        h = h[:m.start(1)] + json.dumps(HW, ensure_ascii=False) + h[m.end(1):]
        # a round header already on screen at the chunk start is shown instantly (no negative-time tweens)
        h = h.replace("tl.fromTo(chip, { opacity: 0, y: -14, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.42, ease: \"back.out(2)\", immediateRender: false }, a + 0.04);",
                      "if (a < 0) tl.set(chip, { opacity: 1, y: 0, scale: 1 }, 0); else tl.fromTo(chip, { opacity: 0, y: -14, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.42, ease: \"back.out(2)\", immediateRender: false }, a + 0.04);")
        h = h.replace("tl.fromTo(ttl, { opacity: 0, y: -18 }, { opacity: 1, y: 0, duration: 0.45, ease: \"power3.out\", immediateRender: false }, a + 0.1);",
                      "if (a < 0) tl.set(ttl, { opacity: 1, y: 0 }, 0); else tl.fromTo(ttl, { opacity: 0, y: -18 }, { opacity: 1, y: 0, duration: 0.45, ease: \"power3.out\", immediateRender: false }, a + 0.1);")
        # small corner logo: already visible; its end fade shifts
        h = h.replace('tl.set("#brandlogo", { opacity: 0 }, 0);', 'tl.set("#brandlogo", { opacity: 0.95 }, 0);')
        h = re.sub(r'\n        tl\.fromTo\("#brandlogo", \{ opacity: 0 \}, \{ opacity: 0\.95[^\n]*\n', '\n', h)
        h = re.sub(r'(tl\.fromTo\("#brandlogo", \{ opacity: 0\.95 \}, [^\n]*\}, )([0-9.]+)\);', lambda m: m.group(1) + f"{round(float(m.group(2)) - t0, 4)});", h)
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

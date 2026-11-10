"""Resumable chunked render (the cloud container restarts now and then; one long render is too fragile).
The reel is cut into chunks at scene starts (frame-aligned). Each chunk renders from its own project copy (scene
slots shifted, host captions/ambient shifted, persistent 3D/rocket layers offset via window.__T0, no audio); chunks already on disk are
skipped. Then: trim + concat (x264) and mux the VO (+ SFX) normalised to -14 LUFS.
Usage: python3 tools/render_chunks.py <project_dir> <out.mp4> [quality]"""
import json, re, shutil, subprocess, sys
from pathlib import Path
P = Path(sys.argv[1]).resolve(); OUT = Path(sys.argv[2]).resolve(); Q = sys.argv[3] if len(sys.argv) > 3 else "looks"
T = json.loads((P / "production/timing.json").read_text()); TOTAL = T["total_sec"]; FPS = 30
S = {s["id"]: s for s in T["scenes"]}
# (render start, keep from, end): scenes do not overlap in this reel, so no pre-roll is needed
CH = [(0.0, 0.0, S["s04"]["start"]),
      (S["s04"]["start"], S["s04"]["start"], S["s07"]["start"]),
      (S["s07"]["start"], S["s07"]["start"], TOTAL)]
WORK = OUT.parent / (OUT.stem + "_chunks"); WORK.mkdir(parents=True, exist_ok=True)
src = (P / "index.html").read_text()
ease_sine = lambda u: -(__import__("math").cos(__import__("math").pi * u) - 1) / 2

def chunk_index(t0, t1):
    d = round(t1 - t0, 4); h = src
    h = re.sub(r'(<div[^>]*\bid="main-root"[^>]*data-duration=")[0-9.]+"', rf'\g<1>{d}"', h)   # tolerant of injected data-hf-id attributes
    for lid in ("bg", "fx", "caps", "robot", "mascot"):
        h = re.sub(rf'(<div[^>]*\bid="{lid}"[^>]*data-duration=")[0-9.]+"', rf'\g<1>{d}"', h)
    def slot(m):
        st = float(m.group(2))
        if st < t0 - 1e-6 or st >= t1 - 1e-6: return ""
        return m.group(1) + f'{round(st - t0, 4)}' + m.group(3)
    h = re.sub(r'(      <div[^>]*\bid="[swr]\d+" class="scene"[^>]*data-start=")([0-9.]+)("[^\n]*\n)', slot, h)   # s01.., w01.., r1..
    h = re.sub(r'\s*<audio [^>]*></audio>', '', h)
    h = h.replace('<script src="vendor/gsap/dist/gsap.min.js"></script>', f'<script>window.__T0 = {t0};</script>\n    <script src="vendor/gsap/dist/gsap.min.js"></script>', 1)
    # ambient drift: piecewise-linear per chunk (continuous across chunk seams)
    def amb(sel, x1, y1):
        e0, e1 = ease_sine(t0 / TOTAL), ease_sine(t1 / TOTAL)
        return (f'tl.fromTo("{sel}", {{ x: {round(x1 * e0, 2)}, y: {round(y1 * e0, 2)} }}, {{ x: {round(x1 * e1, 2)}, y: {round(y1 * e1, 2)}, '
                f'duration: {d}, ease: "none", immediateRender: false }}, 0);')
    # the animated grid + its wandering light are linear over the whole reel: give each chunk its exact slice
    def lin(sel, x0, y0, x1, y1):
        f0, f1 = t0 / TOTAL, t1 / TOTAL
        return (f'tl.fromTo("{sel}", {{ x: {round(x0 + (x1 - x0) * f0, 3)}, y: {round(y0 + (y1 - y0) * f0, 3)} }}, {{ x: {round(x0 + (x1 - x0) * f1, 3)}, '
                f'y: {round(y0 + (y1 - y0) * f1, 3)}, duration: {d}, ease: "none", immediateRender: false }}, 0);')
    h = re.sub(r'tl\.fromTo\("#grid",[^\n]*', lin("#grid", 0, 0, 430, 430), h)
    h = re.sub(r'tl\.fromTo\("#gridhl",[^\n]*', lin("#gridhl", 600, 180, 180, 640), h)
    h = re.sub(r'tl\.fromTo\("#grain"[^\n]*', f'tl.fromTo("#grain", {{ x: {round(64 * t0 / TOTAL, 2)}, y: {round(40 * t0 / TOTAL, 2)} }}, '
               f'{{ x: {round(64 * t1 / TOTAL, 2)}, y: {round(40 * t1 / TOTAL, 2)}, duration: {d}, ease: "steps({max(1, int(d * 15))})", immediateRender: false }}, 0);', h)
    if t0 > 0:
        def shift_block(h, start_marker, fn):
            i = h.index(start_marker) + len(start_marker); j = h.index("\n        ];", i)
            rows = [r.strip().rstrip(",") for r in h[i:j].strip().split("\n")]
            out = [json.dumps(fn(json.loads(r)), ensure_ascii=False) for r in rows if r]
            out = [o for o in out if o != "null"]
            return h[:i] + "\n          " + ",\n          ".join(out) + h[j:]
        h = shift_block(h, "const W = [", lambda r: [r[0], round(r[1] - t0, 3), r[2]])
        h = shift_block(h, "const CAPS = [", lambda r: None if r[1] <= t0 + 0.02 else [round(max(0.001, r[0] - t0), 3), round(r[1] - t0, 3), r[2], r[3], r[4]])
        # corner logo already visible; its end fade shifts
        h = h.replace('tl.set("#brandlogo", { opacity: 0 }, 0);', 'tl.set("#brandlogo", { opacity: 0.95 }, 0.001);')
        h = re.sub(r'\n        tl\.fromTo\("#brandlogo", \{ opacity: 0 \}, \{ opacity: 0\.95[^\n]*\n', '\n', h)
        h = re.sub(r'(tl\.fromTo\("#brandlogo", \{ opacity: 0\.95 \}, [^\n]*\}, )([0-9.]+)\);', lambda m: m.group(1) + f"{round(float(m.group(2)) - t0, 4)});", h)
    return h

import os
ONLY = [int(x) for x in os.environ.get("CHUNKS", "").split(",") if x.strip()]   # e.g. CHUNKS=0,2 renders only those (no concat)
parts = []
for k, (t0, keep, t1) in enumerate(CH):
    part = WORK / f"part{k}.mp4"; parts.append((part, round(keep - t0, 4), round(t1 - keep, 4)))
    if ONLY and k not in ONLY: continue
    if part.exists() and part.stat().st_size > 100000: print("skip", part.name, flush=True); continue
    cp = WORK / f"proj{k}"
    if cp.exists(): shutil.rmtree(cp)
    shutil.copytree(P, cp, ignore=shutil.ignore_patterns("out", ".hyperframes", "thumbnail", "renders", "reference.mp4"))
    hx = chunk_index(t0, t1)
    nsc = hx.count('class="scene"'); want = sum(1 for s in T["scenes"] if t0 - 1e-6 <= s["start"] < t1 - 1e-6)
    assert f'data-duration="{round(t1 - t0, 4)}"' in hx and nsc == want, f"chunk index not rewritten ({nsc} slots, want {want})"
    (cp / "index.html").write_text(hx)
    print(f"render chunk {k}: {t0} -> {t1} (keep from {keep})", flush=True)
    tmp = WORK / f"part{k}.tmp.mp4"
    subprocess.run(["npx", "--yes", "hyperframes@0.8.186", "render", str(cp), "-o", str(tmp), "-q", Q, "-f", str(FPS), "-w", "3"], check=True,
                   stdout=open(WORK / f"part{k}.log", "w"), stderr=subprocess.STDOUT)
    tmp.rename(part); shutil.rmtree(cp)
if ONLY: print("rendered chunks", ONLY, flush=True); sys.exit(0)
# trim pre-rolls (frame-exact) and concat in one x264 pass
ins, fc = [], []
for i, (p, ss, dur) in enumerate(parts):
    ins += ["-i", str(p)]
    f0, n = int(round(ss * FPS)), int(round(dur * FPS))
    fc.append(f"[{i}:v]trim=start_frame={f0}:end_frame={f0 + n},setpts=PTS-STARTPTS,fps={FPS}[v{i}]")
fc.append("".join(f"[v{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=0[v]")
video = WORK / "video.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(fc), "-map", "[v]", "-c:v", "libx264", "-preset", "medium", "-crf", "15",
                "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(video)], check=True)
# audio: VO at its offset (+ SFX bed if present), -14 LUFS
off = int(round(T["vo_offset"] * 1000)); sfx = P / "assets/audio/sfx.wav"
if sfx.exists():
    a_in = ["-i", str(P / "assets/audio/vo.mp3"), "-i", str(sfx)]
    flt = f"[1:a]adelay={off}|{off},aresample=48000[v];[2:a]volume=0.9,aresample=48000[s];[v][s]amix=inputs=2:normalize=0:duration=longest,apad,atrim=0:{TOTAL},loudnorm=I=-14:TP=-1:LRA=11[a]"
else:
    a_in = ["-i", str(P / "assets/audio/vo.mp3")]
    flt = f"[1:a]adelay={off}|{off},aresample=48000,apad,atrim=0:{TOTAL},loudnorm=I=-14:TP=-1:LRA=11[a]"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(video), *a_in, "-filter_complex", flt,
                "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", str(OUT)], check=True)
print("done", OUT, flush=True)

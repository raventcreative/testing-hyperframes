"""Splice whole VO lines from another ElevenLabs take (same voice, same settings) into the main take, with the character
alignment carried over. Cuts sit in the middle of the pauses between lines (8 ms fades).
Usage: python3 -I tools/splice_vo.py <main.mp3> <other.mp3> <out.mp3> <line,line,...>   (0-based line numbers from <other>)
Both .json files (written by tools/el_tts_ts.py) must sit next to their .mp3."""
import json, subprocess, sys
from pathlib import Path
import numpy as np

A, B, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
TAKE_B = {int(x) for x in sys.argv[4].split(",")}
SR = 44100
def pcm(p): return np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout, np.int16).astype(np.float32)
JA, JB = json.loads(A.with_suffix(".json").read_text()), json.loads(B.with_suffix(".json").read_text())
assert [l["text"] for l in JA["lines"]] != [] and len(JA["lines"]) == len(JB["lines"])
def segs(J, n):
    L = J["lines"]; cuts = [0.0] + [(L[i]["end"] + L[i + 1]["start"]) / 2 for i in range(len(L) - 1)] + [n / SR]
    return cuts
def line_chars(J):   # per line: (chars, starts, ends) incl. its tags, split on "\n"
    ch, st, en = J["align"]["chars"], J["align"]["start"], J["align"]["end"]; out = []; pos = 0
    for part in ch.split("\n"):
        out.append((part, st[pos:pos + len(part)], en[pos:pos + len(part)])); pos += len(part) + 1
    return out
xa, xb = pcm(A), pcm(B)
ca, cb = segs(JA, len(xa)), segs(JB, len(xb))
la, lb = line_chars(JA), line_chars(JB)
assert len(la) == len(JA["lines"]) and len(lb) == len(JB["lines"])
fade = int(0.008 * SR); audio = []; chars = []; cst = []; cen = []; lines = []; t0 = 0.0
for i in range(len(JA["lines"])):
    src, x, c, lc, J = ("B", xb, cb, lb, JB) if i in TAKE_B else ("A", xa, ca, la, JA)
    a, b = int(c[i] * SR), int(c[i + 1] * SR); seg = x[a:b].copy()
    if len(seg) > 2 * fade: seg[:fade] *= np.linspace(0, 1, fade); seg[-fade:] *= np.linspace(1, 0, fade)
    off = t0 - c[i]
    txt, s0, e0 = lc[i]
    if chars: chars.append("\n"); cst.append(round(t0, 3)); cen.append(round(t0, 3))
    chars.append(txt); cst += [round(v + off, 3) for v in s0]; cen += [round(v + off, 3) for v in e0]
    ln = dict(J["lines"][i]); ln["start"] = round(ln["start"] + off, 3); ln["end"] = round(ln["end"] + off, 3); ln["take"] = src; lines.append(ln)
    audio.append(seg); t0 += len(seg) / SR
y = np.concatenate(audio)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ar", str(SR), "-ac", "1", "-i", "-", "-c:a", "libmp3lame", "-b:a", "128k", str(OUT)],
               input=np.clip(y, -32768, 32767).astype(np.int16).tobytes(), check=True)
J = dict(JA); J["lines"] = lines; J["duration"] = round(t0, 3); J["align"] = {"chars": "".join(chars), "start": cst, "end": cen}
J["spliced"] = {"main": A.name, "other": B.name, "lines_from_other": sorted(TAKE_B)}
OUT.with_suffix(".json").write_text(json.dumps(J, indent=1, ensure_ascii=False))
print("ok", OUT, round(t0, 2), "s; lines from", B.name, sorted(TAKE_B))
for l in lines: print(f"  {l['start']:7.2f}-{l['end']:7.2f} {l['take']} {l['text'][:50]}")

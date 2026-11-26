"""Check every transition against the real VO.

What is actually being tested, per transition kind:

* a **wipe** (iris / doors / shutter) is a cover that closes, swaps the scene at its *mid*, then
  opens again. Its full span is ~1.1 s — longer than any gap in this VO — so the thing that must land
  on the beat is the **mid**, the moment the new scene is revealed. It should fall just before the
  line that introduces that scene, never after the line has got going.
* a **camera / zoom / slide** has no cover: its motion must be **settled** by the time the next line
  is under way, or the frame is still moving while the new line is read.

Both are allowed to *start* over the tail of the previous line — leading the cut is wanted.

Run: python3 -I tools/beat_audit.py
"""
import json, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
T = json.loads((P / "production/word_timing.json").read_text())
PH = T["phrases"]
ph = lambda s: next(p for p in PH if p["text"].startswith(s))
S = lambda s: ph(s)["start"]

# name, kind, start, offset of the beat that must land (wipe: mid; move: settle), leaves, reveals
TR = [
 ("zoom punch-through", "move", S("Cek simulasinya.") - 0.80, 0.66, "tinggal bales oke dari HP.", "Cek simulasinya."),
 ("tab click + slide",  "move", S("Ini bukan satu prompt") - 0.55, 0.35, "Sistemnya nyala sendiri", "Ini bukan satu prompt"),
 ("FX.iris",            "wipe", S("Bagian satu:") - 0.62, 0.53, "tapi empat bagian.", "Bagian satu:"),
 ("camera slide",       "move", S("Bagian dua:") - 0.46, 0.50, "Edit file itu aja.", "Bagian dua:"),
 ("FX.doors",           "wipe", S("Bagian tiga:") - 0.62, 0.50, "Bagian dua:", "Bagian tiga:"),
 ("zoom punch-in",      "move", S("Bagian empat:") - 0.68, 0.68, "Biar gaya videonya", "Bagian empat:"),
 ("3D swing + pop-out", "move", S("Pas topiknya abis,") - 0.55, 0.60, "sekali jalan.", "Pas topiknya abis,"),
 ("zoom-out reveal",    "move", S("Alurnya simpel: dia kerja,") - 0.60, 0.60, "dari mana aja.", "Alurnya simpel: dia kerja,"),
 ("FX.shutter",         "wipe", S("Nggak ada yang ke-posting") - 0.60, 0.56, "gue bilang oke.", "Nggak ada yang ke-posting"),
 ("zoom-through to CTA", "move", S("Mau sistem kayak gini") - 0.72, 0.72, "Keputusan akhir tetep", "Mau sistem kayak gini"),
]

bad = 0
for name, kind, at, off, lead, into in TR:
    ins = S(into)
    beat = at + off
    slack = round(ins - beat, 2)           # >0: lands before the line; <0: after it has started
    lo, hi = (-0.05, 0.40) if kind == "wipe" else (-0.10, 0.60)
    flag = ""
    if slack < lo:
        flag = f"{-slack:.2f}s LATE — {'reveal' if kind == 'wipe' else 'still moving'} after the line starts"
    elif slack > hi:
        flag = f"{slack:.2f}s early — the new scene sits there before its line"
    bad += bool(flag)
    label = "reveal " if kind == "wipe" else "settles"
    print(f"{name:21} {kind}  starts {at:6.2f}  {label} {beat:6.2f}  next line {ins:6.2f}  "
          f"slack {slack:+.2f}  " + ("OK" if not flag else flag))
print()
print("transitions clashing with speech:", bad)
sys.exit(1 if bad else 0)

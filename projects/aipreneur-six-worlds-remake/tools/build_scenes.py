#!/usr/bin/env python3
"""compositions/sNN.html (back) + sNNf.html (front) + production/mtrack/sNN.js from tools/scenes/sNN.py.
Run: python3 tools/build_scenes.py [s01 s02 ...]   (no args = every scene)  — then tools/gen_mascot.py"""
import importlib.util, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / "tools")); sys.path.insert(0, str(P / "tools/scenes"))
import xk
ids = sys.argv[1:] or [s["id"] for s in xk.SCENES["scenes"]]
for sid in ids:
    f = P / f"tools/scenes/{sid}.py"
    S = xk.Scene(sid)
    if f.exists():
        spec = importlib.util.spec_from_file_location(sid, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.build(S)
    else:   # placeholder keeps the project mountable while scenes are being built
        S.back.append(f'<div class="abs" style="left:140px;top:300px;width:800px;height:80px;font:700 40px Poppins;color:#fff">{sid} placeholder</div>')
    S.write()
    print(f"{sid}: back {len(S.back)} front {len(S.front)} tweens {len(S._tl)} mascot {len(S.mtrack)}")

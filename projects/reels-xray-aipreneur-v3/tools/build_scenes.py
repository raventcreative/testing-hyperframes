#!/usr/bin/env python3
"""Build compositions/sNN.html from tools/scenes/sNN.py (each defines build(S)).
Run: python3 tools/build_scenes.py [s01 s02 ...]   (no args = every scene that has a module)"""
import importlib.util, sys
from pathlib import Path

P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / "tools"))
import xk

ids = sys.argv[1:] or sorted(p.stem for p in (P / "tools/scenes").glob("s[0-9][0-9].py"))
# placeholder for scenes that have no module yet (keeps the whole project mountable while building)
for sc in xk.SCENES["scenes"]:
    if not (P / f"tools/scenes/{sc['id']}.py").exists() and not (P / f"compositions/{sc['id']}.html").exists():
        S = xk.Scene(sc["id"])
        S.mid.append(f'<div class="abs por" style="left:290px;top:700px;width:600px;height:400px;border-radius:40px"></div>')
        S.write()
for sid in ids:
    spec = importlib.util.spec_from_file_location(sid, P / f"tools/scenes/{sid}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    S = xk.Scene(sid)
    mod.build(S)
    S.write()
    print(f"{sid}: {len(S.far) + len(S.mid) + len(S.near)} parts, {len(S._tl)} tweens")

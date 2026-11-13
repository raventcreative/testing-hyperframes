"""Ship the 3D presenter robot (brand/robot3d: decimated client GLB + three.js + rig/face shader) and the FX kit into a
reel project. Use instead of add_mouth.py for reels that use the 3D robot.   python3 -I tools/add_robot3d.py projects/<name>
Page needs (see projects/reel-08-admin-wa-ramah): importmap for three, vendor/robot3d/robot3d_state.js before the
composition script, <script type="module" src="vendor/robot3d/robot3d.js">, <canvas id="robo3d" width="640" height="760">
inside #rmove, and REEL_FX({ ..., r3d: window.R3D, base: "light"|"dark" })."""
import shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P = Path(sys.argv[1]).resolve()
dst = P / "vendor/robot3d"
if dst.exists(): shutil.rmtree(dst)
shutil.copytree(ROOT / "brand/robot3d", dst)
shutil.copy(ROOT / "brand/fx/reel_fx.js", P / "vendor/reel_fx.js")
for n in ("bg-blue.png", "bg-light.png", "logo-aipreneur-white.png", "logo-aipreneur-dark.png"):
    if not (P / "assets" / n).exists(): shutil.copy(ROOT / "brand" / n, P / "assets" / n)
print("robot3d added:", P.name)

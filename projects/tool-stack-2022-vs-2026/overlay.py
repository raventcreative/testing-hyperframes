# Adds tool logos onto the user's own design (assets/user_design.webp) -> out/tool-stack-with-logos.png
import json, re
from pathlib import Path
D = Path(__file__).parent
src = (D / "build.py").read_text()
ns = {"D": D}
exec(src[src.index("import json"):src.index("def group")].replace('open(D / "assets/icons/svg.json")', f'open("{D}/assets/icons/svg.json")'), ns)
logos = ns["logos"]
G = {}
exec(src[src.index("G = ["):src.index("assert")], {}, G)
G = dict(G["G"])
ROWS = [("Create", 110, [514, 567, 619, 674, 725, 778, 831, 887, 938]), ("Research", 110, [1054, 1109, 1160, 1212]),
        ("Build", 560, [512, 565, 621, 672]), ("Run", 560, [788, 841, 894, 950, 1001, 1054])]
items = ""
for grp, x, ys in ROWS:
    for (cat, old, new), y in zip(G[grp], ys):
        items += f'<div class="row" style="top:{y}px;right:{1080 - x - 410 + 10}px">{logos(old)}<b class="sp"></b>{logos(new)}</div>'
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
.slide{{position:relative;width:1080px;height:1350px;background:url(assets/user_design.webp) 0 0/1080px 1350px}}
.row{{position:absolute;transform:translateY(-50%);display:flex;align-items:center;gap:0}}
.row i{{font-style:normal;color:rgba(255,255,255,.6);font-size:14px;margin:0 1px}}
.lg{{flex:none;width:22px;height:22px;border-radius:6px;overflow:hidden;display:grid;place-items:center;background:#fff;box-shadow:0 0 0 1px rgba(255,255,255,.25)}}
.lg img{{width:100%;height:100%;display:block}}.lg svg{{width:14px;height:14px}}
.sp{{width:7px}}.lg+.lg{{margin-left:-9px;box-shadow:0 0 0 1.5px #1a2d57}}
</style></head><body><section class="slide">{items}</section></body></html>'''
(D / "overlay.html").write_text(html)
print("ok")

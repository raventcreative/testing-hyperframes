"""thumbnail/cover.src.html -> thumbnail/cover.html (injects the mascot FACE/DECALS constants from compositions/mascot.html)."""
import re
from pathlib import Path
P = Path(__file__).resolve().parent.parent
m = (P / "compositions/mascot.html").read_text()
face = re.search(r"const FACE = (\{.*?\});\n", m, re.S).group(1)
dec = re.search(r"const DECALS = (\[.*?\]);\n", m, re.S).group(1)
s = (P / "thumbnail/cover.src.html").read_text().replace("/*FACE*/", face).replace("/*DECALS*/", dec)
(P / "thumbnail/cover.html").write_text(s); print("cover.html ok")

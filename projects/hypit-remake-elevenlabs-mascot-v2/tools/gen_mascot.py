"""Builds compositions/mascot.html from tools/mascot_src.html + the face calibration (inlined: compositions may not fetch)."""
import re, sys
from pathlib import Path
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
face = (P / "tools/mascot_face.json").read_text().strip()
(P / "compositions/mascot.html").write_text((P / "tools/mascot_src.html").read_text().replace("__FACE__", face))
print("mascot.html written")

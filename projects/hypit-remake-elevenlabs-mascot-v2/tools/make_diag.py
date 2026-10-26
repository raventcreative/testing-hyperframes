"""Writes diag.html: the full film trimmed to [0, END] for a short diagnostic render (same assets, same code)."""
import re, sys
from pathlib import Path
P = Path(sys.argv[1]).resolve(); END = float(sys.argv[2])
s = (P / "index.html").read_text()
def fix(m):
    tag = m.group(0)
    st = float(re.search(r'data-start="([\d.]+)"', tag).group(1))
    if st >= END - 0.01 and 'id="main"' not in tag:
        return ""
    du = re.search(r'data-duration="([\d.]+)"', tag)
    if du and st + float(du.group(1)) > END:
        tag = tag.replace(du.group(0), f'data-duration="{round(END - st, 4)}"')
    return tag
s = re.sub(r'<(div|audio)[^>]*data-start="[\d.]+"[^>]*>(?:</audio>)?', fix, s)
(P / "diag.html").write_text(s)
print("diag.html ->", END)

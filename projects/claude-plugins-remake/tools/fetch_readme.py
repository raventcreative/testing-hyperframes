"""Fetch the first real (non-badge) image from each repo README via raw.githubusercontent.com.
Saves assets/readme/NN.jpg (first frame, max 900 px wide). Run: python3 -I tools/fetch_readme.py <project>"""
import json, re, subprocess, sys, urllib.parse
from pathlib import Path
P = Path(sys.argv[1]).resolve(); out = P / "assets/readme"; out.mkdir(exist_ok=True)
PL = json.loads((P / "production/plugins.json").read_text())
BAD = re.compile(r"shields\.io|badge|badgen|star-history|contrib\.rocks|logo|avatar|sponsor|\.svg($|\?)|discord|twitter|buymeacoffee|ko-fi|vercel\.com/button|deploy", re.I)
def get(url):
    r = subprocess.run(["curl", "-sS", "-L", "--max-time", "20", "-f", url], capture_output=True)
    return r.stdout if r.returncode == 0 else None
for i, p in enumerate(PL):
    if p.get("unverified"): continue
    repo = p["repo"]; md = None
    for br in ("main", "master"):
        for fn in ("README.md", "readme.md", "Readme.md"):
            md = get(f"https://raw.githubusercontent.com/{repo}/{br}/{fn}")
            if md: base = f"https://raw.githubusercontent.com/{repo}/{br}/"; break
        if md: break
    if not md: print(i, repo, "no README"); continue
    txt = md.decode("utf8", "ignore")
    urls = re.findall(r'!\[[^\]]*\]\(([^)\s]+)', txt) + re.findall(r'<img[^>]+src="([^"]+)"', txt)
    got = None
    for u in urls:
        if BAD.search(u): continue
        if u.startswith("./"): u = u[2:]
        if not u.startswith("http"): u = base + u.lstrip("/")
        u = re.sub(r"github\.com/([^/]+)/([^/]+)/blob/", r"raw.githubusercontent.com/\1/\2/", u)
        if "github.com/user-attachments" in u: continue
        data = get(u)
        if not data or len(data) < 8000 or len(data) > 12_000_000: continue
        tmp = out / f"_{i:02d}"; tmp.write_bytes(data)
        r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-frames:v", "1", "-vf", "scale='min(900,iw)':-2", str(out / f"{i:02d}.jpg")], capture_output=True)
        tmp.unlink()
        if r.returncode == 0:
            wh = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=width,height", "-of", "csv=p=0", str(out / f"{i:02d}.jpg")], capture_output=True, text=True).stdout.strip()
            w, h = map(int, wh.split(",")[:2])
            if w >= 300 and 0.3 < h / w < 2.2: got = (u, wh); break
            (out / f"{i:02d}.jpg").unlink()
    print(i, repo, got[1] if got else "-", (got[0][:90] if got else ""))
    p["readme_img"] = f"assets/readme/{i:02d}.jpg" if got else None
(P / "production/plugins.json").write_text(json.dumps(PL, indent=1, ensure_ascii=False))

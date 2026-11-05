# Builds carousel.html: draws the AI vs Jobs chart from real monthly data (data/*.csv).
# Job openings: BLS JOLTS (FRED series JTSJOL), thousands. S&P 500: monthly average (datasets/s-and-p-500).
import csv
from pathlib import Path

d = Path(__file__).parent
START, END = "2003-01-01", "2025-02-01"
CHATGPT = 2022 + 10 / 12 + 29 / 365  # 30 Nov 2022

def series(path, key, val):
    rows = [r for r in csv.DictReader(open(d / path)) if START <= r[key] <= END]
    return [(int(r[key][:4]) + (int(r[key][5:7]) - 1) / 12, float(r[val])) for r in rows]

jobs = series("data/jolts.csv", "observation_date", "JTSJOL")   # thousands
spx = series("data/spx.csv", "Date", "SP500")

# plot box inside the chart svg
W, H, L, R, T, B = 860, 560, 70, 70, 70, 60
x0, x1 = 2003, 2025 + 1 / 12
def X(t): return L + (t - x0) / (x1 - x0) * (W - L - R)
def YJ(v): return T + (1 - v / 13000) * (H - T - B)      # jobs: 0–13M
def YS(v): return T + (1 - v / 6500) * (H - T - B)       # S&P: 0–6,500

def path(pts, fy):
    return "M" + " L".join(f"{X(t):.1f},{fy(v):.1f}" for t, v in pts)

grid = "".join(f'<line x1="{L}" x2="{W-R}" y1="{YJ(v):.1f}" y2="{YJ(v):.1f}" class="gr"/>' for v in (0, 4000, 8000, 12000))
ylab = "".join(f'<text x="{L-14}" y="{YJ(v)+7:.1f}" text-anchor="end" class="ax">{v//1000}M</text>' for v in (0, 4000, 8000, 12000))
ylab += "".join(f'<text x="{W-R+14}" y="{YS(v)+7:.1f}" class="ax">{v:,}</text>' for v in (0, 2000, 4000, 6000))
xlab = "".join(f'<text x="{X(y):.1f}" y="{H-B+38}" text-anchor="middle" class="ax">{y}</text>' for y in range(2003, 2026, 4))
cx = X(CHATGPT)
jx, jy = X(jobs[-1][0]), YJ(jobs[-1][1])
sx, sy = X(spx[-1][0]), YS(spx[-1][1])

chart = f'''<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" class="chart">
  <defs><linearGradient id="tg" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#0a0d2c"/><stop offset="1" stop-color="#294b77"/></linearGradient></defs>
  {grid}{ylab}{xlab}
  <line x1="{cx:.1f}" x2="{cx:.1f}" y1="{T-26}" y2="{H-B}" class="cg"/>
  <text x="{cx-12:.1f}" y="{T-34}" text-anchor="end" class="cl"><tspan font-weight="700">ChatGPT</tspan> released</text>
  <path d="{path(jobs, YJ)}" class="lj"/>
  <path d="{path(spx, YS)}" class="ls"/>
  <circle cx="{sx:.1f}" cy="{sy:.1f}" r="8" class="ds"/><circle cx="{jx:.1f}" cy="{jy:.1f}" r="8" class="dj"/>
</svg>'''

def pct(s):
    a = next(v for t, v in s if t >= 2022 + 10 / 12 - 1e-6)
    return round((s[-1][1] / a - 1) * 100)

html = (d / "carousel.src.html").read_text()
html = html.replace("{{CHART}}", chart).replace("{{SPX_PCT}}", f"+{pct(spx)}%").replace("{{JOBS_PCT}}", f"−{abs(pct(jobs))}%")
(d / "carousel.html").write_text(html)
print("ok", pct(spx), pct(jobs))

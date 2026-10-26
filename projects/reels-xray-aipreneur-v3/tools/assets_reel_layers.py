"""X-ray layers of our own Hypit Reel (projects/hypit-remake-elevenlabs-mascot-v2) at t = 5.3 s ("Namanya Hypit,").
Each layer was rendered by HyperFrames with the other layers hidden, once over black and once over white;
difference matting gives exact alpha: a = 1 - (W - K)/255, colour = K / a.
Run: python3 tools/assets_reel_layers.py <dir with out_<variant>/frame-00-at-5.3s.png>"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image
S = Path(sys.argv[1]); P = Path(__file__).resolve().parents[1]
out = P / "assets/elements/xray/reel"; out.mkdir(parents=True, exist_ok=True)
L = lambda v: np.asarray(Image.open(S / f"out_{v}/frame-00-at-5.3s.png").convert("RGB")).astype(float)
Image.fromarray(L("full").astype("uint8")).save(out / "full.png")
Image.fromarray(L("bg").astype("uint8")).save(out / "bg.png")
comp = L("bg")
for name in ("scene", "mascot", "cap"):
    k, w = L(name + "_k"), L(name + "_w")
    a = np.clip(1 - (w - k).mean(axis=2) / 255, 0, 1)
    rgb = np.where(a[..., None] > 0.003, k / np.maximum(a[..., None], 1e-3), 0).clip(0, 255)
    Image.fromarray(np.dstack([rgb, a * 255]).astype("uint8"), "RGBA").save(out / f"{name}.png")
    comp = comp * (1 - a[..., None]) + rgb * a[..., None]
err = np.abs(comp - L("full")).mean(axis=2)
print("recomposite vs full: mean err", round(float(err.mean()), 2), "p99", round(float(np.percentile(err, 99)), 1))

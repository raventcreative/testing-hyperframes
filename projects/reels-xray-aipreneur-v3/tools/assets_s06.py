"""S06 assets from the user's screenshots (assets/elements/user/):
- claude_code_screen.png -> assets/elements/xray/s06/cc_screen.png : cropped to the composer area, the private
  'Blocked …' task list and the composer placeholder removed (flat UI colours, so a plain fill is exact).
- google_search.png -> assets/elements/xray/s06/google_logo.png : the logo only, background keyed out, 3x Lanczos.
Run: python3 tools/assets_s06.py"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter
P = Path(__file__).resolve().parents[1]
out = P / "assets/elements/xray/s06"; out.mkdir(parents=True, exist_ok=True)
im = Image.open(P / "assets/elements/user/claude_code_screen.png").convert("RGB")
a = np.asarray(im).copy()
a[240:318, 660:965] = (25, 25, 25)            # private "Blocked" session list
a[641:667, 500:760] = (48, 48, 48)            # composer placeholder text
crop = Image.fromarray(a).crop((440, 120, 1184, 702))   # 744 x 582
crop.save(out / "cc_screen.png")
g = Image.open(P / "assets/elements/user/google_search.png").convert("RGB").crop((128, 103, 322, 168))
ga = np.asarray(g).astype(float)
d = np.clip((np.abs(ga - 255).max(axis=2) - 6) / 60, 0, 1)      # distance from white -> alpha
rgb = np.where(d[..., None] > 0, 255 - (255 - ga) / np.maximum(d[..., None], 1e-3), 255).clip(0, 255)
logo = Image.fromarray(np.dstack([rgb, d * 255]).astype("uint8"), "RGBA")
logo = logo.resize((logo.width * 3, logo.height * 3), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.2, 60, 2))
logo.save(out / "google_logo.png")
print(crop.size, logo.size)

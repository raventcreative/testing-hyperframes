# Replaces the top-left logo in out/tool-stack-with-logos.png with assets/aipreneur_logo_new.png (navy gradient).
# Run after overlay.py + its screenshot step.
from PIL import Image
import numpy as np
img = Image.open('out/tool-stack-with-logos.png').convert('RGB')
x0, y0, x1, y1 = 90, 89, 309, 158; h = y1 - y0
img.paste(img.crop((x0, y0 - h - 4, x1, y0 - 4)), (x0, y0))  # cover old logo with background from just above
al = np.asarray(Image.open('assets/aipreneur_logo_new.png'))[:, :, 3]
yy, xx = np.where(al > 10); al = al[yy.min():yy.max() + 1, xx.min():xx.max() + 1]
H, W = al.shape; t = np.linspace(0, 1, W)[None, :, None]
rgb = (np.array([10, 13, 44]) * (1 - t) + np.array([41, 75, 119]) * t).repeat(H, 0).astype(np.uint8)
logo = Image.fromarray(np.dstack([rgb, al]), 'RGBA'); w = 340
logo = logo.resize((w, round(H * w / W)), Image.LANCZOS)
img.paste(logo, (96, (y0 + y1) // 2 - logo.height // 2), logo)
img.save('out/tool-stack-with-logos.png')

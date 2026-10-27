"""Seeded cumulus sprites (RGBA, lit as volumes from the north-west) + soft ground-shadow sprites -> assets/clouds/."""
import os, numpy as np
from PIL import Image, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "clouds"); os.makedirs(OUT, exist_ok=True)
N = 512

def fbm(rng, octaves=6, base=4):
    acc = np.zeros((N, N), np.float32); amp = 1.0; tot = 0
    for o in range(octaves):
        g = base * 2 ** o
        grid = rng.random((g + 1, g + 1)).astype(np.float32)
        acc += np.asarray(Image.fromarray(grid).resize((N, N), Image.BICUBIC), np.float32) * amp; tot += amp; amp *= 0.5
    return acc / tot

def smooth(a, r):
    k = np.exp(-np.arange(-int(3 * r), int(3 * r) + 1) ** 2 / (2 * r * r)); k /= k.sum()
    a = np.apply_along_axis(lambda m: np.convolve(m, k, mode="same"), 0, a)
    return np.apply_along_axis(lambda m: np.convolve(m, k, mode="same"), 1, a).astype(np.float32)

yy, xx = (np.mgrid[0:N, 0:N] / N - 0.5).astype(np.float32)
for i in range(10):
    rng = np.random.default_rng(2000 + i)
    ang = rng.uniform(0, np.pi); ca, sa = np.cos(ang), np.sin(ang)
    u, v = xx * ca + yy * sa, -xx * sa + yy * ca
    sx, sy = rng.uniform(0.24, 0.33), rng.uniform(0.15, 0.23)
    env = np.exp(-(u / sx) ** 2 - (v / sy) ** 2)
    h = np.zeros((N, N), np.float32)
    for b in range(320):
        cx, cy = rng.normal(0, sx * 0.5), rng.normal(0, sy * 0.5)
        px, py = cx * ca - cy * sa, cx * sa + cy * ca
        r0 = rng.uniform(0.010, 0.045)
        h += rng.uniform(0.3, 1.0) * np.exp(-(((xx - px) ** 2 + (yy - py) ** 2) / (2 * r0 * r0)))
    h = (h / (np.percentile(h, 99.5) + 1e-6)) * env + 0.34 * (fbm(rng, 7, 6) - 0.5)
    dens = np.clip((h - 0.12) / 0.42, 0, 1); dens = dens * dens * (3 - 2 * dens) * np.clip(1 - (np.hypot(xx, yy) / 0.49) ** 8, 0, 1)
    # volume lighting from the height field
    hs = smooth(h, 1.6) * 90
    gy, gx = np.gradient(hs)
    nz = 1 / np.sqrt(gx * gx + gy * gy + 1)
    light = np.clip((-gx * -0.6 + -gy * -0.6) * nz + nz * 0.55, 0, 1.2)  # sun north-west
    light = 0.55 + 0.45 * light + 0.08 * (fbm(rng, 4, 16) - 0.5)
    lo = np.array([168, 182, 202], np.float32); hi = np.array([255, 255, 255], np.float32)
    t = np.clip((light - 0.55) / 0.6, 0, 1)[..., None]
    rgb = lo * (1 - t) + hi * t
    a = np.clip(dens ** 0.85, 0, 1) * 245
    Image.fromarray(np.dstack([rgb, a]).astype(np.uint8), "RGBA").save(os.path.join(OUT, f"c{i}.png"), optimize=True)
    sh = Image.fromarray((dens * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(10))
    shadow = np.dstack([np.full((N, N), 18), np.full((N, N), 30), np.full((N, N), 44), np.asarray(sh)]).astype(np.uint8)
    Image.fromarray(shadow, "RGBA").resize((256, 256), Image.LANCZOS).save(os.path.join(OUT, f"s{i}.png"), optimize=True)
print("clouds", len(os.listdir(OUT)))

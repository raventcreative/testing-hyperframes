# Prints the AIpreneur logo onto the robot's chest panel.
# The logo is bent to follow the curved panel, shaded with the panel's own lighting,
# and the glossy highlights of the body are laid back on top so it reads as a printed decal.
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import map_coordinates, gaussian_filter

ROBOT = "out/robot-cutout.png"          # background already removed
LOGO = sys.argv[1]                      # logo PNG (dark logo, transparent or white bg)

# placement (robot image pixels)
CX, CY = 688, 612        # logo centre on the chest
WIDTH = 330              # logo width along the surface
ARC = 11                 # how much the sides rise (follows the panel's curved lower edge)
RADIUS = 520             # cylinder radius of the panel, for edge foreshortening
INK = np.array([22, 26, 44], float)  # print colour: near-black navy like the body parts

robot = np.array(Image.open(ROBOT).convert("RGBA")).astype(float)
H, W = robot.shape[:2]

# logo alpha mask
lg = Image.open(LOGO).convert("RGBA")
la = np.array(lg)[..., 3].astype(float)
if la.min() > 250:  # opaque logo on white: take alpha from darkness
    la = 255 - np.array(lg.convert("L")).astype(float)
ys, xs = np.where(la > 20)
la = la[ys.min():ys.max() + 1, xs.min():xs.max() + 1] / 255.0
lh, lw = la.shape
HEIGHT = WIDTH * lh / lw

# inverse warp: for every robot pixel near the chest, find the logo pixel it shows
pad = 40
x0, x1 = int(CX - WIDTH / 2 - pad), int(CX + WIDTH / 2 + pad)
y0, y1 = int(CY - HEIGHT / 2 - ARC - pad), int(CY + HEIGHT / 2 + pad)
gy, gx = np.mgrid[y0:y1, x0:x1].astype(float)
dx = gx - CX
theta = np.arcsin(np.clip(dx / RADIUS, -1, 1))
u = (RADIUS * theta) / WIDTH + 0.5                     # arc length -> logo x
base = CY - ARC * (dx / (WIDTH / 2)) ** 2              # smile-shaped baseline
v = (gy - base) / HEIGHT + 0.5
m = map_coordinates(la, [v * (lh - 1), u * (lw - 1)], order=1, mode="constant", cval=0.0)
m = gaussian_filter(m, 0.45)                           # print edge, not a sticker cut

region = robot[y0:y1, x0:x1]
rgb = region[..., :3]
lum = rgb @ [0.299, 0.587, 0.114]
light = gaussian_filter(lum, 6) / 245.0                # panel shading, smooth
spec = np.clip((lum - gaussian_filter(lum, 18)) / 40.0, 0, 1)  # glossy highlights

ink = INK[None, None, :] * np.clip(light, 0.55, 1.08)[..., None]
ink = ink + spec[..., None] * 90                       # clear-coat reflection over the print
k = (m * 0.94)[..., None]
out = rgb * (1 - k) + ink * k

# tiny edge light-catch below the print edges (ink has a hair of thickness)
edge = np.clip(m - np.roll(m, 1, axis=0), 0, 1)
out = out + edge[..., None] * 14

region[..., :3] = np.clip(out, 0, 255)
robot[y0:y1, x0:x1] = region
Image.fromarray(robot.astype(np.uint8)).save("out/robot-aipreneur.png")
print("ok", WIDTH, round(HEIGHT, 1))

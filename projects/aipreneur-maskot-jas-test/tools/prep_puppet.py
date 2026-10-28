#!/usr/bin/env python3
"""Cut the supplied 2D mascot render (assets/puppet/source_cut.png, background removed) into puppet parts on the
same 1254x1254 canvas: body (torso+legs, lower arms removed), armL / armR (shoulder->hand, pivot at the shoulder),
head (everything above the collar). Parts overlap at the joints so rotations never open a gap."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
P = Path(__file__).resolve().parents[1] / "assets/puppet"
src = Image.open(P / "source_cut.png").convert("RGBA")
W, H = src.size
ARM_L = [(452, 686), (510, 698), (505, 765), (478, 830), (458, 885), (448, 935), (440, 985), (310, 985), (315, 860), (370, 800), (412, 730)]
ARM_R = [(W - 1 - x, y) for x, y in ARM_L]
ARM_R = [(802, 686), (745, 698), (752, 765), (778, 830), (800, 885), (812, 935), (822, 985), (950, 985), (945, 860), (885, 800), (842, 730)]
HEAD_Y = 664


def poly_mask(pts, ymin=0):
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).polygon(pts, fill=255)
    if ymin:
        ImageDraw.Draw(m).rectangle([0, 0, W, ymin], fill=0)
    return m


def with_mask(m):
    out = src.copy()
    a = Image.composite(src.split()[-1], Image.new("L", (W, H), 0), m)
    out.putalpha(a)
    return out


full = Image.new("L", (W, H), 255)
head_m = Image.new("L", (W, H), 0); ImageDraw.Draw(head_m).rectangle([0, 0, W, HEAD_Y], fill=255)
head_m = head_m.filter(ImageFilter.GaussianBlur(1.5))
armL_m, armR_m = poly_mask(ARM_L), poly_mask(ARM_R)
# body keeps the shoulders (arm layers cover them again); only the hanging sleeve + hand below y 770 is removed
cut_lo = Image.new("L", (W, H), 0)
cut_lo.paste(poly_mask(ARM_L, 770), (0, 0), poly_mask(ARM_L, 770)); cut_lo.paste(poly_mask(ARM_R, 770), (0, 0), poly_mask(ARM_R, 770))
body_m = Image.new("L", (W, H), 255); ImageDraw.Draw(body_m).rectangle([0, 0, W, HEAD_Y - 6], fill=0)
body_m = Image.composite(Image.new("L", (W, H), 0), body_m, cut_lo)
for name, m in (("head", head_m), ("body", body_m), ("armL", armL_m), ("armR", armR_m)):
    with_mask(m).save(P / f"{name}.png", optimize=True)
    print(name, with_mask(m).split()[-1].getbbox())

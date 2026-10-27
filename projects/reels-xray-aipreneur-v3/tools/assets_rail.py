"""Split the user's camera-on-rail photo (assets/elements/user/camera_rail.webp) into animatable layers.

  rail.png   the rail alone: the dolly is removed and the rail under it is rebuilt from the rail's own
             periodic structure (homography-rectified strip, columns copied one/two/three rung periods back)
  dolly.png  camera + head + cart + wheels (slides along the rail direction in the scene)
  rail_meta.json  rail direction, rung period, lens centre/radius, wheel hubs, dolly contact point (photo px)

Run with the venv that has opencv: <venv>/bin/python -I tools/assets_rail.py <project>
"""
import json, sys
from pathlib import Path
import numpy as np, cv2

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
OUT = P / "assets/elements/xray/rail"
OUT.mkdir(parents=True, exist_ok=True)
im = cv2.imread(str(P / "assets/elements/user/camera_rail.webp"), cv2.IMREAD_UNCHANGED)
Hh, Ww = im.shape[:2]

# ---- rail geometry measured from the navy tube centre lines (photo px)
back = lambda x: 933 - 0.4488 * (x - 160)          # far/back tube
front = lambda x: 1003 - 0.505 * (x - 360)         # near/front tube
Pb0, Pb1, Pf0, Pf1 = (110, 955.4), (1080, 520.1), (316.9, 1024.8), (1221.9, 567.7)
U, V, M, MV = 1100, 230, 150, 130
src = np.float32([[M, MV], [U + M, MV], [U + M, V + MV], [M, V + MV]])
H = cv2.getPerspectiveTransform(src, np.float32([Pb0, Pb1, Pf1, Pf0]))      # rect -> photo
Hi = np.linalg.inv(H)
RW, RH = U + 2 * M, V + 2 * MV
rect = cv2.warpPerspective(im, Hi, (RW, RH), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
PERIOD = 168                                         # rung period in rect px (rungs at 135, 303, ..., 975, 1143)
HID0, HID1 = 380, 1030                               # rect columns hidden by the dolly (incl. wheel footprints)
SRC0, SRC1 = 140, 380                                # clean near section used as source
rebuilt = rect.copy()
for x in range(HID0, HID1):
    k = 1
    while x - k * PERIOD >= SRC1:
        k += 1
    sx = x - k * PERIOD
    rebuilt[:, x] = rect[:, sx]
# feather the two seams over 10 px
for x0 in (HID0, HID1):
    for d in range(-5, 5):
        x = x0 + d
        w = (d + 5) / 10.0 if x0 == HID0 else 1 - (d + 5) / 10.0
        rebuilt[:, x] = (rect[:, x] * (1 - w) + rebuilt[:, x] * w).astype(np.uint8)
back_img = cv2.warpPerspective(rebuilt, H, (Ww, Hh), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
zone_r = np.zeros((RH, RW), np.uint8); zone_r[:, HID0 - 5:HID1 + 5] = 255
zone = cv2.warpPerspective(zone_r, H, (Ww, Hh), flags=cv2.INTER_NEAREST) > 0

# ---- dolly mask (photo px): camera rig above the back tube + cart/axles/wheels polygon
yy, xx = np.mgrid[0:Hh, 0:Ww]
alpha = im[..., 3] > 8
rig = alpha & (xx >= 352) & (xx <= 935) & (yy < back(xx) - 24)
poly = np.array([(398, 700), (492, 640), (842, 622), (920, 648), (920, 745), (836, 752), (700, 750), (697, 884),
                 (576, 888), (568, 806), (518, 818), (398, 818)], np.int32)
pm = np.zeros((Hh, Ww), np.uint8); cv2.fillPoly(pm, [poly], 255)
dmask = (rig | (pm > 0)) & alpha
dmask = cv2.morphologyEx(dmask.astype(np.uint8) * 255, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
soft = cv2.GaussianBlur(dmask, (3, 3), 0).astype(np.float32) / 255.0

dolly = im.copy(); dolly[..., 3] = (im[..., 3].astype(np.float32) * soft).astype(np.uint8)
hard = cv2.dilate(dmask, np.ones((7, 7), np.uint8)) > 0                     # rail cut: no halo of the rig
rail = im.copy(); rail[..., 3][hard] = 0
rail[zone] = back_img[zone]

def save_trim(img, name, pad=4):
    a = img[..., 3] > 4
    ys, xs = np.nonzero(a)
    x0, y0, x1, y1 = max(0, xs.min() - pad), max(0, ys.min() - pad), min(Ww, xs.max() + pad + 1), min(Hh, ys.max() + pad + 1)
    cv2.imwrite(str(OUT / name), img[y0:y1, x0:x1], [cv2.IMWRITE_PNG_COMPRESSION, 9])
    return [int(x0), int(y0), int(x1 - x0), int(y1 - y0)]

meta = {"source": "assets/elements/user/camera_rail.webp", "photo_size": [Ww, Hh],
        "rail_box": save_trim(rail, "rail.png"), "dolly_box": save_trim(dolly, "dolly.png"),
        "rail_dir": [0.9121, -0.4100],                  # unit vector along the rail, toward the far (upper-right) end
        "period_px_near": 165,                          # rung spacing in photo px around the dolly
        "width_at": {"360": 159.8, "1020": 122.7},      # back->front tube gap (perspective scale cue)
        "lens": {"cx": 455, "cy": 362, "rx": 80, "ry": 83},
        "contact": [655, 760],                          # dolly reference point on the rail (scale origin)
        "wheel_hubs": [[455, 755, 30], [636, 812, 32], [870, 683, 26], [776, 618, 22]]}
(OUT / "rail_meta.json").write_text(json.dumps(meta, indent=1))
print(json.dumps(meta))

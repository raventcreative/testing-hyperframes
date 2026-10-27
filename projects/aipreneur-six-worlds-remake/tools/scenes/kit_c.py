"""Private contracts for S06 (spotlight) -> S07 (colour-grade dial) -> S08 ring."""
from kit import WIDE

S06_END = dict(WIDE, fx=470, yaw=0, pitch=6)    # full body on stage, shifted left so the lifted palm is clear of the face
IRIS_C = (785, 1222, 170)                        # iris on the lifted palm at S06 end (centre x, y, diameter)
S07_VIEW = {"fx": 175, "fy": 1700, "h": 860, "yaw": 14, "pitch": 5}   # S07: mascot small, left, hand on the dial
DIAL = (470, 1300, 220)                          # S07 dial (centre x, y, diameter)
CARD = (440, 290, 570, 880)                      # S07 graded frame card (x, y, w, h)
RING_END = (540, 1000, 560)                      # S07 end = S08 start: thin navy ring with 6 detents

# Feature-tracked down-page speed (LK) in the frame's middle band + zoom sign; skips textureless frames.
import cv2, numpy as np, glob, sys
fr = sorted(glob.glob(sys.argv[1] + '/f_*.png')); prev = None; rows = []
for i, f in enumerate(fr):
    g = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2GRAY)
    if prev is not None:
        m = np.zeros_like(prev); m[300:850, 150:1290] = 255
        p0 = cv2.goodFeaturesToTrack(prev, 300, 0.01, 8, mask=m)
        if p0 is not None and len(p0) >= 12:
            p1, st, _ = cv2.calcOpticalFlowPyrLK(prev, g, p0, None, winSize=(31, 31), maxLevel=4)
            ok = st[:, 0] == 1; d = (p1 - p0)[ok, 0]; P = p0[ok, 0]
            vy = -np.median(d[:, 1]); c = P - [720, 576]
            sel = np.abs(c[:,0]) > 150
            zoom = np.median(d[sel,0] / c[sel,0]) if sel.sum() > 8 else 0.0  # horizontal scale change only (tilted parallax-free)
            rows.append((i / 30, vy, zoom, int(ok.sum())))
        else: rows.append((i / 30, None, None, 0))
    prev = g
fl = [r for r in rows if r[0] < 8.2 and r[1] is not None]
import numpy as _n
sm=[_n.median([x[1] for x in fl[max(0,k-4):k+5]]) for k in range(len(fl))]
dips = [(round(fl[k][0],2), round(float(sm[k]),1)) for k in range(1,len(fl)) if 1.7<fl[k][0]<7.2 and sm[k] < 0.8*_n.median(sm[max(0,k-15):k+15])]
_old = [(round(t, 2), round(v, 1)) for k, (t, v, z, n) in enumerate(fl) if 0.1 < t < 8.2 and k > 0 and v < fl[k-1][1] - 2.5 and t < 7.3]
zin = [(round(t, 2), round(z * 1e3, 3)) for t, v, z, n in fl if z > 1e-3]
for t, v, z, n in rows[::9]: print(f'{t:5.2f}', 'no-texture' if v is None else f'{v:6.1f}px/f zoom {z*1e3:+.3f} n={n}')
print('measured frames', len(fl), 'of', sum(1 for r in rows if r[0] < 8.2))
print('DIPS (>2.5px/f drop frame-to-frame, before 7.3s):', dips or 'none')
print('ZOOM-IN during flight:', zin or 'none')

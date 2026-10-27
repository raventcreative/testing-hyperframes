"""17 EFEK (1080x1080) kit: deterministic builders for the scene compositions.

Layering (root, back to front):  plate -> sNN (BACK layer) -> 3D mascot canvas -> sNNf (FRONT layer) -> hud ->
captions -> logo -> grain.  One scene module (tools/scenes/sNN.py) defines build(S) and writes both layers:

  S.back / S.front        lists of HTML strings (inside a shared CSS-3D camera #sNN-cam / #sNNf-cam)
  S.css                   CSS rules (prefix ids with the scene id)
  S.init(sel, props)      gsap.set at build time          S.tset(sel, props, at)   tl.set at GLOBAL time
  S.ft(sel, frm, to, at, dur, ease)                        tl.fromTo at GLOBAL time (converted to local)
  S.keys(sel, keys)       keyframe chain [(t, props, ease)] (first key = initial state)
  S.cam(keys)             camera keys, applied to back AND front cameras (they move as one world)
  S.W(i) / S.WE(i)        measured VO word start / end (global seconds)
Mascot track (the 3D canvas is the scene's "footage"; global times, written into compositions/mascot.html):
  S.mv(keys)              view keys  [(t, {fx, fy, h, yaw, pitch, vis}, ease)]   fx/fy = feet px, h = figure px
  S.mx(keys)              wrapper keys on #m-xf (x, y, scale, rotation, rotationX/Y, opacity, filter ...)
  S.mc(keys)              clip keys on #m-clip ({"clipPath": inset(...)}); use clip_rect()/clip_circle()
  S.mset(sel, props, at)  instant set on a mascot element
Tweens are routed to the composition that owns the element id (back or front). Everything is a pure function
of timeline time: no random, no timers, finite repeats only.
"""
import json, math, re
from pathlib import Path

P = Path(__file__).resolve().parents[1]
WORDS = []   # no voice-over: these are silent effect demos
SCENES = json.loads((P / "production/scenes.json").read_text())
D = SCENES["duration"]
CYAN = "#00D0FE"
# default hero framing (medium shot, centred): feet below frame, face at ~y 1040
HERO = {"fx": 540, "fy": 1180, "h": 1050, "yaw": 0, "pitch": 5}
FACE_U, EYE_U, MOUTH_U, TOP_U = 0.585, 0.583, 0.521, 0.98   # model-space heights (units, figure = 0.98)


def r3(x):
    s = f"{x:.3f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def js(d):
    def fix(v):
        if isinstance(v, float):
            return float(r3(v))
        if isinstance(v, dict):
            return {k: fix(x) for k, x in v.items()}
        if isinstance(v, list):
            return [fix(x) for x in v]
        return v
    return json.dumps(fix(d), ensure_ascii=False)


def scr(view, u, ux=0.0):
    """screen position of a model point at height u (units) for a view (orthographic, pitch ignored)."""
    k = view["h"] / 0.98
    return view["fx"] + ux * k, view["fy"] - u * k


def clip_rect(x, y, w, h, r=0):
    """#m-clip clip-path for a screen rectangle (canvas = 1080x1080)."""
    return f"inset({r3(y)}px {r3(1080 - x - w)}px {r3(1080 - y - h)}px {r3(x)}px round {r3(r)}px)"


CLIP_NONE = clip_rect(-400, -400, 1880, 1880, 0)


def clip_circle(cx, cy, d):
    return clip_rect(cx - d / 2, cy - d / 2, d, d, d / 2)


class Rng:
    def __init__(self, seed):
        self.s = seed & 0x7FFFFFFF or 1
    def f(self):
        self.s = (1103515245 * self.s + 12345) & 0x7FFFFFFF
        return self.s / 0x7FFFFFFF
    def u(self, a, b):
        return a + (b - a) * self.f()


class Scene:
    def __init__(self, sid):
        meta = next(s for s in SCENES["scenes"] if s["id"] == sid)
        self.meta = meta
        self.id, self.t0, self.t1 = sid, meta["start"], meta["end"]
        self.host0 = 0.0 if self.t0 <= 0 else round(self.t0 - 0.001, 4)
        self.back, self.front, self.css = [], [], []
        self._init, self._tl, self.mtrack = [], [], []
        self.persp = 1600
        self.persp_origin = (540, 540)
        self.sfx = []          # (t, name, vol)
        self.acting = {}       # track -> [(t, value, dur)]

    # ---------------------------------------------------------------- time
    def L(self, t):
        return max(0.0, t - self.host0)
    @property
    def dur(self):
        return self.t1 - self.host0

    # ---------------------------------------------------------------- scene tweens
    def init(self, sel, props):
        self._init.append((sel, f"gsap.set({json.dumps(sel)}, {js(props)});"))
    def ft(self, sel, frm, to, at, dur, ease="power2.out"):
        to = dict(to, duration=max(0.01, dur), ease=ease, immediateRender=False)
        self._tl.append((sel, f"tl.fromTo({json.dumps(sel)}, {js(frm)}, {js(to)}, {r3(self.L(at))});"))
    def tset(self, sel, props, at):
        self._tl.append((sel, f"tl.set({json.dumps(sel)}, {js(props)}, {r3(self.L(at))});"))
    def keys(self, sel, keys):
        t_prev, p_prev = keys[0][0], dict(keys[0][1])
        self.init(sel, p_prev)
        for t, p, ease in keys[1:]:
            full = dict(p_prev); full.update(p)
            self.ft(sel, p_prev, full, t_prev, max(0.01, t - t_prev), ease)
            t_prev, p_prev = t, full
    def cam(self, keys):
        self.keys(f"#{self.id}-cam", keys)
    def fx(self, t, name, vol=None):
        self.sfx.append((t, name, vol))

    # ---------------------------------------------------------------- mascot track (global time)
    def _mkeys(self, target, keys):
        t_prev, p_prev = keys[0][0], dict(keys[0][1])
        tgt = target if target == "V" else json.dumps(target)
        self.mtrack.append(f"vt.set({tgt}, {js(p_prev)}, {r3(max(self.t0, t_prev))});")
        for t, p, ease in keys[1:]:
            full = dict(p_prev); full.update(p)
            to = dict(full, duration=max(0.01, t - t_prev), ease=ease or "none", immediateRender=False)
            self.mtrack.append(f"vt.fromTo({tgt}, {js(p_prev)}, {js(to)}, {r3(t_prev)});")
            t_prev, p_prev = t, full
    def mv(self, keys):
        self._mkeys("V", keys)
    def mx(self, keys):
        self._mkeys("#m-xf", keys)
    def mc(self, keys):
        self._mkeys("#m-clip", keys)
    def act(self, track, keys):
        """mascot acting keys (global time). track: armL (screen-right arm) | armR (screen-left arm) | head [rx,ry,rz]
        | torso {spine/chest/hips: [x,y,z]} | root {y, ry, rz, x, s}. keys = [(t, value, transition_dur)].
        Arm poses: rest low explain explainHi together palmUp open point pointUp present stop wave chin shrug fist
        (armL 'point' points screen-right, armR 'point' points screen-left). Head ry > 0 turns toward screen-right.
        Scenes without keys for a track get an automatic talk pattern from the VO words."""
        self.acting.setdefault(track, []).extend([(float(t), v, float(d)) for t, v, d in keys])
    def mset(self, sel, props, at):
        tgt = sel if sel == "V" else json.dumps(sel)
        self.mtrack.append(f"vt.set({tgt}, {js(props)}, {r3(at)});")

    # ---------------------------------------------------------------- write
    def _doc(self, cid, html, lines, inits, cam_id):
        ox, oy = self.persp_origin
        return f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; }}
    #{cid}-persp {{ perspective: {self.persp}px; perspective-origin: {ox}px {oy}px; }}
    {chr(10).join('    ' + c for c in self.css).strip()}
  </style>
  <div id="root" class="fx-root" data-composition-id="{cid}" data-width="1080" data-height="1080">
    <div class="fx-persp" id="{cid}-persp" data-layout-ignore>
      <div class="fx-cam" id="{cam_id}" data-layout-ignore>
{chr(10).join('        ' + h for h in html)}
      </div>
    </div>
  </div>
  <script>
    (function () {{
      // generated by tools/build_scenes.py from tools/scenes/{self.id}.py - local time 0 = {r3(self.host0)} s
      const tl = gsap.timeline({{ paused: true }});
      {(chr(10) + '      ').join(inits)}
      {(chr(10) + '      ').join(lines)}
      tl.set({{}}, {{}}, {r3(self.dur - 0.004)});
      window.__timelines = window.__timelines || {{}};
      window.__timelines["{cid}"] = tl;
    }})();
  </script>
</template>
"""

    def write(self):
        sid = self.id
        idre = re.compile(r'id="([^"]+)"')
        back_ids = set(idre.findall("".join(self.back)))
        front_ids = set(idre.findall("".join(self.front)))
        cam = f"#{sid}-cam"

        def route(items, front):
            out = []
            for sel, line in items:
                if sel == cam:
                    out.append(line.replace(json.dumps(cam), json.dumps(f"#{sid}f-cam")) if front else line)
                    continue
                key = sel.lstrip("#").split(" ")[0]
                if front and key in front_ids:
                    out.append(line)
                elif not front and key not in front_ids:
                    if key not in back_ids:
                        raise ValueError(f"{sid}: selector {sel} not found in back or front")
                    out.append(line)
            return out
        (P / f"compositions/{sid}.html").write_text(self._doc(sid, self.back, route(self._tl, False), route(self._init, False), f"{sid}-cam"))
        (P / f"compositions/{sid}f.html").write_text(self._doc(f"{sid}f", self.front, route(self._tl, True), route(self._init, True), f"{sid}f-cam"))
        (P / f"production/mtrack/{sid}.js").write_text("\n".join(self.mtrack) + "\n")
        (P / f"production/sfx/{sid}.json").write_text(json.dumps(self.sfx))
        (P / f"production/acting/{sid}.json").write_text(json.dumps(self.acting))


# ======================================================================= HTML helpers
def box(x, y, w, h):
    return f"left:{r3(x)}px;top:{r3(y)}px;width:{r3(w)}px;height:{r3(h)}px;"


def el(id_, x, y, w, h, cls="abs", style="", inner=""):
    i = f' id="{id_}"' if id_ else ""
    return f'<div{i} class="{cls}" style="{box(x, y, w, h)}{style}">{inner}</div>'


def txt(id_, x, y, w, text, size=44, weight=700, color="#fff", align="left", style="", lh=1.15):
    i = f' id="{id_}"' if id_ else ""
    return (f'<div{i} class="abs" style="left:{r3(x)}px;top:{r3(y)}px;width:{r3(w)}px;font:{weight} {size}px/{lh} Poppins, sans-serif;'
            f'color:{color};text-align:{align};{style}">{text}</div>')


def shadow(x, y, w, h, op=0.6, id_=None):
    i = f' id="{id_}"' if id_ else ""
    return f'<div{i} class="abs cshadow" style="{box(x, y, w, h)}opacity:{op}"></div>'


def apex(S, layer, id_, x, y, at, size=520, ring=True, sparks=0, seed=7, op=0.7):
    """one controlled cyan-white light burst (+ ring + seeded sparks) centred at (x, y). Use only on hero apexes."""
    layer.append(f'<div class="abs bloom" id="{id_}-bl" style="{box(x - size / 2, y - size / 2, size, size)}"></div>')
    S.init(f"#{id_}-bl", {"opacity": 0, "scale": 0.3})
    S.ft(f"#{id_}-bl", {"opacity": 0, "scale": 0.3}, {"opacity": op, "scale": 0.9}, at - 0.06, 0.12, "power2.in")
    S.ft(f"#{id_}-bl", {"opacity": op, "scale": 0.9}, {"opacity": 0, "scale": 1.3}, at + 0.06, 0.42, "power2.out")
    if ring:
        rs = size * 0.42
        layer.append(f'<div class="abs ringfx" id="{id_}-rg" style="{box(x - rs / 2, y - rs / 2, rs, rs)}"></div>')
        S.init(f"#{id_}-rg", {"opacity": 0, "scale": 0.3})
        S.ft(f"#{id_}-rg", {"opacity": 0.9, "scale": 0.3}, {"opacity": 0, "scale": 2.3}, at, 0.5, "power3.out")
    R = Rng(seed)
    for k in range(sparks):
        ang = 2 * math.pi * (k + R.u(0, 0.6)) / sparks
        dist = R.u(size * 0.22, size * 0.42)
        sid = f"{id_}-sp{k}"
        layer.append(f'<div class="abs spark" id="{sid}" style="left:{r3(x - 6)}px;top:{r3(y - 6)}px"></div>')
        a = {"opacity": 0, "x": 0, "y": 0, "scale": 0.2}
        b = {"opacity": 1, "x": r3(dist * math.cos(ang) * 0.6), "y": r3(dist * math.sin(ang) * 0.6), "scale": 1}
        c = {"opacity": 0, "x": r3(dist * math.cos(ang)), "y": r3(dist * math.sin(ang)), "scale": 0.3}
        S.init(f"#{sid}", a)
        S.ft(f"#{sid}", a, b, at + 0.02, 0.2, "power3.out")
        S.ft(f"#{sid}", b, c, at + 0.22, 0.36, "power2.in")


CHECK_SVG = ('<svg viewBox="0 0 24 24" style="position:absolute;left:0;top:0;width:100%;height:100%;overflow:visible">'
             '<path d="M5 12.5 L10 17.5 L19 7" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" '
             'pathLength="1" stroke-dasharray="1" stroke-dashoffset="{o}" id="{id}"/></svg>')


def check_svg(id_, color=CYAN, width=3.2, drawn=False):
    return CHECK_SVG.format(c=color, w=width, o=0 if drawn else 1, id=id_)



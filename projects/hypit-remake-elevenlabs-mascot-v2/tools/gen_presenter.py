"""Generates the presenter-mode pop-up layers (compositions/p1.html, p2.html, p4.html, p5.html).

Each layer sits between the blurred stage (z 10) and the 3D mascot (z 40). Times in the specs are
GLOBAL seconds (same clock as production/word_timing.json); L() converts them to local time.
Only Freddie's supplied elements + abstract icons are used; no new on-screen text.
"""
import json, math, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
_WT = json.loads((P / "production/word_timing.json").read_text())["words"]
def W(i): return _WT[i]["start"]  # measured VO word start (v4)
WIN = {w["id"]: w for w in json.loads((P / "tools/presenter_windows.json").read_text())}

ICONS = {  # simple navy line icons (24x24 viewBox)
    "film": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3 9h18M3 15h18M7.5 5v4M12 5v4M16.5 5v4M7.5 15v4M12 15v4M16.5 15v4"/>',
    "music": '<path d="M9 18V6l11-2v12"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="17.5" cy="16" r="2.5"/>',
    "image": '<rect x="3" y="4" width="18" height="16" rx="2.5"/><circle cx="9" cy="9.5" r="1.8"/><path d="M4 18l5.5-5.5 4 4 2.5-2.5 4 4"/>',
    "code": '<path d="M8.5 7L3.5 12l5 5M15.5 7l5 5-5 5M13.5 5l-3 14"/>',
    "link": '<path d="M10 14a4.5 4.5 0 0 0 6.4 0l3-3a4.5 4.5 0 0 0-6.4-6.4l-1.2 1.2"/><path d="M14 10a4.5 4.5 0 0 0-6.4 0l-3 3a4.5 4.5 0 0 0 6.4 6.4l1.2-1.2"/>',
    "doc": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 11h6M9 14.5h6M9 18h4"/>',
    "no": '<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
}

CSS = """
    #root { position: absolute; inset: 0; pointer-events: none; overflow: hidden; }
    .veil { position: absolute; inset: 0; background: radial-gradient(ellipse 62% 46% at 52% 74%, rgba(255,255,255,.55), rgba(255,255,255,0) 72%),
      linear-gradient(180deg, rgba(247,250,255,.18), rgba(247,250,255,.30)); }
    .pe { position: absolute; transform-origin: 50% 50%; }
    .fl { position: relative; width: 100%; height: 100%; }
    .pe img { position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: contain; }
    .shadow { filter: drop-shadow(0 26px 34px rgba(10,13,44,.26)); }
    .chip { position: absolute; inset: 0; border-radius: 36px; background: linear-gradient(160deg, rgba(255,255,255,.95), rgba(220,232,246,.92));
      border: 2px solid #ffffff; box-shadow: 0 22px 44px rgba(10,13,44,.20), inset 0 -6px 14px rgba(39,73,118,.10); }
    .chip svg { position: absolute; left: 22%; top: 22%; width: 56%; height: 56%; fill: none; stroke: #1b2f57; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
    .chip.dark { background: linear-gradient(105deg, #0a0d2c 0%, #294b77 100%); border-color: rgba(220,232,246,.6); }
    .chip.dark svg { stroke: #ffffff; }
    .ring { position: absolute; width: 200px; height: 200px; margin: -100px 0 0 -100px; border-radius: 50%; border: 6px solid #ffffff;
      box-shadow: 0 0 30px rgba(120,160,220,.9), inset 0 0 20px rgba(120,160,220,.6); }
    .spk { position: absolute; width: 34px; height: 34px; margin: -17px 0 0 -17px; background: #ffffff;
      clip-path: polygon(50% 0, 61% 39%, 100% 50%, 61% 61%, 50% 100%, 39% 61%, 0 50%, 39% 39%); filter: drop-shadow(0 0 8px rgba(110,150,215,.95)); }
    .ghframe { position: absolute; inset: 0; border-radius: 22px; box-shadow: inset 0 0 0 3px rgba(255,255,255,.75); }
    #p5-gh img { border-radius: 22px; object-fit: cover; }
    .scan { position: absolute; top: -10%; width: 26%; height: 120%; left: -30%;
      background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,.85), rgba(255,255,255,0)); }
"""


def icon(name):
    return f'<svg viewBox="0 0 24 24">{ICONS[name]}</svg>'


class Layer:
    def __init__(self, wid, start, end):
        self.id, self.start, self.end = wid, start, end
        self.html, self.init, self.tl = [], [], []

    def L(self, g):
        return round(g - self.start, 3)

    # ---- markup
    def img(self, eid, src, x, y, w, h, cls="shadow", extra=""):
        self.html.append(f'<div class="pe {cls}" id="{eid}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
                         f'<div class="fl" id="{eid}-f"><img src="{src}" alt="" />{extra}</div></div>')
        self.init.append(f'gsap.set("#{eid}", {{ opacity: 0, scale: 0.2 }});')

    def chip(self, eid, name, x, y, s=150, dark=False):
        self.html.append(f'<div class="pe" id="{eid}" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px">'
                         f'<div class="fl" id="{eid}-f"><div class="chip{" dark" if dark else ""}">{icon(name)}</div></div></div>')
        self.init.append(f'gsap.set("#{eid}", {{ opacity: 0, scale: 0.2 }});')

    def cursor(self, eid, w=130):
        self.html.append(f'<div class="pe" id="{eid}" style="left:0;top:0;width:{w}px;height:{round(w * 411 / 409)}px;transform-origin:5% 3%">'
                         f'<img src="assets/elements/ref6_pixel_cursor.png" alt="" style="filter:drop-shadow(0 10px 12px rgba(10,13,44,.35))" /></div>')
        self.init.append(f'gsap.set("#{eid}", {{ opacity: 0, x: 1200, y: 1300 }});')

    def burst(self, eid, x, y, g, n=6, r=150):
        self.html.append(f'<div class="ring" id="{eid}-r" style="left:{x}px;top:{y}px"></div>')
        self.init.append(f'gsap.set("#{eid}-r", {{ opacity: 0, scale: 0.3 }});')
        self.tl.append(f'tl.fromTo("#{eid}-r", {{ opacity: 0.95, scale: 0.3 }}, {{ opacity: 0, scale: 2.1, duration: 0.5, ease: "power3.out", immediateRender: false }}, {self.L(g)});')
        for k in range(n):
            ang = (k / n) * 2 * math.pi + 0.35
            rr = r * (1 if k % 2 == 0 else 0.72)
            self.html.append(f'<div class="spk" id="{eid}-s{k}" style="left:{x}px;top:{y}px"></div>')
            self.init.append(f'gsap.set("#{eid}-s{k}", {{ opacity: 0, scale: 0 }});')
            self.tl.append(f'tl.fromTo("#{eid}-s{k}", {{ x: 0, y: 0, scale: 0.2, opacity: 1, rotation: 0 }}, {{ x: {round(math.cos(ang) * rr)}, y: {round(math.sin(ang) * rr)}, scale: {1.1 if k % 2 == 0 else 0.7}, opacity: 0, rotation: 90, duration: 0.55, ease: "power2.out", immediateRender: false }}, {self.L(g + 0.02)});')

    # ---- motion
    def pop(self, eid, g, rot=0, rot0=-10, d=0.45, float_amp=10, float_until=None):
        self.tl.append(f'tl.fromTo("#{eid}", {{ opacity: 0, scale: 0.2, rotation: {rot0}, y: 40 }}, {{ opacity: 1, scale: 1, rotation: {rot}, y: 0, duration: {d}, ease: "back.out(2.2)", immediateRender: false }}, {self.L(g)});')
        if float_amp:
            t0 = g + d
            t1 = float_until if float_until else self.end - 0.3
            n = max(1, int((t1 - t0) / 0.9))
            self.tl.append(f'tl.fromTo("#{eid}-f", {{ y: 0 }}, {{ y: {-float_amp}, duration: {round((t1 - t0) / n, 3)}, ease: "sine.inOut", yoyo: true, repeat: {n - 1}, immediateRender: false }}, {self.L(t0)});')

    def pop3d(self, eid, g, side="L", ry=10, rx=6, d=0.7, float_amp=8, float_until=None):
        """reference-style entrance: card swings in on a 3D hinge from off-axis, racks focus (blur -> sharp)."""
        y0 = -72 if side == "L" else 72
        x0 = -160 if side == "L" else 160
        self.tl.append(f'tl.fromTo("#{eid}", {{ opacity: 0, rotationY: {y0}, rotationX: 18, x: {x0}, scale: 0.72, filter: "blur(16px)", transformPerspective: 1100 }}, '
                       f'{{ opacity: 1, rotationY: {ry if side == "L" else -ry}, rotationX: {rx}, x: 0, scale: 1, filter: "blur(0px)", transformPerspective: 1100, duration: {d}, ease: "expo.out", immediateRender: false }}, {self.L(g)});')
        if float_amp:
            t0 = g + d
            t1 = float_until if float_until else self.end - 0.3
            n = max(1, int((t1 - t0) / 1.1))
            self.tl.append(f'tl.fromTo("#{eid}-f", {{ y: 0, rotation: 0 }}, {{ y: {-float_amp}, rotation: 1.2, duration: {round((t1 - t0) / n, 3)}, ease: "sine.inOut", yoyo: true, repeat: {n - 1}, immediateRender: false }}, {self.L(t0)});')

    def flyout(self, ids, g, side="R", d=0.32, ry=0):
        sx = 900 if side == "R" else -900
        self.tl.append(f'tl.fromTo([{", ".join(repr("#" + i) for i in ids)}], {{ opacity: 1, x: 0, filter: "blur(0px)" }}, '
                       f'{{ opacity: 0, x: {sx}, rotationY: {50 if side == "R" else -50}, filter: "blur(18px)", transformPerspective: 1100, duration: {d}, ease: "power3.in", immediateRender: false }}, {self.L(g)});')

    def punch(self, eid, g, s=1.1):
        self.tl.append(f'tl.fromTo("#{eid}-f", {{ scale: 1 }}, {{ scale: {s}, duration: 0.12, ease: "power2.out", immediateRender: false, yoyo: true, repeat: 1 }}, {self.L(g)});')

    def click(self, eid, tx, ty, g, frm=(1150, 1350), leave=None):
        """cursor flies in so its fingertip lands on (tx, ty) at global g, then clicks."""
        x, y = tx - 7, ty - 4
        self.tl.append(f'tl.fromTo("#{eid}", {{ opacity: 0, x: {frm[0]}, y: {frm[1]}, rotation: 18 }}, {{ opacity: 1, x: {x}, y: {y}, rotation: 0, duration: 0.42, ease: "power3.out", immediateRender: false }}, {self.L(g - 0.45)});')
        self.tl.append(f'tl.fromTo("#{eid}", {{ scale: 1 }}, {{ scale: 0.82, duration: 0.07, ease: "power2.in", yoyo: true, repeat: 1, immediateRender: false }}, {self.L(g - 0.03)});')
        if leave:
            self.tl.append(f'tl.fromTo("#{eid}", {{ opacity: 1, x: {x}, y: {y} }}, {{ opacity: 0, x: {x + 160}, y: {y + 220}, duration: 0.35, ease: "power2.in", immediateRender: false }}, {self.L(leave)});')

    def raw(self, js):
        self.tl.append(js)

    def exit(self, ids, g, d=0.27, kind="zoom"):
        sel = ", ".join("#" + i for i in ids)
        if kind == "zoom":
            self.tl.append(f'tl.fromTo([{", ".join(repr("#" + i) for i in ids)}], {{ opacity: 1, scale: 1 }}, {{ opacity: 0, scale: 1.6, duration: {d}, ease: "power3.in", immediateRender: false }}, {self.L(g)});')
        else:
            self.tl.append(f'tl.fromTo([{", ".join(repr("#" + i) for i in ids)}], {{ opacity: 1, scale: 1 }}, {{ opacity: 0, scale: 0.3, duration: {d}, ease: "power2.in", immediateRender: false }}, {self.L(g)});')

    veil_in = None
    veil_out = None

    def veil_js(self):
        if self.veil_in is None:
            return ""
        return (f'tl.fromTo("#{self.id}-veil", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: "power2.out", immediateRender: false }}, {self.L(self.veil_in)});\n'
                f'      tl.fromTo("#{self.id}-veil", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.35, ease: "power2.in", immediateRender: false }}, {self.L(self.veil_out)});')

    def write(self):
        dur = round(self.end - self.start, 3)
        out = f"""<template>
  <style>{CSS}
  </style>
  <div id="root" data-composition-id="{self.id}" data-width="1080" data-height="1920">
    <div class="veil" id="{self.id}-veil" data-layout-ignore></div>
    {chr(10).join("    " + h for h in self.html).strip()}
  </div>
  <script>
    (function () {{
      // Presenter pop-up layer — generated by tools/gen_presenter.py (global {self.start}–{self.end}s).
      gsap.set("#{self.id}-veil", {{ opacity: 0 }});
      {chr(10).join("      " + s for s in self.init).strip()}
      const tl = gsap.timeline({{ paused: true }});
      {self.veil_js()}
      {chr(10).join("      " + s for s in self.tl).strip()}
      tl.set({{}}, {{}}, {round(dur - 0.01, 3)});
      window.__timelines = window.__timelines || {{}};
      window.__timelines["{self.id}"] = tl;
    }})();
  </script>
</template>
"""
        (P / f"compositions/{self.id}.html").write_text(out)
        return self.id


PLAYER = "assets/elements/ref5_player_phone.png"
FILM = "assets/elements/ref12_film_strip.png"        # halftone film strip (869x876)
CLAP = "assets/elements/ref13_clapper_halftone.png"  # halftone clapper (768x855)
CAM = "assets/elements/ref14_camera_halftone.png"    # halftone camera in hand (876x742)
GH_LOGO = "assets/elements/ref11_github_logo.png"   # GitHub mark tile (272x272)
GH_HOME = "assets/elements/ref10_github_home.jpg"   # GitHub home page (1400x656)
built = []

# ------------------------------------------------------------------ P1 0–4.2 (intro)
w = WIN["P1"]; p = Layer("p1", w["host0"], w["host1"]); p.veil_in, p.veil_out = 1.25, 3.93
# glass-arch stage card (Freddie's ref8): he comes forward out of it, the camera pushes through it
p.html.append('<div class="pe" id="p1-arch" style="left:40px;top:430px;width:1000px;height:1440px;border-radius:56px;overflow:hidden;transform-origin:500px 1090px;'
              'box-shadow:0 40px 80px rgba(10,13,44,.28)"><img src="assets/elements/ref8_glass_arches.jpg" alt="" style="position:absolute;left:0;top:0;width:100%;height:100%;object-fit:cover;object-position:14% 50%" /></div>')
p.init.append('gsap.set("#p1-arch", { opacity: 1, scale: 1 });')
p.raw('tl.fromTo("#p1-arch", { scale: 1 }, { scale: 1.08, duration: 1.0, ease: "power1.inOut", immediateRender: false }, 0.1);')
p.raw('tl.fromTo("#p1-arch", { scale: 1.08, opacity: 1, filter: "blur(0px)" }, { scale: 1.5, opacity: 0, filter: "blur(16px)", duration: 0.45, ease: "power2.in", immediateRender: false }, 1.1);')
# "format" -> halftone film strip swings in on the right
p.img("p1-film", FILM, 640, 420, 400, 403)
p.pop3d("p1-film", W(4) - 0.06, side="R", float_until=2.7)
# "video" -> phone player swings in on the left, "viral" pulse
p.img("p1-player", PLAYER, 30, 470, 470, 350, extra='<div class="scan" id="p1-scan"></div>')
p.init.append('gsap.set("#p1-scan", { x: 0, opacity: 0 });')
p.pop3d("p1-player", W(5) - 0.08, side="L", float_until=3.0)
p.burst("p1-b1", 30 + 238, 470 + 96, W(6) + 0.05, r=120)
# "sampai" -> film strip leaves, the clapper snaps in for "efek"
p.flyout(["p1-film"], W(7) - 0.05, side="R")
p.img("p1-clap", CLAP, 650, 430, 340, 378)
p.tl.append(f'tl.fromTo("#p1-clap", {{ opacity: 0, rotation: -38, scale: 0.6, x: 120 }}, {{ opacity: 1, rotation: 6, scale: 1, x: 0, duration: 0.42, ease: "back.out(2.4)", immediateRender: false }}, {p.L(W(8) - 0.3)});')
p.tl.append(f'tl.fromTo("#p1-clap-f", {{ filter: "blur(12px)" }}, {{ filter: "blur(0px)", duration: 0.3, ease: "power2.out", immediateRender: false }}, {p.L(W(8) - 0.3)});')
p.tl.append(f'tl.fromTo("#p1-clap-f", {{ rotation: 0 }}, {{ rotation: -9, duration: 0.07, ease: "power3.in", yoyo: true, repeat: 1, immediateRender: false }}, {p.L(W(8))});')
p.cursor("p1-cur")
p.click("p1-cur", 30 + 238, 470 + 96, W(8), leave=3.6)
p.burst("p1-b2", 30 + 238, 470 + 96, W(8))
p.punch("p1-player", W(8), 1.08)
p.raw(f'tl.fromTo("#p1-scan", {{ x: 0, opacity: 1 }}, {{ x: 640, opacity: 1, duration: 0.3, ease: "power2.inOut", immediateRender: false }}, {p.L(W(8) + 0.05)});')
p.raw(f'tl.fromTo("#p1-scan", {{ x: 0, opacity: 1 }}, {{ x: 640, opacity: 1, duration: 0.4, ease: "power2.inOut", immediateRender: false }}, {p.L(W(10))});')
p.exit(["p1-player", "p1-clap"], 3.93)
built.append(p.write())

# ------------------------------------------------------------------ P2 9.05–13.8 (reference video → coding agent)
w = WIN["P2"]; p = Layer("p2", w["host0"], w["host1"]); p.veil_in, p.veil_out = 9.1, 13.5
# content of this window = Smart Motion Director chat takeover (compositions/director.html)
built.append(p.write())

# ------------------------------------------------------------------ P4 40.6–46.867 (rights)
w = WIN["P4"]; p = Layer("p4", w["host0"], w["host1"]); p.veil_in, p.veil_out = 40.7, 46.6
p.img("p4-card", PLAYER, 40, 470, 440, 328)
p.pop3d("p4-card", W(98) - 0.12, side="L", float_amp=0)
p.chip("p4-no", "no", 180, 520, 170, dark=True)
p.raw('tl.fromTo("#p4-no", { opacity: 0, scale: 1.8, rotation: -30 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.3, ease: "back.out(2.5)", immediateRender: false }, ' + str(p.L(W(99) + 0.02)) + ');')
p.raw('tl.fromTo("#p4-card-f", { x: 0 }, { x: 12, duration: 0.05, ease: "none", yoyo: true, repeat: 5, immediateRender: false }, ' + str(p.L(W(99) + 0.08)) + ');')
p.flyout(["p4-card", "p4-no"], 42.85, side="L")
p.img("p4-cam", CAM, 40, 470, 330, 280)
p.pop3d("p4-cam", W(101) - 0.1, side="L", float_until=45.3)
for k, (name, g) in enumerate([("music", W(102)), ("image", W(104))]):
    p.chip(f"p4-c{k}", name, 400 + k * 190, 500, 150)
    p.pop(f"p4-c{k}", g - 0.06, rot=(4, -3)[k], rot0=-20, float_until=45.3)
p.img("p4-folder", "assets/elements/ref7_folder_shield.png", 590, 440, 450, 389)
p.pop3d("p4-folder", W(106) - 0.15, side="R")
# the assets drop into the protected folder
for k, sel in enumerate(["p4-cam", "p4-c0", "p4-c1"]):
    x0 = [40 + 165, 400 + 75, 590 + 75][k]
    p.raw(f'tl.fromTo("#{sel}", {{ x: 0, y: 0, scale: 1, opacity: 1 }}, {{ x: {815 - x0}, y: 170, scale: 0.22, opacity: 0, duration: 0.42, ease: "power2.in", immediateRender: false }}, {p.L(W(107) + k * 0.09)});')
p.punch("p4-folder", W(108), 1.1)
p.burst("p4-b1", 900, 690, W(108), r=190)
p.exit(["p4-folder"], 46.6)
built.append(p.write())

# ------------------------------------------------------------------ P5 56.6–58.733 (link + repo + guide question)
w = WIN["P5"]; p = Layer("p5", w["host0"], w["host1"]); p.veil_in, p.veil_out = 56.7, 58.45
p.chip("p5-link", "link", 60, 760, 150, dark=True)
p.pop("p5-link", W(135) - 0.06, rot=-6, rot0=-24)
p.img("p5-gh", GH_HOME, 150, 430, 860, 403, cls="shadow", extra='<div class="ghframe"></div>')
p.pop3d("p5-gh", W(136) - 0.1, side="R", ry=12, rx=8)
p.chip("p5-doc", "doc", 880, 770, 150)
p.pop("p5-doc", W(138) - 0.06, rot=5, rot0=-18)
p.cursor("p5-cur")
p.click("p5-cur", 135, 835, W(139) + 0.05)
p.burst("p5-b1", 135, 835, W(139) + 0.05, r=130)
p.exit(["p5-link", "p5-gh", "p5-doc", "p5-cur"], 58.47, kind="shrink")
built.append(p.write())

print("presenter layers:", built)

"""X-ray of a real Reel: a porcelain phone playing our own Hypit Reel, whose screen comes apart into the layers the
Reel was actually built from (rendered separately from projects/hypit-remake-elevenlabs-mascot-v2 at t = 5.3 s,
difference-matted: tools/assets_reel_layers.py). Shared by S01 and S02."""
from xk import box, r3

SW, SH = 486, 864                      # screen (9:16)
BZ = 22                                # bezel
PW, PH = SW + 2 * BZ, SH + 2 * BZ
PX, PY = 575 - PW / 2, 474             # phone front plate at z = 0 (screen space)
LAYERS = [("bg", "bg_540.png"), ("scene", "scene_540.png"), ("mascot", "mascot_540.png"), ("cap", "cap_540.png")]


def reels_ui(pre):
    """Reels-app chrome as a transparent layer: right action column + progress bar (icons only, no text)."""
    ico = lambda d, y: (f'<svg style="position:absolute;left:{SW - 62}px;top:{y}px;width:42px;height:42px;overflow:visible" viewBox="0 0 24 24">'
                        f'<path d="{d}" fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" '
                        f'style="filter:drop-shadow(0 1px 2px rgba(0,0,0,.35))"/></svg>')
    heart = "M12 20 C5 15 3 12 3 8.5 A4.5 4.5 0 0 1 12 6 A4.5 4.5 0 0 1 21 8.5 C21 12 19 15 12 20 Z"
    bubble = "M4 12 A8 8 0 1 1 8 19 L3.5 20.5 L5 16.5 A8 8 0 0 1 4 12 Z"
    plane = "M21 3 L10 14 M21 3 L14.5 21 L10 14 L3 10.5 Z"
    mark = "M6 3 H18 V21 L12 16.5 L6 21 Z"
    return (f'<div class="abs" id="{pre}-ui" style="{box(0, 0, SW, SH)}">'
            + ico(heart, 470) + ico(bubble, 540) + ico(plane, 610) + ico(mark, 680)
            + f'<div class="abs" style="{box(18, SH - 20, SW - 36, 4)}border-radius:2px;background:rgba(255,255,255,.35)"></div>'
            + f'<div class="abs" id="{pre}-prog" style="{box(18, SH - 20, SW - 36, 4)}border-radius:2px;background:#fff"></div>'
            + f'<div class="abs" style="{box(18, SH - 120, 46, 46)}border-radius:23px;background:linear-gradient(135deg,#3a6299,#1c3354);border:2px solid #fff"></div>'
            + f'<div class="abs" style="{box(74, SH - 108, 150, 10)}border-radius:5px;background:rgba(255,255,255,.9)"></div>'
            + f'<div class="abs" style="{box(74, SH - 88, 220, 8)}border-radius:4px;background:rgba(255,255,255,.6)"></div>'
            + "</div>")


def phone(pre, video=False):
    """phone markup (local coords, origin = phone top-left). Layer stack ids: {pre}-L<name>, glass {pre}-glass."""
    out = []
    for k in range(10, 0, -1):            # navy sidewall (thickness)
        c = "#0f1c30" if k > 6 else "#1c3354" if k > 2 else "#294b77"
        out.append(f'<div class="abs" style="{box(0, 0, PW, PH)}border-radius:66px;background:{c};transform:translateZ({-k * 3}px)"></div>')
    out.append(f'<div class="abs" id="{pre}-body" style="{box(0, 0, PW, PH)}border-radius:66px;background:linear-gradient(150deg,#4a72a8,#294b77 40%,#1c3354 85%);'
               f'box-shadow:inset 3px 3px 0 rgba(255,255,255,.35),inset -2px -3px 0 rgba(15,28,48,.6),0 30px 60px -20px rgba(28,51,84,.55)"></div>')
    out.append(f'<div class="abs" style="{box(BZ - 3, BZ - 3, SW + 6, SH + 6)}border-radius:46px;background:#0f1c30;transform:translateZ(-2px)"></div>')
    for (y, h) in ((210, 90), (320, 60)):  # side buttons
        out.append(f'<div class="abs" style="{box(PW - 3, y, 7, h)}border-radius:4px;background:linear-gradient(90deg,#dbe6f6,#9fb6d6)"></div>')
    # the layer stack (each layer is the full screen; separated later along Z)
    st = []
    for name, f in LAYERS:
        st.append(f'<div class="abs p3" id="{pre}-L{name}" style="{box(0, 0, SW, SH)}">'
                  f'<img src="assets/elements/xray/reel/{f}" alt="" style="position:absolute;left:0;top:0;width:{SW}px;height:{SH}px" />'
                  f'<div class="abs" id="{pre}-E{name}" style="{box(-3, -3, SW + 6, SH + 6)}border-radius:30px;border:3px solid #294b77;box-shadow:0 0 14px rgba(172,198,231,.9)"></div></div>')
    st.append(f'<div class="abs p3" id="{pre}-Lui" style="{box(0, 0, SW, SH)}">{reels_ui(pre)}</div>')
    if video:
        st.append(f'<video id="{pre}-vid" class="clip" src="assets/elements/xray/reel/hypit_clip.mp4" muted playsinline data-start="0" '
                  f'data-duration="1.9" data-media-start="0" style="position:absolute;left:0;top:0;width:{SW}px;height:{SH}px;object-fit:cover"></video>')
    out.append(f'<div class="abs p3" id="{pre}-stack" style="{box(BZ, BZ, SW, SH)}border-radius:44px">{"".join(st)}</div>')
    # glass
    out.append(f'<div class="abs" id="{pre}-glass" style="{box(BZ - 2, BZ - 2, SW + 4, SH + 4)}border-radius:46px;'
               f'background:linear-gradient(125deg,rgba(255,255,255,.28),rgba(255,255,255,0) 38%,rgba(255,255,255,0) 70%,rgba(203,219,244,.18));'
               f'border:2px solid rgba(255,255,255,.75);box-shadow:inset 0 0 0 1px rgba(41,75,119,.25)">'
               f'<div class="abs" style="{box(SW / 2 - 60, 16, 120, 30)}border-radius:15px;background:#0f1c30"></div>'
               f'<div class="abs" id="{pre}-gsheen" style="{box(-240, -60, 150, SH + 120)}background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.5),rgba(255,255,255,0))"></div></div>')
    # seam lights around the screen
    for nm, b in (("t", box(BZ, BZ - 6, SW, 3)), ("b", box(BZ, BZ + SH + 3, SW, 3)), ("l", box(BZ - 6, BZ, 3, SH)), ("r", box(BZ + SW + 3, BZ, 3, SH))):
        out.append(f'<div class="abs" id="{pre}-seam{nm}" style="{b}border-radius:2px;background:#fff;box-shadow:0 0 10px 2px rgba(172,198,231,.95)"></div>')
    # four navy rods that pin the layers together ("mesin")
    for k, (x, y) in enumerate(((BZ + 26, BZ + 26), (BZ + SW - 26, BZ + 26), (BZ + 26, BZ + SH - 26), (BZ + SW - 26, BZ + SH - 26))):
        out.append(f'<div class="abs p3" id="{pre}-rod{k}" style="left:{x - 7}px;top:{y - 7}px;width:14px;height:14px">'
                   + "".join(f'<div class="abs" style="left:0;top:0;width:14px;height:14px;border-radius:7px;background:{"#1c3354" if j % 2 else "#3a6299"};transform:translateZ({j * 12}px)"></div>' for j in range(0, 30))
                   + "</div>")
    return "".join(out)

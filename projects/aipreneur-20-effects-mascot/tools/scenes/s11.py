"""S11 — 10 B-ROLL OVERLAY (20.07–23.43)  VO: "B-roll menumpuk di atas video, lalu timeline editornya terbuka."
Opens on S10's key-light rect = an editor MONITOR (smoked-glass bezel) with the live mascot playing inside it.
"B-roll menumpuk di atas video": four B-roll tiles (self-shots of our own effects) land on the video one after
another, slightly rotated, with shadows. "timeline editornya terbuka": a timeline panel unfolds under the monitor
(V2 / V1 / A1 tracks, playhead, VO waveform); the tiles drop from the monitor into the V2 track as clips and the
panel tilts back (camera over the timeline); a cursor grabs the cream "paper" clip.
Hand-off: the editor folds away, the paper clip lifts out of the timeline and lands as S12's paper floor strip,
the mascot is released from the monitor to the WIDE full-body shot (S12's first frame)."""
from xk import box, r3, CYAN, clip_rect, CLIP_NONE
from kit import WIDE, NO_FILTER, MONITOR, FLOOR_Y, paper_strip, SELF

MON_VIEW = {"fx": 540, "fy": 1458, "h": 1128, "yaw": -10, "pitch": 4}
TL = (60, 990, 960, 390)        # timeline panel (x, y, w, h) — stays above the caption band
TILES = [("orbit", 150, 340, -6), ("chat", 760, 330, 5), ("escape", 190, 600, 4), ("checks", 740, 590, -5)]
TW, TH = 180, 320
ROW = {"V2": TL[1] + 92, "V1": TL[1] + 182, "A1": TL[1] + 272}
CLIPS_V2 = [(TL[0] + 150 + k * 150, 128) for k in range(4)]      # where each tile lands in the V2 track (x, w)
PAPER = (TL[0] + 760, ROW["V2"], 150, 64)                        # the paper clip (x, y, w, h)


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W54, W55, W57, W58, W59, W60, W61, W62 = (S.W(i) for i in (54, 55, 57, 58, 59, 60, 61, 62))
    # B-roll 20.16 menumpuk 20.48 atas 20.98 video 21.20 lalu 21.64 timeline 21.88 editornya 22.28 terbuka 22.72
    mx, my, mw, mh, mr = MONITOR
    tx, ty, tw, th = TL
    out0 = t1 - 0.44                  # editor folds away
    # ---------------------------------------------------------------- back: studio glow inside the monitor, monitor body
    S.back.append(f'<div class="abs" id="{s}-amb" style="{box(0, 0, 1080, 1920)}background:radial-gradient(ellipse 60% 30% at 50% 30%,rgba(60,120,200,.35),rgba(60,120,200,0) 70%)"></div>')
    S.back.append(f'<div class="abs" id="{s}-mon" style="{box(mx, my, mw, mh)}border-radius:{mr}px;overflow:hidden;'
                  f'background:radial-gradient(ellipse 70% 60% at 50% 40%,#2a5590 0%,#132c58 55%,#0a1838 100%)">'
                  f'<div class="abs" style="{box(0, mh - 150, mw, 150)}background:radial-gradient(ellipse at 50% 0%,rgba(220,240,255,.3),rgba(220,240,255,0) 70%)"></div></div>')
    # ---------------------------------------------------------------- front: bezel, UI, B-roll tiles, timeline, cursor
    S.front.append(f'<div class="abs" id="{s}-bez" style="{box(mx - 16, my - 16, mw + 32, mh + 32)}border-radius:{mr + 14}px;'
                   f'border:16px solid #121a2c;box-shadow:inset 0 0 0 2px #8b97aa,0 0 0 2px rgba(255,255,255,.18),0 30px 60px -20px rgba(3,8,28,.9)"></div>')
    S.front.append(f'<div class="abs" id="{s}-ui" style="{box(mx, my, mw, mh)}">'
                   f'<div class="abs" style="{box(22, 18, 120, 30)}font:700 20px/30px Poppins;color:#fff;letter-spacing:.14em">'
                   f'<span style="display:inline-block;width:10px;height:10px;border-radius:5px;background:{CYAN};margin-right:8px;vertical-align:1px"></span>V1</div>'
                   f'<div class="abs" id="{s}-tc" style="{box(mw - 170, mh - 44, 150, 30)}font:400 20px/30px Poppins;color:#fff;text-align:right;letter-spacing:.08em">00:20:04</div></div>')
    for k, (nm, x, y, rot) in enumerate(TILES):
        S.front.append(f'<div class="abs" id="{s}-tile{k}" style="{box(x, y, TW, TH)}border-radius:14px;overflow:hidden;border:4px solid #fff;'
                       f'box-shadow:0 18px 30px -10px rgba(3,8,28,.85);transform:rotate({rot}deg)">'
                       f'<img src="{SELF}/{nm}.jpg" alt="" style="position:absolute;left:0;top:0;width:{TW - 8}px;height:{TH - 8}px;object-fit:cover"/>'
                       f'<div class="abs" style="{box(0, TH - 46, TW, 38)}background:linear-gradient(180deg,rgba(3,8,28,0),rgba(3,8,28,.75))"></div>'
                       f'<div class="abs" style="{box(10, TH - 40, TW - 20, 28)}font:700 15px/28px Poppins;color:#fff;letter-spacing:.1em">B-ROLL {k + 1}</div></div>')
    # timeline panel
    rows = ""
    for name, yy in ROW.items():
        ly = yy - ty
        rows += (f'<div class="abs" style="{box(18, ly, 70, 64)}border-radius:10px;background:rgba(255,255,255,.06);font:700 20px/64px Poppins;color:#fff;text-align:center">{name}</div>'
                 f'<div class="abs" style="{box(100, ly, tw - 118, 64)}border-radius:10px;background:rgba(255,255,255,.04);box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)"></div>')
    v1 = f'<div class="abs acrylic" style="{box(110, ROW["V1"] - ty + 6, tw - 140, 52)}border-radius:9px;font:700 18px/52px Poppins;color:#fff;padding-left:16px;letter-spacing:.08em">VIDEO</div>'
    wave = "".join(f'<div class="abs" style="left:{116 + k * 9}px;top:{ROW["A1"] - ty + 32 - h / 2}px;width:5px;height:{h}px;border-radius:3px;background:rgba(0,208,254,.75)"></div>'
                   for k, h in enumerate([(8 + (k * 37) % 41) for k in range(88)]))
    ruler = "".join(f'<div class="abs" style="left:{100 + k * 42}px;top:56px;width:2px;height:{14 if k % 4 == 0 else 7}px;background:rgba(255,255,255,.45)"></div>' for k in range(20))
    S.front.append(f'<div class="abs" id="{s}-tl" style="{box(tx, ty, tw, th)}">'
                   f'<div class="abs smoked" style="{box(0, 0, tw, th)}border-radius:26px"></div>'
                   f'<div class="abs" style="{box(22, 14, 400, 34)}font:700 22px/34px Poppins;color:#fff;letter-spacing:.14em">TIMELINE</div>'
                   f'{ruler}{rows}{v1}{wave}'
                   f'<div class="abs" id="{s}-ph" style="{box(130, 46, 4, th - 60)}background:{CYAN};box-shadow:0 0 10px rgba(0,208,254,.9)">'
                   f'<div class="abs" style="left:-9px;top:-6px;width:22px;height:16px;border-radius:4px;background:{CYAN}"></div></div></div>')
    # B-roll clips in V2 (appear as the tiles drop in) + the paper clip
    for k, (cx, cw) in enumerate(CLIPS_V2):
        S.front.append(f'<div class="abs" id="{s}-c{k}" style="{box(cx, ROW["V2"] + 6, cw, 52)}border-radius:9px;overflow:hidden;background:#1d3b6a;box-shadow:inset 0 0 0 2px rgba(255,255,255,.55)">'
                       + "".join(f'<img src="{SELF}/{TILES[k][0]}.jpg" alt="" style="position:absolute;left:{j * 30}px;top:0;width:30px;height:52px;object-fit:cover;opacity:.9"/>' for j in range(5)) + '</div>')
    px, py, pw, ph = PAPER
    # the paper clip IS the S12 floor strip, transformed down into the timeline slot (origin 0 0)
    S.front.append(paper_strip(f"{s}-paper", -40, FLOOR_Y - 10, 1160, 70))
    S.front.append(f'<div class="abs" id="{s}-cur" style="{box(px + 90, py + 40, 44, 44)}">'
                   f'<svg viewBox="0 0 24 24" style="position:absolute;left:0;top:0;width:44px;height:44px;overflow:visible;filter:drop-shadow(0 3px 4px rgba(3,8,28,.6))">'
                   f'<path d="M3 2 L3 19 L8 14.5 L11.5 22 L14.5 20.7 L11 13.3 L17.5 13.3 Z" fill="#fff" stroke="#0b1636" stroke-width="1.2" stroke-linejoin="round"/></svg></div>')

    # ---------------------------------------------------------------- motion
    S.init(f"#{s}-bez", {"opacity": 0, "scale": 1.04, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-bez", {"opacity": 0, "scale": 1.04}, {"opacity": 1, "scale": 1}, t0, 0.22, "power2.out")
    S.init(f"#{s}-ui", {"opacity": 0})
    S.ft(f"#{s}-ui", {"opacity": 0}, {"opacity": 1}, t0 + 0.1, 0.2, "none")
    # tiles land on the video (B-roll menumpuk ...)
    tland = [W54 + 0.02, W55 + 0.02, W57 - 0.02, W58 + 0.02]
    for k, (nm, x, y, rot) in enumerate(TILES):
        sel = f"#{s}-tile{k}"
        a = {"x": (-1 if x < 540 else 1) * 260, "y": -420, "rotation": rot * 4, "scale": 1.5, "opacity": 0}
        b = {"x": 0, "y": 0, "rotation": rot, "scale": 1, "opacity": 1}
        S.init(sel, dict(a, transformOrigin="50% 50%"))
        S.ft(sel, a, b, tland[k] - 0.1, 0.36, "back.out(1.5)")
        # drop into the V2 track
        cx, cw = CLIPS_V2[k]
        c = {"x": r3(cx + cw / 2 - (x + TW / 2)), "y": r3(ROW["V2"] + 32 - (y + TH / 2)), "rotation": 0, "scale": 0.25, "opacity": 0}
        S.ft(sel, b, c, W61 - 0.02 + 0.07 * k, 0.34, "power3.in")
        S.init(f"#{s}-c{k}", {"opacity": 0, "scaleX": 0.3, "transformOrigin": "0% 50%"})
        S.ft(f"#{s}-c{k}", {"opacity": 0, "scaleX": 0.3}, {"opacity": 1, "scaleX": 1}, W61 + 0.26 + 0.06 * k, 0.18, "power3.out")
    # timeline unfolds ("timeline editornya terbuka") and tilts back (camera over the timeline)
    S.init(f"#{s}-tl", {"opacity": 0, "scaleY": 0.05, "rotationX": 0, "transformOrigin": "50% 0%", "transformPerspective": 1300})
    S.ft(f"#{s}-tl", {"opacity": 0, "scaleY": 0.05}, {"opacity": 1, "scaleY": 1}, W60 - 0.04, 0.38, "power3.out")
    S.ft(f"#{s}-tl", {"rotationX": 0}, {"rotationX": 16}, W60 + 0.3, out0 - W60 - 0.3, "sine.inOut")
    S.init(f"#{s}-ph", {"x": 0})
    S.ft(f"#{s}-ph", {"x": 0}, {"x": 700}, W60 + 0.2, out0 - W60 - 0.2, "none")
    S.init(f"#{s}-tc", {"opacity": 1})
    # paper clip: sits in the V2 slot (scaled strip), cursor grabs it on "terbuka", it lifts and lands as the floor strip
    pa = {"x": r3(px - (-40)), "y": r3(py - (FLOOR_Y - 10)), "scaleX": r3(pw / 1160), "scaleY": r3(ph / 70), "rotation": 0, "opacity": 0}
    pb = dict(pa, opacity=1)
    pc = dict(pb, y=r3(py - 60 - (FLOOR_Y - 10)), rotation=-4, scaleX=r3(pw * 1.15 / 1160), scaleY=r3(ph * 1.15 / 70))
    pd = {"x": 0, "y": 0, "scaleX": 1, "scaleY": 1, "rotation": 0, "opacity": 1}
    S.init(f"#{s}-paper", dict(pa, transformOrigin="0% 0%"))
    S.ft(f"#{s}-paper", pa, pb, W61 + 0.2, 0.2, "power2.out")
    S.ft(f"#{s}-paper", pb, pc, W62 + 0.04, 0.2, "power3.out")
    S.ft(f"#{s}-paper", pc, pd, out0 + 0.04, t1 - out0 - 0.06, "power3.inOut")
    S.init(f"#{s}-cur", {"opacity": 0, "x": 160, "y": 160})
    S.ft(f"#{s}-cur", {"opacity": 0, "x": 160, "y": 160}, {"opacity": 1, "x": 0, "y": 0}, W61 + 0.08, 0.32, "power3.out")
    S.ft(f"#{s}-cur", {"x": 0, "y": 0, "scale": 1}, {"x": 0, "y": 0, "scale": 0.82}, W62 + 0.02, 0.08, "power2.in")
    S.ft(f"#{s}-cur", {"x": 0, "y": 0, "scale": 0.82}, {"x": 0, "y": -60, "scale": 0.82}, W62 + 0.1, 0.26, "power3.out")
    S.ft(f"#{s}-cur", {"opacity": 1}, {"opacity": 0}, out0, 0.15, "none")
    # editor folds away
    for sel in (f"#{s}-bez", f"#{s}-ui", f"#{s}-tl"):
        S.ft(sel, {"opacity": 1}, {"opacity": 0}, out0, 0.24, "power2.in")
    for sel in (f"#{s}-mon", f"#{s}-amb"):
        S.init(sel, {"opacity": 1})
        S.ft(sel, {"opacity": 1}, {"opacity": 0}, out0, 0.3, "power2.in")
    for k in range(4):
        S.ft(f"#{s}-c{k}", {"opacity": 1}, {"opacity": 0}, out0, 0.2, "power2.in")

    # ---------------------------------------------------------------- mascot: plays in the monitor, then released to WIDE (S12 start)
    v_end = dict(WIDE, yaw=-10)
    S.mv([(t0, MON_VIEW, None), (W59, dict(MON_VIEW, yaw=-4), "sine.inOut"), (out0 + 0.1, dict(MON_VIEW, yaw=-8), "sine.inOut"), (t1, v_end, "power3.inOut")])
    S.mc([(t0, {"clipPath": clip_rect(mx, my, mw, mh, mr)}, None), (out0 - 0.04, {"clipPath": clip_rect(mx, my, mw, mh, mr)}, "none"),
          (out0 + 0.14, {"clipPath": CLIP_NONE}, "power2.in")])
    S.mx([(t0, {"filter": NO_FILTER}, None)])
    # acting: presents the B-roll stacking, points at the timeline, follows the paper clip
    S.act("armL", [(t0 + 0.02, "low", 0.3), (W54 - 0.1, "present", 0.32), (W58, "low", 0.4), (W60 - 0.1, "point", 0.3), (W62 + 0.1, "low", 0.4)])
    S.act("armR", [(t0 + 0.02, "low", 0.3), (W55 - 0.05, "open", 0.32), (W58 + 0.1, "low", 0.4)])
    S.act("head", [(t0 + 0.02, [0, -0.2, 0.03], 0.3), (W55, [0, 0.25, -0.03], 0.35), (W60, [0.12, 0.2, 0], 0.35), (W62 + 0.1, [0.16, 0.12, 0], 0.35),
                   (out0 + 0.1, [0, 0, 0], 0.35)])
    S.act("torso", [(t0 + 0.02, {}, 0.3), (W60, {"chest": [0.05, 0.08, 0]}, 0.4), (out0, {}, 0.4)])
    for k in range(4):
        S.fx(tland[k] + 0.12, "pop", 0.05)
    S.fx(W60, "whoosh", 0.05)
    S.fx(W61 + 0.2, "click", 0.04)
    S.fx(W62 + 0.04, "click", 0.06)
    S.fx(out0 + 0.05, "whoosh", 0.05)

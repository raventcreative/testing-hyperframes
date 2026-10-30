"""S03 — CLICK RIPPLE & CLAUDE (W17 – W19). "Claude Code."  The pixel-hand presses the result exactly on the spoken
"Claude": 3 cyan shock rings + a 2-3 px camera impulse; the Claude page opens THROUGH the click point (circular wipe), the
Claude wordmark (typeset, no supplied logo file) gets a 0.3 s soft light reaction, then shrinks into the neutral home UI.
On "Code" the cursor taps the Code tab (-> S04)."""
from kit_op import google_ui, claude_home, cursor, rings, click

HIT = (175, 905)
TAB = (300 + 244 + 114, 300 + 41)      # centre of the "Code" tab


def build(S):
    s, W = S.id, S.W
    S.mv([(S.t0, {"fx": -600, "fy": 3000, "h": 1000, "yaw": 0, "pitch": 5, "vis": 0}, None)])   # mascot off in UI/world shots
    S.back.append(google_ui(s, f"{s}-q"))
    S.back.append(claude_home(s))
    S.back.append(f'<div class="abs" id="{s}-brand" style="left:0;top:800px;width:1080px;text-align:center;font:400 170px/1 Georgia, serif;color:#f5f4ef;'
                  f'text-shadow:0 0 0 rgba(255,214,170,0)">Claude</div>')
    S.front.append(rings(f"{s}-r", *HIT) + rings(f"{s}-r2", *TAB))
    S.front.append(cursor(f"{s}-cur", HIT[0], HIT[1]))
    S.init(f"#{s}-q", {"textContent": "Claude"})
    S.init(f"#{s}-caret", {"opacity": 0})
    at = W(17) - 0.02
    click(S, f"{s}-cur", f"{s}-r", at, 0.09)
    S.cam([(S.t0, {"x": 0, "y": 0}, None), (at + 0.01, {"x": 0, "y": 0}, None), (at + 0.05, {"x": 3, "y": 2}, "power2.out"),
           (at + 0.1, {"x": -2, "y": -1}, "sine.inOut"), (at + 0.16, {"x": 0, "y": 0}, "sine.out")])
    # Claude opens through the click point
    cx, cy = HIT
    S.init(f"#{s}-home", {"clipPath": f"circle(0px at {cx}px {cy}px)"})
    S.ft(f"#{s}-home", {"clipPath": f"circle(0px at {cx}px {cy}px)"}, {"clipPath": f"circle(2300px at {cx}px {cy}px)"}, at + 0.06, 0.32, "power3.in")
    S.init(f"#{s}-hi", {"opacity": 0})
    S.init(f"#{s}-brand", {"opacity": 0, "scale": 0.9})
    S.ft(f"#{s}-brand", {"opacity": 0, "scale": 0.9}, {"opacity": 1, "scale": 1}, at + 0.12, 0.3, "power3.out")
    S.ft(f"#{s}-brand", {"textShadow": "0 0 0px rgba(255,214,170,0)"}, {"textShadow": "0 0 40px rgba(255,214,170,.55)"}, at + 0.2, 0.15, "power2.out")
    S.ft(f"#{s}-brand", {"textShadow": "0 0 40px rgba(255,214,170,.55)"}, {"textShadow": "0 0 0px rgba(255,214,170,0)"}, at + 0.35, 0.2, "power2.in")
    S.fx(at + 0.18, "sparkle", 0.05)
    # the wordmark shrinks into the home UI headline position
    S.ft(f"#{s}-brand", {"y": 0, "scale": 1, "opacity": 1}, {"y": -160, "scale": 0.42, "opacity": 0}, at + 0.42, 0.28, "power3.inOut")
    S.ft(f"#{s}-hi", {"opacity": 0, "y": 20}, {"opacity": 1, "y": 0}, at + 0.5, 0.25, "power2.out")
    # cursor travels to the Code tab and taps it on "Code"
    S.ft(f"#{s}-cur", {"x": 0, "y": 0}, {"x": TAB[0] - HIT[0], "y": TAB[1] - HIT[1]}, at + 0.3, 0.32, "power3.inOut")
    S.init(f"#{s}-cur", {"transformOrigin": "40% 2%"})
    tap = max(W(18) + 0.12, at + 0.66)
    S.ft(f"#{s}-cur", {"scale": 1}, {"scale": 0.88}, tap - 0.05, 0.055, "power2.in")
    S.ft(f"#{s}-cur", {"scale": 0.88}, {"scale": 1}, tap + 0.005, 0.07, "power2.out")
    for k, (t0, d, sc, a) in enumerate(((0.05, 0.4, 5, .6), (0.12, 0.42, 7, .4))):
        S.ft(f"#{s}-r2{k}", {"scale": 0.6, "opacity": a}, {"scale": sc, "opacity": 0}, tap + t0 - 0.05, d, "power2.out")
    S.fx(tap, "click", 0.07)
    S.ft(f"#{s}-tcode", {"backgroundColor": "rgba(58,57,54,0)"}, {"backgroundColor": "rgba(201,100,66,1)"}, tap, 0.12, "power1.out")

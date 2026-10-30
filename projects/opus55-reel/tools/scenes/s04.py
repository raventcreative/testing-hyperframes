"""S04 — CLAUDE CODE PROMPT (W19 – W31). "Dari satu ide, kita bisa arahin karakter, dunia, lighting sampai gerakan
kameranya."  Neutral Claude Code terminal (no repo, no path). The idea is typed as one prompt, Enter, a short status line,
then a luminous aperture opens inside the terminal and becomes the 3D world (world.html takes over)."""
from kit_op import code_ui

PROMPT = ("Build a cinematic 3D pocket universe: an astronaut discovers a glowing cube "
          "that unfolds into a living miniature world.")


def build(S):
    s, W = S.id, S.W
    S.mv([(S.t0, {"fx": -600, "fy": 3000, "h": 1000, "yaw": 0, "pitch": 5, "vis": 0}, None)])   # mascot off in UI/world shots
    S.back.append(f'<div class="abs" style="left:0;top:0;width:1080px;height:1920px;background:#0d0d0c"></div>')
    S.back.append(code_ui(s, f"{s}-p", f"{s}-st"))
    S.init(f"#{s}-term", {"opacity": 0, "scale": 0.94, "y": 40})
    S.ft(f"#{s}-term", {"opacity": 0, "scale": 0.94, "y": 40}, {"opacity": 1, "scale": 1, "y": 0}, S.t0, 0.4, "power3.out")
    S.fx(S.t0 + 0.02, "whoosh", 0.05)
    # typing: whole prompt between "Dari" and "lighting" (chunks of ~3 chars so it never jitters)
    t0, t1 = W(19) + 0.1, W(27) - 0.1
    n = len(PROMPT)
    steps = 60
    S.init(f"#{s}-p", {"textContent": ""})
    for k in range(1, steps + 1):
        at = t0 + (t1 - t0) * k / steps
        S.tset(f"#{s}-p", {"textContent": PROMPT[: round(n * k / steps)]}, at)
        if k % 4 == 0:
            S.fx(at, "key", 0.04)
    enter = W(27) + 0.05
    S.fx(enter, "click", 0.08)
    S.tset(f"#{s}-caret", {"opacity": 0}, enter)
    S.ft(f"#{s}-st", {"opacity": 0, "y": 10}, {"opacity": 1, "y": 0}, enter + 0.1, 0.25, "power2.out")
    for k in range(10):
        S.tset(f"#{s}-dots", {"textContent": "." * (k % 4)}, enter + 0.15 + 0.25 * k)
    S.ft(f"#{s}-ap", {"borderColor": "rgba(0,201,255,0)", "boxShadow": "0 0 0px rgba(0,201,255,0)"},
         {"borderColor": "rgba(0,201,255,0.9)", "boxShadow": "0 0 40px rgba(0,201,255,.6)"}, S.t1 - 0.75, 0.3, "power2.out")
    S.fx(S.t1 - 0.5, "sparkle", 0.05)

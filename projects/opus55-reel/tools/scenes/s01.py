"""S01 — ROOM & HOOK (0 – W6). "Gila, AI sekarang udah sejauh ini."  The camera is already drifting in the navy studio
room; the existing mascot takes two steps toward camera in front of the desk (laptop + monitor behind) and lands one
purposeful gesture on the hook."""
from kit_op import room, MASCOT_ROOM


def build(S):
    s, W = S.id, S.W
    S.back.append(f'<div class="abs" id="{s}-rw" style="left:0;top:0;width:1080px;height:1920px">' + "".join(room(s)) + "</div>")
    S.keys(f"#{s}-rw", [(S.t0, {"scale": 1.0, "x": 0, "y": 0, "transformOrigin": "540px 1100px"}, None), (S.t1, {"scale": 1.06, "x": -14, "y": -10}, "sine.inOut")])
    S.keys(f"#{s}-wall", [(S.t0, {"x": 0}, None), (S.t1, {"x": 22}, "sine.inOut")])          # parallax: wall drifts against the desk
    S.mv([(S.t0, dict(MASCOT_ROOM, fy=1700, h=930), None), (0.85, dict(MASCOT_ROOM), "power2.out")])
    S.intent(W(1), "present", "right")
    S.intent(W(4), "emphasize", "left")

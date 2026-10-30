"""S06 — MASCOT + PIP (W41 – W61). "Kalau kalian masih pakai AI cuma buat tanya jawab, kalian baru nyentuh
permukaannya. Sekarang, waktunya belajar bikin, bukan cuma nonton."  The same world keeps playing: blurred behind, sharp
in the edge-lit frame above (label CLAUDE OPUS 5.5). The mascot rises into a half-body shot below the frame, facing the
viewer; one gesture per idea (question on "tanya jawab", points up to the frame on "permukaannya", no-shake on "bukan")."""

V6 = {"fx": 540, "fy": 2060, "h": 1300, "yaw": 0, "pitch": 4}


def build(S):
    s, W = S.id, S.W
    S.back.append('<div class="abs" style="left:0;top:0;width:10px;height:10px"></div>')
    S.mv([(S.t0, dict(V6, fy=3400, vis=1), None), (S.t0 + 0.25, dict(V6, fy=3400), None), (S.t0 + 0.9, dict(V6), "power3.out")])
    S.fx(S.t0 + 0.3, "whoosh", 0.05)
    S.intent(W(41), "explain", "left")
    S.intent(W(48), "question")
    S.intent(W(52), "pointFwd", "right")
    S.intent(W(54), "emphasize", "left")
    S.intent(W(57), "present", "right")
    S.intent(W(58), "emphasize", "left")

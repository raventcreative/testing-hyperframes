"""S05 — POCKET UNIVERSE (W31 – W41). "Tunggu, lihat hasilnya. Dunia yang tadinya kosong, pelan-pelan jadi hidup."
The 3D world (compositions/world.html) fills the frame: astronaut reaches the cube on "lihat hasilnya", the cube unfolds
on "Dunia", the land blooms from grey to colour and light on "pelan-pelan jadi hidup". This scene only adds sound."""


def build(S):
    W = S.W
    S.mv([(S.t0, {"fx": -600, "fy": 3000, "h": 1000, "yaw": 0, "pitch": 5, "vis": 0}, None)])   # mascot off in the world shot
    S.back.append('<div class="abs" style="left:0;top:0;width:10px;height:10px"></div>')
    S.fx(W(34) - 0.05, "whoosh", 0.05)       # panels hinge open
    S.fx(W(34) + 0.25, "click", 0.05)
    S.fx(W(38), "sparkle", 0.06)             # the world comes alive

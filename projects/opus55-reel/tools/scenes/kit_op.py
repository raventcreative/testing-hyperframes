"""Claude Opus 5.5 reel — shared stage pieces (1080x1920, navy plate, cyan #00C9FF accent, white Poppins).
Room (desk, laptop, monitor, LED strip, floor), privacy-safe recreated UIs (generic dark search page, neutral Claude
home, neutral Claude Code terminal — no account names, no history, no projects), the user's pixel-hand cursor,
click shockwave rings. All absolute px in the 1080x1920 frame."""
from xk import box, r3

CY = "#00C9FF"
# room layout (screen px) — laptop screen is the camera's target in S2 and the landing spot in S7
LAP = (575, 1012, 360, 222)          # laptop screen x, y, w, h
MON = (110, 846, 520, 300)           # monitor screen
MASCOT_ROOM = {"fx": 330, "fy": 1800, "h": 1080, "yaw": 0, "pitch": 5}
MONO = "'DejaVu Sans Mono', 'Liberation Mono', 'Courier New', monospace"


def room(s):
    """the 3D room behind the mascot: wall panels + LED strip, floor, desk, monitor, laptop, mug, lamp glow."""
    lx, ly, lw, lh = LAP
    mx, my, mw, mh = MON
    code = "".join(f'<div class="abs" style="left:{24 + (k % 3) * 18}px;top:{24 + k * 26}px;width:{120 + (k * 53) % 260}px;height:9px;border-radius:5px;'
                   f'background:{"rgba(0,201,255,.55)" if k % 4 == 0 else "rgba(255,255,255,.22)"}"></div>' for k in range(10))
    mini = (f'<div class="abs" style="inset:0;background:#202124">'
            f'<div class="abs" style="left:0;top:58px;width:{lw}px;text-align:center;font:500 38px/1 Arial, sans-serif;letter-spacing:-1px">'
            f'<span style="color:#8ab4f8">G</span><span style="color:#f28b82">o</span><span style="color:#fdd663">o</span><span style="color:#8ab4f8">g</span><span style="color:#81c995">l</span><span style="color:#f28b82">e</span></div>'
            f'<div class="abs" style="left:40px;top:118px;width:{lw - 80}px;height:30px;border-radius:15px;background:#303134"></div></div>')
    return [
        # wall: soft vertical panels + cyan LED strip + lamp glow (key light upper-left)
        f'<div class="abs" id="{s}-wall" style="left:-80px;top:0;width:1240px;height:1520px;'
        f'background:repeating-linear-gradient(90deg,rgba(255,255,255,.035) 0 2px,transparent 2px 180px)"></div>',
        f'<div class="abs" id="{s}-led" style="{box(-40, 760, 1160, 6)}border-radius:3px;background:{CY};opacity:.55;box-shadow:0 0 24px 4px rgba(0,201,255,.45)"></div>',
        f'<div class="abs" style="{box(-200, 200, 900, 900)}border-radius:50%;background:radial-gradient(circle,rgba(120,190,255,.20),rgba(120,190,255,0) 65%)"></div>',
        # floor
        f'<div class="abs" id="{s}-floor" style="left:-300px;top:1440px;width:1680px;height:520px;background:linear-gradient(180deg,#0d1a3a 0%,#070d22 100%)"></div>',
        f'<div class="abs" style="left:-500px;top:900px;width:2080px;height:560px;transform:perspective(900px) rotateX(70deg);transform-origin:50% 100%;'
        f'background-image:linear-gradient(rgba(0,201,255,.10) 2px,transparent 2px),linear-gradient(90deg,rgba(0,201,255,.10) 2px,transparent 2px);background-size:90px 90px;'
        f'top:1440px;-webkit-mask:linear-gradient(180deg,transparent,#000 60%);mask:linear-gradient(180deg,transparent,#000 60%)"></div>',
        # monitor (behind, left)
        f'<div class="abs" id="{s}-mon" style="{box(mx - 14, my - 14, mw + 28, mh + 28)}border-radius:18px;background:linear-gradient(160deg,#2b3550,#121829);'
        f'box-shadow:0 30px 50px -24px rgba(0,0,0,.7),inset 0 1px 0 rgba(255,255,255,.12)">'
        f'<div class="abs" style="left:14px;top:14px;width:{mw}px;height:{mh}px;border-radius:8px;background:#0b1224;overflow:hidden">{code}</div></div>',
        f'<div class="abs" style="{box(mx + mw / 2 - 30, my + mh + 14, 60, 90)}background:linear-gradient(90deg,#3a4560,#1d2438)"></div>',
        # desk: top surface in perspective + front edge
        f'<div class="abs" id="{s}-desk" style="{box(40, 1150, 1000, 150)}transform:perspective(900px) rotateX(62deg);transform-origin:50% 100%;'
        f'background:linear-gradient(180deg,#3b4766 0%,#26304a 100%);border-radius:10px;box-shadow:inset 0 2px 0 rgba(255,255,255,.18)"></div>',
        f'<div class="abs" style="{box(40, 1300, 1000, 46)}border-radius:6px;background:linear-gradient(180deg,#1d2539,#121829);box-shadow:0 30px 40px -10px rgba(0,0,0,.6)"></div>',
        # laptop: screen (lid) + base + soft screen light on the desk
        f'<div class="abs" style="{box(lx - 40, ly + lh - 10, lw + 80, 60)}border-radius:50%;background:radial-gradient(closest-side,rgba(140,200,255,.25),rgba(140,200,255,0))"></div>',
        f'<div class="abs" id="{s}-lid" style="{box(lx - 12, ly - 12, lw + 24, lh + 22)}border-radius:14px 14px 4px 4px;background:linear-gradient(160deg,#c7cfdb,#7d889b);'
        f'box-shadow:0 24px 36px -20px rgba(0,0,0,.7)"><div class="abs" id="{s}-scr" style="left:12px;top:12px;width:{lw}px;height:{lh}px;border-radius:6px;overflow:hidden">{mini}</div></div>',
        f'<div class="abs" style="{box(lx - 50, ly + lh + 8, lw + 100, 22)}border-radius:3px 3px 12px 12px;background:linear-gradient(180deg,#d9dfe8,#8e99ab)"></div>',
        # mug
        f'<div class="abs" style="{box(470, 1196, 56, 66)}border-radius:8px 8px 14px 14px;background:linear-gradient(90deg,#e8edf5,#aab4c4)"></div>',
    ]


def google_ui(s, q_id):
    """privacy-safe recreated dark search page (generic; no history, no account). Typed query lives in #{q_id}."""
    return (f'<div class="abs" id="{s}-g" style="left:0;top:0;width:1080px;height:1920px;background:#202124">'
            f'<div class="abs" style="left:0;top:420px;width:1080px;text-align:center;font:500 150px/1 Arial, sans-serif;letter-spacing:-6px">'
            f'<span style="color:#8ab4f8">G</span><span style="color:#f28b82">o</span><span style="color:#fdd663">o</span>'
            f'<span style="color:#8ab4f8">g</span><span style="color:#81c995">l</span><span style="color:#f28b82">e</span></div>'
            f'<div class="abs" id="{s}-box" style="{box(90, 650, 900, 120)}border-radius:60px;background:#303134;border:1px solid #5f6368">'
            f'<svg class="abs" style="left:40px;top:38px;width:44px;height:44px" viewBox="0 0 24 24"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="#9aa0a6" stroke-width="2.2"/><path d="M15.5 15.5 21 21" stroke="#9aa0a6" stroke-width="2.4" stroke-linecap="round"/></svg>'
            f'<div class="abs" style="left:110px;top:30px;font:400 52px/60px Arial, sans-serif;color:#e8eaed;white-space:nowrap"><span id="{q_id}"></span>'
            f'<span id="{s}-caret" style="display:inline-block;width:3px;height:52px;margin-left:4px;vertical-align:-8px;background:#e8eaed"></span></div></div>'
            # results (generic, public product listing — no personal content)
            f'<div class="abs" id="{s}-res" style="{box(90, 820, 900, 520)}">'
            f'<div class="abs" style="left:0;top:0;font:400 30px/1.3 Arial, sans-serif;color:#bdc1c6">claude.ai</div>'
            f'<div class="abs" id="{s}-hit" style="left:0;top:44px;font:400 56px/1.2 Arial, sans-serif;color:#8ab4f8">Claude</div>'
            f'<div class="abs" style="left:0;top:122px;width:900px;font:400 32px/1.45 Arial, sans-serif;color:#bdc1c6">AI assistant by Anthropic for writing, analysis and coding.</div>'
            f'<div class="abs" style="left:0;top:290px;font:400 30px/1.3 Arial, sans-serif;color:#bdc1c6">claude.com</div>'
            f'<div class="abs" style="left:0;top:334px;font:400 56px/1.2 Arial, sans-serif;color:#8ab4f8">Claude Code</div>'
            f'<div class="abs" style="left:0;top:412px;width:900px;font:400 32px/1.45 Arial, sans-serif;color:#bdc1c6">Agentic coding in your terminal.</div></div></div>')


def claude_home(s):
    """neutral Claude home: no names, no Recent, no Projects — only the public chrome (wordmark, input, model, Chat/Code)."""
    return (f'<div class="abs" id="{s}-home" style="left:0;top:0;width:1080px;height:1920px;background:#262624">'
            f'<div class="abs" style="{box(300, 300, 480, 84)}border-radius:42px;background:#1f1e1d;border:1px solid #3a3936">'
            f'<div class="abs" id="{s}-tchat" style="{box(8, 8, 228, 66)}border-radius:34px;background:#3a3936;font:500 32px/66px Arial, sans-serif;color:#f5f4ef;text-align:center">Chat</div>'
            f'<div class="abs" id="{s}-tcode" style="{box(244, 8, 228, 66)}border-radius:34px;font:500 32px/66px Arial, sans-serif;color:#b8b5ad;text-align:center">Code</div></div>'
            f'<div class="abs" id="{s}-hi" style="left:0;top:640px;width:1080px;text-align:center;font:400 72px/1.2 Georgia, serif;color:#f5f4ef">How can I help you today?</div>'
            f'<div class="abs" style="{box(90, 820, 900, 230)}border-radius:34px;background:#30302e;border:1px solid #45443f">'
            f'<div class="abs" style="left:40px;top:40px;font:400 34px/1 Arial, sans-serif;color:#8f8c84">Message Claude…</div>'
            f'<div class="abs" style="left:600px;top:156px;font:500 28px/1 Arial, sans-serif;color:#d6d3cb">Opus 5.5</div>'
            f'<div class="abs" style="{box(820, 140, 56, 56)}border-radius:16px;background:#c96442"></div></div></div>')


def code_ui(s, prompt_id, status_id):
    """neutral Claude Code terminal (no repo names, no paths); prompt typed into #{prompt_id}."""
    return (f'<div class="abs" id="{s}-term" style="{box(40, 250, 1000, 1110)}border-radius:26px;background:#141413;border:1px solid #3a3936;'
            f'box-shadow:0 40px 80px -30px rgba(0,0,0,.8);overflow:hidden">'
            f'<div class="abs" style="left:0;top:0;width:1000px;height:70px;background:#1f1e1d;border-bottom:1px solid #3a3936">'
            + "".join(f'<div class="abs" style="left:{28 + 30 * i}px;top:26px;width:18px;height:18px;border-radius:50%;background:{c}"></div>' for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840")))
            + f'<div class="abs" style="left:0;top:20px;width:1000px;text-align:center;font:500 28px/30px Arial, sans-serif;color:#b8b5ad">Claude Code</div></div>'
            f'<div class="abs" style="{box(40, 110, 920, 190)}border-radius:16px;border:2px solid #c96442;padding:26px 30px;font:400 30px/1.5 {MONO};color:#e8e6dc">'
            f'<span style="color:#d97757">✻</span> Welcome to <b>Claude Code</b><br><span style="color:#8f8c84">model: Opus 5.5</span></div>'
            f'<div class="abs" style="left:40px;top:340px;width:920px;font:400 34px/1.55 {MONO};color:#e8e6dc;white-space:pre-wrap;word-break:break-word">'
            f'<span style="color:#8f8c84">&gt; </span><span id="{prompt_id}"></span><span id="{s}-caret" style="display:inline-block;width:18px;height:36px;vertical-align:-6px;background:#e8e6dc"></span></div>'
            f'<div class="abs" id="{status_id}" style="left:40px;top:800px;width:920px;font:400 32px/1.6 {MONO};color:#d97757;opacity:0">'
            f'✻ <span style="color:#e8e6dc">Building the pocket universe</span><span id="{s}-dots"></span></div>'
            f'<div class="abs" id="{s}-ap" style="{box(300, 900, 400, 320)}border-radius:18px;border:2px solid rgba(0,201,255,.0)"></div></div>')


def cursor(id_, x, y, w=150):
    """the user's pixel-hand pointer (assets/brand/cursor_trim.png, 397x403). Hotspot = fingertip (≈ 0.40 w, 0.02 h)."""
    h = w * 403 / 397
    return f'<img id="{id_}" class="abs" src="assets/brand/cursor_trim.png" style="left:{r3(x - 0.40 * w)}px;top:{r3(y - 0.02 * h)}px;width:{w}px;height:{r3(h)}px;transform-origin:40% 2%">'


def rings(id_, x, y):
    out = ""
    for k, (w, a) in enumerate(((3, .6), (2, .42), (1.5, .28))):
        out += (f'<div class="abs" id="{id_}{k}" style="left:{x - 10}px;top:{y - 10}px;width:20px;height:20px;border-radius:50%;'
                f'border:{w}px solid {CY};opacity:0"></div>')
    return out


def click(S, cur_id, ring_id, at, vol=0.08):
    """press 0.11 s (1 -> 0.88 -> 1) + 3 shock rings + a restrained 2-3 px camera impulse + click SFX."""
    S.ft(f"#{cur_id}", {"scale": 1, "y": 0}, {"scale": 0.88, "y": 4}, at - 0.05, 0.055, "power2.in")
    S.ft(f"#{cur_id}", {"scale": 0.88, "y": 4}, {"scale": 1, "y": 0}, at + 0.005, 0.07, "power2.out")
    for k, (t0, d, sc, a) in enumerate(((0.05, 0.5, 7, .6), (0.14, 0.53, 9.5, .42), (0.25, 0.5, 12.5, .28))):
        S.ft(f"#{ring_id}{k}", {"scale": 0.6, "opacity": a}, {"scale": sc, "opacity": 0}, at + t0 - 0.05, d, "power2.out")
    S.fx(at - 0.02, "click", vol)

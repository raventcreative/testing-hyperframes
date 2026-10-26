"""Scenes 10-14 (slides 11-15). make(scene_body) -> list of slide dicts."""

# ---------------------------------------------------------------- 10 sketch -> app (wide dashboard window, horizontal wipe)
S11_CSS = """
.win { position:absolute; left:56px; top:48px; width:840px; height:524px; border-radius:24px; overflow:hidden; border:1.5px solid rgba(255,255,255,0.22); background:rgba(8,14,44,0.55); }
.lay { position:absolute; inset:0; }
.lay .bar { position:absolute; left:0; right:0; top:0; height:52px; border-bottom:1.5px solid rgba(255,255,255,0.14); }
.lay .bar i { position:absolute; top:20px; width:12px; height:12px; border-radius:50%; }
.lay .t1 { position:absolute; left:40px; top:78px; font-size:36px; font-weight:700; }
.lay .t2 { position:absolute; left:42px; top:126px; font-size:18px; }
.lay .ringw { position:absolute; left:40px; top:170px; width:310px; height:310px; }
.lay .pct { position:absolute; left:40px; top:270px; width:310px; text-align:center; font-size:84px; font-weight:700; letter-spacing:-0.03em; line-height:1.1; }
.lay .pct small { font-size:34px; }
.lay .cd { position:absolute; left:400px; width:400px; height:150px; border-radius:20px; padding:22px 26px; }
.lay .cd .k { font-size:18px; }
.lay .cd .v { font-size:48px; font-weight:700; letter-spacing:-0.02em; line-height:1.25; }
.lay .cd .pb { position:absolute; left:26px; right:26px; bottom:22px; height:10px; border-radius:5px; }
.lay .cd .dots { position:absolute; left:26px; bottom:20px; display:flex; gap:10px; }
.lay .cd .dots b { width:18px; height:18px; border-radius:50%; display:block; }
/* sketch */
.sk { color:transparent; }
.sk .t1, .sk .t2, .sk .pct, .sk .k, .sk .v { color:transparent; -webkit-text-stroke:1.3px rgba(255,255,255,0.75); }
.sk .cd { border:2px dashed rgba(255,255,255,0.55); }
.sk .bar i { border:1.5px solid rgba(255,255,255,0.6); }
.sk .pb { border:1.5px dashed rgba(255,255,255,0.6); }
.sk .dots b { border:1.5px solid rgba(255,255,255,0.6); }
.sk .grid { position:absolute; inset:0; background:repeating-linear-gradient(90deg,rgba(255,255,255,0.05) 0 1px,transparent 1px 40px),repeating-linear-gradient(0deg,rgba(255,255,255,0.05) 0 1px,transparent 1px 40px); }
/* finished */
.fin { background:linear-gradient(150deg,#16306e,#0b1440); }
.fin .bar { background:rgba(255,255,255,0.05); }
.fin .t1, .fin .v, .fin .pct { color:#fff; }
.fin .t2, .fin .k { color:#00c9ff; }
.fin .cd { background:rgba(255,255,255,0.09); border:1.5px solid rgba(255,255,255,0.18); }
.fin .pb { background:rgba(255,255,255,0.14); overflow:hidden; }
.fin .pb i { position:absolute; left:0; top:0; bottom:0; width:86%; border-radius:5px; background:linear-gradient(90deg,#0078ff,#00c9ff); }
.fin .dots b { background:#00c9ff; }
.fin .dots b.off { background:rgba(255,255,255,0.18); }
#hdl { position:absolute; top:48px; height:524px; width:4px; margin-left:-2px; background:#fff; box-shadow:0 0 18px rgba(0,201,255,0.9); }
#hdl b { position:absolute; left:-26px; top:236px; width:56px; height:56px; border-radius:50%; background:#fff; color:#0b1440; font-weight:700; font-size:22px; display:flex; align-items:center; justify-content:center; box-shadow:0 8px 20px rgba(0,0,0,0.4); }
"""


def _layer(cls, sketch):
    ring = ('<svg class="ringw" viewBox="0 0 310 310"><circle cx="155" cy="155" r="122" fill="none" stroke="rgba(255,255,255,0.6)" stroke-width="3" stroke-dasharray="8 7"/>'
            '<circle cx="155" cy="155" r="96" fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="2" stroke-dasharray="4 6"/></svg>') if sketch else \
           ('<svg class="ringw" viewBox="0 0 310 310"><defs><linearGradient id="rg11" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00c9ff"/><stop offset="1" stop-color="#0078ff"/></linearGradient></defs>'
            '<circle cx="155" cy="155" r="110" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="26"/>'
            '<circle id="arc11" cx="155" cy="155" r="110" fill="none" stroke="url(#rg11)" stroke-width="26" stroke-linecap="round" transform="rotate(-90 155 155)" stroke-dasharray="691" stroke-dashoffset="691"/></svg>')
    dots = "".join(f'<b class="{"off" if i >= 5 else ""}"></b>' for i in range(7))
    return f"""        <div class="lay {cls}" id="{cls}">{'<div class="grid"></div>' if sketch else ''}
          <div class="bar"><i style="left:22px;background:{'' if sketch else '#ff6b6b'}"></i><i style="left:42px;background:{'' if sketch else '#ffd166'}"></i><i style="left:62px;background:{'' if sketch else '#00c9ff'}"></i></div>
          <div class="t1">Progres Kelas</div><div class="t2">AIpreneur &middot; minggu ke-6</div>
          {ring}<div class="pct" id="{'pk' if sketch else 'pf'}">86<small>%</small></div>
          <div class="cd" style="top:170px"><div class="k">Materi selesai</div><div class="v">24 / 28</div><div class="pb"><i></i></div></div>
          <div class="cd" style="top:340px"><div class="k">Streak belajar</div><div class="v">12 hari</div><div class="dots">{dots}</div></div>
        </div>"""


S11_VIS = f"""      <div class="win">
{_layer("sk", True)}
{_layer("fin", False)}
      </div>
      <div id="hdl"><b>&lsaquo;&rsaquo;</b></div>"""
S11_JS = """
  function render(t) {
    const p = t < 3.9 ? io3((t - 0.5) / 1.7) : 1 - io3((t - 4.1) / 1.5);
    const x = 56 + 840 * p;
    $("fin").style.clipPath = "inset(0 " + (840 * (1 - p)).toFixed(1) + "px 0 0)";
    gsap.set("#hdl", { x: x, opacity: env(t, 0.25, 5.85, 0.2) });
    const fill = io3((t - 1.4) / 1.1) * (1 - smooth((t - 4.3) / 0.8));
    $("arc11").setAttribute("stroke-dashoffset", (691 * (1 - 0.86 * fill)).toFixed(1));
    $("pf").firstChild.nodeValue = Math.round(86 * fill);
  }
"""

# ---------------------------------------------------------------- 11 drag -> booked (3-day grid + unscheduled tray)
DAYS = [("Sel", "14"), ("Rab", "15"), ("Kam", "16")]
TIMES = ["09.00", "10.00", "11.00", "12.00"]
X0, CW, Y0, RH = 96, 170, 96, 112
SX, SY = X0 + CW * 1 + 4, Y0 + RH * 1 + 4    # Rabu 10.00
TX, TY = 676, 200                             # tray card pos
S12_CSS = f"""
.cal {{ position:absolute; left:20px; top:20px; width:620px; height:580px; }}
.dh {{ position:absolute; top:28px; width:{CW}px; text-align:center; font-size:20px; }}
.dh b {{ display:block; font-size:40px; line-height:1.1; color:#fff; }}
.dh.on b {{ color:#00c9ff; }}
.tm {{ position:absolute; left:16px; font-size:16px; color:rgba(255,255,255,0.6); }}
.gl {{ position:absolute; left:{X0}px; width:{CW * 3}px; height:0; border-top:1.5px solid rgba(255,255,255,0.12); }}
.gv {{ position:absolute; top:{Y0}px; height:{RH * 4}px; width:0; border-left:1.5px solid rgba(255,255,255,0.12); }}
.slot {{ position:absolute; left:{SX + 20}px; top:{SY + 20}px; width:{CW - 8}px; height:{RH - 8}px; border-radius:16px; border:2px dashed rgba(0,201,255,0.7); }}
.tray {{ position:absolute; left:656px; top:40px; width:270px; height:540px; border-radius:22px; background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.16); }}
.tray .k {{ position:absolute; left:22px; top:22px; font-size:15px; letter-spacing:0.16em; color:#00c9ff; font-weight:700; }}
.tray .ghost {{ position:absolute; left:20px; width:230px; height:90px; border-radius:16px; background:rgba(255,255,255,0.05); border:1.5px dashed rgba(255,255,255,0.2); }}
#ev {{ position:absolute; left:0; top:0; width:{CW - 8}px; height:{RH - 8}px; border-radius:16px; z-index:4; }}
#evb {{ position:absolute; inset:0; border-radius:16px; }}
#ev .n {{ position:absolute; left:16px; top:14px; right:10px; font-size:19px; font-weight:700; line-height:1.25; }}
#ev .tt {{ position:absolute; left:16px; bottom:12px; font-size:15px; }}
#avt {{ position:absolute; right:10px; bottom:10px; width:34px; height:34px; border-radius:50%; background:#0b1440; color:#fff; font-size:13px; font-weight:700; display:flex; align-items:center; justify-content:center; box-shadow:0 0 0 2px #00c9ff; opacity:0; }}
#cur12 {{ position:absolute; left:0; top:0; z-index:6; }}
"""
_grid = "".join(f'<div class="dh{" on" if i == 1 else ""}" style="left:{X0 + CW * i}px"><span class="c r">{d}</span><b>{n}</b></div>' for i, (d, n) in enumerate(DAYS))
_grid += "".join(f'<div class="tm" style="top:{Y0 + RH * i - 10}px">{tm}</div><div class="gl" style="top:{Y0 + RH * i}px"></div>' for i, tm in enumerate(TIMES))
_grid += f'<div class="gl" style="top:{Y0 + RH * 4}px"></div>'
_grid += "".join(f'<div class="gv" style="left:{X0 + CW * i}px"></div>' for i in range(4))
S12_VIS = f"""      <div class="cal">{_grid}</div>
      <div class="slot" id="slot"></div>
      <div class="tray"><div class="k">BELUM DIJADWALKAN</div><div class="ghost" style="top:330px"></div><div class="ghost" style="top:436px"></div></div>
      <div id="ev"><div id="evb"></div><div class="n" id="evn">Live Q&amp;A AIpreneur</div><div class="tt" id="evt">60 menit</div><div id="avt">FK</div></div>
      <svg id="cur12" width="38" height="46" viewBox="0 0 44 52"><path d="M4 3l0 38 10-9 7 16 7-3-7-15 14-1z" fill="#fff" stroke="#0b1440" stroke-width="3" stroke-linejoin="round"/></svg>"""
S12_JS = f"""
  const SX = {SX + 20}, SY = {SY + 20}, TX = {TX}, TY = {TY};
  function render(t) {{
    const d = io3((t - 0.85) / 1.05);
    let x = mix(TX, SX, d), y = mix(TY, SY, d) - 60 * Math.sin(Math.PI * d);
    const snap = t > 1.9 ? Math.exp(-7 * (t - 1.9)) * Math.sin((t - 1.9) * 22) * 6 : 0;
    y += snap;
    const lift = env(t, 0.75, 1.95, 0.12);
    const back = smooth((t - 5.0) / 0.3), ret = smooth((t - 5.35) / 0.35);
    if (t > 5.0) {{ x = ret > 0 ? TX : SX; y = ret > 0 ? TY : SY; }}
    gsap.set("#ev", {{ x: x, y: y, rotation: 4 * lift * Math.sin(Math.PI * d), scale: 1 + 0.05 * lift, opacity: t < 5.0 ? 1 : (ret > 0 ? ret : 1 - back) }});
    const booked = smooth((t - 1.95) / 0.2) * (t < 5.0 ? 1 : 0) + (t >= 5.0 && ret === 0 ? 1 - back : 0);
    const b = $("evb");
    b.style.background = booked > 0.5 ? "#ffffff" : "rgba(0,201,255,0.16)";
    b.style.border = booked > 0.5 ? "none" : "2px solid #00c9ff";
    b.style.boxShadow = "0 " + (14 + 12 * lift).toFixed(0) + "px 30px -12px rgba(0," + (booked > 0.5 ? "0,0" : "201,255") + ",0.6)";
    $("evn").style.color = booked > 0.5 ? "#0b1440" : "#ffffff";
    $("evt").style.color = booked > 0.5 ? "#274976" : "#00c9ff";
    $("evt").textContent = booked > 0.5 ? "Rab 15 \\u00b7 10.00" : "60 menit";
    gsap.set("#avt", {{ opacity: booked > 0.5 ? 1 : 0, scale: backOut((t - 2.15) / 0.4, 2.6), y: -18 * (1 - smooth((t - 2.15) / 0.3)) }});
    gsap.set("#slot", {{ opacity: env(t, 0.8, 1.95, 0.15) }});
    const cin = io3((t - 0.1) / 0.6);
    let cx = mix(900, TX + 120, cin), cy = mix(620, TY + 60, cin);
    if (t > 0.85) {{ cx = x + 120; cy = y + 60; }}
    const cout = smooth((t - 2.1) / 0.4);
    gsap.set("#cur12", {{ x: cx + 80 * cout, y: cy + 80 * cout, opacity: smooth((t - 0.05) / 0.2) * (1 - cout), scale: 1 - 0.1 * lift }});
  }}
"""

# ---------------------------------------------------------------- 12 alerts -> stack (counter left, feed right)
NOTES = [("Order baru", "Rp149.000"), ("Order baru", "Rp349.000"), ("Order baru", "Rp149.000"), ("Order baru", "Rp549.000"), ("Order baru", "Rp149.000")]
ARR = [0.35, 0.8, 1.25, 1.7, 2.15]
S13_CSS = """
.cl { position:absolute; left:50px; top:70px; width:330px; }
.cl .k { font-size:16px; letter-spacing:0.2em; color:#00c9ff; font-weight:700; }
.cl .n { font-size:190px; font-weight:700; line-height:1; letter-spacing:-0.05em; margin-top:16px; }
.cl .u { font-size:30px; margin-top:6px; }
.cl .om { margin-top:28px; font-size:26px; padding:8px 18px; }
.feed { position:absolute; left:420px; top:40px; width:490px; height:540px; border-radius:24px; background:rgba(255,255,255,0.05); border:1.5px solid rgba(255,255,255,0.14); overflow:hidden; }
.feed .hd { position:absolute; left:24px; top:20px; font-size:15px; letter-spacing:0.18em; color:rgba(255,255,255,0.65); font-weight:700; }
.nt { position:absolute; left:20px; top:64px; width:450px; height:96px; border-radius:20px; background:rgba(255,255,255,0.12); border:1.5px solid rgba(255,255,255,0.2); -webkit-backdrop-filter:blur(10px); backdrop-filter:blur(10px); }
.nt .ic { position:absolute; left:18px; top:20px; width:56px; height:56px; border-radius:15px; background:linear-gradient(140deg,#5fe0ff,#0078ff); display:flex; align-items:center; justify-content:center; }
.nt .a { position:absolute; left:92px; top:18px; font-size:17px; color:#00c9ff; }
.nt .b2 { position:absolute; left:92px; top:42px; font-size:30px; font-weight:700; color:#fff; }
.nt .tm { position:absolute; right:20px; top:20px; font-size:14px; color:rgba(255,255,255,0.55); }
#sum { position:absolute; left:20px; top:64px; width:450px; height:150px; border-radius:22px; background:#fff; opacity:0; }
#sum .big { position:absolute; left:28px; top:18px; font-size:80px; font-weight:700; color:#0b1440; letter-spacing:-0.03em; line-height:1.1; }
#sum .s { position:absolute; left:32px; top:108px; font-size:20px; color:#274976; }
#sum .bd { position:absolute; right:24px; top:24px; height:40px; padding:0 16px; border-radius:20px; background:#00c9ff; color:#0b1440; font-weight:700; font-size:18px; display:flex; align-items:center; }
"""
_bag = '<svg width="28" height="28" viewBox="0 0 28 28"><path d="M5 9h18l-1.5 15h-15z" fill="#fff"/><path d="M10 9V7a4 4 0 0 1 8 0v2" fill="none" stroke="#fff" stroke-width="2.5"/></svg>'
S13_VIS = """      <div class="cl"><div class="k">HARI INI</div><div class="n w" id="n13">0</div><div class="u w r">order baru masuk</div><span class="hb om" id="om13">omzet Rp2,1jt</span></div>
      <div class="feed"><div class="hd">NOTIFIKASI</div>
""" + "".join(f'        <div class="nt" id="nt{i}"><div class="ic">{_bag}</div><div class="a">{a} &middot; Kelas AIpreneur</div><div class="b2">{b}</div><div class="tm">baru saja</div></div>\n' for i, (a, b) in enumerate(NOTES)) + """        <div id="sum"><div class="big">12</div><div class="s">order baru &middot; ketuk untuk lihat</div><div class="bd" id="bd13">+12</div></div>
      </div>"""
S13_JS = """
  const ARR = %s, N = ARR.length;
  function render(t) {
    const col = io3((t - 2.85) / 0.5), out = smooth((t - 5.2) / 0.4);
    for (let i = 0; i < N; i++) {
      const el = $("nt" + i);
      const inK = clamp(backOut((t - ARR[i]) / 0.45, 1.6), 0, 1.15);
      let after = 0;
      for (let j = i + 1; j < N; j++) after += clamp(backOut((t - ARR[j]) / 0.45, 1.4), 0, 1.1);
      const listY = 110 * after;
      const rank = N - 1 - i, pileY = 12 * Math.min(rank, 3);
      const y = mix(listY, pileY, col) - 120 * (1 - Math.min(1, inK));
      gsap.set(el, { y: y, scale: mix(1, 1 - 0.05 * Math.min(rank, 4), col), opacity: (t > ARR[i] ? Math.min(1, (t - ARR[i]) * 6) : 0) * (rank > 3 ? 1 - col : 1) * (1 - out), zIndex: 10 + i });
    }
    const s = smooth((t - 3.3) / 0.3) * (1 - out);
    gsap.set("#sum", { opacity: s, scale: 0.94 + 0.06 * s, zIndex: 30 });
    let landed = 0; for (let i = 0; i < N; i++) landed += smooth((t - ARR[i] - 0.15) / 0.1);
    const n = t < 3.3 ? landed : landed + 7 * io3((t - 3.3) / 0.6);
    $("n13").textContent = Math.round(n * (1 - out));
    gsap.set("#om13", { scale: backOut((t - 3.9) / 0.45, 2.4) * (1 - out), opacity: t > 3.9 ? 1 - out : 0 });
    const pop = t > 3.4 ? Math.exp(-6 * (t - 3.4)) * Math.sin(Math.min(Math.PI, (t - 3.4) * 10)) : 0;
    gsap.set("#bd13", { scale: 1 + 0.25 * pop });
  }
""" % (ARR,)

# ---------------------------------------------------------------- 13 rings -> closed (three rings in a row)
RINGS = [("Konten", 30, "#00c9ff"), ("Leads", 120, "#ffffff"), ("Closing", 25, "#6fb6ff")]
RCX = [176, 476, 776]
S14_CSS = """
#sv14 { position:absolute; left:0; top:0; }
.rl { position:absolute; top:410px; width:240px; text-align:center; }
.rl .k { font-size:18px; letter-spacing:0.16em; color:#00c9ff; font-weight:700; }
.rl .v { font-size:36px; font-weight:700; margin-top:4px; }
.gh { position:absolute; left:0; right:0; top:516px; text-align:center; font-size:40px; }
.gh .hb { transform-origin:50% 50%; }
"""
_rsvg = ""
for i, (k, tgt, c) in enumerate(RINGS):
    cx = RCX[i]
    _rsvg += (f'<circle cx="{cx}" cy="240" r="110" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="30"/>'
              f'<circle id="ra{i}" cx="{cx}" cy="240" r="110" fill="none" stroke="{c}" stroke-width="30" stroke-linecap="round" transform="rotate(-90 {cx} 240)" stroke-dasharray="691.2" stroke-dashoffset="691.2"/>'
              f'<circle id="rt{i}" r="15" fill="{c}" filter="url(#gl14)"/>'
              + "".join(f'<line id="sp{i}_{j}" x1="{cx}" y1="100" x2="{cx}" y2="88" stroke="{c}" stroke-width="5" stroke-linecap="round" opacity="0"/>' for j in range(8)))
S14_VIS = f"""      <svg id="sv14" width="952" height="620" viewBox="0 0 952 620"><defs><filter id="gl14" x="-1" y="-1" width="3" height="3"><feGaussianBlur stdDeviation="3"/></filter></defs>{_rsvg}</svg>
""" + "".join(f'      <div class="rl" style="left:{RCX[i] - 120}px"><div class="k">{k.upper()}</div><div class="v w" id="rv{i}">0 / {tgt}</div></div>\n' for i, (k, tgt, c) in enumerate(RINGS)) + \
    '      <div class="gh"><span class="hb" id="gh14">Target bulan ini tercapai &#10003;</span></div>'
S14_JS = """
  const RCX = %s, TGT = %s, C = 691.2;
  function render(t) {
    const un = io3((t - 5.15) / 0.7);
    for (let i = 0; i < 3; i++) {
      const st = 0.35 + i * 0.55, p = io3((t - st) / 1.0) * (1 - un);
      $("ra" + i).setAttribute("stroke-dashoffset", (C * (1 - p)).toFixed(1));
      const a = -Math.PI / 2 + TAU * p, tip = $("rt" + i);
      tip.setAttribute("cx", (RCX[i] + 110 * Math.cos(a)).toFixed(1)); tip.setAttribute("cy", (240 + 110 * Math.sin(a)).toFixed(1));
      tip.setAttribute("opacity", p > 0.01 && p < 0.995 ? 1 : 0);
      $("rv" + i).textContent = Math.round(TGT[i] * p) + " / " + TGT[i];
      const bq = (t - st - 1.0) / 0.5;
      for (let j = 0; j < 8; j++) {
        const ang = j / 8 * TAU, r0 = 150 + 30 * clamp(bq, 0, 1), el = $("sp" + i + "_" + j);
        el.setAttribute("x1", (RCX[i] + r0 * Math.cos(ang)).toFixed(1)); el.setAttribute("y1", (240 + r0 * Math.sin(ang)).toFixed(1));
        el.setAttribute("x2", (RCX[i] + (r0 + 14) * Math.cos(ang)).toFixed(1)); el.setAttribute("y2", (240 + (r0 + 14) * Math.sin(ang)).toFixed(1));
        el.setAttribute("opacity", bq > 0 && bq < 1 ? (1 - bq).toFixed(3) : 0);
      }
    }
    const g = backOut((t - 2.75) / 0.5, 2.2) * (1 - smooth((t - 5.1) / 0.3));
    gsap.set("#gh14", { scale: Math.max(0, g), opacity: t > 2.75 ? 1 - smooth((t - 5.1) / 0.3) : 0 });
  }
""" % (RCX, [r[1] for r in RINGS])

# ---------------------------------------------------------------- 14 dock -> open (vertical dock left, window right)
ICON_Y = [96 + i * 84 for i in range(6)]
S15_CSS = """
.dock { position:absolute; left:40px; top:44px; width:124px; height:532px; border-radius:30px; background:rgba(255,255,255,0.08); border:1.5px solid rgba(255,255,255,0.2); }
.ico { position:absolute; left:62px; width:76px; height:76px; margin:-38px 0 0 -38px; border-radius:20px; display:flex; align-items:center; justify-content:center; box-shadow:0 10px 20px -8px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.4); transform-origin:0% 50%; }
#tip15 { position:absolute; left:186px; height:38px; padding:0 14px; border-radius:10px; background:#fff; color:#0b1440; font-size:17px; font-weight:700; display:flex; align-items:center; opacity:0; }
#w15 { position:absolute; left:210px; top:60px; width:700px; height:500px; border-radius:24px; background:linear-gradient(150deg,#1a3a80,#0d1850); border:1.5px solid rgba(255,255,255,0.25); box-shadow:0 40px 70px -30px rgba(0,0,0,0.8); overflow:hidden; }
#w15 .bar { height:54px; border-bottom:1.5px solid rgba(255,255,255,0.12); display:flex; align-items:center; gap:10px; padding:0 22px; }
#w15 .bar i { width:12px; height:12px; border-radius:50%; display:block; }
#w15 .bar span { margin-left:16px; font-size:20px; font-weight:700; color:#fff; }
#w15 .k { position:absolute; left:40px; top:90px; font-size:20px; color:#00c9ff; }
#w15 .n { position:absolute; left:36px; top:120px; font-size:150px; font-weight:700; letter-spacing:-0.05em; line-height:1.1; color:#fff; }
#w15 .up { position:absolute; left:46px; top:300px; font-size:22px; padding:6px 14px; }
#w15 svg { position:absolute; left:0; bottom:0; }
#cur15 { position:absolute; left:0; top:0; z-index:6; }
"""
_icons = [("linear-gradient(140deg,#ffffff,#c7d6f2)", '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="20" cy="20" r="15" fill="none" stroke="#0078ff" stroke-width="5"/><circle cx="20" cy="20" r="6" fill="#0078ff"/></svg>'),
          ("linear-gradient(140deg,#6b7a99,#3b4766)", '<svg width="40" height="40" viewBox="0 0 40 40"><path d="M8 13h24M8 27h24" stroke="#fff" stroke-width="4" stroke-linecap="round"/><circle cx="15" cy="13" r="5" fill="#fff"/><circle cx="26" cy="27" r="5" fill="#fff"/></svg>'),
          ("linear-gradient(140deg,#1b2350,#050a20)", '<svg width="40" height="40" viewBox="0 0 40 40"><path d="M20 4l4 12 12 4-12 4-4 12-4-12-12-4 12-4z" fill="#00c9ff"/></svg>'),
          ("linear-gradient(140deg,#5fe0ff,#0078ff)", '<svg width="40" height="40" viewBox="0 0 40 40"><rect x="7" y="20" width="6" height="13" rx="2" fill="#fff"/><rect x="17" y="13" width="6" height="20" rx="2" fill="#fff"/><rect x="27" y="6" width="6" height="27" rx="2" fill="#fff"/></svg>'),
          ("linear-gradient(140deg,#ffffff,#dbe6f8)", '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="20" cy="20" r="15" fill="#00c9ff"/><path d="M13 20l5 5 9-10" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>'),
          ("linear-gradient(140deg,#a9c8ff,#4f86e8)", '<svg width="40" height="40" viewBox="0 0 40 40"><rect x="6" y="9" width="28" height="22" rx="5" fill="#fff"/><path d="M9 28l8-9 6 6 4-4 6 7z" fill="#4f86e8"/><circle cx="27" cy="15" r="3" fill="#4f86e8"/></svg>')]
S15_VIS = '      <div class="dock"></div>\n' + "".join(f'      <div class="ico" id="ic{i}" style="top:{y}px;left:102px;background:{bg}">{g}</div>\n' for i, ((bg, g), y) in enumerate(zip(_icons, ICON_Y))) + f"""      <div id="tip15" style="top:{ICON_Y[3] - 19}px">Laporan</div>
      <div id="w15"><div class="bar"><i style="background:#ff6b6b"></i><i style="background:#ffd166"></i><i style="background:#00c9ff"></i><span>Laporan kampanye</span></div>
        <div class="k">Konversi iklan &middot; 30 hari</div><div class="n" id="n15">+0%</div><span class="hb up" id="up15">&uarr; naik dari bulan lalu</span>
        <svg width="700" height="170" viewBox="0 0 700 170"><defs><linearGradient id="wf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00c9ff" stop-opacity="0.35"/><stop offset="1" stop-color="#00c9ff" stop-opacity="0"/></linearGradient><clipPath id="wc"><rect id="wcr" x="0" y="0" width="0" height="170"/></clipPath></defs>
          <path clip-path="url(#wc)" d="M0 150 C90 140,150 120,230 126 S360 90,430 96 S560 50,700 24 L700 170 L0 170Z" fill="url(#wf)"/>
          <path id="wl" d="M0 150 C90 140,150 120,230 126 S360 90,430 96 S560 50,700 24" fill="none" stroke="#00c9ff" stroke-width="5" stroke-linecap="round"/></svg>
      </div>
      <svg id="cur15" width="36" height="44" viewBox="0 0 44 52"><path d="M4 3l0 38 10-9 7 16 7-3-7-15 14-1z" fill="#fff" stroke="#0b1440" stroke-width="3" stroke-linejoin="round"/></svg>"""
S15_JS = """
  const IY = %s;
  const wl = $("wl"), WL = wl.getTotalLength();
  function render(t) {
    const cy = t < 1.5 ? mix(40, IY[3], io3((t - 0.2) / 1.3)) : IY[3];
    const pres = env(t, 0.15, 2.0, 0.2);
    const bt = t - 1.55, bounce = bt > 0 && bt < 0.9 ? Math.abs(Math.sin(Math.PI * bt / 0.45)) * 30 * (1 - bt / 1.1) : 0;
    for (let i = 0; i < 6; i++) {
      const d = (IY[i] - cy) / 80, m = 1 + 0.45 * Math.exp(-d * d) * pres;
      gsap.set("#ic" + i, { scale: m, x: (i === 3 ? bounce : 0) + 14 * (m - 1) });
    }
    gsap.set("#tip15", { opacity: env(t, 1.0, 2.4, 0.15) });
    const open = clamp(backOut((t - 2.45) / 0.55, 1.3), 0, 1.06) * (1 - io3((t - 5.0) / 0.45));
    gsap.set("#w15", { scale: Math.max(0.02, open), opacity: smooth(open / 0.15), transformOrigin: "-108px " + (IY[3] - 60) + "px" });
    const num = io3((t - 2.9) / 0.9) * (1 - smooth((t - 5.0) / 0.2));
    $("n15").textContent = "+" + Math.round(38 * num) + "%%";
    const draw = io3((t - 3.0) / 0.9) * (1 - smooth((t - 5.0) / 0.2));
    wl.setAttribute("stroke-dasharray", (draw * WL).toFixed(1) + " " + (WL + 5).toFixed(1)); wl.style.opacity = draw > 0.01 ? 1 : 0;
    $("wcr").setAttribute("width", (700 * draw).toFixed(1));
    gsap.set("#up15", { scale: Math.max(0, backOut((t - 3.7) / 0.45, 2.4)) * (1 - smooth((t - 4.95) / 0.2)) });
    const cout = smooth((t - 2.3) / 0.4);
    gsap.set("#cur15", { x: 120 + 40 * cout, y: cy - 6 + 60 * cout, opacity: smooth((t - 0.1) / 0.2) * (1 - cout) });
  }
""" % (ICON_Y,)


def make(scene_body):
    return [
        dict(cid="s11", name="Sketch app", eyebrow="SCENE 10", page="11", css=S11_CSS, js=S11_JS,
             body=scene_body("Sketch", "app", "Sketsa yang berubah jadi aplikasi",
                             'Jendela dashboard berisi wireframe garis pensil. Handle vertikal menyapu dari kiri ke kanan dan membuka versi jadinya yang berwarna (<span class="ph">&ldquo;[nama app kamu]&rdquo;</span>, <span class="ph">[2&ndash;3 isi layarnya]</span>).',
                             ["Progres Kelas", "ring 86%", "2 kartu"], S11_VIS)),
        dict(cid="s12", name="Drag booked", eyebrow="SCENE 11", page="12", css=S12_CSS, js=S12_JS,
             body=scene_body("Drag", "booked", "Jadwal yang ditarik ke tempatnya",
                             'Kalender 3 hari. Kursor menarik event <span class="ph">&ldquo;[event kamu]&rdquo;</span> dari tray &ldquo;belum dijadwalkan&rdquo; ke <span class="ph">[hari &amp; jam]</span>, event nempel ke slot-nya, berubah putih, dan avatar kecil muncul.',
                             ["Live Q&amp;A AIpreneur", "Rabu 10.00"], S12_VIS)),
        dict(cid="s13", name="Alerts stack", eyebrow="SCENE 12", page="13", css=S13_CSS, js=S13_JS,
             body=scene_body("Alerts", "stack", "Notifikasi yang menumpuk",
                             'Notifikasi masuk satu per satu dengan spring (<span class="ph">&ldquo;[notif 1]&rdquo;</span>, <span class="ph">&ldquo;[notif 2]&rdquo;</span>), lalu menumpuk rapi jadi satu, dan counter di kiri naik ke <span class="ph">&ldquo;[total kamu]&rdquo;</span>.',
                             ["Order baru Rp149.000", "12 order", "omzet Rp2,1jt"], S13_VIS)),
        dict(cid="s14", name="Rings closed", eyebrow="SCENE 13", page="14", css=S14_CSS, js=S14_JS,
             body=scene_body("Rings", "closed", "Ring target yang tertutup",
                             'Tiga ring target berjajar. Tiap ring berputar dengan ujung bercahaya, menutup dengan percikan kecil, lalu <span class="ph">&ldquo;[kalimat target kamu]&rdquo;</span> muncul di bawahnya.',
                             ["Konten 30", "Leads 120", "Closing 25"], S14_VIS)),
        dict(cid="s15", name="Dock open", eyebrow="SCENE 14", page="15", css=S15_CSS, js=S15_JS,
             body=scene_body("Dock", "open", "Dock yang membuka laporan",
                             'Dock vertikal berisi 6 ikon glossy. Kursor turun menyusuri dock, ikonnya membesar, satu ikon memantul, lalu jendela <span class="ph">&ldquo;[judul jendela kamu]&rdquo;</span> terbuka dari ikon itu.',
                             ["Laporan kampanye", "+38%"], S15_VIS)),
    ]

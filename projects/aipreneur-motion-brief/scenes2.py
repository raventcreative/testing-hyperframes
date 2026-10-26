"""Scenes 05-09 for the Motion brief carousel. make(scene_body) -> list of slide dicts."""
import json

# ---------------------------------------------------------------- 05 visits -> sales (funnel left, counter right)
S6_CSS = """
#cv6 { position:absolute; left:0; top:0; }
.cnt { position:absolute; left:560px; top:150px; width:350px; height:320px; border-radius:28px; background:linear-gradient(150deg,rgba(255,255,255,0.14),rgba(255,255,255,0.05)); border:1.5px solid rgba(255,255,255,0.22); box-shadow:inset 0 1px 0 rgba(255,255,255,0.25), 0 30px 60px -28px rgba(0,0,0,0.6); }
.cnt .k { position:absolute; left:34px; top:34px; font-size:16px; letter-spacing:0.2em; color:#00c9ff; font-weight:700; }
.cnt .n { position:absolute; left:30px; top:66px; font-size:120px; line-height:1.1; font-weight:700; letter-spacing:-0.04em; }
.cnt .u { position:absolute; left:36px; top:204px; font-size:28px; color:#00c9ff; font-weight:700; }
.cnt .f { position:absolute; left:36px; top:254px; font-size:18px; }
.vin { position:absolute; left:60px; top:36px; font-size:18px; letter-spacing:0.16em; font-weight:700; color:rgba(255,255,255,0.7); }
"""
S6_VIS = """      <canvas id="cv6" width="1904" height="1240" style="width:952px;height:620px"></canvas>
      <div class="vin">12.000 VISIT &darr;</div>
      <div class="cnt"><div class="k">HASIL</div><div class="n w" id="n6">0</div><div class="u">penjualan</div><div class="f"><span class="hb" id="cv">konversi 5%</span></div></div>"""
S6_JS = """
  const cv = $("cv6"), ctx = cv.getContext("2d");
  const FX = 300, RIM = 150, RX = 200, RY = 44, SP = 420, SPW = 16;
  let seed = 5; const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
  const P = [...Array(240)].map((_, i) => ({ off: rnd() * 2, x0: FX + (rnd() * 2 - 1) * (RX - 20), wob: rnd() * TAU, keep: i % 7 === 0, r: 2.2 + rnd() * 2.2 }));
  function funnelX(y, s) { const k = clamp((y - RIM) / (SP - RIM), 0, 1); return FX + s * mix(RX, SPW, Math.pow(k, 0.7)); }
  const fmt = (v) => Math.round(v).toString().replace(/\\B(?=(\\d{3})+(?!\\d))/g, ".");
  function render(t) {
    ctx.setTransform(2, 0, 0, 2, 0, 0); ctx.clearRect(0, 0, 952, 620);
    const flow = smooth((t - 0.3) / 0.4) * (1 - smooth((t - 4.6) / 0.5));
    // glass body
    ctx.beginPath(); ctx.moveTo(FX - RX, RIM);
    for (let y = RIM; y <= SP; y += 6) ctx.lineTo(funnelX(y, -1), y);
    ctx.lineTo(FX - SPW, SP + 50); ctx.lineTo(FX + SPW, SP + 50);
    for (let y = SP; y >= RIM; y -= 6) ctx.lineTo(funnelX(y, 1), y);
    ctx.closePath();
    const g = ctx.createLinearGradient(FX - RX, 0, FX + RX, 0);
    g.addColorStop(0, "rgba(255,255,255,0.16)"); g.addColorStop(0.45, "rgba(255,255,255,0.04)"); g.addColorStop(1, "rgba(255,255,255,0.12)");
    ctx.fillStyle = g; ctx.fill(); ctx.strokeStyle = "rgba(255,255,255,0.35)"; ctx.lineWidth = 1.5; ctx.stroke();
    ctx.strokeStyle = "rgba(255,255,255,0.4)"; ctx.beginPath(); ctx.ellipse(FX, RIM, RX, RY, 0, Math.PI, TAU); ctx.stroke();
    // particles
    for (const p of P) {
      const u = ((t + p.off) % 2) / 2;
      let x, y, a = flow, col = "200,235,255";
      if (u < 0.3) { const k = u / 0.3; x = p.x0 + 6 * Math.sin(p.wob + t * 3); y = mix(-10, RIM + 10, k * k); }
      else if (u < 0.7) { const k = (u - 0.3) / 0.4; y = mix(RIM + 10, SP + 10, k); const s = (p.x0 - FX) / RX; x = FX + s * (funnelX(y, 1) - FX) * 0.85 + 8 * Math.sin(p.wob + k * 9) * (1 - k); }
      else { if (!p.keep) continue; const k = (u - 0.7) / 0.3; x = FX + 3 * Math.sin(p.wob); y = mix(SP + 20, 600, k); col = "0,201,255"; a *= 1 - k * 0.6; }
      if (!p.keep && u > 0.62) a *= 1 - (u - 0.62) / 0.08;
      ctx.fillStyle = "rgba(" + col + "," + clamp(a, 0, 1).toFixed(3) + ")";
      ctx.beginPath(); ctx.arc(x, y, p.r, 0, TAU); ctx.fill();
    }
    // front rim + spout ring
    ctx.strokeStyle = "rgba(255,255,255,0.7)"; ctx.lineWidth = 2; ctx.beginPath(); ctx.ellipse(FX, RIM, RX, RY, 0, 0, Math.PI); ctx.stroke();
    ctx.fillStyle = "rgba(255,255,255,0.55)"; ctx.fillRect(FX - SPW - 3, SP - 6, 2 * SPW + 6, 12);
    const gl = ctx.createRadialGradient(FX, SP + 80, 0, FX, SP + 80, 120);
    gl.addColorStop(0, "rgba(0,201,255," + (0.35 * flow).toFixed(3) + ")"); gl.addColorStop(1, "rgba(0,201,255,0)");
    ctx.fillStyle = gl; ctx.fillRect(FX - 140, SP - 40, 280, 240);
    const n = t < 5.5 ? 600 * io3((t - 0.9) / 3.4) : 600 * (1 - io3((t - 5.5) / 0.45));
    $("n6").textContent = fmt(n);
    gsap.set("#cv", { scale: backOut((t - 4.3) / 0.45, 2.4) * (1 - smooth((t - 5.45) / 0.2)), opacity: t > 4.3 && t < 5.65 ? 1 : 0 });
  }
"""

# ---------------------------------------------------------------- 06 click -> done (post composer)
S7_CSS = """
.cmp { position:absolute; left:70px; top:60px; width:812px; height:500px; border-radius:28px; background:linear-gradient(150deg,rgba(255,255,255,0.13),rgba(255,255,255,0.05)); border:1.5px solid rgba(255,255,255,0.22); box-shadow:inset 0 1px 0 rgba(255,255,255,0.25), 0 30px 60px -28px rgba(0,0,0,0.6); }
.cmp .av2 { position:absolute; left:36px; top:34px; width:64px; height:64px; border-radius:50%; background:#fff; color:#0b1440; font-weight:700; font-size:22px; display:flex; align-items:center; justify-content:center; }
.cmp .nm { position:absolute; left:118px; top:38px; font-size:26px; font-weight:700; }
.cmp .hd { position:absolute; left:118px; top:72px; font-size:17px; color:#00c9ff; }
.cmp .tx { position:absolute; left:36px; top:132px; right:36px; font-size:27px; line-height:1.5; }
.cmp .att { position:absolute; left:36px; top:270px; width:300px; height:110px; border-radius:18px; background:linear-gradient(135deg,rgba(0,201,255,0.5),rgba(40,90,255,0.35)); border:1.5px solid rgba(255,255,255,0.25); }
.cmp .att2 { left:352px; background:linear-gradient(135deg,rgba(255,255,255,0.25),rgba(255,255,255,0.08)); }
#btn7 { position:absolute; left:452px; top:392px; width:340px; height:84px; }
#bbg { position:absolute; inset:0; border-radius:42px; }
.bl { position:absolute; left:0; right:0; top:0; line-height:84px; text-align:center; font-size:32px; font-weight:700; white-space:nowrap; }
#ring7 { position:absolute; left:128px; top:0; }
#rip { position:absolute; left:110px; top:-18px; width:120px; height:120px; border-radius:50%; border:3px solid #00c9ff; opacity:0; }
#cur7 { position:absolute; left:0; top:0; z-index:5; }
"""
S7_VIS = """      <div class="cmp">
        <div class="av2">FK</div><div class="nm w">Freddie Kashawan</div><div class="hd">Postingan baru &middot; Instagram</div>
        <div class="tx w r">5 prompt AI yang aku pakai tiap hari buat bikin konten bisnis. Simpan dulu, pakai nanti.</div>
        <div class="att"></div><div class="att att2"></div>
        <div id="btn7"><div id="rip"></div><div id="bbg"></div>
          <div class="bl w" id="lb0">Posting</div>
          <div class="bl" id="lb1" style="color:#0b1440">&#10003; Terposting</div>
          <svg id="ring7" width="84" height="84" viewBox="0 0 84 84"><circle cx="42" cy="42" r="30" fill="none" stroke="rgba(11,20,64,0.12)" stroke-width="6"/>
            <circle id="arc7" cx="42" cy="42" r="30" fill="none" stroke="#00c9ff" stroke-width="6" stroke-linecap="round" transform="rotate(-90 42 42)" stroke-dasharray="188.5" stroke-dashoffset="188.5"/>
            <path id="arr7" d="M42 54V30M32 40l10-10 10 10" fill="none" stroke="#0b1440" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
            <path id="tk7" d="M29 43l9 9 18-19" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="40" stroke-dashoffset="40"/></svg>
        </div>
      </div>
      <svg id="cur7" width="40" height="48" viewBox="0 0 44 52"><path d="M4 3l0 38 10-9 7 16 7-3-7-15 14-1z" fill="#fff" stroke="#0b1440" stroke-width="3" stroke-linejoin="round"/></svg>"""
S7_JS = """
  const CY = [0, 201, 255], WH = [255, 255, 255];
  const mc = (a, b, k) => a.map((v, i) => Math.round(v + (b[i] - v) * k));
  function render(t) {
    // inset per side: pill 20, circle 128, done 0
    let ins;
    if (t < 0.95) ins = 20;
    else if (t < 1.35) ins = mix(20, 128, io3((t - 0.95) / 0.4));
    else if (t < 2.9) ins = 128;
    else if (t < 5.3) ins = mix(128, 0, clamp(backOut((t - 2.9) / 0.5, 1.4), 0, 1.1));
    else ins = mix(0, 20, io3((t - 5.3) / 0.4));
    ins = Math.max(-6, ins);
    const toWhite = smooth((t - 1.0) / 0.3) * (t < 5.3 ? 1 : 1 - smooth((t - 5.3) / 0.3));
    const cyanTick = env(t, 2.35, 3.05, 0.1);
    const bg = mc(mc(CY, WH, toWhite), CY, cyanTick);
    const b = $("bbg");
    b.style.background = "rgb(" + bg + ")";
    b.style.clipPath = "inset(0 " + ins.toFixed(1) + "px round 42px)";
    b.style.boxShadow = "0 18px 36px -14px rgba(0,201,255," + (0.5 + 0.3 * cyanTick).toFixed(2) + ")";
    const press = env(t, 0.75, 0.95, 0.06);
    gsap.set("#btn7", { scale: 1 - 0.06 * press });
    gsap.set("#lb0", { opacity: (1 - smooth((t - 0.95) / 0.15)) + smooth((t - 5.45) / 0.25) });
    gsap.set("#lb1", { opacity: smooth((t - 3.1) / 0.25) * (1 - smooth((t - 5.25) / 0.2)) });
    const ringOn = env(t, 1.3, 2.4, 0.1);
    gsap.set("#ring7", { opacity: Math.max(ringOn, cyanTick) });
    $("arc7").setAttribute("stroke-dashoffset", (188.5 * (1 - io3((t - 1.4) / 0.95))).toFixed(1));
    $("arc7").style.opacity = ringOn; $("arr7").style.opacity = ringOn;
    $("tk7").setAttribute("stroke-dashoffset", (40 * (1 - smooth((t - 2.45) / 0.25))).toFixed(1));
    $("tk7").style.opacity = cyanTick;
    const rq = (t - 2.4) / 0.7;
    gsap.set("#rip", { opacity: rq > 0 && rq < 1 ? 0.9 * (1 - rq) : 0, scale: 0.7 + 1.1 * clamp(rq, 0, 1) });
    // cursor
    const cin = io3((t - 0.1) / 0.6), cout = smooth((t - 1.05) / 0.3);
    gsap.set("#cur7", { x: mix(860, 680, cin), y: mix(600, 480, cin) + 60 * cout, opacity: smooth((t - 0.05) / 0.15) * (1 - cout), scale: 1 - 0.12 * press });
  }
"""

# ---------------------------------------------------------------- 07 card -> paid (pocket left, receipt right)
S8_CSS = """
.pk { position:absolute; left:70px; top:250px; width:440px; height:300px; }
#card8 { position:absolute; left:30px; top:-20px; width:380px; height:236px; border-radius:24px; background:linear-gradient(125deg,#5fe0ff,#00a2ff 45%,#2a5bd7); box-shadow:0 20px 40px -18px rgba(0,0,0,0.6); }
#card8 .chip { position:absolute; left:30px; top:34px; width:54px; height:40px; border-radius:9px; background:linear-gradient(135deg,#f4f7fc,#aab9d1 60%,#dfe7f3); }
#card8 .nfc { position:absolute; right:30px; top:38px; width:44px; height:28px; }
#card8 .nfc i { position:absolute; top:0; width:28px; height:28px; border-radius:50%; background:rgba(255,255,255,0.85); }
#card8 .num { position:absolute; left:30px; top:100px; font-size:24px; letter-spacing:0.12em; color:#fff; font-weight:700; }
.pocket { position:absolute; left:0; top:80px; width:440px; height:220px; border-radius:30px; background:linear-gradient(170deg,rgba(150,190,255,0.35),rgba(30,60,140,0.55)); border:1.5px solid rgba(255,255,255,0.3); -webkit-backdrop-filter:blur(14px); backdrop-filter:blur(14px); box-shadow:inset 0 1px 0 rgba(255,255,255,0.35), 0 30px 50px -24px rgba(0,0,0,0.7); }
#pay { position:absolute; left:40px; top:108px; width:360px; height:80px; }
#pbg { position:absolute; inset:0; border-radius:40px; background:linear-gradient(100deg,#00c9ff,#2a7bff); box-shadow:0 14px 30px -12px rgba(0,201,255,0.8); }
#pok { position:absolute; inset:0; border-radius:40px; background:#fff; opacity:0; }
.pl { position:absolute; left:0; right:0; top:0; line-height:80px; text-align:center; font-size:30px; font-weight:700; white-space:nowrap; }
#lite { position:absolute; left:-8px; top:-8px; overflow:visible; }
.rc { position:absolute; left:560px; top:70px; width:340px; height:480px; border-radius:26px; background:rgba(255,255,255,0.07); border:1.5px dashed rgba(255,255,255,0.3); padding:30px; }
.rc .k { font-size:15px; letter-spacing:0.2em; color:#00c9ff; font-weight:700; }
.rc .row { display:flex; justify-content:space-between; font-size:19px; margin-top:20px; }
.rc .row span:first-child { color:rgba(255,255,255,0.7); }
.rc .tot { margin-top:30px; padding-top:22px; border-top:1.5px dashed rgba(255,255,255,0.3); }
.rc .tot .a { font-size:46px; font-weight:700; letter-spacing:-0.02em; margin-top:6px; }
.rc .stt { position:absolute; left:30px; bottom:30px; width:280px; height:56px; }
.rc .stt div { position:absolute; inset:0; border-radius:16px; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:700; }
#s8a { border:1.5px solid rgba(255,255,255,0.4); color:#fff; }
#s8b { background:#fff; color:#0b1440; opacity:0; }
"""
S8_VIS = """      <div class="pk">
        <div id="card8"><div class="chip"></div><div class="nfc"><i style="left:0"></i><i style="left:16px;opacity:0.7"></i></div><div class="num">&bull;&bull;&bull;&bull; 4417</div></div>
        <div class="pocket">
          <div id="pay"><svg id="lite" width="376" height="96" viewBox="0 0 376 96"><rect id="lr" x="4" y="4" width="368" height="88" rx="44" fill="none" stroke="#ffffff" stroke-width="5" stroke-linecap="round" stroke-dasharray="120 900" opacity="0"/></svg>
            <div id="pbg"></div><div id="pok"></div>
            <div class="pl w" id="pl0">Bayar Rp4,85jt</div><div class="pl" id="pl1" style="color:#0b1440;opacity:0">&#10003; Lunas</div></div>
        </div>
      </div>
      <div class="rc"><div class="k">RINGKASAN</div>
        <div class="row"><span>Program</span><span class="w b">AIpreneur Pro</span></div>
        <div class="row"><span>Durasi</span><span class="w b">12 bulan</span></div>
        <div class="row"><span>Kartu</span><span class="w b">&bull;&bull;&bull;&bull; 4417</span></div>
        <div class="tot"><div style="font-size:16px;color:rgba(255,255,255,0.7)">Total</div><div class="a w">Rp4.850.000</div></div>
        <div class="stt"><div id="s8a">Menunggu&hellip;</div><div id="s8b">&#10003; Lunas</div></div></div>"""
S8_JS = """
  function render(t) {
    const up = clamp(backOut((t - 0.3) / 0.55, 1.6), 0, 1.1) * (1 - io3((t - 2.6) / 0.5));
    gsap.set("#card8", { y: -120 * up, rotation: -3 * up });
    const L = 2 * (368 - 88) + Math.PI * 88;
    const lr = $("lr"), lp = clamp((t - 0.95) / 1.25, 0, 1);
    lr.setAttribute("stroke-dashoffset", (-lp * L * 2).toFixed(1));
    lr.setAttribute("stroke-dasharray", "120 " + (L - 120).toFixed(1));
    lr.setAttribute("opacity", env(t, 0.95, 2.2, 0.12).toFixed(3));
    const ok = smooth((t - 2.25) / 0.2) * (1 - smooth((t - 5.3) / 0.25));
    gsap.set("#pok", { opacity: ok }); gsap.set("#pl1", { opacity: ok }); gsap.set("#pl0", { opacity: 1 - ok });
    const pop = t > 2.25 ? Math.exp(-6 * (t - 2.25)) * Math.sin(Math.min(Math.PI, (t - 2.25) * 10)) : 0;
    gsap.set("#pay", { scale: 1 + 0.07 * pop });
    const st = smooth((t - 2.35) / 0.2) * (1 - smooth((t - 5.35) / 0.25));
    gsap.set("#s8b", { opacity: st, scale: 0.9 + 0.1 * st }); gsap.set("#s8a", { opacity: 1 - st });
  }
"""

# ---------------------------------------------------------------- 08 0 -> 12.480 (big left-aligned number + sparkline)
TARGET = "12480"
SPINS = [1, 1, 2, 2, 3]
S9_CSS = """
.ic9 { position:absolute; left:56px; top:50px; width:60px; height:60px; border-radius:16px; background:#fff; display:flex; align-items:center; justify-content:center; }
.lb9 { position:absolute; left:134px; top:58px; font-size:30px; font-weight:700; }
.lv9 { position:absolute; right:56px; top:68px; display:flex; align-items:center; gap:10px; font-size:17px; color:#00c9ff; font-weight:700; letter-spacing:0.14em; }
.lv9 i { width:12px; height:12px; border-radius:50%; background:#00c9ff; display:block; }
.num9 { position:absolute; left:50px; top:140px; display:flex; height:200px; }
.dg9 { width:136px; height:200px; overflow:hidden; }
.dg9 .strip { display:block; }
.dg9 .strip span { display:block; height:200px; line-height:200px; font-size:210px; font-weight:700; letter-spacing:-0.04em; text-align:center; color:#fff; }
.sep9 { width:56px; height:200px; line-height:200px; font-size:210px; font-weight:700; color:#00c9ff; text-align:center; }
.chip9 { position:absolute; left:56px; top:372px; font-size:24px; padding:8px 18px; transform-origin:0 50%; }
#spk { position:absolute; left:40px; top:440px; }
"""
_strip = "".join(f"<span>{d % 10}</span>" for d in range(11))
_num9 = ""
for i, ch in enumerate(TARGET):
    _num9 += f'<div class="dg9" data-layout-allow-overflow data-layout-allow-overlap><div class="strip" id="g{i}">{_strip}</div></div>'
    if i == 1:
        _num9 += '<div class="sep9">.</div>'
S9_VIS = f"""      <div class="ic9"><svg width="34" height="30" viewBox="0 0 34 30"><circle cx="12" cy="9" r="6" fill="#0b1440"/><path d="M1 28c0-6 5-10 11-10s11 4 11 10z" fill="#0b1440"/><circle cx="25" cy="10" r="4.5" fill="#00c9ff"/><path d="M21 19c1-1 3-1.5 4-1.5 4.5 0 8 3 8 8.5h-8" fill="#00c9ff"/></svg></div>
      <div class="lb9 w">Member komunitas</div>
      <div class="lv9"><i id="lv9"></i>LIVE</div>
      <div class="num9">{_num9}</div>
      <span class="hb chip9" id="chip9">&uarr; +18% bulan ini</span>
      <svg id="spk" width="872" height="150" viewBox="0 0 872 150">
        <defs><linearGradient id="sf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00c9ff" stop-opacity="0.35"/><stop offset="1" stop-color="#00c9ff" stop-opacity="0"/></linearGradient><clipPath id="sc"><rect id="scr" x="0" y="0" width="0" height="150"/></clipPath></defs>
        <path clip-path="url(#sc)" d="M0 128 C80 120,120 104,190 108 S300 80,370 86 S480 52,560 58 S700 22,872 10 L872 150 L0 150Z" fill="url(#sf)"/>
        <path id="spl" d="M0 128 C80 120,120 104,190 108 S300 80,370 86 S480 52,560 58 S700 22,872 10" fill="none" stroke="#00c9ff" stroke-width="5" stroke-linecap="round"/>
      </svg>"""
S9_JS = """
  const T = %s, SP = %s, N = T.length;
  const spl = $("spl"), SL = spl.getTotalLength();
  function pos(t, i) {
    const tgt = T[i] + 10 * SP[i];
    if (t < 0.45) return tgt;
    if (t < 0.95) return tgt * (1 - io3((t - 0.45) / 0.5));
    const d = 1.0 + (N - 1 - i) * 0.12;
    return tgt * io3((t - d) / (1.5 + 0.12 * i));
  }
  function render(t) {
    for (let i = 0; i < N; i++) {
      const p = pos(t, i), p0 = pos(Math.max(0, t - 1 / 30), i), v = Math.abs(p - p0) * 30;
      const g = $("g" + i), m = ((p %% 10) + 10) %% 10;
      g.style.transform = "translateY(" + (-m * 200).toFixed(1) + "px)";
      g.style.filter = v > 2 ? "blur(" + Math.min(8, v / 4).toFixed(1) + "px)" : "none";
    }
    const vis = t < 0.45 ? 1 - smooth(t / 0.3) : smooth((t - 3.0) / 0.3);
    const draw = t < 0.45 ? 1 - smooth(t / 0.35) : io3((t - 2.7) / 0.9);
    spl.setAttribute("stroke-dasharray", (draw * SL).toFixed(1) + " " + (SL + 5).toFixed(1));
    $("scr").setAttribute("width", (872 * draw).toFixed(1)); spl.style.opacity = draw > 0.01 ? 1 : 0;
    const ck = t < 0.45 ? 1 - smooth(t / 0.25) : backOut((t - 3.2) / 0.45, 2.4);
    gsap.set("#chip9", { scale: Math.max(0, ck), opacity: ck > 0.01 ? 1 : 0 });
    const pulse = 0.5 + 0.5 * Math.sin(TAU * t / 1.5);
    $("lv9").style.boxShadow = "0 0 0 " + (3 + 7 * pulse).toFixed(1) + "px rgba(0,201,255," + (0.4 - 0.3 * pulse).toFixed(2) + ")";
  }
""" % (json.dumps([int(c) for c in TARGET]), json.dumps(SPINS))

# ---------------------------------------------------------------- 09 weight -> bold (text left, vertical slider right)
LINES10 = ["Bikin", "hidup."]
S10_CSS = """
.hl10 { position:absolute; left:60px; top:70px; }
.ln10 { display:block; height:200px; white-space:nowrap; font-size:176px; line-height:200px; letter-spacing:-0.03em; }
.ch { position:relative; display:inline-block; }
.ch .bb { font-weight:700; color:#fff; opacity:0; }
.ch .rr { position:absolute; left:0; right:0; top:0; text-align:center; font-weight:400; color:#fff; }
#dot10 { position:absolute; left:50%; margin-left:-17px; top:128px; width:34px; height:34px; border-radius:50%; background:radial-gradient(circle at 35% 30%,#bff3ff,#00c9ff 50%,#0078ff); box-shadow:0 0 24px rgba(0,201,255,0.8); opacity:0; }
.sl10 { position:absolute; left:790px; top:70px; width:110px; height:480px; }
.sl10 .tr { position:absolute; left:47px; top:60px; width:14px; height:340px; border-radius:7px; background:rgba(255,255,255,0.15); }
#sfill { position:absolute; left:47px; top:60px; width:14px; height:340px; border-radius:7px; background:linear-gradient(0deg,#0078ff,#00c9ff); transform-origin:50% 100%; }
#knob { position:absolute; left:32px; top:385px; width:44px; height:44px; border-radius:50%; background:#fff; box-shadow:0 6px 18px rgba(0,0,0,0.4); margin-top:-22px; }
.sl10 .k { position:absolute; left:0; right:0; top:0; text-align:center; font-size:15px; letter-spacing:0.18em; color:#00c9ff; font-weight:700; }
.sl10 .v { position:absolute; left:0; right:0; top:430px; text-align:center; font-size:30px; font-weight:700; }
"""
_chars = []
idx = 0
for li, ln in enumerate(LINES10):
    parts = []
    for ch in ln:
        if ch == ".":
            parts.append(f'<span class="ch" id="per"><span class="bb">.</span><span class="rr" id="perr">.</span><span id="dot10"></span></span>')
        else:
            parts.append(f'<span class="ch" id="c{idx}"><span class="bb">{ch}</span><span class="rr">{ch}</span></span>')
            idx += 1
    _chars.append(f'<span class="ln10">{"".join(parts)}</span>')
NCH = idx
S10_VIS = f"""      <div class="hl10" id="hl10">{''.join(_chars)}</div>
      <div class="sl10"><div class="k">WEIGHT</div><div class="tr"></div><div id="sfill"></div><div id="knob"></div><div class="v w" id="wv">400</div></div>"""
S10_JS = """
  const NCH = %d;
  const ch = [...Array(NCH)].map((_, i) => $("c" + i));
  function wk(t, i) {
    const a = smooth((t - 0.5 - i * 0.12) / 0.45);
    const b = smooth((t - 4.2 - (NCH - 1 - i) * 0.1) / 0.45);
    return a * (1 - b);
  }
  let dotPos = null;
  function render(t) {
    let sum = 0;
    ch.forEach((el, i) => {
      const k = wk(t, i); sum += k;
      el.children[0].style.opacity = k; el.children[1].style.opacity = 1 - k;
      const br = Math.sin(TAU * (t / 1.6) + i * 0.6) * 0.02 * k;
      gsap.set(el, { scaleY: 1 + br, transformOrigin: "50%% 80%%" });
    });
    const avg = sum / NCH;
    const per = $("per"), dk = env(t, 2.35, 4.15, 0.12);
    per.children[0].style.opacity = 0; per.children[1].style.opacity = 1 - dk;
    const bt = t - 2.45, bounce = bt > 0 && bt < 1.2 ? Math.abs(Math.sin(Math.PI * bt / 0.6)) * 60 * Math.exp(-2 * bt) : 0;
    gsap.set("#dot10", { y: -bounce, opacity: dk, scale: 0.6 + 0.4 * smooth((t - 2.35) / 0.2) });
    gsap.set("#sfill", { scaleY: Math.max(0.02, avg) });
    $("knob").style.top = (400 - 340 * avg).toFixed(1) + "px";
    $("wv").textContent = Math.round(400 + 300 * avg);
  }
""" % NCH


def make(scene_body):
    return [
        dict(cid="s6", name="Visits sales", eyebrow="SCENE 05", page="06", css=S6_CSS, js=S6_JS,
             body=scene_body("Visits", "sales", "Visitor yang mengalir jadi penjualan",
                             'Corong kaca 3D. Ratusan partikel kecil masuk dari atas, cuma sedikit yang keluar di bawah, dan counter naik sampai <span class="ph">&ldquo;[hasil kamu]&rdquo;</span>.',
                             ["600 penjualan", "konversi 5%"], S6_VIS)),
        dict(cid="s7", name="Click done", eyebrow="SCENE 06", page="07", css=S7_CSS, js=S7_JS,
             body=scene_body("Click", "done", "Tombol yang diklik sampai selesai",
                             'Tombol <span class="ph">&ldquo;[kata tombol kamu]&rdquo;</span> diklik kursor, menyusut jadi lingkaran dengan progress ring, berubah jadi centang dengan ripple, lalu melebar jadi <span class="ph">&ldquo;[kata selesai]&rdquo;</span>.',
                             ["Posting", "Terposting"], S7_VIS)),
        dict(cid="s8", name="Card paid", eyebrow="SCENE 07", page="08", css=S8_CSS, js=S8_JS,
             body=scene_body("Card", "paid", "Kartu yang langsung lunas",
                             'Kartu keluar dari saku kaca, cahaya berputar mengelilingi tombol &ldquo;Bayar <span class="ph">[nominal kamu]</span>&rdquo;, lalu berubah jadi &ldquo;Lunas&rdquo; dan kartu masuk lagi. Struk di samping ikut update.',
                             ["Rp4.850.000", "AIpreneur Pro"], S8_VIS)),
        dict(cid="s9", name="Counter", eyebrow="SCENE 08", page="09", css=S9_CSS, js=S9_JS,
             body=scene_body("0", "12.480", "Counter yang naik ke angka kamu",
                             'Widget <span class="ph">&ldquo;[metrik kamu]&rdquo;</span>. Tiap digit berputar sendiri kayak odometer dengan blur di digit yang cepat, sampai ke <span class="ph">[angka kamu]</span>, lalu chip <span class="ph">&ldquo;[kenaikan]&rdquo;</span> muncul.',
                             ["Member komunitas", "12.480", "+18% bulan ini"], S9_VIS)),
        dict(cid="s10", name="Weight bold", eyebrow="SCENE 09", page="10", css=S10_CSS, js=S10_JS,
             body=scene_body("Weight", "bold", "Headline yang berubah ketebalan",
                             'Headline <span class="ph">&ldquo;[headline kamu]&rdquo;</span> berubah dari tipis ke tebal huruf per huruf kayak ombak, hurufnya bernapas, dan titiknya jadi bola cyan yang memantul.',
                             ["Bikin hidup."], S10_VIS)),
    ]

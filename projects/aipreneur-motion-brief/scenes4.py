"""Cover, scenes 15-16 and the CTA. make(scene_body) -> (cover, [scene15, scene16, cta])."""
import json
from pathlib import Path

IDN = json.loads((Path(__file__).parent / "idn.json").read_text())

# ---------------------------------------------------------------- 15 card -> 360 (card left, info right)
S16_CSS = """
.stage16 { position:absolute; left:70px; top:40px; width:400px; height:540px; perspective:1600px; }
#card16 { position:absolute; inset:0; transform-style:preserve-3d; }
.face { position:absolute; inset:0; border-radius:30px; backface-visibility:hidden; -webkit-backface-visibility:hidden; overflow:hidden;
  background:linear-gradient(160deg,rgba(255,255,255,0.18),rgba(255,255,255,0.06)); border:1.5px solid rgba(255,255,255,0.28); box-shadow:inset 0 1px 0 rgba(255,255,255,0.3); }
.face.back { transform:rotateY(180deg); }
.prod { position:absolute; left:24px; top:24px; right:24px; height:290px; border-radius:22px; background:radial-gradient(circle at 50% 40%, rgba(0,201,255,0.45), rgba(0,201,255,0) 65%), linear-gradient(160deg,#1c3f8c,#0d1850); display:flex; align-items:center; justify-content:center; }
.pname { position:absolute; left:32px; top:338px; font-size:22px; color:#00c9ff; }
.price16 { position:absolute; left:28px; top:370px; font-size:76px; font-weight:700; letter-spacing:-0.03em; line-height:1.1; }
.price16 small { font-size:32px; color:#00c9ff; margin-right:6px; vertical-align:30px; }
.plus { position:absolute; right:30px; top:394px; width:66px; height:66px; border-radius:50%; background:#fff; color:#0b1440; font-size:38px; font-weight:700; display:flex; align-items:center; justify-content:center; box-shadow:0 12px 26px -10px rgba(0,201,255,0.8); }
.sold { position:absolute; left:32px; top:470px; font-size:17px; color:rgba(255,255,255,0.7); }
.back .k { position:absolute; left:32px; top:36px; font-size:15px; letter-spacing:0.2em; color:#00c9ff; font-weight:700; }
.back .bt { position:absolute; left:30px; top:62px; font-size:34px; font-weight:700; }
.feat { position:absolute; left:24px; right:24px; height:92px; border-radius:20px; background:rgba(255,255,255,0.08); border:1.5px solid rgba(255,255,255,0.16); display:flex; align-items:center; gap:16px; padding:0 20px; font-size:21px; font-weight:700; }
.feat i { width:40px; height:40px; border-radius:50%; border:2.5px solid rgba(255,255,255,0.4); flex:none; display:flex; align-items:center; justify-content:center; font-style:normal; font-size:20px; }
#shine { position:absolute; top:-40px; width:160px; height:640px; background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,0.35),rgba(255,255,255,0)); transform:rotate(14deg); pointer-events:none; }
.shadow16 { position:absolute; left:120px; top:570px; width:300px; height:40px; border-radius:50%; background:radial-gradient(closest-side, rgba(0,0,0,0.5), rgba(0,0,0,0)); }
.side16 { position:absolute; left:520px; top:70px; width:380px; }
.side16 .k { font-size:15px; letter-spacing:0.2em; color:#00c9ff; font-weight:700; }
.side16 .t { font-size:40px; font-weight:700; line-height:1.2; margin-top:10px; }
.side16 .row { display:flex; align-items:center; justify-content:space-between; margin-top:22px; padding:18px 22px; border-radius:18px; background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.14); font-size:19px; }
.side16 .row b { font-size:26px; }
.stars { color:#00c9ff; letter-spacing:4px; font-size:22px; }
"""
_book = ('<svg width="210" height="230" viewBox="0 0 210 230"><defs><linearGradient id="bk1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7fe6ff"/><stop offset="1" stop-color="#0068ff"/></linearGradient>'
         '<linearGradient id="bk2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#cfe0ff"/></linearGradient></defs>'
         '<path d="M40 30 L170 18 L170 190 L40 206 Z" fill="url(#bk1)"/><path d="M40 206 L170 190 L176 198 L46 214 Z" fill="url(#bk2)"/><path d="M170 18 L176 26 L176 198 L170 190 Z" fill="#e6efff"/>'
         '<path d="M40 30 L52 28 L52 204 L40 206 Z" fill="#0b1440" opacity="0.35"/>'
         '<text x="110" y="100" text-anchor="middle" font-size="40" font-weight="700" fill="#fff" font-family="Poppins">AI</text>'
         '<text x="110" y="132" text-anchor="middle" font-size="17" font-weight="700" fill="#0b1440" font-family="Poppins">PROMPT PACK</text>'
         '<rect x="72" y="150" width="76" height="6" rx="3" fill="#fff" opacity="0.7"/></svg>')
_feats = [("120+ prompt siap pakai", 128), ("Update tiap bulan", 236), ("Akses komunitas", 344)]
S16_VIS = f"""      <div class="shadow16" id="sh16"></div>
      <div class="stage16"><div id="card16">
        <div class="face front"><div class="prod">{_book}</div><div class="pname">AIpreneur Prompt Pack</div>
          <div class="price16 w"><small>Rp</small>199rb</div><div class="plus">+</div><div class="sold">&#9733; 4,9 &middot; 2.300 terjual</div></div>
        <div class="face back"><div class="k">ISI PAKET</div><div class="bt w">Yang kamu dapat</div>
          {''.join(f'<div class="feat w" style="top:{y}px"><i id="fi{i}">&#10003;</i>{f}</div>' for i, (f, y) in enumerate(_feats))}
          <div class="sold" style="top:466px">Akses seumur hidup</div></div>
        <div id="shine"></div>
      </div></div>
      <div class="side16"><div class="k">PRODUK DIGITAL</div><div class="t w">Kartu produk yang berputar 360&deg;</div>
        <div class="row"><span class="w r">Rating</span><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span></div>
        <div class="row"><span class="w r">Terjual</span><b class="w" id="sold16">0</b></div>
        <div class="row"><span class="w r">Harga</span><span class="hb" style="font-size:22px;padding:4px 12px">Rp199.000</span></div></div>"""
S16_JS = """
  const fmt = (v) => Math.round(v).toString().replace(/\\B(?=(\\d{3})+(?!\\d))/g, ".");
  function render(t) {
    const a = 180 * clamp(backOut((t - 0.6) / 1.0, 1.1), 0, 1.04) + 180 * clamp(backOut((t - 3.5) / 1.0, 1.1), 0, 1.04);
    gsap.set("#card16", { rotationY: a, y: -10 * Math.sin(TAU * t / 3) });
    const sh = ((a % 180) / 180);
    gsap.set("#shine", { x: -220 + 760 * sh, opacity: Math.sin(Math.PI * sh) });
    gsap.set("#sh16", { scaleX: 0.8 + 0.2 * Math.abs(Math.cos(a * Math.PI / 180)) });
    for (let i = 0; i < 3; i++) {
      const k = smooth((t - 1.75 - i * 0.3) / 0.2) * (1 - smooth((t - 3.4) / 0.2));
      const el = $("fi" + i);
      el.style.background = k > 0.5 ? "#00c9ff" : "transparent"; el.style.borderColor = k > 0.5 ? "#00c9ff" : "rgba(255,255,255,0.4)";
      el.style.color = k > 0.5 ? "#0b1440" : "transparent";
      gsap.set(el, { scale: 1 + 0.3 * Math.sin(Math.PI * clamp((t - 1.75 - i * 0.3) / 0.3, 0, 1)) });
    }
    $("sold16").textContent = fmt(2300 * io3((t - 0.4) / 2.2));
  }
"""

# ---------------------------------------------------------------- 16 map -> route (Indonesia)
P = IDN["pts"]
ORDER = ["Medan", "Jakarta", "Surabaya", "Makassar", "Jayapura"]
S17_CSS = """
.mapw { position:absolute; left:70px; top:60px; width:872px; height:380px; perspective:1400px; }
#map17 { position:absolute; left:6px; top:0; width:860px; height:340px; transform:rotateX(38deg); transform-origin:50% 60%; transform-style:preserve-3d; }
#map17 svg { overflow:visible; }
.pin { position:absolute; width:30px; height:44px; margin:-44px 0 0 -15px; }
.pin .h { position:absolute; left:0; top:0; width:30px; height:30px; border-radius:50%; background:radial-gradient(circle at 35% 30%, #bff3ff, #00c9ff 45%, #0068ff); box-shadow:0 6px 14px rgba(0,0,0,0.4); }
.pin .s { position:absolute; left:14px; top:26px; width:2.5px; height:18px; background:rgba(255,255,255,0.8); }
.pin .nm { position:absolute; left:36px; top:2px; font-size:16px; font-weight:700; color:#fff; white-space:nowrap; text-shadow:0 2px 6px rgba(0,0,0,0.6); }
.res17 { position:absolute; left:56px; top:470px; display:flex; align-items:center; gap:22px; }
.res17 .big { font-size:110px; font-weight:700; line-height:1; color:#00c9ff; letter-spacing:-0.04em; }
.res17 .lb { font-size:34px; line-height:1.15; }
.list17 { position:absolute; left:470px; top:486px; display:flex; gap:10px; flex-wrap:wrap; width:440px; }
.list17 span { font-size:18px; padding:6px 14px; border-radius:14px; border:1.5px solid rgba(255,255,255,0.25); color:#fff; }
"""
_route = "M" + " L".join(f"{P[c][0]} {P[c][1]}" for c in ORDER)
_route_curved = f"M{P[ORDER[0]][0]} {P[ORDER[0]][1]}"
for a, b in zip(ORDER, ORDER[1:]):
    (x1, y1), (x2, y2) = P[a], P[b]
    mx, my = (x1 + x2) / 2, min(y1, y2) - 0.18 * abs(x2 - x1) - 20
    _route_curved += f" Q{mx:.1f} {my:.1f},{x2} {y2}"
S17_VIS = f"""      <div class="mapw"><div id="map17">
        <svg width="860" height="340" viewBox="0 0 860 340">
          <defs><linearGradient id="lf17" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a6fd0"/><stop offset="1" stop-color="#1a3a80"/></linearGradient>
            <filter id="g17" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="5"/></filter></defs>
          <path d="{IDN['d']}" fill="#081038" transform="translate(0 9)" opacity="0.7"/>
          <path d="{IDN['d']}" fill="url(#lf17)" stroke="rgba(160,210,255,0.7)" stroke-width="1"/>
          <path id="rtg" d="{_route_curved}" fill="none" stroke="#00c9ff" stroke-width="10" stroke-linecap="round" filter="url(#g17)"/>
          <path id="rt17" d="{_route_curved}" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 0"/>
        </svg>
      </div>
""" + "".join(f'        <div class="pin" id="pn{i}" style="left:{P[c][0] + 46}px;top:{P[c][1] * 0.79 + 64}px"><div class="s"></div><div class="h"></div><div class="nm" style="{'left:auto;right:36px' if c == 'Jayapura' else ''}">{c}</div></div>\n' for i, c in enumerate(ORDER)) + """      </div>
      <div class="res17"><div class="big" id="big17">0</div><div class="lb w b">kota<br><span class="hb" id="hb17">workshop offline</span></div></div>
      <div class="list17">""" + "".join(f'<span id="ls{i}">{c}</span>' for i, c in enumerate(ORDER)) + "</div>"
S17_JS = """
  const N = 5, rt = $("rt17"), rtg = $("rtg"), L = rt.getTotalLength();
  function render(t) {
    const out = smooth((t - 5.25) / 0.4);
    for (let i = 0; i < N; i++) {
      const at = 0.3 + i * 0.22, k = backOut((t - at) / 0.45, 2.2);
      gsap.set("#pn" + i, { y: -70 * (1 - clamp(k, 0, 1.2)), opacity: (t > at ? Math.min(1, (t - at) * 8) : 0) * (1 - out) });
      const on = smooth((t - 1.6 - i * 0.42) / 0.15) * (1 - out);
      const ls = $("ls" + i); ls.style.background = "rgba(255,255,255," + on.toFixed(3) + ")"; ls.style.color = on > 0.5 ? "#0b1440" : "#fff"; ls.style.fontWeight = on > 0.5 ? 700 : 400;
    }
    const d = io3((t - 1.5) / 1.8) * (1 - out);
    [rt, rtg].forEach((p) => { p.setAttribute("stroke-dasharray", (d * L).toFixed(1) + " " + (L + 5).toFixed(1)); p.style.opacity = d > 0.005 ? 1 : 0; });
    let reached = 0; for (let i = 0; i < N; i++) if (t >= 1.6 + i * 0.42) reached = i + 1;
    $("big17").textContent = Math.round(reached * (1 - out));
    gsap.set("#hb17", { scale: Math.max(0, backOut((t - 3.4) / 0.45, 2.4)) * (1 - out) });
  }
"""

# ---------------------------------------------------------------- cover (grid of 16 live tiles)
SC = [("01", "Bars", "trend"), ("02", "Monthly", "yearly"), ("03", "Dots", "logo"), ("04", "Island", "live"),
      ("05", "Visits", "sales"), ("06", "Click", "done"), ("07", "Card", "paid"), ("08", "0", "12.480"),
      ("09", "Weight", "bold"), ("10", "Sketch", "app"), ("11", "Drag", "booked"), ("12", "Alerts", "stack"),
      ("13", "Rings", "closed"), ("14", "Dock", "open"), ("15", "Card", "360&deg;"), ("16", "Map", "route")]
TW, TH, GAP, GX, GY = 229, 150, 12, 64, 300
COVER_CSS = """
.ct { position:absolute; left:63px; top:104px; font-size:84px; line-height:1.12; letter-spacing:-0.035em; white-space:nowrap; }
.cw { display:inline-block; position:relative; height:94px; width:330px; overflow:hidden; vertical-align:-14px; margin-left:8px; }
.cw span { position:absolute; left:0; top:0; }
.cs { position:absolute; left:66px; top:220px; font-size:26px; }
.tl { position:absolute; width:229px; }
.tl .lb { margin-top:6px; font-size:15px; white-space:nowrap; }
.tl .lb .no { color:#00c9ff; font-weight:700; margin-right:6px; }
.tv { position:absolute; width:229px; height:150px; border-radius:16px; object-fit:cover; border:1.5px solid rgba(255,255,255,0.18); }
"""


def cover_body():
    tiles, vids = [], []
    for i, (no, a, b) in enumerate(SC):
        r, c = divmod(i, 4)
        x, y = GX + c * (TW + GAP), GY + r * (TH + 62)
        tiles.append(f'    <div class="tl" style="left:{x}px;top:{y + TH}px"><div class="lb"><span class="no">{no}</span><span class="w b">{a}</span> <span class="c">&rarr;</span> <span class="w r">{b}</span></div></div>')
        vids.append(f'    <video id="v{no}" class="clip tv" data-start="0" data-duration="6" data-track-index="{i + 1}" src="assets/tiles/t{no}.mp4" muted playsinline style="left:{x}px;top:{y}px"></video>')
    return ("""    <div class="ct"><span class="w b">Claude Motion</span><span class="cw"><span class="hb" id="w0">Graphics</span><span class="hb" id="w1">Charts</span><span class="hb" id="w2">Logos</span><span class="hb" id="w3">Apps</span></span></div>
    <div class="cs w r">16 animasi, <span class="c b">satu prompt</span> per scene. Geser buat lihat semuanya &rarr;</div>
""" + "\n".join(tiles)), "\n".join(vids)


COVER_JS = """
  const W = ["#w0", "#w1", "#w2", "#w3"];
  gsap.set(W.slice(1), { yPercent: 110 });
  for (let i = 0; i < 4; i++) {
    const at = 1.5 * (i + 1) - 0.3;
    tl.to(W[i], { yPercent: -110, duration: 0.28, ease: "power3.in" }, at);
    tl.fromTo(W[(i + 1) % 4], { yPercent: 110 }, { yPercent: 0, duration: 0.42, ease: "back.out(1.7)", immediateRender: false }, at + 0.2);
  }
  function render(t) {}
"""

# ---------------------------------------------------------------- CTA
CTA_CSS = """
.cm { position:absolute; left:63px; top:250px; font-size:110px; font-weight:700; letter-spacing:-0.04em; line-height:1.1; }
#kw { position:absolute; left:63px; top:380px; font-size:150px; padding:0 0.16em 0.04em; letter-spacing:-0.02em; border-radius:16px; line-height:1.12; transform-origin:0 50%; }
.ctxt { position:absolute; left:66px; top:600px; width:560px; font-size:30px; line-height:1.45; }
.inp { position:absolute; left:64px; top:800px; width:560px; height:96px; border-radius:48px; background:rgba(255,255,255,0.08); border:2px solid rgba(255,255,255,0.3); }
.inp .av { position:absolute; left:16px; top:18px; width:56px; height:56px; box-shadow:none; }
.inp .ph { position:absolute; left:96px; top:0; line-height:92px; font-size:28px; color:rgba(255,255,255,0.45); }
.inp .ty { position:absolute; left:96px; top:0; line-height:92px; font-size:30px; font-weight:700; color:#00c9ff; letter-spacing:0.06em; display:flex; }
.inp .ty span { opacity:0; }
#car { width:3px; height:36px; margin:28px 0 0 4px; background:#00c9ff; }
#sendb { position:absolute; right:16px; top:18px; width:56px; height:56px; border-radius:50%; background:#fff; display:flex; align-items:center; justify-content:center; opacity:0.3; }
.gets { position:absolute; left:666px; top:250px; width:350px; }
.gets .k { font-size:15px; letter-spacing:0.2em; color:#00c9ff; font-weight:700; margin-bottom:6px; }
.gc { position:relative; margin-top:20px; height:212px; border-radius:22px; background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.16); padding:22px 24px; }
.gc .no { font-size:52px; font-weight:700; color:#00c9ff; line-height:1; }
.gc .t { font-size:28px; font-weight:700; margin-top:10px; }
.gc .d { font-size:19px; color:rgba(255,255,255,0.7); margin-top:4px; }
.badge { position:absolute; left:64px; top:930px; font-size:24px; padding:10px 20px; }
"""
CTA_BODY = """    <div class="cm w">Comment</div>
    <span class="hb" id="kw">BRIEF</span>
    <div class="ctxt w r">Aku kirim <span class="c b">brief-nya</span> + semua prompt dari 16 video ini. <span class="b">Paste brief, ganti satu baris, export.</span></div>
    <div class="inp"><div class="av">FK</div><div class="ph" id="ph19">Tulis komentar&hellip;</div>
      <div class="ty"><span id="q0">B</span><span id="q1">R</span><span id="q2">I</span><span id="q3">E</span><span id="q4">F</span><i id="car"></i></div>
      <div id="sendb"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M3 11 L21 3 L14 21 L11 13 Z" fill="#0b1440"/></svg></div></div>
    <span class="hb badge" id="bd19">&#10003; Link dikirim via DM</span>
    <div class="gets"><div class="k">YANG KAMU DAPAT</div>
      <div class="gc" id="gc0"><div class="no">01</div><div class="t w">Brief utama</div><div class="d">paste duluan, ini yang bikin look-nya premium</div></div>
      <div class="gc" id="gc1"><div class="no">02</div><div class="t w">16 prompt scene</div><div class="d">satu baris per scene, tinggal ganti</div></div>
      <div class="gc" id="gc2"><div class="no">03</div><div class="t w">Setting export</div><div class="d">MP4, 1080p, 30 fps</div></div></div>
"""
CTA_JS = """
  function render(t) {
    const beat = (t % 2) / 2;
    gsap.set("#kw", { rotation: -2, scale: 1 + 0.04 * Math.exp(-7 * beat) * Math.sin(Math.PI * Math.min(1, beat * 5)) });
    const typing = t >= 0.6 && t < 3.6;
    for (let i = 0; i < 5; i++) gsap.set("#q" + i, { opacity: typing && t >= 0.7 + i * 0.16 ? 1 : 0 });
    gsap.set("#ph19", { opacity: typing ? 0 : 1 });
    gsap.set("#car", { opacity: typing && Math.floor(t * 3) % 2 === 0 ? 1 : 0 });
    gsap.set("#sendb", { opacity: t >= 1.5 && t < 3.6 ? 1 : 0.3, scale: t > 1.9 && t < 2.05 ? 0.85 : 1 });
    gsap.set("#bd19", { scale: Math.max(0, backOut((t - 2.2) / 0.45, 2.4)) * (1 - smooth((t - 5.3) / 0.3)) });
    for (let i = 0; i < 3; i++) {
      const k = env(t, 2.5 + i * 0.35, 3.0 + i * 0.35, 0.15), el = $("gc" + i);
      el.style.borderColor = "rgba(0,201,255," + (0.16 + 0.8 * k).toFixed(3) + ")";
      el.style.boxShadow = "0 16px 34px -14px rgba(0,201,255," + (0.7 * k).toFixed(3) + ")";
    }
  }
"""


def make(scene_body):
    cb, vids = cover_body()
    cover = dict(cid="s0", name="Cover", eyebrow="16 SCENE &middot; 1 PROMPT", css=COVER_CSS, body=cb, js=COVER_JS, extra=vids)
    s16 = dict(cid="s16", name="Card 360", eyebrow="SCENE 15", css=S16_CSS, js=S16_JS,
               body=scene_body("Card", "360&deg;", "Kartu produk yang berputar 360&deg;",
                               'Kartu produk premium untuk <span class="ph">[produk kamu]</span> (<span class="ph">[harga kamu]</span>). Kartu berputar 3D satu putaran penuh dengan kilau yang bergerak, menunjukkan tiga fitur di baliknya, lalu kembali menghadap depan.',
                               ["AIpreneur Prompt Pack", "Rp199.000"], S16_VIS))
    s17 = dict(cid="s17", name="Map route", eyebrow="SCENE 16", css=S17_CSS, js=S17_JS,
               body=scene_body("Map", "route", "Peta yang menggambar rutenya",
                               'Peta 3D miring dari <span class="ph">[negara kamu]</span>. Pin jatuh dan memantul di <span class="ph">[kota-kota kamu]</span>, garis rute bercahaya tergambar di antaranya, lalu <span class="ph">&ldquo;[hasil kamu]&rdquo;</span> muncul.',
                               ["Indonesia", "5 kota", "workshop offline"], S17_VIS))
    cta = dict(cid="s18", name="CTA", eyebrow="BRIEF + 16 PROMPT", css=CTA_CSS, body=CTA_BODY, js=CTA_JS, right="SAVE &middot; SHARE")
    return cover, [s16, s17, cta]

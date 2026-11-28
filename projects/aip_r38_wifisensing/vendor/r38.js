/* R38 · Wi-Fi sensing / RuView (AI PRENEUR, WHITE). Batch-10 2D look: spoken headline on top (one italic accent word), the client's
   mascot comes FORWARD half-body on explaining beats (vendor/r38_host.js, windows exported here as R38_STAGE) and is fully hidden on
   example beats, where ONE big card / diagram gets the whole frame. No beat counter, no voxel world, no robot.
   Every style is a pure function of t (render(t) on hf-seek + timeline update; no timers, no state between frames). Times come from the
   untouched VO take (window.WORDS + 0.3 s offset). Shared elements: wall diagram -> camera-off emblem; repo card -> star counter;
   floor plan -> plan + CSI graph -> graph stays under the sensor board -> board -> AI node -> dashboard; Claude Code input (client's own
   recording) -> grows into the plugin terminal; floor plan returns for the Home Assistant lamp. Closed-form springs; 3-subframe ghosts on
   the flying signal dots; velocity blur on whips. Sound events registered with ev() and exported to tools/sfx.py. */
(function () {
  const OFF = 0.3, D = window.R38_TOTAL, WT = window.WORDS.map((w) => +(w[1] + OFF).toFixed(3));
  const wt = (i) => WT[i];
  // Lucide icons (ISC) used by this reel, on top of the kit set
  const ICO = Object.assign({}, window.R30_ICO, {
    wifi: '<path d="M12 20h.01"/><path d="M2 8.82a15 15 0 0 1 20 0"/><path d="M5 12.859a10 10 0 0 1 14 0"/><path d="M8.5 16.429a5 5 0 0 1 7 0"/>',
    "camera-off": '<line x1="2" x2="22" y1="2" y2="22"/><path d="M7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16"/><path d="M9.5 4h5L17 7h3a2 2 0 0 1 2 2v7.5"/><path d="M14.121 15.121A3 3 0 1 1 9.88 10.88"/>',
    cpu: '<rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/>',
    activity: '<path d="M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2"/>',
    house: '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    laptop: '<path d="M20 16V7a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v9m16 0H4m16 0 1.28 2.55a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45L4 16"/>',
    "shield-check": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    scale: '<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
    code: '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "triangle-alert": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    "door-open": '<path d="M11 20H2"/><path d="M11 4.562v16.157a1 1 0 0 0 1.242.97L19 20V5.562a2 2 0 0 0-1.515-1.94l-4-1A2 2 0 0 0 11 4.561z"/><path d="M11 4H8a2 2 0 0 0-2 2v14"/><path d="M14 12h.01"/><path d="M22 20h-3"/>',
  });
  const $ = (id) => document.getElementById(id);
  const ui = $("ui"), GRAIN = $("grain"), BACK = $("back");
  const ico = (n, c = "#fff", sw = 2.2) => `<svg viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round">${ICO[n]}</svg>`;
  const mk = (html, parent) => { const d = document.createElement("div"); d.innerHTML = html.trim(); const el = d.firstChild; (parent || ui).insertBefore(el, parent ? null : GRAIN); return el; };
  const NS = "http://www.w3.org/2000/svg";
  const sv = (tag, attrs, parent) => { const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; };
  // ------------------------------------------------------------------ math (pure functions of t)
  const cl = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const lin = (t, a, b) => cl((t - a) / (b - a));
  const eo = (t, a, b) => 1 - Math.pow(1 - lin(t, a, b), 3);
  const ei = (t, a, b) => Math.pow(lin(t, a, b), 3);
  const eio = (t, a, b) => { const u = lin(t, a, b); return u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2; };
  const spr = (t, t0, w = 17, z = 0.62) => { const u = t - t0; if (u <= 0) return 0; const wd = w * Math.sqrt(1 - z * z); return 1 - Math.exp(-z * w * u) * (Math.cos(wd * u) + (z * w / wd) * Math.sin(wd * u)); };
  const L = (a, b, u) => a + (b - a) * u;
  function S(el, p) {
    const o = p.o === undefined ? 1 : p.o;
    if (o <= 0.002) { if (el.style.visibility !== "hidden") { el.style.visibility = "hidden"; el.style.opacity = "0"; } return; }
    el.style.visibility = "visible"; el.style.opacity = o.toFixed(3);
    const s = p.s === undefined ? 1 : p.s, sx = (p.sx === undefined ? 1 : p.sx) * s, sy = (p.sy === undefined ? 1 : p.sy) * s;
    el.style.transform = `translate(${(p.x || 0).toFixed(2)}px,${(p.y || 0).toFixed(2)}px)` + (p.ry ? ` perspective(1600px) rotateY(${p.ry.toFixed(2)}deg)` : "") + (p.rx ? ` perspective(1600px) rotateX(${p.rx.toFixed(2)}deg)` : "") + (p.r ? ` rotate(${p.r.toFixed(2)}deg)` : "") + ` scale(${sx.toFixed(4)},${sy.toFixed(4)})`;
    const b = p.b || 0; el.style.filter = b > 0.05 ? `blur(${b.toFixed(2)}px)` : "none";
  }
  const hide = (el) => S(el, { o: 0 });
  // ------------------------------------------------------------------ sound events (exported for tools/sfx.py)
  const EV = []; const ev = (t, n, db = 0, rate = 1) => { EV.push([+t.toFixed(3), n, db, rate]); return t; };
  window.R38_SFX = EV;
  // ------------------------------------------------------------------ 3-subframe ghosts for small fast movers
  function ghosts(el) { return [0, 1].map(() => { const c = el.cloneNode(true); c.removeAttribute("id"); el.parentNode.insertBefore(c, el); return c; }); }
  function mb(el, g, f, t) {
    const p = f(t); S(el, p);
    const a = f(t - 1 / 90), b = f(t + 1 / 90), sp = Math.hypot((b.x || 0) - (a.x || 0), (b.y || 0) - (a.y || 0)) * 45;
    if (sp < 500 || (p.o === undefined ? 1 : p.o) < 0.02) { hide(g[0]); hide(g[1]); return; }
    const k = cl((sp - 500) / 900) * 0.42;
    S(g[0], Object.assign({}, a, { o: (a.o === undefined ? 1 : a.o) * k })); S(g[1], Object.assign({}, b, { o: (b.o === undefined ? 1 : b.o) * k }));
  }
  // whip: x offset with velocity blur (finite difference)
  const whip = (f, t) => { const x = f(t), v = Math.abs(f(t + 1 / 60) - f(t - 1 / 60)) * 30; return { x, b: Math.min(16, v / 260) }; };
  // ------------------------------------------------------------------ sprites (3D Simple Icons logos, 36-frame turntables)
  const spr3 = (name, size, x, y, parent) => mk(`<div class="spr" style="left:${x}px;top:${y}px;width:${size}px;height:${size}px;background-image:url(assets/logos3d/${name}.png)"></div>`, parent);
  function frame(el, deg) { const f = ((Math.round(deg / 10) % 36) + 36) % 36; el.style.backgroundPosition = `${(f % 6) * 20}% ${Math.floor(f / 6) * 20}%`; }
  const wob = (t, ph = 0, amp = 22) => amp * Math.sin(t * 1.7 + ph);
  // ------------------------------------------------------------------ beats (word ranges; headline = the spoken words)
  // [first word, last word, emphasised word]
  const BEATS = [[0, 6, 4], [7, 10, 10], [11, 14, 12], [15, 20, 16], [21, 27, 23], [28, 29, 29], [30, 35, 35], [36, 42, 38], [43, 50, 46], [51, 53, 53],
    [54, 61, 61], [62, 66, 65], [67, 71, 70], [72, 79, 75], [80, 83, 83], [84, 89, 89], [90, 94, 94], [95, 103, 101], [104, 113, 104]];
  const NB = BEATS.length;
  const BS = BEATS.map((b, k) => (k === 0 ? 0 : wt(b[0]) - 0.12));
  const BE = BS.map((s, k) => (k < NB - 1 ? BS[k + 1] : D));
  // explaining beats: the mascot comes forward half-body (host). [tIn, tOut, fx of the big pose]
  const STAGE = [[0, BE[0], 540], [BS[5], BE[5], 540], [BS[14], BE[14], 430], [BS[17], 1e9, 540]];
  window.R38_STAGE = STAGE;
  const AFTER = 0.24;   // an example lands this long after the mascot starts leaving (exit = 0.32 s, gone by ~0.3 s)
  STAGE.forEach(([a, b]) => { ev(a + 0.02, "whoosh", -4, 0.75); if (b < D) ev(b + 0.06, "pop", -5, 0.7); });

  function BUILD() {
  const SHOW = { 23: "100", 46: "9", 105: "WIFI," };
  const HL = BEATS.map((b, k) => {
    const el = mk(`<div class="hl"></div>`);
    const ws = [];
    for (let i = b[0]; i <= b[1]; i++) {
      let s = SHOW[i] !== undefined ? SHOW[i] : window.WORDS[i][0];
      if (i === b[0]) s = s.charAt(0).toUpperCase() + s.slice(1);
      const sp = document.createElement("span"); sp.className = "w" + (i === b[2] ? " em" : ""); sp.textContent = s;
      el.appendChild(sp); el.appendChild(document.createTextNode(" ")); ws.push([sp, i]);
    }
    if (el.offsetHeight > 72 * 2.5) el.style.fontSize = "56px";
    return { el, ws };
  });
  function headline(t) {
    HL.forEach((h, k) => {
      const a = BS[k], b = BE[k];
      if (t < a - 0.3 || t > b + 0.35) { hide(h.el); return; }
      S(h.el, { o: 1 });
      const out = lin(t, b - 0.1, b + 0.1);
      h.ws.forEach(([sp, i]) => {
        const t0 = Math.max(k === 0 ? 0.2 : a + 0.08, wt(i) - 0.1), u = spr(t, t0, 19, 0.7), e = eo(t, t0, t0 + 0.22);
        if (u <= 0) { hide(sp); return; }
        const oo = 1 - eo(out, 0, 1);
        S(sp, { o: e * oo, y: 34 * (1 - u) - 26 * ei(out, 0, 1), b: 8 * (1 - e) + 6 * out, s: 0.94 + 0.06 * u });
      });
    });
  }
  // particles: slow deterministic drift
  const PTS = []; for (let i = 0; i < 22; i++) { const r = 5 + (i * 7) % 9; PTS.push([mk(`<div class="pt" style="width:${r}px;height:${r}px"></div>`, $("pts")), (i * 137.5) % 1080, (i * 291.7) % 1920, 0.06 + ((i * 13) % 10) / 70, i]); }
  function particles(t) { for (const [el, x0, y0, o, i] of PTS) S(el, { x: (x0 + 14 * Math.sin(t * 0.3 + i)) % 1080, y: ((y0 - t * (8 + (i % 5) * 3)) % 1920 + 1920) % 1920, o }); }
  // Wi-Fi rings behind the mascot on the explaining beats (stage layer, under the host canvas)
  const RINGS = [0, 1, 2, 3].map(() => mk(`<div class="ring"></div>`, BACK));
  function rings(t) {
    let w = 0, cx = 540;
    for (const [a, b, fx] of STAGE) { const k = eo(t, a + 0.1, a + 0.5) * (1 - lin(t, b - 0.05, b + 0.2)); if (k > w) { w = k; cx = fx; } }
    RINGS.forEach((r, i) => { const f = ((t * 0.45 + i / 4) % 1); S(r, { x: cx, y: 1000, s: 1 + 7.5 * f, o: w * 0.22 * (1 - f) }); });
  }

  // ================================================================== 1-2 · WALL (through the wall, no camera)
  const T1 = BS[1] + AFTER, T2 = BS[2], T3 = BS[3];
  const WALL = mk(`<div class="card" style="left:70px;top:660px;width:940px;height:780px;overflow:hidden"><div class="lbl" style="left:38px;top:34px">Tembus tembok · ilustrasi</div><div class="demo" style="right:34px;top:26px">SIMULASI</div></div>`);
  const WSV = sv("svg", { width: 940, height: 780, viewBox: "0 0 940 780", style: "position:absolute;left:0;top:0" }, WALL);
  const defs = sv("defs", {}, WSV);
  const pat = sv("pattern", { id: "brick", width: 50, height: 36, patternUnits: "userSpaceOnUse" }, defs);
  sv("rect", { width: 50, height: 36, fill: "#c9d5e8" }, pat); sv("path", { d: "M0 18H50M25 0V18M0 18V36M50 18V36", stroke: "#eef3fb", "stroke-width": 4 }, pat);
  const c1 = sv("clipPath", { id: "wl" }, defs); sv("rect", { x: 20, y: 90, width: 425, height: 600, rx: 24 }, c1);
  const c2 = sv("clipPath", { id: "wr" }, defs); sv("rect", { x: 505, y: 90, width: 415, height: 600, rx: 24 }, c2);
  sv("rect", { x: 20, y: 90, width: 900, height: 600, rx: 26, fill: "#f4f7fc", stroke: "rgba(41,75,119,.14)", "stroke-width": 3 }, WSV);
  const WG = [sv("g", { "clip-path": "url(#wl)" }, WSV), sv("g", { "clip-path": "url(#wr)" }, WSV)];
  const WAVES = [0, 1, 2, 3, 4].map(() => WG.map((g) => sv("circle", { cx: 150, cy: 390, r: 10, fill: "none", stroke: "#2f6bff", "stroke-width": 6 }, g)));
  sv("rect", { x: 445, y: 90, width: 60, height: 600, fill: "url(#brick)", stroke: "#294b77", "stroke-width": 3 }, WSV);
  const ROUT = mk(`<div class="ic" style="position:absolute;left:92px;top:332px;width:116px;height:116px;border-radius:30px">${ico("wifi")}</div>`, WALL);
  mk(`<div style="position:absolute;left:62px;top:466px;width:176px;text-align:center;font:700 24px/1 Poppins;color:#294b77">router Wi-Fi</div>`, WALL);
  const PRING = mk(`<div style="position:absolute;left:640px;top:300px;width:180px;height:180px;border-radius:50%;border:5px solid #2f6bff"></div>`, WALL);
  const PERS = mk(`<div class="ic" style="position:absolute;left:665px;top:325px;width:130px;height:130px;border-radius:50%">${ico("user")}</div>`, WALL);
  const DET = mk(`<div class="chip on" style="left:600px;top:500px">${ico("radar", "#fff", 2.4)}orang terdeteksi</div>`, WALL);
  const RANGE = mk(`<div class="chip" style="left:38px;top:712px">${ico("wifi", "#294b77", 2.4)}tembus tembok, sampai ± 5 m · tergantung sinyal</div>`, WALL);
  const CAM = mk(`<div style="position:absolute;left:330px;top:205px;width:280px;height:280px;border-radius:70px;display:grid;place-items:center;background:#fff;box-shadow:0 0 0 4px rgba(41,75,119,.18),0 30px 60px rgba(19,48,126,.22)"><svg viewBox="0 0 24 24" style="width:170px;height:170px" fill="none" stroke="#294b77" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/><line id="camx" x1="2" y1="2" x2="22" y2="22" stroke="#2f6bff" stroke-width="2.6" stroke-dasharray="28.3" stroke-dashoffset="28.3"/></svg></div>`, WALL);
  const CAMX = CAM.querySelector("line");
  const ZERO = mk(`<div class="stamp" style="left:300px;top:530px">0 KAMERA</div>`, WALL);
  const t1 = { det: wt(10) - 0.05, range: wt(9) + 0.05, cam: wt(11) - 0.05, x: wt(12) + 0.05, zero: wt(13) - 0.05 };
  ev(T1 - 0.05, "whoosh", -2, 1.2); ev(T1 + 0.1, "pop", -8, 0.9); ev(t1.det, "ping", -4); ev(t1.range, "click", -8, 1.1);
  ev(t1.cam, "pop", -2, 0.9); ev(t1.x, "whoosh", -8, 1.8); ev(t1.zero, "impact", -5);
  function wall(t) {
    if (t < T1 - 0.05 || t > T3 + 0.4) { hide(WALL); return; }
    const u = spr(t, T1, 14, 0.74), fl = eio(t, T3 - 0.02, T3 + 0.22);
    const w = whip((tt) => 1150 * (1 - eo(tt, T1, T1 + 0.42)), t);
    S(WALL, { o: Math.min(1, u * 3) * (1 - lin(t, T3 + 0.16, T3 + 0.22)), x: w.x, b: w.b, ry: 90 * fl, s: 0.96 + 0.04 * Math.min(1, u) });
    // waves (stronger before the wall, fainter behind it)
    WAVES.forEach((pair, i) => {
      const f = ((t * 0.7 + i / 5) % 1), r = 20 + 820 * f;
      pair.forEach((c, side) => { c.setAttribute("r", r.toFixed(1)); c.setAttribute("opacity", ((1 - f) * (side ? 0.32 : 0.6)).toFixed(3)); });
    });
    const dim = 1 - 0.75 * eo(t, t1.cam - 0.05, t1.cam + 0.25);
    S(ROUT, { s: 1 + 0.06 * Math.sin(t * 6), o: dim });
    const du = spr(t, t1.det, 16, 0.55);
    S(PERS, { o: Math.min(1, eo(t, T1 + 0.25, T1 + 0.5) + 0) * dim, s: 0.9 + 0.1 * eo(t, T1 + 0.25, T1 + 0.5) });
    S(PRING, { o: t > t1.det ? 0.8 * (1 - ((t - t1.det) * 1.2) % 1) * dim : 0, s: 1 + 0.35 * (((t - t1.det) * 1.2) % 1) });
    S(DET, { o: Math.min(1, du * 3) * dim, s: 0.7 + 0.3 * du, y: 20 * (1 - du) });
    const ru = spr(t, t1.range, 16, 0.65); S(RANGE, { o: Math.min(1, ru * 3) * dim, x: -40 * (1 - ru) });
    WG.forEach((g) => g.setAttribute("opacity", dim.toFixed(3)));
    const cu = spr(t, t1.cam, 15, 0.55); S(CAM, { o: Math.min(1, cu * 3), s: 0.5 + 0.5 * cu, r: -8 * (1 - cu) });
    CAMX.setAttribute("stroke-dashoffset", (28.3 * (1 - eio(t, t1.x, t1.x + 0.3))).toFixed(2)); CAMX.setAttribute("opacity", t > t1.x ? 1 : 0);
    const zu = spr(t, t1.zero, 22, 0.5); S(ZERO, { o: Math.min(1, zu * 3), s: 1.6 - 0.6 * zu, r: -6 });
  }

  // ================================================================== 3-4 · REPO card (GitHub) -> star counter
  const T4 = BS[4], T5 = BS[5];
  const REPO = mk(`<div class="card" style="left:70px;top:660px;width:940px;height:560px"><div style="position:absolute;left:200px;top:52px;font:700 58px/1 Poppins;color:#0a0d2c;white-space:nowrap">ruvnet / <span style="background:linear-gradient(100deg,#13307e,#2f6bff);-webkit-background-clip:text;background-clip:text;color:transparent">RuView</span></div><div class="demo" style="left:202px;top:128px">PUBLIC · GITHUB</div><div style="position:absolute;left:44px;top:210px;width:860px;font:400 34px/1.45 Poppins;color:#0a0d2c">Ubah sinyal Wi-Fi biasa jadi deteksi kehadiran, gerakan &amp; napas, <b style="font-weight:700">tanpa satu piksel video.</b></div></div>`);
  const GH = spr3("github", 140, 40, 28, REPO);
  const OS = mk(`<div class="chip" style="left:44px;top:430px;font-size:30px">${ico("code", "currentColor", 2.4)}Open source</div>`, REPO);
  const MIT = mk(`<div class="chip" style="left:330px;top:430px;font-size:30px">${ico("scale", "currentColor", 2.2)}Lisensi MIT</div>`, REPO);
  const STARS = mk(`<div class="card" style="left:170px;top:1260px;width:740px;height:330px"><div style="position:absolute;left:44px;top:56px;width:130px;height:130px;border-radius:36px;display:grid;place-items:center;background:linear-gradient(135deg,#13307e,#2f6bff)"><svg viewBox="0 0 24 24" style="width:84px;height:84px" fill="#fff"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/></svg></div><div id="stn" style="position:absolute;left:204px;top:44px;font:700 112px/1 Poppins;letter-spacing:-3px;color:#0a0d2c">0</div><div style="position:absolute;left:208px;top:176px;font:700 30px/1 Poppins;color:#294b77">bintang GitHub</div><div style="position:absolute;left:44px;top:250px;font:400 24px/1 Poppins;color:#294b77">dibaca langsung dari repo, 28 Nov 2026</div></div>`);
  const STN = STARS.querySelector("#stn"); STN.removeAttribute("id");
  const t3 = { in: T3 + 0.18, os: wt(17) - 0.06, mit: wt(19) - 0.06, st: T4 + 0.08, cnt: wt(23) - 0.15 };
  ev(T3 + 0.02, "whoosh", -4, 1.4); ev(t3.in + 0.1, "pop", -6, 0.85); ev(t3.os, "pop", -4, 1.05); ev(t3.mit, "pop", -4, 1.15);
  ev(t3.st, "whoosh", -6, 1.1); for (let k = 0; k < 12; k++) ev(t3.cnt + k * 0.07, "click", -10, 1.15 + k * 0.03); ev(t3.cnt + 0.9, "sparkle", -3);
  const fmt = (n) => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  function repo(t) {
    if (t < T3 || t > T5 + 0.5) { hide(REPO); hide(STARS); return; }
    const fl = 1 - eio(t, T3 + 0.08, T3 + 0.36), out = eio(t, T5 - 0.3, T5);
    const up = eio(t, T4, T4 + 0.4);
    S(REPO, { o: lin(t, T3 + 0.1, T3 + 0.14) * (1 - lin(t, T5 - 0.16, T5)), ry: -90 * fl, y: -30 * up + 300 * ei(t, T5 - 0.3, T5), s: L(1, 0.97, up) });
    frame(GH, 360 * eio(t, t3.in, t3.in + 1.0) + wob(t, 1, 22));
    const ou = spr(t, t3.os, 17, 0.55), mu = spr(t, t3.mit, 17, 0.55);
    S(OS, { o: Math.min(1, ou * 3), s: 0.6 + 0.4 * ou }); S(MIT, { o: Math.min(1, mu * 3), s: 0.6 + 0.4 * mu });
    OS.classList.toggle("on", t > t3.os + 0.1); MIT.classList.toggle("on", t > t3.mit + 0.1);
    const su = spr(t, t3.st, 14, 0.7);
    S(STARS, { o: Math.min(1, su * 3) * (1 - out), y: 200 * (1 - su) + 300 * out, s: 0.9 + 0.1 * su });
    STN.textContent = fmt(Math.round(105364 * eio(t, t3.cnt, t3.cnt + 0.85)));
  }

  // ================================================================== 6-7 + 13 · FLOOR PLAN (move, breathe, signal changes; lamp)
  const T6 = BS[6] + AFTER, T7 = BS[7], T8 = BS[8], T13 = BS[13], T14 = BS[14];
  const PLAN = mk(`<div class="card" style="left:90px;top:640px;width:900px;height:700px;transform-origin:450px 0;overflow:hidden"><div class="lbl" style="left:36px;top:34px">Denah · ilustrasi</div><div class="demo" style="right:34px;top:26px">SIMULASI</div></div>`);
  const PSV = sv("svg", { width: 900, height: 700, viewBox: "0 0 900 700", style: "position:absolute;left:0;top:0" }, PLAN);
  const pd = sv("defs", {}, PSV); const pc = sv("clipPath", { id: "room" }, pd); sv("rect", { x: 40, y: 90, width: 820, height: 580, rx: 24 }, pc);
  sv("rect", { x: 40, y: 90, width: 820, height: 580, rx: 24, fill: "#f6f9fe" }, PSV);
  const LIGHT = sv("circle", { cx: 760, cy: 190, r: 260, fill: "url(#lg)", opacity: 0 }, PSV);
  const lg = sv("radialGradient", { id: "lg" }, pd); sv("stop", { offset: "0", "stop-color": "#7fb0ff", "stop-opacity": ".55" }, lg); sv("stop", { offset: "1", "stop-color": "#7fb0ff", "stop-opacity": "0" }, lg);
  const PG = sv("g", { "clip-path": "url(#room)" }, PSV);
  const PWAV = [0, 1, 2, 3, 4].map(() => sv("circle", { cx: 130, cy: 180, r: 10, fill: "none", stroke: "#2f6bff", "stroke-width": 5 }, PG));
  sv("rect", { x: 80, y: 440, width: 170, height: 190, rx: 18, fill: "rgba(41,75,119,.10)", stroke: "rgba(41,75,119,.25)", "stroke-width": 3 }, PSV);
  sv("rect", { x: 98, y: 456, width: 134, height: 44, rx: 12, fill: "rgba(41,75,119,.12)" }, PSV);
  sv("rect", { x: 590, y: 520, width: 220, height: 96, rx: 22, fill: "rgba(41,75,119,.12)", stroke: "rgba(41,75,119,.25)", "stroke-width": 3 }, PSV);
  sv("path", { d: "M470 90V330M470 430V670", stroke: "#294b77", "stroke-width": 10, "stroke-linecap": "round" }, PSV);
  sv("rect", { x: 40, y: 90, width: 820, height: 580, rx: 24, fill: "none", stroke: "#294b77", "stroke-width": 10 }, PSV);
  const RAYS = sv("path", { d: "", fill: "none", stroke: "#2f6bff", "stroke-width": 5, "stroke-dasharray": "14 12", "stroke-linecap": "round", opacity: 0 }, PSV);
  mk(`<div style="position:absolute;left:66px;top:640px;font:700 20px/1 Poppins;color:#294b77;letter-spacing:2px">KAMAR</div>`, PLAN);
  mk(`<div style="position:absolute;left:500px;top:640px;font:700 20px/1 Poppins;color:#294b77;letter-spacing:2px">RUANG TAMU</div>`, PLAN);
  const PROUT = mk(`<div class="ic" style="position:absolute;left:88px;top:138px;width:84px;height:84px;border-radius:24px">${ico("wifi")}</div>`, PLAN);
  const LAMP = mk(`<div style="position:absolute;left:715px;top:145px;width:90px;height:90px;border-radius:50%;display:grid;place-items:center;background:#fff;box-shadow:0 0 0 3px rgba(41,75,119,.25)">${ico("lightbulb", "#294b77", 2.2).replace("<svg", '<svg style="width:52px;height:52px"')}</div>`, PLAN);
  const SENS = mk(`<div class="ic" style="position:absolute;left:770px;top:590px;width:64px;height:64px;border-radius:18px">${ico("cpu")}</div>`, PLAN);
  const BRE = [0, 1].map(() => mk(`<div style="position:absolute;left:0;top:0;width:120px;height:120px;margin:-60px 0 0 -60px;border-radius:50%;border:4px solid #2f6bff"></div>`, PLAN));
  const PP = mk(`<div class="ic" style="position:absolute;left:0;top:0;width:96px;height:96px;margin:-48px 0 0 -48px;border-radius:50%;box-shadow:0 10px 24px rgba(19,48,126,.3)">${ico("user")}</div>`, PLAN);
  const PTAG = mk(`<div class="chip on" style="left:0;top:0;font-size:22px;padding:9px 14px">${ico("activity", "#fff", 2.4)}<span>gerak</span></div>`, PLAN); const PTAGS = PTAG.querySelector("span");
  // CSI graph panel (7-8)
  const GRAPH = mk(`<div class="card" style="left:90px;top:1210px;width:900px;height:330px"><div class="lbl" style="left:36px;top:30px">Sinyal Wi-Fi (CSI) · ilustrasi</div></div>`);
  const GSV = sv("svg", { width: 900, height: 330, viewBox: "0 0 900 330", style: "position:absolute;left:0;top:0" }, GRAPH);
  sv("path", { d: "M40 200H860", stroke: "rgba(41,75,119,.15)", "stroke-width": 2 }, GSV);
  const GL2 = sv("path", { d: "", fill: "none", stroke: "rgba(41,75,119,.35)", "stroke-width": 3 }, GSV);
  const GL1 = sv("path", { d: "", fill: "none", stroke: "#2f6bff", "stroke-width": 5, "stroke-linejoin": "round" }, GSV);
  const GCH = mk(`<div class="chip on" style="left:640px;top:20px">${ico("zap", "#fff", 2.4)}berubah!</div>`, GRAPH);
  const P_PATH = [[300, 300], [470, 380], [640, 360], [700, 470]];
  function walk(u) { const n = P_PATH.length - 1, k = Math.min(n - 1, Math.floor(u * n)), f = u * n - k; return [L(P_PATH[k][0], P_PATH[k + 1][0], f), L(P_PATH[k][1], P_PATH[k + 1][1], f)]; }
  const t6 = { walk0: wt(31), walk1: wt(34) + 0.1, br: wt(35) - 0.05, rays: wt(36) - 0.05, ch: wt(38) - 0.05 };
  const t13 = { in: T13 + 0.05, walk0: wt(73), walk1: wt(75) - 0.05, lamp: wt(75) - 0.05, auto: wt(76) - 0.1, ha: wt(78) - 0.1 };
  const HP = [[470, 760], [470, 380], [640, 330]];   // Home Assistant beat: walks in through the door
  const AUTO = mk(`<div class="card" style="left:90px;top:1370px;width:900px;height:180px"><div style="position:absolute;left:176px;top:40px;font:700 32px/1.2 Poppins;color:#0a0d2c;white-space:nowrap">Ada orang masuk → lampu nyala</div><div style="position:absolute;left:176px;top:94px;font:400 26px/1.2 Poppins;color:#294b77;white-space:nowrap">otomasi lewat Home Assistant</div><div class="demo" style="right:28px;top:22px">CONTOH</div></div>`);
  const HA = spr3("homeassistant", 130, 24, 25, AUTO);
  ev(T6 - 0.05, "whoosh", -3, 0.9); ev(T6 + 0.15, "pop", -8); ev(t6.walk0, "click", -10, 0.9); ev(t6.br, "ping", -6, 0.8);
  ev(t6.rays, "whoosh", -7, 1.5); ev(T7 + 0.05, "pop", -7, 1.1); ev(t6.ch, "impact", -8);
  ev(T13 - 0.02, "whoosh", -3, 1.0); ev(t13.lamp, "ping", -2, 1.1); ev(t13.lamp + 0.05, "sparkle", -6); ev(t13.auto, "pop", -5); ev(t13.ha, "pop", -4, 0.9);
  function gpath(t, amp, ph) {
    let d = "";
    for (let i = 0; i <= 120; i++) {
      const x = 40 + i * 820 / 120, q = i / 120;
      const y = 200 - 34 * Math.sin(q * 18 + t * 3 + ph) - amp * (Math.sin(q * 47 + t * 9.3 + ph) * 0.6 + Math.sin(q * 91 - t * 13.7) * 0.4) * Math.exp(-Math.pow((q - 0.62) * 3.2, 2));
      d += (i ? "L" : "M") + x.toFixed(1) + " " + y.toFixed(1);
    }
    return d;
  }
  function graph(t) {
    if (t < T7 || t > BS[10] + 0.4) { hide(GRAPH); return; }
    const gu = spr(t, T7 + 0.15, 14, 0.72), go = lin(t, BS[10] + 0.05, BS[10] + 0.3);
    S(GRAPH, { o: Math.min(1, gu * 3) * (1 - go), y: 220 * (1 - gu) + 260 * ei(t, BS[10] - 0.02, BS[10] + 0.3) });
    const amp = 8 + 70 * eo(t, t6.ch, t6.ch + 0.3) + 14 * Math.sin(t * 1.6);
    GL1.setAttribute("d", gpath(t, amp, 0)); GL2.setAttribute("d", gpath(t * 0.8, amp * 0.5, 1.7));
    const cu = spr(t, t6.ch, 18, 0.5); S(GCH, { o: Math.min(1, cu * 3), s: 0.6 + 0.4 * cu });
  }
  function plan(t) {
    const seg1 = t > T6 - 0.05 && t < T8 + 0.5, seg2 = t > T13 - 0.05 && t < T14 + 0.45;
    graph(t);
    if (!seg1 && !seg2) { hide(PLAN); hide(AUTO); return; }
    if (seg1) {
      const u = spr(t, T6, 13, 0.75), sh = eio(t, T7 - 0.02, T7 + 0.4);
      const w = whip((tt) => -1200 * ei(tt, T8 - 0.02, T8 + 0.3), t);
      S(PLAN, { o: Math.min(1, u * 3) * (1 - lin(t, T8 + 0.2, T8 + 0.3)), y: 260 * (1 - u) - 40 * sh, s: (0.92 + 0.08 * Math.min(1, u)) * L(1, 0.79, sh), x: w.x, b: w.b });
      // person walks on "gerak", settles on the sofa, breathes on "napas"
      const g = eio(t, t6.walk0, t6.walk1), [px, py] = walk(g);
      S(PP, { x: px, y: py, s: 1 + 0.06 * Math.sin(t * 2 * Math.PI * 0.28) * lin(t, t6.br, t6.br + 0.3) });
      S(PTAG, { x: px + 54, y: py - 96, o: lin(t, t6.walk0, t6.walk0 + 0.15) });
      PTAGS.textContent = t > t6.br ? "napas" : "gerak";
      BRE.forEach((b, i) => { const f = ((t - t6.br) * 0.7 + i * 0.5) % 1; S(b, { x: px, y: py, s: 0.8 + 0.9 * f, o: t > t6.br ? 0.7 * (1 - f) : 0 }); });
      S(SENS, { o: eo(t, T7, T7 + 0.25), s: 0.6 + 0.4 * spr(t, T7, 16, 0.6) });
      RAYS.setAttribute("d", `M130 180 L${px.toFixed(0)} ${py.toFixed(0)} L802 622`); RAYS.setAttribute("opacity", (0.9 * eo(t, t6.rays, t6.rays + 0.3)).toFixed(2));
      RAYS.setAttribute("stroke-dashoffset", (-t * 90).toFixed(1));
      LIGHT.setAttribute("opacity", 0); S(LAMP, { o: 0.55 }); LAMP.style.background = "#fff";
      hide(AUTO);
    } else {
      const u = 1 - eio(t, t13.in, t13.in + 0.34), out = eio(t, T14 - 0.24, T14 + 0.06);
      S(PLAN, { o: lin(t, t13.in, t13.in + 0.06) * (1 - lin(t, T14 - 0.12, T14 + 0.06)), rx: 70 * u, s: 1, y: -10 + 260 * ei(t, T14 - 0.24, T14 + 0.06) });
      const g = eio(t, t13.walk0, t13.walk1), k = g < 0.5 ? 0 : 1, f = g < 0.5 ? g * 2 : g * 2 - 1;
      const px = L(HP[k][0], HP[k + 1][0], f), py = L(HP[k][1], HP[k + 1][1], f);
      S(PP, { x: px, y: py, s: 1, o: lin(t, t13.walk0, t13.walk0 + 0.15) }); hide(PTAG); BRE.forEach(hide); hide(SENS);
      RAYS.setAttribute("opacity", 0);
      const lu = eo(t, t13.lamp, t13.lamp + 0.25);
      LIGHT.setAttribute("opacity", (lu * (0.9 + 0.1 * Math.sin(t * 7))).toFixed(3));
      S(LAMP, { o: 0.55 + 0.45 * lu, s: 1 + 0.25 * Math.sin(Math.PI * lin(t, t13.lamp, t13.lamp + 0.3)) });
      LAMP.style.background = lu > 0.5 ? "#dbe8ff" : "#fff"; LAMP.style.boxShadow = `0 0 0 3px rgba(41,75,119,.25), 0 0 ${(70 * lu).toFixed(0)}px rgba(47,107,255,${(0.55 * lu).toFixed(2)})`;
      const au = spr(t, t13.auto, 14, 0.7);
      S(AUTO, { o: Math.min(1, au * 3) * (1 - out), y: 160 * (1 - au) + 300 * ei(t, T14 - 0.24, T14 + 0.06) });
      const hu = spr(t, t13.ha, 16, 0.55); S(HA, { o: Math.min(1, hu * 3), s: 0.5 + 0.5 * hu }); frame(HA, 360 * eio(t, t13.ha, t13.ha + 0.9) + wob(t, 2, 18));
    }
    PWAV.forEach((c, i) => { const f = ((t * 0.7 + i / 5) % 1); c.setAttribute("r", (20 + 900 * f).toFixed(1)); c.setAttribute("opacity", ((1 - f) * 0.45).toFixed(3)); });
    S(PROUT, { s: 1 + 0.05 * Math.sin(t * 6) });
  }

  // ================================================================== 8-10 · SENSOR board -> AI node -> dashboard
  const T9 = BS[9], T10 = BS[10], T11 = BS[11];
  const BOARD = mk(`<div class="card" style="left:90px;top:640px;width:900px;height:520px"><div style="position:absolute;left:186px;top:46px;font:700 46px/1 Poppins;color:#0a0d2c">ESP32-S3</div><div style="position:absolute;left:188px;top:104px;font:400 26px/1 Poppins;color:#294b77">sensor kecil yang baca CSI Wi-Fi</div></div>`);
  const ESP = spr3("espressif", 120, 40, 28, BOARD);
  const PCB = mk(`<div style="position:absolute;left:150px;top:190px;width:600px;height:270px;border-radius:24px;background:linear-gradient(135deg,#13307e,#0a0d2c);box-shadow:0 20px 40px rgba(10,13,44,.3)"></div>`, BOARD);
  for (let i = 0; i < 14; i++) { mk(`<div style="position:absolute;left:${120 + i * 30}px;top:10px;width:14px;height:14px;border-radius:3px;background:rgba(220,232,255,.55)"></div>`, PCB); mk(`<div style="position:absolute;left:${120 + i * 30}px;top:246px;width:14px;height:14px;border-radius:3px;background:rgba(220,232,255,.55)"></div>`, PCB); }
  mk(`<svg viewBox="0 0 80 160" style="position:absolute;left:22px;top:55px;width:80px;height:160px" fill="none" stroke="#dce8ff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10H60V40H20V70H60V100H20V130H60V150"/></svg>`, PCB);
  mk(`<div style="position:absolute;left:250px;top:45px;width:270px;height:180px;border-radius:14px;background:linear-gradient(160deg,#f4f7fc,#c9d5e8);box-shadow:0 6px 14px rgba(0,0,0,.25);display:grid;place-items:center"><div class="mono" style="font-size:34px;color:#0a0d2c;text-align:center;line-height:1.3">ESP32-S3<br/><span style="font-size:22px;color:#294b77">Wi-Fi · CSI</span></div></div>`, PCB);
  const LED = mk(`<div style="position:absolute;left:546px;top:205px;width:22px;height:22px;border-radius:50%;background:#01ccf7"></div>`, PCB);
  const PRICE = mk(`<div class="stamp" style="left:560px;top:44px;font-size:30px">± $9 / sensor</div>`, BOARD);
  const DOTS = [0, 1, 2, 3, 4, 5, 6, 7].map(() => mk(`<div style="position:absolute;left:0;top:0;width:22px;height:22px;margin:-11px 0 0 -11px;border-radius:50%;background:#2f6bff;box-shadow:0 0 12px rgba(47,107,255,.6)"></div>`));
  const DG = DOTS.map((d) => ghosts(d));
  const AIN = mk(`<div style="position:absolute;left:700px;top:790px;width:240px;height:240px"><div class="ainr" style="position:absolute;left:-20px;top:-20px;width:280px;height:280px;border-radius:50%;border:5px dashed #2f6bff"></div><div class="ic" style="position:absolute;left:0;top:0;width:240px;height:240px;border-radius:50%;background:linear-gradient(135deg,#13307e,#2f6bff);box-shadow:0 24px 50px rgba(19,48,126,.35)">${ico("sparkles", "#fff", 1.8)}</div><div class="chip on" style="left:10px;top:290px">model AI kecil</div></div>`);
  const AINR = AIN.querySelector(".ainr");
  const ARROW = mk(`<svg style="position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920"><path d="M510 910 L660 910" stroke="#294b77" stroke-width="8" stroke-linecap="round" fill="none" stroke-dasharray="150" stroke-dashoffset="150"/><path d="M640 890 L664 910 L640 930" stroke="#294b77" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none" opacity="0"/></svg>`);
  const AR1 = ARROW.children[0], AR2 = ARROW.children[1];
  const DASH = mk(`<div class="card" style="left:90px;top:680px;width:900px;height:700px"><div style="position:absolute;left:34px;top:30px;display:flex;align-items:center;gap:18px"><span class="ic" style="width:66px;height:66px">${ico("house")}</span><span style="font:700 42px/1 Poppins">Ruang tamu</span></div><div class="demo" style="right:34px;top:40px">SIMULASI</div></div>`);
  const ROWS = [["user", "Ada orang?", "kehadiran"], ["activity", "Gerakan", "jalan, duduk"], ["audio-lines", "Napas", "dari gerak dada"]].map(([ic, a, b], i) =>
    mk(`<div class="row" style="top:${140 + i * 180}px;height:140px"><span class="ic">${ico(ic)}</span><div><div class="t">${a}</div><div class="s">${b}</div></div><div class="viz" style="width:190px;height:70px;position:relative;margin-left:auto"></div><span class="tag"></span></div>`, DASH));
  const BARS = [0, 1, 2, 3, 4, 5].map((i) => mk(`<div style="position:absolute;left:${i * 32}px;bottom:4px;width:22px;height:60px;border-radius:6px;background:#2f6bff;transform-origin:50% 100%"></div>`, ROWS[1].querySelector(".viz")));
  const BSV = sv("svg", { width: 190, height: 70, viewBox: "0 0 190 70" }, ROWS[2].querySelector(".viz")); const BRL = sv("path", { d: "", fill: "none", stroke: "#2f6bff", "stroke-width": 5, "stroke-linecap": "round" }, BSV);
  const TAGS = ROWS.map((r) => r.querySelector(".tag"));
  const tickS = ico("check", "#fff", 3);
  const t8 = { in: BS[8] + 0.05, price: wt(46) - 0.08, catch0: wt(48) - 0.05, ai: T9 + 0.1, arrow: T9 + 0.05, dash: T10 + 0.05, r: [wt(54) - 0.08, wt(58) - 0.08, wt(60) - 0.05], tg: [wt(57) - 0.02, wt(59), wt(61) + 0.05] };
  ev(t8.in, "whoosh", -2, 1.25); ev(t8.in + 0.2, "pop", -8); ev(t8.price, "impact", -6); for (let k = 0; k < 8; k++) ev(t8.catch0 + k * 0.07, "click", -12, 1.4);
  ev(t8.catch0 + 0.6, "ping", -6, 1.2); ev(t8.arrow, "whoosh", -6, 1.6); ev(t8.ai + 0.15, "sparkle", -4); ev(t8.dash, "whoosh", -3, 0.85);
  t8.r.forEach((x) => ev(x, "pop", -6, 1.0)); t8.tg.forEach((x, i) => ev(x, "click", -6, 1.1 + 0.05 * i));
  function sensor(t) {
    if (t < BS[8] - 0.05 || t > T11 + 0.5) { hide(BOARD); hide(AIN); hide(ARROW); hide(DASH); DOTS.forEach((d, i) => { hide(d); hide(DG[i][0]); hide(DG[i][1]); }); return; }
    // board: whips in from the right, shrinks left for the AI step, fades on the dashboard zoom
    const w = whip((tt) => 1200 * (1 - eo(tt, t8.in, t8.in + 0.45)), t), sh = eio(t, T9, T9 + 0.4), z = eio(t, T10 - 0.02, T10 + 0.3);
    S(BOARD, { o: lin(t, t8.in, t8.in + 0.08) * (1 - z), x: w.x + L(0, -250, sh), y: L(0, 60, sh), s: L(1, 0.56, sh), b: w.b + 6 * z });
    BOARD.style.transformOrigin = "450px 260px";
    frame(ESP, 360 * eio(t, t8.in + 0.1, t8.in + 1.1) + wob(t, 3, 20));
    const pu = spr(t, t8.price, 20, 0.5); S(PRICE, { o: Math.min(1, pu * 3) * (1 - sh), s: 1.5 - 0.5 * pu, r: 6 });
    const blink = t > t8.catch0 ? 0.5 + 0.5 * Math.sin((t - t8.catch0) * 22) : 0.2;
    S(LED, { o: 0.4 + 0.6 * blink, s: 1 + 0.4 * blink });
    // signal dots fly from the graph into the antenna
    DOTS.forEach((d, i) => {
      const a = t8.catch0 + i * 0.07;
      mb(d, DG[i], (tt) => { const g = eio(tt, a, a + 0.5); return { x: L(420 + i * 60, 285, g), y: L(1370 - 40 * Math.sin(i * 1.3), 965, g) - 120 * Math.sin(Math.PI * g), o: lin(tt, a, a + 0.05) * (1 - lin(tt, a + 0.44, a + 0.5)), s: L(1, 0.5, g) }; }, t);
    });
    // AI node + arrow
    const au = spr(t, t8.ai, 13, 0.6);
    S(AIN, { o: Math.min(1, au * 3) * (1 - lin(t, T10 + 0.15, T10 + 0.32)), s: (0.5 + 0.5 * au) * (1 + 3 * ei(t, T10 - 0.02, T10 + 0.32)), x: -L(0, 260, ei(t, T10 - 0.02, T10 + 0.32)) });
    AINR.style.transform = `rotate(${(t * 70).toFixed(1)}deg)`;
    S(ARROW, { o: 1 - lin(t, T10, T10 + 0.12) });
    AR1.setAttribute("stroke-dashoffset", (150 * (1 - eio(t, t8.arrow, t8.arrow + 0.3))).toFixed(1)); AR2.setAttribute("opacity", lin(t, t8.arrow + 0.25, t8.arrow + 0.3).toFixed(2));
    // dashboard (zoom-through from the AI node)
    const du = spr(t, t8.dash + 0.08, 13, 0.75), dout = eio(t, T11 - 0.02, T11 + 0.32);
    S(DASH, { o: Math.min(1, du * 3) * (1 - lin(t, T11 + 0.1, T11 + 0.3)), s: (0.6 + 0.4 * Math.min(1.02, du)), y: 1000 * ei(t, T11 - 0.02, T11 + 0.32), b: 10 * (1 - Math.min(1, du * 1.5)) });
    ROWS.forEach((r, i) => { const v = spr(t, t8.r[i], 16, 0.65); S(r, { o: Math.min(1, v * 3), x: 60 * (1 - v) }); });
    const tg = (i, on, txt0, txt1) => { TAGS[i].innerHTML = t > t8.tg[i] ? tickS.replace("<svg", '<svg style="width:24px;height:24px"') + txt1 : txt0; TAGS[i].classList.toggle("soft", !(t > t8.tg[i])); S(TAGS[i], { s: 1 + 0.15 * Math.sin(Math.PI * lin(t, t8.tg[i], t8.tg[i] + 0.25)) }); };
    tg(0, 1, "…", "ada"); tg(1, 1, "…", "bergerak"); tg(2, 1, "…", "terdeteksi");
    BARS.forEach((b, i) => S(b, { sy: 0.25 + 0.75 * Math.abs(Math.sin(t * (5 + i * 1.3) + i)) * lin(t, t8.r[1], t8.r[1] + 0.3) }));
    let d = ""; for (let i = 0; i <= 40; i++) { const x = 5 + i * 4.5, y = 35 - 24 * Math.sin(i / 40 * Math.PI * 2 * 1.5 - t * 2.2) * lin(t, t8.r[2], t8.r[2] + 0.3); d += (i ? "L" : "M") + x.toFixed(1) + " " + y.toFixed(1); }
    BRL.setAttribute("d", d);
  }

  // ================================================================== 11-12 · CLAUDE CODE (client's own recording) -> plugin terminal
  const T12 = BS[12];
  const WIN = mk(`<div style="position:absolute;left:90px;top:720px;width:900px;height:300px;border-radius:30px;overflow:hidden;background:#181818;box-shadow:0 30px 60px rgba(10,13,44,.3)"></div>`);
  const RV = mk(`<div style="position:absolute;left:20px;top:20px;width:860px;height:260px;overflow:hidden;background:#181818"></div>`, WIN);
  const KF = []; for (let k = 1; k <= 60; k++) { const im = document.createElement("img"); im.src = `assets/rec/code/c_${String(k).padStart(3, "0")}.jpg`; im.style.cssText = "position:absolute;left:10px;top:30px;width:839px;height:196px;display:none"; RV.appendChild(im); KF.push(im); }
  const MASK = mk(`<div style="position:absolute;left:100px;top:72px;width:720px;height:66px;background:#303030"></div>`, RV);
  const TY = mk(`<div style="position:absolute;left:4px;top:8px;font:400 36px/48px Poppins;color:#f2f2f2;white-space:nowrap"></div>`, MASK);
  const CARET = mk(`<div style="position:absolute;top:12px;width:3px;height:42px;background:#f2f2f2"></div>`, MASK);
  const TERM = mk(`<div style="position:absolute;left:44px;top:110px;width:820px"></div>`, WIN);
  const THEAD = mk(`<div style="position:absolute;left:44px;top:40px;display:flex;align-items:center;gap:14px;font:700 28px/1 Poppins;color:#f2f2f2"><span style="width:16px;height:16px;border-radius:50%;background:#D97757;display:block"></span>Claude Code · plugin RuView</div>`, WIN);
  const CMDS = ["/plugin marketplace add ruvnet/RuView", "/plugin install ruview@ruview", "/ruview-start"];
  const CL = CMDS.map((c, i) => mk(`<div class="mono" style="position:absolute;left:0;top:${i * 118}px;width:820px;font-size:32px;line-height:44px;color:#f2f2f2;white-space:nowrap"><span style="color:#D97757">&gt; </span><span class="tx"></span><span class="cr" style="display:inline-block;width:16px;height:34px;margin-left:2px;vertical-align:-5px;background:#f2f2f2"></span></div>`, TERM));
  const CS = CL.map((c, i) => mk(`<div style="position:absolute;left:0;top:${i * 118 + 54}px;font:400 24px/1 Poppins;color:#9fb6d9;white-space:nowrap">${["tambah daftar plugin dari repo", "pasang plugin-nya", "mulai panduan pasang (demo Docker / ESP32)"][i]}</div>`, TERM));
  const CLOGO = spr3("claude", 150, 870, 650);
  const RECT = mk(`<div class="demo" style="left:90px;top:708px;background:#294b77;color:#fff">REKAMAN ASLI · CLAUDE CODE</div>`);
  const CP = mk(`<div class="chip" style="left:90px;top:1086px">${ico("sparkles", "#294b77", 2.2)}contoh prompt</div>`);
  const READ = mk(`<div class="chip on" style="left:90px;top:1440px">${ico("file-text", "#fff", 2.2)}perintah dari README RuView</div>`);
  const CUR = mk(`<svg class="cur" viewBox="0 0 24 24"><path d="M4 2l16 9-7 2-3 7z" fill="#0a0d2c" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/></svg>`);
  const PROMPT = "Pasang RuView dari GitHub";
  const t11 = { in: T11 + 0.08, cur: T11 + 0.12, click: T11 + 0.62, ty: T11 + 0.72, cps: 0.042, grow: T12 + 0.02, c0: T12 + 0.3, cps2: 0.014, out: BS[13] };
  ev(t11.in, "whoosh", -3, 1.0); ev(t11.click, "click", -2); for (let k = 0; k < 6; k++) ev(t11.ty + k * 0.17, "type", -6 - (k % 2));
  ev(t11.grow, "whoosh", -4, 0.75); let tt0 = t11.c0; CMDS.forEach((c, i) => { ev(tt0, "type", -6); ev(tt0 + c.length * t11.cps2 * 0.5, "type", -7); ev(tt0 + c.length * t11.cps2 + 0.05, "pop", -9, 1.2 + 0.1 * i); tt0 += c.length * t11.cps2 + 0.14; });
  ev(wt(70) - 0.05, "ping", -6, 1.1); ev(t11.out, "whoosh", -4, 1.3);
  function code(t) {
    if (t < T11 || t > BS[13] + 0.4) { [WIN, CLOGO, RECT, CP, READ, CUR].forEach(hide); return; }
    const u = spr(t, t11.in, 13, 0.72), g = eio(t, t11.grow, t11.grow + 0.45), out = eio(t, t11.out - 0.02, t11.out + 0.3);
    WIN.style.height = L(300, 700, g).toFixed(1) + "px"; WIN.style.top = L(760, 660, g).toFixed(1) + "px";
    S(WIN, { o: Math.min(1, u * 3) * (1 - lin(t, t11.out + 0.12, t11.out + 0.3)), y: 500 * (1 - u), s: L(1, 0.5, out), r: -8 * out });
    // the client's real Claude Code input (rec frames), then a typed example prompt
    const fi = Math.min(59, Math.max(0, Math.floor((t - t11.in) * 30)));
    KF.forEach((im, k) => { im.style.display = k === fi ? "block" : "none"; });
    S(RV, { o: 1 - lin(t, t11.grow, t11.grow + 0.2) });
    const n = Math.max(0, Math.min(PROMPT.length, Math.floor((t - t11.ty) / t11.cps)));
    S(MASK, { o: lin(t, t11.click, t11.click + 0.06) });
    TY.textContent = PROMPT.slice(0, n); CARET.style.left = (TY.offsetWidth + 8) + "px"; CARET.style.opacity = (Math.floor(t * 2.5) % 2 || n < PROMPT.length) ? 1 : 0;
    // terminal (README commands typed)
    S(THEAD, { o: lin(t, t11.grow + 0.2, t11.grow + 0.35) }); S(TERM, { o: lin(t, t11.grow + 0.2, t11.grow + 0.35) });
    let a = t11.c0;
    CL.forEach((c, i) => {
      const m = Math.max(0, Math.min(CMDS[i].length, Math.floor((t - a) / t11.cps2)));
      c.querySelector(".tx").textContent = CMDS[i].slice(0, m);
      const done = a + CMDS[i].length * t11.cps2;
      S(c, { o: t > a - 0.05 ? 1 : 0 }); c.querySelector(".cr").style.opacity = (t > a && t < done + 0.15) ? 1 : 0;
      const sv_ = spr(t, done + 0.05, 16, 0.65); S(CS[i], { o: Math.min(1, sv_ * 3), x: 20 * (1 - sv_) });
      a = done + 0.14;
    });
    const lu = spr(t, t11.in + 0.25, 15, 0.55);
    S(CLOGO, { o: Math.min(1, lu * 3) * (1 - out), s: 0.5 + 0.5 * lu, y: L(0, -70, g) }); frame(CLOGO, 360 * eio(t, t11.in + 0.25, t11.in + 1.2) + wob(t, 4, 20));
    S(RECT, { o: lin(t, t11.in + 0.2, t11.in + 0.35) * (1 - lin(t, t11.grow, t11.grow + 0.15)) });
    const pu = spr(t, t11.ty + 0.1, 16, 0.6); S(CP, { o: Math.min(1, pu * 3) * (1 - lin(t, t11.grow, t11.grow + 0.15)), y: 20 * (1 - pu) });
    const ru = spr(t, wt(70) - 0.05, 16, 0.6); S(READ, { o: Math.min(1, ru * 3) * (1 - out), y: 30 * (1 - ru) });
    // cursor glides to the input and clicks (html-demo technique)
    const cg = eio(t, t11.cur, t11.cur + 0.45), pr = lin(t, t11.click, t11.click + 0.06) * (1 - lin(t, t11.click + 0.12, t11.click + 0.2));
    S(CUR, { o: lin(t, t11.cur, t11.cur + 0.1) * (1 - lin(t, t11.ty + 0.4, t11.ty + 0.6)), x: L(1000, 560, cg), y: L(1340, 870, cg), s: 1.2 - 0.2 * pr });
  }

  // ================================================================== 14 · BETA stamp (mascot forward) · 15-16 · LIMITS card
  const T15 = BS[15] + AFTER, T16 = BS[16], T17 = BS[17];
  const BETA = mk(`<div class="stamp" style="left:740px;top:760px;font-size:52px;padding:16px 30px">BETA</div>`);
  const t14 = { st: wt(83) - 0.1 };
  ev(t14.st, "impact", -4);
  const LIM = mk(`<div class="card" style="left:90px;top:660px;width:900px;height:640px"><div class="lbl" style="left:36px;top:36px">Batasannya, jujur aja</div><div class="demo" style="right:34px;top:28px">STATUS: BETA</div></div>`);
  const LR = [["laptop", "Laptop biasa", "tanpa sensor CSI", "deteksi kasar", 1], ["cpu", "Pakai ESP32-S3", "baca CSI penuh", "lebih detail", 0], ["user", "Pose tubuh", "tanpa kamera", "belum akurat", 1]].map(([ic, a, b, tg, soft], i) =>
    mk(`<div class="row" style="top:${110 + i * 170}px"><span class="ic">${ico(ic)}</span><div><div class="t">${a}</div><div class="s">${b}</div></div><span class="tag${soft ? " soft" : ""}">${soft ? ico("triangle-alert", "#294b77", 2.4) : ico("check", "#fff", 3)}${tg}</span></div>`, LIM));
  const t15 = { in: T15, r: [wt(84) - 0.05, wt(86) - 0.05, wt(91) - 0.08] };
  ev(T15 - 0.02, "whoosh", -3, 0.8); ev(T15 + 0.25, "thud", -6); t15.r.forEach((x, i) => ev(x, "pop", -6, 0.95 + 0.07 * i)); ev(wt(89) - 0.05, "click", -7); ev(wt(94) - 0.05, "click", -7);
  function limits(t) {
    const bo = spr(t, t14.st, 20, 0.5);
    S(BETA, { o: t > BS[14] && t < T15 ? Math.min(1, bo * 3) * (1 - lin(t, BE[14] - 0.05, BE[14] + 0.12)) : 0, s: 1.6 - 0.6 * bo, r: -8 });
    if (t < T15 - 0.05 || t > T17 + 0.4) { hide(LIM); return; }
    const u = spr(t, T15, 11, 0.55), out = eio(t, T17 - 0.24, T17 + 0.06);
    S(LIM, { o: Math.min(1, u * 4) * (1 - lin(t, T17 - 0.12, T17 + 0.06)), y: -900 * (1 - u) + 400 * ei(t, T17 - 0.24, T17 + 0.06), s: L(1, 0.9, out) });
    LR.forEach((r, i) => { const v = spr(t, t15.r[i], 16, 0.65); S(r, { o: Math.min(1, v * 3), x: 70 * (1 - v) }); });
  }

  // ================================================================== 17-18 · PRIVACY pills (mascot forward) · CTA
  const T18 = BS[18];
  const PV = [["house", "ruangan sendiri", 70, wt(98) - 0.08], ["users", "penghuni tahu", 600, wt(101) - 0.05]].map(([ic, txt, x, t0]) =>
    [mk(`<div class="pill" style="left:${x}px;top:1490px">${ico(ic, "#294b77", 2.2)}<b>${txt}</b></div>`), t0]);
  const SHIELD = mk(`<div class="ic" style="position:absolute;left:470px;top:1290px;width:140px;height:140px;border-radius:40px;box-shadow:0 20px 40px rgba(19,48,126,.3)">${ico("shield-check")}</div>`);
  PV.forEach(([, t0]) => ev(t0, "pop", -3)); ev(wt(102) - 0.1, "ping", -6);
  const CTAB = mk(`<div id="ctab">${ico("message-circle", "#fff", 2.2)}<span>Komen WIFI</span></div>`);
  const DMC = mk(`<div class="pill" style="left:0;top:1618px;font-size:28px">${ico("send", "#294b77", 2.2)}<b>link GitHub + panduan pasang · DM</b></div>`);
  DMC.style.left = (540 - DMC.offsetWidth / 2) + "px";
  const t18 = { pill: wt(104) - 0.08, press: wt(105) - 0.02, dm: wt(111) - 0.1 };
  ev(T18 - 0.3, "riser", -7); ev(t18.pill + 0.03, "impact", -3); ev(t18.press, "click", 0); ev(t18.dm, "send", -2); ev(t18.dm + 0.1, "sparkle", -4);
  function privacy(t) {
    const out = eio(t, T18 - 0.05, T18 + 0.25);
    PV.forEach(([el, t0], i) => { const v = spr(t, t0, 16, 0.55); S(el, { o: t > T17 ? Math.min(1, v * 3) * (1 - out) : 0, y: 40 * (1 - v) + 120 * out, s: 0.7 + 0.3 * v }); });
    hide(SHIELD);   // removed: it sat on the mascot's chin
    if (t < T18 - 0.05) { hide(CTAB); hide(DMC); return; }
    const pu = spr(t, t18.pill, 15, 0.55), pr = lin(t, t18.press, t18.press + 0.08) * (1 - lin(t, t18.press + 0.16, t18.press + 0.26));
    const breathe = t > t18.press + 0.4 ? 0.025 * Math.sin((t - t18.press) * 5) : 0;
    S(CTAB, { o: Math.min(1, pu * 2.5), y: 90 * (1 - pu), s: (0.8 + 0.2 * pu) * (1 - 0.07 * pr + breathe) });
    const du = spr(t, t18.dm, 18, 0.55); S(DMC, { o: Math.min(1, du * 3), y: 30 * (1 - du), s: 0.8 + 0.2 * du });
  }

  // ================================================================== render
  const LOGO = $("brandlogo"), GR = $("grain");
  function render(t) {
    t = Math.max(0, Math.min(D, t));
    particles(t); rings(t); headline(t);
    S(LOGO, { o: 1 }); S(GR, { x: 64 * ((t * 7.3) % 1), y: 40 * ((t * 5.1) % 1), o: 0.05 });
    wall(t); repo(t); plan(t); sensor(t); code(t); limits(t); privacy(t);
  }
  return render;
  }
  // ------------------------------------------------------------------ timeline + seek hooks
  let R = null, lastT = 0;
  const tl = window.__timelines["main"];
  tl.eventCallback("onUpdate", () => { lastT = tl.time(); if (R) R(lastT); });
  window.addEventListener("hf-seek", (e) => { lastT = e.detail.time; if (R) R(lastT); });
  const imgs = ["github", "claude", "espressif", "homeassistant"].map((n) => `assets/logos3d/${n}.png`);
  for (let k = 1; k <= 60; k++) imgs.push(`assets/rec/code/c_${String(k).padStart(3, "0")}.jpg`);
  window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {};
  const fonts = ["700 24px Poppins", "400 24px Poppins", "italic 700 62px Poppins", "500 32px JBM"].map((f) => document.fonts.load(f));
  window.__hf.buildReady.ui = Promise.all(imgs.map((s) => new Promise((res) => { const i = new Image(); i.onload = i.onerror = () => res(); i.src = s; })).concat(fonts)).then(() => { R = BUILD(); window.R38_render = R; R(lastT); });
})();

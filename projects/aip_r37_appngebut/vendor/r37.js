/* R37 · "App hasil vibe coding biar ngebut" — every frame is a pure function of t (render(t) on hf-seek).
   Layout (ref2 technique, our brand): spoken headline on top (the VO line, word by word, ONE word italic + cyan),
   ONE illustrative card in the middle per beat (html-demo View(t) technique: scripted cursor, chips, flows, bars),
   the 3D mascot whole in the bottom-left corner (vendor/mascot_host.js), beat counter bottom-right, CTA pill at the end.
   Motion: closed-form springs, shared elements (database cylinder through the database tips, hook row -> first card),
   velocity-proportional blur on fast moves. SFX events are collected in window.SFX_EVENTS (tools/sfx_events.cjs -> sfx.py). */
(function () {
  const OFF = 0.3, DUR = window.TOTAL, ICO = window.ICO;
  const LINES = window.R37_LINES, WORDS = window.R37_WORDS;
  // ------------------------------------------------------------------ helpers
  const cl = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const lin = (u, a, b) => cl((u - a) / (b - a));
  const e3 = (x) => 1 - Math.pow(1 - cl(x), 3);
  const e4 = (x) => 1 - Math.pow(1 - cl(x), 4);
  const eio = (x) => { x = cl(x); return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
  const mix = (a, b, p) => a + (b - a) * p;
  const spr = (u, f = 2.2, z = 0.62) => { if (u <= 0) return 0; const w = 2 * Math.PI * f, wd = w * Math.sqrt(1 - z * z); return 1 - Math.exp(-z * w * u) * (Math.cos(wd * u) + (z * w / wd) * Math.sin(wd * u)); };
  const bump = (u, a, d) => { const x = (u - a) / d; return x > 0 && x < 1 ? Math.sin(Math.PI * x) : 0; };
  const $ = (id) => document.getElementById(id);
  function E(parent, css, html, cls) { const e = document.createElement("div"); if (cls) e.className = cls; if (css) e.style.cssText = css; if (html != null) e.innerHTML = html; parent.appendChild(e); return e; }
  const ico = (n, size = 28, col = "#ffffff", sw = 2) => `<svg width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="${col}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round">${ICO[n] || ""}</svg>`;
  const op = (e, v) => { e.style.opacity = v.toFixed(3); };
  const tf = (e, x = 0, y = 0, s = 1, r = 0) => { e.style.transform = `translate(${x.toFixed(1)}px,${y.toFixed(1)}px) scale(${s.toFixed(4)}) rotate(${r.toFixed(2)}deg)`; };
  const pop = (e, u, a, f = 2.4) => { const p = spr(u - a, f, 0.55); op(e, cl(p * 3) * (u >= a ? 1 : 0)); tf(e, 0, 18 * (1 - p), 0.6 + 0.4 * p); return p; };
  function seg(parent, cls) { return E(parent, "", null, "line" + (cls ? " " + cls : "")); }
  function segSet(e, x1, y1, x2, y2, p = 1, o = 1) { const dx = x2 - x1, dy = y2 - y1, L = Math.hypot(dx, dy); e.style.left = x1 + "px"; e.style.top = y1 - 2 + "px"; e.style.width = (L * cl(p)).toFixed(1) + "px"; e.style.transform = `rotate(${Math.atan2(dy, dx)}rad)`; op(e, o); }
  function pkSet(e, x1, y1, x2, y2, p, o = 1) { e.style.left = mix(x1, x2, p).toFixed(1) + "px"; e.style.top = mix(y1, y2, p).toFixed(1) + "px"; op(e, o); }
  const CUR = '<svg width="46" height="46" viewBox="0 0 24 24"><path d="M4 2l15 9.5-6.6 1.4 3.6 7.2-2.9 1.4-3.6-7.3L4 19z" fill="#ffffff" stroke="#0a0d2c" stroke-width="1.4" stroke-linejoin="round"/></svg>';
  function cursor(root) { return E(root, "", CUR, "cur"); }
  // glide through keys [[t,x,y],...] (person-like: eased moves, rests between)
  function glide(u, K) { if (u <= K[0][0]) return [K[0][1], K[0][2]]; for (let i = 1; i < K.length; i++) if (u <= K[i][0]) { const p = eio((u - K[i - 1][0]) / (K[i][0] - K[i - 1][0])); return [mix(K[i - 1][1], K[i][1], p), mix(K[i - 1][2], K[i][2], p)]; } const k = K[K.length - 1]; return [k[1], k[2]]; }
  function curSet(e, u, K, clicks = [], o = 1) { const [x, y] = glide(u, K); let s = 1; for (const c of clicks) s -= 0.16 * bump(u, c - 0.05, 0.2); tf(e, x - 8, y - 4, s); op(e, o); }
  function ripple(root) { return E(root, "position:absolute;width:20px;height:20px;border-radius:50%;border:3px solid #01ccf7;opacity:0", null); }
  function ripSet(e, u, c, x, y) { const p = lin(u, c, c + 0.45); const d = 20 + 100 * e3(p); e.style.left = x - d / 2 + "px"; e.style.top = y - d / 2 + "px"; e.style.width = e.style.height = d + "px"; op(e, p > 0 && p < 1 ? 0.9 * (1 - p) : 0); }
  const spinner = (size = 60) => `<svg width="${size}" height="${size}" viewBox="0 0 50 50"><circle cx="25" cy="25" r="19" fill="none" stroke="rgba(184,241,255,.18)" stroke-width="5"/><path d="M25 6a19 19 0 0 1 19 19" fill="none" stroke="#01ccf7" stroke-width="5" stroke-linecap="round"/></svg>`;
  const picture = (w, h) => `<svg width="${w}" height="${h}" viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="pg${w}${h}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#294b77"/><stop offset="1" stop-color="#0d6f95"/></linearGradient></defs><rect width="300" height="200" fill="url(#pg${w}${h})"/><circle cx="214" cy="62" r="24" fill="#b8f1ff"/><path d="M0 200 L92 96 L150 160 L196 118 L300 200 Z" fill="#01ccf7" opacity=".85"/><path d="M0 200 L70 140 L120 200 Z" fill="#e9fbff" opacity=".6"/></svg>`;
  const DBSVG = '<svg width="132" height="118" viewBox="0 0 132 118"><defs><linearGradient id="dbg" x1="0" x2="1"><stop offset="0" stop-color="#1b3170"/><stop offset=".55" stop-color="#2d5aa8"/><stop offset="1" stop-color="#14265e"/></linearGradient></defs>' +
    '<path d="M10 20 v78 a56 16 0 0 0 112 0 v-78" fill="url(#dbg)" stroke="#6adfff" stroke-width="3"/><path d="M10 46 a56 16 0 0 0 112 0 M10 72 a56 16 0 0 0 112 0" fill="none" stroke="#6adfff" stroke-width="3" opacity=".8"/>' +
    '<ellipse cx="66" cy="20" rx="56" ry="16" fill="#3f78c8" stroke="#b8f1ff" stroke-width="3"/><circle cx="104" cy="58" r="4" fill="#01ccf7"/><circle cx="104" cy="84" r="4" fill="#01ccf7"/></svg>' +
    '<div style="position:absolute;left:-30px;top:122px;width:192px;text-align:center;font:700 18px/1 Poppins;letter-spacing:3px;color:rgba(220,236,255,.7)">DATABASE</div>';
  // ------------------------------------------------------------------ lines / beats
  const L = []; { let k = 0; for (const txt of LINES) { const n = txt.split(/\s+/).length; const ws = WORDS.slice(k, k + n).map((w) => [w[0], w[1] + OFF, w[2] + OFF]); k += n; L.push({ txt, ws, t0: ws[0][1] }); } }
  L.forEach((l, i) => { l.t1 = i < L.length - 1 ? L[i + 1].t0 : DUR + 5; });
  const NL = L.length;
  window.SFX_EVENTS = [];
  const fx = (t, n, db = 0, rate = 1) => window.SFX_EVENTS.push([+t.toFixed(3), n, db, rate]);
  // ------------------------------------------------------------------ headlines
  const EMPH = { 0: [4], 1: [1], 2: [1, 2], 3: [2], 4: [3, 4, 5], 5: [2], 6: [2, 4], 7: [5], 8: [1], 9: [4], 10: [0], 11: [3], 12: [1], 13: [1, 2], 14: [2], 15: [2], 16: [6], 17: [1, 2], 18: [4], 19: [7], 20: [1], 21: [2], 22: [3], 23: [7], 24: [1, 2], 25: [3, 4], 26: [1] };
  const DISP = { 1: { 1: ["24", 3] }, 21: { 2: ["N+1,", 3] } };   // number format only (the VO says "dua puluh empat" / "N plus satu")
  const HL = L.map((l, i) => {
    const d = E($("heads"), "", null, "hl"); const ws = [];
    for (let k = 0; k < l.ws.length; k++) {
      let txt = l.ws[k][0], skip = 0; const o = DISP[i] && DISP[i][k]; if (o) { txt = o[0]; skip = o[1] - 1; }
      const s = document.createElement("span"); s.className = "w" + ((EMPH[i] || []).includes(k) ? " em" : ""); s.textContent = txt;
      d.appendChild(s); d.appendChild(document.createTextNode(" ")); ws.push([s, l.ws[k][1]]); k += skip;
    }
    return { d, ws };
  });
  function heads(t) {
    HL.forEach((h, i) => {
      const l = L[i], last = i === NL - 1;
      const vis = t >= l.t0 - 0.2 && (last || t < l.t1 - 0.02);
      h.d.style.display = vis ? "block" : "none"; if (!vis) return;
      const q = last ? 0 : eio(lin(t, l.t1 - 0.26, l.t1 - 0.04));
      op(h.d, 1 - q); h.d.style.transform = `translateY(${(-22 * q).toFixed(1)}px)`; h.d.style.filter = q > 0.01 ? `blur(${(6 * q).toFixed(2)}px)` : "none";
      for (const [s, ws] of h.ws) { const p = e3(lin(t, ws - 0.1, ws + 0.2)); op(s, p); s.style.transform = `translateY(${(18 * (1 - p)).toFixed(1)}px)`; s.style.filter = p < 0.99 ? `blur(${(8 * (1 - p)).toFixed(2)}px)` : "none"; }
    });
  }
  // ------------------------------------------------------------------ cards
  const CX = 540, CY = 895;
  const TR = [["up", "rise"], ["grow", "pop"], ["left", "left"], ["flip", "flip"], ["right", "right"], ["up", "swing"], ["shrink", "zoom"], ["left", "tilt"], ["down", "drop"], ["shrink", "unfold"],
    ["right", "right"], ["up", "rise"], ["grow", "pop"], ["left", "left"], ["flip", "flip"], ["shrink", "zoom"], ["right", "swing"], ["down", "drop"], ["left", "left"], ["up", "rise"],
    ["shrink", "pop"], ["left", "left"], ["flip", "flip"], ["right", "right"], ["down", "tilt"], ["grow", "zoom"]];
  const ENTER = { rise: (q) => ({ y: 150 * q, s: 1 - 0.08 * q }), drop: (q) => ({ y: -170 * q, s: 1 - 0.06 * q }), left: (q) => ({ x: 380 * q, r: 5 * q }), right: (q) => ({ x: -380 * q, r: -5 * q }),
    zoom: (q) => ({ s: 1 - 0.42 * q }), pop: (q) => ({ s: 1 + 0.26 * q }), flip: (q) => ({ rx: 75 * q, y: 50 * q }), swing: (q) => ({ ry: -58 * q, x: 90 * q }),
    tilt: (q) => ({ r: -10 * q, s: 1 - 0.22 * q, y: 60 * q }), unfold: (q) => ({ sy: 1 - 0.92 * q }) };
  const EXIT = { up: (p) => ({ y: -120 * p, s: 1 - 0.05 * p }), left: (p) => ({ x: -400 * p, r: -4 * p }), right: (p) => ({ x: 400 * p, r: 4 * p }), shrink: (p) => ({ s: 1 - 0.38 * p }),
    grow: (p) => ({ s: 1 + 0.32 * p }), down: (p) => ({ y: 150 * p }), flip: (p) => ({ rx: -75 * p }) };
  const C = [];   // {root, W, H, cy, upd, tin, tout, en, ex}
  function addCard(i, W, H, build, cy = CY) {
    const root = E($("cards"), `left:${CX - W / 2}px;top:${cy - H / 2}px;width:${W}px;height:${H}px`, null, "card");
    const l = L[i], w = (k) => l.ws[k][1] - l.t0, cfx = (u, n, db = 0, r = 1) => fx(l.t0 + u, n, db, r);
    const upd = build(root, w, cfx, l.t1 - l.t0);
    const tin = i === 0 ? 0.05 : l.t0 - 0.24, tout = i < NL - 1 ? L[i + 1].t0 - 0.26 : DUR + 5;
    C[i] = { root, W, H, cy, upd, tin, tout, en: i === 0 ? "rise" : TR[i - 1][1], ex: i < NL - 1 ? TR[i][0] : "up" };
    if (i > 0) { fx(tout + 0.12, "whoosh", -1, [0.8, 1.1, 1.35, 0.95, 1.2][i % 5]); }
    fx(tin + 0.2, "pop", -6, 0.9 + 0.05 * (i % 4));
  }
  function cardState(c, t) {
    const pe = spr(t - c.tin, 2.0, 0.64), fade = e3(lin(t, c.tin, c.tin + 0.18)), px = eio(lin(t, c.tout, c.tout + 0.24));
    const a = ENTER[c.en](1 - pe), b = EXIT[c.ex](px);
    return { x: (a.x || 0) + (b.x || 0), y: (a.y || 0) + (b.y || 0), s: (a.s == null ? 1 : a.s) * (b.s == null ? 1 : b.s), sy: a.sy == null ? 1 : a.sy, r: (a.r || 0) + (b.r || 0), rx: (a.rx || 0) + (b.rx || 0), ry: (a.ry || 0) + (b.ry || 0), o: fade * (1 - px) };
  }
  function cards(t) {
    for (const c of C) {
      const vis = t >= c.tin - 0.01 && t < c.tout + 0.25;
      c.root.style.display = vis ? "block" : "none"; if (!vis) continue;
      const S = cardState(c, t), P = cardState(c, t - 1 / 30);
      const v = Math.hypot(S.x - P.x, S.y - P.y) + Math.abs(S.s - P.s) * c.W * 0.5 + Math.abs(S.r - P.r) * c.W * 0.009 + (Math.abs(S.rx - P.rx) + Math.abs(S.ry - P.ry)) * c.W * 0.006 + Math.abs(S.sy - P.sy) * c.H * 0.5;
      const bl = v > 6 ? Math.min(9, (v - 6) * 0.12) : 0;   // motion blur proportional to speed
      c.root.style.transform = `perspective(1300px) translate(${S.x.toFixed(1)}px,${S.y.toFixed(1)}px) rotateX(${S.rx.toFixed(2)}deg) rotateY(${S.ry.toFixed(2)}deg) rotate(${S.r.toFixed(2)}deg) scale(${S.s.toFixed(4)},${(S.s * S.sy).toFixed(4)})`;
      op(c.root, cl(S.o)); c.root.style.filter = bl > 0.2 ? `blur(${bl.toFixed(2)}px)` : "none";
      c.upd(t - L[C.indexOf(c)].t0);
    }
  }
  const TIPS = ["Skeleton loading", "Tampilan duluan", "Jawaban AI streaming", "Virtualisasi daftar", "Gambar WebP / AVIF", "Lazy-load gambar", "Pecah JavaScript", "Script pihak ketiga belakangan",
    "Buang library nganggur", "File lewat CDN", "Kompresi Gzip", "Cache browser", "Debounce pencarian", "Cegah request dobel", "Request paralel", "Batas waktu layanan luar",
    "Antrean di belakang layar", "Cache Redis", "Index database", "Benahi query N+1", "Ambil kolom perlu", "Pagination", "Connection pooling", "Tes HP murah & sinyal lemah"];

  // ============ 0 · HOOK A — the client's own Claude screen recording + the request + impatient customers
  addCard(0, 900, 530, (R, w, f) => {
    const p1 = E(R, "left:0;top:0;width:900px;height:300px", null, "pn");
    const rv = E(p1, "left:20px;top:20px;width:860px;height:260px;background:#181818", null, "rec");
    const H = [], K = [];
    for (let k = 1; k <= 24; k++) { const im = document.createElement("img"); im.src = `assets/rec/home/h_${String(k).padStart(3, "0")}.jpg`; im.style.cssText = "left:34px;top:0;width:791px;height:260px;display:none"; rv.appendChild(im); H.push(im); }
    const cw = E(rv, "position:absolute;left:0;top:0;width:860px;height:260px;background:#181818", null);
    for (let k = 1; k <= 60; k++) { const im = document.createElement("img"); im.src = `assets/rec/code/c_${String(k).padStart(3, "0")}.jpg`; im.style.cssText = "position:absolute;left:10px;top:30px;width:839px;height:196px;display:none"; cw.appendChild(im); K.push(im); }
    const mask = E(cw, "position:absolute;left:100px;top:72px;width:720px;height:66px;background:#303030;opacity:0", null);
    const ty = E(mask, "position:absolute;left:4px;top:8px;font:400 36px/48px Poppins;color:#f2f2f2;white-space:nowrap", "");
    const caret = E(mask, "position:absolute;top:12px;width:3px;height:42px;background:#f2f2f2", null);
    const chip = E(R, "left:604px;top:-26px", ico("sparkles", 22, "#b8f1ff") + "contoh prompt", "cp");
    const p2 = E(R, "left:0;top:320px;width:900px;height:210px", null, "pn");
    const sp = E(p2, "left:40px;top:55px;width:100px;height:100px", spinner(100), "ic");
    E(p2, "left:170px;top:56px", "Memuat aplikasi…", "tb");
    const tm = E(p2, "left:170px;top:104px;color:rgba(220,236,255,.7)", "", "tx");
    E(p2, "left:530px;top:36px", "pengguna", "lb");
    const AV = [0, 1, 2, 3, 4].map((k) => E(p2, `left:${530 + k * 70}px;top:78px;width:62px;height:62px;border-radius:50%;background:rgba(1,204,247,.16);border:2px solid rgba(1,204,247,.6)`, ico("user", 32, "#b8f1ff"), "ic"));
    const OUT = [[4, w(7)], [3, w(7) + 0.28], [2, w(8) + 0.05]];
    const TXT = "Claude, bikin aplikasiku ngebut", TA = 1.35, TB = 2.3;
    for (let k = 0; k < 9; k++) f(TA + k * 0.1 + 0.03, "key", -4, 1.1 + 0.07 * (k % 3));
    f(w(5) - 0.05, "pop", -3); OUT.forEach(([, a]) => f(a + 0.08, "click", -6, 0.8));
    return (u) => {
      const fh = Math.min(23, Math.max(0, Math.floor((u + 0.6) * 30)));
      H.forEach((im, k) => { im.style.display = k === fh ? "block" : "none"; });
      const sw = lin(u, 0.95, 1.2); op(cw, sw); cw.style.transform = `translateY(${(30 * (1 - e3(sw))).toFixed(1)}px)`;
      const fc = Math.min(59, Math.max(0, Math.floor((u - 0.95) * 30)));
      K.forEach((im, k) => { im.style.display = k === fc ? "block" : "none"; });
      op(mask, u >= TA - 0.05 ? 1 : 0);
      const n = Math.round(TXT.length * lin(u, TA, TB)); ty.textContent = TXT.slice(0, n);
      caret.style.left = 6 + ty.offsetWidth + "px"; op(caret, Math.floor(u * 3) % 2 || u < TB ? 1 : 0.15);
      pop(chip, u, 1.2);
      const q = spr(u - (w(5) - 0.15), 2.2, 0.6); op(p2, cl(q * 3)); p2.style.transform = `translateY(${(50 * (1 - q)).toFixed(1)}px)`;
      sp.style.transform = `rotate(${(u * 400) % 360}deg)`;
      tm.textContent = "menunggu " + Math.max(1, Math.floor(u - w(5) + 1.2)) + " detik";
      AV.forEach((a, k) => { const o = OUT.find((x) => x[0] === k); const p = o ? e3(lin(u, o[1], o[1] + 0.45)) : 0; tf(a, 120 * p, -10 * p, 1 - 0.2 * p); op(a, 1 - p); });
    };
  });
  // ============ 1 · HOOK B — spinning list of the 24 fixes, lands on #01 (shared element into card 2)
  addCard(1, 820, 520, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:520px", null, "pn");
    E(R, "left:40px;top:34px", "24 perbaikan · app ngebut", "lb");
    const vp = E(R, "position:absolute;left:24px;top:76px;width:772px;height:420px;overflow:hidden;border-radius:20px", null);
    const ls = E(vp, "position:absolute;left:0;top:0;width:772px", null);
    for (let r = 0; r < 50; r++) { const k = r % 24; const row = E(ls, `position:absolute;left:0;top:${r * 84}px;width:772px;height:84px`, null);
      E(row, "left:26px;top:22px;color:#01ccf7", String(k + 1).padStart(2, "0"), "tb"); E(row, "left:100px;top:22px", TIPS[k], "tb");
      E(row, "left:700px;top:22px", ico("circle-check", 36, "rgba(184,241,255,.55)"), "ic"); }
    const hi = E(vp, "position:absolute;left:8px;top:168px;width:756px;height:84px;border-radius:18px;border:3px solid #01ccf7;box-shadow:0 0 30px rgba(1,204,247,.45),inset 0 0 20px rgba(1,204,247,.15);opacity:0", null);
    const fadeT = E(vp, "position:absolute;left:0;top:0;width:772px;height:110px;background:linear-gradient(#1b2d66,rgba(27,45,102,0))", null);
    const fadeB = E(vp, "position:absolute;left:0;bottom:0;width:772px;height:110px;background:linear-gradient(rgba(16,28,72,0),#111d4b)", null);
    const pos = (u) => mix(46, 24, e4(lin(u, -0.25, 1.45)));
    { let last = Math.floor(pos(-0.25)), lt = -9; for (let u = -0.25; u < 1.45; u += 0.01) { const p = Math.floor(pos(u)); if (p !== last && u - lt > 0.07) { f(u, "click", -9, 1.6); lt = u; } last = p; } }
    f(1.5, "ping", -6);
    return (u) => {
      const p = pos(u), v = Math.abs(p - pos(u - 1 / 30)) * 84;
      ls.style.transform = `translateY(${(-(p - 2) * 84).toFixed(1)}px)`; ls.style.filter = v > 4 ? `blur(${Math.min(7, v * 0.06).toFixed(2)}px)` : "none";
      const h = spr(u - 1.45, 2.6, 0.5); op(hi, cl(h * 2)); hi.style.transform = `scale(${(0.9 + 0.1 * h).toFixed(3)})`;
    };
  });
  // ============ 2 · skeleton loading
  addCard(2, 800, 500, (R, w, f) => {
    E(R, "left:0;top:0;width:800px;height:500px", null, "pn");
    [28, 50, 72].forEach((x) => E(R, `position:absolute;left:${x}px;top:28px;width:13px;height:13px;border-radius:50%;background:rgba(255,255,255,.28)`, null));
    E(R, "left:104px;top:22px", "contoh app · katalog", "lb");
    const chip = E(R, "left:560px;top:12px", "skeleton", "cp");
    const blocks = [[40, 76, 300, 230, 22], [370, 92, 300, 30, 10], [370, 146, 380, 20, 10], [370, 182, 340, 20, 10], [370, 218, 260, 20, 10], [370, 262, 180, 46, 23], [40, 336, 226, 124, 18], [286, 336, 226, 124, 18], [532, 336, 226, 124, 18]];
    const SK = blocks.map(([x, y, W, H, r]) => { const b = E(R, `position:absolute;left:${x}px;top:${y}px;width:${W}px;height:${H}px;border-radius:${r}px;overflow:hidden;background:rgba(255,255,255,.10)`, null);
      const sh = E(b, `position:absolute;left:0;top:0;width:${W}px;height:${H}px;background:linear-gradient(100deg,rgba(255,255,255,0) 30%,rgba(184,241,255,.22) 50%,rgba(255,255,255,0) 70%);background-size:${W * 3}px ${H}px`, null); return [b, sh, W]; });
    const real = [E(R, "position:absolute;left:40px;top:76px;width:300px;height:230px;border-radius:22px;overflow:hidden", picture(300, 230)),
      E(R, "left:370px;top:84px;font-size:34px", "Kaos Basic", "tb"), E(R, "left:370px;top:140px;color:rgba(220,236,255,.8)", "Bahan katun, adem", "tx"),
      E(R, "left:370px;top:176px;color:rgba(220,236,255,.8)", "Ukuran S sampai XL", "tx"), E(R, "left:370px;top:212px;color:rgba(220,236,255,.8)", "Siap kirim hari ini", "tx"),
      E(R, "left:370px;top:262px", ico("shopping-cart", 22, "#0a0d2c") + "Beli", "cp on")];
    ["Topi", "Tas", "Kemeja"].forEach((n, k) => { const t = E(R, `position:absolute;left:${40 + k * 246}px;top:336px;width:226px;height:124px;border-radius:18px;overflow:hidden`, picture(226, 124));
      E(t, "left:14px;top:80px;font-size:22px;text-shadow:0 2px 8px rgba(0,0,0,.6)", n, "tb"); real.push(t); });
    const RV = 2.05; f(RV + 0.05, "sparkle", -6); f(RV + 0.3, "pop", -5, 1.2);
    return (u) => {
      SK.forEach(([b, sh, W], k) => { sh.style.backgroundPosition = `${(((u * 1.3 + k * 0.07) % 1) * 3 * W - 2 * W).toFixed(0)}px 0`; op(b, 1 - e3(lin(u, RV + k * 0.04, RV + 0.3 + k * 0.04))); });
      real.forEach((e, k) => { const p = e3(lin(u, RV + 0.05 + k * 0.035, RV + 0.4 + k * 0.035)); op(e, p); e.style.filter = p < 0.99 ? `blur(${(6 * (1 - p)).toFixed(1)}px)` : "none"; });
      chip.textContent = u < RV + 0.2 ? "skeleton" : "data masuk ✓"; chip.className = "cp" + (u >= RV + 0.2 ? " on" : "");
      tf(chip, 0, 0, 1 + 0.12 * bump(u, RV + 0.2, 0.3));
    };
  });
  // ============ 3 · optimistic UI
  addCard(3, 820, 500, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:500px", null, "pn");
    E(R, "left:36px;top:34px;width:64px;height:64px;border-radius:50%;background:rgba(1,204,247,.18);border:2px solid rgba(1,204,247,.6)", ico("user", 32, "#b8f1ff"), "ic");
    E(R, "left:122px;top:36px", "Postingan baru", "tb"); E(R, "left:122px;top:74px;font-size:22px;color:rgba(220,236,255,.6)", "barusan", "tx");
    E(R, "position:absolute;left:36px;top:120px;width:748px;height:150px;border-radius:20px;overflow:hidden", picture(748, 150));
    const hb = E(R, "left:36px;top:292px;width:66px;height:66px;border-radius:50%;background:rgba(255,255,255,.08);border:2px solid rgba(184,241,255,.4)", ico("heart", 34, "#ffffff"), "ic");
    const hf = E(R, "left:36px;top:292px;width:66px;height:66px;border-radius:50%;background:#01ccf7;opacity:0", ico("heart", 34, "#0a0d2c", 2.4), "ic");
    hf.querySelector("svg path").setAttribute("fill", "#0a0d2c");
    const lk = E(R, "left:120px;top:306px", "Suka", "tx");
    E(R, "left:36px;top:394px", "tampilan", "lb"); E(R, "left:36px;top:448px", "server", "lb");
    E(R, "left:220px;top:392px;width:470px;height:18px", null, "bar"); E(R, "left:220px;top:446px;width:470px;height:18px", null, "bar");
    const b1 = E(R, "left:220px;top:392px;width:470px;height:18px;transform-origin:0 50%", null, "bar acc"), b2 = E(R, "left:220px;top:446px;width:470px;height:18px;transform-origin:0 50%", null, "bar acc");
    const k1 = E(R, "left:712px;top:382px", ico("circle-check", 38, "#01ccf7"), "ic"), k2 = E(R, "left:712px;top:436px", ico("circle-check", 38, "#01ccf7"), "ic");
    const cur = cursor(R), rp = ripple(R);
    const CK = 0.62, SV = w(5) + 0.05;
    f(CK, "click", -2); f(CK + 0.04, "pop", -4, 1.3); f(SV, "ping", -6);
    return (u) => {
      curSet(cur, u, [[0, 640, 470], [0.45, 70, 326], [1.2, 70, 326], [1.8, 520, 250]], [CK]);
      ripSet(rp, u, CK, 69, 325);
      const on = u >= CK; op(hf, on ? 1 : 0); tf(hf, 0, 0, on ? 1 + 0.25 * bump(u, CK, 0.3) : 1); lk.textContent = on ? "Disukai" : "Suka";
      b1.style.transform = `scaleX(${e3(lin(u, CK, CK + 0.18)).toFixed(3)})`; op(k1, u >= CK + 0.18 ? 1 : 0); tf(k1, 0, 0, 1 + 0.3 * bump(u, CK + 0.18, 0.3));
      const sp = lin(u, CK + 0.1, SV); b2.style.transform = `scaleX(${(sp * 0.92 + 0.08 * (sp >= 1)).toFixed(3)})`; b2.style.opacity = 0.55 + 0.45 * (sp >= 1);
      op(k2, u >= SV ? 1 : 0); tf(k2, 0, 0, 1 + 0.3 * bump(u, SV, 0.3));
    };
  });
  // ============ 4 · streaming AI answer
  addCard(4, 820, 540, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:540px", null, "pn");
    E(R, "left:36px;top:34px", "chat ai", "lb"); const chip = E(R, "left:610px;top:22px", ico("zap", 20, "#b8f1ff") + "streaming", "cp");
    const ub = E(R, "position:absolute;left:330px;top:82px;width:454px;height:66px;border-radius:22px 22px 6px 22px;background:rgba(1,204,247,.16);border:1.5px solid rgba(1,204,247,.5);display:flex;align-items:center;justify-content:center;font:400 26px/1 Poppins;white-space:nowrap", "Ringkas penjualan minggu ini");
    E(R, "left:36px;top:180px;width:58px;height:58px;border-radius:50%;background:#01ccf7", ico("bot", 32, "#0a0d2c"), "ic");
    E(R, "left:110px;top:176px;width:674px;height:320px", null, "pn2");
    const tx = E(R, "position:absolute;left:136px;top:196px;width:624px;font:400 29px/1.5 Poppins;color:#fff", null);
    const WS = "Penjualan paling ramai di hari Jumat. Stok kaos hitam hampir habis. Ada pesanan yang perlu dikirim ulang.".split(" ");
    const SP = WS.map((x) => { const s = document.createElement("span"); s.textContent = x + " "; tx.appendChild(s); return s; });
    const caret = document.createElement("span"); caret.style.cssText = "display:inline-block;width:14px;height:30px;background:#01ccf7;vertical-align:-4px;border-radius:3px"; tx.appendChild(caret);
    const T0 = 0.55, DT = 0.15;
    WS.forEach((_, k) => { if (k % 2 === 0) f(T0 + k * DT, "key", -7, 1.2 + 0.1 * (k % 3)); });
    return (u) => {
      pop(ub, u, 0.05);
      const n = Math.floor((u - T0) / DT) + 1;
      SP.forEach((s, k) => { const p = lin(u, T0 + k * DT, T0 + k * DT + 0.12); s.style.opacity = p.toFixed(2); s.style.display = k < Math.max(0, n) ? "inline" : "none"; });
      op(caret, u > 0.4 ? (Math.floor(u * 4) % 2 ? 1 : 0.35) : 0);
      tf(chip, 0, 0, 1 + 0.1 * bump(u, w(3), 0.3));
    };
  });
  // ============ 5 · virtualised long list
  addCard(5, 820, 540, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:540px", null, "pn");
    const clip = E(R, "position:absolute;left:30px;top:24px;width:440px;height:492px;overflow:hidden", null);
    const frame = E(R, "position:absolute;left:30px;top:126px;width:440px;height:288px;border-radius:18px;border:3px solid #01ccf7;box-shadow:0 0 26px rgba(1,204,247,.35)", null);
    const RH = 58, N = 26, rows = [];
    for (let k = 0; k < N; k++) { const r = E(clip, `position:absolute;left:12px;top:0;width:416px;height:${RH - 10}px;border-radius:12px`, null);
      const t = E(r, "left:20px;top:7px;font-size:23px", "Pesanan " + (1041 + k), "tx"); rows.push([r, t]); }
    E(R, "left:510px;top:120px", "yang kelihatan", "lb");
    E(R, "left:510px;top:154px;width:56px;height:36px;border-radius:10px;background:rgba(1,204,247,.25);border:2px solid #01ccf7", null);
    E(R, "left:584px;top:156px", "digambar", "tb");
    E(R, "left:510px;top:250px", "di luar layar", "lb");
    E(R, "left:510px;top:284px;width:56px;height:36px;border-radius:10px;border:2px dashed rgba(184,241,255,.45)", null);
    E(R, "left:584px;top:286px", "dilewati", "tb");
    const cnt = E(R, "left:510px;top:380px", ico("layers", 22, "#b8f1ff") + "5 baris di layar", "cp");
    f(w(5) + 0.05, "pop", -5);
    return (u) => {
      const sc = 60 + u * 95;
      rows.forEach(([r, t], k) => { const y = k * RH - sc + 102 - 24 + 24; const yy = ((y % (N * RH)) + N * RH) % (N * RH) - 2 * RH;
        r.style.transform = `translateY(${yy.toFixed(1)}px)`;
        const top = yy + 24, inF = cl(Math.min((top - 126 + RH * 0.6) / (RH * 0.6), (126 + 288 - (top + RH - 10) + RH * 0.6) / (RH * 0.6)));
        r.style.background = `rgba(30,58,128,${(0.85 * inF).toFixed(2)})`; r.style.border = inF > 0.5 ? "1.5px solid rgba(150,210,255,.3)" : "2px dashed rgba(184,241,255,.32)"; op(t, cl((inF - 0.9) / 0.1)); });
      pop(cnt, u, w(5) - 0.1);
    };
  });
  // ============ 6 · WebP / AVIF
  addCard(6, 820, 500, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:500px", null, "pn");
    E(R, "left:40px;top:34px", "foto produk", "lb");
    const pic = E(R, "position:absolute;left:40px;top:72px;width:300px;height:300px;border-radius:24px;overflow:hidden;box-shadow:0 18px 40px rgba(0,0,0,.4)", picture(300, 300));
    E(R, "left:388px;top:34px", "ukuran file", "lb");
    const rows = [["JPG", 1, 0.15], ["WebP", 0.55, w(2)], ["AVIF", 0.55, w(4)]].map(([n, len, a], k) => {
      const y = 80 + k * 100; const ch = E(R, `left:388px;top:${y}px;min-width:110px;justify-content:center`, n, "cp" + (k ? " on" : ""));
      E(R, `left:520px;top:${y + 12}px;width:260px;height:22px`, null, "bar");
      const b = E(R, `left:520px;top:${y + 12}px;width:${260 * len}px;height:22px;transform-origin:0 50%`, null, "bar" + (k ? " acc" : ""));
      if (!k) b.style.background = "rgba(255,255,255,.45)";
      f(a + 0.05, "pop", -4, 1 + 0.15 * k); return [ch, b, a]; });
    const ok = E(R, "left:388px;top:396px", ico("circle-check", 24, "#0a0d2c") + "file lebih kecil", "cp on");
    f(w(5) + 0.05, "ping", -7);
    return (u) => {
      rows.forEach(([ch, b, a]) => { pop(ch, u, a - 0.1); b.style.transform = `scaleX(${spr(u - a, 2.4, 0.7).toFixed(3)})`; });
      pop(ok, u, w(5)); tf(pic, 0, 0, 1 - 0.04 * e3(lin(u, w(2), w(2) + 0.4)));
    };
  });
  // ============ 7 · lazy-load below the fold
  addCard(7, 800, 560, (R, w, f) => {
    const ph = E(R, "position:absolute;left:50px;top:6px;width:290px;height:410px;border-radius:44px;border:3px solid rgba(184,241,255,.45);background:#0b1440;box-shadow:0 26px 50px rgba(0,0,0,.45)", null);
    const ghost = E(R, "position:absolute;left:66px;top:22px;width:258px;height:540px;overflow:hidden", null);
    const scr = E(ph, "position:absolute;left:13px;top:13px;width:258px;height:378px;border-radius:32px;overflow:hidden;background:#101c4a", null);
    const G = [], RL = [];
    for (let k = 0; k < 5; k++) { const y = 20 + k * 200;
      G.push(E(ghost, `position:absolute;left:16px;top:${y}px;width:226px;height:150px;border-radius:16px;border:2px dashed rgba(184,241,255,.4)`, null));
      const r = E(scr, `position:absolute;left:16px;top:${y}px;width:226px;height:150px;border-radius:16px;overflow:hidden;background:rgba(255,255,255,.08)`, null);
      const im = E(r, "position:absolute;left:0;top:0", picture(226, 150)); const sp = E(r, "left:83px;top:45px;width:60px;height:60px", spinner(60), "ic");
      E(scr, `position:absolute;left:16px;top:${y + 160}px;width:180px;height:14px;border-radius:7px;background:rgba(255,255,255,.14)`, null);
      RL.push([r, im, sp, y]); }
    const fold = E(R, "position:absolute;left:340px;top:414px;width:440px;height:0;border-top:3px dashed rgba(1,204,247,.8)", null);
    E(R, "left:420px;top:428px;color:#b8f1ff", "batas layar", "lb");
    E(R, "left:420px;top:80px", "di layar", "lb"); const c1 = E(R, "left:420px;top:112px", ico("image", 22, "#0a0d2c") + "dimuat", "cp on");
    E(R, "left:420px;top:250px", "di bawah layar", "lb"); const c2 = E(R, "left:420px;top:282px", ico("clock", 22, "#b8f1ff") + "nanti saja", "cp");
    const sc = (u) => 340 * eio(lin(u, 0.35, 2.1));
    const loadAt = RL.map(([, , , y]) => { for (let u = -0.3; u < 3; u += 0.01) if (y - sc(u) + 60 < 378) return Math.max(0, u); return 9; });
    loadAt.forEach((a) => { if (a > 0.1 && a < 2.4) f(a + 0.25, "pop", -7, 1.3); });
    return (u) => {
      const s = sc(u); G.forEach((g, k) => { g.style.transform = `translateY(${(-s).toFixed(1)}px)`; });
      RL.forEach(([r, im, sp, y], k) => { r.style.transform = `translateY(${(-s).toFixed(1)}px)`; const p = e3(lin(u, loadAt[k] + 0.05, loadAt[k] + 0.35)); op(im, p); op(sp, 1 - p); sp.style.transform = `rotate(${(u * 420) % 360}deg)`; });
      pop(c1, u, 0.3); pop(c2, u, w(5) - 0.1); op(fold, e3(lin(u, 0.1, 0.4)));
      // text bars scroll with the content
      for (const e of scr.children) if (!RL.some((x) => x[0] === e)) e.style.transform = `translateY(${(-s).toFixed(1)}px)`;
    };
  }, 880);
  // ============ 8 · code splitting
  addCard(8, 820, 480, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:480px", null, "pn");
    E(R, "left:40px;top:34px", "javascript aplikasi", "lb");
    const big = E(R, "left:110px;top:110px;width:600px;height:130px;border-radius:24px;border:2.5px solid rgba(1,204,247,.75);background:rgba(1,204,247,.10)", null, "ic");
    big.innerHTML = `<div style="display:flex;align-items:center;gap:18px">${ico("file-code", 44, "#b8f1ff")}<span style="font:700 34px/1 Poppins">semua-halaman.js</span></div>`;
    const NM = ["beranda.js", "produk.js", "keranjang.js", "akun.js"], POS = [[40, 90], [430, 90], [40, 230], [430, 230]];
    const TL = NM.map((n, k) => { const e = E(R, `left:${POS[k][0]}px;top:${POS[k][1]}px;width:350px;height:116px;border-radius:22px;border:2px solid rgba(150,210,255,.3);background:rgba(10,20,58,.75)`, null, "ic");
      e.innerHTML = `<div style="display:flex;align-items:center;gap:14px">${ico("file-code", 34, k ? "#b8f1ff" : "#0a0d2c")}<span style="font:700 28px/1 Poppins;color:${k ? "#fff" : "#0a0d2c"}">${n}</span></div>`; return e; });
    const tags = [1, 2, 3].map((k) => E(R, `left:${POS[k][0] + 262}px;top:${POS[k][1] + 90}px;font:700 16px/1 Poppins;letter-spacing:2px;color:rgba(220,236,255,.55)`, "NANTI", "lb"));
    const note = E(R, "left:40px;top:400px;font-size:25px;color:rgba(220,236,255,.85)", "Buka beranda → cuma beranda.js yang dimuat", "tx");
    const SPL = w(1) + 0.05, LD = w(5);
    f(SPL, "whoosh", -6, 1.6); [0, 1, 2, 3].forEach((k) => f(SPL + 0.1 + k * 0.05, "pop", -8, 1 + 0.1 * k)); f(LD + 0.05, "ping", -6);
    return (u) => {
      const s = spr(u - SPL, 2.3, 0.62); op(big, 1 - cl(s * 3)); tf(big, 0, 0, 1 + 0.1 * cl(s));
      TL.forEach((e, k) => { const cx = POS[k][0] + 175, cy = POS[k][1] + 58; tf(e, (410 - cx) * (1 - s), (175 - cy) * (1 - s), 0.6 + 0.4 * s); op(e, cl(s * 3) * (k && u > LD ? 1 - 0.55 * e3(lin(u, LD, LD + 0.3)) : 1));
        if (!k) { const on = e3(lin(u, LD, LD + 0.25)); e.style.background = `rgba(1,204,247,${(0.1 + 0.9 * on).toFixed(2)})`; e.style.borderColor = on > 0.5 ? "#01ccf7" : "rgba(150,210,255,.3)"; e.style.boxShadow = `0 0 ${(30 * on).toFixed(0)}px rgba(1,204,247,.5)`;
          e.querySelector("span").style.color = on > 0.5 ? "#0a0d2c" : "#fff"; e.querySelector("svg").setAttribute("stroke", on > 0.5 ? "#0a0d2c" : "#b8f1ff"); } });
      tags.forEach((g) => op(g, e3(lin(u, LD, LD + 0.3)))); op(note, e3(lin(u, LD + 0.1, LD + 0.4)));
    };
  });
  // ============ 9 · third-party scripts after the page is ready
  addCard(9, 820, 500, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:500px", null, "pn");
    const br = E(R, "left:36px;top:30px;width:748px;height:250px", null, "pn2");
    const PB = [[24, 22, 700, 30], [24, 70, 420, 80], [460, 70, 264, 80], [24, 166, 220, 64], [258, 166, 220, 64], [492, 166, 232, 64]].map(([x, y, W, H], k) => E(br, `position:absolute;left:${x}px;top:${y}px;width:${W}px;height:${H}px;border-radius:12px;background:${k === 1 ? "rgba(1,204,247,.35)" : "rgba(255,255,255,.16)"}`, null));
    const wid = E(br, "left:640px;top:168px;width:62px;height:62px;border-radius:50%;background:#01ccf7", ico("message-circle", 30, "#0a0d2c"), "ic");
    E(R, "left:36px;top:308px", "urutan muat", "lb");
    E(R, "left:36px;top:350px;width:748px;height:20px", null, "bar");
    const hb = E(R, "left:36px;top:350px;width:380px;height:20px;transform-origin:0 50%", null, "bar acc");
    const ok = E(R, "left:36px;top:394px", ico("circle-check", 22, "#0a0d2c") + "halaman siap", "cp on");
    const mk = E(R, "position:absolute;left:418px;top:336px;width:4px;height:48px;border-radius:2px;background:#ffffff", null);
    const CH = [["chat", 440, w(4) + 0.1], ["analitik", 560, w(4) + 0.35], ["iklan", 704, w(4) + 0.6]].map(([n, x, a]) => [E(R, `left:${x}px;top:396px;padding:9px 16px 10px`, n, "cp"), a]);
    const RD = 1.25; f(RD + 0.05, "ping", -7); CH.forEach(([, a]) => f(a + 0.05, "pop", -6, 1.2));
    return (u) => {
      PB.forEach((b, k) => op(b, e3(lin(u, 0.1 + k * 0.17, 0.3 + k * 0.17))));
      hb.style.transform = `scaleX(${e3(lin(u, 0.1, RD)).toFixed(3)})`; pop(ok, u, RD); op(mk, u >= RD ? 1 : 0);
      CH.forEach(([e, a]) => pop(e, u, a)); pop(wid, u, CH[0][1] + 0.1);
    };
  });
  // ============ 10 · remove unused libraries
  addCard(10, 780, 440, (R, w, f) => {
    E(R, "left:0;top:0;width:780px;height:440px", null, "pn");
    E(R, "left:36px;top:32px", "library terpasang", "lb");
    const NM = ["grafik", "tanggal", "ikon", "editor", "slider", "peta"], kill = [3, 4, 5];
    const CP = NM.map((n, k) => { const x = 36 + (k % 3) * 240, y = 78 + Math.floor(k / 3) * 96;
      const e = E(R, `left:${x}px;top:${y}px;width:218px;height:74px;border-radius:18px;background:rgba(10,20,58,.75);border:2px solid rgba(150,210,255,.3);gap:12px;display:flex;align-items:center;justify-content:center`, `${ico("package", 28, "#b8f1ff")}<span style="font:700 26px/1 Poppins">${n}</span>`, "ic");
      const st = E(e, "position:absolute;left:20px;top:35px;width:178px;height:4px;border-radius:2px;background:#01ccf7;transform-origin:0 50%;transform:scaleX(0)", null); return [e, st]; });
    E(R, "left:36px;top:296px", "ukuran unduhan", "lb");
    E(R, "left:36px;top:336px;width:708px;height:26px", null, "bar");
    const sz = E(R, "left:36px;top:336px;width:708px;height:26px;transform-origin:0 50%", null, "bar acc");
    const T = [0.22, 0.42, 0.62]; T.forEach((a) => { f(a, "click", -4, 1.2); f(a + 0.18, "whoosh", -9, 1.8); });
    return (u) => {
      kill.forEach((k, j) => { const [e, st] = CP[k], a = T[j]; st.style.transform = `scaleX(${e3(lin(u, a, a + 0.15)).toFixed(3)})`; const p = e3(lin(u, a + 0.18, a + 0.5)); tf(e, 260 * p, -30 * p, 1 - 0.2 * p, 12 * p); op(e, 1 - p); });
      const gone = T.reduce((s, a) => s + e3(lin(u, a + 0.18, a + 0.5)), 0); sz.style.transform = `scaleX(${(1 - 0.13 * gone).toFixed(3)})`;
    };
  });
  // ============ 11 · CDN (nearest location)
  addCard(11, 840, 540, (R, w, f) => {
    E(R, "left:0;top:0;width:840px;height:540px", null, "pn");
    const U = [420, 400], O = [110, 110], NOD = [[640, 140], [200, 330], [560, 330], [330, 150]], NEAR = 2;
    const lo = seg(R, "dash"), ln = seg(R); ln.style.background = "#01ccf7"; ln.style.boxShadow = "0 0 14px #01ccf7"; ln.style.height = "6px";
    E(R, `left:${O[0] - 50}px;top:${O[1] - 50}px;width:100px;height:100px`, ico("server", 44, "#b8f1ff"), "node"); E(R, `left:${O[0] - 50}px;top:${O[1] + 62}px`, "server asal", "lb");
    const ND = NOD.map(([x, y], k) => E(R, `left:${x - 38}px;top:${y - 38}px;width:76px;height:76px;border-radius:20px;${k === NEAR ? "border-color:#01ccf7;box-shadow:0 0 24px rgba(1,204,247,.5)" : ""}`, ico("globe", 34, k === NEAR ? "#01ccf7" : "#b8f1ff"), "node"));
    const nl = E(R, `left:${NOD[NEAR][0] + 50}px;top:${NOD[NEAR][1] - 14}px;color:#b8f1ff`, "cdn terdekat", "lb");
    E(R, `left:${U[0] - 42}px;top:${U[1] - 42}px;width:84px;height:84px;border-radius:50%;background:#01ccf7;box-shadow:0 0 30px rgba(1,204,247,.6)`, ico("map-pin", 40, "#0a0d2c", 2.4), "ic");
    E(R, `left:${U[0] - 26}px;top:${U[1] + 54}px`, "kamu", "lb");
    const pk = E(R, "", null, "pk");
    NOD.forEach((_, k) => f(w(3) + 0.05 + k * 0.1, "pop", -8, 1 + 0.1 * k)); f(w(4) + 0.05, "whoosh", -8, 1.7);
    return (u) => {
      segSet(lo, U[0], U[1], O[0], O[1], e3(lin(u, 0.05, 0.6)), u > w(4) ? 0.35 : 0.9);
      ND.forEach((e, k) => pop(e, u, w(3) - 0.1 + k * 0.1)); pop(nl, u, w(4));
      const N = NOD[NEAR]; segSet(ln, U[0], U[1], N[0], N[1], e3(lin(u, w(4) - 0.05, w(4) + 0.2)), u > w(4) - 0.05 ? 1 : 0);
      const cyc = (u - w(4) - 0.2) / 0.55; const pp = cyc - Math.floor(cyc); pkSet(pk, N[0], N[1], U[0], U[1], e3(pp), u > w(4) + 0.2 ? 1 : 0);
    };
  });
  // ============ 12 · gzip compression
  addCard(12, 820, 480, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:480px", null, "pn");
    E(R, "left:40px;top:34px", "kiriman ke browser", "lb");
    const blk = E(R, "left:40px;top:92px;width:520px;height:120px;border-radius:22px;background:rgba(1,204,247,.14);border:2.5px solid rgba(1,204,247,.7);transform-origin:0 50%", null, "ic");
    const bl = E(blk, "display:flex;align-items:center;gap:14px;white-space:nowrap", `${ico("file", 40, "#b8f1ff")}<span style="font:700 30px/1 Poppins">data.json</span>`);
    const jl = E(R, "position:absolute;left:30px;top:84px;width:10px;height:136px;border-radius:5px;background:#ffffff", null), jr = E(R, "position:absolute;left:570px;top:84px;width:10px;height:136px;border-radius:5px;background:#ffffff", null);
    const zt = E(R, "left:40px;top:232px", ico("archive", 22, "#0a0d2c") + "gzip", "cp on");
    E(R, "left:650px;top:92px;width:130px;height:120px", ico("monitor", 52, "#b8f1ff"), "node"); E(R, "left:660px;top:226px", "browser", "lb");
    E(R, "left:40px;top:318px", "sebelum", "lb"); E(R, "left:40px;top:398px", "sesudah", "lb");
    E(R, "left:200px;top:314px;width:580px;height:26px;background:rgba(255,255,255,.4)", null, "bar");
    const b2 = E(R, "left:200px;top:394px;width:580px;height:26px;transform-origin:0 50%", null, "bar acc");
    const Z = w(2) - 0.05; f(Z + 0.1, "click", -3, 0.8); f(Z + 0.35, "pop", -5, 0.9); f(Z + 0.8, "whoosh", -8, 1.6);
    return (u) => {
      const s = spr(u - Z, 2.0, 0.6); const W = mix(1, 0.5, s); tf(blk, 0, 0, 1); blk.style.transform = `scaleX(${W.toFixed(3)})`; bl.style.transform = `scaleX(${(1 / W).toFixed(3)})`;
      const jx = 520 * W; jr.style.transform = `translateX(${(jx - 520).toFixed(1)}px)`; op(jl, cl(lin(u, Z - 0.2, Z)) * (1 - lin(u, Z + 0.6, Z + 0.8))); op(jr, cl(lin(u, Z - 0.2, Z)) * (1 - lin(u, Z + 0.6, Z + 0.8)));
      const mv = e3(lin(u, Z + 0.75, Z + 1.3)); blk.style.transform += ` translateX(${(mv * 470 / W).toFixed(1)}px)`; op(blk, 1 - lin(u, Z + 1.05, Z + 1.3)); op(bl, 1 - lin(u, Z + 0.72, Z + 0.86));
      pop(zt, u, Z + 0.3); b2.style.transform = `scaleX(${(0.5 * spr(u - Z - 0.4, 2.4, 0.7)).toFixed(3)})`;
    };
  });
  // ============ 13 · browser cache
  addCard(13, 820, 500, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:500px", null, "pn");
    E(R, "left:40px;top:34px", "kunjungan pertama", "lb"); E(R, "left:40px;top:262px", "kunjungan berikutnya", "lb");
    E(R, "left:40px;top:72px;width:96px;height:96px", ico("monitor", 42, "#b8f1ff"), "node"); E(R, "left:684px;top:72px;width:96px;height:96px", ico("cloud", 42, "#b8f1ff"), "node");
    E(R, "left:160px;top:110px;width:500px;height:18px", null, "bar"); const p1 = E(R, "left:160px;top:110px;width:500px;height:18px;transform-origin:100% 50%", null, "bar acc");
    E(R, "left:160px;top:140px;font-size:22px;color:rgba(220,236,255,.7)", "unduh dari server", "tx");
    E(R, "left:40px;top:300px;width:96px;height:96px", ico("monitor", 42, "#b8f1ff"), "node");
    const hd = E(R, "left:160px;top:300px;width:96px;height:96px;border-color:#01ccf7;box-shadow:0 0 24px rgba(1,204,247,.45)", ico("hard-drive", 42, "#01ccf7"), "node");
    E(R, "left:168px;top:408px", "cache", "lb");
    const c2 = E(R, "left:684px;top:300px;width:96px;height:96px;opacity:.3", ico("cloud", 42, "#b8f1ff"), "node");
    const ok = E(R, "left:286px;top:322px", ico("zap", 22, "#0a0d2c") + "langsung dari cache", "cp on");
    const no = E(R, "left:286px;top:400px", ico("circle-x", 22, "#b8f1ff") + "nggak unduh ulang", "cp");
    const K2 = w(3) + 0.1; f(K2 + 0.05, "pop", -4); f(w(6), "ping", -7);
    return (u) => {
      p1.style.transform = `scaleX(${e3(lin(u, 0.15, 1.0)).toFixed(3)})`;
      pop(hd, u, K2 - 0.15); pop(ok, u, K2); pop(no, u, w(6) - 0.15);
    };
  });
  // ============ 14 · debounce search
  addCard(14, 820, 500, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:500px", null, "pn");
    E(R, "left:36px;top:36px;width:748px;height:88px;border-radius:44px", null, "pn2");
    E(R, "left:62px;top:60px", ico("search", 38, "#b8f1ff"), "ic");
    const q = E(R, "left:120px;top:58px;font-size:32px", "", "tx"); const caret = E(R, "position:absolute;top:60px;width:3px;height:42px;background:#01ccf7", null);
    const ring = E(R, "left:712px;top:56px;width:48px;height:48px", '<svg width="48" height="48" viewBox="0 0 48 48"><circle cx="24" cy="24" r="18" fill="none" stroke="rgba(184,241,255,.2)" stroke-width="5"/><circle class="rg" cx="24" cy="24" r="18" fill="none" stroke="#01ccf7" stroke-width="5" stroke-linecap="round" stroke-dasharray="113" stroke-dashoffset="113" transform="rotate(-90 24 24)"/></svg>', "ic");
    E(R, "left:36px;top:168px", "ketikan", "lb"); E(R, "left:36px;top:300px", "request ke server", "lb");
    const S = "sepatu lari", TA = 0.15, DT = 0.12, TE = TA + S.length * DT, RQ = Math.max(TE + 0.45, w(4) + 0.05);
    const TK = S.split("").map((_, k) => E(R, `position:absolute;left:${40 + k * 30}px;top:204px;width:10px;height:40px;border-radius:5px;background:rgba(184,241,255,.55)`, null));
    const dot = E(R, "position:absolute;left:40px;top:338px;width:40px;height:40px;border-radius:50%;background:#01ccf7;box-shadow:0 0 22px #01ccf7", null);
    const one = E(R, "left:100px;top:334px", "cukup 1 request", "cp on");
    const res = E(R, "left:36px;top:412px", ico("list", 22, "#b8f1ff") + "hasil pencarian muncul", "cp");
    S.split("").forEach((_, k) => f(TA + k * DT + 0.02, "key", -5, 1.1 + 0.08 * (k % 3))); f(RQ, "pop", -2); f(RQ + 0.45, "ping", -8);
    return (u) => {
      const n = Math.max(0, Math.min(S.length, Math.floor((u - TA) / DT) + 1)); q.textContent = S.slice(0, n);
      caret.style.left = 124 + q.offsetWidth + "px"; op(caret, Math.floor(u * 3) % 2 || u < TE ? 1 : 0.2);
      TK.forEach((e, k) => { const p = spr(u - (TA + k * DT), 3, 0.5); op(e, cl(p * 3)); e.style.transform = `scaleY(${p.toFixed(3)})`; });
      ring.querySelector(".rg").setAttribute("stroke-dashoffset", (113 * (1 - lin(u, TE, RQ))).toFixed(1)); op(ring, u > TE - 0.05 && u < RQ + 0.3 ? 1 : 0);
      pop(dot, u, RQ); pop(one, u, RQ + 0.05); pop(res, u, RQ + 0.45);
    };
  });
  // ============ 15 · block duplicate requests
  addCard(15, 820, 500, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:500px", null, "pn");
    E(R, "left:36px;top:40px;width:370px;height:420px", null, "pn2");
    E(R, "left:66px;top:66px", "Checkout", "tb");
    [[66, 130, 300], [66, 172, 240], [66, 214, 270]].forEach(([x, y, W]) => E(R, `left:${x}px;top:${y}px;width:${W}px;height:18px`, null, "bar"));
    const btn = E(R, "left:66px;top:330px;width:310px;height:84px;border-radius:22px;background:#01ccf7;color:#0a0d2c;font:700 32px/1 Poppins;gap:14px;display:flex;align-items:center;justify-content:center", "", "ic");
    E(R, "left:640px;top:170px;width:130px;height:130px", ico("server", 56, "#b8f1ff"), "node"); E(R, "left:660px;top:316px", "server", "lb");
    const l1 = seg(R, "dash"); const p1 = E(R, "", null, "pk"), p2 = E(R, "", null, "pk");
    const xm = E(R, "left:478px;top:206px;width:58px;height:58px;border-radius:50%;background:#ffffff", ico("x", 32, "#0a0d2c", 3), "ic");
    const no = E(R, "left:430px;top:380px", ico("circle-x", 22, "#b8f1ff") + "klik kedua diabaikan", "cp");
    const C1 = w(5) - 0.02, C2 = w(6) + 0.02, cur = cursor(R), rp1 = ripple(R), rp2 = ripple(R);
    f(C1, "click", -2); f(C1 + 0.5, "pop", -6); f(C2, "click", -3, 1.1); f(C2 + 0.32, "pop", -4, 0.7);
    return (u) => {
      curSet(cur, u, [[0, 560, 460], [C1 - 0.4, 236, 372], [C2 + 0.4, 236, 372], [C2 + 1.0, 300, 440]], [C1, C2]);
      ripSet(rp1, u, C1, 220, 372); ripSet(rp2, u, C2, 220, 372);
      const busy = u >= C1; btn.innerHTML = busy ? spinner(40) + "<span>Memproses…</span>" : "<span>Bayar</span>"; btn.style.opacity = busy ? 0.75 : 1;
      if (busy) btn.querySelector("svg").style.transform = `rotate(${(u * 420) % 360}deg)`;
      segSet(l1, 380, 372, 640, 236, 1, 0.8);
      pkSet(p1, 380, 372, 640, 236, e3(lin(u, C1 + 0.05, C1 + 0.55)), u > C1 && u < C1 + 0.6 ? 1 : 0);
      const b = lin(u, C2 + 0.05, C2 + 0.3); pkSet(p2, 380, 372, 640, 236, b < 1 ? 0.45 * e3(b) : 0.45 - 0.15 * e3(lin(u, C2 + 0.3, C2 + 0.55)), u > C2 && u < C2 + 0.6 ? 1 - lin(u, C2 + 0.4, C2 + 0.6) : 0);
      pop(xm, u, C2 + 0.3); pop(no, u, C2 + 0.45);
    };
  });
  // ============ 16 · parallel requests
  addCard(16, 820, 460, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:460px", null, "pn");
    E(R, "left:36px;top:34px", "request", "lb");
    const B = [["produk", 0, 190, "rgba(1,204,247,.95)"], ["stok", 190, 220, "rgba(106,223,255,.9)"], ["ulasan", 410, 170, "rgba(184,241,255,.85)"]].map(([n, x0, W, col], k) => {
      E(R, `left:36px;top:${84 + k * 84}px`, n, "tb"); return [E(R, `left:190px;top:${86 + k * 84}px;width:${W}px;height:40px;border-radius:12px;background:${col};box-shadow:0 0 18px rgba(1,204,247,.35)`, null, "bar"), x0, W]; });
    E(R, "left:36px;top:388px", "total waktu", "lb");
    const br = E(R, "position:absolute;left:190px;top:340px;height:22px;border:3px solid #ffffff;border-top:0;border-radius:0 0 8px 8px;width:580px", null);
    const ok = E(R, "left:500px;top:384px", ico("zap", 22, "#0a0d2c") + "jalan bareng", "cp on");
    const MV = w(5) - 0.05; B.forEach((_, k) => f(0.1 + k * 0.25, "pop", -8, 1 + 0.1 * k)); f(MV + 0.05, "whoosh", -6, 1.5); f(MV + 0.5, "ping", -7);
    return (u) => {
      const s = spr(u - MV, 2.2, 0.62);
      B.forEach(([e, x0, W], k) => { const g = e3(lin(u, 0.1 + k * 0.25, 0.4 + k * 0.25)); e.style.transform = `translateX(${(x0 * (1 - s)).toFixed(1)}px) scaleX(${g.toFixed(3)})`; e.style.transformOrigin = "0 50%"; });
      const end = Math.max(...B.map(([, x0, W]) => x0 * (1 - cl(s)) + W)); br.style.width = end.toFixed(1) + "px"; op(br, e3(lin(u, 0.6, 0.9)));
      pop(ok, u, MV + 0.45);
    };
  });
  // ============ 17 · timeouts for outside services
  addCard(17, 820, 500, (R, w, f) => {
    E(R, "left:0;top:0;width:820px;height:500px", null, "pn");
    E(R, "left:36px;top:100px;width:290px;height:260px", null, "pn2");
    E(R, "left:62px;top:126px", "Checkout", "tb");
    const st = E(R, "left:62px;top:182px;font-size:24px;color:rgba(220,236,255,.85)", "", "tx");
    const retry = E(R, "left:62px;top:270px", ico("rotate-cw", 22, "#0a0d2c") + "Coba lagi", "cp on");
    E(R, "left:620px;top:140px;width:150px;height:150px", ico("cloud", 64, "#b8f1ff"), "node"); E(R, "left:610px;top:306px", "layanan luar", "lb");
    const ln = seg(R, "dash"); const pk = E(R, "", null, "pk");
    const tm = E(R, "left:420px;top:40px;width:96px;height:96px", '<svg width="96" height="96" viewBox="0 0 96 96"><circle cx="48" cy="48" r="40" fill="rgba(10,20,58,.8)" stroke="rgba(184,241,255,.2)" stroke-width="7"/><circle class="rg" cx="48" cy="48" r="40" fill="none" stroke="#01ccf7" stroke-width="7" stroke-linecap="round" stroke-dasharray="251.3" stroke-dashoffset="251.3" transform="rotate(-90 48 48)"/></svg>', "ic");
    E(tm, "position:absolute;left:28px;top:28px", ico("timer", 40, "#ffffff"), "ic");
    E(R, "left:400px;top:146px", "batas waktu", "lb");
    const xm = E(R, "left:446px;top:206px;width:58px;height:58px;border-radius:50%;background:#ffffff", ico("x", 32, "#0a0d2c", 3), "ic");
    const ok = E(R, "left:36px;top:400px", ico("circle-check", 22, "#0a0d2c") + "aplikasi tetap jalan", "cp on");
    const TO = w(5) + 0.15; f(TO, "click", -3, 0.7); f(TO + 0.25, "pop", -5); f(w(9) - 0.05, "ping", -7);
    return (u) => {
      segSet(ln, 326, 232, 620, 216, e3(lin(u, 0.05, 0.35)), u < TO ? 0.85 : 0.3);
      pkSet(pk, 326, 232, 620, 216, 0.5 * e3(lin(u, 0.2, 1.0)) + 0.02 * Math.sin(u * 9), u > 0.2 && u < TO ? 1 : 0);
      tm.querySelector(".rg").setAttribute("stroke-dashoffset", (251.3 * (1 - lin(u, 0.3, TO))).toFixed(1));
      pop(xm, u, TO); st.textContent = u < TO + 0.1 ? "Cek ongkir…" : "Layanan lambat"; pop(retry, u, TO + 0.25); pop(ok, u, w(9) - 0.15);
    };
  });
  // ============ 18 · background job queue
  addCard(18, 840, 500, (R, w, f) => {
    E(R, "left:0;top:0;width:840px;height:500px", null, "pn");
    E(R, "left:30px;top:36px;width:370px;height:428px", null, "pn2");
    E(R, "left:58px;top:62px", "Laporan", "tb");
    [[58, 122, 300], [58, 160, 250], [58, 198, 280]].forEach(([x, y, W]) => E(R, `left:${x}px;top:${y}px;width:${W}px;height:18px`, null, "bar"));
    const btn = E(R, "left:58px;top:352px;width:310px;height:80px;border-radius:20px;background:#01ccf7;gap:12px;display:flex;align-items:center;justify-content:center;font:700 30px/1 Poppins;color:#0a0d2c", ico("download", 28, "#0a0d2c", 2.4) + "<span>Ekspor PDF</span>", "ic");
    const toast = E(R, "left:46px;top:250px", ico("circle-check", 22, "#0a0d2c") + "diproses di belakang", "cp on");
    E(R, "left:450px;top:36px", "antrean", "lb");
    const SL = ["kirim email", "kecilkan foto"].map((n, k) => E(R, `left:450px;top:${76 + k * 84}px;width:356px;height:66px;border-radius:16px;padding-left:22px;justify-content:flex-start;gap:12px;font:400 25px/1 Poppins;background:rgba(10,20,58,.75);border:1.5px solid rgba(150,210,255,.25);display:flex;align-items:center`, ico("box", 24, "#b8f1ff") + n, "ic"));
    const job = E(R, "left:450px;top:244px;width:356px;height:66px;border-radius:16px;padding-left:22px;justify-content:flex-start;gap:12px;font:700 25px/1 Poppins;background:rgba(1,204,247,.2);border:2px solid #01ccf7;display:flex;align-items:center", ico("file", 24, "#01ccf7") + "ekspor PDF", "ic");
    const gr = E(R, "left:578px;top:344px;width:100px;height:100px", ico("settings", 48, "#01ccf7"), "node"); E(R, "left:584px;top:452px", "pekerja", "lb");
    const cur = cursor(R), rp = ripple(R), CK = 0.4, FL = CK + 0.15;
    f(CK, "click", -2); f(FL + 0.1, "whoosh", -7, 1.6); f(FL + 0.55, "pop", -5); f(1.3, "ping", -7);
    return (u) => {
      curSet(cur, u, [[0, 330, 470], [CK - 0.3, 210, 392], [CK + 0.5, 210, 392], [1.6, 160, 180], [2.3, 300, 140]], [CK, 1.75]);
      ripSet(rp, u, CK, 212, 392); tf(btn, 0, 0, 1 - 0.05 * bump(u, CK - 0.03, 0.2));
      const p = e3(lin(u, FL, FL + 0.55)); tf(job, (1 - p) * -380 + 0, (1 - p) * 108 - Math.sin(Math.PI * p) * 90, 0.6 + 0.4 * p); op(job, u > FL ? 1 : 0);
      SL.forEach((e) => op(e, 1)); gr.querySelector("svg").style.transform = `rotate(${(u * 200) % 360}deg)`; pop(toast, u, 1.25);
    };
  });
  // ============ 19-24 · database tips: the DB cylinder is ONE shared element that glides between them
  const DBP = {};
  addCard(19, 860, 500, (R, w, f) => {
    E(R, "left:0;top:0;width:860px;height:500px", null, "pn");
    E(R, "left:36px;top:150px;width:150px;height:150px", ico("smartphone", 60, "#b8f1ff"), "node"); E(R, "left:52px;top:314px", "aplikasi", "lb");
    const rd = E(R, "left:340px;top:44px;width:200px;height:120px;border-radius:24px;border:2.5px solid #01ccf7;background:rgba(1,204,247,.14);gap:12px;display:flex;align-items:center;justify-content:center", ico("zap", 32, "#01ccf7") + '<span style="font:700 32px/1 Poppins">Redis</span>', "ic");
    E(R, "left:350px;top:14px", "simpan sementara", "lb");
    const la = seg(R, "dash"), lr = seg(R, "dash"), ls = seg(R, "dash"); const p1 = E(R, "", null, "pk"), p2 = E(R, "", null, "pk"), p3 = E(R, "", null, "pk");
    const t1 = E(R, "left:36px;top:400px;font-size:23px;color:rgba(220,236,255,.8)", "pertama kali: ambil dari database", "tx");
    const t2 = E(R, "left:36px;top:440px;font-size:23px;color:#b8f1ff", "berikutnya: langsung dari Redis ✓", "tx");
    DBP[19] = [700, 300];
    const A = [186, 225], D = [640, 300], Rr = [440, 164], S1 = w(4) + 0.02, Q2 = w(7) - 0.1;
    f(0.2, "pop", -8); f(S1 + 0.2, "pop", -5); f(Q2 + 0.12, "ping", -5);
    return (u) => {
      segSet(la, A[0], A[1], D[0], D[1], e3(lin(u, 0, 0.3)), 0.75); segSet(lr, A[0], A[1] - 20, 340, 120, e3(lin(u, 0.1, 0.4)), 0.75); segSet(ls, 560, 160, D[0] + 10, D[1] - 50, 1, u > S1 - 0.1 ? 0.75 : 0);
      const a = lin(u, 0.15, 1.05); pkSet(p1, ...(a < 0.5 ? [A[0], A[1], D[0], D[1], eio(a * 2)] : [D[0], D[1], A[0], A[1], eio(a * 2 - 1)]), a > 0 && a < 1 ? 1 : 0);
      const b = lin(u, S1, S1 + 0.45); pkSet(p3, D[0] + 10, D[1] - 50, 540, 140, eio(b), b > 0 && b < 1 ? 1 : 0);
      rd.style.boxShadow = `0 0 ${(10 + 30 * bump(u, S1 + 0.35, 0.5) + 30 * bump(u, Q2 + 0.05, 0.4)).toFixed(0)}px rgba(1,204,247,.6)`;
      const c = lin(u, Q2 - 0.1, Q2 + 0.3); pkSet(p2, ...(c < 0.5 ? [A[0], A[1] - 20, 340, 120, eio(c * 2)] : [340, 120, A[0], A[1] - 20, eio(c * 2 - 1)]), c > 0 && c < 1 ? 1 : 0);
      op(t1, e3(lin(u, 0.4, 0.7))); op(t2, e3(lin(u, Q2, Q2 + 0.3)));
    };
  });
  addCard(20, 860, 520, (R, w, f) => {
    E(R, "left:0;top:0;width:860px;height:520px", null, "pn");
    const NM = ["andi", "budi", "citra", "dewi", "eka", "fajar", "gita", "hana", "rina"];
    E(R, "left:36px;top:30px", "tabel pelanggan", "lb");
    const RW = NM.map((n, k) => { const r = E(R, `left:36px;top:${66 + k * 48}px;width:440px;height:40px;border-radius:10px;background:rgba(10,20,58,.6);padding-left:18px;justify-content:flex-start;font:400 22px/1 Poppins;display:flex;align-items:center`, n + "@mail.com", "ic"); return r; });
    const IX = E(R, "left:520px;top:200px;width:200px;height:290px", null, "pn2");
    E(R, "left:540px;top:216px;color:#b8f1ff", "index", "lb");
    const GR = ["a – e", "f – j", "k – o", "p – t", "u – z"].map((g, k) => E(R, `left:536px;top:${250 + k * 46}px;width:168px;height:38px;border-radius:10px;font:700 22px/1 Poppins;display:flex;align-items:center;justify-content:center`, g, "ic"));
    const q = E(R, "left:500px;top:140px", ico("search", 22, "#b8f1ff") + "cari: rina", "cp");
    const ar = seg(R); ar.style.background = "#01ccf7"; ar.style.boxShadow = "0 0 12px #01ccf7";
    DBP[20] = [775, 96];
    const IA = w(1) - 0.05, SA = w(4) - 0.05, HIT = SA + 0.55;
    f(IA + 0.1, "pop", -5); f(SA, "pop", -6, 1.2); f(HIT, "ping", -5);
    return (u) => {
      const ip = spr(u - IA, 2.2, 0.6); op(IX, cl(ip * 3)); tf(IX, 40 * (1 - ip), 0); GR.forEach((g, k) => { op(g, cl(ip * 3)); tf(g, 40 * (1 - ip), 0); });
      pop(q, u, SA);
      const gk = 3, on = u > SA + 0.25; GR.forEach((g, k) => { g.style.background = on && k === gk ? "#01ccf7" : "rgba(255,255,255,.06)"; g.style.color = on && k === gk ? "#0a0d2c" : "#fff"; });
      segSet(ar, 536, 250 + gk * 46 + 19, 476, 66 + 8 * 48 + 20, e3(lin(u, SA + 0.3, HIT)), u > SA + 0.3 ? 1 : 0);
      RW.forEach((r, k) => { const hit = k === 8 && u > HIT; r.style.background = hit ? "#01ccf7" : "rgba(10,20,58,.6)"; r.style.color = hit ? "#0a0d2c" : "#fff"; r.style.fontWeight = hit ? 700 : 400;
        op(r, k === 8 ? 1 : 1 - 0.65 * e3(lin(u, HIT + 0.1 + k * 0.04, HIT + 0.4 + k * 0.04))); });
    };
  });
  addCard(21, 860, 520, (R, w, f) => {
    E(R, "left:0;top:0;width:860px;height:520px", null, "pn");
    E(R, "left:36px;top:30px", "daftar postingan", "lb");
    const PS = [0, 1, 2, 3, 4].map((k) => E(R, `left:36px;top:${68 + k * 84}px;width:330px;height:68px;border-radius:16px;background:rgba(10,20,58,.7);border:1.5px solid rgba(150,210,255,.22);padding-left:20px;gap:14px;justify-content:flex-start;font:400 24px/1 Poppins;display:flex;align-items:center`, ico("user", 26, "#b8f1ff") + "Postingan " + (k + 1), "ic"));
    DBP[21] = [720, 270];
    const LN = PS.map(() => seg(R, "dash")), PK = PS.map(() => E(R, "", null, "pk"));
    const big = seg(R); big.style.height = "12px"; big.style.background = "#01ccf7"; big.style.boxShadow = "0 0 20px #01ccf7";
    const brk = E(R, "position:absolute;left:376px;top:72px;width:22px;height:404px;border:4px solid #ffffff;border-left:0;border-radius:0 12px 12px 0", null);
    const cnt = E(R, "left:430px;top:36px;font-size:30px", "", "tb");
    const ok = E(R, "left:430px;top:420px", ico("zap", 22, "#0a0d2c") + "diambil sekaligus", "cp on");
    const MG = w(5) - 0.05;
    PS.forEach((_, k) => f(0.3 + k * 0.2, "click", -8, 1.3)); f(MG + 0.05, "whoosh", -6, 1.4); f(MG + 0.45, "ping", -6);
    return (u) => {
      const m = e3(lin(u, MG, MG + 0.3));
      PS.forEach((p, k) => { const a = 0.3 + k * 0.2; segSet(LN[k], 366, 102 + k * 84, 660, 270, e3(lin(u, a, a + 0.2)), (u > a ? 0.8 : 0) * (1 - m)); pkSet(PK[k], 366, 102 + k * 84, 660, 270, e3(lin(u, a, a + 0.3)), u > a && u < a + 0.32 ? 1 : 0); });
      const n = PS.filter((_, k) => u > 0.3 + k * 0.2).length; cnt.innerHTML = u < MG ? `query: <span style="color:#01ccf7">1 + ${n}</span>` : `query: <span style="color:#01ccf7">digabung</span>`;
      segSet(big, 398, 270, 660, 270, e3(lin(u, MG + 0.1, MG + 0.4)), m); op(brk, m); pop(ok, u, MG + 0.4);
    };
  });
  addCard(22, 860, 480, (R, w, f) => {
    E(R, "left:0;top:0;width:860px;height:480px", null, "pn");
    E(R, "left:36px;top:34px", "ambil dari tabel", "lb");
    const qq = E(R, "left:36px;top:76px", ico("filter", 22, "#0a0d2c") + "nama, email", "cp on");
    const CO = ["id", "nama", "email", "alamat", "foto", "riwayat", "catatan"], KEEP = [1, 2];
    const tb = E(R, "position:absolute;left:36px;top:170px;width:788px;height:280px;overflow:hidden", null);
    const CW0 = [80, 110, 170, 110, 90, 110, 108];
    const COL = CO.map((n, k) => { const c = E(tb, "position:absolute;top:0;height:280px;overflow:hidden", null);
      E(c, "left:10px;top:12px;font:700 22px/1 Poppins;white-space:nowrap", n, "tx"); for (let r = 0; r < 4; r++) E(c, `left:10px;top:${66 + r * 52}px;width:${n === "email" ? 150 : 80}px;height:16px`, null, "bar"); return c; });
    DBP[22] = [770, 86];
    const P1 = w(3) - 0.05, P2 = w(5) - 0.05; f(P1, "pop", -5); f(P2 + 0.05, "whoosh", -7, 1.7);
    return (u) => {
      pop(qq, u, P1);
      const hi = e3(lin(u, P1, P1 + 0.25)), cut = e3(lin(u, P2, P2 + 0.4)); let x = 0;
      COL.forEach((c, k) => { const keep = KEEP.includes(k), W0 = CW0[k], W = keep ? (k === 2 ? mix(170, 260, cut) : mix(110, 170, cut)) : W0 * (1 - cut);
        c.style.left = x + "px"; c.style.width = W + "px"; x += W;
        c.style.background = keep ? `rgba(1,204,247,${(0.2 * hi).toFixed(2)})` : "rgba(255,255,255,.03)"; c.style.borderRight = "1px solid rgba(150,210,255,.15)"; op(c, keep ? 1 : (1 - 0.6 * hi) * Math.pow(1 - cut, 3)); });
    };
  });
  addCard(23, 860, 520, (R, w, f) => {
    E(R, "left:0;top:0;width:860px;height:520px", null, "pn");
    E(R, "left:36px;top:30px", "hasil pencarian", "lb");
    const RW = []; for (let k = 0; k < 14; k++) RW.push(E(R, `left:36px;top:0;width:600px;height:50px;border-radius:12px;background:rgba(10,20,58,.7);border:1.5px solid rgba(150,210,255,.2);padding-left:20px;justify-content:flex-start;font:400 23px/1 Poppins;display:flex;align-items:center`, "Produk " + String(k + 1).padStart(2, "0"), "ic"));
    const pg = E(R, "left:36px;top:430px;display:flex;gap:10px;position:absolute", null);
    const PB = ["‹", "1", "2", "3", "…", "›"].map((n) => E(pg, "position:relative;width:56px;height:56px;border-radius:14px;background:rgba(255,255,255,.08);font:700 24px/1 Poppins", n, "ic"));
    DBP[23] = [760, 100];
    const SPL = w(3) - 0.05, NX = w(7) - 0.15; f(SPL + 0.05, "whoosh", -7, 1.5); f(SPL + 0.4, "pop", -6); f(NX, "click", -3);
    return (u) => {
      const s = e3(lin(u, SPL, SPL + 0.45)), nx = e3(lin(u, NX, NX + 0.3));
      RW.forEach((r, k) => { const y0 = 62 + k * 40, page = k < 5 ? 0 : k < 10 ? 1 : 2; const y1 = 66 + (k % 5) * 70;
        let x = 0, o = 1, y = mix(y0, y1, s); if (page === 0) { x = -200 * nx; o = 1 - nx; } else if (page === 1) { x = mix(300, 0, nx) * s; o = s < 0.01 ? 1 : nx; } else { x = 300 * s; o = 1 - s; }
        if (s < 0.01 && y0 > 400) o = Math.max(0, 1 - (y0 - 400) / 80);
        r.style.top = y.toFixed(1) + "px"; r.style.height = mix(32, 50, s).toFixed(1) + "px"; r.style.fontSize = mix(20, 23, s).toFixed(1) + "px"; tf(r, x, 0); op(r, o); });
      op(pg, s); PB.forEach((b, k) => { const act = (k === 1 && nx < 0.5) || (k === 2 && nx >= 0.5); b.style.background = act ? "#01ccf7" : "rgba(255,255,255,.08)"; b.style.color = act ? "#0a0d2c" : "#fff"; });
    };
  });
  addCard(24, 860, 500, (R, w, f) => {
    E(R, "left:0;top:0;width:860px;height:500px", null, "pn");
    const US = [0, 1, 2].map((k) => E(R, `left:36px;top:${56 + k * 130}px;width:100px;height:100px`, ico("users", 44, "#b8f1ff"), "node"));
    const pool = E(R, "left:300px;top:110px;width:230px;height:260px", null, "pn2"); E(R, "left:326px;top:126px;color:#b8f1ff", "pool", "lb");
    const PI = [0, 1, 2].map((k) => { const s = seg(R); s.style.height = "8px"; s.style.background = "#01ccf7"; s.style.boxShadow = "0 0 14px rgba(1,204,247,.7)"; return s; });
    const PL = [0, 1, 2].map((k) => E(R, `left:330px;top:${172 + k * 64}px;width:170px;height:44px;border-radius:12px;border:2px solid rgba(1,204,247,.7);background:rgba(1,204,247,.12);font:700 20px/1 Poppins;gap:8px;display:flex;align-items:center;justify-content:center`, ico("plug", 20, "#01ccf7") + "koneksi " + (k + 1), "ic"));
    const LI = [0, 1, 2].map(() => seg(R, "dash")); const DOT = []; for (let k = 0; k < 9; k++) DOT.push(E(R, "", null, "pk"));
    const lbl = E(R, "left:300px;top:404px", ico("refresh-cw", 22, "#0a0d2c") + "dipakai ulang", "cp on");
    DBP[24] = [740, 250];
    const PA = w(1) - 0.05; f(PA + 0.1, "pop", -5); [0, 1, 2].forEach((k) => f(PA + 0.25 + k * 0.1, "click", -8, 1.2)); f(w(5) + 0.1, "ping", -7);
    return (u) => {
      const pp = spr(u - PA, 2.2, 0.6); op(pool, cl(pp * 3)); PL.forEach((e, k) => pop(e, u, PA + 0.15 + k * 0.1));
      PI.forEach((s, k) => segSet(s, 500, 194 + k * 64, 680, 250, e3(lin(u, PA + 0.25 + k * 0.1, PA + 0.5 + k * 0.1)), 1));
      LI.forEach((s, k) => segSet(s, 136, 106 + k * 130, 300, 194 + k * 64, 1, 0.6));
      DOT.forEach((d, k) => { const ph = ((u * 0.9 + k / 9) % 1), lane = k % 3; const a = ph < 0.45 ? eio(ph / 0.45) : 1, b = ph < 0.45 ? 0 : eio((ph - 0.45) / 0.55);
        const x = ph < 0.45 ? mix(136, 330, a) : mix(500, 680, b), y = ph < 0.45 ? mix(106 + lane * 130, 194 + lane * 64, a) : mix(194 + lane * 64, 250, b);
        d.style.left = x.toFixed(1) + "px"; d.style.top = y.toFixed(1) + "px"; op(d, u > PA + 0.4 ? (ph > 0.42 && ph < 0.47 ? 0 : 0.95) : 0); d.style.transform = "scale(.75)"; });
      pop(lbl, u, w(5) - 0.05);
    };
  });
  // ============ 25 · test on cheap phones + weak signal
  addCard(25, 820, 540, (R, w, f) => {
    const ph = E(R, "position:absolute;left:40px;top:20px;width:280px;height:500px;border-radius:44px;border:3px solid rgba(184,241,255,.45);background:#0b1440;box-shadow:0 26px 50px rgba(0,0,0,.45)", null);
    const scr = E(ph, "position:absolute;left:13px;top:13px;width:248px;height:468px;border-radius:32px;overflow:hidden;background:#101c4a", null);
    E(scr, "left:18px;top:14px;display:flex;gap:6px;align-items:center", ico("signal-low", 22, "#b8f1ff") + ico("wifi-low", 22, "#b8f1ff"), "ic");
    E(scr, "left:24px;top:120px;width:200px;height:200px;display:grid;place-items:center", spinner(90), "ic");
    E(scr, "left:24px;top:350px;width:200px;height:16px", null, "bar"); const pr = E(scr, "left:24px;top:350px;width:200px;height:16px;transform-origin:0 50%", null, "bar acc");
    E(scr, "left:24px;top:384px;font-size:20px;color:rgba(220,236,255,.7)", "memuat…", "tx");
    E(R, "left:370px;top:40px;width:420px;height:440px", null, "pn");
    E(R, "left:404px;top:76px", "tes dulu di", "lb");
    const TG = [["cpu", "HP murah", w(3)], ["signal-low", "sinyal lemah", w(6)], ["gauge", "cek kecepatan", w(7) + 0.3]].map(([ic, n, a], k) => {
      E(R, `left:404px;top:${130 + k * 104}px`, ico(ic, 34, "#b8f1ff"), "ic"); E(R, `left:452px;top:${128 + k * 104}px;font-size:28px`, n, "tb");
      const tr = E(R, `position:absolute;left:690px;top:${126 + k * 104}px;width:76px;height:42px;border-radius:21px;background:rgba(255,255,255,.14)`, null);
      const kn = E(tr, "position:absolute;left:5px;top:5px;width:32px;height:32px;border-radius:50%;background:#ffffff", null); f(a + 0.05, "click", -4, 1.1); return [tr, kn, a]; });
    return (u) => {
      scr.querySelector("svg circle + path") && (scr.querySelectorAll("svg")[2].style.transform = `rotate(${(u * 300) % 360}deg)`);
      pr.style.transform = `scaleX(${(0.08 + 0.5 * lin(u, 0.4, 2.8)).toFixed(3)})`;
      TG.forEach(([tr, kn, a]) => { const p = spr(u - a, 2.6, 0.6); kn.style.transform = `translateX(${(34 * p).toFixed(1)}px)`; tr.style.background = p > 0.5 ? "#01ccf7" : "rgba(255,255,255,.14)"; });
    };
  }, 890);
  // ============ 26 · CTA — the toolkit + "Komen APP"
  addCard(26, 760, 520, (R, w, f) => {
    E(R, "left:0;top:0;width:760px;height:520px", null, "pn");
    E(R, "left:36px;top:30px;font:700 38px/1 Poppins;white-space:nowrap", 'App ngebut <span style="font-style:italic;background:linear-gradient(95deg,#b8f1ff,#01ccf7 55%,#0aa7d6);-webkit-background-clip:text;background-clip:text;color:transparent;padding-right:.12em">toolkit</span>', "tb");
    E(R, "left:36px;top:84px;font-size:22px;color:rgba(220,236,255,.75)", "24 perbaikan + prompt siap tempel buat Claude", "tx");
    const RW = TIPS.map((n, k) => E(R, `left:${32 + Math.floor(k / 12) * 360}px;top:${130 + (k % 12) * 30.5}px;font:400 19px/1 Poppins;white-space:nowrap;display:flex;align-items:center;gap:8px`, `${ico("circle-check", 19, "#01ccf7", 2.4)}<span style="color:#01ccf7;font-weight:700">${String(k + 1).padStart(2, "0")}</span> ${n}`, "ic"));
    RW.forEach((_, k) => { if (k % 3 === 0) f(0.15 + k * 0.045, "click", -9, 1.4); });
    return (u) => { RW.forEach((r, k) => { const p = e3(lin(u, 0.1 + k * 0.045, 0.3 + k * 0.045)); op(r, p); tf(r, 16 * (1 - p), 0); }); };
  }, 880);
  // ------------------------------------------------------------------ shared database cylinder
  const dbEl = $("db"); dbEl.innerHTML = DBSVG;
  const DBI = [19, 20, 21, 22, 23, 24];
  const dbAbs = (i) => { const c = C[i]; return [CX - c.W / 2 + DBP[i][0], c.cy - c.H / 2 + DBP[i][1]]; };
  function dbAt(t) {
    const a = C[19], z = C[24];
    if (t < a.tin - 0.01 || t > z.tout + 0.3) return null;
    let x, y; const p0 = dbAbs(19); x = p0[0]; y = p0[1];
    for (let j = 0; j < DBI.length - 1; j++) { const i = DBI[j], n = DBI[j + 1]; const s = spr(t - C[i].tout - 0.04, 1.9, 0.68); if (t > C[i].tout) { const A = dbAbs(i), B = dbAbs(n); x = mix(A[0], B[0], s); y = mix(A[1], B[1], s) - 60 * Math.sin(Math.PI * cl(s)); } }
    const sa = cardState(a, t), sz = cardState(z, t);
    let o = cl(e3(lin(t, a.tin, a.tin + 0.2))) * (1 - eio(lin(t, z.tout, z.tout + 0.24)));
    let s = 0.55 + 0.45 * spr(t - a.tin, 2.0, 0.6);
    if (t < a.tin + 0.6) { x += sa.x; y += sa.y; } if (t > z.tout) { x += sz.x; y += sz.y; s *= sz.s; }
    return { x, y, s, o };
  }
  function db(t) {
    const S = dbAt(t); if (!S) { dbEl.style.display = "none"; return; } dbEl.style.display = "block";
    const P = dbAt(t - 1 / 30) || S; const v = Math.hypot(S.x - P.x, S.y - P.y); const bl = v > 8 ? Math.min(7, (v - 8) * 0.1) : 0;
    dbEl.style.transform = `translate(${S.x.toFixed(1)}px,${S.y.toFixed(1)}px) scale(${S.s.toFixed(3)})`; op(dbEl, S.o); dbEl.style.filter = bl > 0.2 ? `blur(${bl.toFixed(2)}px)` : "none";
  }
  DBI.slice(0, -1).forEach((i) => fx(C[i].tout + 0.3, "pop", -7, 0.8));
  // ------------------------------------------------------------------ counter
  const ctr = $("ctr"), dgA = $("dgA"), dgB = $("dgB"), ring = $("ring");
  function counter(t) {
    let i = -1; for (let k = 2; k <= 25; k++) if (t >= L[k].t0 - 0.2) i = k;
    const show = t >= L[2].t0 - 0.3 && t < L[26].t0 - 0.3;
    const p = spr(t - (L[2].t0 - 0.3), 2.4, 0.6) * (1 - eio(lin(t, L[26].t0 - 0.35, L[26].t0 - 0.1)));
    op(ctr, show ? cl(p * 2) : 0); ctr.style.transform = `translateY(${(30 * (1 - cl(p))).toFixed(1)}px) scale(${(0.85 + 0.15 * p).toFixed(3)})`;
    if (i < 0) i = 2;
    const n = i - 1, a = L[i].t0 - 0.2, r = e3(lin(t, a, a + 0.25));
    dgA.textContent = String(Math.max(1, n - 1)).padStart(2, "0"); dgB.textContent = String(n).padStart(2, "0");
    if (n === 1) { dgA.style.transform = "translateY(-44px)"; dgB.style.transform = "translateY(0)"; }
    else { dgA.style.transform = `translateY(${(-44 * r).toFixed(1)}px)`; dgB.style.transform = `translateY(${(44 * (1 - r)).toFixed(1)}px)`; }
    const bp = lin(t, L[i].t0 - 0.2, (i < 26 ? L[i + 1].t0 : DUR) - 0.2); ring.setAttribute("stroke-dashoffset", (106.8 * (1 - bp)).toFixed(1));
  }
  for (let k = 3; k <= 25; k++) fx(L[k].t0 - 0.12, "click", -10, 1.7);
  // ------------------------------------------------------------------ CTA pill + DM chip
  const cta = $("cta"), ctar = $("ctaring"), dmc = $("dmchip");
  $("ctaic").innerHTML = ico("message-circle", 50, "#0a0d2c", 2.6);
  dmc.innerHTML = ico("send", 24, "#b8f1ff") + "aku kirim lewat DM";
  const L26 = L[26], cw = (k) => L26.ws[k][1];
  fx(L26.t0 - 0.05, "impact", 0); fx(L26.t0 - 0.05, "riser", 0); fx(cw(1) + 0.1, "pop", -2, 0.8); fx(cw(9) + 0.05, "ping", -4); fx(cw(9) + 0.3, "sparkle", -6);
  function ctaF(t) {
    const p = spr(t - (L26.t0 - 0.05), 2.0, 0.55); op(cta, t > L26.t0 - 0.05 ? cl(p * 3) : 0);
    const pulse = 0.04 * Math.sin(Math.max(0, t - cw(1)) * 5.5) * (t > cw(1) ? 1 : 0);
    cta.style.transform = `translateY(${(60 * (1 - p)).toFixed(1)}px) scale(${(0.7 + 0.3 * p + pulse).toFixed(3)})`;
    const rr = lin((t - cw(1)) % 1.1, 0, 1.1); op(ctar, t > cw(1) ? 0.8 * (1 - rr) : 0); ctar.style.transform = `scale(${(0.9 + 0.25 * rr).toFixed(3)})`;
    pop(dmc, t, cw(9) - 0.1);
    const fl = $("flash"); op(fl, 0.55 * bump(t, L26.t0 - 0.12, 0.45));
  }
  // ------------------------------------------------------------------ background: glow, particles, grain
  const parts = []; for (let k = 0; k < 30; k++) { const e = document.createElement("i"); const s = 2 + ((k * 37) % 4); e.style.width = e.style.height = s + "px"; $("parts").appendChild(e); parts.push([e, (k * 997) % 1080, (k * 613) % 1920, 12 + ((k * 7) % 20), 0.1 + ((k * 13) % 25) / 100]); }
  function bg(t) {
    parts.forEach(([e, x, y, sp, o], k) => { const yy = ((y - t * sp) % 2000 + 2000) % 2000 - 40; const xx = x + 14 * Math.sin(t * 0.3 + k); e.style.transform = `translate(${xx.toFixed(1)}px,${yy.toFixed(1)}px)`; op(e, o * (0.6 + 0.4 * Math.sin(t * 1.3 + k * 2))); });
    $("glow").style.transform = `scale(${(1 + 0.05 * Math.sin(t * 0.7)).toFixed(3)})`;
    const g = Math.floor(t * 12); $("grain").style.transform = `translate(${(g * 37) % 64}px,${(g * 23) % 64}px)`;
    op($("brandlogo"), 0.96 * e3(lin(t, 0.05, 0.4)));
  }
  // ------------------------------------------------------------------ render
  function render(t) { bg(t); heads(t); cards(t); db(t); counter(t); ctaF(t); }
  window.__r37render = render;
  render(0);
  window.addEventListener("hf-seek", (e) => render(e.detail.time));
})();

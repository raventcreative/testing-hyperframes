/* R36 · Peta AI agent (AI PRENEUR, WHITE). 2D "ref2 look": spoken headline on top (one italic accent word), ONE animated card / map in
   the middle, the client's mascot small + whole bottom-left, beat counter bottom-right. Every style is a pure function of t
   (render(t) on hf-seek + timeline update; no timers, no state between frames). Times come from the untouched VO take
   (window.WORDS + 0.3 s offset). Shared elements: map node <- claude.ai window, input tiles -> node, pill <-> department card,
   agent dot -> task card -> workflow doc, approval chip, morning page -> map doc. Closed-form springs; 3-subframe ghosts on
   the fast flying chips/tiles; velocity blur on card whips. Sound events are registered with ev() and exported to sfx.py. */
(function () {
  const OFF = 0.3, D = window.R36_TOTAL, WT = window.WORDS.map((w) => +(w[1] + OFF).toFixed(3)), WE = window.WORDS.map((w) => +(w[2] + OFF).toFixed(3));
  const wt = (i) => WT[i];
  const ICO = window.R30_ICO;
  const $ = (id) => document.getElementById(id);
  const ui = $("ui"), GRAIN = $("grain");
  const ico = (n, c = "#fff", sw = 2.2) => `<svg viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round">${ICO[n]}</svg>`;
  const mk = (html, parent) => { const d = document.createElement("div"); d.innerHTML = html.trim(); const el = d.firstChild; (parent || ui).insertBefore(el, parent ? null : GRAIN); return el; };
  // ------------------------------------------------------------------ math (pure functions of t)
  const cl = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const lin = (t, a, b) => cl((t - a) / (b - a));
  const eo = (t, a, b) => 1 - Math.pow(1 - lin(t, a, b), 3);
  const ei = (t, a, b) => Math.pow(lin(t, a, b), 3);
  const eio = (t, a, b) => { const u = lin(t, a, b); return u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2; };
  const spr = (t, t0, w = 17, z = 0.62) => { const u = t - t0; if (u <= 0) return 0; const wd = w * Math.sqrt(1 - z * z); return 1 - Math.exp(-z * w * u) * (Math.cos(wd * u) + (z * w / wd) * Math.sin(wd * u)); };
  const L = (a, b, u) => a + (b - a) * u;
  const win = (t, a, b, fi = 0.25, fo = 0.25) => Math.min(eo(t, a, a + fi), 1 - ei(t, b - fo, b));
  function S(el, p) {
    const o = p.o === undefined ? 1 : p.o;
    if (o <= 0.002) { if (el.style.visibility !== "hidden") { el.style.visibility = "hidden"; el.style.opacity = "0"; } return; }
    el.style.visibility = "visible"; el.style.opacity = o.toFixed(3);
    const s = p.s === undefined ? 1 : p.s, sx = (p.sx === undefined ? 1 : p.sx) * s, sy = (p.sy === undefined ? 1 : p.sy) * s;
    el.style.transform = `translate(${(p.x || 0).toFixed(2)}px,${(p.y || 0).toFixed(2)}px)` + (p.ry ? ` perspective(1400px) rotateY(${p.ry.toFixed(2)}deg)` : "") + (p.r ? ` rotate(${p.r.toFixed(2)}deg)` : "") + ` scale(${sx.toFixed(4)},${sy.toFixed(4)})`;
    const b = p.b || 0; el.style.filter = b > 0.05 ? `blur(${b.toFixed(2)}px)` : "none";
  }
  const hide = (el) => S(el, { o: 0 });
  // ------------------------------------------------------------------ sound events (exported for tools/sfx.py)
  const EV = []; const ev = (t, n, db = 0, rate = 1) => { EV.push([+t.toFixed(3), n, db, rate]); return t; };
  window.R36_SFX = EV;
  // ------------------------------------------------------------------ 3-subframe ghosts for small fast movers
  const GH = [];
  function ghosts(el) { const g = [0, 1].map(() => { const c = el.cloneNode(true); c.removeAttribute("id"); c.querySelectorAll("[id]").forEach((n) => n.removeAttribute("id")); el.parentNode.insertBefore(c, el); return c; }); GH.push(g); return g; }
  function mb(el, g, f, t) {   // f(t) -> pose; ghosts at t +- 1/90 s only while the element moves fast
    const p = f(t); S(el, p);
    const a = f(t - 1 / 90), b = f(t + 1 / 90), sp = Math.hypot((b.x || 0) - (a.x || 0), (b.y || 0) - (a.y || 0)) * 45;
    if (sp < 500 || (p.o === undefined ? 1 : p.o) < 0.02) { hide(g[0]); hide(g[1]); return; }
    const k = cl((sp - 500) / 900) * 0.42;
    S(g[0], Object.assign({}, a, { o: (a.o === undefined ? 1 : a.o) * k })); S(g[1], Object.assign({}, b, { o: (b.o === undefined ? 1 : b.o) * k }));
  }
  // ------------------------------------------------------------------ sprites (3D Simple Icons logos, 36-frame turntables)
  const spr3 = (name, size, x, y, parent, extra = "") => mk(`<div class="spr" data-n="${name}" style="left:${x}px;top:${y}px;width:${size}px;height:${size}px;background-image:url(assets/logos3d/${name}.png);${extra}"></div>`, parent);
  function frame(el, deg) { const f = ((Math.round(deg / 10) % 36) + 36) % 36; el.style.backgroundPosition = `${(f % 6) * 20}% ${Math.floor(f / 6) * 20}%`; }
  const wob = (t, ph = 0, amp = 22) => amp * Math.sin(t * 1.7 + ph);
  // ------------------------------------------------------------------ beats (word ranges; headline = the spoken words)
  // [first word, last word, emphasised word]
  const BEATS = [[0, 8, 1], [9, 16, 14], [17, 22, 22], [23, 25, 25], [26, 29, 29], [30, 34, 30], [35, 39, 38], [40, 43, 40], [44, 49, 45], [50, 52, 50],
    [53, 57, 57], [58, 63, 58], [64, 70, 64], [71, 76, 71], [77, 81, 79], [82, 85, 84], [86, 92, 86], [93, 98, 97], [99, 101, 100], [102, 107, 102],
    [108, 110, 110], [111, 116, 116], [117, 123, 122], [124, 131, 125]];
  window.R36_BEATS = BEATS;
  const NB = BEATS.length;
  const BS = BEATS.map((b, k) => (k === 0 ? 0 : wt(b[0]) - 0.12));
  const BE = BS.map((s, k) => (k < NB - 1 ? BS[k + 1] : D));
  function BUILD() {
  const SHOW = { 9: "30", 10: "", 125: "PETA," };
  const HL = BEATS.map((b, k) => {
    const el = mk(`<div class="hl" id="h${k}"></div>`);
    const ws = [];
    for (let i = b[0]; i <= b[1]; i++) {
      let s = SHOW[i] !== undefined ? SHOW[i] : window.WORDS[i][0];
      if (i === b[0]) s = s.charAt(0).toUpperCase() + s.slice(1);
      if (s === "") continue;
      const sp = document.createElement("span"); sp.className = "w" + (i === b[2] ? " em" : ""); sp.textContent = s;
      el.appendChild(sp); el.appendChild(document.createTextNode(" ")); ws.push([sp, i]);
    }
    if (el.offsetHeight > 72 * 2.5) el.style.fontSize = "54px";
    return { el, ws };
  });
  function headline(t) {
    HL.forEach((h, k) => {
      const a = BS[k], b = BE[k];
      if (t < a - 0.3 || t > b + 0.35) { hide(h.el); return; }
      S(h.el, { o: 1 });
      const out = lin(t, b - 0.1, b + 0.1);
      h.ws.forEach(([sp, i], j) => {
        const t0 = Math.max(k === 0 ? 0.2 : a + 0.08, wt(i) - 0.1), u = spr(t, t0, 19, 0.7), e = eo(t, t0, t0 + 0.22);
        if (u <= 0) { hide(sp); return; }
        const oo = 1 - eo(out, 0, 1);
        S(sp, { o: e * oo, y: 34 * (1 - u) - 26 * ei(out, 0, 1), b: 8 * (1 - e) + 6 * out, s: 0.94 + 0.06 * u });
      });
    });
  }
  // counter "07 / 24"
  const CN0 = $("cn0"), CN1 = $("cn1"), ARC = $("cntarc");
  const pad = (n) => String(n).padStart(2, "0");
  function counter(t) {
    let k = 0; for (let i = 0; i < NB; i++) if (t >= BS[i]) k = i;
    const u = k > 0 ? eo(t, BS[k], BS[k] + 0.3) : 1;
    CN0.textContent = pad(k); CN1.textContent = pad(k + 1);
    S(CN0, { y: -36 * u, o: 1 - u }); S(CN1, { y: 36 * (1 - u), o: u });
    ARC.setAttribute("stroke-dashoffset", (100.5 * (1 - lin(t, BS[k], BE[k]))).toFixed(2));
    S($("cnt"), { o: eo(t, 0.3, 0.7), s: 1 + 0.08 * Math.max(0, Math.sin(Math.PI * lin(t, BS[k], BS[k] + 0.25))) });
  }
  BS.forEach((s, k) => { if (k) ev(s + 0.02, "tick", -4, 1.2); });
  // particles: slow deterministic drift
  const PTS = []; for (let i = 0; i < 22; i++) { const r = 5 + (i * 7) % 9; PTS.push([mk(`<div class="pt" style="width:${r}px;height:${r}px"></div>`, $("pts")), (i * 137.5) % 1080, (i * 291.7) % 1920, 0.06 + ((i * 13) % 10) / 70, i]); }
  function particles(t) { for (const [el, x0, y0, o, i] of PTS) S(el, { x: (x0 + 14 * Math.sin(t * 0.3 + i)) % 1080, y: ((y0 - t * (8 + (i % 5) * 3)) % 1920 + 1920) % 1920, o }); }

  // ================================================================== SCENE TIMES
  const T = {
    s1: 0, s2: BS[2], s3: BS[5], s4: BS[6], s5: BS[7], s5b: BS[8], s6: BS[9], s6b: BS[10], s7: BS[11], s8: BS[12], s9: BS[13], s10: BS[14], s10b: BS[15],
    s11: BS[16], s12: BS[17], s12b: BS[18], s13: BS[19], s13b: BS[20], s14: BS[21], s14b: BS[22], s15: BS[23],
  };
  // ================================================================== MAP (through-line: hook, 7 departments, one-task)
  const DEPTS = [
    { id: "jual", n: "Penjualan", ic: "funnel", ag: ["Pencari Prospek", "Penyaring Prospek", "Penulis Chat Pertama", "Pengatur Janji Temu", "Pencatat Prospek"] },
    { id: "close", n: "Closing", ic: "badge-check", ag: ["Penyusun Penawaran", "Penjaga Follow-up", "Penjawab Keberatan", "Pengonfirmasi Order"] },
    { id: "mkt", n: "Marketing", ic: "megaphone", ag: ["Perencana Konten", "Penulis Konten", "Pembalas Komentar", "Pengubah Format", "Pembaca Performa"] },
    { id: "cs", n: "CS", ic: "message-square", ag: ["Penjawab Chat", "Penerus Komplain", "Penjaga Pelanggan", "Pengumpul Ulasan"] },
    { id: "ops", n: "Operasional", ic: "list-checks", ag: ["Pengurus Pesanan", "Penyusun Jadwal Tim", "Pengecek Stok", "Penyusun Ringkasan Pagi"] },
    { id: "adm", n: "Admin & Keuangan", ic: "wallet", ag: ["Pembuat Tagihan", "Pengingat Bayar", "Pencatat Pengeluaran", "Pencocok Mutasi", "Penyusun Laporan"] },
    { id: "ana", n: "Analis", ic: "search", ag: ["Peneliti Klien", "Pemantau Pesaing", "Peringkas Ulasan"] },
  ];
  const MAP = mk(`<div id="map"><svg class="lines" viewBox="0 0 960 520"></svg><div id="cring"></div><div id="cnode"></div></div>`);
  const MSVG = MAP.querySelector("svg"), CNODE = $("cnode"), CRING = $("cring");
  const CLAUDE_N = spr3("claude", 140, 6, 6, CNODE);
  const CX = 480, CY = 260, RX = 330, RY = 195;
  const NS = "http://www.w3.org/2000/svg";
  const PILLS = DEPTS.map((d, k) => {
    const a = (-115.7 + k * 360 / 7) * Math.PI / 180, x = CX + RX * Math.cos(a), y = CY + RY * Math.sin(a);
    const el = mk(`<div class="dp"><span class="ic">${ico(d.ic)}</span>${d.n}</div>`, MAP);
    const w = el.offsetWidth, h = 54; el.style.left = (x - w / 2) + "px"; el.style.top = (y - h / 2) + "px";
    const path = document.createElementNS(NS, "path"); const mx = (CX + x) / 2 + (y - CY) * 0.12, my = (CY + y) / 2 - (x - CX) * 0.12;
    path.setAttribute("d", `M${CX} ${CY} Q${mx.toFixed(1)} ${my.toFixed(1)} ${x.toFixed(1)} ${y.toFixed(1)}`); path.setAttribute("fill", "none"); path.setAttribute("stroke", "#294b77"); path.setAttribute("stroke-width", "3"); path.setAttribute("stroke-linecap", "round");
    MSVG.appendChild(path); const len = path.getTotalLength(); path.style.strokeDasharray = len; path.style.strokeDashoffset = len;
    const dx = Math.cos(a), dy = Math.sin(a), ext = Math.abs(dx) * w / 2 + Math.abs(dy) * 27 + 40;
    const dots = d.ag.map((nm, j) => {
      const m = j - (d.ag.length - 1) / 2, px = x + dx * (ext - Math.abs(m) * 6) - dy * m * 34, py = y + dy * (ext - Math.abs(m) * 6) + dx * m * 34;
      const ln = document.createElementNS(NS, "line"); ln.setAttribute("x1", x + dx * (ext - 30)); ln.setAttribute("y1", y + dy * (ext - 30)); ln.setAttribute("x2", px); ln.setAttribute("y2", py);
      ln.setAttribute("stroke", "rgba(41,75,119,.35)"); ln.setAttribute("stroke-width", "2"); MSVG.appendChild(ln);
      const el2 = mk(`<div class="ad" style="left:${px.toFixed(1)}px;top:${py.toFixed(1)}px"></div>`, MAP);
      return { el: el2, ln, x: px, y: py, nm };
    });
    return { el, path, len, x, y, w, dots, a };
  });
  const ALLDOTS = PILLS.flatMap((p) => p.dots);
  // counter chip + stamp (hook)
  const C30 = mk(`<div class="pill" style="left:0;top:0"><b id="c30n">0</b>&nbsp;agent</div>`, MAP); const C30N = $("c30n");
  C30.style.left = (CX - 105) + "px"; C30.style.top = (CY + 92) + "px";
  const GRAT = mk(`<div class="stamp">PETANYA GRATIS</div>`, MAP); GRAT.style.left = (CX - GRAT.offsetWidth / 2) + "px"; GRAT.style.top = (CY - 168) + "px";
  const C7 = mk(`<div class="pill"><b>7</b>&nbsp;departemen</div>`, MAP); C7.style.left = (CX - C7.offsetWidth / 2) + "px"; C7.style.top = (CY + 92) + "px";
  // hook times
  const H = { node: 0.15, lines: 0.45, pills: 0.6, dots: 1.0, count: wt(9) - 0.05, gratis: wt(14) - 0.06 };
  ev(H.node, "pop", 0); ev(H.lines, "whoosh", -2, 1.3); for (let k = 0; k < 7; k++) ev(H.pills + k * 0.08, "pop", -6, 1 + k * 0.04);
  ev(H.dots + 0.1, "sparkle", -4); for (let k = 0; k < 10; k++) ev(H.count + k * 0.075, "click", -8, 1.2 + k * 0.03); ev(H.gratis, "impact", -4);
  // dept growth (s4)
  const G4 = { grow: wt(37) - 0.1, seven: wt(38) - 0.05 };
  for (let k = 0; k < 7; k++) ev(G4.grow + k * 0.07, "pop", -6, 0.9 + k * 0.05); ev(G4.seven, "ping", -3);
  // one-task (s12)
  const OT = { back: T.s12, dots: T.s12 + 0.25, one: wt(97) - 0.08 };
  ev(OT.back, "whoosh", -3, 0.9); for (let k = 0; k < 8; k++) ev(OT.dots + k * 0.05, "click", -10, 1.3); ev(OT.one, "pop", 0);
  const PB = PILLS[5].dots[1];   // "Pengingat Bayar"

  function map(t) {
    let o = 0, s = 1, y = 0, b = 0;
    const showMap = (t < T.s2 + 0.4) || (t > T.s3 && t < T.s5 + 0.4) || (t > T.s12 - 0.05 && t < T.s13 + 0.4);
    if (!showMap) { hide(MAP); return; }
    if (t < T.s3) {   // hook
      o = 1 - eio(t, T.s2 - 0.05, T.s2 + 0.3); s = L(0.96, 1.03, eio(t, 0, T.s2)) * (1 - 0.7 * ei(t, T.s2 - 0.05, T.s2 + 0.32)); b = 6 * lin(t, T.s2, T.s2 + 0.3);
    } else if (t < T.s12 - 0.05) {   // s3/s4: centre node first, then the departments grow
      o = 1; s = L(0.98, 1.02, lin(t, T.s3, T.s5));
      if (t > T.s5 - 0.05) o = 1 - eo(t, T.s5 + 0.05, T.s5 + 0.3);
    } else {   // s12
      o = eo(t, T.s12 + 0.1, T.s12 + 0.35) * (1 - eo(t, T.s12b - 0.02, T.s12b + 0.3)); s = L(1.0, 1.03, lin(t, T.s12, T.s13));
    }
    S(MAP, { o, s, y, b });
    // centre node
    let no = 0, ns = 1;
    if (t < T.s3) { no = eo(t, H.node, H.node + 0.2); ns = spr(t, H.node, 15, 0.6); }
    else if (t < T.s12) { no = t >= MORPH_N ? 1 : 0; ns = 1 + 0.12 * Math.max(0, Math.sin(Math.PI * lin(t, ABSORB + 0.05, ABSORB + 0.45))); }
    else { no = 1; ns = 1; }
    S(CNODE, { o: no, s: ns }); frame(CLAUDE_N, wob(t, 0, 28) + 360 * eio(t, H.node, H.node + 0.9));
    S(CRING, { o: 0.5 * (1 - lin((t * 0.8) % 1, 0, 1)) * no, s: 1 + 0.5 * ((t * 0.8) % 1) });
    // pills + lines
    PILLS.forEach((p, k) => {
      let pt, po = 1, lp;
      if (t < T.s3) { pt = H.pills + k * 0.08; lp = eio(t, H.lines + k * 0.06, H.lines + k * 0.06 + 0.45); }
      else if (t < T.s12) { pt = G4.grow + k * 0.07 + 0.12; lp = eio(t, G4.grow + k * 0.07, G4.grow + k * 0.07 + 0.3); }
      else { pt = -1; lp = 1; }
      const u = pt < 0 ? 1 : spr(t, pt, 16, 0.62);
      let px = 0, py = 0;
      if (t > T.s3 && t < T.s12) { const g = eo(t, pt - 0.12, pt + 0.28); px = (CX - p.x) * (1 - g); py = (CY - p.y) * (1 - g); }
      if (t > T.s4 && t < T.s5 + 0.4 && k === 0) po = 1 - lin(t, T.s5, T.s5 + 0.06);   // the Penjualan pill becomes the card (morph)
      if (t > T.s12 && t < T.s12 + 0.4 && k === 6) po = lin(t, T.s12 + 0.28, T.s12 + 0.34);   // the Analis card lands back as its pill
      let dim = 1; if (t > OT.one) dim = 1 - 0.65 * eo(t, OT.one, OT.one + 0.25);
      S(p.el, { o: (u > 0 ? Math.min(1, u * 3) : 0) * po * dim, s: 0.6 + 0.4 * u, x: px, y: py });
      p.path.style.strokeDashoffset = (p.len * (1 - lp)).toFixed(1); p.path.style.opacity = (t > OT.one ? dim : 1);
      // agent dots (hook + one-task only)
      p.dots.forEach((d, j) => {
        const gi = ALLDOTS.indexOf(d);
        let dt0 = t < T.s3 ? H.dots + gi * 0.022 : t > T.s12 ? OT.dots + gi * 0.012 : 1e9;
        const du = spr(t, dt0, 18, 0.55);
        let lit = t < T.s3 ? lin(t, H.count + gi * 0.024, H.count + gi * 0.024 + 0.05) * (1 - lin(t, T.s2 - 0.2, T.s2)) : 0;
        let dd = 1; if (t > OT.one && d !== PB) dd = 1 - 0.7 * eo(t, OT.one, OT.one + 0.25);
        if (d === PB && t > OT.one) { S(d.el, { o: 1 - lin(t, OT.one + 0.05, OT.one + 0.12), s: 1 + 2 * eo(t, OT.one, OT.one + 0.12) }); }
        else S(d.el, { o: Math.min(1, du * 2) * dd, s: du * (1 + 0.35 * lit) });
        d.el.style.background = lit > 0.5 ? "#2f6bff" : "#294b77";
        d.ln.style.opacity = (Math.min(1, du * 2) * dd).toFixed(2);
      });
    });
    // hook chips
    const cu = spr(t, H.count, 16, 0.6), cOut = 1 - eo(t, T.s2 - 0.1, T.s2 + 0.15);
    S(C30, { o: Math.min(1, cu * 2) * cOut * (t < T.s3 ? 1 : 0), s: 0.7 + 0.3 * cu });
    C30N.textContent = String(Math.round(30 * eio(t, H.count, H.count + 0.75)));
    const gu = spr(t, H.gratis, 22, 0.5);
    S(GRAT, { o: Math.min(1, gu * 3) * cOut * (t < T.s3 ? 1 : 0), s: 1.6 - 0.6 * gu, r: -6 });
    const su = spr(t, G4.seven, 16, 0.6);
    S(C7, { o: t > T.s3 && t < T.s12 ? Math.min(1, su * 2) * (1 - lin(t, T.s5, T.s5 + 0.15)) : 0, s: 0.7 + 0.3 * su });
  }

  // ================================================================== INPUTS (s2) -> ring around Claude (s3)
  const INP = [["whatsapp", "WhatsApp", 23], ["instagram", "Instagram", 24], ["shopping-bag", "Marketplace", 25], ["googlesheets", "Google Sheets", 26], ["googlecalendar", "Kalender", 28], ["gmail", "Email", 29]];
  const INCARD = mk(`<div class="card" style="left:90px;top:620px;width:900px;height:470px"><div class="lbl" style="position:absolute;left:36px;top:30px">Yang udah kamu pakai</div><div class="demo" style="right:30px;top:24px">INPUT</div></div>`);
  const TILES = INP.map(([n, lab, wi], i) => {
    const c = i % 3, r = Math.floor(i / 3), x = 245 + c * 295, y = 790 + r * 195;
    const el = mk(`<div class="tile" style="left:${x}px;top:${y}px"><div class="slot"></div><div class="nm">${lab}</div></div>`);
    let lg; if (ICO[n]) { lg = mk(`<div class="ico-l">${ico(n, "#fff", 2)}</div>`, el); } else lg = spr3(n, 120, 55, 4, el);
    const ang = (-90 + i * 60) * Math.PI / 180;
    return { el, lg, slot: el.querySelector(".slot"), nm: el.querySelector(".nm"), x, y, w: wt(wi), rx: 540 + 385 * Math.cos(ang), ry: 860 + 215 * Math.sin(ang) };
  });
  const TG = TILES.map((tl) => ghosts(tl.el));
  const REC = mk(`<div id="rec"><div class="bar"><i></i><i></i><i></i><span>claude.ai</span><em>REKAMAN ASLI</em></div><img src="assets/rec/claude_home.jpg" alt="" /></div>`);
  const INSVG = mk(`<svg style="position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920"></svg>`);
  const RD = TILES.map((tl) => {
    const ln = document.createElementNS(NS, "line"); ln.setAttribute("x1", tl.rx); ln.setAttribute("y1", tl.ry); ln.setAttribute("x2", 540); ln.setAttribute("y2", 860);
    ln.setAttribute("stroke", "#294b77"); ln.setAttribute("stroke-width", "3"); ln.setAttribute("stroke-dasharray", "8 12"); ln.setAttribute("stroke-linecap", "round"); INSVG.appendChild(ln);
    const dot = document.createElementNS(NS, "circle"); dot.setAttribute("r", "8"); dot.setAttribute("fill", "#2f6bff"); INSVG.appendChild(dot); return { ln, dot, tl };
  });
  const MORPH_N = wt(33) - 0.1 + 0.32;   // "membaca": the claude.ai window collapses into the map's centre node
  const ABSORB = wt(34) - 0.1;            // "semuanya": the input tiles fly into the node
  ev(T.s2 + 0.05, "whoosh", -3, 1.1); TILES.forEach((tl, i) => { ev(T.s2 + 0.15 + i * 0.06, "click", -10, 1.3); ev(tl.w, "pop", -1, 0.95 + i * 0.04); });
  ev(T.s3, "whoosh", -2, 0.8); ev(T.s3 + 0.1, "pop", -4); ev(MORPH_N - 0.32, "whoosh", -4, 1.4); ev(MORPH_N, "ping", -3); ev(ABSORB + 0.25, "sparkle", -2);
  function inputs(t) {
    if (t < T.s2 - 0.1 || t > T.s4 + 0.3) { hide(INCARD); TILES.forEach((tl, i) => { hide(tl.el); hide(TG[i][0]); hide(TG[i][1]); }); hide(REC); hide(INSVG); return; }
    const cu = spr(t, T.s2, 15, 0.7);
    S(INCARD, { o: Math.min(1, cu * 2) * (1 - eo(t, T.s3 - 0.02, T.s3 + 0.2)), y: 80 * (1 - cu), s: 0.95 + 0.05 * cu });
    TILES.forEach((tl, i) => {
      const su = spr(t, T.s2 + 0.15 + i * 0.06, 16, 0.65), lu = spr(t, tl.w - 0.06, 18, 0.5);
      tl.slot.style.opacity = (1 - lin(t, tl.w - 0.06, tl.w + 0.1)).toFixed(2);
      S(tl.lg, { o: Math.min(1, lu * 3), s: lu, y: 20 * (1 - lu) });
      if (tl.lg.classList.contains("spr")) frame(tl.lg, 360 * eo(t, tl.w - 0.06, tl.w + 0.7) + wob(t, i, 20));
      S(tl.nm, { o: lin(t, tl.w, tl.w + 0.15) * (1 - lin(t, T.s3 - 0.05, T.s3 + 0.06)) });
      const fly = (tt) => {
        const g = eio(tt, T.s3 + i * 0.03, T.s3 + 0.42 + i * 0.03), ab = ei(tt, ABSORB + i * 0.04, ABSORB + 0.3 + i * 0.04);
        const x = L(0, tl.rx - tl.x, g) + (540 - tl.rx) * ab, y = L(0, tl.ry - tl.y, g) + (860 - tl.ry) * ab;
        return { x, y, s: Math.min(1, su * 1.0) * L(1, 0.78, g) * (1 - 0.8 * ab), o: Math.min(1, su * 3) * (1 - lin(tt, ABSORB + 0.2 + i * 0.04, ABSORB + 0.32 + i * 0.04)) };
      };
      mb(tl.el, TG[i], fly, t);
    });
    // claude.ai window (client's real recording) -> collapses into the centre node
    const ru = spr(t, T.s3 + 0.08, 15, 0.7), m = eio(t, MORPH_N - 0.32, MORPH_N);
    S(REC, { o: Math.min(1, ru * 2) * (1 - lin(t, MORPH_N - 0.08, MORPH_N)), s: (0.85 + 0.15 * ru) * L(1, 0.27, m), y: 40 * (1 - ru) + L(0, 860 - (740 + 125), m) * 0 });
    REC.style.borderRadius = L(22, 140, m).toFixed(1) + "px";
    // reading lines + travelling dots
    const ro = lin(t, MORPH_N - 0.1, MORPH_N + 0.15) * (1 - lin(t, ABSORB + 0.05, ABSORB + 0.3));
    S(INSVG, { o: ro });
    RD.forEach((r, i) => { r.ln.setAttribute("stroke-dashoffset", (-t * 60).toFixed(1)); const u = ((t * 1.4 + i * 0.17) % 1); r.dot.setAttribute("cx", L(r.tl.rx, 540, u)); r.dot.setAttribute("cy", L(r.tl.ry, 860, u)); r.dot.setAttribute("opacity", Math.sin(Math.PI * u).toFixed(2)); });
  }

  // ================================================================== DEPARTMENT CARDS (s5..s11)
  const mm = (k) => { let s = `<svg class="mm" viewBox="0 0 84 84"><circle cx="42" cy="42" r="9" fill="#294b77"/>`; for (let j = 0; j < 7; j++) { const a = (-115.7 + j * 360 / 7) * Math.PI / 180, x = 42 + 31 * Math.cos(a), y = 42 + 31 * Math.sin(a); s += `<line x1="42" y1="42" x2="${x.toFixed(1)}" y2="${y.toFixed(1)}" stroke="rgba(41,75,119,.25)" stroke-width="2"/><circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${j === k ? 9 : 5.5}" fill="${j === k ? "#2f6bff" : "rgba(41,75,119,.35)"}"/>`; } return s + "</svg>"; };
  const DC = DEPTS.map((d, k) => {
    const el = mk(`<div class="dc"><div class="card bg"></div><div class="dcin"><div class="hd"><span class="ic">${ico(d.ic)}</span><span class="t">${d.n}</span><span class="c">${d.ag.length} agent</span></div>${mm(k)}<div class="chips">${d.ag.map((a) => `<span class="chip">${a}</span>`).join("")}</div><div class="wg"></div></div></div>`);
    return { el, bg: el.querySelector(".bg"), inn: el.querySelector(".dcin"), chips: [...el.querySelectorAll(".chip")], wg: el.querySelector(".wg") };
  });
  // scene windows + enter/exit styles (never the same motion twice in a row)
  const DS = [
    { a: T.s5, b: T.s6, in: "morph", out: "whipL" }, { a: T.s6, b: T.s7, in: "whipL", out: "flip" }, { a: T.s7, b: T.s8, in: "flip", out: "zoom" },
    { a: T.s8, b: T.s9, in: "zoom", out: "whipR" }, { a: T.s9, b: T.s10, in: "whipR", out: "drop" }, { a: T.s10, b: T.s11, in: "rise", out: "flip" },
    { a: T.s11, b: T.s12, in: "flip", out: "morph" },
  ];
  DS.forEach((s, k) => { ev(s.a, k === 0 ? "whoosh" : "whoosh", -1, [0.9, 1.3, 1.0, 1.15, 0.85, 1.2, 1.05][k]); ev(s.a + 0.28, "pop", -8, 1.1); });
  const PR = { x: 60 + PILLS[0].x - PILLS[0].w / 2, y: 600 + PILLS[0].y - 27, w: PILLS[0].w, h: 54 };   // Penjualan pill (global)
  const PA = { x: 60 + PILLS[6].x - PILLS[6].w / 2, y: 600 + PILLS[6].y - 27, w: PILLS[6].w, h: 54 };   // Analis pill (global)
  function deptCard(t, k) {
    const c = DC[k], s = DS[k];
    if (t < s.a - 0.05 || t > s.b + 0.45) { hide(c.el); return false; }
    let p = { o: 1 }, bgRect = null, content = 1;
    // enter
    const ia = s.a;
    if (s.in === "morph") { const m = eio(t, ia, ia + 0.36); bgRect = [L(PR.x, 90, m), L(PR.y, 600, m), L(PR.w, 900, m), L(PR.h, 520, m), L(27, 30, m)]; content = lin(t, ia + 0.28, ia + 0.45); }
    if (s.in === "whipL") { const u = spr(t, ia, 15, 0.72), v = Math.abs(spr(t + 1 / 60, ia, 15, 0.72) - u) * 60 * 1150; p = { x: 1150 * (1 - u), b: Math.min(12, v / 350) }; }
    if (s.in === "whipR") { const u = spr(t, ia, 15, 0.72), v = Math.abs(spr(t + 1 / 60, ia, 15, 0.72) - u) * 60 * 1150; p = { x: -1150 * (1 - u), b: Math.min(12, v / 350) }; }
    if (s.in === "flip") { const u = eo(t, ia + 0.12, ia + 0.42); p = { ry: -90 * (1 - u), o: lin(t, ia + 0.12, ia + 0.16) }; }
    if (s.in === "zoom") { const u = spr(t, ia + 0.05, 15, 0.7); p = { s: 0.8 + 0.2 * u, o: Math.min(1, u * 2.5) }; }
    if (s.in === "rise") { const u = spr(t, ia + 0.05, 14, 0.7); p = { y: 60 * (1 - u), o: Math.min(1, u * 2.5) }; }
    // exit
    const oa = s.b;
    if (t > oa - 0.08) {
      if (s.out === "whipL") { const u = ei(t, oa - 0.08, oa + 0.24); p = { x: -1150 * u, b: 12 * u }; }
      if (s.out === "whipR") { const u = ei(t, oa - 0.08, oa + 0.24); p = { x: 1150 * u, b: 12 * u }; }
      if (s.out === "flip") { const u = ei(t, oa - 0.08, oa + 0.12); p = { ry: 90 * u, o: 1 - lin(t, oa + 0.08, oa + 0.12) }; }
      if (s.out === "zoom") { const u = eo(t, oa - 0.08, oa + 0.2); p = { s: 1 + 0.25 * u, o: 1 - u, b: 6 * u }; }
      if (s.out === "drop") { const u = eo(t, oa - 0.08, oa + 0.22); p = { s: 1 - 0.08 * u, y: 16 * u, o: 1 - u }; }
      if (s.out === "morph") { const m = eio(t, oa, oa + 0.34); bgRect = [L(90, PA.x, m), L(600, PA.y, m), L(900, PA.w, m), L(520, PA.h, m), L(30, 27, m)]; content = 1 - lin(t, oa, oa + 0.1); p = { o: 1 - lin(t, oa + 0.3, oa + 0.36) }; }
    }
    S(c.el, p);
    if (bgRect) { const [x, y, w, h, r] = bgRect; Object.assign(c.bg.style, { left: (x - 90) + "px", top: (y - 600) + "px", width: w + "px", height: h + "px", borderRadius: r + "px" }); }
    else Object.assign(c.bg.style, { left: "0px", top: "0px", width: "900px", height: "520px", borderRadius: "30px" });
    S(c.inn, { o: content });
    return true;
  }
  function chipsOn(k, t, list) {   // list: [[time, chipIndex], ...] -> the active chip at time t
    let a = -1; for (const [tt, i] of list) if (t >= tt) a = i;
    DC[k].chips.forEach((ch, i) => { const on = i === a; if (ch.classList.contains("on") !== on) ch.classList.toggle("on", on); S(ch, { s: on ? 1 + 0.08 * Math.max(0, Math.sin(Math.PI * lin(t, list.find((x) => x[1] === i)?.[0] ?? 0, (list.find((x) => x[1] === i)?.[0] ?? 0) + 0.25))) : 1 }); });
  }
  const typed = (s, t, a, b) => s.slice(0, Math.round(s.length * lin(t, a, b)));
  const W = (k, html) => mk(html, DC[k].wg);
  const DEMO = (k) => W(k, `<div class="demo" style="right:0;top:-48px">CONTOH</div>`);
  DEPTS.forEach((d, k) => DEMO(k));
  const tickSvg = ico("check", "#fff", 3);

  // --- Penjualan (s5): search prospects, then first chat + appointment
  const P5 = { q: W(0, `<div class="row" style="top:0"><span class="ico-l">${ico("search", "#294b77")}</span><span id="p5q"></span><span class="s" id="p5c">|</span></div>`),
    r: [["Kantor konsultan", "40 orang"], ["Klinik gigi", "12 orang"], ["Coworking space", "60 orang"]].map(([a, b], i) => W(0, `<div class="row" style="top:${86 + i * 62}px;height:54px;font-size:24px"><span class="ico-l" style="width:38px;height:38px">${ico("users", "#294b77")}</span>${a}<span class="s">· ${b}</span><span class="tag">calon pembeli</span></div>`)),
    bub: W(0, `<div class="bub" style="left:0;top:0;width:500px"><small>CHAT PERTAMA</small><span id="p5b"></span></div>`),
    cal: W(0, `<div class="mini" style="left:540px;top:0;width:296px;height:250px"><div class="lbl" style="position:absolute;left:20px;top:20px;font-size:18px">Janji temu</div>${["Rab 14.00", "Kam 10.00", "Jum 09.00"].map((s, i) => `<div class="row p5s" style="left:16px;top:${56 + i * 62}px;width:264px;height:52px;font-size:23px;padding:0 14px">${s}<span class="tag" style="opacity:0">${tickSvg}</span></div>`).join("")}</div>`) };
  const P5Q = $("p5q"), P5B = $("p5b"), P5S = [...P5.cal.querySelectorAll(".p5s")];
  const Q5 = "kantor butuh katering harian", B5 = "Halo! Kami katering harian untuk kantor. Boleh kami kirim menu contoh minggu ini?";
  const t5 = { type: wt(41) - 0.2, rows: [wt(42), wt(43) - 0.05, wt(43) + 0.18], chat: wt(44) - 0.05, cal: wt(47) - 0.1, book: wt(48) };
  ev(t5.type, "type", -10); t5.rows.forEach((x) => ev(x, "pop", -5, 1.1)); ev(t5.chat + 0.85, "send", -3); ev(t5.cal, "pop", -6); ev(t5.book + 0.05, "ping", -2);
  function s5(t) {
    if (!deptCard(t, 0)) return;
    chipsOn(0, t, [[wt(40), 0], [wt(44) - 0.1, 2], [wt(47) - 0.1, 3]]);
    const A = t < T.s5b + 0.05, ao = 1 - lin(t, T.s5b - 0.05, T.s5b + 0.12);
    S(P5.q, { o: ao }); P5Q.textContent = typed(Q5, t, t5.type, t5.type + 0.6); S($("p5c"), { o: Math.floor(t * 4) % 2 ? 1 : 0.2 });
    P5.r.forEach((r, i) => { const u = spr(t, t5.rows[i], 17, 0.65); S(r, { o: Math.min(1, u * 2.5) * ao, x: 60 * (1 - u) }); });
    const bu = spr(t, t5.chat, 15, 0.65); S(P5.bub, { o: A ? 0 : Math.min(1, bu * 2.5), y: 30 * (1 - bu), s: 0.9 + 0.1 * bu }); P5B.textContent = typed(B5, t, t5.chat + 0.1, t5.chat + 0.85);
    const cu = spr(t, t5.cal, 15, 0.65); S(P5.cal, { o: A ? 0 : Math.min(1, cu * 2.5), x: 40 * (1 - cu) });
    P5S.forEach((r, i) => { const on = i === 1 && t >= t5.book; r.style.background = on ? "#294b77" : "#f4f7fc"; r.style.color = on ? "#fff" : "#0a0d2c"; S(r.querySelector(".tag"), { o: on ? 1 : 0, s: on ? spr(t, t5.book, 20, 0.5) : 1 }); });
  }
  // --- Closing (s6): proposal, then follow-ups until an answer
  const P6 = { doc: W(1, `<div class="mini" style="left:0;top:0;width:500px;height:250px"><div style="position:absolute;left:24px;top:22px;display:flex;align-items:center;gap:14px;font:700 26px/1 Poppins"><span class="ico-l" style="width:54px;height:54px">${ico("file-text", "#294b77")}</span>Penawaran_katering.pdf</div>${[0, 1, 2, 3].map((i) => `<div class="p6l" style="position:absolute;left:24px;top:${104 + i * 30}px;height:14px;border-radius:7px;background:rgba(41,75,119,.16);width:${[430, 380, 410, 260][i]}px;transform-origin:0 50%"></div>`).join("")}</div>`),
    sent: W(1, `<div class="stamp" style="left:560px;top:84px">TERKIRIM</div>`),
    fu: [["H+1", "Menu contohnya sudah sampai, kak?"], ["H+3", "Mau dijadwalkan tes rasa minggu ini?"]].map(([a, b], i) => W(1, `<div class="bub" style="left:0;top:${i * 92}px;width:560px;padding:12px 20px;font-size:24px"><small>FOLLOW-UP · ${a}</small>${b}</div>`)),
    rep: W(1, `<div class="bub in" style="left:236px;top:190px;width:600px;padding:12px 20px;font-size:24px"><small style="color:#294b77">JAWABAN MASUK</small>Boleh, Kamis kami coba dulu ya.</div>`) };
  const P6L = [...P6.doc.querySelectorAll(".p6l")];
  const t6 = { doc: T.s6 + 0.15, sent: wt(52) + 0.2, fu: [wt(54) - 0.05, wt(55) + 0.15], rep: wt(57) - 0.05 };
  ev(t6.doc + 0.3, "type", -11); ev(t6.sent, "impact", -6); t6.fu.forEach((x) => ev(x, "send", -6)); ev(t6.rep, "ping", -1);
  function s6(t) {
    if (!deptCard(t, 1)) return;
    chipsOn(1, t, [[wt(50), 0], [wt(53) - 0.1, 1]]);
    const ao = 1 - lin(t, T.s6b - 0.05, T.s6b + 0.12), A = t < T.s6b + 0.05;
    S(P6.doc, { o: ao * lin(t, t6.doc, t6.doc + 0.15), y: -8 * eio(t, t6.sent - 0.3, t6.sent) });
    P6L.forEach((l, i) => S(l, { sx: eo(t, t6.doc + 0.2 + i * 0.12, t6.doc + 0.45 + i * 0.12) }));
    const su = spr(t, t6.sent, 22, 0.5); S(P6.sent, { o: Math.min(1, su * 3) * ao, s: 1.5 - 0.5 * su, r: -5 });
    P6.fu.forEach((f, i) => { const u = spr(t, t6.fu[i], 16, 0.65); S(f, { o: A ? 0 : Math.min(1, u * 2.5), y: 26 * (1 - u) }); });
    const ru = spr(t, t6.rep, 16, 0.6); S(P6.rep, { o: A ? 0 : Math.min(1, ru * 2.5), s: 0.85 + 0.15 * ru, y: 20 * (1 - ru) });
  }
  // --- Marketing (s7): post written, comments answered (drafts)
  const P7 = { post: W(2, `<div class="mini" style="left:0;top:0;width:360px;height:264px;overflow:hidden"><div style="position:absolute;left:0;top:0;width:360px;height:120px;background:linear-gradient(135deg,#13307e,#2f6bff);display:grid;place-items:center">${ico("image", "rgba(255,255,255,.8)", 1.6).replace("<svg", '<svg style="width:64px;height:64px"')}</div><div style="position:absolute;left:18px;top:134px;width:324px;font:400 23px/1.35 Poppins;color:#0a0d2c" id="p7c"></div></div>`),
    cm: [["Bisa buat 30 orang?", "Bisa, kak! Menu lengkapnya kami kirim via DM."], ["Ada menu vegetarian?", "Ada, kak. Tiap hari ada 2 pilihan."]].map(([q, a], i) => [W(2, `<div class="bub in" style="left:384px;top:${i * 132}px;width:452px;padding:10px 18px;font-size:22px"><small style="color:#294b77">KOMENTAR</small>${q}</div>`), W(2, `<div class="bub" style="left:420px;top:${i * 132 + 72}px;width:416px;padding:8px 16px;font-size:21px">${a}</div>`)]) };
  const P7C = $("p7c"), C7T = "Menu sehat minggu ini, siap antar ke kantor.";
  const t7 = { cap: wt(59) - 0.05, q: [wt(61) - 0.15, wt(61) + 0.1], a: [wt(62), wt(63) + 0.2] };
  ev(t7.cap, "type", -10); t7.q.forEach((x) => ev(x, "pop", -6)); t7.a.forEach((x) => ev(x, "send", -6));
  function s7(t) {
    if (!deptCard(t, 2)) return;
    chipsOn(2, t, [[wt(58), 1], [wt(61) - 0.1, 2]]);
    const pu = spr(t, T.s7 + 0.3, 15, 0.7); S(P7.post, { o: Math.min(1, pu * 2.5), y: 30 * (1 - pu) }); P7C.textContent = typed(C7T, t, t7.cap, t7.cap + 0.7);
    P7.cm.forEach(([q, a], i) => { const u = spr(t, t7.q[i], 16, 0.65), v = spr(t, t7.a[i], 16, 0.65); S(q, { o: Math.min(1, u * 2.5), x: 40 * (1 - u) }); S(a, { o: Math.min(1, v * 2.5), x: 40 * (1 - v) }); });
  }
  // --- CS (s8): chats answered, a quiet customer flagged
  const P8 = { r: [["Pesanan besok bisa jam 11?", 0], ["Ada paket untuk 50 orang?", 1], ["Bisa bayar transfer?", 2]].map(([q], i) => W(3, `<div class="row" style="top:${i * 64}px;height:56px;font-size:23px"><span class="ico-l" style="width:38px;height:38px">${ico("message-circle", "#294b77")}</span>${q}<span class="tag">${tickSvg}dijawab</span></div>`)),
    q: W(3, `<div class="row" style="top:200px;height:62px;font-size:23px;background:#fff;box-shadow:0 0 0 3px #294b77"><span class="ico-l" style="width:40px;height:40px">${ico("user", "#294b77")}</span>Kantor arsitek<span class="s">· terakhir pesan 30 hari lalu</span><span class="tag">${ico("flag", "#fff", 2.4)}mulai menghilang</span></div>`) };
  const t8 = { r: [wt(65) - 0.05, wt(65) + 0.2, wt(66)], ok: [wt(66) - 0.05, wt(66) + 0.15, wt(66) + 0.35], q: wt(67), flag: wt(70) - 0.05 };
  t8.ok.forEach((x) => ev(x, "click", -6, 1.2)); ev(t8.q, "pop", -5); ev(t8.flag, "impact", -6);
  function s8(t) {
    if (!deptCard(t, 3)) return;
    chipsOn(3, t, [[wt(64), 0], [wt(67) - 0.1, 2]]);
    P8.r.forEach((r, i) => { const u = spr(t, t8.r[i], 17, 0.65); S(r, { o: Math.min(1, u * 2.5), x: 50 * (1 - u) }); S(r.querySelector(".tag"), { o: lin(t, t8.ok[i], t8.ok[i] + 0.08), s: 0.6 + 0.4 * spr(t, t8.ok[i], 20, 0.5) }); });
    const qu = spr(t, t8.q, 16, 0.65); S(P8.q, { o: Math.min(1, qu * 2.5), y: 30 * (1 - qu) }); S(P8.q.querySelector(".tag"), { o: lin(t, t8.flag, t8.flag + 0.08), s: 1.4 - 0.4 * spr(t, t8.flag, 22, 0.5) });
  }
  // --- Operasional (s9): orders move across a board, team schedule fills
  const P9 = { cols: ["Baru", "Dimasak", "Dikirim"].map((n, i) => W(4, `<div class="mini" style="left:${i * 286}px;top:0;width:264px;height:160px;background:#f4f7fc"><div class="lbl" style="position:absolute;left:18px;top:16px;font-size:18px">${n}</div></div>`)),
    ord: ["Order #21 · 40 porsi", "Order #22 · 12 porsi"].map((n) => W(4, `<div class="mini" style="left:12px;top:48px;width:240px;height:46px;display:flex;align-items:center;padding:0 14px;font:700 21px/1 Poppins;color:#0a0d2c">${n}</div>`)),
    sch: W(4, `<div style="position:absolute;left:0;top:184px;width:836px;height:76px;display:flex;gap:10px">${["Sen", "Sel", "Rab", "Kam", "Jum"].map((d) => `<div class="mini p9d" style="position:relative;flex:1;height:76px;display:flex;align-items:center;gap:8px;padding:0 14px;font:700 22px/1 Poppins;color:#294b77">${d}<i style="width:22px;height:22px;border-radius:50%;background:#294b77;display:block;margin-left:auto"></i><i style="width:22px;height:22px;border-radius:50%;background:#2f6bff;display:block"></i></div>`).join("")}</div>`) };
  const P9D = [...P9.sch.querySelectorAll(".p9d")];
  const t9 = { ord: wt(72) - 0.1, m1: wt(73), m2: wt(73) + 0.35, sch: wt(75) - 0.1 };
  ev(t9.ord, "pop", -5); ev(t9.m1, "whoosh", -10, 1.6); ev(t9.m2, "whoosh", -10, 1.7); for (let i = 0; i < 5; i++) ev(t9.sch + i * 0.08, "click", -9, 1.2 + i * 0.05);
  function s9(t) {
    if (!deptCard(t, 4)) return;
    chipsOn(4, t, [[wt(71), 0], [wt(75) - 0.1, 1]]);
    P9.cols.forEach((c, i) => S(c, { o: lin(t, T.s9 + 0.2 + i * 0.05, T.s9 + 0.35 + i * 0.05) }));
    P9.ord.forEach((o, i) => { const u = spr(t, t9.ord + i * 0.12, 17, 0.65); const mv = eio(t, t9.m1 + i * 0.1, t9.m1 + 0.3 + i * 0.1) + (i === 0 ? eio(t, t9.m2, t9.m2 + 0.3) : 0); S(o, { o: Math.min(1, u * 2.5), x: 286 * mv, y: i * 54 - (i && mv > 0 ? 54 * Math.min(1, mv) : 0) }); });
    P9D.forEach((d, i) => { const u = spr(t, t9.sch + i * 0.08, 17, 0.6); S(d, { o: Math.min(1, u * 2.5), y: 20 * (1 - u) }); });
  }
  // --- Admin & Keuangan (s10): invoice sent, reminder drafted for the unpaid one
  const P10 = { inv: W(5, `<div class="mini" style="left:0;top:0;width:520px;height:250px"><div style="position:absolute;left:24px;top:22px;font:700 28px/1 Poppins;color:#0a0d2c">Tagihan INV-0117</div><div style="position:absolute;left:24px;top:66px;font:400 23px/1 Poppins;color:#294b77">Kantor konsultan · katering Mei</div>${[0, 1, 2].map((i) => `<div class="p10l" style="position:absolute;left:24px;top:${112 + i * 30}px;height:14px;border-radius:7px;background:rgba(41,75,119,.16);width:${[420, 360, 300][i]}px;transform-origin:0 50%"></div>`).join("")}<div style="position:absolute;right:24px;bottom:20px;font:700 26px/1 Poppins;color:#13307e">Rp 4.800.000</div></div>`),
    sent: W(5, `<div class="stamp" style="left:560px;top:84px">TERKIRIM</div>`),
    due: W(5, `<div class="row" style="top:0;height:62px;font-size:23px"><span class="ico-l" style="width:40px;height:40px">${ico("clock", "#294b77")}</span>INV-0109<span class="s">· jatuh tempo 3 hari lalu</span><span class="tag">belum bayar</span></div>`),
    rem: W(5, `<div class="bub" style="left:120px;top:94px;width:716px;font-size:24px"><small>DRAF PENGINGAT · PENGINGAT BAYAR</small><span id="p10r"></span></div>`) };
  const P10L = [...P10.inv.querySelectorAll(".p10l")], P10R = $("p10r");
  const R10 = "Halo, Kak. Sekadar mengingatkan tagihan INV-0109 ya. Terima kasih!";
  const t10 = { inv: T.s10 + 0.2, sent: wt(81) - 0.05, due: wt(82) - 0.05, rem: wt(83) - 0.1 };
  ev(t10.inv + 0.3, "type", -11); ev(t10.sent, "impact", -6); ev(t10.due, "pop", -5); ev(t10.rem, "type", -10);
  function s10(t) {
    if (!deptCard(t, 5)) return;
    chipsOn(5, t, [[wt(77), 0], [wt(82) - 0.1, 1]]);
    const ao = 1 - lin(t, T.s10b - 0.05, T.s10b + 0.12), A = t < T.s10b + 0.05;
    S(P10.inv, { o: ao * lin(t, t10.inv, t10.inv + 0.15), y: -8 * eio(t, t10.sent - 0.3, t10.sent) });
    P10L.forEach((l, i) => S(l, { sx: eo(t, t10.inv + 0.2 + i * 0.15, t10.inv + 0.5 + i * 0.15) }));
    const su = spr(t, t10.sent, 22, 0.5); S(P10.sent, { o: Math.min(1, su * 3) * ao, s: 1.5 - 0.5 * su, r: -5 });
    const du = spr(t, t10.due, 17, 0.65); S(P10.due, { o: A ? 0 : Math.min(1, du * 2.5), x: 40 * (1 - du) });
    const ru = spr(t, t10.rem, 15, 0.65); S(P10.rem, { o: A ? 0 : Math.min(1, ru * 2.5), y: 26 * (1 - ru) }); P10R.textContent = typed(R10, t, t10.rem + 0.08, t10.rem + 0.7);
  }
  // --- Analis (s11): client brief before the meeting
  const P11 = { hd: W(6, `<div class="row" style="top:0;height:64px;background:#fff;box-shadow:0 0 0 2px rgba(41,75,119,.16)"><span class="ico-l" style="width:42px;height:42px">${ico("user", "#294b77")}</span>Kantor konsultan<span class="s">· ketemu Kamis 10.00</span></div>`),
    li: ["40 orang, makan siang bareng tiap Jumat", "Butuh pilihan menu vegetarian", "Sumber: website & ulasan publik"].map((s, i) => W(6, `<div style="position:absolute;left:12px;top:${84 + i * 50}px;display:flex;align-items:center;gap:14px;font:400 25px/1 Poppins;color:#0a0d2c;white-space:nowrap"><i style="width:12px;height:12px;border-radius:50%;background:#294b77;display:block"></i>${s}</div>`)),
    ok: W(6, `<div class="stamp" style="left:470px;top:226px;font-size:24px;padding:8px 16px">SIAP SEBELUM KETEMU</div>`) };
  const t11 = { hd: wt(87) - 0.05, li: [wt(88), wt(89) + 0.1, wt(90) + 0.05], ok: wt(92) - 0.05 };
  ev(t11.hd, "pop", -5); t11.li.forEach((x) => ev(x, "click", -7, 1.1)); ev(t11.ok, "impact", -6);
  function s11(t) {
    if (!deptCard(t, 6)) return;
    chipsOn(6, t, [[wt(86), 0]]);
    const hu = spr(t, t11.hd, 16, 0.65); S(P11.hd, { o: Math.min(1, hu * 2.5), y: 20 * (1 - hu) });
    P11.li.forEach((l, i) => { const u = spr(t, t11.li[i], 17, 0.65); S(l, { o: Math.min(1, u * 2.5), x: 40 * (1 - u) }); });
    const ou = spr(t, t11.ok, 22, 0.5); S(P11.ok, { o: Math.min(1, ou * 3), s: 1.4 - 0.4 * ou, r: -4 });
  }

  // ================================================================== ONE TASK (s12): dot -> task card -> workflow doc
  const TASK = mk(`<div class="card" style="left:240px;top:790px;width:600px;height:150px"><div style="position:absolute;left:28px;top:26px;display:flex;align-items:center;gap:16px"><span class="ic" style="width:56px;height:56px">${ico("wallet")}</span><span style="font:700 32px/1 Poppins">Pengingat Bayar</span></div><div style="position:absolute;left:28px;top:98px;font:400 25px/1 Poppins;color:#294b77"><b style="color:#13307e">1 tugas:</b> ingetin yang belum bayar</div></div>`);
  const FLOW = mk(`<div class="card" style="left:90px;top:610px;width:900px;height:500px"><div class="lbl" style="position:absolute;left:36px;top:32px">Alur kerja · Pengingat Bayar</div><div class="demo" style="right:30px;top:24px">CONTOH</div></div>`);
  const STEPS = ["Cek Google Sheets: tagihan lewat jatuh tempo", "Tulis pengingat yang sopan", "Kirim ke kamu untuk disetujui", "Setelah oke: kirim, lalu catat statusnya"].map((s, i) =>
    mk(`<div style="position:absolute;left:36px;top:${92 + i * 96}px;width:828px;height:80px;display:flex;align-items:center;gap:18px;padding:0 20px;border-radius:18px;background:#f4f7fc;font:700 26px/1.1 Poppins;color:#0a0d2c;white-space:nowrap"><span class="ic" style="width:46px;height:46px;border-radius:23px;font:700 22px/1 Poppins;color:#fff">${i + 1}</span><span class="tx"></span><span class="ck" style="margin-left:auto;width:40px;height:40px;border-radius:12px;background:#294b77;display:grid;place-items:center">${tickSvg.replace("<svg", '<svg style="width:24px;height:24px"')}</span></div>`, FLOW));
  const STX = STEPS.map((s) => s.querySelector(".tx")), SCK = STEPS.map((s) => s.querySelector(".ck"));
  const STT = ["Cek Google Sheets: tagihan lewat jatuh tempo", "Tulis pengingat yang sopan", "Kirim ke kamu untuk disetujui", "Setelah oke: kirim, lalu catat statusnya"];
  const t12 = { task: OT.one + 0.05, flow: T.s12b, st: [wt(99) - 0.05, wt(100) - 0.22, wt(100) + 0.1, wt(101) - 0.18] };
  ev(t12.flow, "whoosh", -4, 1.2); t12.st.forEach((x, i) => { ev(x, "type", -12); ev(x + 0.42, "click", -6, 1.2); });
  function s12(t) {
    if (t < T.s12 || t > T.s13 + 0.4) { hide(TASK); hide(FLOW); return; }
    const tu = spr(t, t12.task, 15, 0.65), fm = eio(t, t12.flow, t12.flow + 0.36);
    // the dot grows into the task card (shared element), then the card opens into the workflow doc
    const dx = 60 + PB.x - 540, dy = 600 + PB.y - 865;
    S(TASK, { o: Math.min(1, tu * 3) * (1 - lin(t, t12.flow + 0.2, t12.flow + 0.3)), x: dx * (1 - tu) + L(0, -150, fm) * 0, y: dy * (1 - tu) - 0 * fm, s: (0.05 + 0.95 * tu) * L(1, 1.5, fm) });
    S(FLOW, { o: lin(t, t12.flow + 0.15, t12.flow + 0.3) * (1 - eo(t, T.s13 - 0.05, T.s13 + 0.25)), s: L(0.66, 1, fm), y: -30 * (1 - fm) + 40 * ei(t, T.s13 - 0.05, T.s13 + 0.25) });
    STEPS.forEach((st, i) => { const u = spr(t, t12.st[i], 17, 0.65); S(st, { o: Math.min(1, u * 2.5), x: 40 * (1 - u) }); STX[i].textContent = typed(STT[i], t, t12.st[i], t12.st[i] + 0.34); S(SCK[i], { o: lin(t, t12.st[i] + 0.42, t12.st[i] + 0.5), s: 0.6 + 0.4 * spr(t, t12.st[i] + 0.42, 20, 0.5) }); });
  }

  // ================================================================== APPROVAL (s13)
  const AG = mk(`<div class="card" style="left:90px;top:640px;width:410px;height:190px"><div style="position:absolute;left:24px;top:22px;display:flex;align-items:center;gap:14px"><span class="ic" style="width:50px;height:50px">${ico("bot")}</span><span style="font:700 26px/1 Poppins">Pengingat Bayar</span></div><div style="position:absolute;left:24px;top:92px;width:362px;font:400 22px/1.35 Poppins;color:#294b77">Draf: "Halo, Kak. Sekadar mengingatkan tagihan INV-0109 ya…"</div></div>`);
  const CU = mk(`<div class="card" style="left:770px;top:640px;width:220px;height:190px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px"><span class="ico-l" style="width:76px;height:76px;border-radius:38px">${ico("user", "#294b77", 2)}</span><span style="font:700 26px/1 Poppins">Pelanggan</span><span id="cuok" style="position:absolute;bottom:-58px;font:700 22px/1 Poppins;color:#fff;padding:9px 14px;border-radius:12px;background:#294b77;white-space:nowrap">Terkirim ✓</span></div>`);
  const GATE = mk(`<div style="position:absolute;left:590px;top:620px;width:110px;height:230px"><div style="position:absolute;left:47px;top:0;width:16px;height:230px;border-radius:8px;background:linear-gradient(180deg,#13307e,#294b77)"></div><div id="lockc" class="ic" style="position:absolute;left:19px;top:79px;width:72px;height:72px;border-radius:36px;box-shadow:0 0 0 6px #fff"><span id="lk1" style="position:absolute;inset:0;display:grid;place-items:center">${ico("lock", "#fff", 2.2).replace("<svg", '<svg style="width:38px;height:38px"')}</span><span id="lk2" style="position:absolute;inset:0;display:grid;place-items:center">${ico("lock-open", "#fff", 2.2).replace("<svg", '<svg style="width:38px;height:38px"')}</span></div></div>`);
  const WAITL = mk(`<div class="demo" style="left:470px;top:874px;font-size:20px">NUNGGU PERSETUJUANMU</div>`);
  const MSG = mk(`<div class="bub" style="left:420px;top:700px;width:150px;padding:14px 18px;text-align:center"><svg viewBox="0 0 24 24" style="width:40px;height:40px" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">${ICO["mail"]}</svg></div>`);
  const MG = ghosts(MSG);
  const APP = mk(`<div class="card" style="left:240px;top:930px;width:600px;height:170px"><div style="position:absolute;left:26px;top:24px;display:flex;align-items:center;gap:14px"><span class="ico-l" style="width:46px;height:46px;border-radius:23px">${ico("user", "#294b77")}</span><span style="font:700 26px/1 Poppins">Kamu · persetujuan</span></div><div style="position:absolute;left:26px;top:96px;display:flex;gap:16px"><span style="font:700 26px/1 Poppins;color:#294b77;padding:14px 26px;border-radius:16px;background:rgba(41,75,119,.09)">Ubah</span><span id="apok" style="font:700 26px/1 Poppins;color:#fff;padding:14px 30px;border-radius:16px;background:linear-gradient(100deg,#13307e,#2f6bff);box-shadow:0 10px 20px rgba(19,48,126,.3)">Setujui</span></div></div>`);
  const CUR = mk(`<svg class="cur" viewBox="0 0 24 24"><path d="M4 2.5l15.5 9.2-6.6 1.6 3.9 7.1-3 1.6-3.9-7.2-5 4.5z" fill="#0a0d2c" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/></svg>`);
  const AOK = (() => { const r = $("apok").getBoundingClientRect(); return [r.left + r.width * 0.45, r.top + r.height * 0.55]; })();
  const t13 = { in: T.s13 + 0.2, go: wt(105) - 0.35, hit: wt(105) + 0.05, app: T.s13b + 0.02, cur: T.s13b + 0.2, press: wt(110) - 0.08, open: wt(110) + 0.08, pass: wt(110) + 0.12 };
  ev(t13.in, "whoosh", -3, 1.0); ev(t13.go, "whoosh", -9, 1.5); ev(t13.hit, "thud", -3); ev(t13.app, "pop", -3); ev(t13.press, "click", 0); ev(t13.open, "ping", -2); ev(t13.pass + 0.3, "sparkle", -4);
  const msgPose = (tt) => {
    const go = eio(tt, t13.go, t13.hit), back = Math.sin(Math.PI * lin(tt, t13.hit, t13.hit + 0.22)) * 0.06, pass = eio(tt, t13.pass, t13.pass + 0.35);
    const x = L(0, 120, go) - 120 * back + L(0, 330, pass);
    return { x, y: -20 * Math.sin(Math.PI * pass), o: lin(tt, t13.go - 0.15, t13.go) * (1 - lin(tt, t13.pass + 0.3, t13.pass + 0.38)), s: 1 - 0.3 * lin(tt, t13.pass + 0.2, t13.pass + 0.38) };
  };
  function s13(t) {
    const on = t > T.s13 - 0.05 && t < T.s14 + 0.4;
    if (!on) { [AG, CU, GATE, WAITL, MSG, APP, CUR, MG[0], MG[1]].forEach(hide); return; }
    const out = 1 - eo(t, T.s14 - 0.05, T.s14 + 0.2);
    const u = spr(t, t13.in, 15, 0.7); S(AG, { o: Math.min(1, u * 2.5) * out, x: -60 * (1 - u) }); S(CU, { o: Math.min(1, u * 2.5) * out, x: 60 * (1 - u) });
    const gu = spr(t, t13.in + 0.12, 16, 0.6); S(GATE, { o: Math.min(1, gu * 2.5) * out, sy: 0.4 + 0.6 * gu });
    S($("lockc"), { x: 6 * Math.sin(t * 60) * Math.exp(-8 * Math.max(0, t - t13.hit)) * (t > t13.hit ? 1 : 0), s: 1 + 0.15 * Math.sin(Math.PI * lin(t, t13.open, t13.open + 0.25)) });
    S($("lk1"), { o: 1 - lin(t, t13.open, t13.open + 0.05) }); S($("lk2"), { o: lin(t, t13.open, t13.open + 0.05) });
    S(WAITL, { o: lin(t, t13.hit, t13.hit + 0.15) * (1 - lin(t, t13.open, t13.open + 0.15)) * out });
    mb(MSG, MG, (tt) => { const p = msgPose(tt); p.o *= out; return p; }, t);
    S($("cuok"), { o: lin(t, t13.pass + 0.35, t13.pass + 0.45) * out, s: 0.7 + 0.3 * spr(t, t13.pass + 0.35, 20, 0.5) });
    const au = spr(t, t13.app, 15, 0.7); S(APP, { o: Math.min(1, au * 2.5) * out, y: 60 * (1 - au) });
    const pr = lin(t, t13.press, t13.press + 0.07) * (1 - lin(t, t13.press + 0.15, t13.press + 0.22));
    S($("apok"), { s: 1 - 0.08 * pr });
    // cursor: glides in (0.6 s), arrives early, presses ~0.17 s, rests, fades
    const g = eio(t, t13.cur, t13.cur + 0.6), cx = L(1010, AOK[0] - 6, g), cy = L(1300, AOK[1] - 4, g);
    S(CUR, { o: lin(t, t13.cur, t13.cur + 0.1) * (1 - lin(t, t13.pass + 0.3, t13.pass + 0.5)) * out, x: cx, y: cy, s: 1.15 - 0.17 * pr });
  }

  // ================================================================== MORNING PAGE (s14)
  const PAGE = mk(`<div class="card" style="left:110px;top:620px;width:860px;height:490px"><div style="position:absolute;left:32px;top:28px;display:flex;align-items:center;gap:16px"><span class="ic" style="width:58px;height:58px">${ico("sunrise")}</span><span style="font:700 34px/1 Poppins">Ringkasan pagi</span></div><div style="position:absolute;right:32px;top:44px;font:700 24px/1 Poppins;color:#294b77">Senin · 07.00</div><div class="demo" style="right:32px;top:84px">CONTOH</div></div>`);
  const SEC = [["Beres", ["Chat pelanggan dijawab", "Penawaran kantor konsultan terkirim", "Tagihan INV-0117 terkirim"]], ["Nunggu kamu", ["Setujui pengingat INV-0109", "Cek draf balasan komentar"]]];
  const PR14 = [];
  SEC.forEach(([h, rows], si) => {
    const y0 = si ? 316 : 116, hd = mk(`<div class="lbl" style="position:absolute;left:34px;top:${y0}px">${h}</div>`, PAGE); PR14.push([hd, si, -1]);
    rows.forEach((r, i) => PR14.push([mk(`<div style="position:absolute;left:32px;top:${y0 + 34 + i * 52}px;display:flex;align-items:center;gap:14px;font:700 25px/1 Poppins;color:#0a0d2c;white-space:nowrap"><span style="width:34px;height:34px;border-radius:10px;display:grid;place-items:center;background:${si ? "rgba(41,75,119,.12)" : "#294b77"}">${si ? ico("clock", "#294b77", 2.4).replace("<svg", '<svg style="width:20px;height:20px"') : tickSvg.replace("<svg", '<svg style="width:20px;height:20px"')}</span>${r}${si ? '<span style="margin-left:18px;font:700 20px/1 Poppins;color:#fff;padding:7px 12px;border-radius:10px;background:linear-gradient(100deg,#13307e,#2f6bff)">Buka</span>' : ""}</div>`, PAGE), si, i]));
  });
  const SK = [0, 1, 2, 3, 4].map((i) => mk(`<div style="position:absolute;left:34px;top:${136 + i * 62}px;height:18px;border-radius:9px;background:rgba(41,75,119,.12);width:${[620, 520, 580, 460, 540][i]}px;transform-origin:0 50%"></div>`, PAGE));
  const t14 = { in: T.s14 + 0.03, h0: wt(117) - 0.1, r0: [wt(119) - 0.08, wt(119) + 0.12, wt(119) + 0.32], h1: wt(120) - 0.1, r1: [wt(122) - 0.05, wt(122) + 0.2] };
  ev(t14.in, "whoosh", -2, 0.8); ev(wt(116) - 0.05, "pop", -6); t14.r0.forEach((x) => ev(x, "click", -6, 1.15)); t14.r1.forEach((x) => ev(x, "pop", -6, 1.05));
  function s14(t) {
    if (t < T.s14 - 0.05 || t > T.s15 + 0.5) { hide(PAGE); return; }
    const u = spr(t, t14.in, 13, 0.72), f = eio(t, T.s15, T.s15 + 0.4);
    S(PAGE, { o: Math.min(1, u * 2.5) * (1 - lin(t, T.s15 + 0.16, T.s15 + 0.3)), y: 420 * (1 - u) + L(0, -40, f), s: L(1, 0.62, f) });
    SK.forEach((k, i) => S(k, { sx: eo(t, t14.in + 0.35 + i * 0.12, t14.in + 0.7 + i * 0.12), o: 1 - lin(t, t14.h0 - 0.1, t14.h0 + 0.1) }));
    PR14.forEach(([el, si, i]) => { const t0 = i < 0 ? (si ? t14.h1 : t14.h0) : (si ? t14.r1[i] : t14.r0[i]); const v = spr(t, t0, 17, 0.65); S(el, { o: Math.min(1, v * 2.5), x: 30 * (1 - v) }); });
  }

  // ================================================================== CTA (s15): the map doc, pill button, DM
  const DOC = mk(`<div class="card" style="left:240px;top:650px;width:600px;height:320px"><div style="position:absolute;left:30px;top:28px;display:flex;align-items:center;gap:14px"><span class="ic" style="width:52px;height:52px">${ico("layers")}</span><span style="font:700 32px/1 Poppins">Peta AI agent</span></div>${mm(-1).replace('class="mm"', 'style="position:absolute;right:28px;top:22px;width:110px;height:110px"')}<div style="position:absolute;left:32px;top:104px;font:400 26px/1.55 Poppins;color:#0a0d2c">7 departemen · 30 agent<br/>tugas + alur kerja tiap agent<br/>aturan "kamu setuju dulu"</div><div id="dmok" style="position:absolute;left:30px;bottom:22px;display:flex;align-items:center;gap:10px;font:700 24px/1 Poppins;color:#fff;padding:10px 16px;border-radius:12px;background:#294b77">${ico("send", "#fff", 2.2).replace("<svg", '<svg style="width:24px;height:24px"')}dikirim lewat DM</div></div>`);
  const CTAB = mk(`<div id="ctab">${ico("message-circle", "#fff", 2.2)}<span>Komen PETA</span></div>`);
  const t15 = { doc: T.s15 + 0.05, pill: wt(124) - 0.05, press: wt(125) - 0.02, dm: wt(127) - 0.05 };
  ev(t15.doc, "riser", -6); ev(t15.pill + 0.05, "impact", -3); ev(t15.press, "click", 0); ev(t15.dm, "send", -2); ev(t15.dm + 0.1, "sparkle", -3);
  function s15(t) {
    if (t < T.s15) { hide(DOC); hide(CTAB); return; }
    const u = spr(t, t15.doc + 0.22, 15, 0.7); S(DOC, { o: Math.min(1, u * 2.5), s: 0.85 + 0.15 * u });
    const pu = spr(t, t15.pill, 15, 0.55), pr = lin(t, t15.press, t15.press + 0.08) * (1 - lin(t, t15.press + 0.16, t15.press + 0.26));
    const breathe = t > t15.press + 0.4 ? 0.025 * Math.sin((t - t15.press) * 5) : 0;
    S(CTAB, { o: Math.min(1, pu * 2.5), y: 80 * (1 - pu), s: (0.8 + 0.2 * pu) * (1 - 0.07 * pr + breathe) });
    S($("dmok"), { o: lin(t, t15.dm, t15.dm + 0.1), s: 0.7 + 0.3 * spr(t, t15.dm, 20, 0.5) });
  }

  // ================================================================== render
  const LOGO = $("brandlogo"), GR = $("grain");
  function render(t) {
    t = Math.max(0, Math.min(D, t));
    particles(t); headline(t); counter(t);
    S(LOGO, { o: 1 }); S(GR, { x: 64 * ((t * 7.3) % 1), y: 40 * ((t * 5.1) % 1), o: 0.05 });
    map(t); inputs(t); s5(t); s6(t); s7(t); s8(t); s9(t); s10(t); s11(t); s12(t); s13(t); s14(t); s15(t);
  }
  return render;
  }
  // ------------------------------------------------------------------ timeline + seek hooks
  let R = null, lastT = 0;
  const tl = window.__timelines["main"];
  tl.eventCallback("onUpdate", () => { lastT = tl.time(); if (R) R(lastT); });
  window.addEventListener("hf-seek", (e) => { lastT = e.detail.time; if (R) R(lastT); });
  // preload sprites / recording before the first frame
  const imgs = ["claude", "whatsapp", "instagram", "googlesheets", "googlecalendar", "gmail"].map((n) => `assets/logos3d/${n}.png`).concat(["assets/rec/claude_home.jpg"]);
  window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {};
  const fonts = ["700 24px Poppins", "400 24px Poppins", "italic 700 62px Poppins"].map((f) => document.fonts.load(f));
  window.__hf.buildReady.ui = Promise.all(imgs.map((s) => new Promise((res) => { const i = new Image(); i.onload = i.onerror = () => res(); i.src = s; })).concat(fonts)).then(() => { R = BUILD(); window.R36_render = R; R(lastT); });
})();

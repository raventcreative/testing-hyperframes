/* R39 · "Colibri: model AI raksasa di PC sendiri" — every frame is a pure function of t (render(t) on hf-seek).
   Batch-10 staging (client 2026-11-28): explaining beats = the 3D mascot comes forward half-body under the spoken headline
   (vendor/mascot_host.js reads window.STAGE); example/demo beats = mascot fully hidden, the example gets the whole frame (big
   cards). No beat counter. No voxel world, no robot.
   Look: spoken headline on top (the VO line word by word, ONE emphasised word italic + cyan), brand navy plate, html-demo
   scripted windows (cursor, terminal, browser), shared elements (expert cubes around the mascot -> the model-map grid -> the SSD;
   the terminal URL -> the browser address bar), closed-form springs, velocity-proportional blur on fast moves, real 3D logos
   (Simple Icons, CC0, pre-rendered sprite strips). SFX events go to window.SFX_EVENTS (tools/sfx_events.cjs -> tools/sfx.py).
   Facts: only what github.com/JustVugg/colibri README states (see production/VO_SCRIPT.md). */
(function () {
  const OFF = 0.3, DUR = window.TOTAL, ICO = window.ICO;
  const LINES = window.R_LINES, WORDS = window.R_WORDS;
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
  function E(parent, css, html, cls) { const e = document.createElement("div"); if (cls) e.className = cls; if (css) e.style.cssText = css; if (!cls && !/position\s*:/.test(css || "")) e.style.position = "absolute"; if (html != null) e.innerHTML = html; parent.appendChild(e); return e; }
  const ico = (n, size = 28, col = "#ffffff", sw = 2) => `<svg width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="${col}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round">${ICO[n] || ""}</svg>`;
  const op = (e, v) => { e.style.opacity = cl(v).toFixed(3); };
  const tf = (e, x = 0, y = 0, s = 1, r = 0) => { e.style.transform = `translate(${x.toFixed(1)}px,${y.toFixed(1)}px) scale(${s.toFixed(4)}) rotate(${r.toFixed(2)}deg)`; };
  const pop = (e, u, a, f = 2.4) => { const p = spr(u - a, f, 0.55); op(e, cl(p * 3) * (u >= a ? 1 : 0)); tf(e, 0, 18 * (1 - p), 0.6 + 0.4 * p); return p; };
  function seg(parent, cls) { return E(parent, "", null, "line" + (cls ? " " + cls : "")); }
  function segSet(e, x1, y1, x2, y2, p = 1, o = 1) { const dx = x2 - x1, dy = y2 - y1, L = Math.hypot(dx, dy); e.style.left = x1 + "px"; e.style.top = y1 - 2 + "px"; e.style.width = (L * cl(p)).toFixed(1) + "px"; e.style.transform = `rotate(${Math.atan2(dy, dx)}rad)`; op(e, o); }
  const CUR = '<svg width="46" height="46" viewBox="0 0 24 24"><path d="M4 2l15 9.5-6.6 1.4 3.6 7.2-2.9 1.4-3.6-7.3L4 19z" fill="#ffffff" stroke="#0a0d2c" stroke-width="1.4" stroke-linejoin="round"/></svg>';
  function cursor(root) { return E(root, "", CUR, "cur"); }
  function glide(u, K) { if (u <= K[0][0]) return [K[0][1], K[0][2]]; for (let i = 1; i < K.length; i++) if (u <= K[i][0]) { const p = eio((u - K[i - 1][0]) / (K[i][0] - K[i - 1][0])); return [mix(K[i - 1][1], K[i][1], p), mix(K[i - 1][2], K[i][2], p)]; } const k = K[K.length - 1]; return [k[1], k[2]]; }
  function curSet(e, u, K, clicks = [], o = 1) { const [x, y] = glide(u, K); let s = 1; for (const c of clicks) s -= 0.16 * bump(u, c - 0.05, 0.2); tf(e, x - 8, y - 4, s); op(e, o); }
  function ripple(root) { return E(root, "position:absolute;width:20px;height:20px;border-radius:50%;border:3px solid #01ccf7;opacity:0", null); }
  function ripSet(e, u, c, x, y) { const p = lin(u, c, c + 0.45); const d = 20 + 100 * e3(p); e.style.left = x - d / 2 + "px"; e.style.top = y - d / 2 + "px"; e.style.width = e.style.height = d + "px"; op(e, p > 0 && p < 1 ? 0.9 * (1 - p) : 0); }
  const GRAD = "font-style:italic;background:linear-gradient(95deg,#b8f1ff,#01ccf7 55%,#0aa7d6);-webkit-background-clip:text;background-clip:text;color:transparent;padding-right:.12em";
  // 3D logo sprite (24 yaw frames, 220 px each; frames 18..23,0 = edge-on -> front, never the mirrored back side)
  function logo(parent, name, size, css = "") { const e = E(parent, `position:absolute;width:${size}px;height:${size}px;background:url(assets/logos/${name}_sheet.png) 0 0/${24 * size}px ${size}px no-repeat;${css}`, null); e.dataset.size = size; return e; }
  function logoSet(e, u, a, wob = 0) {   // spin in from edge-on at a (0.45 s), then a gentle wobble (frames 23/0/1)
    const s = +e.dataset.size, p = e3(lin(u, a, a + 0.45));
    let f = p < 1 ? Math.round(18 + 6 * p) % 24 : 0;
    if (p >= 1 && wob) { const w = Math.sin((u - a) * 2.2) * 1.4; f = (Math.round(w) + 24) % 24; }
    e.style.backgroundPosition = `${-f * s}px 0`; op(e, u >= a ? cl(p * 3) : 0); tf(e, 0, 20 * (1 - p), 0.7 + 0.3 * e3(lin(u, a, a + 0.35)));
  }
  // ------------------------------------------------------------------ lines / beats
  const L = []; { let k = 0; for (const txt of LINES) { const n = txt.split(/\s+/).length; const ws = WORDS.slice(k, k + n).map((w) => [w[0], w[1] + OFF, w[2] + OFF]); k += n; L.push({ txt, ws, t0: ws[0][1] }); } }
  L.forEach((l, i) => { l.t1 = i < L.length - 1 ? L[i + 1].t0 : DUR + 5; });
  const NL = L.length;
  const wt = (i, k) => L[i].ws[k][1];
  window.SFX_EVENTS = [];
  const fx = (t, n, db = 0, rate = 1) => window.SFX_EVENTS.push([+t.toFixed(3), n, db, rate]);
  // ------------------------------------------------------------------ staging: explaining beats (mascot forward, half-body)
  // a = mascot starts to come forward, b = mascot starts to leave (it is gone ~0.55 s later, before the next example lands)
  const EXPL = [[0], [4], [9], [17, 18]];
  window.STAGE = EXPL.map((g, n) => {
    const i0 = g[0], i1 = g[g.length - 1];
    const a = i0 === 0 ? 0.05 : L[i0].t0 - 0.2, b = i1 < NL - 1 ? L[i1 + 1].t0 - 0.74 : DUR + 9;
    const w = { a, b, head: [150, 150, 150, 240][n], h: [1380, 1380, 1380, 1280][n], fx: [540, 590, 590, 570][n], acts: [] };
    if (i1 === NL - 1) w.acts.push({ t: L[18].t0 - 0.12, action: "cta", side: "right" }, { t: wt(18, 12) - 0.2, action: "point", side: "left" });
    fx(a + 0.05, "whoosh", -4, 0.8); if (b < DUR) fx(b + 0.22, "pop", -5, 0.75);
    return w;
  });
  const mascotK = (t) => { const p = window.__mascotPose ? window.__mascotPose(t) : null; return p ? p.o : 0; };
  // ------------------------------------------------------------------ headlines
  const EMPH = { 0: [2], 1: [6], 2: [1], 3: [2], 4: [7, 8], 5: [3], 6: [6], 7: [4], 8: [11], 9: [7], 10: [7], 11: [4], 12: [5], 13: [2], 14: [7], 15: [6], 16: [5], 17: [6, 7], 18: [1] };
  const DISP = { 1: { 6: ["8 GB.", 2] }, 10: { 7: ["16 GB.", 3] }, 11: { 4: ["32 GB.", 4] }, 12: { 5: ["8 GB.", 2] } };   // number format only (VO says "delapan giga" …)
  const HL = L.map((l, i) => {
    const d = E($("heads"), "", null, "hl"); const ws = [];
    const n = l.txt.length; d.style.fontSize = (n <= 40 ? 70 : n <= 58 ? 64 : 58) + "px";
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
  // ------------------------------------------------------------------ cards (demo beats; one card may span several lines)
  const CX = 540, CY = 1075;
  const ENTER = { rise: (q) => ({ y: 170 * q, s: 1 - 0.08 * q }), drop: (q) => ({ y: -190 * q, s: 1 - 0.06 * q }), left: (q) => ({ x: 420 * q, r: 5 * q }), right: (q) => ({ x: -420 * q, r: -5 * q }),
    zoom: (q) => ({ s: 1 - 0.42 * q }), pop: (q) => ({ s: 1 + 0.22 * q }), flip: (q) => ({ rx: 70 * q, y: 50 * q }), swing: (q) => ({ ry: -55 * q, x: 90 * q }),
    tilt: (q) => ({ r: -9 * q, s: 1 - 0.22 * q, y: 60 * q }), unfold: (q) => ({ sy: 1 - 0.92 * q }) };
  const EXIT = { up: (p) => ({ y: -130 * p, s: 1 - 0.05 * p }), left: (p) => ({ x: -440 * p, r: -4 * p }), right: (p) => ({ x: 440 * p, r: 4 * p }), shrink: (p) => ({ s: 1 - 0.4 * p }),
    grow: (p) => ({ s: 1 + 0.3 * p }), down: (p) => ({ y: 170 * p }), flip: (p) => ({ rx: -70 * p }) };
  const C = [];
  function addCard(i0, i1, W, H, en, ex, build, cy = CY) {
    const root = E($("cards"), `left:${CX - W / 2}px;top:${cy - H / 2}px;width:${W}px;height:${H}px`, null, "card");
    const l = L[i0], w = (i, k) => L[i].ws[k][1] - l.t0, cfx = (u, n, db = 0, r = 1) => fx(l.t0 + u, n, db, r);
    const upd = build(root, w, cfx);
    const tin = l.t0 - 0.24, tout = i1 < NL - 1 ? L[i1 + 1].t0 - 0.26 : DUR + 5;
    const c = { root, W, H, cy, upd, tin, tout, en, ex, t0: l.t0 }; C.push(c);
    fx(tin + 0.04, "whoosh", -2, [0.9, 1.15, 1.3, 1.0, 1.2, 0.95, 1.1, 1.25][C.length % 8]); fx(tin + 0.24, "pop", -6, 0.9 + 0.05 * (C.length % 4));
    fx(tout + 0.06, "whoosh", -6, [1.35, 1.1, 1.5, 1.2][C.length % 4]);
    return c;
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
      const bl = v > 6 ? Math.min(9, (v - 6) * 0.12) : 0;
      c.root.style.transform = `perspective(1400px) translate(${S.x.toFixed(1)}px,${S.y.toFixed(1)}px) rotateX(${S.rx.toFixed(2)}deg) rotateY(${S.ry.toFixed(2)}deg) rotate(${S.r.toFixed(2)}deg) scale(${S.s.toFixed(4)},${(S.s * S.sy).toFixed(4)})`;
      op(c.root, S.o); c.root.style.filter = bl > 0.2 ? `blur(${bl.toFixed(2)}px)` : "none";
      c.upd(t - c.t0);
    }
  }
  const panel = (R, W, H) => E(R, `left:0;top:0;width:${W}px;height:${H}px`, null, "pn");
  // RAM module drawing (brand colours only)
  const RAMSVG = (w, h, chips = 8) => { let s = `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}"><defs><linearGradient id="rmg${w}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a4d96"/><stop offset="1" stop-color="#16306a"/></linearGradient></defs>` +
      `<path d="M8 6 H${w - 8} V${h - 30} H${w / 2 + 14} v-8 h-28 v8 H8 Z" rx="10" fill="url(#rmg${w})" stroke="#6adfff" stroke-width="3"/>`;
    const cw = (w - 60 - (chips - 1) * 14) / chips; for (let k = 0; k < chips; k++) s += `<rect x="${30 + k * (cw + 14)}" y="${h * 0.16}" width="${cw}" height="${h * 0.46}" rx="6" fill="#0a1033" stroke="rgba(1,204,247,.55)" stroke-width="2"/>`;
    for (let x = 22; x < w - 22; x += 14) s += `<rect x="${x}" y="${h - 26}" width="8" height="18" rx="2" fill="#01ccf7" opacity=".85"/>`;
    return s + "</svg>"; };
  const SSDSVG = (w, h) => `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}"><rect x="4" y="4" width="${w - 8}" height="${h - 8}" rx="18" fill="rgba(10,20,58,.75)" stroke="#6adfff" stroke-width="3"/><rect x="${w - 34}" y="${h / 2 - 40}" width="18" height="80" rx="4" fill="#01ccf7" opacity=".8"/><circle cx="28" cy="28" r="7" fill="#01ccf7"/></svg>`;
  const GPUSVG = (w, h) => `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}"><rect x="4" y="4" width="${w - 8}" height="${h - 24}" rx="18" fill="#16306a" stroke="#6adfff" stroke-width="3"/>` +
    [0.3, 0.7].map((f) => `<circle cx="${w * f}" cy="${(h - 20) / 2 + 2}" r="${(h - 20) * 0.32}" fill="#0a1033" stroke="rgba(1,204,247,.6)" stroke-width="3"/><path d="M${w * f} ${(h - 20) / 2 + 2 - (h - 20) * 0.25} v${(h - 20) * 0.5} M${w * f - (h - 20) * 0.25} ${(h - 20) / 2 + 2} h${(h - 20) * 0.5}" stroke="rgba(184,241,255,.5)" stroke-width="4" stroke-linecap="round"/>`).join("") +
    `<rect x="${w * 0.12}" y="${h - 22}" width="${w * 0.5}" height="16" rx="3" fill="#01ccf7" opacity=".85"/></svg>`;

  // ============ 1 · RAM minimal 8 GB (README: "8 GB of RAM at the very least (16 GB or more is better), 22 GB free on the disk")
  addCard(1, 1, 920, 720, "rise", "left", (R, w, f) => {
    panel(R, 920, 720);
    E(R, "left:44px;top:40px", "RAM minimal", "lb");
    const stick = E(R, "left:60px;top:96px;width:800px;height:220px", RAMSVG(800, 220, 8), "ic");
    const big = E(R, "left:60px;top:350px;font:700 150px/1 Poppins;letter-spacing:-4px;white-space:nowrap", "", "tb");
    const r1 = E(R, "left:470px;top:372px;display:flex;align-items:center;gap:12px;font-size:30px", ico("circle-check", 34, "#01ccf7", 2.4) + "16 GB ke atas: lebih lega", "tb");
    const r2 = E(R, "left:470px;top:440px;display:flex;align-items:center;gap:12px;font-size:30px", ico("hard-drive", 34, "#01ccf7", 2.2) + "disk kosong 22 GB", "tb");
    const r3 = E(R, "left:470px;top:490px;font-size:24px;color:rgba(220,236,255,.66)", "buat model paling kecil", "tx");
    const src = E(R, "left:44px;top:640px;font-size:22px;color:rgba(220,236,255,.55)", "sumber: README colibri", "tx");
    const N = w(1, 6), G = w(1, 7);
    f(N - 0.05, "ping", -6); f(G + 0.25, "pop", -7, 1.1); f(G + 0.55, "pop", -8, 1.2);
    return (u) => {
      const sp = spr(u - 0.0, 1.8, 0.7); tf(stick, 0, 30 * (1 - sp), 0.9 + 0.1 * sp); op(stick, cl(sp * 2));
      const n = Math.round(8 * e3(lin(u, N - 0.35, N + 0.15))); big.innerHTML = `${n} <span style="${GRAD}">GB</span>`; op(big, u > N - 0.4 ? 1 : 0);
      tf(big, 0, 0, 1 + 0.08 * bump(u, N + 0.1, 0.3));
      pop(r1, u, G + 0.2); pop(r2, u, G + 0.5); pop(r3, u, G + 0.6); op(src, e3(lin(u, G + 0.6, G + 1)) * 0.9);
    };
  });
  // ============ 2 · the repo: JustVugg/colibri · open source · Apache-2.0 · free · tiny C engine, immense model
  addCard(2, 2, 940, 760, "left", "flip", (R, w, f) => {
    panel(R, 940, 760);
    const gh = logo(R, "github", 110, "left:40px;top:40px");
    E(R, "left:170px;top:52px;font:400 34px/1 Poppins;color:rgba(220,236,255,.8);white-space:nowrap", "JustVugg /", "tx");
    E(R, "left:170px;top:96px;font:700 56px/1 Poppins;white-space:nowrap", "colibri", "tb");
    const TG = [["lock-open", "open source", w(2, 3)], ["scale", "Apache-2.0", w(2, 4)], ["badge-check", "gratis", w(2, 2)]].map(([ic, n, a], k) =>
      [E(R, `left:${[40, 330, 610][k]}px;top:190px`, ico(ic, 26, "#b8f1ff") + n, "cp"), a]);
    // tiny engine vs immense model
    const box = E(R, "left:40px;top:300px;width:860px;height:400px", null, "pn2");
    const eng = E(R, "left:80px;top:420px;width:210px;height:200px;border-radius:24px;border:2px solid rgba(1,204,247,.7);background:rgba(1,204,247,.1)", null);
    const cl3 = logo(eng, "c", 110, "left:50px;top:16px");
    E(eng, "left:0;top:134px;width:210px;text-align:center;font-size:26px", "mesin C", "tb");
    E(eng, "left:0;top:168px;width:210px;text-align:center;font-size:19px;color:rgba(220,236,255,.65);white-space:normal", "1 file per model", "tx");
    const mdl = E(R, "left:350px;top:330px;width:520px;height:340px;border-radius:26px;background:linear-gradient(150deg,rgba(1,204,247,.28),rgba(41,75,119,.55));border:2px solid rgba(184,241,255,.35);transform-origin:0 100%", null);
    const cells = []; for (let r = 0; r < 6; r++) for (let c = 0; c < 10; c++) cells.push(E(mdl, `position:absolute;left:${22 + c * 49}px;top:${22 + r * 40}px;width:40px;height:31px;border-radius:7px;background:rgba(184,241,255,.22)`, null));
    const mt = E(mdl, "left:24px;top:270px;font:700 34px/1 Poppins;white-space:nowrap", 'model <span style="' + GRAD + '">744B</span> parameter', "tb");
    const mt2 = E(mdl, "left:24px;top:308px;font-size:20px;color:rgba(220,236,255,.75)", "contoh: GLM-5.2", "tx");
    const ENG = w(2, 6) - 0.1, MOD = w(2, 7) - 0.05;
    TG.forEach(([, a]) => f(a + 0.05, "pop", -6, 1.15)); f(ENG + 0.05, "pop", -5, 0.9); f(MOD + 0.05, "whoosh", -7, 0.7);
    return (u) => {
      logoSet(gh, u, 0.15, 1);
      TG.forEach(([e, a]) => pop(e, u, a - 0.1));
      op(box, e3(lin(u, ENG - 0.4, ENG))); const pe = spr(u - ENG, 2.3, 0.55); op(eng, cl(pe * 3) * (u > ENG ? 1 : 0)); tf(eng, 0, 0, 0.5 + 0.5 * pe); logoSet(cl3, u, ENG + 0.05);
      const pm = spr(u - MOD, 1.6, 0.7); op(mdl, u > MOD ? cl(pm * 3) : 0); mdl.style.transform = `scale(${(0.25 + 0.75 * pm).toFixed(3)})`;
      cells.forEach((c, k) => { const on = ((k * 7 + Math.floor(u * 5)) % 23) < 2; c.style.background = on ? "rgba(1,204,247,.9)" : "rgba(184,241,255,.22)"; });
      op(mt2, e3(lin(u, MOD + 0.3, MOD + 0.6)));
    };
  });
  // ============ 3 · GPU optional (README: "No GPU needed … A GPU is a faster place to keep weights, not a requirement")
  addCard(3, 3, 900, 640, "flip", "shrink", (R, w, f) => {
    panel(R, 900, 640);
    E(R, "left:44px;top:40px", "kartu grafis (GPU)", "lb");
    const gpu = E(R, "left:44px;top:96px;width:430px;height:220px", GPUSVG(430, 220), "ic");
    const tr = E(R, "position:absolute;left:560px;top:150px;width:150px;height:78px;border-radius:39px;background:#01ccf7", null);
    const kn = E(tr, "position:absolute;left:6px;top:6px;width:66px;height:66px;border-radius:50%;background:#ffffff;box-shadow:0 4px 10px rgba(0,0,0,.3)", null);
    const tl = E(R, "left:560px;top:246px;font-size:30px", "opsional", "tb");
    const row = E(R, "left:44px;top:370px;width:812px;height:120px", null, "pn2");
    E(row, "left:24px;top:22px;width:76px;height:76px", ico("cpu", 46, "#b8f1ff"), "node");
    E(row, "left:124px;top:26px;font-size:34px", "Jalan di CPU aja", "tb");
    E(row, "left:124px;top:72px;font-size:22px;color:rgba(220,236,255,.7)", "tanpa install apa-apa lagi", "tx");
    const ck = E(row, "left:716px;top:28px;width:64px;height:64px", ico("circle-check", 60, "#01ccf7", 2.4), "ic");
    const note = E(R, "left:44px;top:530px;font-size:28px;white-space:nowrap", 'GPU cuma bikin <span style="' + GRAD + '">lebih cepat</span>, bukan syarat', "tb");
    const OP = w(3, 2) - 0.05, NW = w(3, 3);
    f(OP + 0.05, "click", -3, 0.9); f(NW + 0.1, "ping", -7); f(NW + 0.45, "pop", -7);
    return (u) => {
      const p = spr(u - OP, 2.6, 0.6); kn.style.transform = `translateX(${(72 * (1 - p)).toFixed(1)}px)`; tr.style.background = p > 0.5 ? "rgba(255,255,255,.16)" : "#01ccf7";
      op(gpu, 1 - 0.55 * e3(lin(u, OP, OP + 0.4))); gpu.style.filter = u > OP ? `saturate(${(1 - 0.6 * e3(lin(u, OP, OP + 0.4))).toFixed(2)})` : "none";
      op(tl, e3(lin(u, OP + 0.05, OP + 0.3))); pop(ck, u, NW); op(note, e3(lin(u, NW + 0.35, NW + 0.7)));
    };
  });
  // ============ 5-8 · the model map (ONE card over four lines; the grid becomes the SSD, the core goes to RAM, hot experts cache)
  const MAP = addCard(5, 8, 960, 880, "zoom", "down", (R, w, f) => {
    panel(R, 960, 880);
    const ttl = E(R, "left:44px;top:36px", "1 model · banyak ahli kecil", "lb");
    // RAM (top-left) + GPU (top-right)
    const ram = E(R, "left:40px;top:84px;width:610px;height:220px", RAMSVG(610, 220, 0), "ic");
    const ramL = E(R, "left:58px;top:58px", ico("memory-stick", 22, "#0a0d2c") + "RAM", "cp on");
    const core = E(R, "left:150px;top:116px;width:660px;height:64px;border-radius:16px;background:linear-gradient(90deg,#6adfff,#01ccf7);box-shadow:0 0 24px rgba(1,204,247,.45);display:flex;align-items:center;justify-content:center;font:700 26px/1 Poppins;color:#0a0d2c;white-space:nowrap", "inti model · selalu kepakai", null);
    const gpu = E(R, "left:690px;top:84px;width:230px;height:220px", GPUSVG(230, 150), "ic");
    const gpuL = E(R, "left:704px;top:58px", ico("zap", 22, "#b8f1ff") + "GPU (opsional)", "cp");
    // SSD (bottom)
    const ssd = E(R, "left:40px;top:560px;width:880px;height:270px", SSDSVG(880, 270), "ic");
    const ssdL = E(R, "left:58px;top:532px", ico("hard-drive", 22, "#0a0d2c") + "SSD", "cp on");
    // the token ("kata") + router lines + speed bar
    const tok = E(R, "left:0;top:0", "kata", "cp on");
    const LN = [0, 1].map(() => seg(R, "dash"));
    const spd = E(R, "left:360px;top:420px;width:540px;height:70px;display:flex;align-items:center;gap:14px", null);
    E(spd, "position:relative", ico("gauge", 34, "#b8f1ff"), "ic"); E(spd, "position:relative;font-size:24px", "kecepatan", "tx");
    const tr = E(spd, "position:relative;width:300px;height:18px", null, "bar"); const fill = E(tr, "left:0;top:0;width:300px;height:18px;transform-origin:0 50%", null, "bar acc");
    // 40 experts: grid A (8x5, big) -> SSD layout (14 per row, 3 rows)
    const N = 40, cells = [];
    for (let k = 0; k < N; k++) cells.push(E(R, "position:absolute;left:0;top:0;width:80px;height:80px;border-radius:14px;background:rgba(184,241,255,.16);border:2px solid rgba(184,241,255,.28);transform-origin:0 0", null));
    const A = (k) => [104 + (k % 8) * 96, 280 + Math.floor(k / 8) * 96, 80];
    const B = (k) => [107 + (k % 14) * 54, 610 + Math.floor(k / 14) * 56, 44];
    // RAM cache slots (6) + GPU slots (2): hot experts fly up from the SSD
    const SLOT = [0, 1, 2, 3, 4, 5].map((k) => [80 + k * 90, 210, 60]).concat([[730, 120, 60], [810, 120, 60]]);
    const HOT = [[9, 23.62, 0], [30, 23.62, 1], [16, 24.25, 2], [37, 26.62, 3], [4, 27.05, 4], [9, 26.95, 6], [30, 27.1, 7]];  // [expert, abs time, slot]
    const hot = HOT.map(() => E(R, "position:absolute;left:0;top:0;width:44px;height:44px;border-radius:12px;background:#01ccf7;box-shadow:0 0 22px rgba(1,204,247,.8);transform-origin:0 0;display:grid;place-items:center", ico("pin", 22, "#0a0d2c", 2.4)));
    const t0 = w(5, 0);   // = 0 (card clock starts at line 5)
    const TA = [0.05, 0.75, 1.55].map((x) => x);              // three words light experts (line 5)
    const LIT = [[3, 20], [11, 34], [26, 5]];
    const L6 = L[6].t0 - L[5].t0, L7 = L[7].t0 - L[5].t0, L8 = L[8].t0 - L[5].t0, CALL = w(7, 5) - 0.1, MK1 = w(8, 8), MK2 = w(8, 10);
    TA.forEach((a) => { f(a + 0.15, "click", -6, 1.3); f(a + 0.3, "ping", -12, 1.4); });
    f(L6 + 0.2, "whoosh", -7, 1.4); f(L6 + 0.5, "pop", -5); f(L7 + 0.1, "whoosh", -6, 0.8); f(L7 + 0.6, "pop", -8, 0.8);
    HOT.forEach(([, at]) => f(at - L[5].t0 - 0.3, "pop", -8, 1.3)); f(L8 + 0.2, "pop", -6, 1.1); f(MK1, "ping", -8, 1.2); f(MK2, "ping", -6, 1.4); f(CALL + 0.4, "sparkle", -9);
    return (u) => {
      // phase weights
      const toSSD = eio(lin(u, L7 - 0.1, L7 + 0.55)), ramIn = spr(u - (L6 - 0.15), 2.0, 0.66), gpuIn = spr(u - (L8 + 0.15), 2.2, 0.6);
      ttl.textContent = u < L6 - 0.1 ? "1 model · banyak ahli kecil" : "";
      // RAM + core: core sits above the grid at first, then the RAM forms around it
      op(ram, cl(ramIn * 2) * (u > L6 - 0.15 ? 1 : 0)); tf(ram, 0, -30 * (1 - ramIn), 0.92 + 0.08 * ramIn); pop(ramL, u, L6 + 0.05);
      const cm = e3(lin(u, L6, L6 + 0.5)), cY = mix(170, 112, cm);
      op(core, e3(lin(u, -0.1, 0.25)) * (u < L6 - 0.2 ? 0.55 : 1)); core.style.top = cY.toFixed(1) + "px"; core.style.left = mix(150, 70, cm).toFixed(1) + "px"; core.style.width = mix(660, 550, cm).toFixed(1) + "px";
      core.textContent = u < L6 - 0.2 ? "inti model" : "inti model · selalu kepakai";
      op(gpu, u > L8 + 0.15 ? cl(gpuIn * 2) : 0); tf(gpu, 40 * (1 - gpuIn), 0, 0.9 + 0.1 * gpuIn); pop(gpuL, u, L8 + 0.25);
      op(ssd, e3(lin(u, L7 + 0.1, L7 + 0.5))); tf(ssd, 0, 20 * (1 - e3(lin(u, L7 + 0.1, L7 + 0.5)))); pop(ssdL, u, L7 + 0.3);
      // the token: line 5 above the grid (three words), later in the middle (the next word calls experts)
      let tx, ty, to = 0, tw = "kata";
      if (u < L6 - 0.1) { const k = TA.reduce((a, x, i) => (u >= x ? i : a), 0), p = e3(lin(u, TA[k], TA[k] + 0.3)); tx = mix(-60, 60, p); ty = 210; to = p * (1 - e3(lin(u, L6 - 0.4, L6 - 0.1))); tw = ["kata 1", "kata 2", "kata 3"][k]; }
      else if (u > L7 + 0.6) { const p = e3(lin(u, L7 + 0.6, L7 + 1.0)); tx = 60; ty = 440; to = p; tw = u < L8 ? "kata berikutnya" : "kata lagi"; }
      tok.textContent = tw; if (tx != null) { tok.style.left = tx + "px"; tok.style.top = ty + "px"; } op(tok, to);
      // the grid: lit experts per word (line 5), then morph into the SSD
      const kNow = TA.reduce((a, x, i) => (u >= x + 0.15 ? i : a), -1);
      cells.forEach((c, k) => {
        const a = A(k), b = B(k), x = mix(a[0], b[0], toSSD), y = mix(a[1], b[1], toSSD), s = mix(a[2], b[2], toSSD) / 80;
        const st = spr(u + 0.05 - (k % 8) * 0.012 - Math.floor(k / 8) * 0.02, 2.4, 0.6);
        c.style.transform = `translate(${x.toFixed(1)}px,${y.toFixed(1)}px) scale(${(s * (0.5 + 0.5 * st)).toFixed(3)})`;
        const lit = u < L6 && kNow >= 0 && LIT[kNow].includes(k);
        const gone = HOT.some(([e, at]) => e === k && u > at - L[5].t0 - 0.05) && !(k === 9 || k === 30) ? 1 : 0;
        c.style.background = lit ? "#01ccf7" : gone ? "rgba(184,241,255,.05)" : "rgba(184,241,255,.16)";
        c.style.boxShadow = lit ? "0 0 26px rgba(1,204,247,.8)" : "none";
        op(c, cl(st * 3) * (u < L6 && kNow >= 0 && !lit ? 0.45 : 1));
      });
      // router lines (line 5: token -> lit experts; line 7+: called experts -> RAM)
      LN.forEach((s, j) => {
        if (u < L6 - 0.1 && kNow >= 0) { const a = A(LIT[kNow][j]); segSet(s, 160, 232, a[0] + 40, a[1], e3(lin(u, TA[kNow] + 0.05, TA[kNow] + 0.3)), 0.9 * (1 - e3(lin(u, L6 - 0.4, L6 - 0.1)))); }
        else op(s, 0);
      });
      // hot experts fly up from the SSD into RAM cache slots / GPU slots and get pinned
      hot.forEach((h, j) => { const [e, at, sl] = HOT[j], a = at - L[5].t0; const p = spr(u - a, 1.9, 0.72), b = B(e), S = SLOT[sl];
        const x = mix(b[0], S[0], cl(p)), y = mix(b[1], S[1], cl(p)) - 70 * Math.sin(Math.PI * cl(p)), s = mix(1, S[2] / 44, cl(p));
        h.style.transform = `translate(${x.toFixed(1)}px,${y.toFixed(1)}px) scale(${s.toFixed(3)})`; op(h, u > a ? 1 : 0);
        h.style.boxShadow = `0 0 ${(18 + 20 * bump(u, MK1, 0.5) + 20 * bump(u, MK2, 0.5)).toFixed(0)}px rgba(1,204,247,.85)`; });
      op(spd, e3(lin(u, L8 + 0.6, L8 + 1.0))); fill.style.transform = `scaleX(${(0.18 + 0.32 * e3(lin(u, MK1 - 0.1, MK1 + 0.3)) + 0.42 * e3(lin(u, MK2 - 0.1, MK2 + 0.35))).toFixed(3)})`;
    };
  });
  // ============ 10-12 · models + minimum RAM (README "Which model for my machine": first RAM number = below it the model does not start)
  addCard(10, 12, 960, 840, "right", "up", (R, w, f) => {
    panel(R, 960, 840);
    E(R, "left:44px;top:38px", "model · RAM minimal", "lb");
    const ROWS = [["deepseek", "DeepSeek V4 Flash", "284B parameter · ahli dari SSD", 16, 10, 7], ["kimi", "Kimi K3", "2,8T parameter · paling besar", 32, 11, 4], ["qwen", "Qwen3-Coder-30B", "30B · khusus coding", 8, 12, 5]];
    const RW = ROWS.map(([lg, nm, sub, gb, li, wi], k) => {
      const y = 96 + k * 214; const box = E(R, `left:32px;top:${y}px;width:896px;height:190px`, null, "pn2");
      const lo = logo(box, lg, 140, "left:20px;top:25px");
      E(box, "left:184px;top:34px;font-size:38px", nm, "tb"); E(box, "left:184px;top:84px;font-size:22px;color:rgba(220,236,255,.7)", sub, "tx");
      const tr = E(box, "left:184px;top:132px;width:480px;height:22px", null, "bar"); const fl = E(tr, `left:0;top:0;width:${480 * gb / 32}px;height:22px;transform-origin:0 50%`, null, "bar acc");
      const num = E(box, `left:690px;top:96px;font:700 64px/1 Poppins;white-space:nowrap`, "", "tb");
      const a = L[li].t0 - L[10].t0, n = L[li].ws[wi][1] - L[10].t0;
      f(a - 0.05, "whoosh", -8, 1.3); f(a + 0.2, "pop", -6, 1.0 + 0.1 * k); f(n + 0.1, "ping", -8, 1.0 + 0.15 * k);
      return { box, lo, fl, num, gb, a, n };
    });
    const note = E(R, "left:44px;top:754px;font-size:22px;color:rgba(220,236,255,.62);white-space:nowrap", "angka = RAM minimal di README · RAM lebih besar = lebih lancar", "tx");
    return (u) => {
      RW.forEach((r) => { const p = spr(u - r.a + 0.05, 2.1, 0.62); op(r.box, u > r.a - 0.05 ? cl(p * 3) : 0); tf(r.box, 120 * (1 - p), 0); logoSet(r.lo, u, r.a + 0.05, 1);
        const q = e3(lin(u, r.n - 0.25, r.n + 0.35)); r.fl.style.transform = `scaleX(${q.toFixed(3)})`; r.num.innerHTML = u > r.n - 0.3 ? `${Math.round(r.gb * q)} <span style="${GRAD};font-size:40px">GB</span>` : ""; });
      op(note, e3(lin(u, RW[2].n + 0.3, RW[2].n + 0.8)));
    };
  });
  // ============ 13 · Windows, Mac, Linux (README: START-HERE.bat on Windows, ./start-here.sh on Linux and macOS)
  addCard(13, 13, 940, 520, "drop", "right", (R, w, f) => {
    panel(R, 940, 520);
    const OS = [["Windows", null, w(13, 2)], ["macOS", "apple", w(13, 3)], ["Linux", "linux", w(13, 5)]];
    const T = OS.map(([n, lg, a], k) => { const x = 36 + k * 296; const tile = E(R, `left:${x}px;top:50px;width:276px;height:420px`, null, "pn2");
      const ic = lg ? logo(tile, lg, 170, "left:53px;top:50px") : E(tile, "left:53px;top:50px;width:170px;height:170px", ico("monitor", 150, "#b8f1ff", 1.6), "ic");
      E(tile, "left:0;top:262px;width:276px;text-align:center;font-size:40px", n, "tb");
      const ck = E(tile, "left:108px;top:330px;width:60px;height:60px", ico("circle-check", 60, "#01ccf7", 2.4), "ic");
      f(a + 0.05, "pop", -5, 1.0 + 0.12 * k); return { tile, ic, ck, a, lg }; });
    return (u) => { T.forEach((o, k) => { const p = spr(u - (o.a - 0.3), 2.3, 0.6); op(o.tile, cl(p * 3) * (u > o.a - 0.3 ? 1 : 0)); tf(o.tile, 0, 40 * (1 - p));
      if (o.lg) logoSet(o.ic, u, o.a - 0.2, 1); else { op(o.ic, e3(lin(u, o.a - 0.25, o.a))); }
      pop(o.ck, u, o.a + 0.05); }); };
  }, 1020);
  // ============ 14-15 · START-HERE checks the PC and recommends a model, then the chat opens in the browser
  // (README: "You answer one question, which model, and Enter takes the recommendation" … "starts colibri and opens the chat in
  //  your browser" + the printed lines "Starting colibri" / "Browser: http://127.0.0.1:8000/")
  addCard(14, 15, 960, 900, "swing", "shrink", (R, w, f) => {
    // file window
    const fw = E(R, "left:0;top:0;width:430px;height:420px", null, "pn");
    [28, 50, 72].forEach((x) => E(fw, `position:absolute;left:${x}px;top:26px;width:13px;height:13px;border-radius:50%;background:rgba(255,255,255,.28)`, null));
    E(fw, "left:104px;top:20px;display:flex;align-items:center;gap:8px", ico("folder", 22, "rgba(220,236,255,.7)") + "colibri", "lb");
    const FILES = [["folder", "c"], ["file-code", "START-HERE.bat"], ["file-code", "start-here.sh"], ["file", "README.md"]];
    const FR = FILES.map(([ic, n], k) => E(fw, `left:22px;top:${74 + k * 80}px;width:386px;height:64px;border-radius:14px;display:flex;align-items:center;gap:14px;padding-left:16px;font:400 26px/1 Poppins;justify-content:flex-start`, ico(ic, 30, "#b8f1ff") + n, "ic"));
    // terminal
    const tm = E(R, "left:460px;top:0;width:500px;height:420px;border-radius:26px;background:#070b22;border:1.5px solid rgba(150,210,255,.22);box-shadow:0 30px 64px rgba(2,6,26,.55)", null);
    [28, 50, 72].forEach((x) => E(tm, `position:absolute;left:${x}px;top:26px;width:13px;height:13px;border-radius:50%;background:rgba(255,255,255,.22)`, null));
    E(tm, "left:104px;top:20px;display:flex;align-items:center;gap:8px", ico("terminal", 22, "rgba(220,236,255,.7)") + "start-here", "lb");
    const CK = ["RAM", "disk kosong", "CPU", "GPU"].map((n, k) => E(tm, `left:30px;top:${80 + k * 50}px;display:flex;align-items:center;gap:12px;font:400 26px/1 Poppins`, ico("circle-check", 28, "#01ccf7", 2.4) + `cek ${n}`, "ic"));
    const q = E(tm, "left:30px;top:290px;font:700 26px/1 Poppins;white-space:nowrap", "model mana?", "tb");
    const ent = E(tm, "left:30px;top:336px", ico("keyboard", 22, "#0a0d2c") + "Enter = rekomendasi", "cp on");
    const ill = E(R, "left:744px;top:-24px", "ilustrasi", "cp");
    // the README's printed lines + the URL (shared element -> browser address bar)
    const out = E(R, "left:0;top:446px;width:960px;height:90px;border-radius:20px;background:#070b22;border:1.5px solid rgba(150,210,255,.22)", null);
    E(out, "left:28px;top:16px;font:400 24px/1 Poppins;color:rgba(220,236,255,.75);white-space:nowrap", "Starting colibri", "tx");
    const url = E(R, "left:28px;top:496px;font:700 26px/1 Poppins;white-space:nowrap", 'Browser: <span style="color:#01ccf7">http://127.0.0.1:8000/</span>', "tb");
    // browser
    const br = E(R, "left:0;top:560px;width:960px;height:340px;transform-origin:50% 0", null, "pn");
    [28, 50, 72].forEach((x) => E(br, `position:absolute;left:${x}px;top:28px;width:13px;height:13px;border-radius:50%;background:rgba(255,255,255,.28)`, null));
    const bar = E(br, "left:104px;top:14px;width:820px;height:44px;border-radius:22px;background:rgba(10,20,58,.8);border:1.5px solid rgba(150,210,255,.2)", null);
    const burl = E(bar, "left:22px;top:9px;font:400 23px/1.1 Poppins;color:#b8f1ff;white-space:nowrap", "127.0.0.1:8000", "tx");
    const ub = E(br, "left:430px;top:88px;max-width:500px;padding:16px 22px;border-radius:22px 22px 6px 22px;background:#01ccf7;color:#0a0d2c;font:700 25px/1.3 Poppins;white-space:nowrap", "Halo, kamu jalan di PC aku?", null);
    const ab = E(br, "left:36px;top:178px;width:620px;padding:16px 22px;border-radius:22px 22px 22px 6px;background:rgba(255,255,255,.1);font:400 25px/1.35 Poppins;color:#fff;white-space:normal;min-height:60px", "", null);
    const ill2 = E(br, "left:792px;top:270px", "contoh chat", "cp");
    const cur = cursor(R), rp = ripple(R);
    const DBL = w(14, 1) + 0.1, CHK = w(14, 3) - 0.05, MIL = w(14, 7) - 0.1, L15 = L[15].t0 - L[14].t0, OPEN = w(15, 1) - 0.1;
    f(DBL, "click", -3); f(DBL + 0.14, "click", -4, 1.1); f(DBL + 0.35, "whoosh", -8, 1.5);
    [0, 1, 2, 3].forEach((k) => f(CHK + k * 0.22, "pop", -9, 1.3 + 0.05 * k)); f(MIL + 0.45, "key", -3); f(MIL + 0.5, "ping", -8);
    f(L15 + 0.05, "key", -6, 1.1); f(L15 + 0.35, "whoosh", -6, 1.2); f(OPEN, "pop", -5); f(OPEN + 0.5, "click", -8, 1.4);
    for (let k = 0; k < 6; k++) f(OPEN + 0.9 + k * 0.12, "key", -14, 1.2 + 0.08 * (k % 3));
    const ANS = "Iya, aku jalan di PC kamu.";
    return (u) => {
      op(fw, e3(lin(u, -0.2, 0.1)));
      FR.forEach((r, k) => { r.style.background = k === 1 && u > DBL - 0.3 ? "rgba(1,204,247,.22)" : "transparent"; r.style.border = k === 1 && u > DBL - 0.3 ? "2px solid rgba(1,204,247,.7)" : "2px solid transparent"; });
      curSet(cur, u, [[0, 330, 330], [DBL - 0.5, 300, 280], [DBL + 0.4, 300, 282], [MIL + 0.1, 700, 470], [MIL + 0.6, 700, 470]], [DBL, DBL + 0.14, MIL + 0.45], e3(lin(u, 0.1, 0.4)) * (1 - e3(lin(u, L15 - 0.2, L15))));
      ripSet(rp, u, DBL, 300, 282);
      const tp = spr(u - (DBL + 0.3), 2.2, 0.62); op(tm, u > DBL + 0.3 ? cl(tp * 3) : 0); tf(tm, 0, 0, 0.6 + 0.4 * tp); op(ill, e3(lin(u, DBL + 0.4, DBL + 0.7)) * (1 - e3(lin(u, L15, L15 + 0.3))));
      CK.forEach((c, k) => { const p = e3(lin(u, CHK + k * 0.22, CHK + k * 0.22 + 0.2)); op(c, p); tf(c, 14 * (1 - p), 0); });
      op(q, e3(lin(u, MIL - 0.1, MIL + 0.15))); pop(ent, u, MIL + 0.1); tf(ent, 0, 0, 1 - 0.1 * bump(u, MIL + 0.4, 0.2));
      // line 15: the README lines print, the URL flies into the browser address bar, the browser opens below
      op(out, e3(lin(u, L15 - 0.05, L15 + 0.2)));
      const fly = eio(lin(u, OPEN - 0.05, OPEN + 0.5));
      url.style.left = mix(28, 104 + 22, fly).toFixed(1) + "px"; url.style.top = mix(496, 560 + 23, fly).toFixed(1) + "px"; url.style.fontSize = mix(26, 23, fly).toFixed(1) + "px";
      op(url, u > L15 + 0.1 ? e3(lin(u, L15 + 0.1, L15 + 0.35)) * (1 - e3(lin(u, OPEN + 0.42, OPEN + 0.55))) : 0);
      const bo = spr(u - (OPEN + 0.25), 1.9, 0.7); op(br, u > OPEN + 0.25 ? cl(bo * 3) : 0); br.style.transform = `scaleY(${(0.2 + 0.8 * bo).toFixed(3)})`;
      op(burl, e3(lin(u, OPEN + 0.45, OPEN + 0.6)));
      pop(ub, u, OPEN + 0.6); op(ab, e3(lin(u, OPEN + 0.85, OPEN + 1.0))); const n = Math.round(ANS.length * lin(u, OPEN + 0.9, OPEN + 1.6)); ab.textContent = ANS.slice(0, n) + (n < ANS.length && n > 0 ? " ▍" : "");
      op(ill2, e3(lin(u, OPEN + 0.9, OPEN + 1.2)));
    };
  }, 1080);
  // ============ 16 · honest trade-off (README: the disk sets the speed; DeepSeek V4 Flash 0.93 tok/s with 32 GB, CPU only;
  //  Kimi K3 about 9.4 s per token; downloads 167 GB / 1.56 TB)
  addCard(16, 16, 960, 800, "tilt", "grow", (R, w, f) => {
    panel(R, 960, 800);
    E(R, "left:44px;top:40px", "jujur aja · angka dari README", "lb");
    const r1 = E(R, "left:32px;top:92px;width:896px;height:300px", null, "pn2");
    E(r1, "left:26px;top:28px;width:84px;height:84px", ico("turtle", 50, "#b8f1ff"), "node");
    E(r1, "left:134px;top:36px;font-size:40px", "Model besar = pelan", "tb");
    const s1 = E(r1, "left:134px;top:118px;font:400 27px/1.3 Poppins;white-space:nowrap", 'DeepSeek V4 Flash: <b style="color:#01ccf7">0,93 token/detik</b>', "tx");
    E(r1, "left:134px;top:156px;font-size:21px;color:rgba(220,236,255,.62)", "RAM 32 GB, CPU saja", "tx");
    const s2 = E(r1, "left:134px;top:210px;font:400 27px/1.3 Poppins;white-space:nowrap", 'Kimi K3: <b style="color:#01ccf7">± 9,4 detik per token</b>', "tx");
    const r2 = E(R, "left:32px;top:414px;width:896px;height:340px", null, "pn2");
    E(r2, "left:26px;top:28px;width:84px;height:84px", ico("hard-drive-download", 48, "#b8f1ff"), "node");
    E(r2, "left:134px;top:36px;font-size:40px", "SSD-nya harus lega", "tb");
    const B = [["DeepSeek V4 Flash", 167, "167 GB"], ["Kimi K3", 1560, "1,56 TB"], ["model terkecil", 22, "22 GB"]].map(([n, gb, lab], k) => {
      const y = 126 + k * 70; E(r2, `left:134px;top:${y}px;font-size:24px`, n, "tx");
      const tr = E(r2, `left:410px;top:${y + 6}px;width:300px;height:22px`, null, "bar"); const fl = E(tr, `left:0;top:0;width:${Math.max(10, 300 * Math.log10(gb) / Math.log10(1560))}px;height:22px;transform-origin:0 50%`, null, "bar acc");
      const lb = E(r2, `left:730px;top:${y - 4}px;font-size:30px`, lab, "tb"); return { fl, lb, k }; });
    E(r2, "left:410px;top:332px;font-size:17px;color:rgba(220,236,255,.5)", "skala log", "tx");
    const PL = w(16, 5) - 0.1, SD = w(16, 8) - 0.1;
    f(PL + 0.1, "pop", -6, 0.8); f(PL + 0.45, "pop", -8, 0.85); [0, 1, 2].forEach((k) => f(SD + 0.15 + k * 0.25, "click", -8, 1.3));
    return (u) => {
      op(r1, e3(lin(u, -0.2, 0.15))); pop(s1, u, PL); pop(s2, u, PL + 0.35);
      const p2 = spr(u - (SD - 0.45), 2.1, 0.64); op(r2, u > SD - 0.45 ? cl(p2 * 3) : 0); tf(r2, 0, 60 * (1 - p2));
      B.forEach((b) => { const q = e3(lin(u, SD + b.k * 0.25, SD + b.k * 0.25 + 0.4)); b.fl.style.transform = `scaleX(${q.toFixed(3)})`; op(b.lb, q); });
    };
  }, 1060);

  // ------------------------------------------------------------------ explaining-beat props (beside the half-body mascot)
  const PR = $("props");
  // L0 hook: three model logos spin in around the mascot (Simple Icons, 3D sprites)
  const HK = [["deepseek", 70, 760, wt(0, 2)], ["kimi", 850, 760, wt(0, 2) + 0.2], ["qwen", 90, 1060, wt(0, 2) + 0.4]].map(([n, x, y, a]) => { const e = logo(PR, n, 150, `left:${x}px;top:${y}px`); fx(a + 0.05, "pop", -7, 1.0 + 0.1 * (x % 3)); return [e, a]; });
  const pcChip = E(PR, "left:770px;top:1080px", ico("laptop", 26, "#0a0d2c") + "PC sendiri", "cp on"); fx(wt(0, 9) + 0.0, "ping", -8);
  // L4: little "experts" pop around the mascot, then fly into the model-map grid (shared element)
  const EXP = []; for (let k = 0; k < 12; k++) { const sd = k < 6 ? -1 : 1, j = k % 6; EXP.push([E(PR, "position:absolute;left:0;top:0;width:58px;height:58px;border-radius:12px;background:rgba(184,241,255,.22);border:2px solid rgba(184,241,255,.5);box-shadow:0 0 16px rgba(1,204,247,.35)", null),
    540 + sd * (330 + (j % 3) * 70) - 29, 760 + Math.floor(j / 3) * 120 + (j % 3) * 30, wt(4, 6) + k * 0.05]); }
  EXP.forEach(([, , , a], k) => { if (k % 3 === 0) fx(a + 0.05, "pop", -9, 1.2 + 0.05 * k); });
  // L9: two chips — where an expert sits changes the speed / the model stays whole
  const CH9 = [E(PR, "left:60px;top:740px", ico("gauge", 24, "#b8f1ff") + "kecepatan", "cp"), E(PR, "left:700px;top:740px", ico("circle-check", 24, "#0a0d2c", 2.4) + "model utuh", "cp on")];
  fx(wt(9, 4) + 0.05, "pop", -6); fx(wt(9, 7) + 0.05, "ping", -7);
  // L17: what you need
  const CH17 = [E(PR, "left:60px;top:820px", ico("laptop", 24, "#0a0d2c") + "PC sendiri", "cp on"), E(PR, "left:720px;top:820px", ico("hard-drive", 24, "#0a0d2c") + "SSD lega", "cp on")];
  fx(wt(17, 6) + 0.05, "pop", -6); fx(wt(17, 9) + 0.05, "pop", -6, 1.15);
  function props(t) {
    const k0 = mascotK(t);
    // hook logos (leave with the mascot)
    HK.forEach(([e, a]) => { logoSet(e, t, a, 1); if (t > window.STAGE[0].b) { const p = e3(lin(t, window.STAGE[0].b, window.STAGE[0].b + 0.3)); op(e, 1 - p); e.style.transform += ` scale(${(1 - 0.4 * p).toFixed(3)})`; } });
    pop(pcChip, t, wt(0, 9) - 0.1); if (t > window.STAGE[0].b) op(pcChip, 1 - e3(lin(t, window.STAGE[0].b, window.STAGE[0].b + 0.25)));
    // experts: pop on "ahli kecil", fly into the grid when the model-map card lands
    const g = MAP, gx = CX - g.W / 2, gy = g.cy - g.H / 2;
    EXP.forEach(([e, x0, y0, a], k) => {
      const p = spr(t - a, 2.4, 0.55), fly = eio(lin(t, g.tin - 0.05 + k * 0.012, g.tin + 0.42 + k * 0.012));
      const tgt = [gx + 104 + ((k * 3) % 8) * 96, gy + 280 + Math.floor((k * 3) / 8) * 96];
      const bob = 8 * Math.sin(t * 2.2 + k);
      const x = mix(x0, tgt[0], fly), y = mix(y0 + bob, tgt[1], fly), s = mix(0.4 + 0.6 * p, 80 / 58, fly);
      e.style.transform = `translate(${x.toFixed(1)}px,${y.toFixed(1)}px) scale(${s.toFixed(3)})`;
      op(e, t < a ? 0 : cl(p * 3) * (1 - e3(lin(t, g.tin + 0.35, g.tin + 0.5))));
      e.style.filter = fly > 0.05 && fly < 0.95 ? "blur(1.5px)" : "none";
    });
    const s2 = window.STAGE[2], s3 = window.STAGE[3];
    CH9.forEach((c, k) => { pop(c, t, wt(9, [4, 6][k]) - 0.05); if (t > s2.b) op(c, 1 - e3(lin(t, s2.b, s2.b + 0.25))); });
    CH17.forEach((c, k) => { pop(c, t, wt(17, [6, 9][k]) - 0.05); if (t > L[18].t0 - 0.3) op(c, 1 - e3(lin(t, L[18].t0 - 0.3, L[18].t0 - 0.05))); });
  }
  // ------------------------------------------------------------------ CTA pill + DM chip (above the half-body mascot)
  const cta = $("cta"), ctar = $("ctaring"), dmc = $("dmchip");
  $("ctaic").innerHTML = ico("message-circle", 50, "#0a0d2c", 2.6);
  dmc.innerHTML = ico("send", 24, "#b8f1ff") + "link repo + tabel model per RAM";
  const L18 = L[18], cw = (k) => L18.ws[k][1];
  fx(L18.t0 - 0.05, "impact", 0); fx(L18.t0 - 0.05, "riser", 0); fx(cw(1) + 0.1, "pop", -2, 0.8); fx(cw(4) + 0.05, "ping", -4); fx(cw(12) + 0.1, "sparkle", -6);
  function ctaF(t) {
    const hb = HL[18].d.offsetTop + HL[18].d.offsetHeight, ty = Math.max(560, hb + 36);   // pill sits under the full CTA headline
    cta.style.top = ty + "px"; ctar.style.top = ty - 30 + "px"; dmc.style.top = ty + 136 + "px";
    const p = spr(t - (L18.t0 - 0.05), 2.0, 0.55); op(cta, t > L18.t0 - 0.05 ? cl(p * 3) : 0);
    const pulse = 0.035 * Math.sin(Math.max(0, t - cw(1)) * 5.5) * (t > cw(1) ? 1 : 0);
    cta.style.transform = `translateY(${(50 * (1 - p)).toFixed(1)}px) scale(${(0.7 + 0.3 * p + pulse).toFixed(3)})`;
    const rr = lin((t - cw(1)) % 1.1, 0, 1.1); op(ctar, t > cw(1) ? 0.8 * (1 - rr) : 0); ctar.style.transform = `scale(${(0.9 + 0.2 * rr).toFixed(3)})`;
    dmc.style.left = (540 - dmc.offsetWidth / 2).toFixed(0) + "px"; pop(dmc, t, cw(4) - 0.1);
    op($("flash"), 0.5 * bump(t, L18.t0 - 0.12, 0.45));
  }
  // ------------------------------------------------------------------ background: glow, particles, grain
  const parts = []; for (let k = 0; k < 30; k++) { const e = document.createElement("i"); const s = 2 + ((k * 37) % 4); e.style.width = e.style.height = s + "px"; $("parts").appendChild(e); parts.push([e, (k * 997) % 1080, (k * 613) % 1920, 12 + ((k * 7) % 20), 0.1 + ((k * 13) % 25) / 100]); }
  function bg(t) {
    parts.forEach(([e, x, y, sp, o], k) => { const yy = ((y - t * sp) % 2000 + 2000) % 2000 - 40; const xx = x + 14 * Math.sin(t * 0.3 + k); e.style.transform = `translate(${xx.toFixed(1)}px,${yy.toFixed(1)}px)`; op(e, o * (0.6 + 0.4 * Math.sin(t * 1.3 + k * 2))); });
    $("glow").style.transform = `scale(${(1 + 0.05 * Math.sin(t * 0.7)).toFixed(3)})`;
    const g = Math.floor(t * 12); $("grain").style.transform = `translate(${(g * 37) % 64}px,${(g * 23) % 64}px)`;
    op($("brandlogo"), 0.96 * e3(lin(t, 0.05, 0.4)));
  }
  function render(t) { bg(t); heads(t); cards(t); props(t); ctaF(t); }
  window.__r39render = render;
  window.__r39 = { L, C, STAGE: window.STAGE };
  render(0);
  window.addEventListener("hf-seek", (e) => render(e.detail.time));
})();

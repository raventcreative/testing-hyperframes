// Shared visual system of the R16 PAPERCLIP reel ("Bikin perusahaan AI sendiri pakai Paperclip"), loaded in <head> before every
// scene (after vendor/r16icons.js). Everything is our own design in the AI PRENEUR LIGHT house style: the agent avatars (role colour +
// bot glyph + role badge), the org chart, the heartbeat monitor and the budget rows. No Paperclip logo/UI is reproduced: the paperclip
// glyph is the lucide "paperclip" icon (ISC). All company data (Keripik Renyah, tasks, budgets, token counts) is illustrative.
// - R16.svg(k, sw)          lucide icon (inline, currentColor)
// - R16.ROLE                the agents: ceo · web · konten · riset · desain (name, adapter label, icon, colours)
// - R16.av(id, k, size)     agent avatar (circle in the role colour, white bot glyph, white role badge)
// - R16.ORG / R16.org(p, o) the org chart (goal banner, "Kamu" chip, CEO + team nodes, connector bars, task tickets); ids p-*
// - R16.MON / R16.mon(p, o) the monitor panel with one row per agent (heartbeat in s06, budget in s07); ids p-*
// - R16.scene(ID)           timeline boilerplate: seek-safe scale shorthand, every initial state pinned at 0 in a NESTED timeline that is
//                           the first child at 0 (I), fromTo without immediate render (ft), word lookup (L), and done() = end marker +
//                           backward-seek patch + tl.render(0, true, true) + registration.
(function () {
  const ICO = window.R16_ICO;
  const svg = (k, sw, cls) => `<svg class="${cls || ""}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[k]}</svg>`;

  // ---------------------------------------------------------------- the agents (adapter labels = adapters listed in Paperclip's README)
  const ROLE = {
    ceo: { n: "CEO", s: "Claude Code", ic: "briefcase", c1: "#ffcf4d", c2: "#e39a00" },
    web: { n: "Tim Web", s: "Codex", ic: "globe", c1: "#6f9bff", c2: "#2f5fd6" },
    konten: { n: "Tim Konten", s: "Claude Code", ic: "pen-line", c1: "#ff9b6e", c2: "#dc5f30" },
    riset: { n: "Tim Riset", s: "Gemini CLI", ic: "search", c1: "#45d3a8", c2: "#11946d" },
    desain: { n: "Agent Desain", s: "OpenCode", ic: "palette", c1: "#b796ff", c2: "#7449dc" },
  };
  const av = (id, k, size) => {
    const r = ROLE[k], s = size, b = Math.round(s * 0.44), bi = Math.round(b * 0.58), g = Math.round(s * 0.54);
    return `<div class="r16-av" id="${id}" style="width:${s}px;height:${s}px;margin:${-s / 2}px 0 0 ${-s / 2}px">` +
      `<div class="ci" style="background:linear-gradient(150deg,${r.c1},${r.c2});box-shadow:0 ${Math.round(s * 0.16)}px ${Math.round(s * 0.3)}px -${Math.round(s * 0.14)}px ${r.c2}"></div>` +
      `<div class="bo" style="left:${(s - g) / 2}px;top:${(s - g) / 2 - s * 0.03}px;width:${g}px;height:${g}px">${svg("bot", 2)}</div>` +
      `<div class="rb" style="width:${b}px;height:${b}px;right:${-s * 0.06}px;bottom:${-s * 0.06}px;color:${r.c2}"><i style="left:${(b - bi) / 2}px;top:${(b - bi) / 2}px;width:${bi}px;height:${bi}px">${svg(r.ic, 2.4)}</i></div></div>`;
  };

  // ---------------------------------------------------------------- ORG CHART (global px)
  const ORG = {
    goal: { x: 190, y: 318, w: 700, h: 88 },
    ceo: { x: 540, y: 522, s: 112 },
    kamu: { x: 96, y: 492, w: 262, h: 64 },
    ty: 742, ts: 100,
    x3: { web: 230, konten: 540, riset: 850 },
    x4: { web: 180, konten: 420, riset: 660, desain: 900 },
    bus: 660,
    TASK: { web: "Bikin toko online", konten: "Caption 7 hari", riset: "Cek harga pesaing" },
  };
  // o.layout: 3 | 4 (team x positions); o.desain: include the 4th node; everything visible (scenes pin what they hide)
  const GOALTXT = "Tembus 100 pesanan online / minggu";
  const goalIn = (p, txt) => `<div class="gi">${svg("target", 2.2)}</div><span class="gl">TUJUAN · Keripik Renyah<i class="r16-tag">CONTOH</i></span>` +
    `<b class="gt r16-grad" id="${p}-gt">${txt === undefined ? GOALTXT : txt}</b>`;
  const org = (p, o) => {
    o = o || {}; const X = o.layout === 4 ? ORG.x4 : ORG.x3, G = ORG.goal, C = ORG.ceo, K = ORG.kamu;
    const keys = ["web", "konten", "riset"].concat(o.desain ? ["desain"] : []);
    let h = `<div class="r16-goal r16-card2" id="${p}-goal" style="left:${G.x}px;top:${G.y}px;width:${G.w}px;height:${G.h}px">` +
      `${goalIn(p)}</div>`;
    // connectors (flat bars; scenes scale them in)
    h += `<div class="r16-ln" id="${p}-lg" style="left:${C.x - 1.5}px;top:${G.y + G.h}px;width:3px;height:${C.y - C.s / 2 - G.y - G.h}px"></div>`;
    const XX = (k) => (k === "desain" ? ORG.x4.desain : X[k]);
    const xs = keys.filter((k) => o.layout === 4 || k !== "desain").map(XX), xl = Math.min(...xs), xr = Math.max(...xs);
    h += `<div class="r16-ln" id="${p}-lc" style="left:${C.x - 1.5}px;top:${C.y + 118}px;width:3px;height:${ORG.bus - C.y - 118}px"></div>`;
    h += `<div class="r16-ln" id="${p}-lb" style="left:${xl}px;top:${ORG.bus - 1.5}px;width:${xr - xl}px;height:3px;transform-origin:50% 50%"></div>`;
    keys.forEach((k) => { h += `<div class="r16-ln" id="${p}-ls-${k}" style="left:${XX(k) - 1.5}px;top:${ORG.bus}px;width:3px;height:${ORG.ty - ORG.ts / 2 - ORG.bus}px"></div>`; });
    // you (the board)
    h += `<div class="r16-kamu r16-card2" id="${p}-kamu" style="left:${K.x}px;top:${K.y}px;width:${K.w}px;height:${K.h}px"><div class="ka">${svg("user", 2.2)}</div><b>Kamu</b><span>pemilik · pengawas</span></div>`;
    // nodes
    const node = (k, x, y, s, nid) => `<div class="r16-node" id="${nid}" style="left:${x}px;top:${y}px">${av(nid + "-av", k, s)}` +
      `<div class="nl" style="top:${s / 2 + 8}px"><b>${ROLE[k].n}</b><span>${ROLE[k].s}</span></div></div>`;
    h += node("ceo", C.x, C.y, C.s, `${p}-ceo`);
    keys.forEach((k) => { h += node(k, XX(k), ORG.ty, ORG.ts, `${p}-n-${k}`); });
    if (o.tickets) ["web", "konten", "riset"].forEach((k) => {
      h += `<div class="r16-tka" id="${p}-tk-${k}" style="left:${X[k]}px;top:${ORG.ty + 120}px"><div class="r16-tk"><i>${svg("clipboard-list", 2.2)}</i>${ORG.TASK[k]}</div></div>`;
    });
    return h;
  };

  // ---------------------------------------------------------------- MONITOR PANEL (s06 heartbeat · s07 budget)
  const MON = { x: 80, y: 318, w: 920, h: 596, rows: ["ceo", "web", "konten", "riset", "desain"], ry: [462, 553, 644, 735, 826], ax: 150, as: 70,
    tx0: 352, tx1: 806, px: 822, pw: 160 };
  const mon = (p, o) => {
    o = o || {};
    let h = `<div class="r16-mon r16-card" id="${p}-panel" style="left:${MON.x}px;top:${MON.y}px;width:${MON.w}px;height:${MON.h}px"></div>`;
    MON.rows.forEach((k, i) => {
      const y = MON.ry[i];
      if (i) h += `<div class="r16-sep" id="${p}-sep${i}" style="left:${MON.x + 36}px;top:${y - 45.5}px;width:${MON.w - 72}px"></div>`;
      h += `<div class="r16-rn" id="${p}-rn-${k}" style="left:${MON.ax + 50}px;top:${y - 28}px"><b>${ROLE[k].n}</b><span>${ROLE[k].s}</span></div>`;
    });
    return h;
  };
  // ECG-ish trace path for one row: events = [[x, kind]] where kind "wake" = QRS spike then a working plateau until x2
  const trace = (segs, y0) => {
    // segs: list of [xStart, xEnd] working windows (spike at xStart); returns an SVG path d in panel-local coords (x absolute)
    let d = `M${MON.tx0} ${y0}`;
    for (const [a, b] of segs) {
      d += ` L${a} ${y0} L${a + 6} ${y0 - 8} L${a + 12} ${y0 + 4} L${a + 18} ${y0 - 34} L${a + 25} ${y0 + 20} L${a + 31} ${y0 - 6} L${a + 37} ${y0}`;
      // working plateau: a raised wavy band
      const w0 = a + 44, w1 = Math.max(w0 + 10, b - 8);
      d += ` C${w0 - 2} ${y0} ${w0 - 2} ${y0 - 14} ${w0 + 6} ${y0 - 14}`;
      for (let x = w0 + 6; x < w1 - 8; x += 16) d += ` Q${x + 4} ${y0 - 20} ${Math.min(x + 8, w1 - 8)} ${y0 - 14} T${Math.min(x + 16, w1 - 8)} ${y0 - 14}`;
      d += ` C${w1} ${y0 - 14} ${w1} ${y0} ${w1 + 8} ${y0}`;
    }
    d += ` L${MON.tx1} ${y0}`;
    return d;
  };


  // ---------------------------------------------------------------- EMPLOYEE ID CARD (s01 · s02 · cover): main card "Agent Konten" + two behind
  const idCards = (p) => {
    const card = (id, k, nm, cls) => `<div class="r16-id r16-card ${cls || ""}" id="${id}"><div class="hd"><div class="hi">${svg("bot", 2)}</div><b class="t">KARTU KARYAWAN AI</b><i>ILUSTRASI</i></div>` +
      `<div style="position:absolute;left:150px;top:252px">${av(id + "-av", k, 176)}</div>` + (nm || "") + `</div>`;
    return card(`${p}-b1`, "web", "", "r16-bk") + card(`${p}-b2`, "riset", "", "r16-bk") + card(`${p}-c`, "konten",
      `<b class="r16-id-nm r16-grad">Agent Konten</b><span class="r16-id-sb">AI agent · Claude Code</span>` +
      `<div class="r16-rw" style="top:204px"><span class="lb">JABATAN</span><i class="sk" id="${p}-k0"></i><div class="vl" id="${p}-v0"><div class="r16-ch"><i>${svg("pen-line", 2.2)}</i>Penulis konten</div></div></div>` +
      `<div class="r16-rw" style="top:290px"><span class="lb">ATASAN</span><i class="sk" id="${p}-k1"></i><div class="vl" id="${p}-v1"><div class="r16-boss">${av(p + "-bav", "ceo", 34)}Agent CEO</div></div></div>` +
      `<div class="r16-rw" style="top:376px"><span class="lb">GAJI</span><i class="sk" id="${p}-k2"></i><div class="vl" id="${p}-v2"><div class="r16-gj"><div class="co">${svg("coins", 2.2)}</div><b>Jatah token / bulan</b><div class="mt"><div class="mf" id="${p}-mf"></div></div></div></div></div>` +
      `<div class="r16-id-stp" id="${p}-stp">KARYAWAN AI</div>`);
  };
  const clipGlyph = (id) => `<div class="r16-clip" id="${id}"><i>${svg("paperclip", 2.1)}</i></div>`;


  // ---------------------------------------------------------------- MONITOR scaffolding shared by s06 + s07 (identical geometry)
  MON.p0 = 1.0; MON.p1 = 5.3;                                   // s06-local times of the playhead sweep (tx0 → tx1)
  const monX = (t) => MON.tx0 + Math.max(0, Math.min(1, (t - MON.p0) / (MON.p1 - MON.p0))) * (MON.tx1 - MON.tx0);
  const s06w = (w) => { const st = window.SCN.s06[0], x = window.VO_WORDS.find((v) => v[0] === w && v[1] >= st - 0.05); return x[1] - st; };
  // working windows per row (s06-local times → x): Web wakes on "tugas", Konten on "jadwal", both report on "lapor" → CEO wakes
  const monT = () => { const tT = s06w("tugas"), tJ = s06w("jadwal,"), tL = s06w("lapor,"), tTi = s06w("tidur");
    return { web: [[tT + 0.05, tL + 0.02]], konten: [[tJ + 0.08, tL + 0.08]], ceo: [[tL + 0.14, tTi + 0.12]], riset: [], desain: [] }; };
  const monSegs = () => { const T = monT(), o = {}; for (const k in T) o[k] = T[k].map(([a, b]) => [monX(a), monX(b)]); return o; };
  const monHead = (p, alt) => {
    const lay = (id, ic, t, sub, vis) => `<div class="r16-mh" id="${id}"><div class="mi">${svg(ic, 2.2)}</div><b class="r16-grad">${t}</b><span>${sub}</span></div>`;
    return lay(`${p}-hA`, "activity", "Heartbeat agent", "bangun → kerja → lapor → tidur") + (alt ? lay(`${p}-hB`, "coins", "Token &amp; budget", "jatah bulanan per agent · angka ilustrasi") : "");
  };
  const monTraces = (p) => {
    const S = monSegs(); let h = "";
    MON.rows.forEach((k, i) => {
      const y = MON.ry[i], top = y - 62;
      h += `<div class="r16-base" id="${p}-bs-${k}" style="left:${MON.tx0}px;top:${y - 1}px;width:${MON.tx1 - MON.tx0}px"></div>`;
      h += `<div class="r16-tw" id="${p}-tw-${k}" style="left:${MON.tx0 - 12}px;top:${top}px;width:${MON.tx1 - MON.tx0 + 24}px;height:100px">` +
        `<svg width="1080" height="100" viewBox="0 ${top} 1080 100" style="position:absolute;left:${-(MON.tx0 - 12)}px;top:0" fill="none">` +
        `<path d="${trace(S[k], y)}" stroke="${ROLE[k].c2}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg></div>`;
    });
    return h;
  };
  const PST = [["moon", "tidur", "#eef2f9", "#5d6f8f"], ["zap", "bangun", "#fff4d6", "#8a5a00"], ["activity", "kerja", "#e8f0ff", "#2f5fd6"], ["message-circle", "lapor", "#e8f7ee", "#1d7a3c"]];
  const monPills = (p) => MON.rows.map((k, i) => `<div class="r16-st" id="${p}-st-${k}" style="left:${MON.px}px;top:${MON.ry[i] - 22}px;width:${MON.pw}px">` +
    PST.map(([ic, t, bg, c], j) => `<div id="${p}-st-${k}-${j}" style="background:${bg};color:${c}">${svg(ic, 2.4)}${t}</div>`).join("") + `</div>`).join("");

  // ---------------------------------------------------------------- timeline boilerplate
  const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
  const scene = (ID) => {
    const ST = window.SCN[ID][0], D = window.SCN[ID][1], VW = window.VO_WORDS;
    const tl = gsap.timeline({ paused: true });
    { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); const cq = (q) => (typeof q === "number" ? Math.max(0, q) : q);
      tl.set = (a, v, q) => s0(a, _sc(v), cq(q)); tl.fromTo = (a, x, y, q) => f0(a, _sc(x), _sc(y), cq(q)); tl.to = (a, v, q) => t0(a, _sc(v), cq(q)); }
    const P0 = gsap.timeline(); tl.add(P0, 0);                 // every initial state lives here: nested, first child at 0
    const I = (el, v) => { gsap.set(el, _sc(v)); P0.set(el, _sc(v), 0); };
    const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), t);
    const L = (txt, after) => { const w = VW.find((x) => x[0] === txt && x[1] >= ST + (after || 0) - 0.05); if (!w) throw new Error(ID + ": word not found " + txt); return w[1] - ST; };
    const $ = (id) => document.getElementById(id);
    const done = () => {
      tl.set({}, {}, D - 0.01);
      (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
      tl.render(0, true, true);
      window.__timelines = window.__timelines || {};
      window.__timelines[ID] = tl;
    };
    // typed text: per-letter spans revealed between t0 and t1 (returns the spans)
    const type = (el, text, t0, t1) => {
      el.innerHTML = text.split("").map((c) => `<span>${c === " " ? "&nbsp;" : c}</span>`).join("");
      const sp = Array.from(el.children), n = sp.length;
      sp.forEach((s, i) => { I(s, { opacity: 0 }); tl.set(s, { opacity: 1 }, t0 + (t1 - t0) * (i / Math.max(1, n - 1))); });
      return sp;
    };
    // typed text that pushes an inline caret: letters are display:none until their time (Poppins, no measuring needed)
    const typeD = (el, text, t0, t1, caret) => {
      el.innerHTML = text.split("").map((c) => `<span>${c === " " ? "&nbsp;" : c}</span>`).join("") + (caret || "");
      const sp = Array.from(el.querySelectorAll("span")), n = sp.length;
      sp.forEach((s, i) => { I(s, { display: "none" }); tl.set(s, { display: "inline" }, t0 + (t1 - t0) * (i / Math.max(1, n - 1))); });
      return sp;
    };
    const shake = (el, t, a) => { a = a || 5; [[a, -a * 0.6], [-a * 0.8, a * 0.4], [a * 0.4, -a * 0.2], [0, 0]].forEach(([x, y], k) => tl.set(el, { x, y }, t + k * 0.034)); };
    return { ID, ST, D, tl, P0, I, ft, L, $, done, type, typeD, shake };
  };

  const css = `
  .r16-grad { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .r16-card { position: absolute; border-radius: 32px; background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 56px 90px -42px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); }
  .r16-card2 { position: absolute; background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 26px 46px -26px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); }
  .r16-tag { position: absolute; height: 28px; padding: 0 12px; border-radius: 14px; background: #ffffff; box-shadow: inset 0 0 0 1.5px #d9e2f0;
    font: 700 12px/28px Poppins, sans-serif; letter-spacing: .14em; color: #5d6f8f; white-space: nowrap; font-style: normal; }
  .r16-av { position: absolute; left: 0; top: 0; transform-origin: 50% 50%; }
  .r16-av .ci { position: absolute; inset: 0; border-radius: 50%; }
  .r16-av .bo { position: absolute; color: #ffffff; }
  .r16-av .bo svg { width: 100%; height: 100%; display: block; }
  .r16-av .rb { position: absolute; border-radius: 50%; background: #ffffff; box-shadow: 0 6px 12px -5px rgba(10,13,44,.5); }
  .r16-av .rb i { position: absolute; display: block; }
  .r16-av .rb svg { width: 100%; height: 100%; display: block; }
  .r16-node { position: absolute; width: 0; height: 0; transform-origin: 0 0; }
  .r16-node .nl { position: absolute; left: -130px; width: 260px; text-align: center; }
  .r16-node .nl b { display: block; font: 700 25px/32px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .r16-node .nl span { display: block; font: 400 16px/22px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .r16-ln { position: absolute; border-radius: 2px; background: #9fb2cf; transform-origin: 50% 0%; }
  .r16-goal { border-radius: 28px; transform-origin: 50% 50%; }
  .r16-goal .gi { position: absolute; left: 18px; top: 16px; width: 56px; height: 56px; border-radius: 18px; background: linear-gradient(150deg, #ffcf4d, #e39a00); color: #ffffff;
    box-shadow: 0 10px 18px -10px rgba(227,154,0,.9); }
  .r16-goal .gi svg { position: absolute; left: 13px; top: 13px; width: 30px; height: 30px; display: block; }
  .r16-goal .gl { position: absolute; left: 92px; top: 13px; font: 700 14px/22px Poppins, sans-serif; letter-spacing: .12em; color: #5d6f8f; white-space: nowrap; }
  .r16-goal .gt { position: absolute; left: 92px; top: 37px; font: 700 28px/38px Poppins, sans-serif; white-space: nowrap; letter-spacing: -.01em; }
  .r16-goal .r16-tag { position: relative; display: inline-block; margin-left: 10px; top: -1px; height: 22px; padding: 0 9px; border-radius: 11px; font-size: 10.5px; line-height: 22px; vertical-align: top; }
  .r16-kamu { border-radius: 32px; transform-origin: 50% 50%; }
  .r16-kamu .ka { position: absolute; left: 10px; top: 10px; width: 44px; height: 44px; border-radius: 50%; background: linear-gradient(150deg, #294b77, #0a0d2c); color: #fff; }
  .r16-kamu .ka svg { position: absolute; left: 11px; top: 11px; width: 22px; height: 22px; display: block; }
  .r16-kamu b { position: absolute; left: 66px; top: 7px; font: 700 21px/28px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .r16-kamu span { position: absolute; left: 66px; top: 33px; font: 400 14px/20px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .r16-tka { position: absolute; width: 0; height: 0; }
  .r16-tk { position: absolute; left: 0; top: 0; height: 40px; padding: 0 16px 0 44px; border-radius: 20px; background: #ffffff; box-shadow: 0 12px 22px -14px rgba(10,13,44,.6), 0 0 0 1.5px #dfe6f2;
    font: 700 16px/40px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; transform: translateX(-50%); }
  .r16-tk i { position: absolute; left: 14px; top: 10px; width: 20px; height: 20px; color: #294b77; }
  .r16-tk svg { width: 20px; height: 20px; display: block; }
  .r16-mon { transform-origin: 50% 50%; }
  .r16-sep { position: absolute; height: 1.5px; background: #e6ecf6; }
  .r16-rn { position: absolute; width: 150px; }
  .r16-rn b { display: block; font: 700 20px/27px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .r16-rn span { display: block; font: 400 14px/20px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .r16-st { position: absolute; height: 44px; border-radius: 22px; overflow: hidden; }
  .r16-st > div { position: absolute; inset: 0; border-radius: 22px; display: flex; align-items: center; justify-content: center; gap: 8px; font: 700 17px/44px Poppins, sans-serif; white-space: nowrap; }
  .r16-st svg { width: 19px; height: 19px; display: block; }
  /* employee ID cards (main + two behind, a hint of a team) */
  .r16-id { left: 170px; top: 376px; width: 740px; height: 468px; transform-origin: 50% 100%; font-family: Poppins, sans-serif; }
  .r16-id .hd { position: absolute; left: 0; top: 0; width: 740px; height: 74px; border-radius: 32px 32px 0 0; background-color: #1a2c51; background-image: linear-gradient(135deg, #0a0d2c, #294b77); }
  .r16-id .hd b { position: absolute; left: 34px; top: 0; font: 700 18px/74px Poppins, sans-serif; letter-spacing: .2em; color: #ffffff; white-space: nowrap; }
  .r16-id .hd .hi { position: absolute; left: 34px; top: 23px; width: 28px; height: 28px; color: #8fd8ff; }
  .r16-id .hd .hi svg { width: 28px; height: 28px; display: block; }
  .r16-id .hd b.t { left: 76px; }
  .r16-id .hd i { position: absolute; right: 26px; top: 21px; height: 32px; padding: 0 14px; border-radius: 16px; background-color: #3a4a6c; font: 700 13px/32px Poppins, sans-serif;
    letter-spacing: .14em; color: rgba(227,237,250,.9); font-style: normal; white-space: nowrap; }
  .r16-bk { opacity: .9; }
  .r16-bk .hd { background-color: #44587e; background-image: linear-gradient(135deg, #3b4f74, #5a7099); }
  .r16-id-nm { left: 274px; top: 104px; font: 700 40px/50px Poppins, sans-serif; white-space: nowrap; letter-spacing: -.01em; }
  .r16-id-sb { left: 276px; top: 154px; font: 400 18px/26px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .r16-rw { position: absolute; left: 276px; width: 430px; height: 80px; }
  .r16-rw .lb { position: absolute; left: 0; top: 0; font: 700 14px/20px Poppins, sans-serif; letter-spacing: .16em; color: #5d6f8f; white-space: nowrap; }
  .r16-rw .sk { position: absolute; left: 0; top: 30px; width: 300px; height: 22px; border-radius: 11px; background: linear-gradient(90deg, #e9eef7, #f3f6fb, #e9eef7); }
  .r16-rw .vl { position: absolute; left: 0; top: 24px; height: 44px; display: flex; align-items: center; gap: 10px; white-space: nowrap; }
  .r16-ch { height: 44px; padding: 0 18px 0 44px; border-radius: 22px; background: #fff1ea; box-shadow: inset 0 0 0 1.5px #ffd2bd; font: 700 19px/44px Poppins, sans-serif; color: #a23e14; position: relative; }
  .r16-ch i { position: absolute; left: 14px; top: 11px; width: 22px; height: 22px; }
  .r16-ch svg { width: 22px; height: 22px; display: block; }
  .r16-boss { position: relative; height: 44px; padding: 0 18px 0 52px; border-radius: 22px; background: #fff8e3; box-shadow: inset 0 0 0 1.5px #ffe2a0; font: 700 19px/44px Poppins, sans-serif; color: #7a5200; }
  .r16-boss .r16-av { left: 22px; top: 22px; }
  .r16-gj { position: relative; height: 44px; display: flex; align-items: center; gap: 12px; }
  .r16-gj .co { position: relative; width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(150deg, #ffcf4d, #e39a00); color: #fff; box-shadow: 0 8px 14px -8px rgba(227,154,0,.9); flex: none; }
  .r16-gj .co svg { position: absolute; left: 9px; top: 9px; width: 22px; height: 22px; display: block; }
  .r16-gj b { font: 700 19px/24px Poppins, sans-serif; color: #0a0d2c; }
  .r16-gj .mt { position: relative; width: 130px; height: 14px; border-radius: 7px; background: #e6ecf6; overflow: hidden; flex: none; }
  .r16-gj .mf { position: absolute; left: 0; top: 0; width: 130px; height: 14px; border-radius: 7px; background: linear-gradient(90deg, #ffcf4d, #e39a00); transform-origin: 0 50%; }
  .r16-id-stp { left: 22px; top: 346px; height: 58px; padding: 0 16px; border-radius: 14px; box-shadow: inset 0 0 0 4px #2da44e; color: #2da44e; font: 700 22px/58px Poppins, sans-serif;
    letter-spacing: .1em; white-space: nowrap; transform-origin: 50% 50%; background: rgba(255,255,255,.9); }
  .r16-id, .r16-id-nm, .r16-id-sb, .r16-id-stp { position: absolute; }
  .r16-clip { position: absolute; left: 0; top: 0; width: 0; height: 0; }
  .r16-clip i { position: absolute; left: -64px; top: -64px; width: 128px; height: 128px; color: #6f83a8; filter: drop-shadow(0 8px 8px rgba(10,13,44,.28)); }
  .r16-clip svg { width: 128px; height: 128px; display: block; }
  .r16-mh { position: absolute; left: 116px; top: 338px; width: 560px; height: 70px; }
  .r16-mh .mi { position: absolute; left: 0; top: 4px; width: 58px; height: 58px; border-radius: 18px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #8fd8ff; }
  .r16-mh .mi svg { position: absolute; left: 15px; top: 15px; width: 28px; height: 28px; display: block; }
  .r16-mh b { position: absolute; left: 74px; top: -2px; font: 700 31px/42px Poppins, sans-serif; white-space: nowrap; letter-spacing: -.01em; }
  .r16-mh span { position: absolute; left: 75px; top: 38px; font: 400 16px/24px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .r16-base { position: absolute; height: 2px; background-image: linear-gradient(90deg, #d7e0ee 55%, transparent 55%); background-size: 10px 2px; }
  .r16-tw { position: absolute; overflow: hidden; }
  `;
  const st = document.createElement("style"); st.textContent = css; (document.head || document.documentElement).appendChild(st);
  window.R16 = { ICO, svg, ROLE, av, ORG, org, goalIn, GOALTXT, MON, mon, trace, monX, monT, monSegs, monHead, monTraces, monPills, PST, scene, _sc, idCards, clipGlyph };
})();

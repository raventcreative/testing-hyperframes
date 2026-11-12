// Shared visual system of R18 ("Gladi resik reels sebelum posting" — Virality Predictor by Higgsfield as a Claude Code plugin), loaded in
// <head> before every scene (after vendor/r18icons.js). Our own design in the AI PRENEUR LIGHT house style. Metaphor of the reel: a
// GLADI RESIK (dress rehearsal) — your draft reel plays on a small stage in front of AI viewers before the real audience sees it; the
// result comes back as a RAPOR (school report card). No Higgsfield / Claude logos or UI are reproduced (names as text only); the reel
// in the demos is a fictional UMKM product ("Sambal Bawang", labelled CONTOH); every score is illustrative.
// - K.svg(k, sw)            lucide icon (inline, currentColor)
// - K.reel(id, o)           the draft reel card (9:16): our own flat illustration of a sambal jar, caption bars, DRAFT chip
// - K.viewer(id, o)         an "AI viewer" (navy head, two eyes, sparkle badge) or a real person (o.real: user glyph, colour)
// - K.scene(ID)             timeline boilerplate: seek-safe scale shorthand, every initial state pinned at 0 in a NESTED timeline that is
//                           the first child at 0 (I), fromTo without immediate render (ft), word lookup (L), typed text (type), shake,
//                           and done() = end marker + backward-seek patch + tl.render(0, true, true) + registration.
(function () {
  const ICO = window.R18_ICO;
  const svg = (k, sw, cls) => `<svg class="${cls || ""}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[k] || ""}</svg>`;

  const CSS = `
  .k-grad { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .k-card { background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 40px 70px -40px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); }
  .k-a { position: absolute; }
  .k-eb { font: 700 15px/22px Poppins, sans-serif; letter-spacing: .16em; color: #5d6f8f; white-space: nowrap; }
  .k-ic { width: 72px; height: 72px; border-radius: 22px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff; box-shadow: 0 14px 24px -14px rgba(10,13,44,.8); }
  .k-ic svg { position: absolute; left: 18px; top: 18px; width: 36px; height: 36px; display: block; }
  .k-chip { position: absolute; height: 54px; padding: 0 22px 0 56px; border-radius: 27px; background: #ffffff; color: #0a0d2c; white-space: nowrap; font: 700 22px/54px Poppins, sans-serif;
    box-shadow: 0 16px 26px -16px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); transform-origin: 50% 50%; }
  .k-chip svg { position: absolute; left: 18px; top: 14px; width: 26px; height: 26px; display: block; color: #294b77; }
  .k-chip.ok { background: #e8f6ed; color: #1f7a3a; box-shadow: inset 0 0 0 1.5px rgba(31,122,58,.22); }
  .k-chip.ok svg { color: #1f7a3a; }
  .k-chip.info { background: #eaf0fe; color: #2a55c4; box-shadow: inset 0 0 0 1.5px rgba(42,85,196,.22); }
  .k-chip.info svg { color: #2a55c4; }
  .k-chip.warn { background: #fff3dc; color: #94540a; box-shadow: inset 0 0 0 1.5px rgba(148,84,10,.25); }
  .k-chip.warn svg { color: #94540a; }
  .k-ex { position: absolute; height: 30px; padding: 0 12px; border-radius: 15px; background: #ffffff; box-shadow: inset 0 0 0 1.5px #d9e2f0; font: 700 12px/30px Poppins, sans-serif; letter-spacing: .14em; color: #5d6f8f; white-space: nowrap; }
  .k-stamp { position: absolute; padding: 0 22px; height: 64px; border-radius: 14px; font: 700 30px/58px Poppins, sans-serif; letter-spacing: .12em; white-space: nowrap; transform-origin: 50% 50%;
    border: 4px solid currentColor; background: rgba(255,255,255,.88); }
  .k-stamp.navy { color: #294b77; } .k-stamp.green { color: #1f8a43; } .k-stamp.amber { color: #b46a07; }
  .k-btn { position: absolute; height: 72px; border-radius: 36px; padding: 0 34px 0 74px; font: 700 28px/72px Poppins, sans-serif; color: #ffffff; white-space: nowrap; transform-origin: 50% 50%;
    background: linear-gradient(150deg, #4a7ff0, #294b77); box-shadow: 0 18px 30px -16px rgba(58,111,224,.95); }
  .k-btn svg { position: absolute; left: 30px; top: 20px; width: 32px; height: 32px; display: block; }
  .k-cur { position: absolute; left: 0; top: 0; width: 0; height: 0; }
  .k-cur svg { position: absolute; left: -6px; top: -4px; width: 56px; height: 56px; overflow: visible; filter: drop-shadow(0 6px 8px rgba(10,13,44,.35)); }
  /* the draft reel (9:16) */
  .k-rl { position: absolute; border-radius: 26px; overflow: hidden; transform-origin: 50% 50%; background: linear-gradient(170deg, #ffb46b 0%, #f2683c 58%, #c93b2b 100%);
    box-shadow: 0 36px 60px -30px rgba(10,13,44,.6), 0 0 0 4px #ffffff, 0 0 0 5.5px rgba(10,13,44,.08); }
  .k-rl > * { position: absolute; }
  .k-rl .sh { left: -20%; top: 52%; width: 140%; height: 60%; border-radius: 50%; background: radial-gradient(closest-side, rgba(120,20,10,.35), rgba(120,20,10,0)); }
  .k-rl .jar { left: 27%; top: 30%; width: 46%; height: 40%; border-radius: 16% 16% 20% 20%; background: linear-gradient(90deg, #b8241a, #e2442f 45%, #a91f17);
    box-shadow: inset 0 -10px 18px rgba(80,0,0,.25); }
  .k-rl .lid { left: 30%; top: 24%; width: 40%; height: 8%; border-radius: 10px 10px 4px 4px; background: linear-gradient(180deg, #3a3f55, #1c2033); }
  .k-rl .lbl { left: 29%; top: 41%; width: 42%; height: 17%; border-radius: 8px; background: #fff7ea; }
  .k-rl .lbl b { position: absolute; left: 0; right: 0; top: 16%; text-align: center; font: 700 .74em/1.1 Poppins, sans-serif; color: #b8241a; letter-spacing: .02em; }
  .k-rl .lbl i { position: absolute; left: 0; right: 0; top: 58%; text-align: center; font: 400 .62em/1 Poppins, sans-serif; font-style: normal; color: #7a4a2a; }
  .k-rl .chili { left: 64%; top: 18%; width: 22%; height: 22%; color: #fff3d6; transform: rotate(18deg); }
  .k-rl .chili svg { width: 100%; height: 100%; display: block; }
  .k-rl .cap1, .k-rl .cap2 { left: 12%; height: 4.2%; border-radius: 99px; background: rgba(255,255,255,.92); }
  .k-rl .cap1 { top: 77%; width: 76%; } .k-rl .cap2 { top: 83.5%; width: 52%; left: 24%; background: rgba(255,255,255,.7); }
  .k-rl .bar { left: 8%; bottom: 4%; width: 84%; height: 1.6%; border-radius: 99px; background: rgba(255,255,255,.35); }
  .k-rl .bar i { position: absolute; left: 0; top: 0; height: 100%; width: 30%; border-radius: 99px; background: #ffffff; }
  .k-rl .dft { left: 7%; top: 4.5%; height: 9%; padding: 0 .7em; border-radius: 99px; background: rgba(10,13,44,.78); color: #fff; font: 700 .6em/1 Poppins, sans-serif; letter-spacing: .14em;
    display: flex; align-items: center; white-space: nowrap; }
  /* viewers */
  .k-vw { position: absolute; transform-origin: 50% 100%; }
  .k-vw .hd { position: absolute; left: 0; top: 0; border-radius: 50%; background: linear-gradient(150deg, #3b5f92, #0a0d2c); box-shadow: 0 10px 18px -10px rgba(10,13,44,.8); }
  .k-vw .ey { position: absolute; border-radius: 50%; background: #ffffff; }
  .k-vw .ey i { position: absolute; border-radius: 50%; background: #0a0d2c; }
  .k-vw .sp { position: absolute; border-radius: 50%; background: #ffffff; color: #3a6fe0; box-shadow: 0 4px 10px -4px rgba(10,13,44,.6), 0 0 0 1.5px rgba(58,111,224,.25); }
  .k-vw .sp svg { position: absolute; left: 18%; top: 18%; width: 64%; height: 64%; display: block; }
  .k-vw.real .hd { background: var(--c, #f2a65a); }
  .k-vw.real .hd svg { position: absolute; left: 20%; top: 18%; width: 60%; height: 60%; color: #ffffff; display: block; }
  `;
  if (!document.getElementById("k-css")) { const st = document.createElement("style"); st.id = "k-css"; st.textContent = CSS; document.head.appendChild(st); }

  // the draft reel: o = { x, y, w, fs (label font px), draft (text or ""), sub (label 2nd line) }
  const reel = (id, o) => {
    const w = o.w, h = Math.round(w * 16 / 9);
    return `<div class="k-rl" id="${id}" style="left:${o.x}px;top:${o.y}px;width:${w}px;height:${h}px;font-size:${o.fs || Math.round(w / 10)}px">` +
      `<div class="sh"></div><div class="chili">${svg("flame", 2)}</div><div class="lid"></div><div class="jar"></div>` +
      `<div class="lbl"><b>SAMBAL</b><i>${o.sub || "bawang"}</i></div><div class="cap1"></div><div class="cap2"></div>` +
      `<div class="bar"><i id="${id}-pg"></i></div>` + (o.draft === "" ? "" : `<div class="dft">${o.draft || "DRAFT"}</div>`) + `</div>`;
  };
  // an AI viewer: o = { x, y, s (head size), real, c (colour for real people), look (pupil dx) }
  const viewer = (id, o) => {
    const s = o.s, e = Math.round(s * 0.2), p = Math.round(e * 0.55);
    if (o.real) return `<div class="k-vw real" id="${id}" style="left:${o.x}px;top:${o.y}px;width:${s}px;height:${s}px;--c:${o.c}"><div class="hd" style="width:${s}px;height:${s}px">${svg("user", 2.2)}</div></div>`;
    const ey = (cx) => `<div class="ey" style="left:${cx - e / 2}px;top:${Math.round(s * 0.36)}px;width:${e}px;height:${Math.round(e * 1.15)}px"><i id="${id}-p${cx < s / 2 ? "l" : "r"}" style="left:${(e - p) / 2}px;top:${Math.round((e * 1.15 - p) / 2)}px;width:${p}px;height:${p}px"></i></div>`;
    const b = Math.round(s * 0.42);
    return `<div class="k-vw" id="${id}" style="left:${o.x}px;top:${o.y}px;width:${s}px;height:${s}px"><div class="hd" style="width:${s}px;height:${s}px">` +
      ey(Math.round(s * 0.36)) + ey(Math.round(s * 0.64)) + `</div><div class="sp" id="${id}-sp" style="left:${s - b * 0.8}px;top:${-b * 0.2}px;width:${b}px;height:${b}px">${svg("sparkles", 2.2)}</div></div>`;
  };

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
    const shake = (el, t, a) => { a = a || 5; [[a, -a * 0.6], [-a * 0.8, a * 0.4], [a * 0.4, -a * 0.2], [0, 0]].forEach(([x, y], k) => tl.set(el, { x, y }, t + k * 0.034)); };
    // pop in (scale + fade) and the shared scene exit
    const pop = (el, t, o) => { o = o || {}; const s0 = o.s0 == null ? 0.6 : o.s0; I(el, { opacity: 0, scale: s0, y: o.y || 0 });
      ft(el, { opacity: 0, scale: s0, y: o.y || 0 }, { opacity: 1, scale: 1, y: 0, duration: o.d || 0.3, ease: o.ease || "back.out(1.8)" }, t); };
    const out = (el, t) => ft(el, { opacity: 1, y: 0 }, { opacity: 0, y: -26, duration: 0.2, ease: "power2.in" }, t == null ? D - 0.24 : t);
    return { ID, ST, D, tl, P0, I, ft, L, $, done, type, shake, pop, out };
  };

  window.K = { svg, ICO, reel, viewer, scene };
})();

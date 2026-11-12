// Shared visual system of R20 ("Claude Code pakai model AI gratis — FreeLLMAPI"), loaded in <head> before every scene
// (after vendor/r20icons.js). Everything is our own design in the AI PRENEUR LIGHT house style. No third-party logos or UI:
// Claude Code / FreeLLMAPI / providers appear as TEXT + generic lucide icons (ISC). Quota bars, files and chats are illustrative.
// Metaphors of the reel: the app (Claude Code) is the BODY, the model is the BRAIN; FreeLLMAPI is a small SERVER BOX on your laptop
// that understands Claude's API format and passes each request on ("dioper") to whichever provider still has FREE QUOTA left
// ("sisa jatah gratis", like checking the remaining data quota on a phone).
// - K.svg(k, sw)        lucide icon markup (currentColor)
// - K.P                 the providers shown (text only, from the FreeLLMAPI README's provider list)
// - K.term(p, o)        "Claude Code" app window (white card + navy terminal body); ids p-tm, p-ty (typed line), p-bd (body)
// - K.box(p, o)         the mini server box "FreeLLMAPI · localhost:3001"; ids p-bx, p-led0..2, p-bxl (label)
// - K.quota(p, o)       "Sisa jatah gratis" panel with one row per provider; ids p-q, p-qr<i>, p-qf<i> (bar fill), p-qs<i>-<state>
// - K.laptop(p, o)      a simple laptop (screen + base); ids p-lp, p-scr (screen content box)
// - K.boot(ID)          timeline boilerplate: seek-safe scale shorthand; EVERY initial state pinned at 0 in a NESTED timeline P0 that is
//                       the first child of the scene timeline at 0 (I); fromTo without immediate render (ft); word lookup (L, throws if a
//                       word is missing); typeD (typed text with caret); shake; pop; done() = end marker + backward-seek patch +
//                       tl.render(0, true, true) + registration.
(function () {
  const ICO = window.R20_ICO;
  const svg = (k, sw, cls) => `<svg class="${cls || ""}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[k]}</svg>`;

  // providers named in the VO + two more from the README's provider table (github.com/tashfeenahmed/freellmapi, checked 2026-11-12)
  const P = [
    { n: "Google", pct: 0.86 },
    { n: "Groq", pct: 0.72 },
    { n: "Mistral", pct: 0.64 },
    { n: "Cerebras", pct: 0.58 },
  ];

  const CSS = `
  .k-grad { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .k-card { background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 40px 70px -40px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); }
  .k-a { position: absolute; }
  /* ---------------- Claude Code app window */
  .k-tm { position: absolute; border-radius: 28px; font-family: Poppins, sans-serif; transform-origin: 50% 50%; overflow: hidden; }
  .k-tm > * { position: absolute; }
  .k-tm .bar { left: 0; top: 0; right: 0; height: 64px; }
  .k-tm .dots { left: 24px; top: 26px; width: 60px; height: 14px; }
  .k-tm .dots i { position: absolute; top: 0; width: 14px; height: 14px; border-radius: 50%; background: #d7deeb; }
  .k-tm .ti { left: 96px; top: 13px; height: 38px; display: flex; align-items: center; gap: 10px; font: 700 24px/38px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .k-tm .ti svg { width: 28px; height: 28px; display: block; color: #294b77; flex: none; }
  .k-tm .tg { right: 22px; top: 16px; height: 32px; padding: 0 14px; border-radius: 16px; background: #eef2f9; color: #5d6f8f; font: 700 14px/32px Poppins, sans-serif; letter-spacing: .12em; white-space: nowrap; }
  .k-tm .bd { left: 14px; right: 14px; top: 64px; bottom: 14px; border-radius: 18px; background: linear-gradient(160deg, #111a44, #0a0d2c 70%); box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.06); overflow: hidden; }
  .k-tm .ln { position: absolute; left: 26px; font: 400 23px/34px Poppins, sans-serif; color: #c9d6f2; white-space: nowrap; }
  .k-tm .ln b { font-weight: 700; color: #8fd8ff; }
  .k-tm .ln em { font-style: normal; color: #7f8db0; }
  .k-tm .ty { position: absolute; left: 26px; font: 400 23px/34px Poppins, sans-serif; color: #ffffff; white-space: nowrap; }
  .k-tm .ty b { font-weight: 700; color: #8fd8ff; }
  .k-caret { display: inline-block; width: 12px; height: 26px; margin-left: 4px; vertical-align: -4px; border-radius: 2px; background: #8fd8ff; }
  /* ---------------- the mini server box */
  .k-bx { position: absolute; font-family: Poppins, sans-serif; transform-origin: 50% 60%; }
  .k-bx > * { position: absolute; }
  .k-bx .body { left: 0; top: 0; border-radius: 30px; background: linear-gradient(160deg, #3a5f95, #1b2f5c 55%, #0a0d2c); box-shadow: 0 34px 50px -26px rgba(10,13,44,.75), inset 0 2px 0 rgba(255,255,255,.18); }
  .k-bx .slot { left: 22px; right: 22px; height: 30%; border-radius: 16px; background: rgba(255,255,255,.08); box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.12); }
  .k-bx .led { position: absolute; left: 20px; top: 50%; width: 16px; height: 16px; margin-top: -8px; border-radius: 50%; background: #4ee08a; box-shadow: 0 0 12px rgba(78,224,138,.95); }
  .k-bx .vent { position: absolute; right: 18px; top: 50%; height: 6px; margin-top: -3px; border-radius: 3px; background: rgba(255,255,255,.22); }
  .k-bx .nm { left: 0; width: 100%; text-align: center; font: 700 30px/40px Poppins, sans-serif; color: #ffffff; white-space: nowrap; letter-spacing: .01em; }
  .k-bx .ad { left: 0; width: 100%; text-align: center; font: 400 18px/24px Poppins, sans-serif; color: #8fd8ff; white-space: nowrap; }
  /* ---------------- "Sisa jatah gratis" panel */
  .k-q { position: absolute; border-radius: 32px; font-family: Poppins, sans-serif; transform-origin: 50% 50%; }
  .k-q > * { position: absolute; }
  .k-q .hi { left: 26px; top: 24px; width: 64px; height: 64px; border-radius: 20px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff; }
  .k-q .hi svg { position: absolute; left: 16px; top: 16px; width: 32px; height: 32px; display: block; }
  .k-q .ht { left: 108px; top: 22px; font: 700 32px/42px Poppins, sans-serif; white-space: nowrap; padding-right: 4px; }
  .k-q .hs { left: 110px; top: 62px; font: 400 18px/24px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .k-q .ex { right: 26px; top: 30px; height: 30px; padding: 0 12px; border-radius: 15px; background: #ffffff; box-shadow: inset 0 0 0 1.5px #d9e2f0; font: 700 12px/30px Poppins, sans-serif; letter-spacing: .14em; color: #5d6f8f; white-space: nowrap; }
  .k-qr { position: absolute; left: 22px; right: 22px; height: 78px; border-radius: 20px; background: #f4f7fc; box-shadow: inset 0 0 0 1.5px #e3e9f4; transform-origin: 50% 50%; }
  .k-qr > * { position: absolute; }
  .k-qr .rg { left: -3px; top: -3px; right: -3px; bottom: -3px; border-radius: 22px; box-shadow: 0 0 0 4px #3a6fe0, 0 12px 26px -10px rgba(58,111,224,.55); }
  .k-qr .pn { left: 24px; top: 0; font: 700 26px/78px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .k-qr .tr { left: 210px; top: 32px; width: 380px; height: 14px; border-radius: 7px; background: #e1e8f3; overflow: hidden; }
  .k-qr .fl { position: absolute; left: 0; top: 0; width: 380px; height: 14px; border-radius: 7px; background: linear-gradient(90deg, #2da44e, #5fd07f); transform-origin: 0 50%; }
  .k-qr .fl.lo { background: linear-gradient(90deg, #d9534f, #f08a6a); }
  .k-qr.more { background: transparent; box-shadow: inset 0 0 0 2px #d5deec; }
  .k-qr.more .pn { color: #294b77; }
  .k-qr .mo { right: 26px; top: 0; font: 400 19px/78px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .k-qr .st { right: 18px; top: 19px; height: 40px; padding: 0 16px 0 40px; border-radius: 20px; font: 700 17px/40px Poppins, sans-serif; white-space: nowrap; }
  .k-qr .st svg { position: absolute; left: 14px; top: 11px; width: 18px; height: 18px; display: block; }
  .k-qr .st.idle { background: #ffffff; color: #5d6f8f; box-shadow: inset 0 0 0 1.5px #dbe3f0; }
  .k-qr .st.on { background: #3a6fe0; color: #ffffff; }
  .k-qr .st.ok { background: #e8f6ed; color: #1f7a3a; }
  .k-qr .st.bad { background: #fdeaea; color: #b4322f; }
  /* ---------------- laptop */
  .k-lp { position: absolute; transform-origin: 50% 100%; }
  .k-lp > * { position: absolute; }
  .k-lp .lid { left: 0; top: 0; border-radius: 26px 26px 10px 10px; background: linear-gradient(180deg, #24355f, #0a0d2c); box-shadow: 0 30px 50px -30px rgba(10,13,44,.7); }
  .k-lp .scr { border-radius: 14px; background: linear-gradient(180deg, #f9fbff, #eaf0fa); overflow: hidden; }
  .k-lp .base { border-radius: 4px 4px 22px 22px; background: linear-gradient(180deg, #dbe3f0, #b8c5da); box-shadow: 0 18px 26px -16px rgba(10,13,44,.6); }
  .k-lp .notch { border-radius: 0 0 10px 10px; background: #a9b7cf; }
  /* ---------------- chips, stamps, footnotes */
  .k-chip { position: absolute; height: 54px; padding: 0 22px 0 56px; border-radius: 27px; background: #ffffff; color: #0a0d2c; white-space: nowrap; font: 700 22px/54px Poppins, sans-serif;
    box-shadow: 0 16px 26px -16px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); transform-origin: 50% 50%; }
  .k-chip svg { position: absolute; left: 18px; top: 14px; width: 26px; height: 26px; display: block; color: #294b77; }
  .k-chip.ok { background: #e8f6ed; color: #1f7a3a; box-shadow: inset 0 0 0 1.5px rgba(31,122,58,.22); } .k-chip.ok svg { color: #1f7a3a; }
  .k-chip.info { background: #eaf0fe; color: #2a55c4; box-shadow: inset 0 0 0 1.5px rgba(42,85,196,.22); } .k-chip.info svg { color: #2a55c4; }
  .k-chip.warn { background: #fff3dc; color: #8a4d08; box-shadow: inset 0 0 0 1.5px rgba(148,84,10,.25); } .k-chip.warn svg { color: #8a4d08; }
  .k-chip.bad { background: #fdeaea; color: #b4322f; box-shadow: inset 0 0 0 1.5px rgba(180,50,47,.22); } .k-chip.bad svg { color: #b4322f; }
  .k-chip.navy { background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff; box-shadow: 0 16px 26px -14px rgba(10,13,44,.8); } .k-chip.navy svg { color: #8fd8ff; }
  .k-stamp { position: absolute; height: 72px; padding: 0 22px; border-radius: 14px; border: 5px solid #1f7a3a; color: #1f7a3a; background: rgba(232,246,237,.92);
    font: 700 34px/62px Poppins, sans-serif; letter-spacing: .1em; text-indent: .1em; white-space: nowrap; transform-origin: 50% 50%; }
  .k-stamp.bad { border-color: #b4322f; color: #b4322f; background: rgba(253,234,234,.94); }
  .k-stamp.warn { border-color: #94540a; color: #94540a; background: rgba(255,243,220,.94); }
  .k-fn { position: absolute; height: 40px; padding: 0 16px 0 44px; border-radius: 20px; background: rgba(255,255,255,.92); box-shadow: inset 0 0 0 1.5px #d9e2f0; color: #5d6f8f;
    font: 400 17px/40px Poppins, sans-serif; white-space: nowrap; }
  .k-fn b { font-weight: 700; color: #294b77; }
  .k-fn svg { position: absolute; left: 14px; top: 10px; width: 20px; height: 20px; display: block; color: #294b77; }
  .k-ok { position: absolute; width: 40px; height: 40px; border-radius: 50%; background: #2da44e; color: #ffffff; box-shadow: 0 0 0 4px #ffffff, 0 10px 18px -8px rgba(31,122,58,.8); }
  .k-ok svg { position: absolute; left: 9px; top: 9px; width: 22px; height: 22px; display: block; }
  .k-no { position: absolute; width: 40px; height: 40px; border-radius: 50%; background: #d9534f; color: #ffffff; box-shadow: 0 0 0 4px #ffffff, 0 10px 18px -8px rgba(180,50,47,.8); }
  .k-no svg { position: absolute; left: 9px; top: 9px; width: 22px; height: 22px; display: block; }
  .k-glow { position: absolute; border-radius: 50%; background: radial-gradient(closest-side, rgba(255,255,255,.95), rgba(255,255,255,0)); }
  `;
  if (!document.getElementById("k-css")) { const st = document.createElement("style"); st.id = "k-css"; st.textContent = CSS; (document.head || document.documentElement).appendChild(st); }

  // Claude Code app window. o: {x, y, w, h, tag, lines: [html...], ty: true}
  const term = (p, o) => {
    const fs = o.fs || 23, lh = o.lh || 38, t0 = o.t0 == null ? 18 : o.t0, f = `font-size:${fs}px;line-height:${Math.round(fs * 1.48)}px`;
    const lines = (o.lines || []).map((l, i) => `<div class="ln" id="${p}-l${i}" style="top:${t0 + i * lh}px;${f}">${l}</div>`).join("");
    const ty = o.ty ? `<div class="ty" id="${p}-ty" style="top:${t0 + (o.lines || []).length * lh}px;${f}"></div>` : "";
    return `<div class="k-tm k-card" id="${p}-tm" style="left:${o.x}px;top:${o.y}px;width:${o.w}px;height:${o.h}px">` +
      `<div class="bar"></div><div class="dots"><i style="left:0"></i><i style="left:22px"></i><i style="left:44px"></i></div>` +
      `<div class="ti">${svg("square-terminal", 2.2)}Claude Code</div>${o.tag ? `<div class="tg" id="${p}-tg">${o.tag}</div>` : ""}` +
      `<div class="bd" id="${p}-bd">${lines}${ty}</div></div>`;
  };
  // the mini server box. o: {x, y, w, h}
  const box = (p, o) => {
    const w = o.w || 300, h = o.h || 200, bh = Math.round(h * 0.62), sh = Math.round(bh * 0.3), gap = Math.round((bh - 2 * sh) / 3);
    const vent = (k) => [0, 1, 2].map((j) => `<i class="vent" style="width:${[46, 32, 20][j]}px;right:${18 + j * 54}px"></i>`).join("");
    return `<div class="k-bx" id="${p}-bx" style="left:${o.x}px;top:${o.y}px;width:${w}px;height:${h}px">` +
      `<div class="body" style="width:${w}px;height:${h}px"></div>` +
      `<div class="slot" style="top:${gap}px"><i class="led" id="${p}-led0"></i>${vent(0)}</div>` +
      `<div class="slot" style="top:${2 * gap + sh}px"><i class="led" id="${p}-led1"></i>${vent(1)}</div>` +
      `<div class="nm" id="${p}-bxl" style="top:${bh + 8}px">FreeLLMAPI</div><div class="ad" style="top:${bh + 46}px">localhost:3001</div></div>`;
  };
  // "Sisa jatah gratis" panel. o: {x, y, w, rows: [{n, pct}], sub}
  const quota = (p, o) => {
    const rows = o.rows || P;
    const rh = o.rh || 78, rs = o.rs || 92, r0 = o.r0 || 112, sty = (rh - 40) / 2;
    let h = `<div class="k-q k-card" id="${p}-q" style="left:${o.x}px;top:${o.y}px;width:${o.w}px;height:${r0 + rows.length * rs + 4}px">` +
      `<div class="hi">${svg("gauge", 2.2)}</div><div class="ht k-grad">Sisa jatah gratis</div><div class="hs">${o.sub || "per penyedia · reset harian"}</div><div class="ex">ILUSTRASI</div>`;
    rows.forEach((r, i) => {
      const ss = `style="top:${sty}px"`;
      h += `<div class="k-qr${r.more ? " more" : ""}" id="${p}-qr${i}" style="top:${r0 + i * rs}px;height:${rh}px"><div class="rg" id="${p}-rg${i}"></div><div class="pn" style="line-height:${rh}px">${r.n}</div>` +
        (r.more ? `<div class="mo" style="line-height:${rh}px">${r.sub || ""}</div>` :
        `<div class="tr" style="width:${o.bar || 380}px;top:${rh / 2 - 7}px"><div class="fl" id="${p}-qf${i}" style="width:${o.bar || 380}px"></div><div class="fl lo" id="${p}-ql${i}" style="width:${o.bar || 380}px"></div></div>` +
        `<div class="st idle" id="${p}-qs${i}-idle" ${ss}>${svg("clock-3", 2.4)}siap</div>` +
        `<div class="st on" id="${p}-qs${i}-on" ${ss}>${svg("zap", 2.4)}melayani</div>` +
        `<div class="st bad" id="${p}-qs${i}-bad" ${ss}>${svg("battery-low", 2.4)}habis</div>`) + `</div>`;
    });
    return h + `</div>`;
  };
  // laptop. o: {x, y, w, h (lid)}
  const laptop = (p, o) => {
    const w = o.w, h = o.h, bez = 18;
    return `<div class="k-lp" id="${p}-lp" style="left:${o.x}px;top:${o.y}px;width:${w + 80}px;height:${h + 34}px">` +
      `<div class="lid" style="left:40px;width:${w}px;height:${h}px"></div>` +
      `<div class="scr" id="${p}-scr" style="left:${40 + bez}px;top:${bez}px;width:${w - 2 * bez}px;height:${h - 2 * bez}px"></div>` +
      `<div class="base" style="left:0;top:${h}px;width:${w + 80}px;height:30px"></div><div class="notch" style="left:${40 + w / 2 - 70}px;top:${h}px;width:140px;height:10px"></div></div>`;
  };

  // ---------------------------------------------------------------- timeline boilerplate (initial states nested at 0)
  const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
  const boot = (ID) => {
    const ST = window.SCN[ID][0], D = window.SCN[ID][1], VW = window.VO_WORDS;
    const tl = gsap.timeline({ paused: true });
    { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); const cq = (q) => (typeof q === "number" ? Math.max(0, q) : q);
      tl.set = (a, v, q) => s0(a, _sc(v), cq(q)); tl.fromTo = (a, x, y, q) => f0(a, _sc(x), _sc(y), cq(q)); tl.to = (a, v, q) => t0(a, _sc(v), cq(q)); }
    const P0 = gsap.timeline(); tl.add(P0, 0);                 // every initial state lives here: nested, first child at 0
    const I = (el, v) => { gsap.set(el, _sc(v)); P0.set(el, _sc(v), 0); };
    const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), t);
    const L = (txt, after) => { const w = VW.find((x) => x[0] === txt && x[1] >= ST + (after || 0) - 0.05); if (!w) throw new Error(ID + ": word not found " + txt); return w[1] - ST; };
    const $ = (id) => document.getElementById(id);
    const shake = (el, t, amp = 6) => { [[amp, -amp * 0.6], [-amp * 0.8, amp * 0.4], [amp * 0.4, -amp * 0.2], [0, 0]].forEach(([x, y], k) => tl.set(el, { x, y }, t + k * 0.034)); };
    // pop in (hidden at 0)
    const pop = (el, t, from, dur, ease) => { const a = Object.assign({ opacity: 0, scale: 0.6, y: 20 }, from || {}); const b = {}; for (const k in a) b[k] = k === "opacity" ? 1 : (k === "scale" ? 1 : 0);
      I(el, a); ft(el, a, Object.assign(b, { duration: dur || 0.3, ease: ease || "back.out(1.9)" }), t); };
    // typed text that pushes an inline caret: letters are display:none until their time
    const typeD = (el, text, t0, t1, caret) => {
      el.innerHTML = text.split("").map((c) => `<span>${c === " " ? "&nbsp;" : c}</span>`).join("") + (caret ? `<i class="k-caret"></i>` : "");
      const sp = Array.from(el.querySelectorAll("span")), n = sp.length;
      sp.forEach((s, i) => { I(s, { display: "none" }); tl.set(s, { display: "inline" }, t0 + (t1 - t0) * (i / Math.max(1, n - 1))); });
      return sp;
    };
    const done = () => {
      tl.set({}, {}, D - 0.01);
      (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
      tl.render(0, true, true);
      window.__timelines = window.__timelines || {};
      window.__timelines[ID] = tl;
    };
    return { ST, D, L, tl, ft, I, $, shake, pop, typeD, done };
  };
  // shared exit: everything drops + fades
  const out = (S, els, tOut) => els.forEach((e, k) => S.ft(e, { opacity: 1, y: 0 }, { opacity: 0, y: 46, duration: 0.24, ease: "power2.in" }, tOut + k * 0.025));

  window.K = { svg, P, term, box, quota, laptop, boot, out };
})();

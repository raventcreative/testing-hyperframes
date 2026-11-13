// Shared visual system of R22 ("Agent AI di server klien: checklist AMAN"), loaded in <head> before every scene (after
// vendor/r22icons.js). Everything is our own design in the AI PRENEUR LIGHT house style (white cards, navy gradient text, Poppins).
// No third-party logos or UI: Hermes Agent / OpenCode / auditd / git appear as TEXT + generic lucide icons (ISC). Every command and
// setting shown is the real one from the official docs (see production/VO_SCRIPT.md); file names, times and logs are illustrative.
// Metaphors of the reel: a three-act CHECKLIST (sebelum · selama · sesudah agent kerja) — the agent's own ACCESS BADGE (not the
// master key), a SNAPSHOT photo as the starting point, a HANDBRAKE selector (Hermes approvals), TOLL GATES per tool (OpenCode
// permission), a cashier RECEIPT PRINTER that prints every command (auditd), a LOCKED VAULT owned by root, a BEFORE/AFTER compare
// slider (git status + git diff), and a sticky note vs a real fence (a prompt is not a guard rail).
// - K.svg(k, sw)        lucide icon markup (currentColor)
// - K.hd(o)             card header: icon tile + eyebrow + gradient title + sub line (absolute, inside a positioned card)
// - K.boot(ID)          timeline boilerplate: seek-safe scale shorthand; EVERY initial state pinned at 0 in a NESTED timeline P0 that is
//                       the first child of the scene timeline at 0 (I); fromTo without immediate render (ft); word lookup (L, throws if a
//                       word is missing); typeD (typed text with caret); shake; pop; done() = end marker + backward-seek patch +
//                       tl.render(0, true, true) + registration.
// - K.out(S, els, t)    shared exit: drop + fade
(function () {
  const ICO = window.R22_ICO;
  const svg = (k, sw, cls) => {
    if (!ICO[k]) throw new Error("icon missing: " + k);
    return `<svg class="${cls || ""}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[k]}</svg>`;
  };

  const CSS = `
  .k-grad { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .k-card { background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 40px 70px -40px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); }
  .k-a { position: absolute; }
  /* ---------------- card header */
  .k-hd { position: absolute; left: 0; top: 0; width: 100%; height: 110px; }
  .k-hd > * { position: absolute; }
  .k-hd .ic { left: 24px; top: 24px; width: 64px; height: 64px; border-radius: 20px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff; }
  .k-hd .ic svg { position: absolute; left: 16px; top: 16px; width: 32px; height: 32px; display: block; }
  .k-hd .eb { left: 106px; top: 22px; font: 700 14px/20px Poppins, sans-serif; letter-spacing: .16em; color: #5d6f8f; white-space: nowrap; }
  .k-hd .tt { left: 104px; top: 40px; font: 700 30px/40px Poppins, sans-serif; white-space: nowrap; padding-right: 4px; }
  .k-hd .ts { left: 106px; top: 80px; font: 400 18px/24px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .k-tag { position: absolute; height: 30px; padding: 0 12px; border-radius: 15px; background: #ffffff; box-shadow: inset 0 0 0 1.5px #d9e2f0; font: 700 12px/30px Poppins, sans-serif; letter-spacing: .14em; color: #5d6f8f; white-space: nowrap; }
  /* ---------------- command strip (navy, Poppins only) */
  .k-cmd { position: absolute; height: 52px; padding: 0 20px; border-radius: 14px; background: #0f1740; color: #ffffff; font: 400 19px/52px Poppins, sans-serif; white-space: nowrap;
    box-shadow: 0 14px 24px -16px rgba(10,13,44,.8); }
  .k-cmd b { font-weight: 700; color: #8fd8ff; }
  .k-cmd em { font-style: normal; color: #7f8db0; }
  .k-caret { display: inline-block; width: 9px; height: 22px; margin-left: 4px; vertical-align: -4px; border-radius: 2px; background: #8fd8ff; }
  /* ---------------- chips, stamps, footnotes */
  .k-chip { position: absolute; height: 54px; padding: 0 22px 0 56px; border-radius: 27px; background: #ffffff; color: #0a0d2c; white-space: nowrap; font: 700 22px/54px Poppins, sans-serif;
    box-shadow: 0 16px 26px -16px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); transform-origin: 50% 50%; }
  .k-chip svg { position: absolute; left: 18px; top: 14px; width: 26px; height: 26px; display: block; color: #294b77; }
  .k-chip.sm { height: 44px; padding: 0 18px 0 46px; border-radius: 22px; font: 700 18px/44px Poppins, sans-serif; }
  .k-chip.sm svg { left: 15px; top: 11px; width: 22px; height: 22px; }
  .k-chip.ok { background: #e8f6ed; color: #1f7a3a; box-shadow: inset 0 0 0 1.5px rgba(31,122,58,.22); } .k-chip.ok svg { color: #1f7a3a; }
  .k-chip.info { background: #eaf0fe; color: #2a55c4; box-shadow: inset 0 0 0 1.5px rgba(42,85,196,.22); } .k-chip.info svg { color: #2a55c4; }
  .k-chip.warn { background: #fff3dc; color: #8a4d08; box-shadow: inset 0 0 0 1.5px rgba(148,84,10,.25); } .k-chip.warn svg { color: #8a4d08; }
  .k-chip.bad { background: #fdeaea; color: #b4322f; box-shadow: inset 0 0 0 1.5px rgba(180,50,47,.22); } .k-chip.bad svg { color: #b4322f; }
  .k-chip.navy { background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff; box-shadow: 0 16px 26px -14px rgba(10,13,44,.8); } .k-chip.navy svg { color: #8fd8ff; }
  .k-stamp { position: absolute; height: 72px; padding: 0 22px; border-radius: 14px; border: 5px solid #1f7a3a; color: #1f7a3a; background: rgba(232,246,237,.94);
    font: 700 34px/62px Poppins, sans-serif; letter-spacing: .1em; text-indent: .1em; white-space: nowrap; transform-origin: 50% 50%; }
  .k-stamp.bad { border-color: #b4322f; color: #b4322f; background: rgba(253,234,234,.95); }
  .k-stamp.warn { border-color: #94540a; color: #94540a; background: rgba(255,243,220,.95); }
  .k-fn { position: absolute; height: 40px; padding: 0 16px 0 44px; border-radius: 20px; background: rgba(255,255,255,.94); box-shadow: inset 0 0 0 1.5px #d9e2f0; color: #5d6f8f;
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

  // card header. o: {icon, eb, tt, ts}
  const hd = (o) => `<div class="k-hd"><div class="ic">${svg(o.icon, 2.2)}</div>${o.eb ? `<div class="eb">${o.eb}</div>` : ""}` +
    `<div class="tt k-grad"${o.eb ? "" : ' style="top:28px"'}>${o.tt}</div>${o.ts ? `<div class="ts">${o.ts}</div>` : ""}</div>`;

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
    // word time relative to the scene start; only words spoken inside this scene count (a word from an earlier scene throws)
    const L = (txt, after) => { const w = VW.find((x) => x[0] === txt && x[1] >= ST + (after || 0) - 0.05); if (!w || w[1] > ST + D + 0.05) throw new Error(ID + ": word not found " + txt); return w[1] - ST; };
    const $ = (id) => document.getElementById(id);
    const shake = (el, t, amp = 6) => { [[amp, -amp * 0.6], [-amp * 0.8, amp * 0.4], [amp * 0.4, -amp * 0.2], [0, 0]].forEach(([x, y], k) => tl.set(el, { x, y }, t + k * 0.034)); };
    // pop in (hidden at 0)
    const pop = (el, t, from, dur, ease) => { const a = Object.assign({ opacity: 0, scale: 0.6, y: 20 }, from || {}); const b = {}; for (const k in a) b[k] = k === "opacity" ? 1 : (k === "scale" ? 1 : 0);
      I(el, a); ft(el, a, Object.assign(b, { duration: dur || 0.3, ease: ease || "back.out(1.9)" }), t); };
    // typed text that pushes an inline caret: letters are display:none until their time
    const typeD = (el, text, t0, t1, caret) => {
      el.innerHTML = text.split("").map((c) => `<span>${c === " " ? "&nbsp;" : c.replace("<", "&lt;").replace(">", "&gt;")}</span>`).join("") + (caret ? `<i class="k-caret"></i>` : "");
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

  window.K = { svg, hd, boot, out };
})();

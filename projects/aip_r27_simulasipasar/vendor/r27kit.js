// Shared visual system of R27 ("Tes ide produk ke warga AI dulu — MiroFish"), loaded in <head> before every scene (after
// vendor/r27icons.js). Our own design in the AI PRENEUR WHITE house style — brand colours only in UI (navy #0a0d2c, #294b77,
// blue gradient #13307e -> #2f6bff for a headline word, greys for small text, white cards). No red / yellow / green UI.
// No reference UI or likeness: MiroFish appears as TEXT only (it has no open-source logo set); the two brand logos (GitHub,
// Claude) are Simple Icons (CC0) paths extruded in Three.js (tools/logo3d.html) and baked into 36-frame turntable sprites.
// Metaphor of the reel (ours): your idea is thrown into a DIGITAL TOWN of AI residents ("warga AI") before you spend on stock/ads.
// - K.svg(k, sw)          lucide icon markup (currentColor)
// - K.card / chips (.k-chip, .k-chip.navy, .k-chip.soft), stamp (.k-stamp), footnote (.k-fn), tag (.k-tag)
// - K.term(p, o)          "Claude Code" app window; ids p-tm, p-l<i>, p-ty
// - K.av(p, i, x, y, s, v) a resident avatar (circle + person icon), variant v 0..4 (brand blues)
// - K.post(p, o)          a feed post card (avatar, name, "warga AI" tag, text)
// - K.cursor(p, label)    pointer + label tag
// - K.spin(p, name, x, y, size)  3D logo turntable sprite (assets/logos/<name>_spin.png, 6x6 frames of 300 px); S.spin(el, t0, t1, turns)
// - K.boot(ID)            timeline boilerplate (initial states pinned at 0 in a nested timeline P0; see done()).
(function () {
  const ICO = window.R27_ICO;
  const svg = (k, sw, cls) => { if (!ICO[k]) throw new Error("icon missing " + k); return `<svg class="${cls || ""}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[k]}</svg>`; };

  const CSS = `
  .k-grad { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .k-blue { background: linear-gradient(120deg, #13307e 10%, #2f6bff 90%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .k-card { background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 40px 70px -40px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); }
  .k-a { position: absolute; }
  .k-eb { position: absolute; font: 700 16px/22px Poppins, sans-serif; letter-spacing: .16em; color: #5d6f8f; white-space: nowrap; }
  .k-ic { position: absolute; border-radius: 24px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff; box-shadow: 0 14px 24px -14px rgba(10,13,44,.85), inset 0 2px 0 rgba(255,255,255,.14); }
  .k-ic svg { position: absolute; left: 22%; top: 22%; width: 56%; height: 56%; display: block; }
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
  /* ---------------- residents (warga AI) */
  .k-av { position: absolute; border-radius: 50%; transform-origin: 50% 50%; overflow: hidden; }
  .k-av svg { position: absolute; left: 20%; top: 18%; width: 60%; height: 60%; display: block; }
  .k-av.v0 { background: linear-gradient(150deg, #294b77, #0a0d2c); color: #ffffff; }
  .k-av.v1 { background: linear-gradient(150deg, #2f6bff, #13307e); color: #ffffff; }
  .k-av.v2 { background: linear-gradient(150deg, #dfe8f7, #b9cbe8); color: #294b77; }
  .k-av.v3 { background: #ffffff; color: #294b77; box-shadow: inset 0 0 0 3px #c3d2ea; }
  .k-av.v4 { background: linear-gradient(150deg, #6f93cf, #294b77); color: #ffffff; }
  /* ---------------- feed post */
  .k-post { position: absolute; border-radius: 22px; background: #ffffff; box-shadow: 0 18px 30px -22px rgba(10,13,44,.6), 0 0 0 1.5px rgba(10,13,44,.07); font-family: Poppins, sans-serif; transform-origin: 50% 50%; }
  .k-post > * { position: absolute; }
  .k-post .nm { left: 78px; top: 12px; font: 700 18px/26px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .k-post .tg { left: 78px; top: 38px; height: 22px; padding: 0 9px; border-radius: 11px; background: #eaf0fe; color: #294b77; font: 700 11px/22px Poppins, sans-serif; letter-spacing: .12em; white-space: nowrap; }
  .k-post .tx { left: 20px; top: 74px; right: 20px; font: 400 19px/27px Poppins, sans-serif; color: #24324f; }
  .k-post .rx { left: 20px; bottom: 12px; height: 26px; display: flex; gap: 18px; font: 700 15px/26px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .k-post .rx span { display: flex; align-items: center; gap: 6px; }
  .k-post .rx svg { width: 18px; height: 18px; display: block; color: #294b77; }
  /* ---------------- cursor */
  .k-cur { position: absolute; left: 0; top: 0; width: 0; height: 0; }
  .k-cur .pt { position: absolute; left: -6px; top: -4px; width: 46px; height: 46px; filter: drop-shadow(0 6px 8px rgba(10,13,44,.35)); }
  .k-cur .pt svg { width: 46px; height: 46px; display: block; }
  .k-cur .lb { position: absolute; left: 34px; top: 34px; height: 38px; padding: 0 14px; border-radius: 19px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #fff;
    font: 700 16px/38px Poppins, sans-serif; white-space: nowrap; box-shadow: 0 10px 18px -10px rgba(10,13,44,.8); }
  /* ---------------- chips, stamps, footnotes (brand colours only) */
  .k-chip { position: absolute; height: 54px; padding: 0 22px 0 56px; border-radius: 27px; background: #ffffff; color: #0a0d2c; white-space: nowrap; font: 700 22px/54px Poppins, sans-serif;
    box-shadow: 0 16px 26px -16px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); transform-origin: 50% 50%; }
  .k-chip svg { position: absolute; left: 18px; top: 14px; width: 26px; height: 26px; display: block; color: #294b77; }
  .k-chip.soft { background: #eaf0fe; color: #13307e; box-shadow: inset 0 0 0 1.5px rgba(41,75,119,.22); }
  .k-chip.navy { background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff; box-shadow: 0 16px 26px -14px rgba(10,13,44,.8); } .k-chip.navy svg { color: #ffffff; }
  .k-chip.sm { height: 44px; padding: 0 18px 0 46px; border-radius: 22px; font-size: 18px; line-height: 44px; } .k-chip.sm svg { left: 15px; top: 11px; width: 22px; height: 22px; }
  .k-stamp { position: absolute; height: 72px; padding: 0 22px; border-radius: 14px; border: 5px solid #294b77; color: #294b77; background: rgba(234,240,254,.94);
    font: 700 34px/62px Poppins, sans-serif; letter-spacing: .1em; text-indent: .1em; white-space: nowrap; transform-origin: 50% 50%; }
  .k-fn { position: absolute; height: 40px; padding: 0 16px 0 44px; border-radius: 20px; background: rgba(255,255,255,.92); box-shadow: inset 0 0 0 1.5px #d9e2f0; color: #5d6f8f;
    font: 400 17px/40px Poppins, sans-serif; white-space: nowrap; }
  .k-fn b { font-weight: 700; color: #294b77; }
  .k-fn svg { position: absolute; left: 14px; top: 10px; width: 20px; height: 20px; display: block; color: #294b77; }
  .k-ok { position: absolute; width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(135deg, #13307e, #2f6bff); color: #ffffff; box-shadow: 0 0 0 4px #ffffff, 0 10px 18px -8px rgba(19,48,126,.8); }
  .k-ok svg { position: absolute; left: 9px; top: 9px; width: 22px; height: 22px; display: block; }
  .k-glow { position: absolute; border-radius: 50%; background: radial-gradient(closest-side, rgba(255,255,255,.95), rgba(255,255,255,0)); }
  .k-tag { position: absolute; height: 30px; padding: 0 12px; border-radius: 15px; background: #ffffff; box-shadow: inset 0 0 0 1.5px #d9e2f0; font: 700 12px/30px Poppins, sans-serif;
    letter-spacing: .14em; color: #5d6f8f; white-space: nowrap; }
  .k-bub { position: absolute; border-radius: 26px 26px 26px 8px; background: #ffffff; box-shadow: 0 18px 30px -20px rgba(10,13,44,.65), 0 0 0 1.5px rgba(10,13,44,.07);
    font: 700 22px/30px Poppins, sans-serif; color: #0a0d2c; padding: 14px 20px; white-space: nowrap; transform-origin: 0% 100%; }
  .k-spin { position: absolute; background-repeat: no-repeat; transform-origin: 50% 50%; }
  `;
  if (!document.getElementById("k-css")) { const st = document.createElement("style"); st.id = "k-css"; st.textContent = CSS; (document.head || document.documentElement).appendChild(st); }

  // Claude Code app window. o: {x, y, w, h, tag, lines: [html...], ty: true, fs, lh, t0}
  const term = (p, o) => {
    const fs = o.fs || 23, lh = o.lh || 38, t0 = o.t0 == null ? 18 : o.t0, f = `font-size:${fs}px;line-height:${Math.round(fs * 1.48)}px`;
    const lines = (o.lines || []).map((l, i) => `<div class="ln" id="${p}-l${i}" style="top:${t0 + i * lh}px;${f}">${l}</div>`).join("");
    const ty = o.ty ? `<div class="ty" id="${p}-ty" style="top:${t0 + (o.ty === true ? (o.lines || []).length : o.ty) * lh}px;${f}"></div>` : "";
    return `<div class="k-tm k-card" id="${p}-tm" style="left:${o.x}px;top:${o.y}px;width:${o.w}px;height:${o.h}px">` +
      `<div class="bar"></div><div class="dots"><i style="left:0"></i><i style="left:22px"></i><i style="left:44px"></i></div>` +
      `<div class="ti">${svg("square-terminal", 2.2)}Claude Code</div>${o.tag ? `<div class="tg" id="${p}-tg">${o.tag}</div>` : ""}` +
      `<div class="bd" id="${p}-bd">${lines}${ty}</div></div>`;
  };
  const av = (p, i, x, y, s, v) => `<div class="k-av v${v % 5}" id="${p}-av${i}" style="left:${x}px;top:${y}px;width:${s}px;height:${s}px">${svg("user-round", 2.2)}</div>`;
  // feed post. o: {i, x, y, w, h, v, name, text, likes, replies}
  const post = (p, o) => `<div class="k-post" id="${p}-po${o.i}" style="left:${o.x}px;top:${o.y}px;width:${o.w}px;height:${o.h}px">` +
    `<div class="k-av v${o.v % 5}" style="left:16px;top:12px;width:50px;height:50px">${svg("user-round", 2.2)}</div><div class="nm">${o.name}</div><div class="tg">WARGA AI</div>` +
    `<div class="tx">${o.text}</div>` + (o.likes != null ? `<div class="rx"><span>${svg("thumbs-up", 2)}<b id="${p}-lk${o.i}">${o.likes}</b></span><span>${svg("reply", 2)}${o.replies || 0}</span></div>` : "") + `</div>`;
  const cursor = (p, label) => `<div class="k-cur" id="${p}-cur"><div class="pt"><svg viewBox="0 0 24 24" fill="#fff" stroke="#0a0d2c" stroke-width="1.7" stroke-linejoin="round">${ICO["mouse-pointer-2"]}</svg></div>` +
    (label ? `<div class="lb" id="${p}-curl">${label}</div>` : "") + `</div>`;
  // 3D logo turntable sprite: 6x6 frames of 300 px in assets/logos/<name>_spin.png, shown at `size` px
  const spin = (p, name, x, y, size) => `<div class="k-spin" id="${p}-sp${name}" data-size="${size}" style="left:${x}px;top:${y}px;width:${size}px;height:${size}px;` +
    `background-image:url(assets/logos/${name}_spin.png);background-size:${size * 6}px ${size * 6}px;background-position:0 0"></div>`;

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
    const $ = (id) => { const e = document.getElementById(id); if (!e) throw new Error(ID + ": element not found " + id); if (document.querySelectorAll("#" + id).length > 1) throw new Error(ID + ": duplicate id " + id); return e; };
    const shake = (el, t, amp = 6) => { [[amp, -amp * 0.6], [-amp * 0.8, amp * 0.4], [amp * 0.4, -amp * 0.2], [0, 0]].forEach(([x, y], k) => tl.set(el, { x, y }, t + k * 0.034)); };
    // pop in (hidden at 0) on a small-overshoot spring
    const pop = (el, t, from, dur, ease) => { const a = Object.assign({ opacity: 0, scale: 0.6, y: 20 }, from || {}); const b = {}; for (const k in a) b[k] = k === "opacity" ? 1 : (k === "scale" ? 1 : 0);
      I(el, a); ft(el, a, Object.assign(b, { duration: dur || 0.3, ease: ease || "back.out(1.6)" }), t); };
    // typed text that pushes an inline caret: letters are display:none until their time
    const typeD = (el, text, t0, t1, caret) => {
      el.innerHTML = text.split("").map((c) => `<span>${c === " " ? "&nbsp;" : c}</span>`).join("") + (caret ? `<i class="k-caret"></i>` : "");
      const sp = Array.from(el.querySelectorAll("span")), n = sp.length;
      sp.forEach((s, i) => { I(s, { display: "none" }); tl.set(s, { display: "inline" }, t0 + (t1 - t0) * (i / Math.max(1, n - 1))); });
      return sp;
    };
    // camera: slow push 1.0 -> 1.04 over the whole scene (never still), around (ox, oy)
    const push = (el, ox, oy, z1) => { I(el, { scale: 1, transformOrigin: `${ox || 540}px ${oy || 620}px` }); ft(el, { scale: 1 }, { scale: z1 || 1.04, duration: D, ease: "sine.inOut" }, 0); };
    // 3D logo turntable: frame index by time (turns full spins between t0 and t1, easing out), then a slow idle sway
    const spinT = (el, t0, t1, turns) => {
      const sz = +el.dataset.size, fr = (k) => { k = ((k % 36) + 36) % 36; return `${-(k % 6) * sz}px ${-Math.floor(k / 6) * sz}px`; };
      I(el, { backgroundPosition: fr(0) });
      const n = Math.round(36 * (turns || 1)), steps = Math.max(1, Math.round((t1 - t0) * 30));
      for (let s = 1; s <= steps; s++) { const u = s / steps, e = 1 - Math.pow(1 - u, 3); tl.set(el, { backgroundPosition: fr(Math.round(e * n)) }, t0 + (t1 - t0) * u); }
      for (let t = t1 + 0.1, k = 0; t < D; t += 0.1, k++) tl.set(el, { backgroundPosition: fr(Math.round(2.2 * Math.sin(k * 0.3))) }, t);
    };
    const done = () => {
      tl.set({}, {}, D - 0.01);
      (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
      tl.render(0, true, true);
      window.__timelines = window.__timelines || {};
      window.__timelines[ID] = tl;
    };
    return { ST, D, L, tl, ft, I, $, shake, pop, typeD, push, spinT, done };
  };
  // shared exit: everything drops + fades
  const out = (S, els, tOut) => els.forEach((e, k) => S.ft(e, { opacity: 1, y: 0 }, { opacity: 0, y: 46, duration: 0.24, ease: "power2.in" }, tOut + k * 0.025));

  window.K = { svg, term, av, post, cursor, spin, boot, out };
})();

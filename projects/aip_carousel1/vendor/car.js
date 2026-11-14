// AI PRENEUR carousel kit (window.CAR). Loaded after gsap + vendor/icons.js, before the effect demo scripts.
// - CAR.def(id, { build(K) })   registers an effect demo (effects/<id>/demo.js). build() fills K.root (932x588 "page" inside the
//                                browser card) and animates on K.tl (a 6 s timeline that must LOOP: state at D == state at 0).
// - CAR.run(SLIDE)              builds one slide from the config injected by tools/build.py (kind: cover | effect | closing).
// Seek rules (house lessons): every initial state is pinned at 0 in a nested timeline P0 (first child at 0); fromTo never renders
// immediately; scale shorthand expanded to scaleX/scaleY; backward seeks re-render 0 first; tl.render(0, true, true) at the end.
(function () {
  const ICO = window.CAR_ICO;
  const svg = (k, sw, cls, extra) => {
    if (!ICO[k]) throw new Error("icon missing " + k);
    return `<svg class="${cls || "i"}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round"${extra || ""}>${ICO[k]}</svg>`;
  };
  const mk = (tag, cls, parent, html, style) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; if (style) e.style.cssText = style; if (parent) parent.appendChild(e); return e; };
  const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
  const starRow = (n, size) => `<span class="k-stars">${Array.from({ length: n || 5 }, () => svg("star", 1.5, "", size ? ` style="width:${size}px;height:${size}px"` : "")).join("")}</span>`;

  // one seek-safe timeline + its P0 (initial states)
  function timeline() {
    const tl = gsap.timeline({ paused: true });
    const P0 = gsap.timeline(); tl.add(P0, 0);
    const I = (el, v) => { gsap.set(el, _sc(v)); P0.set(el, _sc(v), 0); };
    const ft = (el, a, b, t) => tl.fromTo(el, _sc(a), Object.assign({ immediateRender: false }, _sc(b)), Math.max(0, t));
    const set = (el, v, t) => tl.set(el, _sc(v), Math.max(0, t));
    return { tl, P0, I, ft, set };
  }
  // animation helpers bound to one timeline
  function helpers(T, D) {
    const { I, ft, set } = T;
    // pop in from a hidden state (pinned hidden at 0)
    const pop = (el, t, from, dur, ease) => {
      const a = Object.assign({ opacity: 0, scale: 0.7, y: 16 }, from || {}); const b = {};
      for (const k in a) b[k] = k === "opacity" || k === "scale" ? 1 : 0;
      I(el, a); ft(el, a, Object.assign(b, { duration: dur || 0.4, ease: ease || "back.out(1.7)" }), t);
    };
    // leave to a hidden state (from the shown state)
    const hide = (el, t, to, dur, ease) => {
      const b = Object.assign({ opacity: 0, scale: 0.9, y: 10 }, to || {}); const a = {};
      for (const k in b) a[k] = k === "opacity" || k === "scale" ? 1 : 0;
      ft(el, a, Object.assign(b, { duration: dur || 0.3, ease: ease || "power2.in" }), t);
    };
    // press: quick squash + spring back, with a ripple (needs el position != static and overflow hidden)
    const tap = (el, t, o) => {
      o = o || {};
      const r = mk("i", "k-rip", el); if (o.color) r.style.background = o.color;
      I(r, { scale: 0, opacity: 0 });
      ft(r, { scale: 0.2, opacity: 0.75 }, { scale: o.s || 6, opacity: 0, duration: 0.55, ease: "power2.out" }, t);
      if (o.press !== false) {
        ft(el, { scale: 1 }, { scale: o.to || 0.95, duration: 0.09, ease: "power1.out" }, t);
        ft(el, { scale: o.to || 0.95 }, { scale: 1, duration: 0.3, ease: "back.out(2.2)" }, t + 0.09);
      }
      return r;
    };
    // typed text: letters display:none until their time; returns clear(t) to hide them again (for the loop reset)
    const typeText = (el, text, t0, t1, caret) => {
      el.innerHTML = text.split("").map((c) => `<span>${c === " " ? "&nbsp;" : c}</span>`).join("") + (caret ? `<i class="k-caret"></i>` : "");
      const sp = Array.from(el.querySelectorAll("span")), n = sp.length;
      sp.forEach((s, i) => { I(s, { display: "none" }); set(s, { display: "inline" }, t0 + (t1 - t0) * (i / Math.max(1, n - 1))); });
      return (t) => sp.forEach((s) => set(s, { display: "none" }, t));
    };
    return { pop, hide, tap, typeText };
  }

  // ------------------------------------------------------------------ demos
  const DEMOS = {};
  const def = (id, spec) => { DEMOS[id] = spec; };
  function makeDemo(id, host, D) {
    const spec = DEMOS[id]; if (!spec) throw new Error("demo not loaded: " + id);
    const root = mk("div", "fx fx-" + id, host);
    const T = timeline();
    const q = (s) => { const e = root.querySelector(s); if (!e) throw new Error(id + ": missing element " + s); return e; };
    const qa = (s) => { const l = Array.from(root.querySelectorAll(s)); if (!l.length) throw new Error(id + ": no elements " + s); return l; };
    const K = Object.assign({ id, root, D, q, qa, svg, mk, stars: starRow, img: (n) => `effects/${id}/img/${n}.jpg` }, T, helpers(T, D));
    spec.build(K);
    T.tl.set({}, {}, D);                              // exact loop length
    if (Math.abs(T.tl.duration() - D) > 1e-6) throw new Error(id + ": demo runs past its loop (" + T.tl.duration() + " s)");
    return { root, tl: T.tl };
  }

  // ------------------------------------------------------------------ slide frame
  function background(stage, M, D) {
    stage.insertAdjacentHTML("beforeend", `<div class="bg-plate"></div><div class="bg-tint"></div><div class="bg-gridwrap"><div class="bg-grid"></div></div><div class="bg-glow"></div>`);
    const g = stage.querySelector(".bg-grid");
    M.I(g, { x: 0, y: 0 });
    M.ft(g, { x: 0, y: 0 }, { x: 43, y: 43, duration: D, ease: "none" }, 0);    // exactly one cell per loop = seamless
  }
  function header(stage, S) {
    stage.insertAdjacentHTML("beforeend", `<img class="hd-logo" src="vendor/brand/logo_dark.png" alt="AI PRENEUR"><i class="hd-div"></i>` +
      `<div class="hd-name">Freddie Kashawan</div><div class="ctr">${String(S.index).padStart(2, "0")} <span>/ ${String(S.total).padStart(2, "0")}</span></div>`);
  }
  function footer(stage, S, M, D) {
    const sw = mk("div", "ft-sw", stage, `${S.swipe}<i class="ft-ar">${svg(S.swipeIcon || "arrow-right", 2.4)}</i>`);
    const dots = mk("div", "ft-dots", stage, Array.from({ length: S.total }, (_, i) => `<i class="${i + 1 === S.index ? "on" : ""}"></i>`).join(""));
    const ar = sw.querySelector(".ft-ar svg");
    M.ft(ar, { x: -2 }, { x: 6, duration: D / 4, ease: "sine.inOut", repeat: 3, yoyo: true }, 0);
    M.I(ar, { x: -2 });
    return { sw, dots };
  }
  function promptStrip(stage, S, M) {
    const p = mk("div", "pr", stage, `<div class="pr-lb">PROMPT</div><div class="pr-tx"><span>${S.promptLead}</span> <span class="bl">${S.promptRest}</span></div>` +
      `<div class="pr-btn">${svg("message-circle-more", 2.2)}Komen <b>${S.keyword}</b><i class="sh"></i></div>`);
    const sh = p.querySelector(".sh");
    M.I(sh, { x: -140 });
    M.ft(sh, { x: -140 }, { x: 380, duration: 1.0, ease: "power2.inOut" }, 1.4);
    return p;
  }
  function browser(stage, S, cls) {
    const b = mk("div", "br" + (cls ? " " + cls : ""), stage,
      `<div class="br-dots"><i style="left:0;background:#f4a59d"></i><i style="left:22px;background:#f5d27f"></i><i style="left:44px;background:#9bd8a6"></i></div>` +
      `<div class="br-url">${svg("lock", 2.4)}${S.url}</div><div class="br-chip">${svg("sparkles", 2.2)}CONTOH · 1 PROMPT</div><div class="br-body"></div>`);
    return b;
  }

  // ------------------------------------------------------------------ slide kinds
  function effectSlide(stage, S, M, D) {
    stage.insertAdjacentHTML("beforeend",
      `<div class="wm">${S.num}</div>` +
      `<div class="eb"><i>${svg(S.icon, 2.2)}</i><span>${S.num} / ${S.count}</span><em>·</em><b>${S.category}</b></div>` +
      `<div class="ttl grad" style="font-size:${S.titleSize || 92}px">${S.title}</div>` +
      `<div class="sub">${S.subtitle}</div>`);
    const b = browser(stage, S);
    const demo = makeDemo(S.effect, b.querySelector(".br-body"), D);
    M.tl.add(demo.tl, 0);
    mk("div", "use", stage, `<b>COCOK BUAT</b><span>${S.use}</span>`);
    promptStrip(stage, S, M);
  }

  function cover(stage, S, M, D) {
    const C = S.cover;
    stage.insertAdjacentHTML("beforeend",
      `<div class="eb"><i>${svg("gift", 2.2)}</i><span>${C.eyebrow}</span></div>` +
      `<div class="cv-t1 grad">${C.title1}</div><div class="cv-t2 grad">${C.title2}</div>` +
      `<div class="cv-sub">${C.sub}</div>` +
      `<div class="cv-stk"><i>${svg("sparkles", 2.2)}</i>${C.sticker}</div>`);
    const n = S.effects.length;
    const rows = n <= 4 ? 1 : n <= 10 ? 2 : 3, cols = Math.ceil(n / rows);
    const gx = 14, gy = 14, W = 952, top = 498, avail = 470;
    let tw = (W - gx * (cols - 1)) / cols;
    const chrome = 14, lab = 30;
    let bh = tw * 588 / 932;
    const maxH = (avail - gy * (rows - 1)) / rows - chrome - lab;
    if (bh > maxH) { bh = maxH; tw = bh * 932 / 588; }
    const left0 = 64 + (W - (tw * cols + gx * (cols - 1))) / 2;
    const sc = tw / 932;
    S.effects.forEach((e, i) => {
      const c = i % cols, r = Math.floor(i / cols);
      const x = left0 + c * (tw + gx), y = top + r * (bh + chrome + lab + gy);
      const tile = mk("div", "cv-tile", stage, `<div class="cv-chr"><i></i><i></i><i></i></div><div class="cv-body"></div>` +
        `<div class="cv-lab"><b>${String(i + 1).padStart(2, "0")}</b>${e.short}</div>`, `left:${x}px;top:${y}px;width:${tw}px;height:${bh + chrome}px`);
      const body = tile.querySelector(".cv-body"); body.style.height = bh + "px";
      const demo = makeDemo(e.id, body, 6);
      demo.root.style.transform = `scale(${sc})`;
      demo.tl.timeScale(6 / D);                         // the 6 s loop stretched over the cover's 8 s: still seamless
      M.tl.add(demo.tl, 0);
    });
    const cta = mk("div", "cv-cta", stage, `<i class="ic">${svg("message-circle-more", 2.2)}</i><span>Komen <b>${S.keyword}</b>, ${C.cta}</span><em>${svg("gift", 2.2)}Gratis</em><i class="sh"></i>`);
    const sh = cta.querySelector(".sh");
    M.I(sh, { x: -160 });
    M.ft(sh, { x: -160 }, { x: 1000, duration: 1.4, ease: "power2.inOut" }, 2.2);
  }

  function closing(stage, S, M, D) {
    const C = S.closing, H = helpers(M, D);
    stage.insertAdjacentHTML("beforeend",
      `<div class="eb"><i>${svg("package", 2.2)}</i><span>${C.eyebrow}</span></div>` +
      `<div class="cl-t grad">${C.title1}</div><div class="cl-t2 grad">${C.title2}</div><div class="cl-sub">${C.sub}</div>`);
    // three steps
    const steps = C.steps.map((s, i) => mk("div", "cl-step", stage, `<i class="n">${i + 1}</i><i class="ic">${svg(s[0], 2.1)}</i><b>${s[1]}</b><span>${s[2]}</span>`, `left:${64 + i * 324}px`));
    C.steps.slice(0, 2).forEach((_, i) => mk("i", "cl-arr", stage, svg("chevron-right", 2.6), `left:${64 + i * 324 + 296}px`));
    steps.forEach((s, i) => {
      const t = 0.35 + i * 0.55;
      M.ft(s, { y: 0 }, { y: -8, duration: 0.25, ease: "power2.out", yoyo: true, repeat: 1 }, t);
      const ic = s.querySelector(".ic");
      M.ft(ic, { scale: 1 }, { scale: 1.16, duration: 0.25, ease: "power2.out", yoyo: true, repeat: 1 }, t);
    });
    // package contents: all effects, ticked in sequence
    const box = mk("div", "cl-box", stage, `<div class="cl-bh"><i>${svg("folder-open", 2.1)}</i><b>Isi paket</b><span>${S.effects.length} prompt animasi · Bahasa Indonesia</span></div>`);
    const n = S.effects.length, cols = 3, rows = Math.ceil(n / cols);
    S.effects.forEach((e, i) => {
      const c = Math.floor(i / rows), r = i % rows;
      const it = mk("div", "cl-it", box, `<em>${String(i + 1).padStart(2, "0")}</em><span>${e.short}</span><i class="ck">${svg("check", 3.2)}</i>`, `left:${24 + c * 302}px;top:${84 + r * 50}px`);
      const ck = it.querySelector(".ck");
      M.I(ck, { scale: 0, opacity: 0 });
      const t = 0.5 + i * 0.12;
      M.ft(ck, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.4)" }, t);
      M.ft(ck, { scale: 1, opacity: 1 }, { scale: 0, opacity: 0, duration: 0.22, ease: "power2.in" }, D - 0.5 + i * 0.012);
    });
    box.style.height = 84 + rows * 50 + 16 + "px";
    // comment box: "ANIMASI" types in, send, sent chip; resets before the loop ends
    const cm = mk("div", "cl-cm", stage, `<i class="av">FK</i><div class="fld"><span class="ph">Tambahkan komentar...</span><span class="ty"></span></div>` +
      `<div class="snd">${svg("send", 2.2)}</div><div class="ok">${svg("circle-check", 2.2)}Terkirim, cek DM-mu</div>`);
    const ph = cm.querySelector(".ph"), ty = cm.querySelector(".ty"), snd = cm.querySelector(".snd"), ok = cm.querySelector(".ok");
    M.I(ph, { opacity: 1 });
    M.set(ph, { opacity: 0 }, 1.2);
    const clear = H.typeText(ty, S.keyword, 1.25, 1.95, false);
    H.tap(snd, 2.35, { s: 3 });
    H.pop(ok, 2.55, { scale: 0.8, y: 8 });
    H.hide(ok, 5.0, { y: 6 }, 0.25);
    clear(5.1);
    M.set(ph, { opacity: 1 }, 5.1);
    mk("div", "cl-note", stage, `${svg("shield-check", 2.2)}<b>${C.note1}</b><span>· ${C.note2}</span>`);
  }

  // ------------------------------------------------------------------ run
  function done(M, comp, D) {
    M.tl.set({}, {}, D);
    (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(M.tl);
    M.tl.render(0, true, true);
    window.__timelines = window.__timelines || {};
    window.__timelines[comp] = M.tl;
  }
  function run(S) {
    const stage = document.getElementById("stage");
    const D = S.duration, M = timeline();
    background(stage, M, D);
    header(stage, S);
    if (S.kind === "effect") effectSlide(stage, S, M, D);
    else if (S.kind === "cover") cover(stage, S, M, D);
    else if (S.kind === "closing") closing(stage, S, M, D);
    else throw new Error("unknown slide kind " + S.kind);
    footer(stage, S, M, D);
    done(M, S.comp, D);
  }

  window.CAR = { svg, mk, def, run, makeDemo, timeline, helpers, starRow };
})();

// R21 PILIH (6 agent AI: cloud vs open source vs orchestrator) — shared scene kit (loaded in index.html <head> after vo_words.js +
// r21icons.js; every scene uses window.R21K). Adapted from the R19 kit. Components (identical in every scene that shows them): the
// TOPIC HEADER (icon roll, name, one-line job, chip, 7 progress segments), lucide icons (ISC), the AGENT CARD (our own mock: generic
// lucide icon + name + maker, never the products' logos), the timeline boilerplate (scale patch, ft, I, wt, seek patch, per-letter
// typing). Every initial state is pinned at 0 in a NESTED timeline that is the first child of the scene timeline at 0 (I);
// finish() = end marker + backward-seek patch + tl.render(0, true, true) + registration. Deterministic: no Math.random, no Date, no rAF.
(function () {
  const K = (window.R21K = {});
  const ICO = window.R21_ICO || {};
  K.svg = (n, cls = "", extra = "") =>
    `<svg class="${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ${extra}>${ICO[n] || ""}</svg>`;

  // ------------------------------------------------------------------ the six agents (names + makers verified, see production/VO_SCRIPT.md)
  K.AG = {
    dots: { n: "Dots", by: "OpenAI &middot; di ChatGPT", ic: "circle-dot" },
    grok: { n: "Grok Bot", by: "x.ai &middot; tim bot", ic: "bot" },
    muse: { n: "Muse", by: "Meta &middot; agen personal", ic: "sparkles" },
    claw: { n: "OpenClaw", by: "OpenClaw Foundation", ic: "message-circle" },
    herm: { n: "Hermes", by: "Nous Research", ic: "book-open" },
    maus: { n: "MausBot", by: "open source &middot; Apache 2.0", ic: "network" },
  };

  // ------------------------------------------------------------------ topic header items (s02 … s08)
  K.HD = [
    { tile: "cloud", name: "Tinggal pakai", sub: "jalan di cloud mereka &middot; <i>3 agent</i>", chip: "CLOUD", chipIc: "cloud" },
    { tile: "scale", name: "Plus-minusnya", sub: "praktis &middot; <i>tapi datamu di sana</i>", chip: "JUJUR", chipIc: "info" },
    { tile: "key-round", name: "Pegang sendiri", sub: "open source &middot; <i>di mesinmu</i>", chip: "OPEN SOURCE", chipIc: "lock-open" },
    { tile: "message-circle", name: "OpenClaw &amp; Hermes", sub: "chat dari WhatsApp &middot; <i>belajar sendiri</i>", chip: "MIT", chipIc: "lock-open" },
    { tile: "shield-alert", name: "Izin bawaan", sub: "cek dulu sebelum dipakai", chip: "PENTING", chipIc: "triangle-alert" },
    { tile: "network", name: "MausBot", sub: "pengatur agent yang kamu punya", chip: "APACHE 2.0", chipIc: "lock-open" },
    { tile: "signpost", name: "Cara milih", sub: "praktis &middot; <i>atau kendali</i>", chip: "PILIH", chipIc: "check" },
  ];
  K.NSEG = 7;

  // ------------------------------------------------------------------ geometry (global px)
  K.HDR = { x: 60, y: 312, w: 960, h: 140 };
  K.SEG = (k) => ({ x: 798 + (k - 1) * 29, y: 342 });

  // ------------------------------------------------------------------ shared CSS (injected once)
  const CSS = `
  .k-ab{position:absolute;left:0;top:0}
  .k-glass{position:absolute;border-radius:28px;background:rgba(12,22,64,.84);box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.10),0 22px 46px rgba(2,6,26,.5)}
  .k-white{position:absolute;border-radius:28px;background:linear-gradient(180deg,#ffffff,#f4f7fc);box-shadow:0 26px 56px rgba(2,6,26,.55)}
  .k-lab{position:absolute;font:700 19px/26px Poppins;letter-spacing:2.5px;color:#6adfff;white-space:nowrap}
  .k-hplate{position:absolute;left:60px;top:312px;width:960px;height:140px;border-radius:30px;background:rgba(12,22,64,.84);
    box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.10),0 18px 40px rgba(3,6,24,.35);transform-origin:50% 50%}
  .k-hglow{position:absolute;left:60px;top:312px;width:960px;height:140px;border-radius:30px;box-shadow:inset 0 0 0 2px rgba(106,223,255,.9),0 0 34px rgba(1,204,247,.35);opacity:0}
  .k-hnum{position:absolute;left:78px;top:326px;width:112px;height:112px;border-radius:24px;overflow:hidden;
    background:linear-gradient(160deg,#9cecff 0%,#01ccf7 52%,#0aa7d6 100%);box-shadow:0 0 26px rgba(1,204,247,.45),inset 0 1px 0 rgba(255,255,255,.5)}
  .k-hroll{position:absolute;left:0;top:0;width:112px}
  .k-hroll b{display:block;position:relative;height:112px}
  .k-hroll b svg{position:absolute;left:28px;top:28px;width:56px;height:56px;color:#0b1440}
  .k-hbox{position:absolute;overflow:hidden}
  .k-hname{position:absolute;left:0;top:0;white-space:nowrap;font:700 48px/66px Poppins;color:#fff;letter-spacing:-.5px}
  .k-hsub{position:absolute;left:0;top:0;white-space:nowrap;font:400 22px/40px Poppins;color:#9fdcf2}
  .k-hsub i{font-style:normal;color:#86a9c9}
  .k-hseg{position:absolute;top:342px;width:23px;height:8px;border-radius:4px;background:rgba(255,255,255,.16);overflow:hidden}
  .k-hseg b{position:absolute;left:0;top:0;width:23px;height:8px;background:#01ccf7;border-radius:4px;transform-origin:0 50%;box-shadow:0 0 10px rgba(1,204,247,.8)}
  .k-hchip{position:absolute;right:0;top:0;height:40px;padding:0 16px 0 12px;border-radius:20px;display:flex;align-items:center;gap:8px;
    font:700 18px/1 Poppins;letter-spacing:1.5px;color:#6adfff;background:rgba(1,204,247,.10);box-shadow:inset 0 0 0 1.5px rgba(1,204,247,.5);white-space:nowrap}
  .k-hchip svg{width:20px;height:20px}
  .k-hchip.am{color:#ffc761;background:rgba(255,183,77,.10);box-shadow:inset 0 0 0 1.5px rgba(255,183,77,.6)}
  .k-chk{position:absolute;height:46px;padding:0 18px 0 12px;border-radius:23px;display:flex;align-items:center;gap:10px;font:700 21px/1 Poppins;color:#fff;
    background:rgba(45,164,78,.22);box-shadow:inset 0 0 0 1.5px rgba(80,210,120,.7);white-space:nowrap}
  .k-chk svg{width:24px;height:24px;color:#5be08a}
  .k-amb{position:absolute;height:46px;padding:0 18px 0 12px;border-radius:23px;display:flex;align-items:center;gap:10px;font:700 21px/1 Poppins;color:#ffd58a;
    background:rgba(255,183,77,.14);box-shadow:inset 0 0 0 1.5px rgba(255,183,77,.7);white-space:nowrap}
  .k-amb svg{width:24px;height:24px;color:#ffc761}
  .k-demo{position:absolute;height:30px;padding:0 12px;border-radius:15px;font:700 15px/30px Poppins;letter-spacing:1.5px;color:#b8c7dd;
    background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 1.2px rgba(255,255,255,.22);white-space:nowrap}
  .k-demo.w{color:#5d6f8f;background:#eef3fb;box-shadow:inset 0 0 0 1.2px #d5deec}
  /* agent card: white, generic lucide icon in a cyan tile, name + maker (text only, never a product logo) */
  .k-ag{position:absolute;left:0;top:0;border-radius:24px;background:linear-gradient(180deg,#ffffff,#f3f7fd);box-shadow:0 18px 40px rgba(2,6,26,.5);transform-origin:50% 50%}
  .k-ag .it{position:absolute;left:18px;top:18px;width:64px;height:64px;border-radius:18px;background:linear-gradient(160deg,#9cecff,#01ccf7 55%,#0aa7d6);color:#0b1440;box-shadow:0 0 16px rgba(1,204,247,.35)}
  .k-ag .it svg{position:absolute;left:16px;top:16px;width:32px;height:32px}
  .k-ag .nm{position:absolute;left:98px;top:14px;font:700 32px/42px Poppins;color:#0a0d2c;white-space:nowrap;letter-spacing:-.3px}
  .k-ag .by{position:absolute;left:98px;top:56px;font:400 18px/26px Poppins;color:#5d6f8f;white-space:nowrap}
  .k-ag.sm .it{left:14px;top:14px;width:52px;height:52px;border-radius:15px}
  .k-ag.sm .it svg{left:13px;top:13px;width:26px;height:26px}
  .k-ag.sm .nm{left:80px;top:10px;font-size:27px;line-height:36px}
  .k-ag.sm .by{left:80px;top:46px;font-size:16px;line-height:22px}
  `;
  if (!document.getElementById("r21kit-css")) {
    const st = document.createElement("style"); st.id = "r21kit-css"; st.textContent = CSS; document.head.appendChild(st);
  }
  // agent card markup (w x h set by caller); extra = inner html appended (chips, stamps)
  K.agentHTML = (id, key, w, h, extra = "", sm = false) => {
    const a = K.AG[key];
    return `<div class="k-ag${sm ? " sm" : ""}" id="${id}" style="width:${w}px;height:${h}px"><div class="it">${K.svg(a.ic)}</div><div class="nm">${a.n}</div><div class="by">${a.by}</div>${extra}</div>`;
  };

  // ------------------------------------------------------------------ timeline boilerplate
  const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
  K.dur = (id) => { const s = (window.VO_SCENES || []).find((x) => x.id === id); if (!s) throw new Error("no scene " + id); return s.dur; };
  K.total = () => { const v = window.VO_SCENES || []; const L = v[v.length - 1]; return L ? Math.round((L.start + L.dur) * 1e4) / 1e4 : 0; };
  K.scene = (id, D) => {
    const tl = gsap.timeline({ paused: true });
    // positions are clamped to >= 0 (a child placed before 0 would render BEFORE the frame-0 pins and be overridden by them)
    const cl = (p) => (typeof p === "number" ? Math.max(0, p) : p);
    { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); tl.set = (a, v, p) => s0(a, _sc(v), cl(p)); tl.fromTo = (a, x, y, p) => f0(a, _sc(x), _sc(y), cl(p)); tl.to = (a, v, p) => t0(a, _sc(v), cl(p)); }
    const P0 = gsap.timeline(); tl.add(P0, 0);                  // every initial state lives here: nested, first child at 0
    const I = (el, v) => { gsap.set(el, _sc(v)); P0.set(el, _sc(v), 0); };
    const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), typeof t === "number" ? Math.max(0.005, t) : t);
    const SC = (window.VO_SCENES || []).find((s) => s.id === id) || { start: 0 };
    const T0 = SC.start;
    // scene-local time of a spoken word (first match at/after `after`, global seconds; default = this scene's start)
    const wt = (txt, after) => { const a = after === undefined ? T0 - 0.05 : after; const w = (window.VO_WORDS || []).find((x) => x[0] === txt && x[1] >= a - 1e-6); if (!w) throw new Error(id + ": word not found " + txt); return w[1] - T0; };
    const $ = (x) => document.getElementById(x);
    const finish = () => {
      tl.set({}, {}, D - 0.01);
      (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
      tl.render(0, true, true);   // apply every pinned initial state now (frame 0 of the real runtime)
      window.__timelines = window.__timelines || {};
      window.__timelines[id] = tl;
    };
    // per-letter typing: letter spans whose opacity is set at times (no onUpdate). Words are wrapped in nowrap spans separated by real
    // spaces, so a long line still wraps at word boundaries (layout is fixed from frame 0: hidden letters keep their space).
    const esc = (c) => c.replace(/&/g, "&amp;").replace(/</g, "&lt;");
    const type = (el, text, t0, cps, cls = "") => {
      el.innerHTML = text.split(" ").map((w) => `<span style="white-space:nowrap">${Array.from(w).map((c) => `<span class="${cls}">${esc(c)}</span>`).join("")}</span>`).join(" ");
      const sp = el.querySelectorAll(":scope > span > span"); let k = 0, ci = 0;
      Array.from(text).forEach((c) => { if (c === " ") { ci++; return; } const s = sp[k++]; I(s, { opacity: 0 }); tl.set(s, { opacity: 1 }, t0 + ci / cps); ci++; });
      return t0 + text.length / cps;
    };
    // typing that fits a window: reveal all letters evenly between t0 and t1
    const typeIn = (el, text, t0, t1, cls = "") => type(el, text, t0, Math.max(8, text.length / Math.max(0.15, t1 - t0)), cls);
    const popIn = (el, t, from = 0.4, dur = 0.3) => { I(el, { scale: from, opacity: 0, transformOrigin: "50% 50%" }); ft(el, { scale: from, opacity: 0 }, { scale: 1, opacity: 1, duration: dur, ease: "back.out(2.4)" }, t); };
    return { tl, ft, I, wt, $, finish, type, typeIn, popIn, T0, D, P0 };
  };

  // ------------------------------------------------------------------ TOPIC HEADER
  K.headerHTML = (P) => {
    let h = `<div class="k-hplate" id="${P}-hplate"></div><div class="k-hglow" id="${P}-hglow"></div>`;
    h += `<div class="k-hnum" id="${P}-hnum"><div class="k-hroll" id="${P}-hroll">` + K.HD.map((d) => `<b>${K.svg(d.tile)}</b>`).join("") + `</div></div>`;
    h += `<div class="k-hbox" id="${P}-hnb" style="left:214px;top:328px;width:560px;height:66px">` + K.HD.map((d, k) => `<div class="k-hname" id="${P}-hn${k}">${d.name}</div>`).join("") + `</div>`;
    h += `<div class="k-hbox" id="${P}-hsb" style="left:214px;top:396px;width:540px;height:40px">` + K.HD.map((d, k) => `<div class="k-hsub" id="${P}-hs${k}">${d.sub}</div>`).join("") + `</div>`;
    h += `<div class="k-hbox" id="${P}-hlb" style="left:752px;top:384px;width:250px;height:40px">` + K.HD.map((d, k) => `<div class="k-hchip${d.chip === "PENTING" ? " am" : ""}" id="${P}-hl${k}">${K.svg(d.chipIc)}${d.chip}</div>`).join("") + `</div>`;
    for (let k = 1; k <= K.NSEG; k++) h += `<div class="k-hseg" id="${P}-ht${k}" style="left:${K.SEG(k).x}px"><b id="${P}-hg${k}"></b></div>`;
    return `<div class="k-ab" id="${P}-hdr" style="width:1080px;height:1920px">${h}</div>`;
  };
  const segOn = (j, k) => j <= k + 1;   // item k lights segments 1..k+1
  // state at frame 0: item k shown
  K.headerSet = (S, P, k) => {
    const { I, $ } = S;
    I($(`${P}-hroll`), { y: -k * 112 });
    for (let j = 0; j < K.HD.length; j++) {
      I($(`${P}-hn${j}`), { y: j === k ? 0 : 66, opacity: j === k ? 1 : 0 });
      I($(`${P}-hs${j}`), { y: j === k ? 0 : 40, opacity: j === k ? 1 : 0 });
      I($(`${P}-hl${j}`), { y: j === k ? 0 : 40, opacity: j === k ? 1 : 0 });
    }
    for (let j = 1; j <= K.NSEG; j++) I($(`${P}-hg${j}`), { scaleX: segOn(j, k) ? 1 : 0 });
    I($(`${P}-hglow`), { opacity: 0 });
  };
  // animated switch a → b starting at local time t
  K.headerSwap = (S, P, a, b, t) => {
    const { ft, $ } = S;
    ft($(`${P}-hroll`), { y: -a * 112 }, { y: -b * 112, duration: 0.5, ease: "power3.inOut" }, t);
    const out = (el, d) => ft(el, { y: 0, opacity: 1 }, { y: -d, opacity: 0, duration: 0.26, ease: "power2.in" }, t);
    const inn = (el, d, dt) => ft(el, { y: d, opacity: 0 }, { y: 0, opacity: 1, duration: 0.42, ease: "power3.out" }, t + dt);
    out($(`${P}-hn${a}`), 66); inn($(`${P}-hn${b}`), 66, 0.16);
    out($(`${P}-hs${a}`), 40); inn($(`${P}-hs${b}`), 40, 0.24);
    out($(`${P}-hl${a}`), 40); inn($(`${P}-hl${b}`), 40, 0.3);
    for (let j = 1; j <= K.NSEG; j++) {
      if (!segOn(j, a) && segOn(j, b)) ft($(`${P}-hg${j}`), { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: "power2.out" }, t + 0.22);
    }
    ft($(`${P}-hglow`), { opacity: 0 }, { opacity: 1, duration: 0.14, ease: "power2.out" }, t + 0.05);
    ft($(`${P}-hglow`), { opacity: 1 }, { opacity: 0, duration: 0.5, ease: "power2.inOut" }, t + 0.19);
  };
  // standard scene opening for s03 … s08: header shows item a at 0 and rolls to b
  K.headerScene = (S, P, a, b, t = 0.02) => { K.headerSet(S, P, a); K.headerSwap(S, P, a, b, t); };
  // header exit (last scene with a header): plate + contents lift away
  K.headerOut = (S, P, t) => { const { ft, $ } = S; ft($(`${P}-hdr`), { opacity: 1, y: 0 }, { opacity: 0, y: -30, duration: 0.24, ease: "power2.in" }, t); };
})();

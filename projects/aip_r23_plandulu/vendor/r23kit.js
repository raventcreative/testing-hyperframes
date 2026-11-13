// R23 PLAN (rencana dulu) — shared scene kit (loaded in index.html <head> after vo_words.js + r23icons.js; every scene uses window.R23K).
// Adapted from the R19/R15 NAVY kit. Components (identical in every scene that shows them): the TOPIC HEADER (icon roll, name, one-line
// job, chip, 7 progress segments), lucide icons (ISC), the PROMPT PILL (icon disc + typed request), the BLUEPRINT sheet (cyan grid on
// deep blue), the PLAN DOCUMENT (our own mock of a written plan: Tujuan / File disentuh / Dihapus / Cara ngetes), file rows, the
// timeline boilerplate (scale patch, ft, I, wt, seek patch, per-letter typing). Every initial state is pinned at 0 in a NESTED timeline
// that is the first child of the scene timeline at 0 (I); finish() = end marker + backward-seek patch + tl.render(0, true, true) +
// registration. Deterministic: no Math.random, no Date, no rAF.
(function () {
  const K = (window.R23K = {});
  const ICO = window.R23_ICO || {};
  K.svg = (n, cls = "", extra = "") =>
    `<svg class="${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ${extra}>${ICO[n] || ""}</svg>`;

  // ------------------------------------------------------------------ topic header items (s04 … s10)
  K.HD = [
    { tile: "package-open", name: "OpenCode + Hermes", sub: "agent AI open source &middot; <i>gratis</i>", chip: "MIT", chipIc: "lock-open" },
    { tile: "folder-code", name: "Kerja di folder", sub: "model bebas &middot; <i>skill &middot; sub-agent</i>", chip: "BEBAS", chipIc: "sparkles" },
    { tile: "square-terminal", name: "OpenCode", sub: "agent Plan &middot; <i>baca, belum ngedit</i>", chip: "PLAN", chipIc: "eye" },
    { tile: "scroll-text", name: "Hermes", sub: "/plan &middot; <i>rencana jadi file .md</i>", chip: "/plan", chipIc: "file-text" },
    { tile: "scan-search", name: "Cek rencana", sub: "3 hal sebelum kamu setuju", chip: "3 CEK", chipIc: "list-checks" },
    { tile: "eraser", name: "Revisi di rencana", sub: "coret denah, <i>bukan bongkar kode</i>", chip: "HEMAT", chipIc: "coins" },
    { tile: "hammer", name: "Baru kerja", sub: "setuju dulu &middot; <i>baru jalan</i>", chip: "JALAN", chipIc: "play" },
  ];
  K.NSEG = 7;

  // ------------------------------------------------------------------ geometry (global px)
  K.HDR = { x: 60, y: 312, w: 960, h: 140 };
  K.SEG = (k) => ({ x: 768 + (k - 1) * 33, y: 342 });
  K.DOC = { x: 90, y: 476, w: 900, h: 432 };            // the plan document (s07 → s10 hand it over at this position)

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
  .k-hseg{position:absolute;top:342px;width:26px;height:8px;border-radius:4px;background:rgba(255,255,255,.16);overflow:hidden}
  .k-hseg b{position:absolute;left:0;top:0;width:26px;height:8px;background:#01ccf7;border-radius:4px;transform-origin:0 50%;box-shadow:0 0 10px rgba(1,204,247,.8)}
  .k-hchip{position:absolute;right:0;top:0;height:40px;padding:0 16px 0 12px;border-radius:20px;display:flex;align-items:center;gap:8px;
    font:700 18px/1 Poppins;letter-spacing:1.5px;color:#6adfff;background:rgba(1,204,247,.10);box-shadow:inset 0 0 0 1.5px rgba(1,204,247,.5);white-space:nowrap}
  .k-hchip svg{width:20px;height:20px}
  .k-chk{position:absolute;height:46px;padding:0 18px 0 12px;border-radius:23px;display:flex;align-items:center;gap:10px;font:700 21px/1 Poppins;color:#fff;
    background:rgba(45,164,78,.22);box-shadow:inset 0 0 0 1.5px rgba(80,210,120,.7);white-space:nowrap}
  .k-chk svg{width:24px;height:24px;color:#5be08a}
  .k-amb{position:absolute;height:46px;padding:0 18px 0 12px;border-radius:23px;display:flex;align-items:center;gap:10px;font:700 21px/1 Poppins;color:#ffd58a;
    background:rgba(255,183,77,.14);box-shadow:inset 0 0 0 1.5px rgba(255,183,77,.7);white-space:nowrap}
  .k-amb svg{width:24px;height:24px;color:#ffc761}
  .k-demo{position:absolute;height:30px;padding:0 12px;border-radius:15px;font:700 15px/30px Poppins;letter-spacing:1.5px;color:#b8c7dd;
    background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 1.2px rgba(255,255,255,.22);white-space:nowrap}
  .k-demo.w{color:#5d6f8f;background:#eef3fb;box-shadow:inset 0 0 0 1.2px #d5deec}
  .k-foot{position:absolute;font:400 20px/30px Poppins;color:#9fb3cf;white-space:nowrap}
  .k-foot b{font-weight:700;color:#e3edfa}
  /* prompt pill: what you ask the agent */
  .k-ask{position:absolute;left:0;top:0;height:84px;border-radius:42px;background:rgba(8,16,52,.92);box-shadow:inset 0 0 0 2px rgba(106,223,255,.55),0 0 30px rgba(1,204,247,.22),0 20px 40px rgba(2,6,26,.5);transform-origin:50% 50%}
  .k-ask .ic{position:absolute;left:10px;top:10px;width:64px;height:64px;border-radius:32px;background:linear-gradient(160deg,#9cecff,#01ccf7 55%,#0aa7d6);color:#0b1440;box-shadow:0 0 20px rgba(1,204,247,.5)}
  .k-ask .ic svg{position:absolute;left:16px;top:16px;width:32px;height:32px}
  .k-ask .tx{position:absolute;left:92px;top:0;font:400 29px/84px Poppins;color:#ffffff;white-space:nowrap}
  .k-ask .tx b{font-weight:700;color:#6adfff}
  .k-caret{display:inline-block;width:3px;height:34px;margin-left:3px;vertical-align:-6px;background:#6adfff}
  /* blueprint sheet (denah): cyan grid on deep blue */
  .k-bp{position:absolute;border-radius:22px;overflow:hidden;background-color:#0e3478;
    background-image:linear-gradient(rgba(140,225,255,.16) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(140,225,255,.16) 1.5px,transparent 1.5px),
      linear-gradient(rgba(140,225,255,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(140,225,255,.07) 1px,transparent 1px);
    background-size:60px 60px,60px 60px,15px 15px,15px 15px;box-shadow:inset 0 0 0 2px rgba(150,230,255,.45),0 24px 50px rgba(2,6,26,.55)}
  .k-bp .tag{position:absolute;height:34px;padding:0 14px;border-radius:17px;font:700 16px/34px Poppins;letter-spacing:2px;color:#0b1440;background:#bff0ff;white-space:nowrap}
  /* plan document (our mock of a written plan) */
  .k-doc{position:absolute;left:0;top:0;width:900px;height:432px;border-radius:26px;background:linear-gradient(180deg,#ffffff,#f4f7fc);box-shadow:0 26px 56px rgba(2,6,26,.55);overflow:hidden;transform-origin:0 0}
  .k-doc .st{position:absolute;left:0;top:0;width:900px;height:66px;background-color:#0e3478;
    background-image:linear-gradient(rgba(140,225,255,.18) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(140,225,255,.18) 1.5px,transparent 1.5px);background-size:22px 22px,22px 22px}
  .k-doc .st svg{position:absolute;left:22px;top:17px;width:32px;height:32px;color:#bff0ff}
  .k-doc .st b{position:absolute;left:66px;top:0;font:700 25px/66px Poppins;letter-spacing:3px;color:#ffffff;white-space:nowrap}
  .k-doc .st span{position:absolute;left:236px;top:0;font:400 21px/66px Poppins;color:#9fdcf2;white-space:nowrap}
  .k-doc .st i{position:absolute;right:18px;top:16px;height:34px;padding:0 13px;border-radius:17px;font:700 15px/34px Poppins;font-style:normal;letter-spacing:1.5px;color:#0b1440;background:#bff0ff;white-space:nowrap}
  .k-doc .rw{position:absolute;left:18px;width:864px;height:80px;border-radius:18px}
  .k-doc .rw .hl{position:absolute;inset:0;border-radius:18px;background:#e6f8ff;box-shadow:inset 0 0 0 2px #8fe3fb;opacity:0}
  .k-doc .rw .hl.am{background:#fff4e0;box-shadow:inset 0 0 0 2px #ffc761}
  .k-doc .rw .nb{position:absolute;left:12px;top:18px;width:44px;height:44px;border-radius:13px;background:#0e3478;color:#bff0ff;font:700 22px/44px Poppins;text-align:center}
  .k-doc .rw .nb svg{position:absolute;left:10px;top:10px;width:24px;height:24px}
  .k-doc .rw .lb{position:absolute;left:72px;top:0;font:700 23px/80px Poppins;color:#294b77;white-space:nowrap}
  .k-doc .rw .vl{position:absolute;left:282px;top:0;font:400 28px/80px Poppins;color:#0a0d2c;white-space:nowrap}
  .k-doc .rw .vl b{font-weight:700}
  .k-doc .rw .ok{position:absolute;right:14px;top:16px;width:48px;height:48px;border-radius:24px;background:#2da44e;color:#fff;box-shadow:0 0 0 5px rgba(45,164,78,.18)}
  .k-doc .rw .ok svg{position:absolute;left:11px;top:11px;width:26px;height:26px}
  .k-doc .rw .wa{position:absolute;right:14px;top:16px;width:48px;height:48px;border-radius:24px;background:#f0a020;color:#fff;box-shadow:0 0 0 5px rgba(240,160,32,.2)}
  .k-doc .rw .wa svg{position:absolute;left:11px;top:10px;width:26px;height:26px}
  .k-doc .ln{position:absolute;left:18px;width:864px;height:1.5px;background:#e2e8f3}
  /* file row (dark) */
  .k-file{position:absolute;left:0;top:0;height:62px;border-radius:16px;background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.12);white-space:nowrap}
  .k-file svg.fi{position:absolute;left:16px;top:15px;width:32px;height:32px;color:#9fdcf2}
  .k-file b{position:absolute;left:60px;top:0;font:700 25px/62px Poppins;color:#ffffff}
  /* stamp */
  .k-stamp{position:absolute;left:0;top:0;height:78px;padding:0 26px;border-radius:16px;font:700 32px/72px Poppins;letter-spacing:3px;white-space:nowrap;
    border:4px solid currentColor;transform-origin:50% 50%}
  .k-stamp.am{color:#ffb547;background:rgba(40,24,0,.82)}
  .k-stamp.gr{color:#3fd47a;background:rgba(4,40,20,.86)}
  `;
  if (!document.getElementById("r23kit-css")) {
    const st = document.createElement("style"); st.id = "r23kit-css"; st.textContent = CSS; document.head.appendChild(st);
  }

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

  // ------------------------------------------------------------------ PROMPT PILL
  K.askHTML = (id, w, icon = "bot") => `<div class="k-ask" id="${id}" style="width:${w}px"><div class="ic">${K.svg(icon)}</div><div class="tx" id="${id}-tx"></div></div>`;

  // ------------------------------------------------------------------ PLAN DOCUMENT
  // rows: Tujuan / File disentuh / Dihapus / Cara ngetes (CONTOH). File row value is split so "style.css" can be flagged and struck.
  K.DOC_ROWS = [
    { nb: "target", lb: "Tujuan", vl: "tombol WA buka chat pesanan" },
    { nb: "1", lb: "File disentuh", vl: `tombol-wa.js, index.html<span class="xtra">, <b>style.css</b></span>` },
    { nb: "2", lb: "Dihapus", vl: "<b>tidak ada</b>" },
    { nb: "3", lb: "Cara ngetes", vl: "klik tombol &rarr; chat WA terbuka" },
  ];
  K.docHTML = (P, title = "RENCANA", file = "tombol-wa.md") => {
    let h = `<div class="k-doc" id="${P}-doc"><div class="st">${K.svg("scroll-text")}<b>${title}</b><span id="${P}-dfile">${file}</span><i>CONTOH</i></div>`;
    K.DOC_ROWS.forEach((r, i) => {
      const y = 82 + i * 86;
      if (i) h += `<div class="ln" style="top:${y - 4}px"></div>`;
      h += `<div class="rw" id="${P}-r${i}" style="top:${y}px"><div class="hl" id="${P}-h${i}"></div><div class="hl am" id="${P}-a${i}"></div>` +
        `<div class="nb">${r.nb === "target" ? K.svg("map") : r.nb}</div><div class="lb">${r.lb}</div><div class="vl" id="${P}-v${i}">${r.vl}</div>` +
        `<div class="ok" id="${P}-o${i}">${K.svg("check")}</div><div class="wa" id="${P}-w${i}">${K.svg("triangle-alert")}</div></div>`;
    });
    return h + `</div>`;
  };
  // frame-0 state of the plan document at its standard position (all rows shown, no marks)
  K.docSet = (S, P, opts = {}) => {
    const { I, $ } = S;
    I($(`${P}-doc`), Object.assign({ x: K.DOC.x, y: K.DOC.y, scale: 1, opacity: 1 }, opts.doc || {}));
    for (let i = 0; i < 4; i++) {
      I($(`${P}-h${i}`), { opacity: 0 }); I($(`${P}-a${i}`), { opacity: 0 });
      I($(`${P}-o${i}`), { scale: 0, opacity: 0, transformOrigin: "50% 50%" }); I($(`${P}-w${i}`), { scale: 0, opacity: 0, transformOrigin: "50% 50%" });
    }
  };

  // ------------------------------------------------------------------ TOPIC HEADER
  K.headerHTML = (P) => {
    let h = `<div class="k-hplate" id="${P}-hplate"></div><div class="k-hglow" id="${P}-hglow"></div>`;
    h += `<div class="k-hnum" id="${P}-hnum"><div class="k-hroll" id="${P}-hroll">` + K.HD.map((d) => `<b>${K.svg(d.tile)}</b>`).join("") + `</div></div>`;
    h += `<div class="k-hbox" id="${P}-hnb" style="left:214px;top:328px;width:540px;height:66px">` + K.HD.map((d, k) => `<div class="k-hname" id="${P}-hn${k}">${d.name}</div>`).join("") + `</div>`;
    h += `<div class="k-hbox" id="${P}-hsb" style="left:214px;top:396px;width:530px;height:40px">` + K.HD.map((d, k) => `<div class="k-hsub" id="${P}-hs${k}">${d.sub}</div>`).join("") + `</div>`;
    h += `<div class="k-hbox" id="${P}-hlb" style="left:752px;top:384px;width:250px;height:40px">` + K.HD.map((d, k) => `<div class="k-hchip" id="${P}-hl${k}">${K.svg(d.chipIc)}${d.chip}</div>`).join("") + `</div>`;
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
  // standard scene opening for s05 … s10: header shows item a at 0 and rolls to b
  K.headerScene = (S, P, a, b, t = 0.02) => { K.headerSet(S, P, a); K.headerSwap(S, P, a, b, t); };
})();

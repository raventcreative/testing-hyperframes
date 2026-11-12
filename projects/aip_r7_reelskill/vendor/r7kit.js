// R7 REELSKILL — shared scene kit (loaded in index.html <head> after vo_words.js; every scene uses window.R7K).
// "1 skill Claude bikin reels animasi tanpa kredit video AI": the four SHOWCASE mini-scenes are real HTML/CSS/SVG + GSAP builds
// (cerita anak sebelum tidur, kartun lompat-lompat, kolam koi, film pendek) that any scene can mount at any size, plus the style
// chips row, the player stage, the code "compile" flash, lucide icons (ISC), the Claude mark and the timeline boilerplate
// (scale patch, ft, I = pin at frame 0, wt = scene-local word time, seek patch). Deterministic: no Math.random, no Date, no rAF.
(function () {
  const K = (window.R7K = {});
  // ------------------------------------------------------------------ icons (lucide, ISC)
  K.IC = {
    moon: '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>',
    smile: '<circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" x2="9.01" y1="9" y2="9"/><line x1="15" x2="15.01" y1="9" y2="9"/>',
    fish: '<path d="M6.5 12c.94-3.46 4.94-6 8.5-6 3.56 0 6.06 2.54 7 6-.94 3.47-3.44 6-7 6s-7.56-2.53-8.5-6Z"/><path d="M18 12v.5"/><path d="M16 17.93a9.77 9.77 0 0 1 0-11.86"/><path d="M7 10.67C7 8 5.58 5.97 2.73 5.5c-1 1.5-1 5 .23 6.5-1.24 1.5-1.24 5-.23 6.5C5.58 18.03 7 16 7 13.33"/><path d="M10.46 7.26C10.2 5.88 9.17 4.24 8 3h5.8a2 2 0 0 1 1.98 1.67l.23 1.4"/><path d="m16.01 17.93-.23 1.4A2 2 0 0 1 13.8 21H9.5a5.96 5.96 0 0 0 1.49-3.98"/>',
    clap: '<path d="M20.2 6 3 11l-.9-2.4c-.3-1.1.3-2.2 1.3-2.5l13.5-4c1.1-.3 2.2.3 2.5 1.3Z"/><path d="m6.2 5.3 3.1 3.9"/><path d="m12.4 3.4 3.1 4"/><path d="M3 11h18v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/>',
    coins: '<circle cx="8" cy="8" r="6"/><path d="M18.09 10.37A6 6 0 1 1 10.34 18"/><path d="M7 6h1v4"/><path d="m16.71 13.88.7.71-2.82 2.82"/>',
    scissors: '<circle cx="6" cy="6" r="3"/><path d="M8.12 8.12 12 12"/><path d="M20 4 8.12 15.88"/><circle cx="6" cy="18" r="3"/><path d="M14.8 14.8 20 20"/>',
    bulb: '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>',
    film: '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 3v18"/><path d="M3 7.5h4"/><path d="M3 12h18"/><path d="M3 16.5h4"/><path d="M17 3v18"/><path d="M17 7.5h4"/><path d="M17 16.5h4"/>',
    wave: '<path d="M2 10v3"/><path d="M6 6v11"/><path d="M10 3v18"/><path d="M14 8v7"/><path d="M18 5v13"/><path d="M22 10v3"/>',
    video: '<path d="m16 13 5.223 3.482a.5.5 0 0 0 .777-.416V7.87a.5.5 0 0 0-.752-.432L16 10.5"/><rect x="2" y="6" width="14" height="12" rx="2"/>',
    book: '<path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/>',
    download: '<path d="M12 15V3"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/>',
    eye: '<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>',
    terminal: '<path d="M12 19h8"/><path d="m4 17 6-6-6-6"/>',
    code: '<path d="m18 16 4-4-4-4"/><path d="m6 8-4 4 4 4"/><path d="m14.5 4-5 16"/>',
    check: '<path d="M20 6 9 17l-5-5"/>',
    x: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    play: '<path d="M5 5a2 2 0 0 1 3.008-1.728l11.997 6.998a2 2 0 0 1 .003 3.458l-12 7A2 2 0 0 1 5 19z"/>',
    laptop: '<path d="M18 5a2 2 0 0 1 2 2v8.526a2 2 0 0 0 .212.897l1.068 2.127a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45l1.068-2.127A2 2 0 0 0 4 15.526V7a2 2 0 0 1 2-2z"/><path d="M20.054 15.987H3.946"/>',
    sparkles: '<path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/>',
    heart: '<path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5"/>',
    send: '<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/>',
    user: '<circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/>',
    link: '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
    unlock: '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/>',
    file: '<path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/><path d="M14 2v5a1 1 0 0 0 1 1h5"/>',
    type: '<path d="M12 4v16"/><path d="M4 7V5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2"/><path d="M9 20h6"/>',
    pointer: '<path d="M4.037 4.688a.495.495 0 0 1 .651-.651l16 6.5a.5.5 0 0 1-.063.947l-6.124 1.58a2 2 0 0 0-1.438 1.435l-1.579 6.126a.5.5 0 0 1-.947.063z"/>',
  };
  K.svg = (n, cls = "", extra = "") =>
    `<svg class="${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ${extra}>${K.IC[n]}</svg>`;
  K.CLAUDE_D = "M4.709 15.955l4.72-2.647.08-.23-.08-.128H9.2l-.79-.048-2.698-.073-2.339-.097-2.266-.122-.571-.121L0 11.784l.055-.352.48-.321.686.06 1.52.103 2.278.158 1.652.097 2.449.255h.389l.055-.157-.134-.098-.103-.097-2.358-1.596-2.552-1.688-1.336-.972-.724-.491-.364-.462-.158-1.008.656-.722.881.06.225.061.893.686 1.908 1.476 2.491 1.833.365.304.145-.103.019-.073-.164-.274-1.355-2.446-1.446-2.49-.644-1.032-.17-.619a2.970 2.970 0 01-.104-.729L6.283.134 6.696 0l.996.134.42.364.62 1.414 1.002 2.229 1.555 3.03.456.898.243.832.091.255h.158V9.01l.128-1.706.237-2.095.23-2.695.08-.76.376-.91.747-.492.584.28.48.685-.067.444-.286 1.851-.559 2.903-.364 1.942h.212l.243-.242.985-1.306 1.652-2.064.73-.82.85-.904.547-.431h1.033l.76 1.129-.34 1.166-1.064 1.347-.881 1.142-1.264 1.7-.79 1.36.073.11.188-.02 2.856-.606 1.543-.28 1.841-.315.833.388.091.395-.328.807-1.969.486-2.309.462-3.439.813-.042.03.049.061 1.549.146.662.036h1.622l3.020.225.79.522.474.638-.079.485-1.215.62-1.64-.389-3.829-.91-1.312-.329h-.182v.11l1.093 1.068 2.006 1.81 2.509 2.33.127.578-.322.455-.34-.049-2.205-1.657-.851-.747-1.926-1.62h-.128v.17l.444.649 2.345 3.521.122 1.08-.17.353-.608.213-.668-.122-1.374-1.925-1.415-2.167-1.143-1.943-.14.08-.674 7.254-.316.37-.729.28-.607-.461-.322-.747.322-1.476.389-1.924.315-1.53.286-1.9.17-.632-.012-.042-.14.018-1.434 1.967-2.18 2.945-1.726 1.845-.414.164-.717-.37.067-.662.401-.589 2.388-3.036 1.44-1.882.93-1.086-.006-.158h-.055L4.132 18.56l-1.13.146-.487-.456.061-.746.231-.243 1.908-1.312-.006.006z";
  K.claude = (cls = "") => `<svg class="${cls}" viewBox="0 0 24 24"><path d="${K.CLAUDE_D}" fill="#D97757"/></svg>`;
  K.hash = (n) => { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };

  // ------------------------------------------------------------------ the four styles (chips + code shown in the "compile" flash)
  K.STYLES = [
    { id: "bed", label: "cerita anak", ic: "moon", w: 236,
      code: ['<div id="bulan" class="ngantuk"></div>', 'gsap.to("#bulan", { y: -150, duration: 1.2 })', 'gsap.to(".bintang", { scale: 1, stagger: 0.08 })'] },
    { id: "toon", label: "kartun", ic: "smile", w: 168,
      code: ['<div id="bolo" class="kartun"></div>', 'gsap.to("#bolo", { y: -170, yoyo: true, repeat: 5 })', 'gsap.to("#bolo", { scaleY: 0.72, ease: "bounce" })'] },
    { id: "koi", label: "kolam koi", ic: "fish", w: 208,
      code: ['<svg class="koi" id="koi-1">…</svg>', 'gsap.to(".koi", { x: 420, rotation: 30 })', 'gsap.to(".riak", { scale: 1.6, opacity: 0 })'] },
    { id: "film", label: "film pendek", ic: "clap", w: 236,
      code: ['<section class="adegan-1"></section>', 'gsap.to(".hujan", { y: 520, repeat: 40 })', 'gsap.from(".subtitle", { opacity: 0 })'] },
  ];
  K.CHIPS = { y: 316, h: 60, gap: 16 };
  K.STAGE = { x: 60, y: 392, w: 960, h: 520 };
  K.chipX = (k) => { const tot = K.STYLES.reduce((a, s) => a + s.w, 0) + K.CHIPS.gap * 3; let x = 540 - tot / 2; for (let i = 0; i < k; i++) x += K.STYLES[i].w + K.CHIPS.gap; return x; };

  // tiny syntax highlighter for the code lines (Poppins only — house rule)
  const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  K.hl = (s) => {
    if (/^\s*(\/\/|<!--|#)/.test(s)) return `<span class="c-com">${esc(s)}</span>`;
    let o = ""; const re = /("[^"]*")|(<\/?[a-zA-Z][\w-]*|\/?>)|(\b(?:gsap|const|tl|def|return)\b)|(\b\d+(?:\.\d+)?\b)|(\b[a-zA-Z_]\w*(?=\s*:))|([\s\S])/g; let m;
    while ((m = re.exec(s))) {
      if (m[1]) o += `<span class="c-str">${esc(m[1])}</span>`;
      else if (m[2]) o += `<span class="c-tag">${esc(m[2])}</span>`;
      else if (m[3]) o += `<span class="c-kw">${esc(m[3])}</span>`;
      else if (m[4]) o += `<span class="c-num">${esc(m[4])}</span>`;
      else if (m[5]) o += `<span class="c-key">${esc(m[5])}</span>`;
      else o += esc(m[6]);
    }
    return o;
  };

  // ------------------------------------------------------------------ shared CSS (injected once)
  const CSS = `
  .k-ab{position:absolute;left:0;top:0}
  .k-glass{position:absolute;border-radius:30px;background:rgba(12,22,64,.82);box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.10),0 18px 40px rgba(3,6,24,.35)}
  .c-com{color:#7f8db0}.c-str{color:#a6e88a}.c-tag{color:#6adfff}.c-kw{color:#ff9ac1}.c-num{color:#ffd27a}.c-key{color:#ffd27a}
  /* style chips */
  .k-chip{position:absolute;left:0;top:0;height:60px;border-radius:30px;background:rgba(12,22,64,.86);box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.12),0 12px 26px rgba(3,6,24,.35);transform-origin:50% 50%}
  .k-chip .f{position:absolute;inset:0;border-radius:30px;background:linear-gradient(160deg,#9cecff 0%,#01ccf7 52%,#0aa7d6 100%);box-shadow:0 0 22px rgba(1,204,247,.5);opacity:0}
  .k-chip .l{position:absolute;left:0;top:0;right:0;height:60px;display:flex;align-items:center;justify-content:center;gap:10px;font:700 24px/60px Poppins;color:#e3edfa;white-space:nowrap}
  .k-chip .l.n{color:#0b1440;opacity:0}
  .k-chip svg{width:26px;height:26px}
  /* player stage */
  .k-stage{position:absolute;left:60px;top:392px;width:960px;height:520px;border-radius:28px;overflow:hidden;background:#060b26;
    box-shadow:0 0 0 1.5px rgba(255,255,255,.16),0 30px 60px rgba(2,6,26,.55)}
  .k-stage .host{position:absolute;left:0;top:0;width:960px;height:520px;overflow:hidden}
  .k-stage-ring{position:absolute;left:60px;top:392px;width:960px;height:520px;border-radius:28px;box-shadow:inset 0 0 0 2px rgba(106,223,255,.9),0 0 34px rgba(1,204,247,.35);opacity:0}
  .k-badge{position:absolute;height:40px;padding:0 16px 0 12px;border-radius:20px;display:flex;align-items:center;gap:8px;white-space:nowrap;
    font:700 19px/40px Poppins;color:#e3edfa;background:rgba(6,11,38,.72);box-shadow:inset 0 0 0 1.5px rgba(106,223,255,.45)}
  .k-badge svg{width:20px;height:20px;color:#6adfff}
  .k-bar{position:absolute;left:24px;right:24px;bottom:14px;height:6px;border-radius:3px;background:rgba(255,255,255,.22);overflow:hidden}
  .k-bar b{position:absolute;left:0;top:0;width:100%;height:6px;border-radius:3px;background:#01ccf7;transform-origin:0 50%;box-shadow:0 0 10px rgba(1,204,247,.8)}
  /* code flash ("compile") */
  .k-code{position:absolute;left:0;top:0;width:960px;height:520px;background:linear-gradient(180deg,#0a1132,#070c28);overflow:hidden}
  .k-code .hd{position:absolute;left:0;top:0;width:960px;height:52px;background:rgba(255,255,255,.04);border-bottom:1.5px solid rgba(255,255,255,.06)}
  .k-code .hd i{position:absolute;top:20px;width:12px;height:12px;border-radius:50%}
  .k-code .fn{position:absolute;left:96px;top:0;font:700 20px/52px Poppins;color:#9fdcf2;white-space:nowrap}
  .k-code .ln{position:absolute;left:44px;font:400 26px/40px Poppins;color:#e3edfa;white-space:nowrap}
  .k-code .ln u{position:absolute;left:-34px;top:0;text-decoration:none;font:400 20px/40px Poppins;color:#4b5a86}
  .k-code .scan{position:absolute;left:0;top:0;width:960px;height:520px;background:linear-gradient(90deg,rgba(1,204,247,0) 0%,rgba(1,204,247,.55) 88%,#bff4ff 100%);transform-origin:0 50%}
  /* ============ MINI-SCENES (pure HTML/CSS/SVG, animated on the scene timeline) */
  .m-abs{position:absolute;left:0;top:0}
  .m-fill{position:absolute;left:0;top:0;width:100%;height:100%}
  .m-star{position:absolute;border-radius:50%;background:#fff;box-shadow:0 0 6px rgba(255,255,255,.9)}
  .m-moon{position:absolute;border-radius:50%;background:radial-gradient(circle at 38% 35%,#fff8d8 0%,#ffe9a3 55%,#f6cf6e 100%);box-shadow:0 0 40px rgba(255,233,163,.55),0 0 110px rgba(255,214,120,.28)}
  .m-moon i{position:absolute;border-radius:50%;background:rgba(214,170,80,.35)}
  .m-cloud{position:absolute}
  .m-cloud b{position:absolute;border-radius:50%}
  .m-story{position:absolute;white-space:nowrap;border-radius:999px;background:rgba(10,10,40,.62);color:#fff7e0;box-shadow:inset 0 0 0 1.5px rgba(255,240,200,.25)}
  .m-zzz{position:absolute;font-weight:700;color:#fff3c4;white-space:nowrap}
  .m-comic{position:absolute;font-weight:700;color:#ffd54a;white-space:nowrap;letter-spacing:1px;transform-origin:50% 50%}
  .m-ripple{position:absolute;border-radius:50%;border:2px solid rgba(230,255,252,.7);transform-origin:50% 50%}
  .m-pad{position:absolute;border-radius:50%;transform-origin:50% 50%}
  .m-fish{position:absolute;left:0;top:0;transform-origin:50% 50%}
  .m-fish .tl{position:absolute;transform-origin:100% 50%}
  .m-rain{position:absolute;left:0;top:0;width:100%}
  .m-sub{position:absolute;left:0;width:100%;text-align:center;font-weight:400;color:#fff;white-space:nowrap}
  `;
  if (!document.getElementById("r7kit-css")) {
    const st = document.createElement("style"); st.id = "r7kit-css"; st.textContent = CSS; document.head.appendChild(st);
  }

  // ------------------------------------------------------------------ timeline boilerplate
  K.scene = (id, D) => {
    const tl = gsap.timeline({ paused: true });
    const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
    // positions are clamped to >= 0 (a child placed before 0 would render BEFORE the frame-0 pins and be overridden by them)
    const cl = (p) => (typeof p === "number" ? Math.max(0, p) : p);
    { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); tl.set = (a, v, p) => s0(a, _sc(v), cl(p)); tl.fromTo = (a, x, y, p) => f0(a, _sc(x), _sc(y), cl(p)); tl.to = (a, v, p) => t0(a, _sc(v), cl(p)); }
    const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), typeof t === "number" ? Math.max(0.005, t) : t);
    const I = (el, v) => { gsap.set(el, _sc(v)); tl.set(el, v, 0); };
    const SC = (window.VO_SCENES || []).find((s) => s.id === id) || { start: 0 };
    const T0 = SC.start;
    const wt = (txt, after = 0) => { const w = (window.VO_WORDS || []).find((x) => x[0] === txt && x[1] >= after - 1e-6); if (!w) throw new Error(id + ": word not found " + txt); return w[1] - T0; };
    const $ = (x) => document.getElementById(x);
    const finish = () => {
      tl.set({}, {}, D - 0.01);
      (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
      window.__timelines = window.__timelines || {};
      window.__timelines[id] = tl;
    };
    let seed = 7; const rnd = () => { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; };
    // per-letter typing: spans with opacity set at times (no onUpdate)
    const type = (el, text, t0, cps, cls = "") => {
      el.innerHTML = Array.from(text).map((c) => `<span class="${cls}">${c === " " ? "&nbsp;" : c.replace(/&/g, "&amp;").replace(/</g, "&lt;")}</span>`).join("");
      const sp = el.querySelectorAll("span"); sp.forEach((s, i) => { I(s, { opacity: 0 }); tl.set(s, { opacity: 1 }, t0 + i / cps); });
      return t0 + sp.length / cps;
    };
    // finite seekable loop (no repeat: -1 → the timeline keeps a finite duration)
    const loop = (el, a, b, per, t0, t1, ease = "sine.inOut", yoyo = true) => {
      const n = Math.max(1, Math.ceil((t1 - t0) / per));
      I(el, a);
      return ft(el, a, Object.assign({}, b, { duration: per, ease, repeat: n - 1, yoyo }), t0);
    };
    return { tl, ft, I, wt, $, finish, rnd, type, loop, T0, D, id };
  };

  // ------------------------------------------------------------------ STYLE CHIPS ROW (s04)
  K.chipsHTML = (P) => K.STYLES.map((s, k) => `<div class="k-chip" id="${P}-chip${k}" style="width:${s.w}px"><div class="f" id="${P}-chipf${k}"></div>` +
    `<div class="l" id="${P}-chipw${k}">${K.svg(s.ic)}${s.label}</div><div class="l n" id="${P}-chipn${k}">${K.svg(s.ic)}${s.label}</div></div>`).join("");
  K.chipSet = (S, P, act) => { for (let k = 0; k < 4; k++) { S.I(S.$(`${P}-chip${k}`), { x: K.chipX(k), y: K.CHIPS.y, scale: 1, opacity: 1 }); S.I(S.$(`${P}-chipf${k}`), { opacity: k === act ? 1 : 0 }); S.I(S.$(`${P}-chipn${k}`), { opacity: k === act ? 1 : 0 }); S.I(S.$(`${P}-chipw${k}`), { opacity: k === act ? 0 : 1 }); } };
  K.chipGo = (S, P, a, b, t) => {
    const { ft, $ } = S;
    if (a >= 0) { ft($(`${P}-chipf${a}`), { opacity: 1 }, { opacity: 0, duration: 0.18 }, t); ft($(`${P}-chipn${a}`), { opacity: 1 }, { opacity: 0, duration: 0.18 }, t); ft($(`${P}-chipw${a}`), { opacity: 0 }, { opacity: 1, duration: 0.18 }, t); }
    ft($(`${P}-chipw${b}`), { opacity: 1 }, { opacity: 0, duration: 0.18 }, t + 0.04);
    ft($(`${P}-chipf${b}`), { opacity: 0 }, { opacity: 1, duration: 0.18 }, t + 0.04); ft($(`${P}-chipn${b}`), { opacity: 0 }, { opacity: 1, duration: 0.18 }, t + 0.04);
    ft($(`${P}-chip${b}`), { scale: 1 }, { scale: 1.1, duration: 0.12, yoyo: true, repeat: 1, ease: "power2.out" }, t + 0.04);
  };

  // ------------------------------------------------------------------ CODE FLASH ("compile": code lines → scan wipe → picture)
  K.codeHTML = (P, k, file) => {
    const st = K.STYLES[k];
    let h = `<div class="k-code" id="${P}-code${k}"><div class="hd"><i style="left:24px;background:#ff6b6b"></i><i style="left:44px;background:#ffd166"></i><i style="left:64px;background:#4ade80"></i>` +
      `<div class="fn">${file || st.id + ".html"}</div></div>`;
    st.code.forEach((l, i) => { h += `<div class="ln" id="${P}-cl${k}_${i}" style="left:${84}px;top:${96 + i * 64}px"><u>${i + 1}</u>${K.hl(l)}</div>`; });
    h += `<div class="scan" id="${P}-scan${k}"></div></div>`;
    return h;
  };
  // pins + tweens: overlay visible from tOn, lines appear, then the scan bar sweeps and the overlay is cut away (clip) at tWipe
  K.codeFlash = (S, P, k, tOn, tWipe) => {
    const { I, ft, tl, $ } = S;
    const c = $(`${P}-code${k}`), sc = $(`${P}-scan${k}`);
    I(c, { opacity: 0, clipPath: "inset(0px 0px 0px 0px)" }); tl.set(c, { opacity: 1 }, tOn);
    K.STYLES[k].code.forEach((_, i) => { const l = $(`${P}-cl${k}_${i}`); I(l, { opacity: 0, x: -16 }); ft(l, { opacity: 0, x: -16 }, { opacity: 1, x: 0, duration: 0.14, ease: "power2.out" }, tOn + 0.03 + i * 0.09); });
    I(sc, { scaleX: 0, opacity: 0 });
    ft(sc, { scaleX: 0, opacity: 0.9 }, { scaleX: 1, opacity: 0.9, duration: 0.24, ease: "power2.in" }, tWipe - 0.24);
    ft(c, { clipPath: "inset(0px 0px 0px 0px)" }, { clipPath: "inset(0px 0px 0px 960px)", duration: 0.26, ease: "power2.inOut" }, tWipe);
    tl.set(c, { opacity: 0 }, tWipe + 0.27);
  };

  // =================================================================== MINI-SCENES
  // Each builder: (S, host, P, o) with o = { w, h, t0, t1, ev: {...}, still } — fills `host` (a w×h box, overflow hidden) and adds its
  // animation to S.tl between t0 and t1 (scene-local). Ambient motion = finite yoyo loops; story beats at o.ev times.
  // `still`: the beats are already done at frame 0 (used by the hook tiles, which open mid-story).
  const px = (v) => v.toFixed(1) + "px";

  // ---------------- 1. CERITA ANAK SEBELUM TIDUR: night sky, sleepy moon rises, stars + constellation, house, Zzz, story line
  K.MINI = {};
  K.MINI.bed = (S, host, P, o) => {
    const { w, h, t0, t1 } = o, u = h / 520, ev = o.ev || {}, still = !!o.still;
    const { I, ft, loop, tl } = S;
    let H = `<div class="m-fill" style="background:linear-gradient(180deg,#0b1452 0%,#26236e 52%,#4b3a8c 100%)"></div>`;
    const NS = 30, stars = [];
    for (let i = 0; i < NS; i++) {
      const sx = K.hash(i * 3.1 + 1) * w, sy = K.hash(i * 5.7 + 2) * h * 0.62, r = (2 + 3 * K.hash(i * 7.3 + 3)) * u;
      stars.push(`<i class="m-star" id="${P}-st${i}" style="left:${px(sx)};top:${px(sy)};width:${px(r)};height:${px(r)}"></i>`);
    }
    H += stars.join("");
    // constellation (5 sparkle stars + line)
    const CS = [[0.16, 0.2], [0.27, 0.12], [0.37, 0.24], [0.79, 0.12], [0.9, 0.26]];
    H += `<svg class="m-abs" width="${w}" height="${h}" style="overflow:visible"><polyline id="${P}-cline" points="${CS.slice(0, 3).map(([a, b]) => `${a * w},${b * h}`).join(" ")}" fill="none" stroke="rgba(255,243,196,.55)" stroke-width="${2 * u}" stroke-dasharray="${600 * u}" />` +
      `<polyline id="${P}-cline2" points="${CS.slice(3).map(([a, b]) => `${a * w},${b * h}`).join(" ")}" fill="none" stroke="rgba(255,243,196,.55)" stroke-width="${2 * u}" stroke-dasharray="${600 * u}" /></svg>`;
    CS.forEach(([a, b], i) => {
      const s = 34 * u;
      H += `<div class="m-abs" id="${P}-bs${i}" style="left:${px(a * w - s / 2)};top:${px(b * h - s / 2)};width:${px(s)};height:${px(s)}"><svg viewBox="0 0 24 24" width="${s}" height="${s}"><path d="M12 0 C13 8 16 11 24 12 C16 13 13 16 12 24 C11 16 8 13 0 12 C8 11 11 8 12 0Z" fill="#fff3c4"/></svg></div>`;
    });
    // moon with a sleepy face (rises from behind the hills)
    const mr = 0.27 * h, mx = 0.5 * w - mr / 2, my = 0.13 * h;
    H += `<div class="m-abs" id="${P}-mw" style="left:${px(mx)};top:${px(my)};width:${px(mr)};height:${px(mr)}"><div class="m-abs" id="${P}-mb" style="width:${px(mr)};height:${px(mr)}">` +
      `<div class="m-moon" style="left:0;top:0;width:${px(mr)};height:${px(mr)}"><i style="left:${px(mr * .2)};top:${px(mr * .62)};width:${px(mr * .14)};height:${px(mr * .14)}"></i><i style="left:${px(mr * .66)};top:${px(mr * .18)};width:${px(mr * .1)};height:${px(mr * .1)}"></i></div>` +
      `<svg class="m-abs" width="${mr}" height="${mr}" viewBox="0 0 100 100"><path d="M30 46 Q37 53 44 46" fill="none" stroke="#8a5a2b" stroke-width="3.4" stroke-linecap="round"/><path d="M56 46 Q63 53 70 46" fill="none" stroke="#8a5a2b" stroke-width="3.4" stroke-linecap="round"/>` +
      `<ellipse cx="28" cy="58" rx="7" ry="4" fill="#ff9d8a" opacity=".55"/><ellipse cx="72" cy="58" rx="7" ry="4" fill="#ff9d8a" opacity=".55"/><path d="M43 63 Q50 69 57 63" fill="none" stroke="#8a5a2b" stroke-width="3" stroke-linecap="round"/></svg></div></div>`;
    // clouds
    const cloud = (id, x, y, s, a) => `<div class="m-cloud" id="${id}" style="left:${px(x)};top:${px(y)};width:${px(s * 2.2)};height:${px(s)}">` +
      `<b style="left:0;top:${px(s * .35)};width:${px(s * .9)};height:${px(s * .65)};background:rgba(196,190,245,${a})"></b><b style="left:${px(s * .5)};top:0;width:${px(s)};height:${px(s)};background:rgba(196,190,245,${a})"></b>` +
      `<b style="left:${px(s * 1.2)};top:${px(s * .3)};width:${px(s * .9)};height:${px(s * .7)};background:rgba(196,190,245,${a})"></b></div>`;
    H += cloud(`${P}-cl0`, 0.06 * w, 0.32 * h, 0.12 * h, 0.22) + cloud(`${P}-cl1`, 0.66 * w, 0.4 * h, 0.1 * h, 0.18);
    // hills
    H += `<svg class="m-abs" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none"><path d="M0 ${h * .64} Q ${w * .22} ${h * .5} ${w * .45} ${h * .62} T ${w} ${h * .58} V ${h} H 0Z" fill="#2c2c78"/>` +
      `<path d="M0 ${h * .78} Q ${w * .3} ${h * .62} ${w * .62} ${h * .7} T ${w} ${h * .72} V ${h} H 0Z" fill="#191a50"/></svg>`;
    // house + tree on the front hill
    const hx = 0.58 * w, hy = 0.55 * h, hs = 0.25 * h;
    H += `<svg class="m-abs" style="left:${px(hx)};top:${px(hy)}" width="${hs * 1.2}" height="${hs * 1.1}" viewBox="0 0 120 110"><path d="M10 50 L60 10 L110 50Z" fill="#6a4fb0"/><rect x="22" y="48" width="76" height="62" fill="#4a3a8e"/>` +
      `<rect x="70" y="16" width="12" height="22" fill="#6a4fb0"/><rect x="34" y="62" width="26" height="24" rx="3" fill="#ffd27a"/><path d="M47 62v24M34 74h26" stroke="#4a3a8e" stroke-width="3"/><rect x="70" y="78" width="16" height="32" fill="#2a2058"/></svg>`;
    H += `<div class="m-abs" id="${P}-win" style="left:${px(hx + 0.28 * hs * 1.2 - 0.25 * hs)};top:${px(hy + 0.56 * hs * 1.1 - 0.25 * hs)};width:${px(hs * .75)};height:${px(hs * .75)};border-radius:50%;background:radial-gradient(circle,rgba(255,210,122,.55),rgba(255,210,122,0) 68%)"></div>`;
    H += `<svg class="m-abs" style="left:${px(0.3 * w)};top:${px(0.5 * h)}" width="${0.16 * h}" height="${0.26 * h}" viewBox="0 0 60 100"><rect x="26" y="60" width="8" height="40" fill="#120f33"/><ellipse cx="30" cy="40" rx="24" ry="34" fill="#1f2a5e"/><ellipse cx="24" cy="32" rx="10" ry="14" fill="#2a3a74" opacity=".7"/></svg>`;
    // Zzz from the window
    for (let i = 0; i < 3; i++) H += `<div class="m-zzz" id="${P}-z${i}" style="left:${px(hx + 0.2 * hs)};top:${px(hy - 0.02 * h)};font-size:${px((22 + i * 6) * u)}">z</div>`;
    // shooting star
    H += `<div class="m-abs" id="${P}-shoot" style="width:${px(150 * u)};height:${px(3 * u)};border-radius:2px;background:linear-gradient(90deg,rgba(255,255,255,0),#fff);transform-origin:100% 50%"></div>`;
    // story line
    const story = o.story || "Malam itu, Kiki pamit ke Bulan…", fs = 26 * u;
    H += `<div class="m-story" id="${P}-story" style="left:50%;bottom:${px(22 * u)};height:${px(fs * 1.9)};padding:0 ${px(fs * .9)};font:400 ${px(fs)}/${px(fs * 1.9)} Poppins;transform:translateX(-50%)"><span id="${P}-storyt"></span></div>`;
    host.innerHTML = H;
    const $ = S.$;
    // ---- ambient
    for (let i = 0; i < NS; i++) { const per = 0.9 + 1.1 * K.hash(i * 1.9 + 4), a0 = 0.25 + 0.3 * K.hash(i + 9); loop($(`${P}-st${i}`), { opacity: a0 }, { opacity: 1 }, per, t0 + 0.1 * (i % 7) - 0.0, t1); }
    loop($(`${P}-mb`), { y: -4 * u }, { y: 5 * u }, 1.6, t0, t1);
    loop($(`${P}-cl0`), { x: 0 }, { x: 0.12 * w }, Math.max(1, t1 - t0), t0, t1, "none", false);
    loop($(`${P}-cl1`), { x: 0 }, { x: -0.1 * w }, Math.max(1, t1 - t0), t0, t1, "none", false);
    loop($(`${P}-win`), { opacity: 0.75, scale: 0.94 }, { opacity: 1, scale: 1.04 }, 0.7, t0, t1);
    for (let i = 0; i < 3; i++) { const z = $(`${P}-z${i}`); I(z, { opacity: 0, x: 0, y: 0 });
      const per = 1.5, n = Math.max(1, Math.ceil((t1 - t0) / per));
      for (let k = 0; k < n; k++) { const s = t0 + i * 0.5 + k * per; if (s > t1) break;
        ft(z, { opacity: 0, x: 0, y: 0 }, { opacity: 1, x: 10 * u, y: -28 * u, duration: per * 0.45, ease: "sine.out" }, s);
        ft(z, { opacity: 1, x: 10 * u, y: -28 * u }, { opacity: 0, x: 24 * u, y: -64 * u, duration: per * 0.5, ease: "sine.in" }, s + per * 0.45); } }
    // ---- beats
    const mw = $(`${P}-mw`), tMoon = ev.moon != null ? ev.moon : t0 + 0.4;
    if (still) I(mw, { y: 0 }); else { I(mw, { y: 0.42 * h }); ft(mw, { y: 0.42 * h }, { y: 0, duration: 1.1, ease: "power2.out" }, tMoon); }
    const tSt = ev.stars != null ? ev.stars : t0 + 0.6;
    CS.forEach((_, i) => { const b = $(`${P}-bs${i}`);
      if (still) { I(b, { scale: 1, rotation: 0, opacity: 1 }); loop(b, { scale: 0.85 }, { scale: 1.12 }, 0.8 + 0.15 * i, t0, t1); }
      else { I(b, { scale: 0, rotation: -60, opacity: 1 }); ft(b, { scale: 0, rotation: -60 }, { scale: 1, rotation: 0, duration: 0.42, ease: "back.out(2.4)" }, tSt + i * 0.09);
        ft(b, { scale: 1 }, { scale: 0.86, duration: 0.7, yoyo: true, repeat: Math.max(1, Math.ceil((t1 - tSt) / 0.7)), ease: "sine.inOut" }, tSt + 0.5 + i * 0.09); } });
    [`${P}-cline`, `${P}-cline2`].forEach((id, j) => { const l = $(id); if (still) I(l, { strokeDashoffset: 0 }); else { I(l, { strokeDashoffset: 600 * u }); ft(l, { strokeDashoffset: 600 * u }, { strokeDashoffset: 0, duration: 0.7, ease: "power2.inOut" }, tSt + 0.2 + j * 0.15); } });
    const sh = $(`${P}-shoot`), tSh = ev.shoot != null ? ev.shoot : t0 + 0.9;
    I(sh, { x: 0.86 * w, y: 0.06 * h, rotation: -24, opacity: 0, scaleX: 0.3 });
    ft(sh, { x: 0.86 * w, y: 0.06 * h, opacity: 0, scaleX: 0.3 }, { x: 0.52 * w, y: 0.24 * h, opacity: 1, scaleX: 1, duration: 0.5, ease: "power1.in" }, tSh);
    ft(sh, { opacity: 1 }, { opacity: 0, duration: 0.2 }, tSh + 0.5);
    const stEl = $(`${P}-storyt`), tStory = ev.story != null ? ev.story : t0 + 0.3;
    if (still) stEl.textContent = story; else S.type(stEl, story, tStory, 26);
    return { moon: mw };
  };

  // ---------------- 2. KARTUN LUCU YANG LOMPAT-LOMPAT: sunny hills, Bolo the blob hops (squash & stretch), dust, BOING!
  K.MINI.toon = (S, host, P, o) => {
    const { w, h, t0, t1 } = o, u = h / 520, ev = o.ev || {};
    const { I, ft, loop } = S;
    let H = `<div class="m-fill" style="background:linear-gradient(180deg,#6fcdfd 0%,#b5e9ff 62%,#e1f7ff 100%)"></div>`;
    const sr = 0.2 * h, sx = 0.8 * w, sy = 0.08 * h;
    H += `<div class="m-abs" id="${P}-rays" style="left:${px(sx - sr * .55)};top:${px(sy - sr * .55)};width:${px(sr * 2.1)};height:${px(sr * 2.1)}"><svg viewBox="0 0 100 100" width="${sr * 2.1}" height="${sr * 2.1}">` +
      Array.from({ length: 12 }, (_, i) => `<path d="M50 50 L${50 + 50 * Math.cos((i * 30 - 6) * Math.PI / 180)} ${50 + 50 * Math.sin((i * 30 - 6) * Math.PI / 180)} L${50 + 50 * Math.cos((i * 30 + 6) * Math.PI / 180)} ${50 + 50 * Math.sin((i * 30 + 6) * Math.PI / 180)}Z" fill="rgba(255,230,120,.55)"/>`).join("") + `</svg></div>`;
    H += `<div class="m-abs" style="left:${px(sx)};top:${px(sy)};width:${px(sr)};height:${px(sr)};border-radius:50%;background:radial-gradient(circle at 40% 38%,#fff3a6,#ffd23f 60%,#ffb703);box-shadow:0 0 40px rgba(255,210,63,.7)"></div>`;
    const cloud = (id, x, y, s) => `<div class="m-cloud" id="${id}" style="left:${px(x)};top:${px(y)};width:${px(s * 2.2)};height:${px(s)}">` +
      `<b style="left:0;top:${px(s * .35)};width:${px(s * .9)};height:${px(s * .65)};background:#fff"></b><b style="left:${px(s * .5)};top:0;width:${px(s)};height:${px(s)};background:#fff"></b>` +
      `<b style="left:${px(s * 1.2)};top:${px(s * .3)};width:${px(s * .9)};height:${px(s * .7)};background:#fff"></b></div>`;
    H += cloud(`${P}-c0`, 0.08 * w, 0.1 * h, 0.13 * h) + cloud(`${P}-c1`, 0.48 * w, 0.2 * h, 0.09 * h);
    H += `<svg class="m-abs" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none"><ellipse cx="${w * .18}" cy="${h * 1.02}" rx="${w * .42}" ry="${h * .42}" fill="#7fdc8a"/>` +
      `<ellipse cx="${w * .86}" cy="${h * 1.05}" rx="${w * .46}" ry="${h * .44}" fill="#6ccf79"/><rect x="0" y="${h * .8}" width="${w}" height="${h * .2}" fill="#58c26a"/></svg>`;
    // flowers swaying
    const FL = [[0.12, 0.84, "#ff6b9a"], [0.24, 0.9, "#ffd23f"], [0.78, 0.86, "#ff6b9a"], [0.9, 0.9, "#ffffff"], [0.66, 0.92, "#ffd23f"]];
    FL.forEach(([a, b, c], i) => { const fs = 22 * u;
      H += `<div class="m-abs" id="${P}-fl${i}" style="left:${px(a * w)};top:${px(b * h - fs * 1.6)};width:${px(fs)};height:${px(fs * 2)};transform-origin:50% 100%"><div class="m-abs" style="left:${px(fs * .45)};top:${px(fs * .8)};width:${px(3 * u)};height:${px(fs * 1.2)};background:#2f9e4f"></div>` +
        `<div class="m-abs" style="width:${px(fs)};height:${px(fs)};border-radius:50%;background:radial-gradient(circle,#fff6c2 0 28%,${c} 30%)"></div></div>`; });
    // Bolo: wrapper (x travel) > hop (y) > squash (scale, origin bottom centre)
    const br = 0.3 * h, bx = 0.5 * w - br / 2, by = 0.8 * h - br;
    H += `<div class="m-abs" id="${P}-shadow" style="left:${px(0.5 * w - br * .42)};top:${px(0.8 * h - br * .07)};width:${px(br * .84)};height:${px(br * .16)};border-radius:50%;background:rgba(30,90,40,.35);transform-origin:50% 50%"></div>`;
    H += `<div class="m-abs" id="${P}-bw" style="left:${px(bx)};top:${px(by)};width:${px(br)};height:${px(br)}"><div class="m-abs" id="${P}-bh" style="width:${px(br)};height:${px(br)}">` +
      `<div class="m-abs" id="${P}-bq" style="width:${px(br)};height:${px(br)};transform-origin:50% 100%">` +
      `<svg viewBox="0 0 100 100" width="${br}" height="${br}" style="overflow:visible"><path d="M50 2 Q46 -10 38 -12 Q46 -2 50 2Z" fill="#3fbf5a"/><path d="M50 2 Q56 -12 66 -10 Q56 -1 50 2Z" fill="#2fa84a"/>` +
      `<ellipse cx="34" cy="98" rx="12" ry="5" fill="#b33b1e"/><ellipse cx="66" cy="98" rx="12" ry="5" fill="#b33b1e"/>` +
      `<circle cx="50" cy="52" r="47" fill="url(#${P}-bg)"/><defs><radialGradient id="${P}-bg" cx=".38" cy=".32" r=".75"><stop offset="0" stop-color="#ffb37a"/><stop offset=".6" stop-color="#ff7a45"/><stop offset="1" stop-color="#e5532b"/></radialGradient></defs>` +
      `<ellipse cx="36" cy="44" rx="11" ry="13" fill="#fff"/><ellipse cx="64" cy="44" rx="11" ry="13" fill="#fff"/><g id="${P}-pup"><circle cx="38" cy="46" r="6" fill="#1b1b3a"/><circle cx="66" cy="46" r="6" fill="#1b1b3a"/><circle cx="40" cy="43" r="2" fill="#fff"/><circle cx="68" cy="43" r="2" fill="#fff"/></g>` +
      `<g id="${P}-lid"><rect x="24" y="30" width="24" height="0" fill="#ff7a45"/></g>` +
      `<ellipse cx="24" cy="62" rx="7" ry="4.5" fill="#ff4f6d" opacity=".55"/><ellipse cx="76" cy="62" rx="7" ry="4.5" fill="#ff4f6d" opacity=".55"/><path d="M38 64 Q50 78 62 64 Q50 70 38 64Z" fill="#7a1f12"/></svg></div></div></div>`;
    for (let i = 0; i < 4; i++) H += `<div class="m-abs" id="${P}-d${i}" style="left:${px(0.5 * w - 10 * u)};top:${px(0.8 * h - 14 * u)};width:${px(20 * u)};height:${px(20 * u)};border-radius:50%;background:rgba(255,255,255,.85)"></div>`;
    const cf = 50 * u;
    H += `<div class="m-comic" id="${P}-boing" style="left:${px(0.5 * w + br * .5)};top:${px(0.18 * h)};font:700 ${px(cf)}/1 Poppins;text-shadow:0 ${px(4 * u)} 0 #e5532b,${px(3 * u)} ${px(3 * u)} 0 #1b1b3a,${px(-3 * u)} ${px(3 * u)} 0 #1b1b3a,${px(3 * u)} ${px(-3 * u)} 0 #1b1b3a,${px(-3 * u)} ${px(-3 * u)} 0 #1b1b3a">BOING!</div>`;
    host.innerHTML = H;
    const $ = S.$;
    loop($(`${P}-rays`), { rotation: 0 }, { rotation: 30 * (t1 - t0) }, Math.max(1, t1 - t0), t0, t1, "none", false);
    loop($(`${P}-c0`), { x: 0 }, { x: 0.1 * w }, Math.max(1, t1 - t0), t0, t1, "none", false);
    loop($(`${P}-c1`), { x: 0 }, { x: -0.08 * w }, Math.max(1, t1 - t0), t0, t1, "none", false);
    FL.forEach((_, i) => loop($(`${P}-fl${i}`), { rotation: -8 }, { rotation: 8 }, 0.55 + 0.1 * i, t0, t1));
    loop($(`${P}-pup`), { x: -2 }, { x: 3 }, 0.9, t0, t1);
    const bw = $(`${P}-bw`), bh = $(`${P}-bh`), bq = $(`${P}-bq`), shd = $(`${P}-shadow`);
    I(bw, { x: 0 }); I(bh, { y: 0 }); I(bq, { scaleX: 1, scaleY: 1 }); I(shd, { scale: 1, opacity: 1 });
    // hop schedule: small idle hops until ev.jump, then big hops (x travel), each: crouch → stretch up → fall → squash
    const tJ = ev.jump != null ? ev.jump : t0 + 0.6;
    const hops = []; let t = t0 + 0.05, x = 0;
    while (t < tJ - 0.5) { hops.push({ t, hgt: 0.07 * h, dur: 0.46, dx: 0 }); t += 0.5; }
    const BIG = [[0.32, 0.16], [0.36, -0.22], [0.34, 0.12], [0.3, -0.06], [0.26, 0.0]];
    t = Math.max(t, tJ - 0.08);
    for (let k = 0; t <= t1 - 0.3; k++) { const [hg, dx] = BIG[k % BIG.length]; hops.push({ t, hgt: hg * h, dur: 0.56, dx: dx * w, big: 1 }); t += 0.62; }
    hops.forEach((p, k) => {
      const c = 0.08, up = (p.dur - c) * 0.5;
      ft(bq, { scaleX: 1, scaleY: 1 }, { scaleX: 1.18, scaleY: 0.8, duration: c, ease: "power2.out" }, p.t);
      ft(bq, { scaleX: 1.18, scaleY: 0.8 }, { scaleX: 0.86, scaleY: 1.16, duration: 0.12, ease: "power2.out" }, p.t + c);
      ft(bq, { scaleX: 0.86, scaleY: 1.16 }, { scaleX: 1, scaleY: 1, duration: up, ease: "sine.out" }, p.t + c + 0.12);
      ft(bh, { y: 0 }, { y: -p.hgt, duration: up, ease: "power2.out" }, p.t + c);
      ft(bh, { y: -p.hgt }, { y: 0, duration: up, ease: "power2.in" }, p.t + c + up);
      ft(shd, { scale: 1, opacity: 1 }, { scale: 0.55, opacity: 0.5, duration: up, ease: "power2.out" }, p.t + c);
      ft(shd, { scale: 0.55, opacity: 0.5 }, { scale: 1, opacity: 1, duration: up, ease: "power2.in" }, p.t + c + up);
      if (p.dx) { ft(bw, { x }, { x: x + p.dx, duration: up * 2, ease: "sine.inOut" }, p.t + c); ft(shd, { x }, { x: x + p.dx, duration: up * 2, ease: "sine.inOut" }, p.t + c); x += p.dx; }
      const land = p.t + c + 2 * up;
      if (land < t1) ft(bq, { scaleX: 1, scaleY: 1 }, { scaleX: 1.22, scaleY: 0.78, duration: 0.06, yoyo: true, repeat: 1, ease: "power2.out" }, land);
      if (p.big) for (let i = 0; i < 4; i++) { const d = $(`${P}-d${i}`); const dir = i < 2 ? -1 : 1, sp = (i % 2 ? 0.6 : 1);
        ft(d, { x: x, y: 0, scale: 0.3, opacity: 0.9 }, { x: x + dir * (40 + 30 * sp) * u, y: -(10 + 14 * sp) * u, scale: 1.3, opacity: 0, duration: 0.45, ease: "power2.out" }, land); }
    });
    for (let i = 0; i < 4; i++) I($(`${P}-d${i}`), { opacity: 0, scale: 0.3 });
    const bo = $(`${P}-boing`); I(bo, { scale: 0, rotation: -14, opacity: 0 });
    if (o.still) { I(bo, { scale: 1, rotation: -8, opacity: 1 }); loop(bo, { scale: 0.92 }, { scale: 1.06 }, 0.45, t0, t1); }
    else { const tb = tJ + 0.25; ft(bo, { scale: 0, rotation: -14, opacity: 0 }, { scale: 1, rotation: -8, opacity: 1, duration: 0.3, ease: "back.out(3)" }, tb);
      ft(bo, { scale: 1 }, { scale: 1.08, duration: 0.2, yoyo: true, repeat: Math.max(1, Math.floor((t1 - tb - 0.3) / 0.2)), ease: "sine.inOut" }, tb + 0.3); }
  };

  // ---------------- 3. KOLAM KOI: teal water with moving caustics (morphing light lines), ripples, 4 koi swimming, lily pads + lotus
  K.koiSVG = (L, kind) => {
    // body drawn pointing right in a 100×40 box; kinds: 0 kohaku (white/red), 1 ogon (orange), 2 showa (black/red/white), 3 tancho (white + red crown)
    const base = ["#fbf6ee", "#ff8a2a", "#f4efe6", "#fbf6ee"][kind];
    const spots = [
      `<path d="M30 9 Q45 4 58 12 Q50 22 36 20Z" fill="#e8442b"/><path d="M60 22 Q72 30 80 22 Q74 32 62 30Z" fill="#e8442b"/>`,
      `<path d="M40 8 Q60 4 78 14 Q66 12 48 14Z" fill="#ffb05a" opacity=".8"/>`,
      `<path d="M28 10 Q40 3 52 10 Q44 18 30 16Z" fill="#1d1d2b"/><path d="M56 12 Q70 8 82 16 Q70 24 58 20Z" fill="#e8442b"/><path d="M50 24 Q62 30 70 26 Q60 34 48 30Z" fill="#1d1d2b"/>`,
      `<circle cx="80" cy="20" r="6" fill="#e8442b"/>`][kind];
    const body = `<svg viewBox="0 0 100 40" width="${L}" height="${L * .4}" style="position:absolute;left:0;top:0;overflow:visible"><path d="M8 20 Q14 9 40 7 Q78 5 96 20 Q78 35 40 33 Q14 31 8 20Z" fill="${base}"/>${spots}` +
      `<path d="M50 9 Q58 0 66 7Z" fill="${base}" opacity=".85"/><path d="M58 31 Q50 40 44 32Z" fill="${base}" opacity=".7"/><path d="M60 9 Q56 2 50 4" fill="none" stroke="rgba(0,0,0,.08)"/>` +
      `<circle cx="88" cy="16" r="1.8" fill="#1d1d2b"/><circle cx="88" cy="24" r="1.8" fill="#1d1d2b"/></svg>`;
    const tail = `<svg viewBox="0 0 30 40" width="${L * .3}" height="${L * .4}" style="position:absolute;left:0;top:0;overflow:visible"><path d="M30 20 Q16 8 2 2 Q8 20 2 38 Q16 32 30 20Z" fill="${kind === 1 ? "#ff9d45" : base}" opacity=".92"/>` +
      `<path d="M30 20 Q18 14 8 8" stroke="rgba(0,0,0,.08)" fill="none"/></svg>`;
    return { body, tail };
  };
  K.MINI.koi = (S, host, P, o) => {
    const { w, h, t0, t1 } = o, u = h > w ? w / 420 : Math.min(w, h * 1.85) / 960, ev = o.ev || {};
    const { I, ft, loop, tl } = S;
    let H = `<div class="m-fill" id="${P}-water" style="background:radial-gradient(ellipse 80% 70% at 50% 42%,#22b3a6 0%,#128a8f 46%,#0b5a72 100%)"></div>`;
    // pebbles on the pond floor
    for (let i = 0; i < 16; i++) { const r = (14 + 30 * K.hash(i + 40)) * u; H += `<i class="m-abs" style="left:${px(K.hash(i * 2.3 + 41) * w)};top:${px(K.hash(i * 3.7 + 42) * h)};width:${px(r)};height:${px(r * .7)};border-radius:50%;background:rgba(8,60,70,.28)"></i>`; }
    // caustics: 2 layers of wavy light lines whose path data morphs (GSAP attr tween, same command structure)
    const NL = 9, waves = (ph, amp, sp, y0) => { const out = []; for (let i = 0; i < NL; i++) { const y = y0 + i * (h / (NL - 1.5)); let d = `M${-0.1 * w} ${y.toFixed(1)}`;
      for (let k = 0; k < 6; k++) { const xa = -0.1 * w + (k + 0.5) * (1.2 * w / 6), xb = -0.1 * w + (k + 1) * (1.2 * w / 6); const a = amp * Math.sin(ph + k * 1.7 + i * 0.9) * h; d += ` Q${xa.toFixed(1)} ${(y + a).toFixed(1)} ${xb.toFixed(1)} ${(y + 0.3 * a * Math.cos(ph + i)).toFixed(1)}`; }
      out.push(d); } return out; };
    const A1 = waves(0, 0.06, 1, 0), B1 = waves(2.2, 0.07, 1, 0), A2 = waves(1.1, 0.05, 1, 0.5 * h / (NL - 1.5)), B2 = waves(3.6, 0.06, 1, 0.5 * h / (NL - 1.5));
    H += `<svg class="m-abs" id="${P}-cau" width="${w}" height="${h}" style="overflow:visible">` + A1.map((d, i) => `<path id="${P}-ca${i}" d="${d}" fill="none" stroke="rgba(220,255,250,.16)" stroke-width="${(5 * u).toFixed(1)}" stroke-linecap="round"/>`).join("") +
      A2.map((d, i) => `<path id="${P}-cb${i}" d="${d}" fill="none" stroke="rgba(200,255,245,.10)" stroke-width="${(9 * u).toFixed(1)}" stroke-linecap="round"/>`).join("") + `</svg>`;
    // fish
    const FISH = [ // [kind, length (fraction of h), cx, cy, rx, ry (fractions), turns per second, phase, dir]
      [0, 0.34, 0.5, 0.5, 0.3, 0.26, 0.085, 0.0, 1], [2, 0.28, 0.45, 0.42, 0.36, 0.3, 0.07, 2.4, -1],
      [1, 0.3, 0.55, 0.56, 0.24, 0.2, 0.1, 4.1, 1], [3, 0.24, 0.5, 0.48, 0.4, 0.33, 0.06, 1.2, -1]];
    if (h > w) { FISH.forEach((f) => { f[4] *= 0.75; f[5] *= 1.15; }); }
    FISH.forEach(([kind, len], i) => { const L = len * h * (h > w ? 0.9 : 1), sv = K.koiSVG(L, kind);
      H += `<div class="m-fish" id="${P}-f${i}" style="width:${px(L)};height:${px(L * .4)};margin:${px(-L * .2)} 0 0 ${px(-L * .5)};filter:drop-shadow(0 ${px(10 * u)} ${px(6 * u)} rgba(4,40,50,.45))">` +
        `<div class="tl" id="${P}-ft${i}" style="left:${px(-L * .2)};top:0;width:${px(L * .3)};height:${px(L * .4)}">${sv.tail}</div>${sv.body}</div>`; });
    // ripples
    const RP = [[0.2, 0.3], [0.78, 0.22], [0.66, 0.74], [0.3, 0.78], [0.88, 0.58], [0.12, 0.6]];
    RP.forEach(([a, b], i) => { const r = 120 * u; H += `<div class="m-ripple" id="${P}-r${i}" style="left:${px(a * w - r / 2)};top:${px(b * h - r / 2)};width:${px(r)};height:${px(r)};border-width:${px(2.5 * u)}"></div>`; });
    for (let i = 0; i < 3; i++) { const r = 260 * u; H += `<div class="m-ripple" id="${P}-burst${i}" style="left:${px(0.5 * w - r / 2)};top:${px(0.5 * h - r / 2)};width:${px(r)};height:${px(r)};border-width:${px(4 * u)}"></div>`; }
    // lily pads + lotus
    const PADS = [[0.14, 0.18, 0.2], [0.86, 0.8, 0.24], [0.9, 0.16, 0.15], [0.1, 0.86, 0.16], [0.68, 0.24, 0.17]];
    if (h > w) { PADS[0] = [0.2, 0.12, 0.3]; PADS[1] = [0.78, 0.88, 0.36]; PADS[2] = [0.86, 0.36, 0.2]; PADS[3] = [0.16, 0.66, 0.22]; PADS[4] = [0.7, 0.62, 0.16]; }
    PADS.forEach(([a, b, s], i) => { const r = s * (h > w ? w : Math.min(w, h * 1.85) * 0.5);
      H += `<div class="m-pad" id="${P}-p${i}" style="left:${px(a * w - r / 2)};top:${px(b * h - r / 2)};width:${px(r)};height:${px(r)};background:conic-gradient(from 20deg,transparent 0 22deg,#3fae5c 22deg 360deg);box-shadow:inset 0 0 0 ${px(3 * u)} rgba(255,255,255,.12),0 ${px(8 * u)} ${px(14 * u)} rgba(4,40,50,.35)">` +
        `<div class="m-abs" style="left:18%;top:18%;width:64%;height:64%;border-radius:50%;background:radial-gradient(circle at 40% 40%,rgba(160,240,160,.35),rgba(60,160,80,0) 70%)"></div>` +
        (i === 4 ? `<svg class="m-abs" viewBox="0 0 100 100" width="${r}" height="${r}" style="left:0;top:0;overflow:visible"><g transform="translate(50 50)">` +
          [0, 60, 120, 180, 240, 300].map((a) => `<ellipse cx="0" cy="-22" rx="11" ry="22" transform="rotate(${a})" fill="#ffb3cd"/>`).join("") +
          [30, 90, 150, 210, 270, 330].map((a) => `<ellipse cx="0" cy="-15" rx="8" ry="16" transform="rotate(${a})" fill="#ff8fb6"/>`).join("") + `<circle r="8" fill="#ffd54a"/></g></svg>` : "") + `</div>`; });
    // glints
    for (let i = 0; i < 10; i++) H += `<i class="m-abs" id="${P}-g${i}" style="left:${px(K.hash(i * 4.1 + 70) * w)};top:${px(K.hash(i * 6.3 + 71) * h)};width:${px(6 * u)};height:${px(6 * u)};border-radius:50%;background:#fff;box-shadow:0 0 ${px(10 * u)} #fff"></i>`;
    host.innerHTML = H;
    const $ = S.$;
    // ---- caustics morph (A ↔ B), whole layers drift
    A1.forEach((d, i) => loop($(`${P}-ca${i}`), { attr: { d } }, { attr: { d: B1[i] } }, 1.7 + 0.13 * (i % 3), t0, t1));
    A2.forEach((d, i) => loop($(`${P}-cb${i}`), { attr: { d } }, { attr: { d: B2[i] } }, 2.3 + 0.11 * (i % 4), t0, t1));
    loop($(`${P}-cau`), { x: -0.02 * w, y: -0.01 * h }, { x: 0.02 * w, y: 0.015 * h }, 2.6, t0, t1);
    // ---- fish: ellipse paths sampled every 0.2 s, heading from the tangent (unwrapped), tail wiggle
    const fishEls = [];
    FISH.forEach(([kind, len, cx, cy, rx, ry, tps, ph, dir], i) => {
      const f = $(`${P}-f${i}`), tail = $(`${P}-ft${i}`); fishEls.push(f);
      const pos = (t) => { const a = ph + dir * 2 * Math.PI * tps * (t - t0) + 0.35 * Math.sin(1.3 * (t - t0) + i);
        return [(cx + rx * Math.cos(a)) * w, (cy + ry * Math.sin(a) * (1 + 0.15 * Math.sin(2 * a))) * h]; };
      const dt = 0.2, N = Math.max(1, Math.ceil((t1 - t0) / dt)); let prevA = null;
      const ang = (t) => { const [x0, y0] = pos(t - 0.02), [x1, y1] = pos(t + 0.02); let a = Math.atan2(y1 - y0, x1 - x0) * 180 / Math.PI;
        if (prevA != null) { while (a - prevA > 180) a -= 360; while (a - prevA < -180) a += 360; } prevA = a; return a; };
      let [x, y] = pos(t0), r = ang(t0);
      I(f, { x, y, rotation: r });
      for (let k = 0; k < N; k++) { const ta = t0 + k * dt, tb = ta + dt; const [x2, y2] = pos(tb), r2 = ang(tb);
        ft(f, { x, y, rotation: r }, { x: x2, y: y2, rotation: r2, duration: dt, ease: "none" }, ta); x = x2; y = y2; r = r2; }
      loop(tail, { rotation: -20 }, { rotation: 20 }, 0.22 + 0.04 * i, t0, t1);
    });
    // ---- ripples, pads bob, glints
    RP.forEach((_, i) => { const r = $(`${P}-r${i}`); I(r, { scale: 0.15, opacity: 0 }); const per = 1.6, off = (i * 0.37) % per, n = Math.ceil((t1 - t0) / per) + 1;
      for (let k = 0; k < n; k++) { const s = t0 + off + (k - 1) * per; if (s + per < t0 || s > t1) continue;
        ft(r, { scale: 0.15, opacity: 0.85 }, { scale: 1.5, opacity: 0, duration: per, ease: "power1.out" }, s); } });
    PADS.forEach((_, i) => loop($(`${P}-p${i}`), { rotation: -6 + i, scale: 0.98 }, { rotation: 6 + i, scale: 1.02 }, 1.3 + 0.2 * i, t0, t1));
    for (let i = 0; i < 10; i++) loop($(`${P}-g${i}`), { opacity: 0, scale: 0.4 }, { opacity: 0.9, scale: 1 }, 0.5 + 0.3 * K.hash(i + 80), t0 + 0.07 * i, t1);
    // ---- beat: "airnya beneran gerak" → a splash burst from the centre + pads rock
    const tB = ev.burst;
    for (let i = 0; i < 3; i++) { const b = $(`${P}-burst${i}`); I(b, { scale: 0.1, opacity: 0 });
      if (tB != null) ft(b, { scale: 0.1, opacity: 1 }, { scale: 2.2, opacity: 0, duration: 1.1, ease: "power2.out" }, tB + i * 0.16); }
    return { fish: fishEls, pads: PADS.map((_, i) => $(`${P}-p${i}`)), ripples: RP.map((_, i) => $(`${P}-r${i}`)), cau: $(`${P}-cau`), water: $(`${P}-water`) };
  };

  // ---------------- 4. FILM PENDEK: letterboxed rainy night street, kid with umbrella walks to the lamp, clapperboard, subtitle
  K.MINI.film = (S, host, P, o) => {
    const { w, h, t0, t1 } = o, u = h / 520, ev = o.ev || {};
    const { I, ft, loop, tl } = S;
    let H = `<div class="m-abs" id="${P}-cam" style="width:${px(w)};height:${px(h)};transform-origin:58% 60%">`;
    H += `<div class="m-fill" style="background:linear-gradient(180deg,#0e1434 0%,#2a2a5c 50%,#5c3a62 74%,#1a1530 75%,#141026 100%)"></div>`;
    // skyline
    let sky = "", wins = []; let bx = -10;
    for (let i = 0; bx < w; i++) { const bw = (60 + 70 * K.hash(i + 200)) * u, bh = (110 + 180 * K.hash(i + 300)) * u, by = 0.75 * h - bh;
      sky += `<rect x="${bx.toFixed(1)}" y="${by.toFixed(1)}" width="${bw.toFixed(1)}" height="${bh.toFixed(1)}" fill="${i % 2 ? "#1b1a40" : "#221f4a"}"/>`;
      for (let r = 0; r < 6; r++) for (let c = 0; c < 3; c++) { if (K.hash(i * 31 + r * 7 + c) > 0.62) continue; const wx = bx + 10 * u + c * (bw - 20 * u) / 3, wy = by + 14 * u + r * 26 * u; if (wy > 0.73 * h) continue;
        wins.push([wx, wy, 9 * u, 12 * u, wins.length]); }
      bx += bw + 6 * u; }
    H += `<svg class="m-abs" width="${w}" height="${h}">${sky}${wins.map(([x, y, a, b, k]) => `<rect id="${P}-w${k}" x="${x.toFixed(1)}" y="${y.toFixed(1)}" width="${a.toFixed(1)}" height="${b.toFixed(1)}" fill="#ffcf7a" opacity="${(0.45 + 0.5 * K.hash(k + 9)).toFixed(2)}"/>`).join("")}</svg>`;
    // street + puddle reflections
    H += `<div class="m-abs" style="left:0;top:${px(0.75 * h)};width:${px(w)};height:${px(0.25 * h)};background:linear-gradient(180deg,#221c3e,#0d0a1c)"></div>`;
    for (let i = 0; i < 7; i++) H += `<i class="m-abs" id="${P}-rf${i}" style="left:${px((0.1 + 0.12 * i) * w)};top:${px((0.8 + 0.025 * (i % 3)) * h)};width:${px(70 * u)};height:${px(3 * u)};border-radius:2px;background:rgba(255,207,122,.35)"></i>`;
    // street lamp + light cone + pool
    const lx = 0.64 * w;
    H += `<div class="m-abs" style="left:${px(lx - 0.17 * w)};top:${px(0.25 * h)};width:${px(0.34 * w)};height:${px(0.52 * h)};clip-path:polygon(44% 0,56% 0,100% 100%,0 100%);background:linear-gradient(180deg,rgba(255,214,140,.5),rgba(255,214,140,.06))"></div>`;
    H += `<div class="m-abs" id="${P}-pool" style="left:${px(lx - 0.17 * w)};top:${px(0.73 * h)};width:${px(0.34 * w)};height:${px(0.08 * h)};border-radius:50%;background:radial-gradient(ellipse,rgba(255,214,140,.55),rgba(255,214,140,0) 70%)"></div>`;
    H += `<div class="m-abs" style="left:${px(lx - 4 * u)};top:${px(0.24 * h)};width:${px(8 * u)};height:${px(0.52 * h)};background:#0c0a1e"></div>`;
    H += `<div class="m-abs" style="left:${px(lx - 26 * u)};top:${px(0.2 * h)};width:${px(52 * u)};height:${px(22 * u)};border-radius:${px(10 * u)} ${px(10 * u)} ${px(4 * u)} ${px(4 * u)};background:#0c0a1e"></div>`;
    H += `<div class="m-abs" id="${P}-bulb" style="left:${px(lx - 40 * u)};top:${px(0.2 * h)};width:${px(80 * u)};height:${px(80 * u)};border-radius:50%;background:radial-gradient(circle,#fff3c8 0 14%,rgba(255,214,140,.55) 30%,rgba(255,214,140,0) 70%)"></div>`;
    // the kid with a red umbrella (walks in, legs swing; looks up at the subtitle beat)
    const kh = 0.36 * h;
    H += `<div class="m-abs" id="${P}-kid" style="left:0;top:${px(0.76 * h - kh)};width:${px(kh * .7)};height:${px(kh)}"><svg viewBox="0 0 70 100" width="${kh * .7}" height="${kh}" style="overflow:visible">` +
      `<g id="${P}-legL"><rect x="27" y="74" width="7" height="24" rx="3" fill="#2b2140"/></g><g id="${P}-legR"><rect x="37" y="74" width="7" height="24" rx="3" fill="#2b2140"/></g>` +
      `<path d="M22 46 Q35 40 48 46 L52 80 Q35 84 18 80Z" fill="#ffc83d"/><g id="${P}-head"><circle cx="35" cy="36" r="10" fill="#f2b48a"/><path d="M25 34 Q35 22 45 34 Q40 29 35 30 Q30 29 25 34Z" fill="#3a2414"/></g>` +
      `<path d="M47 50 L52 18" stroke="#2b2140" stroke-width="2.4"/><path d="M14 22 Q52 -12 90 22 Q80 16 71 22 Q62 15 52 22 Q42 15 33 22 Q24 16 14 22Z" fill="#e5484d"/></svg></div>`;
    // rain: a seamless tile of streaks, two copies, moving down
    let rs = ""; for (let i = 0; i < 70; i++) { const x = K.hash(i + 500) * (w + 0.2 * h), y = K.hash(i + 600) * h, l = (18 + 22 * K.hash(i + 700)) * u;
      rs += `<line x1="${x.toFixed(1)}" y1="${y.toFixed(1)}" x2="${(x - l * .35).toFixed(1)}" y2="${(y + l).toFixed(1)}"/>`; }
    H += `<div class="m-rain" id="${P}-rain" style="height:${px(2 * h)};top:${px(-h)}"><svg width="${w + 0.2 * h}" height="${h}" style="position:absolute;left:0;top:0" stroke="rgba(200,215,255,.42)" stroke-width="${(1.6 * u).toFixed(2)}">${rs}</svg>` +
      `<svg width="${w + 0.2 * h}" height="${h}" style="position:absolute;left:0;top:${px(h)}" stroke="rgba(200,215,255,.42)" stroke-width="${(1.6 * u).toFixed(2)}">${rs}</svg></div>`;
    H += `</div>`;
    // vignette, grain, letterbox, subtitle
    H += `<div class="m-fill" style="background:radial-gradient(ellipse 75% 70% at 55% 50%,rgba(0,0,0,0) 55%,rgba(0,0,0,.55) 100%)"></div>`;
    H += `<div class="m-fill" id="${P}-grain" style="background:url(assets/brand/grain_256.png);opacity:.12"></div>`;
    const lb = 0.12 * h;
    H += `<div class="m-abs" style="left:0;top:0;width:${px(w)};height:${px(lb)};background:#000"></div><div class="m-abs" style="left:0;top:${px(h - lb)};width:${px(w)};height:${px(lb)};background:#000"></div>`;
    const fs = 24 * u;
    H += `<div class="m-sub" id="${P}-sub" style="top:${px(h - lb + (lb - fs * 1.4) / 2)};font:400 ${px(fs)}/${px(fs * 1.4)} Poppins">“Besok, aku coba lagi.”</div>`;
    H += `<div class="m-abs" id="${P}-title" style="left:0;top:${px((lb - 18 * u) / 2)};width:${px(w)};text-align:center;font:700 ${px(15 * u)}/${px(18 * u)} Poppins;letter-spacing:${px(5 * u)};color:rgba(255,255,255,.7)">BAB 1 · HUJAN</div>`;
    // clapperboard (snaps on "film")
    const cw = 230 * u;
    H += `<div class="m-abs" id="${P}-clap" style="left:${px(0.5 * w - cw / 2)};top:${px(0.5 * h - cw * .42)};width:${px(cw)};height:${px(cw * .84)}"><div class="m-abs" style="top:${px(cw * .2)};width:${px(cw)};height:${px(cw * .64)};border-radius:${px(8 * u)};background:#16162a;box-shadow:0 ${px(12 * u)} ${px(26 * u)} rgba(0,0,0,.5)">` +
      `<div style="position:absolute;left:${px(14 * u)};top:${px(14 * u)};font:700 ${px(20 * u)}/1.3 Poppins;color:#fff;white-space:nowrap">ADEGAN 1<br><span style="font-weight:400;color:#c9d3f0">TAKE 1 · REELS</span></div></div>` +
      `<div class="m-abs" id="${P}-arm" style="top:${px(cw * .08)};width:${px(cw)};height:${px(cw * .13)};border-radius:${px(5 * u)};transform-origin:0% 100%;background:repeating-linear-gradient(120deg,#fff 0 ${px(18 * u)},#16162a ${px(18 * u)} ${px(36 * u)})"></div></div>`;
    host.innerHTML = H;
    const $ = S.$;
    loop($(`${P}-rain`), { y: 0 }, { y: h }, 0.55, t0, t1, "none", false);
    loop($(`${P}-cam`), { scale: 1 }, { scale: 1.07 }, Math.max(1, t1 - t0), t0, t1, "sine.inOut", false);
    loop($(`${P}-bulb`), { opacity: 0.85 }, { opacity: 1 }, 0.25, t0, t1);
    loop($(`${P}-grain`), { x: 0, y: 0 }, { x: 64, y: 40 }, Math.max(1, t1 - t0), t0, t1, `steps(${Math.max(2, Math.round((t1 - t0) * 15))})`, false);
    for (let i = 0; i < 7; i++) loop($(`${P}-rf${i}`), { opacity: 0.2, scaleX: 0.8 }, { opacity: 0.6, scaleX: 1.15 }, 0.4 + 0.1 * i, t0, t1);
    wins.forEach(([, , , , k]) => { if (k % 9 === 3) loop($(`${P}-w${k}`), { opacity: 0.2 }, { opacity: 0.9 }, 0.35 + 0.1 * (k % 4), t0, t1, "steps(1)"); });
    const kid = $(`${P}-kid`), x0 = 0.3 * w - kh * .35, x1 = 0.55 * w - kh * .35, tStop = Math.min(t1, t0 + (o.walk || 1.6));
    if (o.still) I(kid, { x: x1 }); else { I(kid, { x: x0 }); ft(kid, { x: x0 }, { x: x1, duration: tStop - t0, ease: "sine.out" }, t0); }
    if (!o.still) { const n = Math.max(1, Math.round((tStop - t0) / 0.3)); loop($(`${P}-legL`), { rotation: -14, transformOrigin: "50% 0%" }, { rotation: 14 }, (tStop - t0) / n, t0, tStop);
      loop($(`${P}-legR`), { rotation: 14, transformOrigin: "50% 0%" }, { rotation: -14 }, (tStop - t0) / n, t0, tStop); }
    const hd = $(`${P}-head`); I(hd, { rotation: 0, transformOrigin: "50% 80%" });
    const sub = $(`${P}-sub`), tSub = ev.sub;
    if (o.still) I(sub, { opacity: 1 }); else { I(sub, { opacity: 0, y: 6 }); if (tSub != null) { ft(sub, { opacity: 0, y: 6 }, { opacity: 1, y: 0, duration: 0.3, ease: "power2.out" }, tSub); ft(hd, { rotation: 0 }, { rotation: -14, duration: 0.4, ease: "power2.out" }, tSub - 0.1); } }
    const clap = $(`${P}-clap`), arm = $(`${P}-arm`);
    if (ev.clap == null) I(clap, { opacity: 0 });
    else { const tc = ev.clap; I(clap, { opacity: 1, scale: 0.6, rotation: -6 }); I(arm, { rotation: -26 });
      ft(clap, { scale: 0.6, rotation: -6 }, { scale: 1, rotation: 0, duration: 0.22, ease: "back.out(2)" }, t0);
      ft(arm, { rotation: -26 }, { rotation: 0, duration: 0.09, ease: "power3.in" }, tc - 0.09);
      ft(clap, { scale: 1, opacity: 1, y: 0 }, { scale: 0.7, opacity: 0, y: -30 * u, duration: 0.24, ease: "power2.in" }, tc + 0.22); }
    const ti = $(`${P}-title`); I(ti, { opacity: o.still ? 1 : 0 }); if (!o.still) ft(ti, { opacity: 0 }, { opacity: 1, duration: 0.4 }, (ev.clap || t0) + 0.3);
  };
})();

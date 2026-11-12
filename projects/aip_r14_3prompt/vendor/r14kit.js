// Shared visual system of R14 "3 prompt buat ngedit reels pakai Claude Code" (LIGHT), loaded in <head> before every scene.
// Our own design: the PROMPT CARD (big, copyable: number, title, the real prompt text in a well, "Salin" button), its collapsed
// STRIP (top of the hero zone while the prompt's demo plays), the cursor, and the scene boilerplate. Icons: lucide-static 1.70.0
// (ISC, inlined so they take currentColor). Claude mark: assets/icons/lobe-claude-color.svg (lobehub, MIT).
// - R14.svg(k, sw)          : lucide icon
// - R14.P[i]                : the three prompts (on-screen short form; the full DM version is production/TIGA_PROMPT.md)
// - R14.card(p, i)          : big prompt card 940×560 at (70, 330); ids p-card · p-num · p-tt · p-ln{k} (text lines) · p-lm{k} (line
//                             masks) · p-btn (Salin) · p-ok (Tersalin) · p-cc (Claude Code target chip)
// - R14.strip(p, i)         : collapsed card 940×76 at (70, 306); ids p-strip · p-sst (status chip)
// - R14.cursor(p)           : pointer; id p-cur (place with x/y)
// - R14.scene(ID)           : { ST, D, L, tl, ft, I, $, done } — the timeline boilerplate every scene uses
(function () {
  const ICO = {
    folder: "<path d=\"M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z\" />",
    folderOpen: "<path d=\"m6 14 1.5-2.9A2 2 0 0 1 9.24 10H20a2 2 0 0 1 1.94 2.5l-1.54 6a2 2 0 0 1-1.95 1.5H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h3.9a2 2 0 0 1 1.69.9l.81 1.2a2 2 0 0 0 1.67.9H18a2 2 0 0 1 2 2v2\" />",
    download: "<path d=\"M12 15V3\" /><path d=\"M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4\" /><path d=\"m7 10 5 5 5-5\" />",
    audio: "<path d=\"M2 10v3\" /><path d=\"M6 6v11\" /><path d=\"M10 3v18\" /><path d=\"M14 8v7\" /><path d=\"M18 5v13\" /><path d=\"M22 10v3\" />",
    scissors: "<circle cx=\"6\" cy=\"6\" r=\"3\" /><path d=\"M8.12 8.12 12 12\" /><path d=\"M20 4 8.12 15.88\" /><circle cx=\"6\" cy=\"18\" r=\"3\" /><path d=\"M14.8 14.8 20 20\" />",
    clap: "<path d=\"m12.296 3.464 3.02 3.956\" /><path d=\"M20.2 6 3 11l-.9-2.4c-.3-1.1.3-2.2 1.3-2.5l13.5-4c1.1-.3 2.2.3 2.5 1.3z\" /><path d=\"M3 11h18v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z\" /><path d=\"m6.18 5.276 3.1 3.899\" />",
    sparkles: "<path d=\"M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z\" /><path d=\"M20 2v4\" /><path d=\"M22 4h-4\" /><circle cx=\"4\" cy=\"20\" r=\"2\" />",
    bookmark: "<path d=\"M17 3a2 2 0 0 1 2 2v15a1 1 0 0 1-1.496.868l-4.512-2.578a2 2 0 0 0-1.984 0l-4.512 2.578A1 1 0 0 1 5 20V5a2 2 0 0 1 2-2z\" />",
    bookmarkCheck: "<path d=\"M17 3a2 2 0 0 1 2 2v15a1 1 0 0 1-1.496.868l-4.512-2.578a2 2 0 0 0-1.984 0l-4.512 2.578A1 1 0 0 1 5 20V5a2 2 0 0 1 2-2z\" /><path d=\"m9 10 2 2 4-4\" />",
    copy: "<rect width=\"14\" height=\"14\" x=\"8\" y=\"8\" rx=\"2\" ry=\"2\" /><path d=\"M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2\" />",
    check: "<path d=\"M20 6 9 17l-5-5\" />",
    circleCheck: "<circle cx=\"12\" cy=\"12\" r=\"10\" /><path d=\"m16 9-5.5 5.5L8 12\" />",
    send: "<path d=\"M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z\" /><path d=\"m21.854 2.147-10.94 10.939\" />",
    heart: "<path d=\"M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5\" />",
    msg: "<path d=\"M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719\" />",
    user: "<path d=\"M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2\" /><circle cx=\"12\" cy=\"7\" r=\"4\" />",
    ban: "<circle cx=\"12\" cy=\"12\" r=\"10\" /><path d=\"M4.929 4.929 19.07 19.071\" />",
    upload: "<path d=\"M12 3v12\" /><path d=\"m17 8-5-5-5 5\" /><path d=\"M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4\" />",
    refresh: "<path d=\"M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8\" /><path d=\"M21 3v5h-5\" /><path d=\"M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16\" /><path d=\"M8 16H3v5\" />",
    arrow: "<path d=\"M5 12h14\" /><path d=\"m12 5 7 7-7 7\" />",
    up: "<path d=\"m5 12 7-7 7 7\" /><path d=\"M12 19V5\" />",
    sliders: "<path d=\"M10 8h4\" /><path d=\"M12 21v-9\" /><path d=\"M12 8V3\" /><path d=\"M17 16h4\" /><path d=\"M19 12V3\" /><path d=\"M19 21v-5\" /><path d=\"M3 14h4\" /><path d=\"M5 10V3\" /><path d=\"M5 21v-7\" />",
    captions: "<rect width=\"18\" height=\"14\" x=\"3\" y=\"5\" rx=\"2\" ry=\"2\" /><path d=\"M7 15h4M15 15h2M7 11h2M13 11h4\" />",
    wand: "<path d=\"m21.64 3.64-1.28-1.28a1.21 1.21 0 0 0-1.72 0L2.36 18.64a1.21 1.21 0 0 0 0 1.72l1.28 1.28a1.2 1.2 0 0 0 1.72 0L21.64 5.36a1.2 1.2 0 0 0 0-1.72\" /><path d=\"m14 7 3 3\" /><path d=\"M5 6v4\" /><path d=\"M19 14v4\" /><path d=\"M10 2v2\" /><path d=\"M7 8H3\" /><path d=\"M21 16h-4\" /><path d=\"M11 3H9\" />",
    file: "<path d=\"M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z\" /><path d=\"M14 2v5a1 1 0 0 0 1 1h5\" /><path d=\"M10 9H8\" /><path d=\"M16 13H8\" /><path d=\"M16 17H8\" />",
    lock: "<rect width=\"18\" height=\"11\" x=\"3\" y=\"11\" rx=\"2\" ry=\"2\" /><path d=\"M7 11V7a5 5 0 0 1 10 0v4\" />",
    play: "<path d=\"M5 5a2 2 0 0 1 3.008-1.728l11.997 6.998a2 2 0 0 1 .003 3.458l-12 7A2 2 0 0 1 5 19z\" />",
    terminal: "<path d=\"M12 19h8\" /><path d=\"m4 17 6-6-6-6\" />",
    shield: "<path d=\"M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z\" /><path d=\"m9 12 2 2 4-4\" />",
    film: "<rect width=\"18\" height=\"18\" x=\"3\" y=\"3\" rx=\"2\" /><path d=\"M7 3v18\" /><path d=\"M3 7.5h4\" /><path d=\"M3 12h18\" /><path d=\"M3 16.5h4\" /><path d=\"M17 3v18\" /><path d=\"M17 7.5h4\" /><path d=\"M17 16.5h4\" />",
    mic: "<path d=\"M12 19v3\" /><path d=\"M19 10v2a7 7 0 0 1-14 0v-2\" /><rect x=\"9\" y=\"2\" width=\"6\" height=\"13\" rx=\"3\" />",
    route: "<circle cx=\"6\" cy=\"19\" r=\"3\" /><path d=\"M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15\" /><circle cx=\"18\" cy=\"5\" r=\"3\" />",
    pointer: "<path d=\"M4.037 4.688a.495.495 0 0 1 .651-.651l16 6.5a.5.5 0 0 1-.063.947l-6.124 1.58a2 2 0 0 0-1.438 1.435l-1.579 6.126a.5.5 0 0 1-.947.063z\" />",
    clock: "<circle cx=\"12\" cy=\"12\" r=\"10\" /><path d=\"M12 6v6h4\" />",
    workflow: "<rect width=\"8\" height=\"8\" x=\"3\" y=\"3\" rx=\"2\" /><path d=\"M7 11v4a2 2 0 0 0 2 2h4\" /><rect width=\"8\" height=\"8\" x=\"13\" y=\"13\" rx=\"2\" />",
    type: "<path d=\"M12 4v16\" /><path d=\"M4 7V5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2\" /><path d=\"M9 20h6\" />",
    layers: "<path d=\"M13 13.74a2 2 0 0 1-2 0L2.5 8.87a1 1 0 0 1 0-1.74L11 2.26a2 2 0 0 1 2 0l8.5 4.87a1 1 0 0 1 0 1.74z\" /><path d=\"m20 14.285 1.5.845a1 1 0 0 1 0 1.74L13 21.74a2 2 0 0 1-2 0l-8.5-4.87a1 1 0 0 1 0-1.74l1.5-.845\" />",
    hand: "<path d=\"M18 11V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2\" /><path d=\"M14 10V4a2 2 0 0 0-2-2a2 2 0 0 0-2 2v2\" /><path d=\"M10 10.5V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2v8\" /><path d=\"M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15\" />",
    plus: "<path d=\"M5 12h14\" /><path d=\"M12 5v14\" />",
    x: "<path d=\"M18 6 6 18\" /><path d=\"m6 6 12 12\" />",
    listChecks: "<path d=\"M13 5h8\" /><path d=\"M13 12h8\" /><path d=\"M13 19h8\" /><path d=\"m3 17 2 2 4-4\" /><path d=\"m3 7 2 2 4-4\" />"
  };
  const svg = (k, sw, cls) => `<svg class="${cls || ""}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[k]}</svg>`;
  const CL = `<i class="r14-cl"></i>`;   // Claude mark
  // the three prompts — on-screen short form (real, usable). Lines are pre-broken (measured: every line fits the 860 px well at 28 px).
  // <b> = the words that matter (tools, files). Full versions with notes: production/TIGA_PROMPT.md
  const P = [
    { n: 1, title: "Siapin alat", sub: "folder + 5 alat", ic: "folder",
      lines: ["Bikin folder <b>studio-reels</b> isi 3 folder:", "<b>rekaman</b>, <b>inspirasi</b>, <b>final</b>. Terus pasang", "<b>Remotion</b>, <b>HyperFrames</b>, <b>FFmpeg</b>, <b>Whisper</b>,",
              "<b>yt-dlp</b>. Jelasin tiap perintah sebelum", "kamu jalanin, lalu tes semuanya jalan."] },
    { n: 2, title: "Bikin selera", sub: "selera.md dari reels favorit", ic: "sliders",
      lines: ["Di folder <b>inspirasi</b> ada reels favoritku.", "Pecah jadi <b>frame + transkrip</b>, lalu tulis", "<b>selera.md</b>: tempo potongan, gaya caption,",
              "warna, font, 3 detik pembuka.", "Ambil <b>polanya</b> aja, jangan tiru isinya."] },
    { n: 3, title: "Edit", sub: "potong, caption, revisi", ic: "scissors",
      lines: ["Edit video di folder <b>rekaman</b> pakai", "<b>selera.md</b>: potong jeda & kata yang diulang,", "<b>caption per kata</b> dari Whisper, animasi di",
              "poin penting. Render <b>1080×1920</b> ke <b>final</b>,", "lalu tulis apa aja yang kamu ubah."] },
  ];
  const card = (p, i) => {
    const q = P[i];
    return `<div class="r14-card" id="${p}-card"><div class="cb"></div>` +
      `<div class="num" id="${p}-num">${q.n}</div><span class="lab">PROMPT ${q.n} DARI 3</span><b class="tt r14-grad" id="${p}-tt">${q.title}</b>` +
      `<div class="cc" id="${p}-cc">${CL}<span>buat Claude Code</span></div>` +
      `<div class="well"><div class="wq">“</div>` + q.lines.map((l, k) => `<div class="ln" id="${p}-ln${k}" style="top:${26 + k * 46}px">${l}<i class="lm" id="${p}-lm${k}"></i></div>`).join("") + `</div>` +
      `<div class="hint">${svg("terminal", 2.2)}<span>salin → tempel ke Claude Code</span></div>` +
      `<div class="btn" id="${p}-btn">${svg("copy", 2.2)}<b>Salin</b></div>` +
      `<div class="btn ok" id="${p}-ok">${svg("check", 3)}<b>Tersalin</b></div></div>`;
  };
  const strip = (p, i, st) => {
    const q = P[i];
    return `<div class="r14-strip" id="${p}-strip"><div class="num">${q.n}</div><span class="lab">PROMPT ${q.n}</span><b class="tt r14-grad">${q.title}</b>` +
      `<div class="sst" id="${p}-sst">${CL}<span>${st || "dikerjain Claude"}</span></div></div>`;
  };
  const cursor = (p) => `<div class="r14-cur" id="${p}-cur"><svg viewBox="0 0 24 24"><path d="M4.037 4.688a.495.495 0 0 1 .651-.651l16 6.5a.5.5 0 0 1-.063.947l-6.124 1.58a2 2 0 0 0-1.438 1.435l-1.579 6.126a.5.5 0 0 1-.947.063z" fill="#0a0d2c" stroke="#ffffff" stroke-width="1.6" stroke-linejoin="round"/></svg></div>`;
  // scene boilerplate: word lookup (scene-local seconds), timeline with the seek-safe "scale" shorthand, pinned initial states
  const scene = (ID) => {
    const ST = window.SCN[ID][0], D = window.SCN[ID][1], VW = window.VO_WORDS;
    const L = (txt, after = 0) => { const w = VW.find((x) => x[0] === txt && x[1] >= ST + after - 0.05); return w ? w[1] - ST : 0; };
    const $ = (id) => document.getElementById(id);
    const tl = gsap.timeline({ paused: true });
    const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
    { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); tl.set = (a, v, p) => s0(a, _sc(v), p); tl.fromTo = (a, x, y, p) => f0(a, _sc(x), _sc(y), p); tl.to = (a, v, p) => t0(a, _sc(v), p); }
    const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), t);
    const I = (el, v) => { gsap.set(el, _sc(v)); tl.set(el, v, 0); };
    const done = () => {
      tl.set({}, {}, D - 0.01);
      (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
      window.__timelines = window.__timelines || {};
      window.__timelines[ID] = tl;
    };
    return { ST, D, L, tl, ft, I, $, done };
  };
  // card helpers: deal in (from the deck, lower right), reveal the lines, cursor click on Salin, collapse into the strip
  const cardIn = (S, p, t) => {
    const { ft, I, $ } = S, c = $(p + "-card");
    I(c, { opacity: 0, x: 260, y: 120, rotation: 9, scale: 0.72 });
    ft(c, { opacity: 0, x: 260, y: 120, rotation: 9, scale: 0.72 }, { opacity: 1, x: 0, y: 0, rotation: 0, scale: 1, duration: 0.5, ease: "back.out(1.3)" }, t);
    I($(p + "-num"), { scale: 0.4 }); ft($(p + "-num"), { scale: 0.4 }, { scale: 1, duration: 0.4, ease: "back.out(3)" }, t + 0.18);
    I($(p + "-cc"), { opacity: 0, x: 20 }); ft($(p + "-cc"), { opacity: 0, x: 20 }, { opacity: 1, x: 0, duration: 0.3, ease: "power2.out" }, t + 0.4);
    for (let k = 0; k < 5; k++) { const m = $(p + "-lm" + k); I(m, { scaleX: 1 }); ft(m, { scaleX: 1 }, { scaleX: 0, duration: 0.26, ease: "power1.inOut" }, t + 0.36 + k * 0.1); }
    I($(p + "-ok"), { opacity: 0, scale: 0.8 });
  };
  const cardCopy = (S, p, t) => {   // cursor glides in, clicks Salin at t
    const { ft, I, $ } = S, cur = $(p + "-cur"), btn = $(p + "-btn"), ok = $(p + "-ok");
    I(cur, { opacity: 0, x: 700, y: 980 });
    ft(cur, { opacity: 0, x: 700, y: 980 }, { opacity: 1, x: 905, y: 842, duration: 0.42, ease: "power2.out" }, t - 0.48);
    ft(cur, { scale: 1 }, { scale: 0.8, duration: 0.08, yoyo: true, repeat: 1, ease: "power2.out" }, t - 0.04);
    ft(btn, { scale: 1 }, { scale: 0.92, duration: 0.08, yoyo: true, repeat: 1, ease: "power2.out" }, t - 0.04);
    ft(btn, { opacity: 1 }, { opacity: 0, duration: 0.12 }, t + 0.06);
    ft(ok, { opacity: 0, scale: 0.8 }, { opacity: 1, scale: 1, duration: 0.26, ease: "back.out(2.5)" }, t + 0.06);
    ft(cur, { opacity: 1 }, { opacity: 0, duration: 0.2 }, t + 0.45);
  };
  const cardOut = (S, p, t) => {   // the card folds up into the strip
    const { ft, I, $ } = S, c = $(p + "-card"), s = $(p + "-strip");
    ft(c, { opacity: 1, y: 0, scale: 1 }, { opacity: 0, y: -250, scale: 0.55, duration: 0.36, ease: "power2.in" }, t);
    I(s, { opacity: 0, y: 30, scaleX: 0.86 });
    ft(s, { opacity: 0, y: 30, scaleX: 0.86 }, { opacity: 1, y: 0, scaleX: 1, duration: 0.36, ease: "back.out(1.6)" }, t + 0.22);
    I($(p + "-sst"), { opacity: 0, x: 16 });
    ft($(p + "-sst"), { opacity: 0, x: 16 }, { opacity: 1, x: 0, duration: 0.28, ease: "power2.out" }, t + 0.5);
  };
  const css = `
  .r14-grad { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .r14-cl { display: block; background: url(assets/icons/lobe-claude-color.svg) center / contain no-repeat; }
  .r14-card { position: absolute; left: 70px; top: 330px; width: 940px; height: 560px; transform-origin: 50% 50%; font-family: Poppins, sans-serif; }
  .r14-card .cb { position: absolute; inset: 0; border-radius: 34px; background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 56px 90px -42px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); }
  .r14-card .num { position: absolute; left: 32px; top: 30px; width: 88px; height: 88px; border-radius: 26px; background: linear-gradient(150deg, #294b77, #0a0d2c); color: #ffffff;
    font: 700 50px/88px Poppins, sans-serif; text-align: center; box-shadow: 0 16px 26px -14px rgba(10,13,44,.8); transform-origin: 50% 50%; }
  .r14-card .lab { position: absolute; left: 142px; top: 34px; font: 700 17px/24px Poppins, sans-serif; letter-spacing: .16em; color: #5d6f8f; white-space: nowrap; }
  .r14-card .tt { position: absolute; left: 140px; top: 58px; font: 700 50px/62px Poppins, sans-serif; letter-spacing: -.01em; white-space: nowrap; }
  .r14-card .cc { position: absolute; right: 30px; top: 40px; height: 48px; padding: 0 18px 0 52px; border-radius: 24px; background: #fff4ee; box-shadow: inset 0 0 0 1.5px #f3d9cc; white-space: nowrap; }
  .r14-card .cc .r14-cl { position: absolute; left: 14px; top: 11px; width: 26px; height: 26px; }
  .r14-card .cc span { font: 700 17px/48px Poppins, sans-serif; color: #7a3d1f; }
  .r14-card .well { position: absolute; left: 32px; top: 146px; width: 876px; height: 284px; border-radius: 24px; background: #f2f5fb; box-shadow: inset 0 0 0 2px #dfe7f3; overflow: hidden; }
  .r14-card .wq { position: absolute; right: 22px; top: -16px; font: 700 120px/1 Poppins, sans-serif; color: rgba(41,75,119,.10); }
  .r14-card .ln { position: absolute; left: 30px; font: 400 28px/40px Poppins, sans-serif; color: #294b77; white-space: nowrap; }
  .r14-card .ln b { font-weight: 700; color: #0a0d2c; }
  .r14-card .lm { position: absolute; left: -6px; right: -8px; top: 0; bottom: -4px; background: #f2f5fb; transform-origin: 100% 50%; }
  .r14-card .hint { position: absolute; left: 34px; top: 470px; height: 60px; display: flex; align-items: center; gap: 10px; color: #5d6f8f; white-space: nowrap; }
  .r14-card .hint svg { width: 24px; height: 24px; display: block; }
  .r14-card .hint span { font: 400 20px/60px Poppins, sans-serif; }
  .r14-card .btn { position: absolute; right: 32px; top: 462px; width: 214px; height: 68px; border-radius: 34px; background: linear-gradient(150deg, #294b77, #0a0d2c); color: #ffffff;
    display: flex; align-items: center; justify-content: center; gap: 12px; box-shadow: 0 16px 26px -14px rgba(10,13,44,.85); transform-origin: 50% 50%; }
  .r14-card .btn svg { width: 26px; height: 26px; display: block; }
  .r14-card .btn b { font: 700 24px/68px Poppins, sans-serif; }
  .r14-card .btn.ok { background: linear-gradient(150deg, #2fb35a, #1a7434); box-shadow: 0 16px 26px -14px rgba(26,116,52,.8); }
  .r14-strip { position: absolute; left: 70px; top: 306px; width: 940px; height: 76px; border-radius: 26px; background: linear-gradient(180deg, #ffffff, #f6f8fd); transform-origin: 50% 0%;
    box-shadow: 0 22px 40px -26px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); font-family: Poppins, sans-serif; }
  .r14-strip .num { position: absolute; left: 12px; top: 10px; width: 56px; height: 56px; border-radius: 18px; background: linear-gradient(150deg, #294b77, #0a0d2c); color: #fff; font: 700 30px/56px Poppins, sans-serif; text-align: center; }
  .r14-strip .lab { position: absolute; left: 86px; top: 10px; font: 700 14px/20px Poppins, sans-serif; letter-spacing: .16em; color: #5d6f8f; white-space: nowrap; }
  .r14-strip .tt { position: absolute; left: 85px; top: 28px; font: 700 30px/40px Poppins, sans-serif; white-space: nowrap; }
  .r14-strip .sst { position: absolute; right: 14px; top: 14px; height: 48px; padding: 0 18px 0 50px; border-radius: 24px; background: #fff4ee; box-shadow: inset 0 0 0 1.5px #f3d9cc; white-space: nowrap; }
  .r14-strip .sst .r14-cl { position: absolute; left: 13px; top: 11px; width: 26px; height: 26px; }
  .r14-strip .sst span { font: 700 17px/48px Poppins, sans-serif; color: #7a3d1f; }
  .r14-cur { position: absolute; left: 0; top: 0; width: 46px; height: 46px; transform-origin: 20% 20%; filter: drop-shadow(0 8px 10px rgba(10,13,44,.35)); }
  .r14-cur svg { width: 46px; height: 46px; display: block; }
  `;
  const st = document.createElement("style"); st.textContent = css; (document.head || document.documentElement).appendChild(st);
  window.R14 = { ICO, svg, CL, P, card, strip, cursor, scene, cardIn, cardCopy, cardOut };
})();

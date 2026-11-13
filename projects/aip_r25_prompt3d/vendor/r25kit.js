// R25 SITUS (bedah prompt website 3D) — shared scene kit (loaded in index.html <head> after vo_words.js + r25icons.js; every scene
// uses window.R25K). Boilerplate adapted from the R19 kit: timeline wrapper with every initial state pinned at 0 in a NESTED timeline
// that is the first child of the scene timeline (I), ft (fromTo, immediateRender:false), wt (scene-local word time), per-letter typing,
// finish() = end marker + backward-seek patch + tl.render(0, true, true) + registration. Topic header (s03).
// R25 components (identical wherever they appear, so scenes hand them over at the same position):
//   PROMPT CARD  (x 60, y 330, 600 x 600): white "prompt-website-3d.txt" card whose five parts are rows (number disc, label, text).
//   PHONE        (x 700, y 330, 320 x 600): our own example 3D landing page (toko parfum lokal, CONTOH), built layer by layer:
//                blank -> objek (amber glass bottle, floating) -> suasana (teal background, warm light, shadow) -> gerakan (scroll,
//                spin, closer) -> isi halaman (headline, products, testimonial, WhatsApp button) -> teknis (sheet: 1 file HTML,
//                Three.js, ringan di HP).
// Deterministic: no Math.random, no Date, no rAF.
(function () {
  const K = (window.R25K = {});
  const ICO = window.R25_ICO || {};
  K.svg = (n, cls = "", extra = "") =>
    `<svg class="${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ${extra}>${ICO[n] || ""}</svg>`;

  // ------------------------------------------------------------------ content (our own example prompt, CONTOH)
  K.ROWS = [
    { lab: "Objek utama", txt: "botol parfum kaca warna amber, tutup hitam, melayang pelan di tengah layar" },
    { lab: "Suasana", txt: "latar hijau toska gelap, cahaya hangat dari kiri atas, bayangan lembut di bawah botol" },
    { lab: "Gerakan", txt: "saat di-scroll, botol berputar 360° dan makin dekat ke kamera" },
    { lab: "Isi halaman", txt: "judul besar, 3 produk, testimoni pembeli, tombol pesan via WhatsApp" },
    { lab: "Teknis", txt: "1 file HTML, Three.js + GSAP ScrollTrigger dari CDN, ringan di HP, versi gambar biasa kalau HP lemah" },
  ];
  K.CARD = { x: 60, y: 330, w: 600, h: 600 };
  K.PHONE = { x: 700, y: 330, w: 320, h: 600 };
  // accordion geometry (card-local): rows start at 72, collapsed 64 tall, gap 10, the active row 216 tall
  K.ROW0 = 72; K.RH = 64; K.RG = 10; K.RX = 216;
  K.rowTops = (k) => K.ROWS.map((_, i) => (k < 0 || i <= k ? K.ROW0 + i * (K.RH + K.RG) : K.ROW0 + k * (K.RH + K.RG) + K.RX + K.RG + (i - k - 1) * (K.RH + K.RG)));
  K.rowH = (k, i) => (i === k ? K.RX : K.RH);
  // the uncut "wall of text" (s01, frame 0): five 100-px paragraphs
  K.WALL0 = 72; K.WALLH = 100;

  // ------------------------------------------------------------------ topic header (s03)
  K.HD = [{ tile: "coins", name: "Harga jasa", sub: "hitung dalam rupiah &middot; <i>tanpa janji cuan</i>", chip: "JUJUR", chipIc: "shield-check" }];
  K.NSEG = 0;
  K.SEG = (k) => ({ x: 768 + (k - 1) * 29, y: 342 });

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
  /* ---------------- PROMPT CARD */
  .k-card{position:absolute;left:0;top:0;width:600px;height:600px;border-radius:28px;background:linear-gradient(180deg,#ffffff,#f4f7fc);
    box-shadow:0 26px 56px rgba(2,6,26,.55);overflow:hidden;transform-origin:50% 50%}
  .k-card .ttl{position:absolute;left:0;top:0;width:600px;height:58px;border-bottom:1.5px solid #e2e8f3}
  .k-card .ttl .fi{position:absolute;left:16px;top:12px;width:34px;height:34px;border-radius:10px;background:linear-gradient(160deg,#9cecff,#01ccf7 55%,#0aa7d6);color:#0b1440}
  .k-card .ttl .fi svg{position:absolute;left:7px;top:7px;width:20px;height:20px}
  .k-card .ttl b{position:absolute;left:62px;top:0;font:700 21px/58px Poppins;color:#0a0d2c;white-space:nowrap}
  .k-card .ttl .k-demo{right:16px;top:14px}
  .k-row{position:absolute;left:16px;top:0;width:568px;height:64px;border-radius:16px;overflow:hidden}
  .k-row .bp{position:absolute;inset:0;border-radius:16px;background:#f2f5fa;box-shadow:inset 0 0 0 1.5px #e1e8f2}
  .k-card .ft{position:absolute;left:0;top:452px;width:600px;text-align:center}
  .k-card .ft b{display:block;font:700 50px/62px Poppins;color:#0a0d2c;letter-spacing:-1px}
  .k-card .ft b em{font-style:normal;color:#01a9d6}
  .k-card .ft span{display:block;font:400 21px/32px Poppins;color:#5d6f8f}
  .k-card .cg{position:absolute;inset:0;border-radius:28px;box-shadow:inset 0 0 0 3px #01ccf7,inset 0 0 26px rgba(1,204,247,.35);opacity:0}
  .k-row .hi{position:absolute;inset:0;border-radius:16px;background:#ffffff;box-shadow:inset 0 0 0 2.5px #01ccf7,0 10px 26px rgba(1,150,200,.18);opacity:0}
  .k-row .dc{position:absolute;left:12px;top:12px;width:40px;height:40px;border-radius:20px;background:#ffffff;box-shadow:inset 0 0 0 2px #c9d5e8;
    font:700 20px/40px Poppins;color:#5d6f8f;text-align:center}
  .k-row .dc .on{position:absolute;inset:0;border-radius:20px;background:linear-gradient(160deg,#9cecff,#01ccf7 55%,#0aa7d6);color:#0b1440;opacity:0}
  .k-row .dc .ok{position:absolute;inset:0;border-radius:20px;background:#2da44e;color:#fff;opacity:0}
  .k-row .dc .ok svg{position:absolute;left:9px;top:9px;width:22px;height:22px}
  .k-row .lb{position:absolute;left:66px;top:12px;font:700 22px/40px Poppins;color:#0a0d2c;white-space:nowrap}
  .k-row .pv{position:absolute;left:228px;top:12px;width:326px;font:400 17px/40px Poppins;color:#8a99b3;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .k-row .tx{position:absolute;left:66px;top:58px;width:486px;font:400 25px/36px Poppins;color:#1f2d4d}
  .k-row .para{position:absolute;left:14px;top:6px;width:540px;font:400 20px/29px Poppins;color:#34445f}
  .k-row .para b{font-weight:700;color:#0a0d2c}
  /* ---------------- PHONE */
  .k-ph{position:absolute;left:0;top:0;width:320px;height:600px;border-radius:50px;background:linear-gradient(170deg,#26306a,#0a0f30 60%,#050822);
    box-shadow:inset 0 0 0 2px rgba(255,255,255,.16),inset 0 0 0 6px rgba(0,0,0,.35),0 30px 60px rgba(2,6,26,.6);transform-origin:50% 50%}
  .k-ph .glw{position:absolute;left:-5px;top:-5px;width:330px;height:610px;border-radius:55px;box-shadow:0 0 0 3px #5be08a,0 0 34px rgba(91,224,138,.6);opacity:0}
  .k-ph .scr{position:absolute;left:12px;top:12px;width:296px;height:576px;border-radius:38px;overflow:hidden;background:#e9eef6}
  .k-ph .blank{position:absolute;inset:0}
  .k-ph .blank i{position:absolute;left:24px;height:12px;border-radius:6px;background:#d3dbe8}
  .k-ph .blank .ph{position:absolute;left:78px;top:168px;width:140px;height:208px;border-radius:26px;border:3px dashed #b3c0d6}
  .k-ph .blank .ph b{position:absolute;left:0;top:78px;width:134px;text-align:center;font:700 16px/22px Poppins;color:#8a99b3}
  .k-ph .bg{position:absolute;inset:0;background:linear-gradient(165deg,#155b6c 0%,#0d3b48 52%,#061f28 100%)}
  .k-ph .lit{position:absolute;inset:0;background:radial-gradient(circle at 16% 10%,rgba(255,212,140,.55),rgba(255,212,140,0) 58%)}
  .k-ph .beam{position:absolute;left:-30px;top:-80px;width:200px;height:600px;transform-origin:50% 0%;
    background:linear-gradient(180deg,rgba(255,228,170,.46),rgba(255,228,170,.10) 70%,rgba(255,228,170,0))}
  .k-ph .col{position:absolute;left:0;top:0;width:296px;height:1100px}
  .k-ph .hl{position:absolute;left:22px;top:54px;width:256px;font:700 25px/31px Poppins;color:#ffffff;text-shadow:0 3px 12px rgba(0,0,0,.35);transform-origin:0 0}
  .k-ph .shd{position:absolute;left:78px;top:378px;width:140px;height:30px;border-radius:50%;background:radial-gradient(ellipse at 50% 50%,rgba(0,0,0,.72),rgba(0,0,0,0) 70%);transform-origin:50% 50%}
  .k-ph .bpos{position:absolute;left:88px;top:170px;width:120px;height:200px;transform-origin:50% 60%}
  .k-ph .bfl,.k-ph .bsp{position:absolute;left:0;top:0;width:120px;height:200px;transform-origin:50% 50%}
  .k-ph .bsp svg{position:absolute;left:0;top:0;width:120px;height:200px;overflow:visible}
  .k-ph .sect{position:absolute;left:14px;width:268px}
  .k-ph .sect h4{font:700 16px/22px Poppins;color:#bff3ff;letter-spacing:.5px}
  .k-ph .pc{position:absolute;top:30px;width:84px;height:120px;border-radius:16px;background:rgba(255,255,255,.10);box-shadow:inset 0 0 0 1.2px rgba(255,255,255,.18)}
  .k-ph .pc .mb{position:absolute;left:28px;top:14px;width:28px;height:50px}
  .k-ph .pc .mb i{position:absolute;left:8px;top:0;width:12px;height:11px;border-radius:3px;background:#1a1a1e}
  .k-ph .pc .mb u{position:absolute;left:0;top:12px;width:28px;height:38px;border-radius:9px}
  .k-ph .pc b{position:absolute;left:0;top:72px;width:84px;text-align:center;font:700 14px/20px Poppins;color:#fff}
  .k-ph .pc span{position:absolute;left:0;top:92px;width:84px;text-align:center;font:400 12px/18px Poppins;color:#a9d6df}
  .k-ph .tb{position:absolute;left:0;top:30px;width:268px;height:104px;border-radius:18px;background:#ffffff;box-shadow:0 8px 20px rgba(0,0,0,.25)}
  .k-ph .tb .st{position:absolute;left:14px;top:12px;display:flex;gap:2px;color:#f5b43c}
  .k-ph .tb .st svg{width:16px;height:16px;fill:#f5b43c}
  .k-ph .tb b{position:absolute;left:14px;top:34px;font:700 16px/24px Poppins;color:#0a0d2c;white-space:nowrap}
  .k-ph .tb span{position:absolute;left:14px;top:62px;font:400 13px/20px Poppins;color:#5d6f8f;white-space:nowrap}
  .k-ph .wa{position:absolute;left:24px;top:500px;width:248px;height:54px;border-radius:27px;background:#2da44e;box-shadow:0 8px 20px rgba(0,0,0,.3);
    display:flex;align-items:center;justify-content:center;gap:8px;font:700 17px/1 Poppins;color:#fff;white-space:nowrap;transform-origin:50% 50%}
  .k-ph .wa svg{width:22px;height:22px}
  .k-ph .sbar{position:absolute;right:7px;top:70px;width:5px;height:420px;border-radius:3px;background:rgba(255,255,255,.18)}
  .k-ph .sbar i{position:absolute;left:0;top:0;width:5px;height:70px;border-radius:3px;background:#ffffff}
  .k-ph .hand{position:absolute;left:0;top:0;width:58px;height:58px;color:#ffffff;filter:drop-shadow(0 4px 8px rgba(0,0,0,.45))}
  .k-ph .hand svg{width:58px;height:58px}
  .k-ph .tag{position:absolute;left:0;top:0;height:34px;padding:0 12px 0 8px;border-radius:17px;display:flex;align-items:center;gap:6px;background:rgba(6,12,40,.84);
    box-shadow:inset 0 0 0 1.2px rgba(106,223,255,.6);font:700 16px/1 Poppins;color:#fff;white-space:nowrap;transform-origin:50% 50%}
  .k-ph .tag svg{width:18px;height:18px;color:#6adfff}
  .k-ph .sheet{position:absolute;left:10px;top:376px;width:276px;height:188px;border-radius:24px;background:rgba(6,12,40,.94);box-shadow:inset 0 0 0 1.5px rgba(106,223,255,.45),0 -10px 30px rgba(0,0,0,.35)}
  .k-ph .sheet .sr{position:absolute;left:12px;width:252px;height:52px}
  .k-ph .sheet .sr .ic{position:absolute;left:0;top:6px;width:40px;height:40px;border-radius:12px;background:rgba(1,204,247,.14);color:#6adfff}
  .k-ph .sheet .sr .ic svg{position:absolute;left:9px;top:9px;width:22px;height:22px}
  .k-ph .sheet .sr b{position:absolute;left:52px;top:4px;font:700 17px/24px Poppins;color:#fff;white-space:nowrap}
  .k-ph .sheet .sr span{position:absolute;left:52px;top:27px;font:400 13px/20px Poppins;color:#9fdcf2;white-space:nowrap}
  .k-ph .sheet .sr .ck{position:absolute;right:0;top:12px;width:28px;height:28px;border-radius:14px;background:#2da44e;color:#fff}
  .k-ph .sheet .sr .ck svg{position:absolute;left:6px;top:6px;width:16px;height:16px}
  .k-ph .sheet .mt{position:absolute;left:52px;top:31px;width:150px;height:8px;border-radius:4px;background:rgba(255,255,255,.14);overflow:hidden}
  .k-ph .sheet .mt i{position:absolute;left:0;top:0;width:150px;height:8px;border-radius:4px;background:linear-gradient(90deg,#5be08a,#2da44e);transform-origin:0 50%}
  .k-ph .scan{position:absolute;left:0;top:0;width:296px;height:4px;background:#6adfff;box-shadow:0 0 16px 4px rgba(1,204,247,.7)}
  .k-ph .isl{position:absolute;left:106px;top:10px;width:84px;height:24px;border-radius:12px;background:#05060c}
  .k-ph .cth{position:absolute;right:12px;top:42px;height:22px;padding:0 8px;border-radius:11px;font:700 11px/22px Poppins;letter-spacing:1.2px;color:#5d6f8f;background:rgba(255,255,255,.85)}
  `;
  if (!document.getElementById("r25kit-css")) {
    const st = document.createElement("style"); st.id = "r25kit-css"; st.textContent = CSS; document.head.appendChild(st);
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

  // ------------------------------------------------------------------ TOPIC HEADER (single item; s03)
  K.headerHTML = (P) => {
    let h = `<div class="k-hplate" id="${P}-hplate"></div><div class="k-hglow" id="${P}-hglow"></div>`;
    h += `<div class="k-hnum" id="${P}-hnum"><div class="k-hroll" id="${P}-hroll">` + K.HD.map((d) => `<b>${K.svg(d.tile)}</b>`).join("") + `</div></div>`;
    h += `<div class="k-hbox" id="${P}-hnb" style="left:214px;top:328px;width:540px;height:66px">` + K.HD.map((d, k) => `<div class="k-hname" id="${P}-hn${k}">${d.name}</div>`).join("") + `</div>`;
    h += `<div class="k-hbox" id="${P}-hsb" style="left:214px;top:396px;width:540px;height:40px">` + K.HD.map((d, k) => `<div class="k-hsub" id="${P}-hs${k}">${d.sub}</div>`).join("") + `</div>`;
    h += `<div class="k-hbox" id="${P}-hlb" style="left:752px;top:356px;width:250px;height:40px">` + K.HD.map((d, k) => `<div class="k-hchip" id="${P}-hl${k}">${K.svg(d.chipIc)}${d.chip}</div>`).join("") + `</div>`;
    return `<div class="k-ab" id="${P}-hdr" style="width:1080px;height:1920px">${h}</div>`;
  };
  // header builds in from nothing at local time t (plate scales up, tile pops, name/sub/chip rise)
  K.headerIn = (S, P, t) => {
    const { I, ft, $ } = S;
    const pl = $(`${P}-hplate`), nm = $(`${P}-hnum`);
    I(pl, { scale: 0.94, opacity: 0, transformOrigin: "50% 50%" }); ft(pl, { scale: 0.94, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.34, ease: "power3.out" }, t);
    I(nm, { scale: 0.4, opacity: 0, transformOrigin: "50% 50%" }); ft(nm, { scale: 0.4, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.34, ease: "back.out(2.2)" }, t + 0.08);
    I($(`${P}-hroll`), { y: 0 });
    [[`${P}-hn0`, 66, 0.14], [`${P}-hs0`, 40, 0.22], [`${P}-hl0`, 40, 0.28]].forEach(([id, d, dt]) => { I($(id), { y: d, opacity: 0 }); ft($(id), { y: d, opacity: 0 }, { y: 0, opacity: 1, duration: 0.42, ease: "power3.out" }, t + dt); });
    I($(`${P}-hglow`), { opacity: 0 });
    ft($(`${P}-hglow`), { opacity: 0 }, { opacity: 1, duration: 0.14 }, t + 0.2); ft($(`${P}-hglow`), { opacity: 1 }, { opacity: 0, duration: 0.5, ease: "power2.inOut" }, t + 0.34);
  };

  // ------------------------------------------------------------------ PROMPT CARD
  // markup only; every row has: hi (active plate), dc (disc: number / on / ok), lb (label), pv (one-line preview), tx (typed text),
  // para (s01 paragraph). Ids: P-card, P-ttl, P-r{i}, P-r{i}-hi, -dc, -on, -ok, -lb, -pv, -tx, -para.
  K.cardHTML = (P, title = "prompt-website-3d.txt") =>
    `<div class="k-card" id="${P}-card"><div class="ttl"><div class="fi">${K.svg("file-text")}</div><b id="${P}-ttl">${title}</b><div class="k-demo w">CONTOH</div></div>` +
    K.ROWS.map((r, i) => `<div class="k-row" id="${P}-r${i}"><div class="bp" id="${P}-r${i}-bp"></div><div class="hi" id="${P}-r${i}-hi"></div>` +
      `<div class="para" id="${P}-r${i}-para"><b>${r.lab}:</b> ${r.txt}</div>` +
      `<div class="dc" id="${P}-r${i}-dc">${i + 1}<div class="on" id="${P}-r${i}-on">${i + 1}</div><div class="ok" id="${P}-r${i}-ok">${K.svg("check")}</div></div>` +
      `<div class="lb" id="${P}-r${i}-lb">${r.lab}</div><div class="pv" id="${P}-r${i}-pv">${r.txt}</div><div class="tx" id="${P}-r${i}-tx"></div></div>`).join("") +
    `<div class="ft" id="${P}-ft"><b><em>5</em> bagian</b><span>kita isi satu per satu</span></div><div class="cg" id="${P}-cg"></div></div>`;
  // pin the card in the "collapsed" state (s01 end = s02 start): rows labelled, no preview, footer shown
  K.cardCollapsed = (S, P) => {
    const { I, $ } = S, tops = K.rowTops(-1);
    I($(`${P}-card`), { x: K.CARD.x, y: K.CARD.y, scale: 1, opacity: 1 });
    I($(`${P}-cg`), { opacity: 0 }); I($(`${P}-ft`), { opacity: 1, y: 0, scale: 1, transformOrigin: "50% 50%" });
    K.ROWS.forEach((_, i) => {
      const r = (x) => $(`${P}-r${i}${x}`);
      I(r(""), { top: tops[i], height: K.RH, x: 0, rotation: 0, opacity: 1 });
      I(r("-bp"), { opacity: 1 }); I(r("-hi"), { opacity: 0 }); I(r("-para"), { opacity: 0 });
      I(r("-dc"), { scale: 1, opacity: 1, transformOrigin: "50% 50%" }); I(r("-on"), { opacity: 0 }); I(r("-ok"), { opacity: 0 });
      I(r("-lb"), { opacity: 1, x: 0 }); I(r("-pv"), { opacity: 0 }); I(r("-tx"), { opacity: 1 });
    });
  };

  // ------------------------------------------------------------------ BOTTLE (our own SVG: amber glass perfume bottle, front + back)
  K.bottleSVG = (P) => {
    const g = (id) => `${P}-${id}`;
    const body = "M30 52 H90 Q112 52 112 76 V170 Q112 194 88 194 H32 Q8 194 8 170 V76 Q8 52 30 52 Z";
    return `<svg viewBox="0 0 120 200"><defs>
      <linearGradient id="${g("am")}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7a3a0c"/><stop offset=".28" stop-color="#d27a1c"/><stop offset=".5" stop-color="#f8bb52"/><stop offset=".72" stop-color="#d47a1c"/><stop offset="1" stop-color="#6e330a"/></linearGradient>
      <linearGradient id="${g("lq")}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd27e" stop-opacity=".0"/><stop offset="1" stop-color="#5a2a06" stop-opacity=".45"/></linearGradient>
      <linearGradient id="${g("cp")}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0b0b0e"/><stop offset=".45" stop-color="#3a3a42"/><stop offset="1" stop-color="#0b0b0e"/></linearGradient>
      <linearGradient id="${g("gd")}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9c7422"/><stop offset=".5" stop-color="#f6d98a"/><stop offset="1" stop-color="#8e661c"/></linearGradient>
    </defs>
    <rect x="40" y="4" width="40" height="34" rx="7" fill="url(#${g("cp")})"/>
    <rect x="36" y="36" width="48" height="10" rx="3" fill="url(#${g("gd")})"/>
    <rect x="47" y="45" width="26" height="9" fill="#8a4512"/>
    <path d="${body}" fill="url(#${g("am")})"/>
    <path d="${body}" fill="url(#${g("lq")})"/>
    <g id="${g("front")}"><rect x="30" y="102" width="60" height="54" rx="7" fill="#f8efe0" opacity=".96"/>
      <text x="60" y="126" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="11" letter-spacing="1.5" fill="#6b3a12">PARFUM</text>
      <rect x="44" y="132" width="32" height="1.6" fill="#c08a4a"/>
      <text x="60" y="146" text-anchor="middle" font-family="Poppins" font-weight="400" font-size="9" fill="#8a5a2a">lokal</text></g>
    <rect x="20" y="64" width="9" height="114" rx="4.5" fill="#ffffff" opacity=".42"/>
    <rect x="96" y="70" width="5" height="70" rx="2.5" fill="#ffffff" opacity=".22"/>
    <g id="${g("bhi")}"><rect x="13" y="60" width="22" height="126" rx="11" fill="#fff3d6" opacity=".55"/><circle cx="34" cy="70" r="5" fill="#ffffff" opacity=".9"/></g>
    </svg>`;
  };

  // ------------------------------------------------------------------ PHONE (our own example page: toko parfum lokal, CONTOH)
  const miniB = (c1, c2) => `<div class="mb"><i></i><u style="background:linear-gradient(90deg,${c1},${c2} 50%,${c1})"></u></div>`;
  K.phoneHTML = (P) =>
    `<div class="k-ph" id="${P}-ph"><div class="glw" id="${P}-glw"></div><div class="scr" id="${P}-scr">` +
    `<div class="blank" id="${P}-blank"><i style="top:60px;width:150px"></i><i style="top:82px;width:110px"></i><div class="ph" id="${P}-phd"><b>objek<br>utama?</b></div>` +
    `<i style="top:420px;width:248px;height:54px;border-radius:27px;opacity:.6"></i></div>` +
    `<div class="bg" id="${P}-bg"></div><div class="lit" id="${P}-lit"></div><div class="beam" id="${P}-beam"></div>` +
    `<div class="col" id="${P}-col">` +
      `<div class="hl" id="${P}-hl">Wangi lokal,<br>nempel seharian.</div>` +
      `<div class="shd" id="${P}-shd"></div>` +
      `<div class="bpos" id="${P}-bpos"><div class="bfl" id="${P}-bfl"><div class="bsp" id="${P}-bsp">${K.bottleSVG(P)}</div></div></div>` +
      `<div class="sect" id="${P}-prod" style="top:600px"><h4>Pilihan aroma</h4>` +
        [["Senja", "#c8701a", "#f4b04a", 0], ["Hujan", "#2f6f8a", "#7cc6dc", 92], ["Kopi", "#5a3214", "#a8683a", 184]].map(([n, a, b, x]) =>
          `<div class="pc" style="left:${x}px">${miniB(a, b)}<b>${n}</b><span>50 ml</span></div>`).join("") + `</div>` +
      `<div class="sect" id="${P}-testi" style="top:790px"><h4>Kata pembeli</h4><div class="tb"><div class="st">${[0, 1, 2, 3, 4].map(() => K.svg("star")).join("")}</div>` +
        `<b>&ldquo;Wanginya awet seharian!&rdquo;</b><span>Rina, Bandung &middot; contoh</span></div></div>` +
    `</div>` +
    `<div class="sbar" id="${P}-sbar"><i id="${P}-sth"></i></div>` +
    `<div class="tag" id="${P}-tg0">${K.svg("move-vertical")}melayang</div>` +
    `<div class="tag" id="${P}-tg1">${K.svg("palette")}warna latar</div>` +
    `<div class="tag" id="${P}-tg2">${K.svg("sun")}cahaya</div>` +
    `<div class="tag" id="${P}-tg3">${K.svg("layers")}bayangan</div>` +
    `<div class="tag" id="${P}-tg4">${K.svg("rotate-3d")}360&deg;</div>` +
    `<div class="tag" id="${P}-tg5">${K.svg("zap")}mendekat</div>` +
    `<div class="tag" id="${P}-tg6">${K.svg("check")}judul diperbesar</div>` +
    `<div class="hand" id="${P}-hand">${K.svg("pointer")}</div>` +
    `<div class="wa" id="${P}-wa">${K.svg("message-circle")}Pesan via WhatsApp</div>` +
    `<div class="sheet" id="${P}-sheet">` +
      `<div class="sr" style="top:12px"><div class="ic">${K.svg("file-code")}</div><b>index.html</b><span>cukup 1 file</span><div class="ck" id="${P}-ck0">${K.svg("check")}</div></div>` +
      `<div class="sr" style="top:68px"><div class="ic">${K.svg("box")}</div><b>Three.js</b><span>objek 3D-nya</span><div class="ck" id="${P}-ck1">${K.svg("check")}</div></div>` +
      `<div class="sr" style="top:124px"><div class="ic">${K.svg("gauge")}</div><b>Ringan di HP</b><div class="mt"><i id="${P}-mt"></i></div><div class="ck" id="${P}-ck2">${K.svg("check")}</div></div>` +
    `</div>` +
    `<div class="scan" id="${P}-scan"></div><div class="isl"></div><div class="cth">CONTOH</div>` +
    `</div></div>`;
  // tag anchors (screen-local px; xc = centre x)
  K.TAGS = [[200, 150], [92, 520], [70, 66], [148, 420], [222, 150], [74, 470], [148, 470]];
  // pin the phone at a stage: "blank" (placeholder page) or "full" (the finished example page)
  K.phoneSet = (S, P, stage) => {
    const { I, $ } = S, full = stage === "full";
    I($(`${P}-ph`), { x: K.PHONE.x, y: K.PHONE.y, scale: 1, opacity: 1 });
    I($(`${P}-glw`), { opacity: 0 });
    I($(`${P}-blank`), { opacity: full ? 0 : 1 });
    I($(`${P}-phd`), { scale: 1, opacity: 1, transformOrigin: "50% 50%" });
    I($(`${P}-bg`), { opacity: full ? 1 : 0, clipPath: full ? "circle(150% at 0% 0%)" : "circle(0% at 0% 0%)" });
    I($(`${P}-lit`), { opacity: full ? 1 : 0 });
    I($(`${P}-beam`), { opacity: full ? 1 : 0, rotation: -26, scaleY: full ? 1 : 0, transformOrigin: "50% 0%" });
    I($(`${P}-col`), { y: 0 });
    I($(`${P}-hl`), { opacity: full ? 1 : 0, y: 0, scale: 1, transformOrigin: "0% 0%" });
    I($(`${P}-shd`), { opacity: full ? 1 : 0, scale: full ? 1 : 0.4, transformOrigin: "50% 50%" });
    I($(`${P}-bpos`), { opacity: full ? 1 : 0, y: 0, scale: 1, transformOrigin: "50% 60%" });
    I($(`${P}-bfl`), { y: 0, rotation: 0 });
    I($(`${P}-bsp`), { scaleX: 1 });
    I($(`${P}-front`), { opacity: 1 });
    I($(`${P}-bhi`), { opacity: full ? 1 : 0 });
    I($(`${P}-prod`), { opacity: full ? 1 : 0 }); I($(`${P}-testi`), { opacity: full ? 1 : 0 });
    I($(`${P}-sbar`), { opacity: 0 }); I($(`${P}-sth`), { y: 0 });
    for (let k = 0; k < 7; k++) I($(`${P}-tg${k}`), { x: K.TAGS[k][0], y: K.TAGS[k][1], xPercent: -50, yPercent: -50, scale: 0.5, opacity: 0 });
    I($(`${P}-hand`), { x: 190, y: 470, opacity: 0 });
    I($(`${P}-wa`), { opacity: full ? 1 : 0, scale: 1, y: 0 });
    I($(`${P}-sheet`), { y: 230, opacity: 0 });
    for (let k = 0; k < 3; k++) I($(`${P}-ck${k}`), { scale: 0, opacity: 0, transformOrigin: "50% 50%" });
    I($(`${P}-mt`), { scaleX: 0.08 });
    I($(`${P}-scan`), { y: -10, opacity: 0 });
  };
  // a floating bob between local times t0 and t1 (yoyo sine; starts and ends at y = -amp)
  K.bob = (S, el, t0, t1, amp = 7, per = 2.4) => {
    const { ft, I } = S;
    const half = per / 2, n = Math.max(1, Math.floor((t1 - t0) / half));
    ft(el, { y: -amp, rotation: -1.6 }, { y: amp, rotation: 1.6, duration: half, ease: "sine.inOut", yoyo: true, repeat: n - 1 }, t0);
  };
  // a 360° spin of the bottle (scaleX 1 -> -1 -> 1; the label hides while the back faces the viewer)
  K.spin = (S, P, t, dur = 0.9) => {
    const { ft, tl, $ } = S, b = $(`${P}-bsp`), f = $(`${P}-front`);
    ft(b, { scaleX: 1 }, { scaleX: -1, duration: dur / 2, ease: "sine.inOut" }, t);
    ft(b, { scaleX: -1 }, { scaleX: 1, duration: dur / 2, ease: "sine.inOut" }, t + dur / 2);
    tl.set(f, { opacity: 0 }, t + dur / 4); tl.set(f, { opacity: 1 }, t + (3 * dur) / 4);
  };
  K.tagIn = (S, P, k, t) => { const { ft, $ } = S; ft($(`${P}-tg${k}`), { scale: 0.5, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.28, ease: "back.out(2.4)" }, t); };
  K.tagOut = (S, P, k, t) => { const { ft, $ } = S; ft($(`${P}-tg${k}`), { scale: 1, opacity: 1 }, { scale: 0.85, opacity: 0, duration: 0.2, ease: "power2.in" }, t); };
})();

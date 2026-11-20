// R28 SISTEM (bangun 5 sistem bisnis) — shared scene kit (loaded in index.html <head> after vo_words.js + r28icons.js; every
// scene uses window.R28K). Boilerplate from the R25/R19 kit: timeline wrapper with every initial state pinned at 0 in a NESTED
// timeline that is the first child of the scene timeline (I), ft (fromTo, immediateRender:false), wt (scene-local word time),
// per-letter typing, finish() = end marker + backward-seek patch + tl.render(0, true, true) + registration.
// R28 components (identical wherever they appear, so scenes hand them over at the same position):
//   SYSTEM BAR  five tiles (x 60 + i*195, y 318, 180 x 120): icon disc, number, label, process-fill bar, done check.
//   ACCENT DOT  the guide object (#01ccf7, 26 px) that carries every hand-off.
//   CAMERA      per scene a slow push 1.00 -> 1.04 on the stage wrapper (origin 540, 560); the system bar stays outside it.
// Brand: navy theme = white text, cyan #01ccf7 / #6adfff accents, white cards with navy text (#0a0d2c / #294b77 / #5d6f8f).
// Deterministic: no Math.random, no Date, no rAF.
(function () {
  const K = (window.R28K = {});
  const ICO = window.R28_ICO || {};
  K.svg = (n, cls = "", extra = "") =>
    `<svg class="${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ${extra}>${ICO[n] || ""}</svg>`;

  K.SYS = [
    { ic: "shopping-cart", lab: "Penjualan" },
    { ic: "megaphone", lab: "Pemasaran" },
    { ic: "wallet", lab: "Keuangan" },
    { ic: "users", lab: "Rekrutmen" },
    { ic: "truck", lab: "Pengiriman" },
  ];
  K.TILE = (i) => ({ x: 60 + i * 195, y: 318, w: 180, h: 120 });
  K.TC = (i) => ({ x: 60 + i * 195 + 90, y: 318 + 60 });     // tile centre
  // s01 -> s02 hand-over: the "kamu" node with 8 jammed task chips wired into it (identical in both scenes)
  K.NODE = { x: 540, y: 620, r: 92 };
  K.JAM = [["message-circle", "Balas chat"], ["receipt", "Catat order"], ["banknote", "Cek transfer"], ["pencil", "Bikin konten"],
           ["package", "Packing"], ["wallet", "Rekap kas"], ["user-plus", "Cari karyawan"], ["phone", "Jawab komplain"]]
    .map(([ic, t], i) => { const a = (Math.PI / 180) * (337.5 - i * 45); return { ic, t, x: Math.round(540 + 330 * Math.cos(a)), y: Math.round(620 - 214 * Math.sin(a)) }; });
  K.jamHTML = (P) =>
    `<svg class="k-ab" width="1080" height="1000" style="overflow:visible">` + K.JAM.map((j, i) =>
      `<line id="${P}-jl${i}" x1="540" y1="620" x2="${j.x}" y2="${j.y}" stroke="#6adfff" stroke-width="3" stroke-dasharray="10 9" stroke-linecap="round" opacity=".7"/>`).join("") + `</svg>` +
    K.JAM.map((j, i) => `<div class="k-jc" id="${P}-jc${i}" style="left:${j.x}px;top:${j.y}px"><i>${K.svg(j.ic)}</i>${j.t}</div>`).join("") +
    `<div class="k-node" id="${P}-node"><div class="rg" id="${P}-rg0"></div><div class="rg" id="${P}-rg1"></div><div class="cc">${K.svg("user")}<b>KAMU</b></div></div>`;

  const CSS = `
  .k-ab{position:absolute;left:0;top:0}
  .k-cam{position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:540px 560px}
  .k-glass{position:absolute;border-radius:28px;background:rgba(12,22,64,.86);box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.12),0 22px 46px rgba(2,6,26,.5)}
  .k-white{position:absolute;border-radius:28px;background:linear-gradient(180deg,#ffffff,#f4f7fc);box-shadow:0 26px 56px rgba(2,6,26,.55)}
  .k-hd{position:absolute;left:24px;top:20px;height:44px;display:flex;align-items:center;gap:12px;font:700 25px/1 Poppins;color:#0a0d2c;white-space:nowrap}
  .k-hd .di{width:44px;height:44px;border-radius:14px;background:linear-gradient(160deg,#9cecff,#01ccf7 55%,#0aa7d6);color:#0b1440;position:relative;flex:none}
  .k-hd .di svg{position:absolute;left:11px;top:11px;width:22px;height:22px}
  .k-glass .k-hd{color:#fff}
  .k-tag{position:absolute;height:30px;padding:0 12px;border-radius:15px;font:700 15px/30px Poppins;letter-spacing:1.5px;color:#5d6f8f;background:#eef3fb;box-shadow:inset 0 0 0 1.2px #d5deec;white-space:nowrap}
  .k-tag.n{color:#c7d5ea;background:rgba(255,255,255,.07);box-shadow:inset 0 0 0 1.2px rgba(255,255,255,.25)}
  .k-chip{position:absolute;height:48px;padding:0 20px 0 14px;border-radius:24px;display:flex;align-items:center;gap:10px;font:700 22px/1 Poppins;color:#ffffff;
    background:rgba(1,204,247,.16);box-shadow:inset 0 0 0 2px rgba(1,204,247,.8),0 0 22px rgba(1,204,247,.3);white-space:nowrap}
  .k-chip svg{width:24px;height:24px;color:#6adfff}
  .k-chip.s{background:#01ccf7;color:#0b1440;box-shadow:0 0 26px rgba(1,204,247,.55)}
  .k-chip.s svg{color:#0b1440}
  .k-dot{position:absolute;left:0;top:0;width:26px;height:26px;margin:-13px 0 0 -13px;border-radius:13px;background:#01ccf7;
    box-shadow:0 0 0 6px rgba(1,204,247,.22),0 0 26px 6px rgba(1,204,247,.55)}
  .k-x{position:absolute;left:0;top:0;width:76px;height:76px;margin:-38px 0 0 -38px;border-radius:38px;background:#ffffff;color:#0b1440;box-shadow:0 10px 26px rgba(2,6,26,.5)}
  .k-x svg{position:absolute;left:14px;top:14px;width:48px;height:48px;stroke-width:3}
  .k-ok{position:absolute;width:40px;height:40px;border-radius:20px;background:#01ccf7;color:#0b1440;box-shadow:0 0 16px rgba(1,204,247,.6)}
  .k-ok svg{position:absolute;left:9px;top:9px;width:22px;height:22px;stroke-width:3}
  /* ---------------- KAMU node + jammed chips */
  .k-jc{position:absolute;height:56px;padding:0 22px 0 10px;border-radius:28px;display:flex;align-items:center;gap:10px;
    background:#ffffff;box-shadow:0 12px 28px rgba(2,6,26,.45);font:700 22px/1 Poppins;color:#0a0d2c;white-space:nowrap}
  .k-jc i{position:relative;width:38px;height:38px;border-radius:19px;background:#e6f8fe;color:#0786b0;flex:none}
  .k-jc i svg{position:absolute;left:9px;top:9px;width:20px;height:20px}
  .k-node{position:absolute;left:448px;top:528px;width:184px;height:184px;transform-origin:50% 50%}
  .k-node .cc{position:absolute;inset:0;border-radius:92px;background:radial-gradient(circle at 40% 32%,#ffffff,#e6eef9 70%,#cfdcf0);
    box-shadow:0 0 0 6px rgba(1,204,247,.35),0 0 44px rgba(1,204,247,.45),0 24px 50px rgba(2,6,26,.55)}
  .k-node .cc svg{position:absolute;left:58px;top:30px;width:68px;height:68px;color:#0b1440;stroke-width:2.2}
  .k-node .cc b{position:absolute;left:0;top:104px;width:184px;text-align:center;font:700 30px/40px Poppins;color:#0a0d2c;letter-spacing:1px}
  .k-node .rg{position:absolute;inset:0;border-radius:92px;box-shadow:inset 0 0 0 4px #01ccf7;opacity:0;transform-origin:50% 50%}
  /* ---------------- SYSTEM BAR */
  .k-tile{position:absolute;width:180px;height:120px;border-radius:24px;transform-origin:50% 50%}
  .k-tile .bp{position:absolute;inset:0;border-radius:24px;background:rgba(12,22,64,.88);box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.14),0 16px 34px rgba(2,6,26,.45)}
  .k-tile .hi{position:absolute;inset:0;border-radius:24px;box-shadow:inset 0 0 0 3px #01ccf7,0 0 30px rgba(1,204,247,.45);background:rgba(1,204,247,.10);opacity:0}
  .k-tile .ic{position:absolute;left:16px;top:16px;width:48px;height:48px;border-radius:15px;background:linear-gradient(160deg,#9cecff,#01ccf7 55%,#0aa7d6);color:#0b1440}
  .k-tile .ic svg{position:absolute;left:12px;top:12px;width:24px;height:24px}
  .k-tile .nm{position:absolute;right:16px;top:20px;width:36px;height:36px;border-radius:18px;font:700 19px/36px Poppins;color:#6adfff;text-align:center;box-shadow:inset 0 0 0 1.5px rgba(106,223,255,.5)}
  .k-tile .ok{position:absolute;right:16px;top:20px;width:36px;height:36px;border-radius:18px;background:#01ccf7;color:#0b1440;opacity:0;box-shadow:0 0 14px rgba(1,204,247,.7)}
  .k-tile .ok svg{position:absolute;left:8px;top:8px;width:20px;height:20px;stroke-width:3}
  .k-tile b{position:absolute;left:16px;top:70px;font:700 21px/26px Poppins;color:#ffffff;white-space:nowrap}
  .k-tile .fb{position:absolute;left:16px;right:16px;bottom:12px;height:6px;border-radius:3px;background:rgba(255,255,255,.14);overflow:hidden}
  .k-tile .fb u{position:absolute;left:0;top:0;width:100%;height:6px;border-radius:3px;background:linear-gradient(90deg,#6adfff,#01ccf7);transform-origin:0 50%}
  `;
  if (!document.getElementById("r28kit-css")) {
    const st = document.createElement("style"); st.id = "r28kit-css"; st.textContent = CSS; document.head.appendChild(st);
  }

  // ------------------------------------------------------------------ timeline boilerplate (R25 kit)
  const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
  K.dur = (id) => { const s = (window.VO_SCENES || []).find((x) => x.id === id); if (!s) throw new Error("no scene " + id); return s.dur; };
  K.total = () => { const v = window.VO_SCENES || []; const L = v[v.length - 1]; return L ? Math.round((L.start + L.dur) * 1e4) / 1e4 : 0; };
  K.scene = (id, D) => {
    const tl = gsap.timeline({ paused: true });
    const cl = (p) => (typeof p === "number" ? Math.max(0, p) : p);
    { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); tl.set = (a, v, p) => s0(a, _sc(v), cl(p)); tl.fromTo = (a, x, y, p) => f0(a, _sc(x), _sc(y), cl(p)); tl.to = (a, v, p) => t0(a, _sc(v), cl(p)); }
    const P0 = gsap.timeline(); tl.add(P0, 0);
    const I = (el, v) => { gsap.set(el, _sc(v)); P0.set(el, _sc(v), 0); };
    const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), typeof t === "number" ? Math.max(0.005, t) : t);
    const SC = (window.VO_SCENES || []).find((s) => s.id === id) || { start: 0 };
    const T0 = SC.start;
    const wt = (txt, after) => { const a = after === undefined ? T0 - 0.05 : after; const w = (window.VO_WORDS || []).find((x) => x[0] === txt && x[1] >= a - 1e-6); if (!w) throw new Error(id + ": word not found " + txt); return w[1] - T0; };
    const $ = (x) => document.getElementById(x);
    const finish = () => {
      tl.set({}, {}, D - 0.01);
      (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
      tl.render(0, true, true);
      window.__timelines = window.__timelines || {};
      window.__timelines[id] = tl;
    };
    const esc = (c) => c.replace(/&/g, "&amp;").replace(/</g, "&lt;");
    const type = (el, text, t0, cps, cls = "") => {
      el.innerHTML = text.split(" ").map((w) => `<span style="white-space:nowrap">${Array.from(w).map((c) => `<span class="${cls}">${esc(c)}</span>`).join("")}</span>`).join(" ");
      const sp = el.querySelectorAll(":scope > span > span"); let k = 0, ci = 0;
      Array.from(text).forEach((c) => { if (c === " ") { ci++; return; } const s = sp[k++]; I(s, { opacity: 0 }); tl.set(s, { opacity: 1 }, t0 + ci / cps); ci++; });
      return t0 + text.length / cps;
    };
    const typeIn = (el, text, t0, t1, cls = "") => type(el, text, t0, Math.max(8, text.length / Math.max(0.15, t1 - t0)), cls);
    // small-overshoot spring pop (back.out(1.6) ~ 6 % overshoot): nothing appears from nothing
    const popIn = (el, t, from = 0.5, dur = 0.32, ease = "back.out(1.7)") => { I(el, { scale: from, opacity: 0, transformOrigin: "50% 50%" }); ft(el, { scale: from, opacity: 0 }, { scale: 1, opacity: 1, duration: dur, ease }, t); };
    const fadeOut = (el, t, dur = 0.22, extra = {}) => ft(el, Object.assign({ opacity: 1 }, extra.from || {}), Object.assign({ opacity: 0, duration: dur, ease: "power2.in" }, extra.to || {}), t);
    // camera: one eased push 1.00 -> 1.04 over the whole scene (never still, never reversed)
    const cam = (el, z0 = 1, z1 = z0 + 0.04) => { I(el, { scale: z0 }); ft(el, { scale: z0 }, { scale: z1, duration: Math.max(0.1, D - 0.02), ease: "sine.inOut" }, 0.005); };
    return { tl, ft, I, wt, $, finish, type, typeIn, popIn, fadeOut, cam, T0, D, P0 };
  };

  // ------------------------------------------------------------------ system bar
  K.barHTML = (P) => K.SYS.map((s, i) => {
    const b = K.TILE(i);
    return `<div class="k-tile" data-layout-allow-occlusion id="${P}-t${i}" style="left:${b.x}px;top:${b.y}px"><div class="bp"></div><div class="hi" id="${P}-th${i}"></div>` +
      `<div class="ic">${K.svg(s.ic)}</div><div class="nm" data-layout-allow-occlusion id="${P}-tn${i}">${i + 1}</div><div class="ok" id="${P}-tk${i}">${K.svg("check")}</div>` +
      `<b data-layout-allow-occlusion>${s.lab}</b><div class="fb"><u id="${P}-tf${i}"></u></div></div>`;
  }).join("");
  // pin the bar: tiles < done are complete (fill 1 + check), tile `act` highlighted
  K.barSet = (S, P, done, act = -1, vis = true) => {
    const { I, $ } = S;
    K.SYS.forEach((_, i) => {
      I($(`${P}-t${i}`), { opacity: vis ? 1 : 0, scale: 1, x: 0, y: 0 });
      I($(`${P}-th${i}`), { opacity: i === act ? 1 : 0 });
      I($(`${P}-tf${i}`), { scaleX: i < done ? 1 : 0 });
      I($(`${P}-tk${i}`), { opacity: i < done ? 1 : 0, scale: 1, transformOrigin: "50% 50%" });
      I($(`${P}-tn${i}`), { opacity: i < done ? 0 : 1 });
    });
  };
  K.tileOn = (S, P, i, t) => { const { ft, $ } = S; ft($(`${P}-th${i}`), { opacity: 0 }, { opacity: 1, duration: 0.2 }, t);
    ft($(`${P}-t${i}`), { scale: 1 }, { scale: 1.06, duration: 0.14, yoyo: true, repeat: 1, ease: "power2.out" }, t); };
  K.tileFill = (S, P, i, t0, t1) => { const { ft, $ } = S; ft($(`${P}-tf${i}`), { scaleX: 0 }, { scaleX: 1, duration: Math.max(0.1, t1 - t0), ease: "power1.inOut" }, t0); };
  K.tileDone = (S, P, i, t) => { const { ft, $ } = S;
    ft($(`${P}-tn${i}`), { opacity: 1 }, { opacity: 0, duration: 0.12 }, t);
    ft($(`${P}-tk${i}`), { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(1.8)" }, t);
    ft($(`${P}-th${i}`), { opacity: 1 }, { opacity: 0, duration: 0.3 }, t + 0.25); };
})();

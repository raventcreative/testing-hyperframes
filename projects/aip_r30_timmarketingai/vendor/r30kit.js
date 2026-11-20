// R30 MARKETING (tim marketing AI, 3 modul) — shared scene kit (loaded in index.html <head> after vo_words.js + r30icons.js; every
// scene uses window.R30K). Boilerplate from the R25 kit: timeline wrapper with every initial state pinned at 0 in a NESTED timeline
// that is the first child of the scene timeline (I), ft (fromTo, immediateRender:false), wt (scene-local word time), per-letter
// typing, finish() = end marker + backward-seek patch + tl.render(0, true, true) + registration.
// R30 additions:
//   - two layers per scene: #P-cam (scene content, slow camera push 1.00 -> 1.04 around the hero centre) and #P-hud (header,
//     accent dot, hand-over objects: never scaled, so objects handed between scenes sit at identical pixels on both sides of a cut)
//   - MODULE HEADER (modules 1-3) with a mini loop map (3 stations, the active one cyan)
//   - 3D LOGOS: Simple Icons (CC0) paths extruded with Three.js (tools/logo_sprites.html) rendered as 36-frame turntables
//     (assets/logos3d/<name>.png, 6 x 6 cells of 240 px); a logo spins/sways by stepping frames on the timeline (20 Hz)
//   - ACCENT DOT (#01ccf7): the guide object that carries every hand-off
// Brand: navy theme, white text, accent #01ccf7 only. Deterministic: no Math.random, no Date, no rAF.
(function () {
  const K = (window.R30K = {});
  const ICO = window.R30_ICO || {};
  K.svg = (n, cls = "", extra = "") =>
    `<svg class="${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ${extra}>${ICO[n] || ""}</svg>`;

  K.MOD = [
    { n: 1, name: "Riset &amp; konten", sub: "cari tren &middot; pertanyaan pembeli &middot; draf" },
    { n: 2, name: "Kreatif &amp; distribusi", sub: "gambar &middot; video &middot; suara &middot; posting" },
    { n: 3, name: "Putaran analitik", sub: "chat &middot; booking &middot; penjualan" },
  ];
  // the org / loop stations (hud coordinates, centre points)
  K.BOX = [{ x: 210, y: 790 }, { x: 540, y: 790 }, { x: 870, y: 790 }];
  K.BOSS = { x: 540, y: 470 };

  const CSS = `
  .k-ab{position:absolute;left:0;top:0}
  .k-zone{position:absolute;left:0;top:0;width:1080px;height:945px;overflow:hidden}
  .k-cam{position:absolute;left:0;top:0;width:1080px;height:945px;transform-origin:540px 640px}
  .k-glass{position:absolute;border-radius:28px;background:rgba(12,22,64,.86);box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.10),0 22px 46px rgba(2,6,26,.5)}
  .k-white{position:absolute;border-radius:26px;background:linear-gradient(180deg,#ffffff,#f4f7fc);box-shadow:0 22px 50px rgba(2,6,26,.55)}
  .k-cy{color:#01ccf7}
  .k-chip{position:absolute;height:46px;padding:0 18px 0 12px;border-radius:23px;display:flex;align-items:center;gap:10px;font:700 21px/1 Poppins;color:#fff;
    background:rgba(10,18,56,.92);box-shadow:inset 0 0 0 1.5px rgba(106,223,255,.7),0 10px 24px rgba(2,6,26,.45);white-space:nowrap;transform-origin:50% 50%}
  .k-chip svg{width:24px;height:24px;color:#6adfff;flex:none}
  .k-chip.on{background:#01ccf7;color:#0b1440;box-shadow:0 0 26px rgba(1,204,247,.55)}
  .k-chip.on svg{color:#0b1440}
  .k-demo{position:absolute;height:28px;padding:0 11px;border-radius:14px;font:700 14px/28px Poppins;letter-spacing:1.5px;color:#e3edfa;
    background:rgba(255,255,255,.07);box-shadow:inset 0 0 0 1.2px rgba(255,255,255,.28);white-space:nowrap}
  .k-demo.w{color:#294b77;background:#eef3fb;box-shadow:inset 0 0 0 1.2px #d5deec}
  .k-ic{position:absolute;border-radius:18px;background:linear-gradient(160deg,#9cecff,#01ccf7 55%,#0aa7d6);color:#0b1440;box-shadow:0 0 20px rgba(1,204,247,.35)}
  .k-ic svg{position:absolute;left:22%;top:22%;width:56%;height:56%}
  .k-ico{position:absolute;border-radius:16px;background:rgba(1,204,247,.14);color:#6adfff;box-shadow:inset 0 0 0 1.5px rgba(1,204,247,.5)}
  .k-ico svg{position:absolute;left:22%;top:22%;width:56%;height:56%}
  .k-dot{position:absolute;left:0;top:0;width:30px;height:30px;margin:-15px 0 0 -15px;border-radius:15px;background:radial-gradient(circle at 38% 34%,#d6f8ff,#01ccf7 58%,#0aa7d6);
    box-shadow:0 0 0 5px rgba(1,204,247,.18),0 0 26px 6px rgba(1,204,247,.6);transform-origin:50% 50%}
  .k-lg{position:absolute;left:0;top:0;background-repeat:no-repeat;transform-origin:50% 50%;filter:drop-shadow(0 14px 18px rgba(2,6,26,.55))}
  .k-pre{position:absolute;left:0;top:0;width:2px;height:2px;opacity:0}
  .k-btn{position:absolute;height:84px;padding:0 36px 0 26px;border-radius:42px;display:flex;align-items:center;gap:14px;font:700 34px/1 Poppins;color:#0b1440;
    background:linear-gradient(180deg,#8cebff,#01ccf7 60%,#0aa7d6);box-shadow:0 0 0 6px rgba(1,204,247,.18),0 0 40px rgba(1,204,247,.5),0 18px 36px rgba(2,6,26,.5);white-space:nowrap;transform-origin:50% 50%}
  .k-btn svg{width:38px;height:38px}
  .k-strike{position:absolute;height:10px;border-radius:5px;background:#ffffff;box-shadow:0 0 14px rgba(255,255,255,.75);transform-origin:0 50%}
  /* ---------------- org: module boxes + boss card (s01/s02/s07) */
  .k-box { position: absolute; left: 0; top: 0; width: 300px; height: 200px; margin: -100px 0 0 -150px; border-radius: 28px; background: rgba(12,22,64,.9);
  box-shadow: inset 0 0 0 2px rgba(106,223,255,.55), 0 0 30px rgba(1,204,247,.18), 0 22px 46px rgba(2,6,26,.5); transform-origin: 50% 50%; }
  .k-box .nm { position: absolute; left: 20px; top: 18px; width: 48px; height: 48px; border-radius: 16px; background: linear-gradient(160deg,#9cecff,#01ccf7 55%,#0aa7d6);
  font: 700 28px/48px Poppins; color: #0b1440; text-align: center; }
  .k-box .ai { position: absolute; left: 80px; top: 26px; height: 32px; padding: 0 12px 0 8px; border-radius: 16px; display: flex; align-items: center; gap: 6px;
  background: rgba(1,204,247,.14); box-shadow: inset 0 0 0 1.2px rgba(1,204,247,.5); font: 700 15px/1 Poppins; letter-spacing: 1.5px; color: #6adfff; white-space: nowrap; }
  .k-box .ai svg { width: 18px; height: 18px; }
  .k-box b { position: absolute; left: 20px; top: 76px; width: 262px; font: 700 25px/31px Poppins; color: #fff; }
  .k-box .ics { position: absolute; left: 20px; top: 146px; display: flex; gap: 8px; }
  .k-box .ics i { position: relative; display: block; width: 36px; height: 36px; border-radius: 11px; background: rgba(1,204,247,.16); color: #6adfff; box-shadow: inset 0 0 0 1.2px rgba(1,204,247,.5); }
  .k-box .ics i svg { position: absolute; left: 8px; top: 8px; width: 20px; height: 20px; }
  .k-boss { position: absolute; left: 0; top: 0; width: 380px; height: 116px; margin: -58px 0 0 -190px; border-radius: 30px; background: linear-gradient(180deg,#ffffff,#f1f5fc);
  box-shadow: 0 0 0 3px #01ccf7, 0 0 36px rgba(1,204,247,.45), 0 22px 46px rgba(2,6,26,.5); transform-origin: 50% 50%; }
  .k-boss .k-ic { left: 18px; top: 18px; width: 80px; height: 80px; border-radius: 24px; }
  .k-boss b { position: absolute; left: 118px; top: 16px; font: 700 40px/50px Poppins; color: #0a0d2c; white-space: nowrap; }
  .k-boss span { position: absolute; left: 118px; top: 64px; font: 400 21px/30px Poppins; color: #294b77; white-space: nowrap; }
  /* ---------------- module header */
  .k-hplate{position:absolute;left:60px;top:330px;width:960px;height:112px;border-radius:30px;background:rgba(12,22,64,.88);
    box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.10),0 18px 40px rgba(3,6,24,.35);transform-origin:50% 50%}
  .k-hglow{position:absolute;left:60px;top:330px;width:960px;height:112px;border-radius:30px;box-shadow:inset 0 0 0 2px rgba(106,223,255,.9),0 0 34px rgba(1,204,247,.35)}
  .k-hnum{position:absolute;left:76px;top:344px;width:84px;height:84px;border-radius:22px;background:linear-gradient(160deg,#9cecff 0%,#01ccf7 52%,#0aa7d6 100%);
    box-shadow:0 0 26px rgba(1,204,247,.45),inset 0 1px 0 rgba(255,255,255,.5);font:700 52px/84px Poppins;color:#0b1440;text-align:center;transform-origin:50% 50%}
  .k-hk{position:absolute;left:182px;top:344px;font:700 17px/24px Poppins;letter-spacing:3px;color:#6adfff;white-space:nowrap}
  .k-hname{position:absolute;left:182px;top:364px;font:700 42px/54px Poppins;color:#fff;letter-spacing:-.5px;white-space:nowrap}
  .k-hsub{position:absolute;left:182px;top:410px;font:400 19px/24px Poppins;color:#e3edfa;opacity:.82;white-space:nowrap}
  .k-map{position:absolute;left:896px;top:344px;width:108px;height:84px}
  .k-map svg{position:absolute;left:0;top:0;width:108px;height:84px;overflow:visible}
  `;
  if (!document.getElementById("r30kit-css")) {
    const st = document.createElement("style"); st.id = "r30kit-css"; st.textContent = CSS; document.head.appendChild(st);
  }

  // ------------------------------------------------------------------ timeline boilerplate (R25 kit)
  const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
  K.dur = (id) => { const s = (window.VO_SCENES || []).find((x) => x.id === id); if (!s) throw new Error("no scene " + id); return s.dur; };
  K.scene = (id, D) => {
    const tl = gsap.timeline({ paused: true });
    const cl = (p) => (typeof p === "number" ? Math.max(0, p) : p);
    { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); tl.set = (a, v, p) => s0(a, _sc(v), cl(p)); tl.fromTo = (a, x, y, p) => f0(a, _sc(x), _sc(y), cl(p)); tl.to = (a, v, p) => t0(a, _sc(v), cl(p)); }
    const P0 = gsap.timeline(); tl.add(P0, 0);
    const I = (el, v) => { gsap.set(el, _sc(v)); P0.set(el, _sc(v), 0); };
    const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), typeof t === "number" ? Math.max(0.005, t) : t);
    const SC = (window.VO_SCENES || []).find((s) => s.id === id) || { start: 0 };
    const T0 = SC.start;
    const wt = (txt, after) => { const a = after === undefined ? T0 - 0.05 : after + T0; const w = (window.VO_WORDS || []).find((x) => x[0] === txt && x[1] >= a - 1e-6); if (!w) throw new Error(id + ": word not found " + txt); return w[1] - T0; };
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
    const popIn = (el, t, from = 0.4, dur = 0.32) => { I(el, { scale: from, opacity: 0, transformOrigin: "50% 50%" }); ft(el, { scale: from, opacity: 0 }, { scale: 1, opacity: 1, duration: dur, ease: "back.out(1.7)" }, t); };
    const fadeOut = (el, t, dur = 0.22) => ft(el, { opacity: 1 }, { opacity: 0, duration: dur, ease: "power2.in" }, t);
    const S = { tl, ft, I, wt, $, finish, type, typeIn, popIn, fadeOut, T0, D, P0, P: id };
    return S;
  };

  // ------------------------------------------------------------------ layers + camera push (1.00 -> 1.04 over the scene, one eased move)
  K.layers = (P) => `<div class="k-zone" id="${P}-zone"><div class="k-cam" id="${P}-cam"></div><div class="k-ab" id="${P}-hud" style="width:1080px;height:945px"></div></div>`;
  K.cam = (S, z0 = 1, z1 = 1.04) => { const c = S.$(`${S.P}-cam`); S.I(c, { scale: z0 }); S.ft(c, { scale: z0 }, { scale: z1, duration: S.D - 0.02, ease: "sine.inOut" }, 0.005); };

  // ------------------------------------------------------------------ module header (hud)
  const mapSVG = (n) => {
    const st = [[54, 12], [92, 64], [16, 64]];
    return `<svg viewBox="0 0 108 84"><circle cx="54" cy="44" r="34" fill="none" stroke="rgba(106,223,255,.45)" stroke-width="3" stroke-dasharray="6 6"/>` +
      st.map(([x, y], i) => `<circle cx="${x}" cy="${y}" r="${i + 1 === n ? 13 : 9}" fill="${i + 1 === n ? "#01ccf7" : "rgba(12,22,64,1)"}" stroke="${i + 1 === n ? "#d6f8ff" : "rgba(106,223,255,.8)"}" stroke-width="2.5"/>` +
        `<text x="${x}" y="${y + 5}" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="${i + 1 === n ? 15 : 12}" fill="${i + 1 === n ? "#0b1440" : "#e3edfa"}">${i + 1}</text>`).join("") + `</svg>`;
  };
  K.headerHTML = (P, n) => {
    const m = K.MOD[n - 1];
    return `<div class="k-ab" id="${P}-hdr" style="width:1080px;height:945px"><div class="k-hplate" id="${P}-hplate"></div><div class="k-hglow" id="${P}-hglow"></div>` +
      `<div class="k-hnum" id="${P}-hnum">${n}</div><div class="k-hk" id="${P}-hk">MODUL ${n} DARI 3</div><div class="k-hname" id="${P}-hn">${m.name}</div>` +
      `<div class="k-hsub" id="${P}-hs">${m.sub}</div><div class="k-map" id="${P}-map">${mapSVG(n)}</div></div>`;
  };
  // header builds in at local time t: plate grows out of a cyan flood rect (the previous scene's button/flood) or scales up
  K.headerIn = (S, t, fromFlood) => {
    const { I, ft, $, P } = S;
    const pl = $(`${P}-hplate`), gl = $(`${P}-hglow`);
    if (fromFlood) {
      I(pl, { opacity: 0 }); ft(pl, { opacity: 0 }, { opacity: 1, duration: 0.2 }, t + 0.25);
    } else {
      I(pl, { scale: 0.94, opacity: 0, transformOrigin: "50% 50%" }); ft(pl, { scale: 0.94, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.34, ease: "power3.out" }, t);
    }
    S.popIn($(`${P}-hnum`), t + 0.1, 0.3);
    [[`${P}-hk`, 0.16], [`${P}-hn`, 0.2], [`${P}-hs`, 0.28]].forEach(([id, dt]) => { I($(id), { y: 22, opacity: 0 }); ft($(id), { y: 22, opacity: 0 }, { y: 0, opacity: id.endsWith("hs") ? 0.82 : 1, duration: 0.4, ease: "power3.out" }, t + dt); });
    S.popIn($(`${P}-map`), t + 0.3, 0.5);
    I(gl, { opacity: 0 }); ft(gl, { opacity: 0 }, { opacity: 1, duration: 0.14 }, t + 0.3); ft(gl, { opacity: 1 }, { opacity: 0, duration: 0.5, ease: "power2.inOut" }, t + 0.46);
  };
  K.headerOut = (S, t) => S.fadeOut(S.$(`${S.P}-hdr`), t, 0.24);
  // the cyan flood rect that a pressed button grows into (end of one scene) and that contracts into the next header (start of next)
  K.FLOOD = { x: 30, y: 316, w: 1020, h: 620 };
  // start of a module scene: the flood rect (identical to the previous scene's last frame) contracts into the header plate
  K.floodToHeader = (S, t = 0.02, dur = 0.45) => {
    const fl = S.$(`${S.P}-flood`), F = K.FLOOD;
    S.I(fl, { left: F.x, top: F.y, width: F.w, height: F.h, borderRadius: 34, opacity: 1 });
    S.ft(fl, { left: F.x, top: F.y, width: F.w, height: F.h, borderRadius: 34 }, { left: 60, top: 330, width: 960, height: 112, borderRadius: 30, duration: dur, ease: "power3.inOut" }, t);
    S.ft(fl, { opacity: 1 }, { opacity: 0, duration: 0.25, ease: "power2.in" }, t + dur - 0.05);
  };
  // end of a scene: the accent dot at (x, y) floods the FLOOD rect (circle scales past all four corners in ~0.35 s)
  K.dfHTML = (P) => `<div class="k-ab" id="${P}-df" style="left:${K.FLOOD.x}px;top:${K.FLOOD.y}px;width:${K.FLOOD.w}px;height:${K.FLOOD.h}px;border-radius:34px;overflow:hidden">` +
    `<div id="${P}-dfc" style="position:absolute;left:0;top:0;width:100px;height:100px;margin:-50px 0 0 -50px;border-radius:50px;background:linear-gradient(180deg,#8cebff,#01ccf7 60%,#0aa7d6)"></div></div>`;
  K.dotFlood = (S, x, y, t) => {
    const F = K.FLOOD, c = S.$(`${S.P}-dfc`), df = S.$(`${S.P}-df`);
    const lx = x - F.x, ly = y - F.y, R = Math.max(...[[0, 0], [F.w, 0], [0, F.h], [F.w, F.h]].map(([a, b]) => Math.hypot(a - lx, b - ly)));
    S.I(df, { opacity: 0 }); S.tl.set(df, { opacity: 1 }, t);
    S.I(c, { x: lx, y: ly, scale: 0.3 });
    S.ft(c, { scale: 0.3 }, { scale: (2 * R) / 100 + 0.2, duration: 0.36, ease: "power2.in" }, t);
  };
  K.floodHTML = (P) => `<div class="k-ab" id="${P}-flood" style="border-radius:34px;background:linear-gradient(180deg,#8cebff,#01ccf7 60%,#0aa7d6)"></div>`;

  // ------------------------------------------------------------------ 3D logo sprites
  K.logoHTML = (id, name, size) =>
    `<div class="k-lg" id="${id}" style="width:${size}px;height:${size}px;background-image:url(assets/logos3d/${name}.png);background-size:${size * 6}px ${size * 6}px"></div>` +
    `<img class="k-pre" src="assets/logos3d/${name}.png" alt="">`;
  const bp = (i, size) => { i = ((Math.round(i) % 36) + 36) % 36; return `${-(i % 6) * size}px ${-Math.floor(i / 6) * size}px`; };
  // angle(t) in degrees (local time) sampled at 20 Hz between t0 and t1
  K.logoTurn = (S, el, size, t0, t1, angle) => {
    S.I(el, { backgroundPosition: bp(angle(t0) / 10, size) });
    for (let t = t0; t <= t1 + 1e-6; t += 0.05) S.tl.set(el, { backgroundPosition: bp(angle(t) / 10, size) }, t);
  };
  // sway around the front (+-amp deg) with optional full spins at given times (each spin 0.9 s, eased)
  K.logoLive = (S, el, size, t0, t1, spins = [], amp = 24, per = 3.2, ph = 0) => {
    const e = (u) => (u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2);
    K.logoTurn(S, el, size, t0, t1, (t) => {
      let a = amp * Math.sin((2 * Math.PI * (t + ph)) / per);
      for (const s of spins) if (t >= s) a += 360 * e(Math.min(1, (t - s) / 0.9));
      return a;
    });
  };

  // ------------------------------------------------------------------ org markup (identical in every scene that shows it)
  K.CH = [["trending-up", "Cari tren"], ["pen-line", "Nulis caption"], ["palette", "Bikin desain"], ["mic", "Isi suara"], ["send", "Posting"],
    ["message-circle", "Balas komen"], ["chart-column", "Cek angka"]];
  K.MODN = [["Riset &amp; konten", [0, 1]], ["Kreatif &amp; distribusi", [2, 3, 4, 5]], ["Putaran analitik", [6]]];
  K.boxHTML = (P, i) => `<div class="k-box" id="${P}-bx${i}"><div class="nm">${i + 1}</div><div class="ai">${K.svg("bot")}TIM AI</div><b>${K.MODN[i][0]}</b>` +
    `<div class="ics">${K.MODN[i][1].map((c) => `<i id="${P}-bi${c}">${K.svg(K.CH[c][0])}</i>`).join("")}</div></div>`;
  K.bossHTML = (P, sub = "bos tim marketing") => `<div class="k-boss" id="${P}-boss"><div class="k-ic">${K.svg("crown")}</div><b>Kamu</b><span>${sub}</span></div>`;
  K.linesHTML = (P) => `<svg class="k-ab" id="${P}-lines" viewBox="0 0 1080 945" style="width:1080px;height:945px;overflow:visible">` + K.BOX.map((b, i) => `<path id="${P}-ln${i}" d="M540 528 C540 610 ${b.x} 600 ${b.x} ${b.y - 100}" fill="none" stroke="#01ccf7" stroke-width="4" stroke-linecap="round" stroke-dasharray="6 10"/>`).join("") + `</svg>`;

  // our own example illustration (kedai kopi, CONTOH): a cup with steam on a navy plate
  K.cupSVG = (w = 80, h = 100) => `<svg viewBox="0 0 80 100" style="width:${w}px;height:${h}px"><path d="M14 30 H66 L60 92 Q59 98 52 98 H28 Q21 98 20 92 Z" fill="#ffffff"/><path d="M17 44 H63 L60 74 H20 Z" fill="#c98a52"/>` +
    `<rect x="10" y="22" width="60" height="10" rx="4" fill="#e3edfa"/><path d="M30 14 Q34 6 30 0 M42 14 Q46 6 42 0 M54 14 Q58 6 54 0" stroke="#6adfff" stroke-width="3" fill="none" stroke-linecap="round"/></svg>`;

  // ------------------------------------------------------------------ small helpers
  K.dotHTML = (P, id = "dot") => `<div class="k-dot" id="${P}-${id}"></div>`;
  K.btnHTML = (id, label, ic = "check") => `<div class="k-btn" id="${id}">${K.svg(ic)}${label}</div>`;
  K.chipHTML = (id, ic, label, on) => `<div class="k-chip${on ? " on" : ""}" id="${id}">${K.svg(ic)}${label}</div>`;
  K.at = (S, el, x, y, extra) => S.I(el, Object.assign({ x, y, xPercent: -50, yPercent: -50 }, extra || {}));
  // an arc flight from (x0,y0) to (x1,y1) with lift h (keyframes on x/y, eased)
  K.fly = (S, el, a, b, t, dur = 0.5, h = 80, extra0 = {}, extra1 = {}) => {
    const n = 8, kf = [];
    for (let i = 1; i <= n; i++) { const u = i / n; kf.push({ x: a[0] + (b[0] - a[0]) * u, y: a[1] + (b[1] - a[1]) * u - h * Math.sin(Math.PI * u), duration: dur / n, ease: "none" }); }
    S.tl.to(el, { keyframes: kf, ease: "power2.inOut" }, t);
    if (Object.keys(extra1).length) S.ft(el, extra0, Object.assign({ duration: dur, ease: "power2.inOut" }, extra1), t);
  };
})();

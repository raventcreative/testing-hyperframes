// AIP R2 ORKESTRATOR — shared visual kit (loaded in index.html <head>, before the compositions):
//   window.R2.TOOLS   the 4 verified projects (names + repo paths as TEXT only, no third-party logos)
//   window.R2.ic()    lucide icon (ISC) as a CSS-mask <i>, tinted by `background`
//   window.R2.rail*   the 4-pill TOOL RAIL shared by s01 · t1–t4 · s06 (exact same geometry everywhere → invisible cuts)
//   window.R2.card*   the white app-card header used by t1–t4
// RAIL SPEC: 4 pills 200×56 (radius 28) at y 312, x = 124 + i·212 (124, 336, 548, 760 → right edge 960).
//   state 0 upcoming = white, number + grey skeleton bar · 1 active = navy gradient, white name, soft ring · 2 done = white, green check + name.
(function () {
  const TOOLS = [
    { name: "OpenHands", title: "OpenHands Agent Canvas", repo: "OpenHands/OpenHands", icon: "layout-dashboard" },
    { name: "Paperclip", title: "Paperclip", repo: "paperclipai/paperclip", icon: "building-2" },
    { name: "Orca", title: "Orca", repo: "stablyai/orca", icon: "workflow" },
    { name: "TeamAI", title: "TeamAI", repo: "Tencent/teamai-cli", icon: "folder-git-2" },
  ];
  const ic = (name, size, color, style) =>
    `<i class="rk-ic" style="width:${size}px;height:${size}px;background:${color};-webkit-mask-image:url(assets/icons/lucide-${name}.svg);mask-image:url(assets/icons/lucide-${name}.svg);${style || ""}"></i>`;
  const CHECK = (w, col) => `<svg width="${w}" height="${w}" viewBox="0 0 24 24" fill="none" stroke="${col || "#fff"}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 12.5l5 5L19.5 7"/></svg>`;
  const CSS = `
  .rk-a { position: absolute; }
  .rk-g { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; white-space: nowrap; }
  .rk-ic { display: block; flex: none; -webkit-mask-size: contain; mask-size: contain; -webkit-mask-repeat: no-repeat; mask-repeat: no-repeat; -webkit-mask-position: center; mask-position: center; }
  .rk-nav { background: linear-gradient(135deg, #0a0d2c, #294b77); }
  /* ---- TOOL RAIL */
  .rk-pill { position: absolute; top: 312px; width: 200px; height: 56px; transform-origin: 50% 50%; }
  .rk-pl { position: absolute; left: 0; top: 0; width: 200px; height: 56px; border-radius: 28px; overflow: hidden; }
  .rk-pu { background: #ffffff; box-shadow: inset 0 0 0 1.5px #d5e0f0, 0 12px 22px -16px rgba(10,13,44,.45); }
  .rk-pa { background: linear-gradient(135deg, #0a0d2c, #294b77); box-shadow: 0 0 0 7px rgba(41,75,119,.15), 0 16px 26px -14px rgba(10,13,44,.65); overflow: visible; }
  .rk-pd { background: #ffffff; box-shadow: inset 0 0 0 1.5px #bfe5c9, 0 12px 22px -16px rgba(10,13,44,.4); }
  .rk-pn { position: absolute; left: 10px; top: 10px; width: 36px; height: 36px; border-radius: 50%; text-align: center; font: 700 18px/36px Poppins, sans-serif; }
  .rk-pu .rk-pn { background: #eef3fb; color: #294b77; }
  .rk-pa .rk-pn { background: #ffffff; color: #0a0d2c; }
  .rk-pd .rk-pn { background: #2da44e; }
  .rk-pd .rk-pn svg { position: absolute; left: 8px; top: 8px; }
  .rk-sk { position: absolute; left: 58px; top: 23px; width: 104px; height: 10px; border-radius: 5px; background: #e3e9f4; }
  .rk-pt { position: absolute; left: 56px; top: 0; font: 700 21px/56px Poppins, sans-serif; letter-spacing: -0.01em; white-space: nowrap; }
  .rk-pa .rk-pt { color: #ffffff; }
  .rk-pd .rk-pt { color: #294b77; }
  /* ---- APP CARD (t1–t4): x 70–1010, y 392–930 */
  .rk-card { position: absolute; left: 70px; top: 392px; width: 940px; height: 538px; transform-origin: 50% 50%; }
  .rk-cbg { position: absolute; left: 0; top: 0; width: 940px; height: 538px; border-radius: 32px; background: linear-gradient(180deg, #ffffff, #f6f8fd);
    box-shadow: 0 40px 70px -36px rgba(10,13,44,.5), 0 0 0 1.5px rgba(10,13,44,.06); }
  .rk-hic { position: absolute; left: 28px; top: 24px; width: 66px; height: 66px; border-radius: 20px; background: linear-gradient(135deg, #0a0d2c, #294b77); box-shadow: 0 12px 22px -10px rgba(10,13,44,.6); }
  .rk-hic .rk-ic { position: absolute; left: 16px; top: 16px; }
  .rk-htw { position: absolute; left: 112px; top: 18px; height: 50px; overflow: hidden; }
  .rk-ht { position: relative; font: 700 37px/50px Poppins, sans-serif; letter-spacing: -0.015em; }
  .rk-hr { position: absolute; left: 113px; top: 66px; height: 28px; display: flex; align-items: center; gap: 8px; font: 400 19px/28px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .rk-hos { position: absolute; right: 28px; top: 34px; height: 40px; padding: 0 18px 0 42px; border-radius: 20px; background: #e9f7ee; box-shadow: inset 0 0 0 1.5px #bfe5c9;
    font: 700 16px/40px Poppins, sans-serif; color: #17733a; white-space: nowrap; letter-spacing: .02em; }
  .rk-hos .rk-ic { position: absolute; left: 14px; top: 10px; }
  .rk-hdv { position: absolute; left: 28px; right: 28px; top: 112px; height: 2px; background: #e9eef7; }
  `;
  const st = document.createElement("style"); st.textContent = CSS; document.head.appendChild(st);

  // ---------------------------------------------------------------- RAIL
  function railHTML(px) {
    return TOOLS.map((T, i) => `<div class="rk-pill" id="${px}-p${i}" style="left:${124 + i * 212}px">` +
      `<div class="rk-pl rk-pu" id="${px}-p${i}u"><div class="rk-pn">${i + 1}</div><i class="rk-sk"></i></div>` +
      `<div class="rk-pl rk-pd" id="${px}-p${i}d"><div class="rk-pn">${CHECK(20)}</div><div class="rk-pt">${T.name}</div></div>` +
      `<div class="rk-pl rk-pa" id="${px}-p${i}a"><div class="rk-pn">${i + 1}</div><div class="rk-pt" id="${px}-p${i}t">${T.name}</div></div></div>`).join("");
  }
  // pin every pill's start state at t = 0 (states: array of 0/1/2; opacity of the whole rail via `vis`)
  function railInit(tl, px, states) {
    states.forEach((s, i) => {
      tl.set(`#${px}-p${i}`, { scaleX: 1, scaleY: 1, y: 0, x: 0, opacity: 1, rotation: 0 }, 0);
      tl.set(`#${px}-p${i}u`, { opacity: s === 0 ? 1 : 0 }, 0);
      tl.set(`#${px}-p${i}a`, { opacity: s === 1 ? 1 : 0 }, 0);
      tl.set(`#${px}-p${i}d`, { opacity: s === 2 ? 1 : 0 }, 0);
      tl.set(`#${px}-p${i}t`, { clipPath: "inset(0px 0px 0px 0px)" }, 0);
    });
  }
  // upcoming → active on the spoken number; the name wipes in on the spoken name
  function railActivate(tl, px, i, t, tName) {
    const p = `#${px}-p${i}`;
    tl.fromTo(p + "a", { opacity: 0 }, { opacity: 1, duration: 0.16, ease: "power1.out", immediateRender: false }, t);
    tl.set(p + "u", { opacity: 0 }, t + 0.16);
    tl.fromTo(p, { scaleX: 1, scaleY: 1 }, { scaleX: 1.12, scaleY: 1.12, duration: 0.13, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, t);
    tl.set(p + "t", { clipPath: "inset(0px 140px 0px 0px)" }, 0);
    tl.fromTo(p + "t", { clipPath: "inset(0px 140px 0px 0px)" }, { clipPath: "inset(0px 0px 0px 0px)", duration: 0.32, ease: "power2.out", immediateRender: false }, Math.max(t + 0.05, tName - 0.08));
  }
  // active → done (check) near the end of a tool's scene
  function railDone(tl, px, i, t) {
    const p = `#${px}-p${i}`;
    tl.fromTo(p + "d", { opacity: 0 }, { opacity: 1, duration: 0.18, ease: "power1.out", immediateRender: false }, t);
    tl.fromTo(p + "a", { opacity: 1 }, { opacity: 0, duration: 0.18, ease: "power1.in", immediateRender: false }, t + 0.04);
    tl.fromTo(p, { scaleX: 1, scaleY: 1 }, { scaleX: 1.08, scaleY: 1.08, duration: 0.1, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, t);
  }
  // ---------------------------------------------------------------- APP CARD header (t1–t4)
  function cardHeadHTML(px, k, sub) {
    const T = TOOLS[k];
    return `<div class="rk-cbg"></div><div class="rk-hic" id="${px}-hic">${ic(T.icon, 34, "#ffffff")}</div>` +
      `<div class="rk-htw"><div class="rk-ht rk-g" id="${px}-ht">${T.title}</div></div>` +
      `<div class="rk-hr" id="${px}-hr">${ic("folder-git-2", 20, "#8293b0")}<span>github.com/${T.repo}</span>${sub ? `<span style="color:#b3bfd3">·</span><span>${sub}</span>` : ""}</div>` +
      `<div class="rk-hos" id="${px}-hos">${ic("badge-check", 20, "#2da44e")}open source</div><div class="rk-hdv"></div>`;
  }
  window.R2 = { TOOLS, ic, CHECK, railHTML, railInit, railActivate, railDone, cardHeadHTML };
})();

// Shared visual system of the REMOTE reel ("Tim 3 Claude cari kerja remote"), loaded in <head> before every scene.
// Icons: lucide (ISC), inlined so they can be coloured with currentColor. Claude mark: assets/icons/lobe-claude-color.svg (lobehub, MIT).
// - R4.M      : the 3 Claude team members (name, role, colour, icon)
// - R4.RAIL   : the TEAM RAIL (3 member chips, y 312–396) shared by s03 (end) · s04 · s05 · s06 · s07 (start) — same spot in every scene
// - R4.JOBS   : the illustrative example listings (labelled "contoh" wherever they are shown; no real companies, no job-site logos)
// - R4.chip(p, i) : HTML of member chip i with ids  p-c{i} (chip) · p-c{i}g (active ring) · p-c{i}d (ready dot) · p-c{i}s (spinner)
//                  · p-c{i}k (done check)
(function () {
  const ICO = {
    search: '<path d="m21 21-4.34-4.34"/><circle cx="11" cy="11" r="8"/>',
    funnel: '<path d="M10 20a1 1 0 0 0 .553.895l2 1A1 1 0 0 0 14 21v-7a2 2 0 0 1 .517-1.341L21.74 4.67A1 1 0 0 0 21 3H3a1 1 0 0 0-.742 1.67l7.225 7.989A2 2 0 0 1 10 14z"/>',
    fileText: '<path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/><path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    filePen: '<path d="M12.659 22H18a2 2 0 0 0 2-2V8a2.4 2.4 0 0 0-.706-1.706l-3.588-3.588A2.4 2.4 0 0 0 14 2H6a2 2 0 0 0-2 2v9.34"/><path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="M10.378 12.622a1 1 0 0 1 3 3.003L8.36 20.637a2 2 0 0 1-.854.506l-2.867.837a.5.5 0 0 1-.62-.62l.836-2.869a2 2 0 0 1 .506-.853z"/>',
    brief: '<path d="M12 12h.01"/><path d="M16 6V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><path d="M22 13a18.15 18.15 0 0 1-20 0"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
    globe: '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
    laptop: '<path d="M18 5a2 2 0 0 1 2 2v8.526a2 2 0 0 0 .212.897l1.068 2.127a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45l1.068-2.127A2 2 0 0 0 4 15.526V7a2 2 0 0 1 2-2z"/><path d="M20.054 15.987H3.946"/>',
    battery: '<path d="M22 14v-4"/><rect x="2" y="6" width="16" height="12" rx="2"/>',
    inbox: '<polyline points="22 12 16 12 14 15 10 15 8 12 2 12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/>',
    send: '<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/>',
    pointer: '<path d="M4.037 4.688a.495.495 0 0 1 .651-.651l16 6.5a.5.5 0 0 1-.063.947l-6.124 1.58a2 2 0 0 0-1.438 1.435l-1.579 6.126a.5.5 0 0 1-.947.063z"/>',
    check: '<path d="M20 6 9 17l-5-5"/>',
    x: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    shieldAlert: '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="M12 8v4"/><path d="M12 16h.01"/>',
    userCheck: '<path d="m16 11 2 2 4-4"/><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>',
    pin: '<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
    trash: '<path d="M10 11v6"/><path d="M14 11v6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"/><path d="M3 6h18"/><path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>',
    eye: '<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>',
    star: '<path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"/>',
    board: '<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
    terminal: '<path d="M12 19h8"/><path d="m4 17 6-6-6-6"/>',
    enter: '<path d="M20 4v7a4 4 0 0 1-4 4H4"/><path d="m9 10-5 5 5 5"/>',
    loader: '<path d="M21 12a9 9 0 1 1-6.219-8.56"/>',
    spark: '<path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/>',
    out: '<path d="M7 7h10v10"/><path d="M7 17 17 7"/>',
    badge: '<path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"/><path d="m16 9-5.5 5.5L8 12"/>',
    house: '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-6a2 2 0 0 1 2.582 0l7 6A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    user: '<circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/>',
    heart: '<path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5"/>',
    msg: '<path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/>',
    clock: '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    plus: '<path d="M5 12h14"/><path d="M12 5v14"/>',
  };
  const svg = (k, sw, cls) => `<svg class="${cls || ""}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[k]}</svg>`;
  const M = [
    { n: "Claude 1", r: "Pencari", job: "Cari lowongan", c: "#3a6fe0", d: "#2a57c2", soft: "#e8effd", ic: "search" },
    { n: "Claude 2", r: "Penyaring", job: "Saring yang cocok", c: "#7c5cff", d: "#6141e8", soft: "#efebff", ic: "funnel" },
    { n: "Claude 3", r: "Penulis CV", job: "CV & cover letter", c: "#294b77", d: "#1c3658", soft: "#e7edf6", ic: "filePen" },
  ];
  const RAIL = { top: 312, w: 258, h: 84, left: [141, 411, 681] };
  // example listings (illustrative only): t title, m meta, k = fail reason key (null = passes), L initial, c colour
  const JOBS = [
    { t: "Frontend Developer", m: "Startup SaaS · Remote global", L: "F", c: "#3a6fe0", k: null, s: 92 },
    { t: "Senior Accountant", m: "Wajib lisensi CPA", L: "A", c: "#8a97ad", k: "skill" },
    { t: "React Developer", m: "Agensi digital · Remote APAC", L: "R", c: "#2da44e", k: null, s: 88 },
    { t: "Data Engineer", m: "Remote · khusus warga AS", L: "D", c: "#7c5cff", k: "id" },
    { t: "Admin Online", m: "Bayar biaya daftar dulu", L: "?", c: "#e5484d", k: "scam" },
    { t: "UI Engineer", m: "E-commerce · Remote Asia", L: "U", c: "#f4b400", k: null, s: 81 },
  ];
  const chip = (p, i) => {
    const m = M[i], x = RAIL.left[i];
    return `<div class="r4-chip" id="${p}-c${i}" style="left:${x}px;top:${RAIL.top}px;--c:${m.c}">` +
      `<div class="bg"></div><div class="rg" id="${p}-c${i}g"></div>` +
      `<div class="av" id="${p}-c${i}v"><i></i></div><div class="bd">${svg(m.ic, 2.4)}</div>` +
      `<b class="nm">${m.n}</b><span class="rl">${m.r}</span>` +
      `<i class="dt" id="${p}-c${i}d"></i><div class="sp" id="${p}-c${i}s">${svg("loader", 3)}</div>` +
      `<div class="ok" id="${p}-c${i}k">${svg("check", 3.4)}</div></div>`;
  };
  const css = `
  .r4-chip { position: absolute; width: 258px; height: 84px; transform-origin: 50% 50%; font-family: Poppins, sans-serif; }
  .r4-chip .bg { position: absolute; inset: 0; border-radius: 24px; background: linear-gradient(180deg, #ffffff, #f6f8fd);
    box-shadow: 0 18px 34px -20px rgba(10,13,44,.45), 0 0 0 1.5px rgba(10,13,44,.06); }
  .r4-chip .rg { position: absolute; left: -4px; top: -4px; right: -4px; bottom: -4px; border-radius: 28px; box-shadow: 0 0 0 3px var(--c), 0 10px 28px -6px var(--c); opacity: 0; }
  .r4-chip .av { position: absolute; left: 14px; top: 14px; width: 56px; height: 56px; border-radius: 50%; background: #ffffff;
    box-shadow: inset 0 0 0 3px var(--c), 0 6px 12px -8px rgba(10,13,44,.5); }
  .r4-chip .av i { position: absolute; left: 13px; top: 13px; width: 30px; height: 30px; background: url(assets/icons/lobe-claude-color.svg) center / contain no-repeat; }
  .r4-chip .bd { position: absolute; left: 50px; top: 50px; width: 26px; height: 26px; border-radius: 50%; background: var(--c); color: #ffffff; box-shadow: 0 0 0 2.5px #ffffff; }
  .r4-chip .bd svg { position: absolute; left: 6px; top: 6px; width: 14px; height: 14px; display: block; }
  .r4-chip .nm { position: absolute; left: 86px; top: 15px; font: 700 22px/28px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .r4-chip .rl { position: absolute; left: 86px; top: 44px; font: 400 17px/24px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .r4-chip .dt { position: absolute; left: 224px; top: 35px; width: 14px; height: 14px; border-radius: 50%; background: var(--c); box-shadow: 0 0 0 5px rgba(255,255,255,1), 0 0 0 7px #e3eaf5; }
  .r4-chip .sp { position: absolute; left: 216px; top: 28px; width: 28px; height: 28px; color: var(--c); opacity: 0; transform-origin: 50% 50%; }
  .r4-chip .sp svg, .r4-chip .ok svg { display: block; }
  .r4-chip .ok { position: absolute; left: 214px; top: 27px; width: 30px; height: 30px; border-radius: 50%; background: #2da44e; color: #ffffff; opacity: 0; box-shadow: 0 6px 12px -6px rgba(45,164,78,.9); }
  .r4-chip .ok svg { position: absolute; left: 6px; top: 6px; width: 18px; height: 18px; }
  .r4-job { position: absolute; width: 420px; height: 76px; transform-origin: 50% 50%; font-family: Poppins, sans-serif; }
  .r4-job .jb { position: absolute; inset: 0; border-radius: 20px; background: linear-gradient(180deg, #ffffff, #f7f9fd); box-shadow: 0 16px 28px -18px rgba(10,13,44,.5), 0 0 0 1.5px rgba(10,13,44,.06); }
  .r4-job .jl { position: absolute; left: 14px; top: 14px; width: 48px; height: 48px; border-radius: 14px; background: var(--jc); color: #ffffff; font: 700 24px/48px Poppins, sans-serif; text-align: center; }
  .r4-job .jt { position: absolute; left: 76px; top: 12px; font: 700 21px/28px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .r4-job .jm { position: absolute; left: 76px; top: 40px; font: 400 16px/22px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .r4-grad { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  `;
  const job = (id, j, x, y) => `<div class="r4-job" id="${id}" style="left:${x}px;top:${y}px;--jc:${j.c}"><div class="jb"></div><div class="jl">${j.L}</div><b class="jt">${j.t}</b><span class="jm">${j.m}</span></div>`;
  // ---------------------------------------------------------------- THE JOB BOARD (s07 · s08 · s09): one local page Claude builds
  // Absolute frame: left 70, top 316, 940 × 614 (bottom 930). ids: p-bd (frame) · p-bt (title) · p-bpv ("Pribadi" chip) · p-bav{0..2}
  // (team avatars) · p-bf{0..2} (filter chips) · p-br{q} (row) · p-brg{q} (row ring arc) · p-bap{q} (Apply button) · p-bhl{q} (row
  // highlight) · p-bbest ("Paling cocok" badge on row 0) · p-baddr (address pill).
  const BOARD = { x: 70, y: 316, w: 940, h: 614, rowY: (q) => 222 + q * 112 };
  const ROWS = [{ k: 0, org: "Startup SaaS · Remote global" }, { k: 2, org: "Agensi digital · Remote APAC" }, { k: 5, org: "E-commerce · Remote Asia" }];
  const board = (p) => {
    let h = `<div class="r4-bd" id="${p}-bd"><div class="bb"></div><div class="dots"><i></i><i></i><i></i></div>` +
      `<div class="ad" id="${p}-baddr">${svg("fileText", 2)}<span>papan-loker.html</span></div><div class="ex">DATA CONTOH</div>` +
      `<div class="hi">${svg("board", 2.2)}</div><div class="tt r4-grad" id="${p}-bt">Papan Loker Remote-ku</div>` +
      `<div class="pv" id="${p}-bpv">${svg("user", 2.4)}Pribadi</div><div class="st">lolos saring · CV & cover letter siap</div>` +
      M.map((m, i) => `<div class="av" id="${p}-bav${i}" style="left:${776 + i * 40}px;--c:${m.c}"><i></i></div>`).join("") +
      [["globe", "Remote"], ["pin", "Bisa dari Indonesia"], ["userCheck", "Cocok sama skill"]].map((f, i) =>
        `<div class="fc" id="${p}-bf${i}" style="left:${[24, 160, 404][i]}px">${svg(f[0], 2.2)}${f[1]}</div>`).join("");
    ROWS.forEach((r, q) => {
      const j = JOBS[r.k], C = 2 * Math.PI * 26, col = j.s >= 85 ? "#2da44e" : "#f4b400";
      h += `<div class="rw" id="${p}-br${q}" style="top:${BOARD.rowY(q)}px"><i class="hl" id="${p}-bhl${q}"></i>` +
        `<svg class="rg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="26" fill="none" stroke="#e6ecf6" stroke-width="6"/>` +
        `<circle id="${p}-brg${q}" cx="32" cy="32" r="26" fill="none" stroke="${col}" stroke-width="6" stroke-linecap="round" stroke-dasharray="${C.toFixed(2)} ${C.toFixed(2)}" stroke-dashoffset="${(C * (1 - j.s / 100)).toFixed(2)}" transform="rotate(-90 32 32)"/></svg>` +
        `<b class="sc">${j.s}%</b><b class="t">${j.t}</b><span class="m">${r.org}</span>` +
        `<div class="dc" style="left:470px">${svg("check", 3)}CV</div><div class="dc" style="left:566px">${svg("check", 3)}Cover letter</div>` +
        `<div class="ap" id="${p}-bap${q}">Apply${svg("out", 2.6)}</div>` +
        (q === 0 ? `<div class="best" id="${p}-bbest">${svg("star", 2.2)}Paling cocok</div>` : "") + `</div>`;
    });
    return h + `</div>`;
  };
  const bcss = `
  .r4-bd { position: absolute; left: 70px; top: 316px; width: 940px; height: 614px; border-radius: 32px; transform-origin: 50% 50%; font-family: Poppins, sans-serif;
    background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 50px 90px -40px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); }
  .r4-bd .bb { position: absolute; left: 0; top: 0; width: 940px; height: 58px; border-radius: 32px 32px 0 0; background: #eef2f9; }
  .r4-bd .dots { position: absolute; left: 26px; top: 23px; display: flex; gap: 9px; }
  .r4-bd .dots i { display: block; width: 12px; height: 12px; border-radius: 50%; background: #c9d4e6; }
  .r4-bd .ad { position: absolute; left: 100px; top: 11px; width: 400px; height: 36px; border-radius: 18px; background: #ffffff; box-shadow: inset 0 0 0 1.5px #d9e2f0; transform-origin: 50% 50%; }
  .r4-bd .ad svg { position: absolute; left: 14px; top: 8px; width: 20px; height: 20px; color: #5d6f8f; display: block; }
  .r4-bd .ad span { position: absolute; left: 44px; top: 0; font: 400 17px/36px Poppins, sans-serif; color: #294b77; white-space: nowrap; }
  .r4-bd .ex { position: absolute; right: 24px; top: 14px; height: 30px; padding: 0 14px; border-radius: 15px; background: #ffffff; box-shadow: inset 0 0 0 1.5px #d9e2f0;
    font: 700 13px/30px Poppins, sans-serif; letter-spacing: .14em; color: #8a97ad; white-space: nowrap; }
  .r4-bd .hi { position: absolute; left: 24px; top: 78px; width: 56px; height: 56px; border-radius: 17px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #fff; box-shadow: 0 10px 18px -10px rgba(10,13,44,.8); }
  .r4-bd .hi svg { position: absolute; left: 14px; top: 14px; width: 28px; height: 28px; display: block; }
  .r4-bd .tt { position: absolute; left: 96px; top: 72px; font: 700 32px/40px Poppins, sans-serif; white-space: nowrap; letter-spacing: -.01em; }
  .r4-bd .pv { position: absolute; left: 524px; top: 78px; height: 32px; padding: 0 14px 0 38px; border-radius: 16px; background: #294b77; color: #ffffff;
    font: 700 15px/32px Poppins, sans-serif; white-space: nowrap; transform-origin: 50% 50%; }
  .r4-bd .pv svg { position: absolute; left: 13px; top: 7px; width: 18px; height: 18px; display: block; }
  .r4-bd .st { position: absolute; left: 97px; top: 112px; font: 400 17px/24px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .r4-bd .av { position: absolute; top: 82px; width: 50px; height: 50px; border-radius: 50%; background: #ffffff; box-shadow: inset 0 0 0 3px var(--c), 0 0 0 3px #ffffff, 0 6px 12px -6px rgba(10,13,44,.5); }
  .r4-bd .av i { position: absolute; left: 12px; top: 12px; width: 26px; height: 26px; background: url(assets/icons/lobe-claude-color.svg) center / contain no-repeat; }
  .r4-bd .fc { position: absolute; top: 158px; height: 42px; padding: 0 16px 0 44px; border-radius: 21px; background: #eaf7ee; color: #218a3e; font: 700 16px/42px Poppins, sans-serif; white-space: nowrap; }
  .r4-bd .fc svg { position: absolute; left: 15px; top: 11px; width: 20px; height: 20px; display: block; }
  .r4-bd .rw { position: absolute; left: 24px; width: 892px; height: 100px; border-radius: 22px; background: #ffffff; box-shadow: 0 12px 22px -18px rgba(10,13,44,.5), 0 0 0 1.5px #e3eaf5; transform-origin: 50% 50%; }
  .r4-bd .rw .hl { position: absolute; left: -3px; top: -3px; right: -3px; bottom: -3px; border-radius: 25px; box-shadow: 0 0 0 3px #f4b400, 0 14px 30px -10px rgba(244,180,0,.55); opacity: 0; }
  .r4-bd .rw .rg { position: absolute; left: 18px; top: 18px; width: 64px; height: 64px; }
  .r4-bd .rw .sc { position: absolute; left: 18px; top: 18px; width: 64px; font: 700 17px/64px Poppins, sans-serif; color: #0a0d2c; text-align: center; }
  .r4-bd .rw .t { position: absolute; left: 100px; top: 20px; font: 700 22px/30px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .r4-bd .rw .m { position: absolute; left: 100px; top: 52px; font: 400 16px/24px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .r4-bd .rw .dc { position: absolute; top: 30px; height: 40px; padding: 0 14px 0 36px; border-radius: 20px; background: #eaf7ee; color: #218a3e; font: 700 15px/40px Poppins, sans-serif; white-space: nowrap; }
  .r4-bd .rw .dc svg { position: absolute; left: 13px; top: 11px; width: 17px; height: 17px; display: block; }
  .r4-bd .rw .ap { position: absolute; left: 730px; top: 24px; width: 144px; height: 52px; border-radius: 26px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff;
    font: 700 19px/52px Poppins, sans-serif; text-align: center; white-space: nowrap; box-shadow: 0 12px 20px -12px rgba(10,13,44,.75); transform-origin: 50% 50%; }
  .r4-bd .rw .ap svg { display: inline-block; width: 18px; height: 18px; margin-left: 6px; vertical-align: -2px; }
  .r4-bd .rw .best { position: absolute; left: 92px; top: -16px; height: 32px; padding: 0 14px 0 36px; border-radius: 16px; background: #f4b400; color: #0a0d2c;
    font: 700 14px/32px Poppins, sans-serif; letter-spacing: .04em; white-space: nowrap; box-shadow: 0 8px 16px -8px rgba(217,154,0,.9); opacity: 0; transform-origin: 30% 50%; }
  .r4-bd .rw .best svg { position: absolute; left: 12px; top: 8px; width: 16px; height: 16px; display: block; }
  `;
  const st = document.createElement("style"); st.textContent = css + bcss; (document.head || document.documentElement).appendChild(st);
  // spinner angle as a pure function of GLOBAL time (so chips hand over between scenes without a jump)
  const spinAt = (g) => (g * 420) % 360;
  window.R4 = { ICO, svg, M, RAIL, JOBS, chip, job, spinAt, BOARD, ROWS, board, rail: (p) => [0, 1, 2].map((i) => chip(p, i)).join("") };
})();

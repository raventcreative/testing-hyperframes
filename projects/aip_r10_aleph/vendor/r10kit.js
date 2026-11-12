// Shared visual system of R10 "Edit video yang sudah ada pakai AI (Runway Aleph)" (LIGHT), loaded in <head> before every scene.
// Everything shown inside the player is OUR OWN ILLUSTRATION (HTML/CSS/SVG), labelled "ILUSTRASI" — no footage, no Runway branding.
// Icons: lucide (ISC), inlined so they take currentColor.
// - R10.park(p, look)      : park scene (look = day | night | sakura | snow | dusk), layered for parallax, 1100x600 scene space
// - R10.street(p, car)     : Indonesian shophouse street with an empty kerb (car = true → a parked car at the kerb)
// - R10.shelf(p, products) : plain wall shelf (products = true → a branded product line "PRODUKMU", fictitious)
// - R10.copy(p, html)      : wraps a scene as a 940x528 player copy (clip-path wipes between copies)
// - R10.player(p) / R10.prompt(p, lines) : the before/after player (frame, viewport, divider, labels) and the prompt pill
// - R10.footage(api, prefixes, t0, dur, o) : identical "camera + life" motion for every copy (copies stay pixel-aligned)
// - R10.wipe / R10.type / R10.untype      : divider wipes, prompt typing
(function () {
  const ICO = {
    sparkles: '<path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/>',
    video: '<path d="m16 13 5.223 3.482a.5.5 0 0 0 .777-.416V7.87a.5.5 0 0 0-.752-.432L16 10.5"/><rect x="2" y="6" width="14" height="12" rx="2"/>',
    videoOff: '<path d="M10.66 6H14a2 2 0 0 1 2 2v2.5l5.248-3.062A.5.5 0 0 1 22 7.87v8.196"/><path d="M16 16a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h2"/><path d="m2 2 20 20"/>',
    image: '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>',
    moveH: '<path d="m18 8 4 4-4 4"/><path d="M2 12h20"/><path d="m6 8-4 4 4 4"/>',
    arrowUp: '<path d="m5 12 7-7 7 7"/><path d="M12 19V5"/>',
    sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>',
    moon: '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>',
    flower: '<circle cx="12" cy="12" r="3"/><path d="M12 16.5A4.5 4.5 0 1 1 7.5 12 4.5 4.5 0 1 1 12 7.5a4.5 4.5 0 1 1 4.5 4.5 4.5 4.5 0 1 1-4.5 4.5"/><path d="M12 7.5V9"/><path d="M7.5 12H9"/><path d="M16.5 12H15"/><path d="M12 16.5V15"/>',
    snow: '<path d="M2 12h20"/><path d="M12 2v20"/><path d="m20 16-4-4 4-4"/><path d="m4 8 4 4-4 4"/><path d="m16 4-4 4-4-4"/><path d="m8 20 4-4 4 4"/>',
    car: '<path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/>',
    package: '<path d="M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z"/><path d="M12 22V12"/><polyline points="3.29 7 12 12 20.71 7"/><path d="m7.5 4.27 9 5.15"/>',
    upload: '<path d="M12 3v12"/><path d="m17 8-5-5-5 5"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>',
    pen: '<path d="M12 20h9"/><path d="M16.376 3.622a1 1 0 0 1 3.002 3.002L7.368 18.635a2 2 0 0 1-.855.506l-2.872.838a.5.5 0 0 1-.62-.62l.838-2.872a2 2 0 0 1 .506-.854z"/>',
    film: '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 3v18"/><path d="M3 7.5h4"/><path d="M3 12h18"/><path d="M3 16.5h4"/><path d="M17 3v18"/><path d="M17 7.5h4"/><path d="M17 16.5h4"/>',
    clapper: '<path d="M20.2 6 3 11l-.9-2.4c-.3-1.1.3-2.2 1.3-2.5l13.5-4c1.1-.3 2.2.3 2.5 1.3Z"/><path d="m6.2 5.3 3.1 3.9"/><path d="m12.4 3.4 3.1 4"/><path d="M3 11h18v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/>',
    layers: '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
    megaphone: '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
    phone: '<rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/>',
    info: '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
    coins: '<circle cx="8" cy="8" r="6"/><path d="M18.09 10.37A6 6 0 1 1 10.34 18"/><path d="M7 6h1v4"/><path d="m16.71 13.88.7.71-2.82 2.82"/>',
    lock: '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    check: '<path d="M20 6 9 17l-5-5"/>',
    circleCheck: '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    x: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    user: '<circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/>',
    msg: '<path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/>',
    send: '<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/>',
    play: '<path d="M5 5a2 2 0 0 1 3.008-1.728l11.997 6.998a2 2 0 0 1 .003 3.458l-12 7A2 2 0 0 1 5 19z"/>',
    repeat: '<path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/>',
    out: '<path d="M7 7h10v10"/><path d="M7 17 17 7"/>',
    tag: '<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r=".5" fill="currentColor"/>',
  };
  const svg = (k, sw, cls) => `<svg class="${cls || ""}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[k]}</svg>`;
  const H = (n) => { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };   // deterministic hash 0..1
  const f1 = (v) => (Math.round(v * 10) / 10).toString();
  const C = (cx, cy, r, fill, extra) => `<circle cx="${f1(cx)}" cy="${f1(cy)}" r="${f1(r)}" fill="${fill}"${extra || ""}/>`;
  const LY = (p, id, inner, style) => `<div class="r10-ly" id="${p}-${id}"${style ? ` style="${style}"` : ""}>${inner}</div>`;
  const SV = (inner) => `<svg class="r10-sv" viewBox="-40 0 1180 600" width="1180" height="600">${inner}</svg>`;
  const AX = (x) => x + 40;   // scene x → layer-local x (layers start at scene x = -40)

  // ================================================================ PARK palettes
  const PK = {
    day: { sky: "#4ea6f0 0%, #8cc9fa 46%, #d6edfe 80%, #eef8ff 100%", cloud: ["#ffffff", "#e4eefb", 0.95], hill: ["#b6d3ee", "#97c0e3"], city: "#adc9e7", win: "#d3e4f5", lit: 0,
      tl: ["#3c9156", "#4fa765", "#6cbf74"], g: "#8bd273 0%, #6dc062 40%, #4f9f4b 100%", path: ["#f1e6cf", "#dbc8a4"], crown: ["#3a8a50", "#4ea262", "#67ba70", "#8bd486"],
      trunk: ["#7b5236", "#5e3c27"], bench: ["#b07a4c", "#7e5232"], metal: "#3b4256", lampHead: "#e7edf6", fg: ["#3a8d4c", "#52a95f", "#74c476"],
      grade: "radial-gradient(ellipse 70% 70% at 50% 45%, rgba(20,40,90,0) 55%, rgba(20,40,90,.16) 100%)", per: "none", dots: ["#ffd34d", "#ff8fa3", "#ffffff", "#ffb347"], shadow: "rgba(30,70,30,.22)" },
    night: { sky: "#050b29 0%, #0d1846 42%, #1c2c66 78%, #2f427e 100%", cloud: ["#2a3a74", "#1d2a5c", 0.55], hill: ["#1b285a", "#141f4a"], city: "#111a40", win: "#ffd57a", lit: 0.62,
      tl: ["#0d262f", "#123139", "#183e45"], g: "#183b37 0%, #12302d 45%, #0b2222 100%", path: ["#3b4568", "#2a3354"], crown: ["#0c2729", "#113234", "#173f3d", "#235049"],
      trunk: ["#2b2222", "#1e1717"], bench: ["#4b3a33", "#33271f"], metal: "#1b1f31", lampHead: "#fff1c2", fg: ["#0a221e", "#0f2d27", "#153830"],
      grade: "radial-gradient(ellipse 72% 72% at 55% 42%, rgba(5,10,35,0) 45%, rgba(5,10,35,.5) 100%)", per: "brightness(.42) saturate(.75) contrast(1.05)", dots: null, shadow: "rgba(0,0,0,0)" },
    sakura: { sky: "#78bdf5 0%, #b3dbfb 48%, #f6e1ee 84%, #fdeef4 100%", cloud: ["#ffffff", "#f5e6f0", 0.92], hill: ["#c7d8f0", "#b4cbe9"], city: "#c3d5ec", win: "#e1ebf7", lit: 0,
      tl: ["#e488ae", "#f0a3c3", "#f9c8dc"], tlg: ["#4f9b5c", "#64b06a", "#82c784"], g: "#9fd884 0%, #80c66b 42%, #5fa955 100%", path: ["#f5e5d8", "#e3c8b8"], crown: ["#d9719c", "#ea8fb6", "#f5b3cf", "#fde3ee"],
      trunk: ["#6b4436", "#4f3128"], bench: ["#b07a4c", "#7e5232"], metal: "#3b4256", lampHead: "#e7edf6", fg: ["#4f9e57", "#6ab86c", "#f3a7c4"],
      grade: "linear-gradient(180deg, rgba(255,200,225,.16), rgba(255,255,255,0) 60%)", per: "saturate(1.05)", dots: ["#f7a9c6", "#fbd0e0", "#ffffff", "#f48fb1"], shadow: "rgba(60,80,40,.2)" },
    snow: { sky: "#9db0c8 0%, #c2cfdf 50%, #e2e8f0 84%, #eef2f7 100%", cloud: ["#e6ecf4", "#cfd8e5", 0.9], hill: ["#e6ecf4", "#d4dde9"], city: "#c8d3e1", win: "#e6edf5", lit: 0.12,
      tl: ["#c9d5e4", "#e9eff6", "#ffffff"], g: "#f7fafd 0%, #e7eef6 45%, #d5dfeb 100%", path: ["#dfe6ef", "#c7d2e0"], crown: ["#b9c8da", "#d8e2ee", "#eef3f9", "#ffffff"],
      trunk: ["#4c3a33", "#352823"], bench: ["#8a6248", "#5f412f"], metal: "#3b4256", lampHead: "#f1f4f8", fg: ["#d3dde9", "#e6edf5", "#ffffff"],
      grade: "linear-gradient(180deg, rgba(240,245,252,.22), rgba(240,245,252,.04))", per: "saturate(.85) brightness(.97)", dots: null, shadow: "rgba(90,110,140,.18)", snow: true },
    dusk: { sky: "#2c3778 0%, #7d55a3 32%, #ec8579 66%, #ffc47c 100%", cloud: ["#f6a796", "#d98aa0", 0.85], hill: ["#7a5a96", "#5d4a86"], city: "#4c3d76", win: "#ffcf7a", lit: 0.4,
      tl: ["#3a3c5c", "#474566", "#585272"], g: "#86a05c 0%, #6a844f 45%, #4d6640 100%", path: ["#ebbd98", "#c99a7c"], crown: ["#3c4741", "#4d5748", "#5d644c", "#6f6e52"],
      trunk: ["#4a3326", "#33231a"], bench: ["#8a5a3a", "#5e3c27"], metal: "#2b2c40", lampHead: "#ffe7b0", fg: ["#45563a", "#566643", "#6b784b"],
      grade: "linear-gradient(180deg, rgba(255,140,90,.08), rgba(90,40,120,.2))", per: "brightness(.78) sepia(.25) saturate(1.2)", dots: ["#ffcf7a", "#ff9f8a"], shadow: "rgba(40,20,40,.3)" },
  };
  // big tree crown (relative to the crown centre): [dx, dy, r, tier]
  const CROWN = [[-120, 20, 70, 0], [120, 25, 72, 0], [0, -70, 82, 0], [-62, -30, 78, 0], [70, -40, 80, 0], [0, 40, 78, 0],
    [-96, -6, 66, 1], [96, 0, 66, 1], [-40, -76, 64, 1], [45, -80, 62, 1], [0, -10, 78, 1], [-22, 44, 60, 1], [52, 40, 58, 1],
    [-110, 30, 46, 2], [104, 34, 46, 2], [-56, -50, 50, 2], [56, -56, 48, 2], [0, -96, 46, 2], [0, 22, 52, 2],
    [-72, -76, 26, 3], [20, -112, 24, 3], [76, -70, 22, 3], [-102, -22, 22, 3], [30, 0, 20, 3]];

  // pivots (local person space) for attr-transform rotations
  const PIV = { pb: [640, 520], lg1: [631.5, 432], lg2: [649.5, 432], al: [606.5, 367], ar: [673.5, 367], hd: [640, 342] };
  function person(p, x, y, s) {
    // a simple presenter figure (navy jacket), feet at (x, y), scale s. Groups: -pw walk offset > -pb body (sway / bob) > -al/-ar arms ·
    // -lg1/-lg2 legs · -hd head. Every animated group carries an explicit transform attribute (tweened with attr, fixed pivots).
    const R = (k) => `transform="rotate(0 ${PIV[k][0]} ${PIV[k][1]})"`;
    return `<g transform="translate(${f1(x - 640 * s)} ${f1(y - 520 * s)}) scale(${s})">` +
      `<g id="${p}-pw" transform="translate(0 0)"><ellipse cx="642" cy="521" rx="38" ry="7" fill="rgba(10,20,40,.22)"/>` +
      `<g id="${p}-pb" transform="translate(0 0) rotate(0 640 520)">` +
      `<g id="${p}-lg1" ${R("lg1")}><rect x="624" y="430" width="15" height="86" rx="7" fill="#27304a"/><ellipse cx="628" cy="517" rx="12" ry="5.5" fill="#161925"/></g>` +
      `<g id="${p}-lg2" ${R("lg2")}><rect x="642" y="430" width="15" height="86" rx="7" fill="#2d3754"/><ellipse cx="654" cy="517" rx="12" ry="5.5" fill="#161925"/></g>` +
      `<g id="${p}-al" ${R("al")}><rect x="599" y="364" width="15" height="74" rx="7.5" fill="#29416f"/><circle cx="606.5" cy="440" r="7.5" fill="#efc29e"/></g>` +
      `<path d="M612 362 Q640 350 668 362 L673 438 Q640 448 607 438 Z" fill="#33558f"/>` +
      `<path d="M629 356 L640 388 L651 356 Z" fill="#f5f7fb"/><path d="M640 388 L640 440" stroke="#24406e" stroke-width="2"/>` +
      `<path d="M612 362 Q626 356 631 357 L628 400 Z" fill="rgba(255,255,255,.08)"/>` +
      `<g id="${p}-ar" ${R("ar")}><rect x="666" y="364" width="15" height="74" rx="7.5" fill="#29416f"/><circle cx="673.5" cy="440" r="7.5" fill="#efc29e"/></g>` +
      `<rect x="634" y="336" width="12" height="16" rx="5" fill="#e3b28c"/>` +
      `<g id="${p}-hd" ${R("hd")}><circle cx="640" cy="322" r="21" fill="#efc29e"/><path d="M619 321 Q618 298 640 297 Q663 297 662 320 Q655 309 641 310 Q627 309 619 321 Z" fill="#23202b"/></g>` +
      `</g></g></g>`;
  }

  function cloud(id, cx, cy, s, c) {
    return `<g id="${id}" opacity="${c[2]}" transform="translate(0 0)">` + `<ellipse cx="${cx}" cy="${cy + 14 * s}" rx="${92 * s}" ry="${22 * s}" fill="${c[1]}"/>` +
      C(cx - 46 * s, cy + 2 * s, 30 * s, c[0]) + C(cx - 10 * s, cy - 14 * s, 42 * s, c[0]) + C(cx + 34 * s, cy - 4 * s, 33 * s, c[0]) + C(cx + 66 * s, cy + 8 * s, 22 * s, c[0]) +
      `<ellipse cx="${cx + 4 * s}" cy="${cy + 10 * s}" rx="${88 * s}" ry="${18 * s}" fill="${c[0]}"/></g>`;
  }

  // particles registry (built per copy; animated by footage())
  const PT = {};
  function particles(p, kind, n) {
    let h = ""; const list = [];
    for (let i = 0; i < n; i++) {
      const x = -20 + H(i * 3.1 + 7) * 1140, y0 = -560 + H(i * 5.7 + 2) * 1140, sz = kind === "snow" ? 4 + H(i + 40) * 6 : 9 + H(i + 40) * 6;
      const id = `${p}-pt${i}`;
      if (kind === "snow") h += `<i class="r10-sn" id="${id}" style="left:${f1(AX(x))}px;top:${f1(y0)}px;width:${f1(sz)}px;height:${f1(sz)}px;opacity:${(0.65 + H(i + 9) * 0.35).toFixed(2)}"></i>`;
      else if (kind === "petal") h += `<i class="r10-pe" id="${id}" style="left:${f1(AX(x))}px;top:${f1(y0)}px;width:${f1(sz)}px;height:${f1(sz * 0.66)}px;background:${["#f7a9c6", "#fbd0e0", "#f48fb1", "#fde3ee"][i % 4]}"></i>`;
      else if (kind === "fly") h += `<i class="r10-ff" id="${id}" style="left:${f1(AX(60 + H(i * 2.3) * 1000))}px;top:${f1(360 + H(i * 4.1) * 200)}px"></i>`;
      else if (kind === "dust") h += `<i class="r10-du" id="${id}" style="left:${f1(AX(430 + H(i * 2.9) * 300))}px;top:${f1(150 + H(i * 3.7) * 260)}px"></i>`;
      list.push({ id, kind, sp: kind === "snow" ? 70 + H(i + 21) * 70 : kind === "petal" ? 60 + H(i + 21) * 60 : 0, sw: 10 + H(i + 33) * 22, per: 0.9 + H(i + 51) * 1.2, rot: (H(i + 61) - 0.5) * 900, ph: H(i + 71) });
    }
    PT[p] = (PT[p] || []).concat(list);
    return h;
  }

  function park(p, look) {
    const k = PK[look];
    let h = `<div class="r10-sc" id="${p}">`;
    h += LY(p, "sky", "", `background:linear-gradient(180deg, ${k.sky})`);
    // ---- celestial
    let cel = "";
    if (look === "night") {
      let st = ""; for (let i = 0; i < 52; i++) st += C(-40 + H(i * 1.7) * 1180, 12 + H(i * 2.3 + 5) * 280, 0.8 + H(i + 17) * 1.6, "#ffffff", ` id="${p}-st${i}" opacity="${(0.55 + H(i + 3) * 0.45).toFixed(2)}"`);
      cel = `<svg class="r10-sv" viewBox="-40 0 1180 600" width="1180" height="600">${st}</svg>` +
        `<i class="r10-glow" style="left:${AX(830) - 160}px;top:${105 - 160}px;width:320px;height:320px;background:radial-gradient(circle, rgba(200,215,255,.42), rgba(200,215,255,0) 62%)"></i>` +
        `<i class="r10-moon" style="left:${AX(830) - 34}px;top:${105 - 34}px"><b style="left:16px;top:20px;width:12px;height:12px"></b><b style="left:38px;top:34px;width:9px;height:9px"></b><b style="left:24px;top:44px;width:6px;height:6px"></b></i>`;
    } else if (look === "dusk") {
      cel = `<i class="r10-glow" style="left:${AX(800) - 260}px;top:${318 - 260}px;width:520px;height:520px;background:radial-gradient(circle, rgba(255,214,140,.85), rgba(255,160,100,.35) 30%, rgba(255,150,100,0) 62%)"></i>` +
        `<i class="r10-sun" style="left:${AX(800) - 62}px;top:${318 - 62}px;width:124px;height:124px;background:radial-gradient(circle at 50% 45%, #fff3cc, #ffc070 55%, #ff9a55)"></i>`;
    } else if (look === "snow") {
      cel = `<i class="r10-sun" style="left:${AX(860) - 40}px;top:${120 - 40}px;width:80px;height:80px;background:rgba(255,255,255,.55);box-shadow:0 0 50px 20px rgba(255,255,255,.35)"></i>`;
    } else {
      cel = `<i class="r10-glow" style="left:${AX(860) - 170}px;top:${108 - 170}px;width:340px;height:340px;background:radial-gradient(circle, rgba(255,246,205,.95), rgba(255,236,170,.45) 22%, rgba(255,236,170,0) 60%)"></i>` +
        `<i class="r10-sun" id="${p}-sun" style="left:${AX(860) - 36}px;top:${108 - 36}px;width:72px;height:72px;background:radial-gradient(circle, #fffef4, #fff3c4)"></i>`;
    }
    h += LY(p, "cel", cel);
    // ---- clouds
    const cl = [[200, 92, 1.0], [560, 58, 0.78], [930, 150, 0.9], [40, 196, 0.62]].concat(look === "snow" ? [[380, 150, 1.2], [760, 96, 1.1]] : []);
    h += LY(p, "cld", SV(cl.map(([x, y, s], i) => cloud(`${p}-cl${i}`, x, y, s, k.cloud)).join("")));
    // ---- far: hills + small city
    let far = `<path d="M-40 336 C 60 286, 160 270, 280 300 S 520 262, 660 292 S 900 252, 1140 296 L1140 400 L-40 400 Z" fill="${k.hill[0]}"/>`;
    const BL = [[704, 270, 40, 72], [748, 246, 50, 96], [802, 280, 36, 62], [842, 228, 46, 114], [892, 258, 52, 84], [948, 238, 40, 104], [992, 270, 50, 72], [1046, 252, 44, 90]];
    BL.forEach(([x, y, w, hh], b) => {
      far += `<rect x="${x}" y="${y}" width="${w}" height="${hh}" fill="${k.city}"/>`;
      for (let yy = y + 8; yy < y + hh - 14; yy += 14) for (let xx = x + 6; xx < x + w - 8; xx += 11) {
        const on = H(b * 97 + xx * 1.3 + yy * 0.7) < k.lit;
        far += `<rect x="${xx}" y="${yy}" width="5" height="7" fill="${on ? k.win : look === "night" ? "#1a2552" : look === "dusk" ? "#5a4a80" : k.win}"${!on && (look === "day" || look === "sakura" || look === "snow") ? ' opacity=".7"' : ""}/>`;
      }
    });
    far += `<path d="M-40 352 C 100 320, 240 318, 380 336 S 640 312, 780 332 S 1000 318, 1140 338 L1140 400 L-40 400 Z" fill="${k.hill[1]}"/>`;
    h += LY(p, "far", SV(far));
    // ---- treeline
    let tl = `<rect x="-40" y="330" width="1180" height="40" fill="${k.tl[0]}"/>`;
    for (let i = 0; i < 18; i++) {
      const x = -30 + i * 68 + (H(i) - 0.5) * 20, y = 326 + (H(i + 50) - 0.5) * 12, r = 30 + H(i + 9) * 20;
      const c = look === "sakura" && i % 3 === 0 ? k.tlg : k.tl;
      tl += C(x, y + 4, r, c[0]) + C(x - r * 0.22, y - r * 0.14, r * 0.8, c[1]) + C(x + r * 0.22, y - r * 0.36, r * 0.44, c[2], ' opacity=".9"');
    }
    h += LY(p, "mid", SV(tl));
    // ---- ground: gradient plate + path, tree, bench, lamp, details
    let g = `<path d="M455 600 L 776 600 Q 664 452 609 336 L 590 336 Q 566 452 455 600 Z" fill="${k.path[0]}"/>` +
      `<path d="M455 600 Q 566 452 590 336" fill="none" stroke="${k.path[1]}" stroke-width="5"/><path d="M776 600 Q 664 452 609 336" fill="none" stroke="${k.path[1]}" stroke-width="5"/>`;
    for (let i = 0; i < 9; i++) g += `<ellipse cx="${f1(-20 + H(i + 300) * 1160)}" cy="${f1(380 + H(i + 310) * 200)}" rx="${f1(90 + H(i + 320) * 120)}" ry="${f1(10 + H(i + 330) * 10)}" fill="${look === "snow" ? "rgba(150,170,200,.13)" : look === "night" ? "rgba(0,0,0,.12)" : "rgba(255,255,255,.08)"}"/>`;
    if (k.dots) for (let i = 0; i < (look === "sakura" ? 120 : 60); i++) {
      const x = -30 + H(i * 1.9 + 400) * 1160, y = 360 + H(i * 2.7 + 401) * 236;
      const px = 455 + (600 - y) / 264 * 135, qx = 776 - (600 - y) / 264 * 167;
      if (x > px - 10 && x < qx + 10) continue;
      const r = (look === "sakura" ? 2.4 : 2.2) + H(i + 402) * 2.2;
      g += look === "sakura" ? `<ellipse cx="${f1(x)}" cy="${f1(y)}" rx="${f1(r * 1.3)}" ry="${f1(r * 0.8)}" fill="${k.dots[i % 4]}" opacity=".95"/>` : C(x, y, r * 0.8, k.dots[i % k.dots.length]);
    }
    // tree shadow
    g += `<ellipse cx="${look === "dusk" ? 180 : 270}" cy="532" rx="${look === "dusk" ? 220 : 150}" ry="22" fill="${k.shadow}"/>`;
    // bench
    g += `<rect x="112" y="440" width="136" height="9" rx="3" fill="${k.bench[0]}"/><rect x="112" y="453" width="136" height="9" rx="3" fill="${k.bench[0]}"/>` +
      `<rect x="108" y="474" width="146" height="11" rx="3" fill="${k.bench[0]}"/><rect x="108" y="483" width="146" height="4" fill="${k.bench[1]}"/>` +
      `<rect x="120" y="440" width="6" height="64" fill="${k.metal}"/><rect x="234" y="440" width="6" height="64" fill="${k.metal}"/>`;
    if (k.snow) g += `<path d="M106 474 Q 140 462 180 466 Q 220 461 256 474 Z" fill="#ffffff"/><path d="M110 440 Q 150 430 182 434 Q 220 429 250 440 Z" fill="#ffffff"/>`;
    // big tree
    const TX = 300, TY = 220;
    g += `<path d="M282 530 C 290 470, 287 400, 279 334 L 300 302 L 322 334 C 315 400, 314 470, 324 530 Z" fill="${k.trunk[0]}"/>` +
      `<path d="M300 302 L 300 530 L 324 530 C 314 470, 315 400, 322 334 Z" fill="${k.trunk[1]}" opacity=".5"/>` +
      `<path d="M296 330 L 236 262 M304 322 L 372 252 M300 310 L 300 230" stroke="${k.trunk[0]}" stroke-width="12" stroke-linecap="round"/>`;
    CROWN.forEach(([dx, dy, r, t]) => { g += C(TX + dx, TY + dy, r, k.crown[t]); });
    if (look === "sakura") for (let i = 0; i < 70; i++) { const a = H(i + 500) * Math.PI * 2, d = Math.sqrt(H(i + 501)) * 130; g += C(TX + Math.cos(a) * d * 1.15, TY - 20 + Math.sin(a) * d * 0.8, 3 + H(i + 502) * 4, i % 3 ? "#fde3ee" : "#ffffff", ' opacity=".9"'); }
    if (k.snow) { for (let i = 0; i < 26; i++) { const a = H(i + 520) * Math.PI * 2, d = Math.sqrt(H(i + 521)) * 120; g += C(TX + Math.cos(a) * d * 1.15, TY + Math.sin(a) * d * 0.8 + 18, 5 + H(i + 522) * 6, "#b4c4d8", ' opacity=".55"'); } }
    // lamp post
    g += `<rect x="826" y="516" width="28" height="14" rx="4" fill="${k.metal}"/><rect x="836" y="232" width="8" height="290" fill="${k.metal}"/>` +
      `<path d="M824 206 L 856 206 L 852 236 L 828 236 Z" fill="${k.lampHead}"/><path d="M820 206 L 840 192 L 860 206 Z" fill="${k.metal}"/><rect x="826" y="235" width="28" height="5" rx="2" fill="${k.metal}"/>`;
    if (k.snow) g += `<path d="M818 205 Q 840 186 862 205 Z" fill="#ffffff"/>`;
    h += LY(p, "gnd", `<i class="r10-plate" style="top:332px;height:268px;background:linear-gradient(180deg, ${k.g})"></i>` + SV(g));
    // lamp light (night / dusk)
    if (look === "night" || look === "dusk") {
      const a = look === "night" ? 1 : 0.55;
      h += LY(p, "lit", `<i class="r10-glow" id="${p}-lg" style="left:${AX(840) - 170}px;top:${222 - 170}px;width:340px;height:340px;opacity:${a};background:radial-gradient(circle, rgba(255,232,160,.95), rgba(255,210,120,.4) 18%, rgba(255,200,110,0) 58%)"></i>` +
        `<i class="r10-glow" id="${p}-lp" style="left:${AX(840) - 190}px;top:${528 - 50}px;width:380px;height:100px;opacity:${a};background:radial-gradient(ellipse closest-side, rgba(255,220,140,.55), rgba(255,220,140,0))"></i>` +
        `<i class="r10-glow" id="${p}-lc" style="left:${AX(840) - 120}px;top:236px;width:240px;height:300px;opacity:${a * 0.7};background:linear-gradient(180deg, rgba(255,226,150,.32), rgba(255,226,150,0));clip-path:polygon(44% 0, 56% 0, 100% 100%, 0 100%)"></i>`);
    }
    // person
    h += LY(p, "per", SV(person(p, 640, 520, 1)), k.per !== "none" ? `filter:${k.per}` : "");
    // particles
    if (look === "sakura") h += LY(p, "pt", particles(p, "petal", 34));
    if (look === "snow") h += LY(p, "pt", particles(p, "snow", 64));
    if (look === "night") h += LY(p, "pt", particles(p, "fly", 9));
    // foreground bushes
    let fg = "";
    [[-30, 580, 1], [70, 600, 0.8], [1040, 586, 1], [1130, 570, 0.9]].forEach(([x, y, s], i) => {
      fg += C(x, y, 70 * s, k.fg[0]) + C(x - 40 * s, y + 6, 52 * s, k.fg[1]) + C(x + 44 * s, y - 4, 48 * s, k.fg[1]) + C(x + 6, y - 30 * s, 40 * s, k.fg[2]);
      if (look === "sakura") for (let j = 0; j < 8; j++) fg += C(x - 50 * s + H(i * 9 + j) * 100 * s, y - 40 * s + H(i * 9 + j + 3) * 50 * s, 4, "#fde3ee");
    });
    h += LY(p, "fg", SV(fg));
    h += LY(p, "gr", "", `background:${k.grade}`);
    return h + `</div>`;
  }

  // ================================================================ STREET (ruko row + kerb)
  function car(p) {
    return `<g id="${p}-car" transform="translate(0 0)"><defs><linearGradient id="${p}-cb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6ea0f7"/><stop offset=".45" stop-color="#3a6fe0"/><stop offset="1" stop-color="#1f4aa8"/></linearGradient>` +
      `<linearGradient id="${p}-cw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b9d4f2"/><stop offset="1" stop-color="#2b3f6a"/></linearGradient></defs>` +
      `<ellipse cx="180" cy="119" rx="178" ry="10" fill="rgba(10,15,30,.38)"/>` +
      `<path d="M18 96 C 12 78 18 66 40 62 L 96 54 C 118 30 140 20 172 18 L 246 17 C 274 18 292 30 314 50 L 336 56 C 352 60 358 70 356 86 L 354 98 C 353 104 348 106 342 106 L 26 106 C 20 106 18 102 18 96 Z" fill="url(#${p}-cb)"/>` +
      `<path d="M108 54 C 126 34 144 27 170 26 L 202 26 L 204 55 Z" fill="url(#${p}-cw)"/><path d="M214 26 L 246 26 C 268 27 284 36 302 54 L 216 56 Z" fill="url(#${p}-cw)"/>` +
      `<path d="M120 50 C 134 38 146 33 160 31" stroke="rgba(255,255,255,.55)" stroke-width="3" fill="none" stroke-linecap="round"/>` +
      `<path d="M34 70 L 340 68" stroke="rgba(255,255,255,.4)" stroke-width="3" stroke-linecap="round"/>` +
      `<path d="M207 58 L 207 100 M112 58 L 110 100" stroke="rgba(10,20,50,.25)" stroke-width="2"/>` +
      `<rect x="150" y="66" width="22" height="5" rx="2.5" fill="rgba(10,20,50,.35)"/><rect x="252" y="66" width="22" height="5" rx="2.5" fill="rgba(10,20,50,.35)"/>` +
      `<ellipse cx="28" cy="74" rx="9" ry="6" fill="#fff4c2"/><rect x="344" y="66" width="10" height="13" rx="3" fill="#e5484d"/>` +
      `<path d="M46 106 a 36 36 0 0 1 72 0 Z" fill="#17203a"/><path d="M244 106 a 36 36 0 0 1 72 0 Z" fill="#17203a"/>` +
      [82, 280].map((x) => `<circle cx="${x}" cy="104" r="26" fill="#141824"/><circle cx="${x}" cy="104" r="15" fill="#c9d3e3"/><circle cx="${x}" cy="104" r="6" fill="#7d889c"/>`).join("") +
      `<path d="M52 100 L 330 100" stroke="rgba(255,255,255,.18)" stroke-width="2"/></g>`;
  }
  function street(p, withCar) {
    let h = `<div class="r10-sc" id="${p}">`;
    h += LY(p, "sky", "", "background:linear-gradient(180deg, #59aef3 0%, #98d0fb 50%, #dff1ff 100%)");
    h += LY(p, "cel", `<i class="r10-glow" style="left:${AX(170) - 150}px;top:${70 - 150}px;width:300px;height:300px;background:radial-gradient(circle, rgba(255,246,205,.95), rgba(255,236,170,.4) 24%, rgba(255,236,170,0) 60%)"></i>` +
      `<i class="r10-sun" style="left:${AX(170) - 32}px;top:${70 - 32}px;width:64px;height:64px;background:radial-gradient(circle, #fffef4, #fff3c4)"></i>`);
    h += LY(p, "cld", SV([[420, 70, 0.8], [820, 50, 0.9], [1080, 120, 0.6]].map(([x, y, s], i) => cloud(`${p}-cl${i}`, x, y, s, ["#ffffff", "#e4eefb", 0.95])).join("")));
    let far = "";
    [[-30, 150, 90], [70, 120, 70], [150, 170, 120], [800, 130, 80], [890, 90, 60], [960, 150, 100], [1070, 120, 80]].forEach(([x, y, w]) => { far += `<rect x="${x}" y="${y}" width="${w}" height="${300 - y}" fill="#b9d2ec"/>`; });
    h += LY(p, "far", SV(far));
    // ruko row
    const WALL = ["#f3e2c4", "#d6e6f5", "#f5d5cc", "#d8ecdf", "#efe0f3"], SIGN = ["#294b77", "#e5484d", "#2da44e", "#7c5cff", "#d99a00"], WORD = ["KOPI", "TOKO", "ROTI", "FOTO", "BENGKEL"];
    let b = "";
    for (let u = 0; u < 5; u++) {
      const x0 = -40 + u * 270;
      b += `<rect x="${x0}" y="118" width="270" height="296" fill="${WALL[u]}"/><rect x="${x0}" y="104" width="270" height="22" fill="rgba(10,13,44,.10)"/><rect x="${x0}" y="100" width="270" height="8" fill="#ffffff" opacity=".7"/>`;
      for (let i = 0; i < 3; i++) { const wx = x0 + 32 + i * 76; b += `<rect x="${wx}" y="146" width="56" height="78" rx="4" fill="#ffffff"/><rect x="${wx + 5}" y="151" width="46" height="68" rx="2" fill="#a7c9e8"/><path d="M${wx + 5} 200 L ${wx + 30} 151 L ${wx + 42} 151 L ${wx + 5} 216 Z" fill="rgba(255,255,255,.35)"/><rect x="${wx - 4}" y="224" width="64" height="6" rx="2" fill="#ffffff"/>`; }
      b += `<rect x="${x0 + 22}" y="244" width="226" height="36" rx="5" fill="${SIGN[u]}"/><text x="${x0 + 135}" y="270" text-anchor="middle" font-family="Poppins, sans-serif" font-weight="700" font-size="19" letter-spacing="3" fill="#ffffff">${WORD[u]}</text>`;
      for (let s = 0; s < 10; s++) b += `<path d="M${x0 + 12 + s * 25} 292 l 25 0 l 0 18 q -12.5 10 -25 0 Z" fill="${s % 2 ? "#ffffff" : SIGN[u]}"/>`;
      b += `<rect x="${x0 + 24}" y="318" width="132" height="96" fill="#cdd5e1"/>`;
      for (let l = 0; l < 9; l++) b += `<rect x="${x0 + 24}" y="${322 + l * 10}" width="132" height="2" fill="rgba(80,95,120,.25)"/>`;
      b += `<rect x="${x0 + 168}" y="318" width="80" height="96" fill="#ffffff"/><rect x="${x0 + 174}" y="324" width="68" height="90" fill="#8fb7dc"/><path d="M${x0 + 174} 380 L ${x0 + 210} 324 L ${x0 + 226} 324 L ${x0 + 174} 404 Z" fill="rgba(255,255,255,.3)"/>`;
      b += `<rect x="${x0 - 7}" y="118" width="14" height="296" fill="#ebe5da"/>`;
    }
    h += LY(p, "bld", SV(b));
    // sidewalk + kerb + road
    let g = `<rect x="-40" y="410" width="1180" height="44" fill="#e2e5eb"/><rect x="-40" y="410" width="1180" height="8" fill="rgba(10,13,44,.08)"/>`;
    for (let x = -40; x < 1140; x += 64) g += `<rect x="${x}" y="418" width="2" height="36" fill="#cfd5df"/>`;
    g += `<rect x="-40" y="452" width="1180" height="9" fill="#f4f5f8"/><rect x="-40" y="461" width="1180" height="11" fill="#b5bccb"/>` +
      `<rect x="-40" y="472" width="1180" height="128" fill="#5b6273"/><rect x="-40" y="472" width="1180" height="14" fill="rgba(0,0,0,.14)"/>`;
    for (let x = -40; x < 1140; x += 170) g += `<rect x="${x + 20}" y="566" width="92" height="8" rx="2" fill="#f2f2f2" opacity=".85"/>`;
    for (let i = 0; i < 26; i++) g += `<rect x="${f1(-40 + H(i + 700) * 1180)}" y="${f1(492 + H(i + 701) * 100)}" width="${f1(6 + H(i + 702) * 18)}" height="2" fill="rgba(255,255,255,.07)"/>`;
    g += `<rect x="232" y="463" width="44" height="8" rx="2" fill="#3a3f4d"/>`;
    // street tree in a planter (sidewalk, left)
    g += `<rect x="286" y="398" width="44" height="22" rx="4" fill="#9aa3b5"/><rect x="304" y="300" width="9" height="102" fill="#6b4a33"/>` +
      C(308, 280, 46, "#3f9a58") + C(286, 296, 34, "#4fa765") + C(332, 292, 34, "#4fa765") + C(310, 262, 30, "#67ba70");
    h += LY(p, "gnd", SV(g));
    h += LY(p, "per", SV(person(p, 900, 446, 0.74)));
    if (withCar) h += LY(p, "car", SV(`<g transform="translate(420 440)">${car(p)}</g>`));
    h += LY(p, "fg", SV(`<rect x="1040" y="0" width="22" height="600" fill="#3b4256"/><rect x="1032" y="560" width="38" height="40" fill="#2b3040"/><path d="M1040 70 L 960 70 L 948 82 L 1040 82 Z" fill="#3b4256"/><rect x="940" y="82" width="34" height="10" rx="3" fill="#e7edf6"/>`));
    h += LY(p, "gr", "", "background:radial-gradient(ellipse 70% 70% at 50% 45%, rgba(20,40,90,0) 55%, rgba(20,40,90,.16) 100%)");
    return h + `</div>`;
  }

  // ================================================================ SHELF (plain shelf → product line)
  function bottle(p, cx, base, i) {
    return `<g><rect x="${cx - 30}" y="${base - 124}" width="60" height="124" rx="15" fill="url(#${p}-bt)"/><rect x="${cx - 11}" y="${base - 142}" width="22" height="22" fill="#14284a"/>` +
      `<rect x="${cx - 15}" y="${base - 162}" width="30" height="22" rx="5" fill="#01ccf7"/><rect x="${cx - 15}" y="${base - 162}" width="10" height="22" rx="4" fill="rgba(255,255,255,.35)"/>` +
      `<rect x="${cx - 30}" y="${base - 98}" width="60" height="56" fill="#ffffff"/><rect x="${cx - 30}" y="${base - 50}" width="60" height="5" fill="#01ccf7"/>` +
      `<text x="${cx}" y="${base - 76}" text-anchor="middle" font-family="Poppins, sans-serif" font-weight="700" font-size="9.4" letter-spacing=".6" fill="#0a0d2c">PRODUKMU</text>` +
      `<text x="${cx}" y="${base - 61}" text-anchor="middle" font-family="Poppins, sans-serif" font-weight="400" font-size="7.5" fill="#5d6f8f">${["serum", "toner", "essence"][i]}</text>` +
      `<rect x="${cx - 23}" y="${base - 118}" width="7" height="104" rx="3.5" fill="rgba(255,255,255,.22)"/></g>`;
  }
  function shelf(p, withProducts) {
    let h = `<div class="r10-sc" id="${p}">`;
    let wall = "";
    for (let x = -40; x < 1140; x += 110) wall += `<rect x="${x}" y="0" width="2" height="466" fill="rgba(140,110,80,.07)"/>`;
    wall += `<rect x="-40" y="466" width="1180" height="74" fill="#e8d9c5"/><rect x="-40" y="462" width="1180" height="8" fill="#f8f2ea"/>`;
    h += LY(p, "wall", `<i class="r10-plate" style="top:0;height:600px;background:linear-gradient(180deg, #f8f2ea, #efe4d6)"></i>` + SV(wall));
    let win = `<rect x="104" y="84" width="182" height="262" rx="10" fill="#ffffff"/><rect x="118" y="98" width="154" height="234" rx="4" fill="#d8ecfc"/>` +
      `<rect x="118" y="230" width="154" height="102" fill="#cfe8f7"/>` + C(150, 300, 40, "#9fd08f") + C(200, 312, 34, "#86c27a") + C(246, 296, 30, "#a8d79a") +
      `<rect x="191" y="98" width="8" height="234" fill="#ffffff"/><rect x="118" y="210" width="154" height="8" fill="#ffffff"/>` +
      `<path d="M290 110 L 440 150 L 440 440 L 290 372 Z" fill="rgba(255,252,236,.45)"/>`;
    h += LY(p, "win", SV(win));
    // pendant lamp + light cone (in every copy: the room light is part of the original)
    h += LY(p, "lamp", SV(`<path d="M556 70 L 604 70 L 800 484 L 360 484 Z" fill="rgba(255,240,200,.22)"/><rect x="578" y="-10" width="4" height="44" fill="#3a3f52"/>` +
      `<path d="M546 70 Q 546 34 580 32 Q 614 34 614 70 Z" fill="#294b77"/><rect x="544" y="66" width="72" height="6" rx="3" fill="#1c3658"/><ellipse cx="580" cy="74" rx="16" ry="6" fill="#fff3cf"/>`) +
      `<i class="r10-glow" id="${p}-lg" style="left:${AX(580) - 150}px;top:${78 - 150}px;width:300px;height:300px;background:radial-gradient(circle, rgba(255,236,180,.85), rgba(255,226,160,.25) 30%, rgba(255,226,160,0) 62%)"></i>`);
    let sh = "";
    [262, 424].forEach((y) => {
      sh += `<rect x="300" y="${y + 14}" width="560" height="20" fill="rgba(80,50,20,.07)"/><rect x="300" y="${y + 14}" width="560" height="9" fill="rgba(80,50,20,.07)"/>` +
        `<path d="M340 ${y + 16} l 0 30 l 26 -30 Z M820 ${y + 16} l 0 30 l -26 -30 Z" fill="#8a5d38"/>` +
        `<rect x="296" y="${y}" width="568" height="16" rx="3" fill="#b9875a"/><rect x="296" y="${y}" width="568" height="3" rx="1.5" fill="#d9a878"/><rect x="296" y="${y + 11}" width="568" height="5" fill="#9a6c44"/>`;
    });
    // the original props (stay in every copy): plant, books, vase (shifted with the planks)
    sh += `<g transform="translate(0 14)">` +
      `<path d="M330 248 L 370 248 L 366 212 L 334 212 Z" fill="#d9825b"/><rect x="330" y="208" width="40" height="7" rx="2" fill="#c4704b"/>` +
      `<ellipse cx="338" cy="186" rx="10" ry="26" fill="#4f9a5d" transform="rotate(-24 338 186)"/><ellipse cx="362" cy="182" rx="10" ry="28" fill="#6ab86f" transform="rotate(22 362 182)"/><ellipse cx="350" cy="174" rx="9" ry="30" fill="#5aa863"/>` +
      `<rect x="770" y="236" width="74" height="12" rx="2" fill="#294b77"/><rect x="775" y="224" width="64" height="12" rx="2" fill="#e5484d"/><rect x="772" y="212" width="70" height="12" rx="2" fill="#f4b400"/>` +
      `<path d="M352 410 C 340 392 344 372 356 366 L 358 352 L 374 352 L 376 366 C 388 372 392 392 380 410 Z" fill="#ffffff" stroke="#d6cbbd" stroke-width="2"/><path d="M346 386 L 386 386" stroke="#7f9cc6" stroke-width="5"/>` + `</g>`;
    h += LY(p, "back", SV(sh));
    if (withProducts) {
      let pr = `<defs><linearGradient id="${p}-bt" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3a5f93"/><stop offset=".55" stop-color="#294b77"/><stop offset="1" stop-color="#0a0d2c"/></linearGradient></defs>`;
      [500, 590, 680].forEach((cx, i) => { pr += bottle(p, cx, 262, i); });
      pr += `<g transform="translate(0 14)">`;
      pr += `<rect x="432" y="300" width="88" height="110" rx="6" fill="#ffffff"/><rect x="432" y="300" width="88" height="34" rx="6" fill="#294b77"/><rect x="432" y="326" width="88" height="8" fill="#294b77"/>` +
        `<text x="476" y="322" text-anchor="middle" font-family="Poppins, sans-serif" font-weight="700" font-size="10" letter-spacing=".5" fill="#ffffff">PRODUKMU</text><rect x="446" y="350" width="60" height="4" rx="2" fill="#01ccf7"/>` +
        `<rect x="446" y="362" width="44" height="3" rx="1.5" fill="#c9d4e6"/><rect x="446" y="372" width="52" height="3" rx="1.5" fill="#c9d4e6"/><rect x="520" y="306" width="6" height="104" fill="rgba(10,13,44,.08)"/>`;
      [592, 684].forEach((cx) => {
        pr += `<rect x="${cx - 38}" y="352" width="76" height="58" rx="14" fill="#f7f9fd" stroke="#dfe6f2" stroke-width="2"/><rect x="${cx - 40}" y="336" width="80" height="20" rx="7" fill="#294b77"/>` +
          `<rect x="${cx - 38}" y="370" width="76" height="22" fill="#e6f6fd"/><text x="${cx}" y="385" text-anchor="middle" font-family="Poppins, sans-serif" font-weight="700" font-size="8.5" letter-spacing=".5" fill="#0a0d2c">PRODUKMU</text>` +
          `<rect x="${cx - 32}" y="340" width="18" height="12" rx="4" fill="rgba(255,255,255,.25)"/>`;
      });
      pr += `</g>`;
      for (let i = 0; i < 4; i++) { const sx = [452, 712, 640, 548][i], sy = [130, 120, 314, 328][i]; pr += `<path id="${p}-sk${i}" transform="translate(${sx} ${sy}) scale(0.3) translate(${-sx} ${-sy})" d="M${sx} ${sy - 12} L ${sx + 3} ${sy - 3} L ${sx + 12} ${sy} L ${sx + 3} ${sy + 3} L ${sx} ${sy + 12} L ${sx - 3} ${sy + 3} L ${sx - 12} ${sy} L ${sx - 3} ${sy - 3} Z" fill="#ffffff"/>`; }
      h += LY(p, "prod", `<i class="r10-glow" style="left:${AX(590) - 280}px;top:${300 - 200}px;width:560px;height:400px;background:radial-gradient(ellipse closest-side, rgba(255,248,226,.9), rgba(255,248,226,0))"></i>` + SV(pr));
    }
    h += LY(p, "flr", `<i class="r10-plate" style="top:540px;height:60px;background:linear-gradient(180deg, #c9a27c, #b58e69)"></i>` + SV([0, 1, 2, 3, 4, 5, 6, 7, 8].map((i) => `<rect x="${-40 + i * 150}" y="540" width="2" height="60" fill="rgba(90,60,30,.18)"/>`).join("")));
    h += LY(p, "dust", particles(p, "dust", 14));
    h += LY(p, "fg", SV(`<path d="M1140 600 C 1060 520, 980 470, 900 470 C 960 520, 1000 560, 1020 600 Z" fill="#2f6b45"/><path d="M1140 560 C 1080 460, 1010 400, 940 392 C 990 450, 1040 520, 1070 600 L 1140 600 Z" fill="#3c7f52"/>` +
      `<path d="M-40 600 C 20 540, 70 520, 120 526 C 80 556, 50 580, 40 600 Z" fill="#3c7f52"/>`), "filter:blur(3px)");
    h += LY(p, "gr", "", "background:radial-gradient(ellipse 75% 75% at 55% 40%, rgba(60,30,10,0) 50%, rgba(60,30,10,.16) 100%)");
    return h + `</div>`;
  }

  // ================================================================ player (before / after viewport) + prompt
  const FR = { x: 60, y: 318, w: 960, h: 548, vx: 70, vy: 328, vw: 940, vh: 528 };
  const copy = (p, inner) => `<div class="r10-cp" id="${p}-w">${inner}</div>`;
  const player = (p) => `<div class="r10-fr" id="${p}-fr"></div><div class="r10-vp" id="${p}-vp"><div class="r10-stage" id="${p}-stg"></div><i class="r10-streak" id="${p}-stk"></i>` +
    `<div class="r10-dv" id="${p}-dv"><i></i><b>${svg("moveH", 2.6)}</b></div>` +
    `<div class="r10-lb r10-lbA" id="${p}-lbA">${svg("video", 2.2)}VIDEO ASLI</div>` +
    `<div class="r10-lb r10-lbB" id="${p}-lbB">${svg("sparkles", 2.2)}HASIL EDIT AI</div>` +
    `<div class="r10-il" id="${p}-il">${svg("image", 2.2)}ILUSTRASI</div></div>`;
  const prompt = (p, lines) => {
    let h = `<div class="r10-pp" id="${p}-pp"><div class="ic">${svg("sparkles", 2.2)}</div><div class="tx"><span class="ph" id="${p}-pph">Tulis perubahannya…</span>`;
    lines.forEach((t, k) => { h += `<span class="ln" id="${p}-pl${k}">` + [...t].map((c, i) => `<i id="${p}-pc${k}_${i}">${c === " " ? "&nbsp;" : c}</i>`).join("") + `</span>`; });
    return h + `<b class="ca" id="${p}-pca"></b></div><div class="sd"><i class="on" id="${p}-psd"></i>${svg("arrowUp", 2.8)}</div></div>`;
  };
  // pin + type line k of the prompt between t0 and t1 (chars appear one by one; the placeholder leaves)
  function type(api, p, lines, k, t0, t1) {
    const $ = (id) => document.getElementById(id), n = lines[k].length;
    for (let i = 0; i < n; i++) { const e = $(`${p}-pc${k}_${i}`); api.tl.set(e, { display: "inline" }, t0 + (t1 - t0) * (i / Math.max(1, n - 1))); }
    api.tl.set($(`${p}-pph`), { display: "none" }, t0 - 0.01);
  }
  function untype(api, p, lines, k, t, back) {
    const $ = (id) => document.getElementById(id), n = lines[k].length;
    for (let i = 0; i < n; i++) api.tl.set($(`${p}-pc${k}_${i}`), { display: "none" }, t + (back || 0) * ((n - 1 - i) / Math.max(1, n - 1)));
  }
  function pinPrompt(api, p, lines) {
    const $ = (id) => document.getElementById(id);
    lines.forEach((t, k) => { for (let i = 0; i < t.length; i++) api.I($(`${p}-pc${k}_${i}`), { display: "none" }); });
    api.I($(`${p}-pph`), { display: "inline" });
    api.I($(`${p}-psd`), { opacity: 0 });
    // caret blink (deterministic)
    const ca = $(`${p}-pca`); api.I(ca, { opacity: 1 });
  }
  const clip = (x) => `inset(0px 0px 0px ${f1(x)}px)`;
  // reveal copy `cp` (its wrapper id) from x0 to x1 (viewport px; the divider follows)
  function wipe(api, p, cp, t, x0, x1, d, ease) {
    const $ = (id) => document.getElementById(id);
    api.ft($(cp + "-w"), { clipPath: clip(x0) }, { clipPath: clip(x1), duration: d, ease: ease || "power2.inOut" }, t);
    api.ft($(p + "-dv"), { x: x0 }, { x: x1, duration: d, ease: ease || "power2.inOut" }, t);
  }

  // identical footage motion for every copy (camera drift + parallax, clouds, stars, person idle, particles, lamp)
  const FX = { sky: 0.08, cel: 0.1, cld: 0.18, far: 0.3, mid: 0.5, bld: 0.62, wall: 0.3, win: 0.42, lamp: 0.7, back: 0.85, prod: 0.85, gnd: 1, lit: 1, per: 1, car: 1, mk: 1, flr: 1, pt: 1.12, dust: 1.05, fg: 1.6, gr: 0 };
  function footage(api, ps, t0, dur, o) {
    o = Object.assign({ pan: 34, s0: 1, push: 0.035, ox: 50, oy: 55 }, o || {});
    const $ = (id) => document.getElementById(id), ft = api.ft, I = api.I;
    ps.forEach((p) => {
      const sc = $(p); if (!sc) return;
      I(sc, { scale: o.s0, x: o.x || 0, y: o.y || 0, transformOrigin: `${o.ox}% ${o.oy}%` });
      ft(sc, { scale: o.s0 }, { scale: o.s0 + o.push, duration: dur, ease: "none" }, t0);
      for (const [k, f] of Object.entries(FX)) { const e = $(`${p}-${k}`); if (!e || !f) continue; I(e, { x: 0 }); ft(e, { x: 0 }, { x: -f * o.pan, duration: dur, ease: "none" }, t0); }
      for (let i = 0; i < 6; i++) { const c = $(`${p}-cl${i}`); if (!c) continue; const dx = (14 + i * 6) * dur / 4;
        I(c, { attr: { transform: "translate(0 0)" } }); ft(c, { attr: { transform: "translate(0 0)" } }, { attr: { transform: `translate(${dx.toFixed(1)} 0)` }, duration: dur, ease: "none" }, t0); }
      for (let i = 0; i < 14; i++) { const s = $(`${p}-st${i * 3}`); if (!s) continue; const per = 0.35 + H(i + 90) * 0.5; I(s, { opacity: 1 });
        ft(s, { opacity: 1 }, { opacity: 0.2, duration: per, yoyo: true, repeat: Math.ceil(dur / per) + 1, ease: "sine.inOut" }, t0 + H(i + 91) * 0.5); }
      const sun = $(`${p}-sun`); if (sun) { I(sun, { scale: 1 }); ft(sun, { scale: 1 }, { scale: 1.08, duration: 0.9, yoyo: true, repeat: Math.ceil(dur / 0.9), ease: "sine.inOut" }, t0); }
      // person: idle sway + arm life, or a walk (attr transforms around fixed pivots)
      const rot = (k, a) => ({ attr: { transform: `rotate(${a.toFixed(2)} ${PIV[k][0]} ${PIV[k][1]})` } });
      const body = (y, a) => ({ attr: { transform: `translate(0 ${y.toFixed(2)}) rotate(${a.toFixed(2)} 640 520)` } });
      const E = (k) => $(`${p}-${k}`);
      if (E("pw")) {
        I(E("pw"), { attr: { transform: "translate(0 0)" } }); I(E("pb"), body(0, 0));
        ["lg1", "lg2", "al", "ar", "hd"].forEach((k) => I(E(k), rot(k, 0)));
        const yo = (k, a, b, d, t, n) => ft(E(k), k === "pb" ? body(0, a) : rot(k, a), Object.assign(k === "pb" ? body(0, b) : rot(k, b), { duration: d, yoyo: true, repeat: n, ease: "sine.inOut" }), t);
        if (o.walk) {
          const st = 0.34, n = Math.ceil(dur / st) + 1;
          ft(E("pw"), { attr: { transform: "translate(0 0)" } }, { attr: { transform: `translate(${o.walk} 0)` }, duration: dur, ease: "none" }, t0);
          yo("lg1", -18, 18, st, t0, n); yo("lg2", 18, -18, st, t0, n); yo("al", 14, -14, st, t0, n); yo("ar", -14, 14, st, t0, n);
          ft(E("pb"), body(0, 0), Object.assign(body(-5, 0), { duration: st / 2, yoyo: true, repeat: n * 2, ease: "sine.inOut" }), t0);
        } else {
          yo("pb", -1.4, 1.4, 1.4, t0, Math.ceil(dur / 1.4));
          yo("al", 3, -3, 1.1, t0, Math.ceil(dur / 1.1));
          yo("hd", -3, 4, 1.7, t0, Math.ceil(dur / 1.7));
          (o.wave || []).forEach((tw) => {   // a hand wave (right arm up, swings, down)
            ft(E("ar"), rot("ar", 0), Object.assign(rot("ar", -150), { duration: 0.22, ease: "power2.out" }), tw);
            ft(E("ar"), rot("ar", -150), Object.assign(rot("ar", -122), { duration: 0.16, yoyo: true, repeat: 3, ease: "sine.inOut" }), tw + 0.22);
            ft(E("ar"), rot("ar", -150), Object.assign(rot("ar", 0), { duration: 0.3, ease: "power2.inOut" }), tw + 0.86);
          });
        }
      }
      // particles
      (PT[p] || []).forEach((q, i) => {
        const e = $(q.id); if (!e) return;
        if (q.kind === "snow" || q.kind === "petal") {
          I(e, { x: 0, y: 0, rotation: 0 });
          ft(e, { y: 0 }, { y: q.sp * dur, duration: dur, ease: "none" }, t0);
          const sg = i % 2 ? 1 : -1;   // never insert at a negative position (GSAP would shift the other children)
          ft(e, { x: -q.sw * sg }, { x: q.sw * sg, duration: q.per, yoyo: true, repeat: Math.ceil(dur / q.per) + 1, ease: "sine.inOut" }, t0);
          if (q.kind === "petal") ft(e, { rotation: 0 }, { rotation: q.rot, duration: dur, ease: "none" }, t0);
        } else if (q.kind === "fly") {
          I(e, { x: 0, y: 0, opacity: 0.2 });
          ft(e, { x: i % 2 ? 18 : -18 }, { x: i % 2 ? -18 : 18, duration: 1.3 + q.ph, yoyo: true, repeat: Math.ceil(dur / 1.3) + 1, ease: "sine.inOut" }, t0);
          ft(e, { y: 10 }, { y: -12, duration: 0.9 + q.ph * 0.6, yoyo: true, repeat: Math.ceil(dur / 0.9) + 1, ease: "sine.inOut" }, t0);
          ft(e, { opacity: 0.2 }, { opacity: 1, duration: 0.5 + q.ph * 0.4, yoyo: true, repeat: Math.ceil(dur / 0.5) + 1, ease: "sine.inOut" }, t0 + q.ph * 0.4);
        } else if (q.kind === "dust") {
          I(e, { x: 0, y: 0, opacity: 0.7 });
          ft(e, { y: 0 }, { y: -40 - q.sw, duration: dur, ease: "none" }, t0);
          ft(e, { x: -6 }, { x: 6, duration: q.per, yoyo: true, repeat: Math.ceil(dur / q.per) + 1, ease: "sine.inOut" }, t0);
        }
      });
      // lamp flicker-on at o.lampOn (night copies)
      if (o.lampOn != null) ["lg", "lp", "lc"].forEach((k, j) => {
        const e = $(`${p}-${k}`); if (!e) return; const a = parseFloat(e.style.opacity || "1");
        I(e, { opacity: 0 });
        [[0, a * 0.8], [0.06, 0], [0.12, a], [0.18, a * 0.3], [0.24, a]].forEach(([dt, v]) => api.tl.set(e, { opacity: v }, o.lampOn + dt));
      });
      // product sparkles (shelf)
      for (let i = 0; i < 4; i++) { const s = $(`${p}-sk${i}`); if (!s) continue; const sx = [452, 712, 640, 548][i], sy = [130, 120, 314, 328][i];
        const sk = (v) => ({ attr: { transform: `translate(${sx} ${sy}) scale(${v}) translate(${-sx} ${-sy})` } });
        I(s, sk(0.3)); I(s, { opacity: 0 });
        const per = 0.55, n = Math.ceil(dur / (2 * per + 0.25)) + 1;
        ft(s, Object.assign(sk(0.3), { opacity: 0 }), Object.assign(sk(1.1), { opacity: 1, duration: per, yoyo: true, repeat: n * 2, repeatDelay: 0.25, ease: "sine.inOut" }), t0 + 0.2 + i * 0.27); }
    });
  }

  const css = `
  .r10-sc { position: absolute; left: -80px; top: -36px; width: 1100px; height: 600px; transform-origin: 50% 55%; }
  .r10-ly { position: absolute; left: -40px; top: 0; width: 1180px; height: 600px; }
  .r10-sv { position: absolute; left: 0; top: 0; display: block; overflow: visible; }
  .r10-plate { position: absolute; left: 0; width: 1180px; display: block; }
  .r10-glow, .r10-sun, .r10-moon { position: absolute; display: block; border-radius: 50%; }
  .r10-moon { width: 68px; height: 68px; background: radial-gradient(circle at 36% 34%, #fffdf0, #f4e7c0 68%, #e3d29e); box-shadow: 0 0 36px 8px rgba(220,230,255,.35); }
  .r10-moon b { position: absolute; display: block; border-radius: 50%; background: rgba(190,170,120,.35); }
  .r10-sn { position: absolute; display: block; border-radius: 50%; background: #ffffff; box-shadow: 0 0 6px rgba(255,255,255,.8); }
  .r10-pe { position: absolute; display: block; border-radius: 70% 0 70% 0; box-shadow: inset 0 0 0 1px rgba(255,255,255,.35); }
  .r10-ff { position: absolute; display: block; width: 7px; height: 7px; border-radius: 50%; background: #fff3b0; box-shadow: 0 0 10px 4px rgba(255,230,120,.7); }
  .r10-du { position: absolute; display: block; width: 4px; height: 4px; border-radius: 50%; background: rgba(255,250,230,.95); box-shadow: 0 0 6px rgba(255,240,200,.9); }
  .r10-cp { position: absolute; left: 0; top: 0; width: 940px; height: 528px; overflow: hidden; }
  .r10-fr { position: absolute; left: 60px; top: 318px; width: 960px; height: 548px; border-radius: 34px; background: linear-gradient(180deg, #ffffff, #f4f7fd);
    box-shadow: 0 50px 90px -40px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); transform-origin: 50% 50%; }
  .r10-vp { position: absolute; left: 70px; top: 328px; width: 940px; height: 528px; border-radius: 25px; overflow: hidden; background: linear-gradient(180deg, #dfe8f6, #eef3fb); transform-origin: 50% 50%; }
  .r10-stage { position: absolute; left: 0; top: 0; width: 940px; height: 528px; }
  .r10-streak { position: absolute; left: 0; top: 0; width: 940px; height: 528px; display: block; opacity: 0;
    background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,.85) 45%, rgba(220,232,252,.9) 55%, rgba(255,255,255,0)); }
  .r10-dv { position: absolute; left: 0; top: 0; width: 0; height: 528px; opacity: 0; }
  .r10-dv i { position: absolute; left: -2.5px; top: 0; width: 5px; height: 528px; display: block; background: #ffffff; box-shadow: 0 0 0 1px rgba(10,13,44,.08), 0 0 22px 4px rgba(160,200,255,.85); }
  .r10-dv b { position: absolute; left: -30px; top: 234px; width: 60px; height: 60px; border-radius: 50%; display: block; background: #ffffff; color: #294b77;
    box-shadow: 0 10px 24px -8px rgba(10,13,44,.55), 0 0 0 4px rgba(255,255,255,.55); }
  .r10-dv b svg { position: absolute; left: 15px; top: 15px; width: 30px; height: 30px; display: block; }
  .r10-lb { position: absolute; top: 18px; height: 46px; padding: 0 20px 0 50px; border-radius: 23px; font: 700 18px/46px Poppins, sans-serif; letter-spacing: .1em; white-space: nowrap; transform-origin: 50% 50%; }
  .r10-lb svg { position: absolute; left: 17px; top: 12px; width: 22px; height: 22px; display: block; }
  .r10-lbA { left: 18px; background: rgba(255,255,255,.94); color: #0a0d2c; box-shadow: 0 10px 22px -12px rgba(10,13,44,.6); }
  .r10-lbB { right: 18px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff; box-shadow: 0 12px 24px -10px rgba(10,13,44,.75), inset 0 0 0 1.5px rgba(255,255,255,.14); }
  .r10-il { position: absolute; left: 18px; top: 450px; height: 34px; padding: 0 14px 0 38px; border-radius: 17px; background: rgba(10,13,44,.55); color: #ffffff;
    font: 700 14px/34px Poppins, sans-serif; letter-spacing: .16em; white-space: nowrap; }
  .r10-il svg { position: absolute; left: 13px; top: 8px; width: 18px; height: 18px; display: block; }
  .r10-pp { position: absolute; left: 150px; top: 842px; width: 780px; height: 76px; border-radius: 38px; background: linear-gradient(180deg, #ffffff, #f6f8fd); transform-origin: 50% 50%;
    box-shadow: 0 24px 44px -20px rgba(10,13,44,.6), 0 0 0 1.5px rgba(10,13,44,.07); font-family: Poppins, sans-serif; }
  .r10-pp .ic { position: absolute; left: 14px; top: 14px; width: 48px; height: 48px; border-radius: 50%; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff; }
  .r10-pp .ic svg { position: absolute; left: 12px; top: 12px; width: 24px; height: 24px; display: block; }
  .r10-pp .tx { position: absolute; left: 78px; top: 0; right: 92px; height: 76px; font: 400 27px/76px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; overflow: hidden; }
  .r10-pp .tx i { font-style: normal; }
  .r10-pp .ph { color: #9aa7c0; }
  .r10-pp .ca { display: inline-block; width: 3px; height: 34px; margin-left: 3px; vertical-align: -7px; border-radius: 2px; background: #3a6fe0; }
  .r10-pp .sd { position: absolute; right: 12px; top: 12px; width: 52px; height: 52px; border-radius: 50%; background: #c9d4e6; color: #ffffff; }
  .r10-pp .sd i.on { position: absolute; inset: 0; border-radius: 50%; background: linear-gradient(135deg, #3a6fe0, #294b77); box-shadow: 0 10px 20px -8px rgba(58,111,224,.9); }
  .r10-pp .sd svg { position: absolute; left: 13px; top: 13px; width: 26px; height: 26px; display: block; }
  .r10-sub { position: absolute; top: 74px; height: 36px; padding: 0 16px 0 42px; border-radius: 18px; font: 700 17px/36px Poppins, sans-serif; white-space: nowrap;
    background: rgba(255,255,255,.92); color: #294b77; box-shadow: 0 8px 18px -10px rgba(10,13,44,.5); transform-origin: 50% 0; }
  .r10-sub svg { position: absolute; left: 14px; top: 8px; width: 20px; height: 20px; display: block; }
  .r10-subA { left: 18px; } .r10-subB { right: 18px; }
  .r10-th { position: absolute; overflow: hidden; border-radius: 18px; background: #dfe8f6; }
  .r10-th > .r10-cp { transform-origin: 0 0; }
  .r10-grad { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .r10-card { position: absolute; border-radius: 30px; background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 34px 64px -30px rgba(10,13,44,.5), 0 0 0 1.5px rgba(10,13,44,.07); transform-origin: 50% 50%; }
  `;
  const st = document.createElement("style"); st.textContent = css; (document.head || document.documentElement).appendChild(st);
  // a scaled copy (thumbnail): w px wide, the 940x528 copy scaled into it; dx/dy shift the crop (copy px)
  const thumb = (p, inner, w, h, s, dx, dy) => `<div class="r10-th" id="${p}-th" style="width:${w}px;height:${h}px"><div class="r10-cp" id="${p}-w" style="transform:translate(${dx || 0}px,${dy || 0}px) scale(${s})">${inner}</div></div>`;
  // a sub-label chip under VIDEO ASLI (side A) or HASIL EDIT AI (side B)
  const sub = (id, side, ic, txt) => `<div class="r10-sub r10-sub${side}" id="${id}">${svg(ic, 2.4)}<span>${txt}</span></div>`;
  // an annotation layer that rides the footage (same scale + parallax as layer `key`): give its prefix to footage()
  const overlay = (p, inner, key) => `<div class="r10-cp" id="${p}-w"><div class="r10-sc" id="${p}">${LY(p, key || "mk", SV(inner))}</div></div>`;
  window.R10 = { sub, overlay, ICO, svg, H, PK, park, street, shelf, copy, player, prompt, type, untype, pinPrompt, wipe, clip, footage, thumb, FR, person };
})();

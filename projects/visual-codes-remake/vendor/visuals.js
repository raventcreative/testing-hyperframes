// 15 mini visuals (900x450 SVG) — one per code. Elements with data-o build in order:
//   .dr = stroke draws on (pathLength=1), .pop = scales in, .fd = fades/rises in.
// Optional life(tl, card, t0, dur) adds the per-visual motion after the build. All deterministic.
(function () {
  const C = "#01ccf7", W = "#ffffff", DIM = "rgba(255,255,255,.45)", F = "rgba(1,204,247,.16)";
  const css = `<style>
    .card .dr{fill:none;stroke-dasharray:1 1;stroke-dashoffset:1;stroke-linecap:round;stroke-linejoin:round}
    .card .pop,.card .fd{opacity:0}
    .card text{font-family:Poppins,sans-serif;fill:#fff;font-size:24px}
    .card text.b{font-weight:700}.card text.c{fill:${C}}.card text.d{fill:rgba(255,255,255,.6)}
    .card text.n{fill:#061334;font-weight:700}
  </style>`;
  const svg = (inner) => `<svg width="900" height="450" viewBox="0 0 900 450">${inner}</svg>`;
  const PL = 'pathLength="1"';
  // handwriting-like scribble
  function scrib(x, y, w, amp, sd) {
    let d = `M${x} ${y}`, cx = x, s = sd;
    while (cx < x + w) { s = (s * 9301 + 49297) % 233280; const r = s / 233280; const step = 14 + r * 12; const a = amp * (0.5 + r);
      d += ` q${step / 2} ${-a} ${step} 0`; cx += step; if (r > 0.82) { d += ` m10 0`; cx += 10; } }
    return d;
  }
  const V = [];

  // 01 blueprint
  V.push({ svg: svg(`<defs><pattern id="bp" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M30 0H0V30" fill="none" stroke="rgba(255,255,255,.10)" stroke-width="1.5"/></pattern></defs>
    <rect class="fd" data-o="0" width="900" height="450" fill="url(#bp)"/>
    <text class="fd b c" data-o="0" x="40" y="56">SISTEM AI · v1</text>
    <rect class="dr" data-o="1" ${PL} x="330" y="125" width="240" height="200" rx="18" stroke="${W}" stroke-width="3"/>
    <rect class="dr" data-o="2" ${PL} x="380" y="175" width="140" height="100" rx="10" stroke="${C}" stroke-width="3"/>
    <path class="dr" data-o="3" ${PL} d="M330 160h-24M330 200h-24M330 240h-24M330 280h-24M570 160h24M570 200h24M570 240h24M570 280h24M380 125v-20M450 125v-20M520 125v-20M380 325v20M450 325v20M520 325v20" stroke="${W}" stroke-width="3"/>
    <text class="fd b" data-o="4" x="450" y="234" text-anchor="middle" font-size="26">MODEL</text>
    <rect class="dr" data-o="5" ${PL} x="50" y="186" width="170" height="78" rx="12" stroke="${W}" stroke-width="3"/>
    <text class="fd" data-o="6" x="135" y="234" text-anchor="middle">INPUT</text>
    <path class="dr" data-o="6" ${PL} d="M224 225h76M290 215l12 10-12 10" stroke="${C}" stroke-width="4"/>
    <rect class="dr" data-o="7" ${PL} x="680" y="186" width="170" height="78" rx="12" stroke="${W}" stroke-width="3"/>
    <text class="fd" data-o="8" x="765" y="234" text-anchor="middle">OUTPUT</text>
    <path class="dr" data-o="7" ${PL} d="M600 225h76M666 215l12 10-12 10" stroke="${C}" stroke-width="4"/>
    <path class="dr" data-o="9" ${PL} d="M330 395h240M330 383v24M570 383v24" stroke="${DIM}" stroke-width="2" stroke-dasharray="6 6"/>
    <text class="fd d" data-o="9" x="450" y="428" text-anchor="middle" font-size="20">240 × 200</text>`) });

  // 02 roadmap
  V.push({ svg: svg(`<path id="rmp" class="dr" data-o="0" ${PL} d="M70 370 C 220 370, 200 150, 360 160 S 560 340, 660 260 S 780 100, 840 100" stroke="${C}" stroke-width="10"/>
    <path class="dr" data-o="1" ${PL} d="M70 370 C 220 370, 200 150, 360 160 S 560 340, 660 260 S 780 100, 840 100" stroke="rgba(255,255,255,.55)" stroke-width="2" stroke-dasharray="2 14"/>
    ${[[70, 370, "Dasar"], [360, 160, "Prompt"], [660, 260, "Workflow"], [840, 100, "Jago"]].map(([x, y, l], i) => `
      <g class="pop" data-o="${2 + i * 1.2}"><circle cx="${x}" cy="${y}" r="26" fill="${C}"/><text class="n" x="${x}" y="${y + 9}" text-anchor="middle" font-size="24">${i + 1}</text></g>
      <text class="fd b" data-o="${2.5 + i * 1.2}" x="${Math.min(800, Math.max(90, x))}" y="${y > 300 ? y - 44 : y + 66}" text-anchor="middle">${l}</text>`).join("")}
    <circle id="rmdot" cx="70" cy="370" r="13" fill="${W}" opacity="0" style="filter:drop-shadow(0 0 10px #01ccf7)"/>`),
    life(tl, card, t0, dur) {
      const p = card.querySelector("#rmp"), dot = card.querySelector("#rmdot"), L = p.getTotalLength(), o = { u: 0 };
      tl.fromTo(o, { u: 0 }, { u: 1, duration: Math.max(0.6, dur - 0.9), ease: "power1.inOut", immediateRender: false,
        onUpdate: () => { const q = p.getPointAtLength(o.u * L); dot.setAttribute("cx", q.x); dot.setAttribute("cy", q.y); } }, t0 + 0.7);
      tl.fromTo(dot, { opacity: 0 }, { opacity: 1, duration: 0.2, immediateRender: false }, t0 + 0.7);
    } });

  // 03 handwritten
  V.push({ svg: svg(`<g transform="rotate(-2 450 225)"><rect class="fd" data-o="0" x="150" y="28" width="600" height="394" rx="10" fill="#f4f8ff"/>
    ${[110, 160, 210, 260, 310, 360].map((y) => `<path class="fd" data-o="0" d="M170 ${y + 8}h560" stroke="rgba(1,120,220,.22)" stroke-width="2"/>`).join("")}
    <path class="fd" data-o="0" d="M210 40v370" stroke="rgba(230,80,80,.35)" stroke-width="2"/>
    <rect class="pop" data-o="5" x="232" y="198" width="300" height="26" rx="6" fill="rgba(1,204,247,.45)"/>
    <path class="dr" data-o="1" ${PL} d="${scrib(232, 102, 260, 16, 3)}" stroke="#14235e" stroke-width="5"/>
    <path class="dr" data-o="2" ${PL} d="${scrib(232, 162, 460, 9, 11)}" stroke="#14235e" stroke-width="3"/>
    <path class="dr" data-o="3" ${PL} d="${scrib(232, 212, 420, 9, 29)}" stroke="#14235e" stroke-width="3"/>
    <path class="dr" data-o="4" ${PL} d="${scrib(232, 262, 380, 9, 47)}" stroke="#14235e" stroke-width="3"/>
    <path class="dr" data-o="4.6" ${PL} d="${scrib(232, 312, 300, 9, 71)}" stroke="#14235e" stroke-width="3"/>
    <ellipse class="dr" data-o="6" ${PL} cx="640" cy="262" rx="78" ry="34" stroke="${C}" stroke-width="5"/>
    <path class="dr" data-o="7" ${PL} d="M600 360c40 10 80-6 110-40m-20 0l22-2-4 22" stroke="${C}" stroke-width="5"/></g>`) });

  // 04 decision matrix
  const cols = ["Harga", "Cepat", "Mudah", "Skor"], rowsM = [["Opsi A", [.3, .6, .4], "6"], ["Opsi B", [.8, .7, .9], "9"], ["Opsi C", [.5, .3, .6], "5"]];
  V.push({ svg: svg(`${cols.map((c, j) => `<text class="fd b c" data-o="0" x="${330 + j * 140}" y="80" text-anchor="middle">${c}</text>`).join("")}
    ${rowsM.map(([n, v, s], r) => `<text class="fd b" data-o="${1 + r}" x="100" y="${168 + r * 95}">${n}</text>
      ${v.map((x, j) => `<rect class="pop" data-o="${1 + r + j * 0.25}" x="${270 + j * 140}" y="${125 + r * 95}" width="120" height="70" rx="12" fill="rgba(1,204,247,${(0.12 + x * 0.6).toFixed(2)})"/>
        <text class="fd b" data-o="${1.3 + r + j * 0.25}" x="${330 + j * 140}" y="${169 + r * 95}" text-anchor="middle">${Math.round(x * 10)}</text>`).join("")}
      <rect class="pop" data-o="${1.8 + r}" x="690" y="${125 + r * 95}" width="120" height="70" rx="12" fill="rgba(255,255,255,.12)"/>
      <text class="fd b c" data-o="${2 + r}" x="750" y="${171 + r * 95}" text-anchor="middle" font-size="32">${s}</text>`).join("")}
    <rect class="dr" data-o="5" ${PL} x="80" y="214" width="742" height="92" rx="16" stroke="${C}" stroke-width="5"/>
    <g class="pop" data-o="5.6"><circle cx="845" cy="260" r="26" fill="${C}"/><path d="M833 260l9 9 16-18" stroke="#061334" stroke-width="5" fill="none" stroke-linecap="round"/></g>`) });

  // 05 flowchart
  V.push({ svg: svg(`<rect class="pop" data-o="0" x="40" y="70" width="160" height="70" rx="35" fill="${C}"/><text class="n" x="120" y="114" text-anchor="middle" font-size="24">Mulai</text>
    <path class="dr" data-o="1" ${PL} d="M200 105h80M270 95l12 10-12 10" stroke="${W}" stroke-width="4"/>
    <rect class="dr" data-o="1.6" ${PL} x="290" y="60" width="180" height="90" rx="14" stroke="${W}" stroke-width="3"/><text class="fd b" data-o="2" x="380" y="114" text-anchor="middle">Proses</text>
    <path class="dr" data-o="2.6" ${PL} d="M470 105h70M530 95l12 10-12 10" stroke="${W}" stroke-width="4"/>
    <path class="dr" data-o="3.2" ${PL} d="M620 40l75 65-75 65-75-65z" stroke="${C}" stroke-width="4"/><text class="fd b" data-o="3.6" x="620" y="114" text-anchor="middle">Cek?</text>
    <path class="dr" data-o="4.2" ${PL} d="M695 105h50M735 95l12 10-12 10" stroke="${W}" stroke-width="4"/><text class="fd c b" data-o="4.4" x="715" y="88" text-anchor="middle" font-size="20">Ya</text>
    <rect class="pop" data-o="4.8" x="750" y="70" width="130" height="70" rx="35" fill="${W}"/><text class="n" x="815" y="114" text-anchor="middle" font-size="22">Selesai</text>
    <path class="dr" data-o="5.2" ${PL} d="M620 170v90M610 250l10 12 10-12" stroke="${W}" stroke-width="4"/><text class="fd d" data-o="5.4" x="650" y="222" font-size="20">Tidak</text>
    <rect class="dr" data-o="5.8" ${PL} x="530" y="270" width="180" height="80" rx="14" stroke="${W}" stroke-width="3"/><text class="fd b" data-o="6.2" x="620" y="318" text-anchor="middle">Perbaiki</text>
    <path class="dr" data-o="6.6" ${PL} d="M530 310H380V160M370 170l10-12 10 12" stroke="${C}" stroke-width="4" stroke-dasharray="1 0"/>`) });

  // 06 infographic
  V.push({ svg: svg(`<circle class="fd" data-o="0" cx="210" cy="225" r="120" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="34"/>
    <circle id="dnt" cx="210" cy="225" r="120" fill="none" stroke="${C}" stroke-width="34" ${PL} stroke-dasharray="1 1" stroke-dashoffset="1" transform="rotate(-90 210 225)" stroke-linecap="round"/>
    <text id="pct" class="b" x="210" y="244" text-anchor="middle" font-size="60">0%</text>
    <text class="fd d" data-o="1" x="210" y="290" text-anchor="middle" font-size="20">lebih paham</text>
    ${[0.45, 0.7, 0.55, 0.92].map((h, i) => `<rect class="bar6" x="${430 + i * 110}" y="${380 - h * 280}" width="70" height="${h * 280}" rx="10" fill="${i === 3 ? C : "rgba(255,255,255,.35)"}"/>
      <text class="fd d" data-o="${2 + i * 0.5}" x="${465 + i * 110}" y="420" text-anchor="middle" font-size="20">${["Sen", "Sel", "Rab", "Kam"][i]}</text>`).join("")}
    <path class="dr" data-o="5" ${PL} d="M465 190L575 120 685 165 795 60" stroke="${W}" stroke-width="4"/>`),
    life(tl, card, t0, dur) {
      const o = { v: 0 }, pct = card.querySelector("#pct");
      tl.fromTo(card.querySelector("#dnt"), { strokeDashoffset: 1 }, { strokeDashoffset: 0.13, duration: 0.9, ease: "power3.out", immediateRender: false }, t0);
      tl.fromTo(o, { v: 0 }, { v: 87, duration: 0.9, ease: "power3.out", immediateRender: false, onUpdate: () => { pct.textContent = Math.round(o.v) + "%"; } }, t0);
      tl.fromTo(card.querySelectorAll(".bar6"), { scaleY: 0, transformOrigin: "50% 100%" }, { scaleY: 1, duration: 0.5, ease: "back.out(1.6)", stagger: 0.1, immediateRender: false }, t0 + 0.15);
      tl.set(card.querySelectorAll(".bar6"), { scaleY: 0, transformOrigin: "50% 100%" }, 0);
    } });

  // 07 canvas (one-page board)
  const cv = [[40, 40, 190, 370, "Masalah"], [250, 40, 190, 175, "Solusi"], [250, 235, 190, 175, "Metrik"], [460, 40, 190, 370, "Nilai Unik"], [670, 40, 190, 175, "Channel"], [670, 235, 190, 175, "Target"]];
  V.push({ svg: svg(cv.map(([x, y, w, h, l], i) => `<g class="pop" data-o="${i * 0.5}"><rect x="${x}" y="${y}" width="${w}" height="${h}" rx="14" fill="rgba(255,255,255,.07)" stroke="${C}" stroke-width="2"/>
      <text class="b c" x="${x + 16}" y="${y + 36}" font-size="20">${l}</text></g>
      ${[0, 1].map((k) => `<rect class="pop" data-o="${3 + i * 0.35 + k * 0.2}" x="${x + 16 + k * 70}" y="${y + 56 + k * 18}" width="60" height="56" rx="6" fill="${k ? "rgba(255,255,255,.85)" : "rgba(1,204,247,.85)"}" transform="rotate(${k ? 4 : -3} ${x + 46 + k * 70} ${y + 84})"/>`).join("")}`).join("")) });

  // 08 layers (isometric stack that separates)
  const lay = ["Konsep", "Cara kerja", "Contoh", "Praktik"];
  V.push({ svg: svg(lay.map((l, i) => `<g class="ly" data-k="${i}"><path class="pop" data-o="${i * 0.5}" d="M450 168L650 230 450 292 250 230z" fill="${["rgba(1,204,247,.9)", "rgba(1,204,247,.6)", "rgba(80,150,255,.55)", "rgba(255,255,255,.35)"][i]}" stroke="${W}" stroke-width="2"/></g>
      <g class="lyl" data-k="${i}"><path class="dr" data-o="${3 + i * 0.4}" ${PL} d="M650 ${88 + i * 92}h70" stroke="${W}" stroke-width="2"/><circle class="pop" data-o="${3 + i * 0.4}" cx="650" cy="${88 + i * 92}" r="6" fill="${C}"/>
      <text class="fd b" data-o="${3.2 + i * 0.4}" x="732" y="${96 + i * 92}">${l}</text></g>`).reverse().join("")),
    life(tl, card, t0) {
      card.querySelectorAll(".ly").forEach((g) => { const k = +g.dataset.k; tl.fromTo(g, { y: 0 }, { y: -142 + k * 92, duration: 0.6, ease: "back.out(1.4)", immediateRender: false }, t0 + 0.55); });
    } });

  // 09 cycle
  const cyN = ["Belajar", "Coba", "Evaluasi", "Ulangi"];
  V.push({ svg: svg(`<g id="cyr">${[0, 1, 2, 3].map((i) => { const a0 = -90 + i * 90 + 18, a1 = a0 + 54, r = 150, p = (a) => [450 + r * Math.cos(a * Math.PI / 180), 225 + r * Math.sin(a * Math.PI / 180)];
      const [x0, y0] = p(a0), [x1, y1] = p(a1); return `<path class="dr" data-o="${1 + i * 0.6}" ${PL} d="M${x0.toFixed(1)} ${y0.toFixed(1)}A${r} ${r} 0 0 1 ${x1.toFixed(1)} ${y1.toFixed(1)}" stroke="${C}" stroke-width="6"/>`; }).join("")}</g>
    ${cyN.map((l, i) => { const a = (-90 + i * 90) * Math.PI / 180, x = 450 + 150 * Math.cos(a), y = 225 + 150 * Math.sin(a);
      return `<g class="pop" data-o="${i * 0.6}"><circle cx="${x}" cy="${y}" r="40" fill="${i === 0 ? C : "rgba(6,19,52,.9)"}" stroke="${C}" stroke-width="3"/><text class="${i === 0 ? "n" : "b"}" x="${x}" y="${y + 8}" text-anchor="middle" font-size="22">${i + 1}</text></g>
      <text class="fd b" data-o="${0.4 + i * 0.6}" x="${x + (i === 1 || i === 2 ? 58 : i === 3 ? -58 : 0)}" y="${y + (i === 0 ? -56 : 8)}" text-anchor="${i === 1 || i === 2 ? "start" : i === 3 ? "end" : "middle"}">${l}</text>`; }).join("")}
    <text class="fd b c" data-o="3.5" x="450" y="234" text-anchor="middle" font-size="30">SIKLUS</text>
    <circle id="cyd" cx="450" cy="75" r="12" fill="${W}" opacity="0" style="filter:drop-shadow(0 0 10px #01ccf7)"/>`),
    life(tl, card, t0, dur) {
      const d = card.querySelector("#cyd"), o = { a: -90 };
      tl.fromTo(d, { opacity: 0 }, { opacity: 1, duration: 0.2, immediateRender: false }, t0 + 0.9);
      tl.fromTo(o, { a: -90 }, { a: 270, duration: Math.max(0.8, dur - 1.0), ease: "power1.inOut", immediateRender: false,
        onUpdate: () => { d.setAttribute("cx", 450 + 150 * Math.cos(o.a * Math.PI / 180)); d.setAttribute("cy", 225 + 150 * Math.sin(o.a * Math.PI / 180)); } }, t0 + 0.9);
    } });

  // 10 diagram (labelled lightbulb)
  const dg = [[410, 150, 170, 90, "Kaca", "end"], [470, 170, 730, 90, "Filamen", "start"], [420, 300, 170, 330, "Ulir", "end"], [470, 340, 730, 360, "Kontak", "start"]];
  V.push({ svg: svg(`<path class="dr" data-o="0" ${PL} d="M450 60c-70 0-115 52-115 110 0 45 25 70 45 95 12 15 15 30 15 45h110c0-15 3-30 15-45 20-25 45-50 45-95 0-58-45-110-115-110z" stroke="${W}" stroke-width="4" fill="rgba(1,204,247,.08)"/>
    <path class="dr" data-o="1" ${PL} d="M425 300v-80l25 30 25-30v80" stroke="${C}" stroke-width="4"/>
    <path class="dr" data-o="1.5" ${PL} d="M400 315h100M405 335h90M412 355h76M430 378h40" stroke="${W}" stroke-width="5"/>
    ${dg.map(([x1, y1, x2, y2, l, a], i) => `<path class="dr" data-o="${2.5 + i * 0.5}" ${PL} d="M${x1} ${y1}L${(x1 + x2) / 2} ${y2}H${x2}" stroke="${C}" stroke-width="2.5"/>
      <circle class="pop" data-o="${2.5 + i * 0.5}" cx="${x1}" cy="${y1}" r="7" fill="${C}"/>
      <text class="fd b" data-o="${2.9 + i * 0.5}" x="${x2 + (a === "end" ? -12 : 12)}" y="${y2 + 9}" text-anchor="${a}" font-size="28">${l}</text>`).join("")}`) });

  // 11 sketchnotes
  V.push({ svg: svg(`<circle class="pop" data-o="0" cx="160" cy="130" r="70" fill="rgba(1,204,247,.25)"/>
    <path class="dr" data-o="0.5" ${PL} d="M160 70l17 38 41 4-31 27 9 40-36-21-36 21 9-40-31-27 41-4z" stroke="${W}" stroke-width="4"/>
    <path class="dr" data-o="1.5" ${PL} d="M300 70h250a20 20 0 0 1 20 20v90a20 20 0 0 1-20 20H380l-40 34 6-34h-46a20 20 0 0 1-20-20V90a20 20 0 0 1 20-20z" stroke="${W}" stroke-width="4"/>
    <text class="fd b c" data-o="2.2" x="425" y="146" text-anchor="middle" font-size="44">IDE!</text>
    <path class="dr" data-o="3" ${PL} d="M640 90c-20 60 40 80 20 140" stroke="${C}" stroke-width="5"/><path class="dr" data-o="3.4" ${PL} d="M645 215l15 20 18-18" stroke="${C}" stroke-width="5"/>
    <rect class="pop" data-o="3.8" x="720" y="60" width="130" height="130" rx="10" fill="rgba(255,255,255,.9)" transform="rotate(6 785 125)"/>
    <path class="dr" data-o="4.2" ${PL} d="${scrib(735, 110, 90, 7, 5)}" stroke="#14235e" stroke-width="3"/><path class="dr" data-o="4.4" ${PL} d="${scrib(735, 145, 80, 7, 9)}" stroke="#14235e" stroke-width="3"/>
    <circle class="dr" data-o="5" ${PL} cx="200" cy="330" r="55" stroke="${W}" stroke-width="4"/><path class="dr" data-o="5.4" ${PL} d="M180 318v2M220 318v2M175 345c15 18 35 18 50 0" stroke="${W}" stroke-width="5"/>
    <path class="dr" data-o="6" ${PL} d="${scrib(320, 320, 480, 12, 21)}" stroke="${W}" stroke-width="4"/>
    <path class="dr" data-o="6.6" ${PL} d="M320 360c120 14 300 14 480-6" stroke="${C}" stroke-width="7"/>`),
    life(tl, card, t0, dur) { tl.fromTo(card.querySelector("svg"), { rotation: -1 }, { rotation: 1, duration: 0.5, ease: "sine.inOut", yoyo: true, repeat: Math.max(1, Math.floor(dur / 0.5)), immediateRender: false, transformOrigin: "50% 50%" }, t0); } });

  // 12 iceberg
  V.push({ svg: svg(`<rect class="fd" data-o="0" x="0" y="150" width="900" height="300" fill="rgba(1,204,247,.14)"/>
    <g id="ib"><path class="pop" data-o="1" d="M450 60l60 90H390z" fill="${W}"/>
    <path class="pop" data-o="2" d="M390 150h120l90 90-40 120-110 70-120-60-50-130z" fill="rgba(1,204,247,.42)" stroke="${C}" stroke-width="3"/></g>
    <path id="wav" class="dr" data-o="0.5" ${PL} d="M0 150q37 -12 75 0t75 0 75 0 75 0 75 0 75 0 75 0 75 0 75 0 75 0 75 0 75 0 75 0" stroke="${W}" stroke-width="4"/>
    <text class="fd b" data-o="3" x="560" y="98" font-size="30">Kelihatan</text><path class="dr" data-o="3" ${PL} d="M550 90h-50" stroke="${W}" stroke-width="2"/>
    <text class="fd b c" data-o="4" x="640" y="300" font-size="32">Tersembunyi</text><path class="dr" data-o="4" ${PL} d="M630 292h-60" stroke="${C}" stroke-width="2"/>
    <text class="fd d" data-o="4.5" x="640" y="336" font-size="22">90% ada di bawah</text>`),
    life(tl, card, t0, dur) {
      tl.fromTo(card.querySelector("#ib"), { y: 0 }, { y: 8, duration: 0.6, ease: "sine.inOut", yoyo: true, repeat: Math.max(1, Math.floor(dur / 0.6)), immediateRender: false }, t0 + 0.5);
      tl.fromTo(card.querySelector("#wav"), { x: 0 }, { x: -75, duration: dur, ease: "none", immediateRender: false }, t0 + 0.4);
    } });

  // 13 exploded view
  const ex = [["Tutup", 85], ["Ring", 175], ["Pegas", 265], ["Basis", 365]];
  V.push({ svg: svg(`<path class="dr" data-o="0" ${PL} d="M450 30v400" stroke="${DIM}" stroke-width="2" stroke-dasharray="1 0"/>
    <g class="xp" data-y="85"><g class="pop" data-o="0.4"><ellipse cx="450" cy="70" rx="110" ry="26" fill="${C}"/><rect x="340" y="70" width="220" height="30" fill="rgba(1,204,247,.6)"/><ellipse cx="450" cy="100" rx="110" ry="26" fill="rgba(1,204,247,.6)"/></g></g>
    <g class="xp" data-y="175"><g class="pop" data-o="0.8"><ellipse cx="450" cy="175" rx="90" ry="22" fill="none" stroke="${W}" stroke-width="12"/></g></g>
    <g class="xp" data-y="265"><path class="dr" data-o="1.2" ${PL} d="M380 235l140 10-140 10 140 10-140 10 140 10-140 10" stroke="${C}" stroke-width="7"/></g>
    <g class="xp" data-y="365"><g class="pop" data-o="1.6"><rect x="360" y="345" width="180" height="40" rx="8" fill="rgba(255,255,255,.75)"/><ellipse cx="450" cy="345" rx="90" ry="18" fill="${W}"/></g></g>
    ${ex.map(([l, y], i) => `<path class="dr" data-o="${3 + i * 0.35}" ${PL} d="M580 ${y}h90" stroke="${C}" stroke-width="2"/><text class="fd b" data-o="${3.2 + i * 0.35}" x="684" y="${y + 9}">${l}</text>
      <text class="fd d" data-o="${3.2 + i * 0.35}" x="300" y="${y + 9}" text-anchor="end" font-size="20">0${i + 1}</text>`).join("")}`),
    life(tl, card, t0) {
      card.querySelectorAll(".xp").forEach((g) => { const y = +g.dataset.y; tl.fromTo(g, { y: 225 - y }, { y: 0, duration: 0.7, ease: "back.out(1.3)", immediateRender: false }, t0 + 0.3); tl.set(g, { y: 225 - y }, 0); });
    } });

  // 14 tree
  const tr = [[450, 250, 270, 150], [450, 250, 630, 150], [270, 150, 160, 70], [270, 150, 340, 60], [630, 150, 560, 60], [630, 150, 750, 70]];
  const lv = [[160, 70, "Detail"], [340, 60, "Detail"], [560, 60, "Detail"], [750, 70, "Detail"], [270, 150, "Sub"], [630, 150, "Sub"]];
  V.push({ svg: svg(`<path class="dr" data-o="0" ${PL} d="M450 430V250" stroke="${W}" stroke-width="14"/>
    <path class="dr" data-o="0.5" ${PL} d="M450 430c-40 0-70 10-100 4M450 430c40 0 80 10 110 2M450 430c-10 10-20 14-40 16" stroke="${C}" stroke-width="4"/>
    ${tr.map(([x1, y1, x2, y2], i) => `<path class="dr" data-o="${1 + (i < 2 ? 0 : 1)}" ${PL} d="M${x1} ${y1}Q${(x1 + x2) / 2} ${y1} ${x2} ${y2}" stroke="${W}" stroke-width="${i < 2 ? 8 : 5}"/>`).join("")}
    ${lv.map(([x, y, l], i) => `<g class="pop" data-o="${i < 4 ? 3 + i * 0.3 : 2}"><circle cx="${x}" cy="${y}" r="${i < 4 ? 40 : 40}" fill="${i < 4 ? C : "rgba(6,19,52,.9)"}" stroke="${C}" stroke-width="3"/>
      <text class="${i < 4 ? "n" : "b"}" x="${x}" y="${y + 7}" text-anchor="middle" font-size="${i < 4 ? 15 : 20}">${l}</text></g>`).join("")}
    <g class="pop" data-o="0.8"><rect x="370" y="380" width="160" height="50" rx="25" fill="${C}"/><text class="n" x="450" y="413" text-anchor="middle" font-size="22">Akar</text></g>`) });

  // 15 timeline
  const yrs = [["1950", "Mulai"], ["1980", "Tumbuh"], ["2000", "Internet"], ["2015", "Mobile"], ["2025", "AI"]];
  V.push({ svg: svg(`<path class="dr" data-o="0" ${PL} d="M60 240H840" stroke="${W}" stroke-width="6"/><path class="dr" data-o="0.6" ${PL} d="M826 226l16 14-16 14" stroke="${W}" stroke-width="6"/>
    ${yrs.map(([y, l], i) => { const x = 110 + i * 170; return `<g class="pop" data-o="${1 + i * 0.5}"><circle cx="${x}" cy="240" r="${i === 4 ? 24 : 16}" fill="${i === 4 ? C : W}"/></g>
      <text class="fd b ${i === 4 ? "c" : ""}" data-o="${1.2 + i * 0.5}" x="${x}" y="${i % 2 ? 320 : 190}" text-anchor="middle" font-size="34">${y}</text>
      <text class="fd d" data-o="${1.4 + i * 0.5}" x="${x}" y="${i % 2 ? 355 : 150}" text-anchor="middle" font-size="22">${l}</text>`; }).join("")}
    <path id="tmk" d="M98 200h24l-12 18z" fill="${C}" opacity="0"/>`),
    life(tl, card, t0, dur) {
      const m = card.querySelector("#tmk");
      tl.fromTo(m, { opacity: 0, x: 0 }, { opacity: 1, x: 0, duration: 0.2, immediateRender: false }, t0 + 1);
      tl.fromTo(m, { x: 0 }, { x: 680, duration: Math.max(0.6, dur - 1.1), ease: "power2.inOut", immediateRender: false }, t0 + 1.1);
    } });

  function build(tl, card, t0, dur) {
    const els = Array.from(card.querySelectorAll("[data-o]"));
    const maxO = Math.max(...els.map((e) => +e.dataset.o));
    const step = Math.min(0.14, Math.max(0.06, (Math.min(dur, 1.9) - 0.5) / (maxO + 1)));
    els.forEach((e) => {
      const at = t0 + +e.dataset.o * step;
      if (e.classList.contains("dr")) tl.fromTo(e, { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.45, ease: "power2.out", immediateRender: false }, at);
      else if (e.classList.contains("pop")) { tl.fromTo(e, { opacity: 0, scale: 0, transformOrigin: "50% 50%" }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2)", immediateRender: false }, at); }
      else if (e.classList.contains("fd")) tl.fromTo(e, { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.3, ease: "power2.out", immediateRender: false }, at);
    });
    return step;
  }
  window.VISUALS = V.map((v) => ({ svg: css + v.svg, build: (tl, card, t0, dur) => { const step = build(tl, card, t0, dur); if (v.life) v.life(tl, card, t0, dur, step); } }));
})();

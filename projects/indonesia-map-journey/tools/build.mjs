// Generates compositions/<city>.html, data/plan.js and index.html from data/plan.json + data/photos.json.
// Usage: node tools/build.mjs   (run from the project root)
import fs from "node:fs";

const W = 1920, H = 1080, SAFE = 80;
const plan = JSON.parse(fs.readFileSync("data/plan.json", "utf8"));
const photos = Object.fromEntries(JSON.parse(fs.readFileSync("data/photos.json", "utf8")).map((p) => [p.id, p]));
const geoHead = fs.readFileSync("assets/maps/geo.js", "utf8").slice(0, 4000);
const num = (k) => Number(new RegExp(`"${k}":(-?[\\d.]+)`).exec(geoHead)[1]);
const S = num("S"), LON0 = num("LON0"), LAT0 = num("LAT0");
const baliBBox = JSON.parse(/"baliBBox":(\[[^\]]+\])/.exec(fs.readFileSync("assets/maps/geo.js", "utf8"))[1]);

// ---- projection (identical to index.html) ----
const M = (lat) => Math.log(Math.tan(Math.PI / 4 + (lat * Math.PI) / 360));
const proj = (lon, lat) => [(lon - LON0) * S, (M(LAT0) - M(lat)) * S * (180 / Math.PI)];
const kOf = (span) => W / (span * S);

// camera state: world centre (ux, uy) + visible world width w
function stateFor(city) {
  const k = kOf(city.span);
  const [x, y] = proj(city.lon, city.lat);
  return { ux: x - (city.P[0] - W / 2) / k, uy: y - (city.P[1] - H / 2) / k, w: W / k };
}
const nat = plan.national;
const [nx, ny] = proj(nat.lon, nat.lat);
const NATIONAL = { ux: nx, uy: ny, w: W / kOf(nat.span) };
const OPEN = { ux: nx, uy: ny, w: NATIONAL.w / plan.opening.zoomFrom };

// ---- city timing ----
const cities = plan.cities.map((c) => {
  const long = c.dur >= 9;
  const A = c.start + (c.arriveOffset ?? (long ? 1.6 : 1.4));
  const hold = c.start + (long ? 7.3 : 6.5);
  return { ...c, A, reveal: A + 0.5, hold, depart: c.start + (long ? 7.72 : 6.92), state: stateFor(c), k: kOf(c.span) };
});
const byId = Object.fromEntries(cities.map((c) => [c.id, c]));

// ---- travel segments ----
const travel = [];
let prev = null;
for (const t of plan.travel) {
  const to = t.to === "national" || t.to === "final" ? NATIONAL : byId[t.to].state;
  const fromState = t.from === "opening" ? NATIONAL : t.from === "national" ? NATIONAL : t.from ? byId[t.from].state : byId[prev].state;
  const fromId = t.from && !["opening", "national"].includes(t.from) ? t.from : t.from ? null : prev;
  const t0 = t.t0 ?? byId[fromId].depart - (t.early ?? 0);
  const t1 = t.t1 ?? byId[t.to].A;
  travel.push({ to: t.to, from: t.from ?? prev, t0, t1, rho: t.rho, a: fromState, b: to });
  prev = byId[t.to] ? t.to : prev;
}
// ---- routes (draw while the camera travels) ----
const routes = plan.routes.map((r) => {
  const seg = travel.find((s) => s.to === r.to);
  const a = byId[r.from], b = byId[r.to];
  const t0 = r.t0 ?? seg.t0 + 0.12, t1 = r.t1 ?? seg.t1 - 0.12;
  return { ...r, t0, t1, a: proj(a.lon, a.lat), b: proj(b.lon, b.lat) };
});

// ---- card geometry ----
const PAD = 10, CAP = 64;
function aspectOf(p) {
  if (p.w && p.h) return p.w / p.h;
  return p.expect === "portrait" ? 2 / 3 : 3 / 2;
}
function rectOf(slot) {
  const p = photos[slot.photo];
  const ar = aspectOf(p);
  let pw = slot.maxW - 2 * PAD, ph = pw / ar;
  const maxPh = slot.maxH - 2 * PAD - CAP;
  if (ph > maxPh) { ph = maxPh; pw = ph * ar; }
  pw = Math.round(pw); ph = Math.round(ph);
  const w = pw + 2 * PAD, h = ph + 2 * PAD + CAP;
  return { x: Math.round(slot.cx - w / 2), y: Math.round(slot.cy - h / 2), w, h, pw, ph };
}
function rayRect(cx, cy, tx, ty, r) {
  // point where segment (cx,cy)->(rect centre) enters rect r
  const rx = r.x + r.w / 2, ry = r.y + r.h / 2;
  const dx = rx - cx, dy = ry - cy;
  let best = 1;
  const cands = [];
  if (dx) { cands.push((r.x - cx) / dx, (r.x + r.w - cx) / dx); }
  if (dy) { cands.push((r.y - cy) / dy, (r.y + r.h - cy) / dy); }
  for (const t of cands) {
    if (t <= 0 || t > 1) continue;
    const px = cx + dx * t, py = cy + dy * t;
    if (px >= r.x - 0.5 && px <= r.x + r.w + 0.5 && py >= r.y - 0.5 && py <= r.y + r.h + 0.5) best = Math.min(best, t);
  }
  return [cx + dx * best, cy + dy * best];
}
function segHitsRect(a, b, r, inset = 0) {
  const R = { x: r.x - inset, y: r.y - inset, w: r.w + 2 * inset, h: r.h + 2 * inset };
  for (let i = 1; i < 40; i++) {
    const t = i / 40, x = a[0] + (b[0] - a[0]) * t, y = a[1] + (b[1] - a[1]) * t;
    if (x > R.x && x < R.x + R.w && y > R.y && y < R.y + R.h) return true;
  }
  return false;
}
const overlap = (a, b) => a.x < b.x + b.w && b.x < a.x + a.w && a.y < b.y + b.h && b.y < a.y + a.h;
const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");

const warnings = [];
const TITLE_PX = 44, TRACK = 0.16;
for (const c of cities) {
  c.rects = c.slots.map(rectOf);
  // anchor geometry (screen space, camera holding at c.state)
  if (c.anchor === "island") {
    const [x0, y1] = proj(baliBBox[0], baliBBox[1]);
    const [x1, y0] = proj(baliBBox[2], baliBBox[3]);
    const sx = (x) => (x - c.state.ux) * c.k + W / 2, sy = (y) => (y - c.state.uy) * c.k + H / 2;
    c.island = { x0: sx(x0), x1: sx(x1), y0: sy(y0), y1: sy(y1) };
    c.ell = { cx: (c.island.x0 + c.island.x1) / 2, cy: (c.island.y0 + c.island.y1) / 2, rx: (c.island.x1 - c.island.x0) / 2 + 34, ry: (c.island.y1 - c.island.y0) / 2 + 34 };
  }
  c.conns = c.rects.map((r) => {
    const o = c.ell ? [c.ell.cx, c.ell.cy] : c.P;
    const E = rayRect(o[0], o[1], 0, 0, r);
    const dx = E[0] - o[0], dy = E[1] - o[1], L = Math.hypot(dx, dy);
    let s;
    if (c.ell) {
      const ang = Math.atan2(dy, dx);
      // ellipse boundary along the direction
      const t = 1 / Math.sqrt((Math.cos(ang) / c.ell.rx) ** 2 + (Math.sin(ang) / c.ell.ry) ** 2);
      s = [o[0] + Math.cos(ang) * t, o[1] + Math.sin(ang) * t];
    } else s = [o[0] + (dx / L) * 22, o[1] + (dy / L) * 22];
    return { s: s.map(Math.round), e: E.map(Math.round) };
  });
  const n = c.title.length;
  const tw = n * TITLE_PX * 0.74 + n * TITLE_PX * TRACK;
  const mkRect = (tx, ty, ta) => ({ x: ta === "middle" ? tx - tw / 2 : ta === "end" ? tx - tw : tx, y: ty - TITLE_PX * 0.5, w: tw, h: TITLE_PX * 1.25 + 14 });
  const titleOk = (R) => R.x >= SAFE && R.x + R.w <= W - SAFE && R.y >= SAFE && R.y + R.h <= H - SAFE - 30 &&
    !c.rects.some((r) => overlap({ x: r.x - 18, y: r.y - 18, w: r.w + 36, h: r.h + 36 }, R)) &&
    !c.conns.some((cn) => segHitsRect(cn.s, cn.e, R, 8)) &&
    !overlap(R, { x: c.P[0] - 26, y: c.P[1] - 26, w: 52, h: 52 });
  if (c.titlePos === "auto") {
    const o = c.ell ? [c.ell.cx, c.ell.cy] : c.P;
    const ex = c.ell ? c.ell.rx : 0, ey = c.ell ? c.ell.ry : 0;
    const cands = [];
    for (const d of [72, 96, 128, 170]) {
      cands.push([o[0], o[1] + ey + d, "middle"], [o[0], o[1] - ey - d + 12, "middle"],
        [o[0] + ex + d * 0.55, o[1] + 14, "start"], [o[0] - ex - d * 0.55, o[1] + 14, "end"],
        [o[0] + ex + d * 0.5, o[1] + ey + d * 0.75, "start"], [o[0] - ex - d * 0.5, o[1] + ey + d * 0.75, "end"],
        [o[0] + ex + d * 0.5, o[1] - ey - d * 0.6, "start"], [o[0] - ex - d * 0.5, o[1] - ey - d * 0.6, "end"]);
    }
    const hit = cands.find(([x, y, a]) => titleOk(mkRect(x, y, a)));
    if (!hit) warnings.push(`${c.id}: no clear title position`);
    c.titlePos = hit ?? [o[0], o[1] + 90, "middle"];
  }
  const [tx, ty, ta] = c.titlePos;
  c.titleRect = mkRect(tx, ty, ta);
  // checks
  c.rects.forEach((r, i) => {
    if (r.x < SAFE || r.y < SAFE * 0.75 || r.x + r.w > W - SAFE || r.y + r.h > H - SAFE * 0.75) warnings.push(`${c.id}: card ${i} outside safe area ${JSON.stringify(r)}`);
    c.rects.forEach((q, j) => { if (j > i && overlap(r, q)) warnings.push(`${c.id}: cards ${i} & ${j} overlap`); });
    if (overlap(r, c.titleRect)) warnings.push(`${c.id}: title overlaps card ${i}`);
    c.conns.forEach((cn, j) => { if (j !== i && segHitsRect(cn.s, cn.e, r, 6)) warnings.push(`${c.id}: connector ${j} crosses card ${i}`); });
    const markerBox = { x: c.P[0] - 30, y: c.P[1] - 30, w: 60, h: 60 };
    if (!c.ell && overlap(r, markerBox)) warnings.push(`${c.id}: card ${i} covers marker`);
  });
  c.conns.forEach((cn, j) => { if (segHitsRect(cn.s, cn.e, c.titleRect, 4)) warnings.push(`${c.id}: connector ${j} crosses title`); });
}

// ---- sub-composition writer ----
function credit(p) {
  if (!p.file) return "Foto belum diunduh";
  return `Foto: ${p.author} · ${p.license} · Wikimedia Commons`;
}
function cityHtml(c) {
  const ns = c.id.slice(0, 3);
  const L = (t) => +(t - c.start).toFixed(3); // local seconds
  const a = L(c.A), r = L(c.reveal), x = L(c.hold);
  const cards = c.slots.map((slot, i) => {
    const p = photos[slot.photo], R = c.rects[i], E = c.conns[i].e;
    const ox = (((E[0] - R.x) / R.w) * 100).toFixed(1), oy = (((E[1] - R.y) / R.h) * 100).toFixed(1);
    const fx = ((p.focus?.[0] ?? 0.5) * 100).toFixed(0), fy = ((p.focus?.[1] ?? 0.5) * 100).toFixed(0);
    const media = p.file
      ? `<img id="${ns}-img${i}" class="${ns}-img" src="${p.file}" alt="${esc(p.label)}" style="object-position:${fx}% ${fy}%;transform-origin:${fx}% ${fy}%">`
      : `<div id="${ns}-img${i}" class="${ns}-img ${ns}-ph"><span data-layout-ignore>FOTO MENUNGGU<br>AKSES WIKIMEDIA</span></div>`;
    const lblLen = p.label.length * 28 * 0.6;
    const lblSize = lblLen > R.w - 2 * PAD ? Math.max(24, Math.floor(((R.w - 2 * PAD) / (p.label.length * 0.6)))) : 28;
    return `    <div id="${ns}-card${i}" class="${ns}-card" style="left:${R.x}px;top:${R.y}px;width:${R.w}px;height:${R.h}px;transform-origin:${ox}% ${oy}%">
      <div class="${ns}-frame" style="width:${R.pw}px;height:${R.ph}px">${media}</div>
      <div class="${ns}-cap"><div class="${ns}-lbl" style="font-size:${lblSize}px">${esc(p.label)}</div><div class="${ns}-cr" data-layout-ignore>${esc(credit(p))}</div></div>
    </div>`;
  }).join("\n");
  const conns = c.conns.map((cn, i) => `      <path id="${ns}-ln${i}u" class="${ns}-lnu" d="M${cn.s[0]} ${cn.s[1]} L${cn.e[0]} ${cn.e[1]}" pathLength="100" />
      <path id="${ns}-ln${i}" class="${ns}-ln" d="M${cn.s[0]} ${cn.s[1]} L${cn.e[0]} ${cn.e[1]}" pathLength="100" />
      <circle id="${ns}-end${i}" class="${ns}-end" cx="${cn.e[0]}" cy="${cn.e[1]}" r="4" />`).join("\n");
  const [tx, ty, ta] = c.titlePos;
  const letters = [...c.title].map((ch, i) => `<span class="${ns}-ch" id="${ns}-ch${i}">${ch === " " ? "&nbsp;" : esc(ch)}</span>`).join("");
  const tiltY = c.slots.map((s, i) => (c.rects[i].x + c.rects[i].w / 2 < (c.ell ? c.ell.cx : c.P[0]) ? 14 : -14));
  const order = [0, 1, 2];
  return `<template>
  <style>
    #root { position: absolute; inset: 0; width: 1920px; height: 1080px; pointer-events: none; font-family: Montserrat, sans-serif; }
    .${ns}-svg { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; overflow: visible; }
    .${ns}-lnu { fill: none; stroke: #FBFCFE; stroke-width: 5; stroke-linecap: round; stroke-dasharray: 100 120; stroke-dashoffset: 110; opacity: 0.9; }
    .${ns}-ln { fill: none; stroke: #294B77; stroke-width: 1.6; stroke-linecap: round; stroke-dasharray: 100 120; stroke-dashoffset: 110; }
    .${ns}-end { fill: #294B77; stroke: #FBFCFE; stroke-width: 2; opacity: 0; }
    .${ns}-card { position: absolute; box-sizing: border-box; padding: ${PAD}px; background: #FBFCFE; border-radius: 6px;
      box-shadow: 0 2px 4px rgba(32,43,59,0.10), 0 18px 38px -10px rgba(32,43,59,0.30); opacity: 0; }
    .${ns}-frame { position: relative; overflow: hidden; border-radius: 3px; background: #E8F0FB; }
    .${ns}-img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; }
    .${ns}-ph { display: flex; align-items: center; justify-content: center; text-align: center;
      background: repeating-linear-gradient(135deg, #E8F0FB 0 18px, #DCE7F7 18px 36px); color: #3A6299;
      font: 600 15px/1.5 Montserrat, sans-serif; letter-spacing: 0.14em; }
    .${ns}-cap { height: ${CAP}px; padding: 10px 4px 0; box-sizing: border-box; }
    .${ns}-lbl { font-weight: 600; font-size: 26px; line-height: 1.05; color: #202B3B; white-space: nowrap; letter-spacing: 0.005em; }
    .${ns}-cr { margin-top: 5px; font-weight: 400; font-size: 13px; line-height: 1.1; color: #3A6299; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; letter-spacing: 0.02em; }
    .${ns}-title { position: absolute; left: ${Math.round(c.titleRect.x)}px; top: ${Math.round(ty - TITLE_PX * 0.62)}px; width: ${Math.round(c.titleRect.w)}px;
      text-align: ${ta === "middle" ? "center" : ta === "end" ? "right" : "left"}; white-space: nowrap;
      font-weight: 700; font-size: ${TITLE_PX}px; line-height: 1.2; letter-spacing: ${TRACK}em; color: #202B3B;
      text-shadow: 0 0 18px rgba(251,252,254,0.95), 0 0 4px rgba(251,252,254,0.9); }
    .${ns}-ch { display: inline-block; opacity: 0; }
    .${ns}-rule { position: absolute; left: ${Math.round(ta === "middle" ? tx - 36 : ta === "start" ? tx + 3 : tx - 75)}px; top: ${Math.round(ty + TITLE_PX * 0.72)}px; width: 72px; height: 2px; background: #294B77; transform-origin: ${ta === "end" ? "100%" : ta === "start" ? "0%" : "50%"} 50%; opacity: 0; }
  </style>
  <div id="root" data-composition-id="${c.id}" data-width="1920" data-height="1080" data-layout-allow-overlap>
    <svg class="${ns}-svg" viewBox="0 0 1920 1080">
${conns}
    </svg>
${cards}
    <div id="${ns}-title" class="${ns}-title">${letters}</div>
    <div id="${ns}-rule" class="${ns}-rule"></div>
  </div>
  <script>
    (function () {
      const tl = gsap.timeline({ paused: true });
      const q = (id) => document.getElementById(id);
      // title: per-letter, light blur, no translate
      tl.fromTo("#${ns}-title .${ns}-ch", { opacity: 0.0, filter: "blur(5px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.32, stagger: 0.035, ease: "power2.out" }, ${(a + 0.12).toFixed(2)});
      tl.fromTo(q("${ns}-rule"), { scaleX: 0, opacity: 0 }, { scaleX: 1, opacity: 1, duration: 0.5, ease: "expo.out" }, ${(a + 0.35).toFixed(2)});
${order.map((i) => {
  const t0 = r + i * 0.2;
  return `      // photo ${i}: connector draws, then the frame unfolds from its endpoint
      tl.fromTo([q("${ns}-ln${i}u"), q("${ns}-ln${i}")], { strokeDashoffset: 110 }, { strokeDashoffset: 0, duration: 0.3, ease: "power2.out" }, ${t0.toFixed(2)});
      tl.fromTo(q("${ns}-end${i}"), { opacity: 0 }, { opacity: 1, duration: 0.12, ease: "none" }, ${(t0 + 0.24).toFixed(2)});
      tl.fromTo(q("${ns}-card${i}"), { scale: 0.06, rotationY: ${tiltY[i]}, rotationX: 5, transformPerspective: 1600 }, { scale: 1, rotationY: 0, rotationX: 0, duration: 0.7, ease: "expo.out" }, ${(t0 + 0.1).toFixed(2)});
      tl.fromTo(q("${ns}-card${i}"), { opacity: 0 }, { opacity: 1, duration: 0.18, ease: "power1.out" }, ${(t0 + 0.1).toFixed(2)});
      tl.fromTo(q("${ns}-img${i}"), { scale: 1.0 }, { scale: 1.035, duration: ${(x - t0).toFixed(2)}, ease: "sine.inOut" }, ${t0.toFixed(2)});`;
}).join("\n")}
      // retract: frames compress toward the destination cluster, then the lines pull back
${[2, 1, 0].map((i, j) => `      tl.to(q("${ns}-card${i}"), { scale: 0.06, rotationY: ${-tiltY[i] * 0.6}, duration: 0.36, ease: "power3.in" }, ${(x + j * 0.06).toFixed(2)});
      tl.to(q("${ns}-card${i}"), { opacity: 0, duration: 0.12, ease: "none" }, ${(x + j * 0.06 + 0.24).toFixed(2)});
      tl.to(q("${ns}-end${i}"), { opacity: 0, duration: 0.08, ease: "none" }, ${(x + j * 0.06 + 0.12).toFixed(2)});
      tl.to([q("${ns}-ln${i}u"), q("${ns}-ln${i}")], { strokeDashoffset: 110, duration: 0.28, ease: "power2.in" }, ${(x + j * 0.06 + 0.12).toFixed(2)});`).join("\n")}
      tl.to("#${ns}-title .${ns}-ch", { opacity: 0, filter: "blur(6px)", duration: 0.22, stagger: 0.015, ease: "power1.in" }, ${(x + 0.12).toFixed(2)});
      tl.to(q("${ns}-rule"), { scaleX: 0, opacity: 0, duration: 0.25, ease: "power2.in" }, ${(x + 0.12).toFixed(2)});
      window.__timelines = window.__timelines || {};
      window.__timelines["${c.id}"] = tl;
    })();
  </script>
</template>
`;
}

fs.mkdirSync("compositions", { recursive: true });
for (const c of cities) fs.writeFileSync(`compositions/${c.id}.html`, cityHtml(c));

// ---- plan.js for the root composition ----
const outPlan = {
  W, H, NATIONAL, OPEN, pullEnd: plan.opening.pullEnd, duration: plan.duration,
  cities: cities.map((c) => ({ id: c.id, title: c.title, lon: c.lon, lat: c.lat, A: c.A, depart: c.depart, hold: c.hold, start: c.start, dur: c.dur, island: c.anchor === "island", state: c.state, P: c.P, ell: c.ell ?? null })),
  travel: travel.map(({ to, from, t0, t1, rho, a, b }) => ({ to, from, t0, t1, rho, a, b })),
  routes: routes.map(({ from, to, t0, t1, bend, a, b }) => ({ from, to, t0, t1, bend, a, b })),
  overviews: plan.overviews,
  labelOffsets: plan.labelOffsets,
};
fs.writeFileSync("data/plan.js", "/* generated by tools/build.mjs from data/plan.json */\nwindow.__PLAN=" + JSON.stringify(outPlan) + ";\n");

// ---- camera-state manifest (human-readable) ----
const lines = ["# Camera-state manifest (generated)", "", "World units: Web Mercator base px (S = " + S + " px per degree lon at k = 1). k = screen px per world unit.", "", "| Segment | t0 → t1 (s) | from (ux, uy, k) | to (ux, uy, k) | rho |", "|---|---|---|---|---|"];
const fmt = (s) => `${s.ux.toFixed(1)}, ${s.uy.toFixed(1)}, ${(W / s.w).toFixed(3)}`;
lines.push(`| opening pullback | 0.00 → ${plan.opening.pullEnd.toFixed(2)} | ${fmt(OPEN)} | ${fmt(NATIONAL)} | zoom only |`);
for (const t of travel) lines.push(`| ${t.from} → ${t.to} | ${t.t0.toFixed(2)} → ${t.t1.toFixed(2)} | ${fmt(t.a)} | ${fmt(t.b)} | ${t.rho} |`);
lines.push("", "Between segments the camera holds exactly at the last `to` state (connectors stay attached).", "", "| City | block | arrive | photos | hold end | depart | marker P | span° |", "|---|---|---|---|---|---|---|---|");
for (const c of cities) lines.push(`| ${c.title} | ${c.start}–${c.start + c.dur} | ${c.A.toFixed(2)} | ${c.reveal.toFixed(2)} | ${c.hold.toFixed(2)} | ${c.depart.toFixed(2)} | ${c.P.join(", ")} | ${c.span} |`);
fs.writeFileSync("CAMERA.md", lines.join("\n") + "\n");

// ---- index.html from template ----
const hosts = cities.map((c) => `      <div id="sc-${c.id}" class="clip scene-host" data-composition-id="${c.id}" data-composition-src="compositions/${c.id}.html" data-start="${c.start}" data-duration="${c.dur}" data-track-index="2" data-track-kind="graphics" data-width="1920" data-height="1080"></div>`).join("\n");
// ---- sound cues (bundled Pixabay SFX; each cue has a cause on screen) ----
{
  const cues = [];
  const longT = travel.filter((t) => t.t1 - t.t0 >= 2.85);
  let alt = 0;
  for (const t of travel) {
    const fast = t.t0 + 0.45 * (t.t1 - t.t0); // fastest frame of the travel ease
    if (longT.includes(t) && t.rho >= 1.3) cues.push({ file: "assets/sfx/whoosh-cinematic.mp3", t: fast - 2.5, d: 4.4, v: 0.3, why: `travel ${t.from}->${t.to}` });
    else cues.push({ file: alt++ % 2 ? "assets/sfx/whoosh.mp3" : "assets/sfx/whoosh-short.mp3", t: fast - 0.18, d: 0.575, v: 0.32, why: `travel ${t.from}->${t.to}` });
  }
  for (const c of cities) {
    cues.push({ file: "assets/sfx/click-soft.mp3", t: c.A + 0.02, d: 0.37, v: 0.5, why: `${c.id} marker lands` });
    cues.push({ file: "assets/sfx/key-press.mp3", t: c.reveal + 0.05, d: 0.4, v: 0.16, why: `${c.id} connector tick` });
    const hero = c.slots.findIndex((s) => s.role === "hero");
    cues.push({ file: "assets/sfx/pop.mp3", t: c.reveal + Math.max(0, hero) * 0.2 + 0.1, d: 0.72, v: 0.2, why: `${c.id} hero frame unfolds` });
  }
  cues.push({ file: "assets/sfx/chime.mp3", t: 79.85, d: 2.1, v: 0.28, why: "closing resolve on the final map" });
  cues.sort((a, b) => a.t - b.t);
  fs.writeFileSync("data/sfx.json", JSON.stringify(cues, null, 1));
}
let audio = "";
if (fs.existsSync("data/sfx.json")) {
  const sfx = JSON.parse(fs.readFileSync("data/sfx.json", "utf8"));
  audio = sfx.map((s, i) => `      <audio id="sfx${i}" class="clip" src="${s.file}" data-start="${s.t.toFixed(3)}" data-duration="${s.d.toFixed(3)}" data-track-index="${10 + (i % 3)}" data-volume="${s.v}" data-track-kind="audio"></audio>`).join("\n");
}
const tpl = fs.readFileSync("tools/index.template.html", "utf8");
fs.writeFileSync("index.html", tpl.replace("<!--HOSTS-->", hosts).replace("<!--AUDIO-->", audio));

console.log(warnings.length ? "WARNINGS:\n" + warnings.join("\n") : "layout: no collisions");
for (const c of cities) console.log(c.id.padEnd(11), "A", c.A.toFixed(2), "reveal", c.reveal.toFixed(2), "hold", c.hold.toFixed(2), "depart", c.depart.toFixed(2));
for (const t of travel) console.log("travel", String(t.from).padEnd(10), "->", t.to.padEnd(10), t.t0.toFixed(2), t.t1.toFixed(2), (t.t1 - t.t0).toFixed(2) + "s");

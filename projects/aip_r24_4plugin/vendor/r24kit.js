// Shared visual system of R24 ("4 alat biar web dari Claude Code jadi sampai online"), loaded in <head> before every scene (after
// vendor/r24icons.js). Everything is our own design in the AI PRENEUR LIGHT house style. No third-party logos or UI: Claude Code,
// Context7, Supabase, Chrome DevTools MCP, Vercel and Chrome appear as TEXT + generic lucide icons (ISC). The order web app
// ("Toko Kue Rumahan") is a fictional Indonesian UMKM example; its data, links and versions are illustrative (labelled CONTOH).
// Metaphors of the reel (ours): the code alone is only HALF the road; four tools = a library card (Context7: borrow the official
// docs of the exact version you use), a key to the data warehouse (Supabase MCP), a test buyer's eyes + hands in a real Chrome
// (Chrome DevTools MCP), a launch console with a covered production switch (Vercel).
// - K.svg(k, sw)        lucide icon markup (currentColor)
// - K.term(p, o)        "Claude Code" app window (white card + navy terminal body); ids p-tm, p-l<i>, p-ty (typed line), p-bd
// - K.head(p, o)        tool title card: icon tile + eyebrow + tool name + maker line; ids p-hd, p-hdi, p-hde, p-hdt, p-hds
// - K.store(p, w)       the order page header (cake tile + "Toko Kue Rumahan"), K.item(p, i, name, price), K.field(p, label, val)
// - K.phone(p, o)       phone frame with a screen box (id p-scr) to fill
// - K.cursor(p, label)  pointer + label tag (id p-cur, label p-curl)
// - K.boot(ID)          timeline boilerplate: seek-safe scale shorthand; EVERY initial state pinned at 0 in a NESTED timeline P0 that is
//                       the first child of the scene timeline at 0 (I); fromTo without immediate render (ft); word lookup (L, throws if a
//                       word is missing); typeD (typed text with caret); shake; pop; done() = end marker + backward-seek patch +
//                       tl.render(0, true, true) + registration.
(function () {
  const ICO = window.R24_ICO;
  const svg = (k, sw, cls) => { if (!ICO[k]) throw new Error("icon missing " + k); return `<svg class="${cls || ""}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[k]}</svg>`; };

  const CSS = `
  .k-grad { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .k-card { background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 40px 70px -40px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); }
  .k-a { position: absolute; }
  /* ---------------- Claude Code app window */
  .k-tm { position: absolute; border-radius: 28px; font-family: Poppins, sans-serif; transform-origin: 50% 50%; overflow: hidden; }
  .k-tm > * { position: absolute; }
  .k-tm .bar { left: 0; top: 0; right: 0; height: 64px; }
  .k-tm .dots { left: 24px; top: 26px; width: 60px; height: 14px; }
  .k-tm .dots i { position: absolute; top: 0; width: 14px; height: 14px; border-radius: 50%; background: #d7deeb; }
  .k-tm .ti { left: 96px; top: 13px; height: 38px; display: flex; align-items: center; gap: 10px; font: 700 24px/38px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .k-tm .ti svg { width: 28px; height: 28px; display: block; color: #294b77; flex: none; }
  .k-tm .tg { right: 22px; top: 16px; height: 32px; padding: 0 14px; border-radius: 16px; background: #eef2f9; color: #5d6f8f; font: 700 14px/32px Poppins, sans-serif; letter-spacing: .12em; white-space: nowrap; }
  .k-tm .bd { left: 14px; right: 14px; top: 64px; bottom: 14px; border-radius: 18px; background: linear-gradient(160deg, #111a44, #0a0d2c 70%); box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.06); overflow: hidden; }
  .k-tm .ln { position: absolute; left: 26px; font: 400 23px/34px Poppins, sans-serif; color: #c9d6f2; white-space: nowrap; }
  .k-tm .ln b { font-weight: 700; color: #8fd8ff; }
  .k-tm .ln em { font-style: normal; color: #7f8db0; }
  .k-tm .ln i { font-style: normal; color: #ffd08a; }
  .k-tm .ty { position: absolute; left: 26px; font: 400 23px/34px Poppins, sans-serif; color: #ffffff; white-space: nowrap; }
  .k-tm .ty b { font-weight: 700; color: #8fd8ff; }
  .k-caret { display: inline-block; width: 12px; height: 26px; margin-left: 4px; vertical-align: -4px; border-radius: 2px; background: #8fd8ff; }
  /* ---------------- tool title card */
  .k-hd { position: absolute; border-radius: 30px; font-family: Poppins, sans-serif; transform-origin: 50% 50%; }
  .k-hd > * { position: absolute; }
  .k-hd .ic { left: 22px; top: 50%; width: 96px; height: 96px; margin-top: -48px; border-radius: 28px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #8fd8ff;
    box-shadow: 0 16px 26px -14px rgba(10,13,44,.8), inset 0 2px 0 rgba(255,255,255,.14); }
  .k-hd .ic svg { position: absolute; left: 24px; top: 24px; width: 48px; height: 48px; display: block; }
  .k-hd .nb { left: 140px; top: 22px; height: 30px; padding: 0 12px 0 12px; border-radius: 15px; background: #eaf0fe; color: #2a55c4; font: 700 14px/30px Poppins, sans-serif; letter-spacing: .14em; white-space: nowrap; }
  .k-hd .tt { left: 138px; top: 52px; font: 700 42px/56px Poppins, sans-serif; white-space: nowrap; padding-right: 6px; }
  .k-hd .ts { left: 140px; top: 106px; font: 400 19px/26px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .k-hd .ts b { font-weight: 700; color: #294b77; }
  /* ---------------- phone */
  .k-ph { position: absolute; border-radius: 56px; background: linear-gradient(160deg, #2b3f6b, #0a0d2c 60%); box-shadow: 0 50px 80px -40px rgba(10,13,44,.75), inset 0 2px 0 rgba(255,255,255,.18);
    transform-origin: 50% 50%; }
  .k-ph > .scr { position: absolute; left: 14px; top: 14px; right: 14px; bottom: 14px; border-radius: 44px; background: #ffffff; overflow: hidden; }
  .k-ph > .nt { position: absolute; left: 50%; top: 26px; width: 104px; height: 28px; margin-left: -52px; border-radius: 14px; background: #0a0d2c; }
  /* ---------------- the order web app (fictional UMKM example) */
  .k-pg { position: absolute; font-family: Poppins, sans-serif; color: #0a0d2c; }
  .k-pg > * { position: absolute; }
  .k-st { position: absolute; height: 64px; }
  .k-st > * { position: absolute; }
  .k-st .lg { left: 0; top: 0; width: 64px; height: 64px; border-radius: 20px; background: linear-gradient(150deg, #f7a25c, #e2712a); color: #fff; box-shadow: 0 10px 18px -10px rgba(226,113,42,.9); }
  .k-st .lg svg { position: absolute; left: 15px; top: 15px; width: 34px; height: 34px; display: block; }
  .k-st .nm { left: 80px; top: 3px; font: 700 21px/30px Poppins, sans-serif; white-space: nowrap; color: #0a0d2c; }
  .k-st .sb { left: 80px; top: 34px; font: 400 15px/22px Poppins, sans-serif; white-space: nowrap; color: #6b7a96; }
  .k-it { position: absolute; height: 70px; border-radius: 20px; background: #fbf7f2; box-shadow: inset 0 0 0 1.5px #f1e6d8; }
  .k-it > * { position: absolute; }
  .k-it .ii { left: 12px; top: 11px; width: 48px; height: 48px; border-radius: 15px; background: #ffe9d6; color: #d0651f; }
  .k-it .ii svg { position: absolute; left: 11px; top: 11px; width: 26px; height: 26px; display: block; }
  .k-it .in { left: 74px; top: 9px; font: 700 18px/26px Poppins, sans-serif; white-space: nowrap; color: #0a0d2c; }
  .k-it .ip { left: 74px; top: 35px; font: 400 15px/22px Poppins, sans-serif; white-space: nowrap; color: #8a6a4c; }
  .k-it .ia { right: 12px; top: 17px; width: 36px; height: 36px; border-radius: 12px; background: #e2712a; color: #fff; }
  .k-it .ia svg { position: absolute; left: 8px; top: 8px; width: 20px; height: 20px; display: block; }
  .k-fl { position: absolute; height: 58px; border-radius: 16px; background: #f4f6fb; box-shadow: inset 0 0 0 1.5px #e0e6f1; }
  .k-fl > * { position: absolute; }
  .k-fl .fl { left: 16px; top: 6px; font: 700 12px/16px Poppins, sans-serif; letter-spacing: .1em; color: #8592ad; white-space: nowrap; }
  .k-fl .fv { left: 16px; top: 23px; font: 400 18px/28px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .k-bt { position: absolute; height: 60px; border-radius: 18px; background: linear-gradient(150deg, #f08a4b, #d9621f); color: #fff; font: 700 20px/60px Poppins, sans-serif;
    text-align: center; white-space: nowrap; box-shadow: 0 14px 22px -14px rgba(217,98,31,.95); transform-origin: 50% 50%; }
  .k-wf { position: absolute; border-radius: 18px; border: 3px dashed #c3cfe3; background: rgba(240,244,251,.6); }
  /* ---------------- cursor */
  .k-cur { position: absolute; left: 0; top: 0; width: 0; height: 0; }
  .k-cur .pt { position: absolute; left: -6px; top: -4px; width: 46px; height: 46px; color: #0a0d2c; filter: drop-shadow(0 6px 8px rgba(10,13,44,.35)); }
  .k-cur .pt svg { width: 46px; height: 46px; display: block; fill: #ffffff; }
  .k-cur .lb { position: absolute; left: 34px; top: 34px; height: 38px; padding: 0 14px 0 14px; border-radius: 19px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #fff;
    font: 700 16px/38px Poppins, sans-serif; white-space: nowrap; box-shadow: 0 10px 18px -10px rgba(10,13,44,.8); }
  .k-cur .rp { position: absolute; left: -26px; top: -26px; width: 52px; height: 52px; border-radius: 50%; border: 4px solid #3a6fe0; }
  /* ---------------- chips, stamps, footnotes */
  .k-chip { position: absolute; height: 54px; padding: 0 22px 0 56px; border-radius: 27px; background: #ffffff; color: #0a0d2c; white-space: nowrap; font: 700 22px/54px Poppins, sans-serif;
    box-shadow: 0 16px 26px -16px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); transform-origin: 50% 50%; }
  .k-chip svg { position: absolute; left: 18px; top: 14px; width: 26px; height: 26px; display: block; color: #294b77; }
  .k-chip.ok { background: #e8f6ed; color: #1f7a3a; box-shadow: inset 0 0 0 1.5px rgba(31,122,58,.22); } .k-chip.ok svg { color: #1f7a3a; }
  .k-chip.info { background: #eaf0fe; color: #2a55c4; box-shadow: inset 0 0 0 1.5px rgba(42,85,196,.22); } .k-chip.info svg { color: #2a55c4; }
  .k-chip.warn { background: #fff3dc; color: #8a4d08; box-shadow: inset 0 0 0 1.5px rgba(148,84,10,.25); } .k-chip.warn svg { color: #8a4d08; }
  .k-chip.bad { background: #fdeaea; color: #b4322f; box-shadow: inset 0 0 0 1.5px rgba(180,50,47,.22); } .k-chip.bad svg { color: #b4322f; }
  .k-chip.navy { background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff; box-shadow: 0 16px 26px -14px rgba(10,13,44,.8); } .k-chip.navy svg { color: #8fd8ff; }
  .k-chip.sm { height: 44px; padding: 0 18px 0 46px; border-radius: 22px; font-size: 18px; line-height: 44px; } .k-chip.sm svg { left: 15px; top: 11px; width: 22px; height: 22px; }
  .k-stamp { position: absolute; height: 72px; padding: 0 22px; border-radius: 14px; border: 5px solid #1f7a3a; color: #1f7a3a; background: rgba(232,246,237,.92);
    font: 700 34px/62px Poppins, sans-serif; letter-spacing: .1em; text-indent: .1em; white-space: nowrap; transform-origin: 50% 50%; }
  .k-stamp.bad { border-color: #b4322f; color: #b4322f; background: rgba(253,234,234,.94); }
  .k-stamp.warn { border-color: #94540a; color: #94540a; background: rgba(255,243,220,.94); }
  .k-stamp.navy { border-color: #294b77; color: #294b77; background: rgba(234,240,254,.94); }
  .k-fn { position: absolute; height: 40px; padding: 0 16px 0 44px; border-radius: 20px; background: rgba(255,255,255,.92); box-shadow: inset 0 0 0 1.5px #d9e2f0; color: #5d6f8f;
    font: 400 17px/40px Poppins, sans-serif; white-space: nowrap; }
  .k-fn b { font-weight: 700; color: #294b77; }
  .k-fn svg { position: absolute; left: 14px; top: 10px; width: 20px; height: 20px; display: block; color: #294b77; }
  .k-ok { position: absolute; width: 40px; height: 40px; border-radius: 50%; background: #2da44e; color: #ffffff; box-shadow: 0 0 0 4px #ffffff, 0 10px 18px -8px rgba(31,122,58,.8); }
  .k-ok svg { position: absolute; left: 9px; top: 9px; width: 22px; height: 22px; display: block; }
  .k-no { position: absolute; width: 40px; height: 40px; border-radius: 50%; background: #d9534f; color: #ffffff; box-shadow: 0 0 0 4px #ffffff, 0 10px 18px -8px rgba(180,50,47,.8); }
  .k-no svg { position: absolute; left: 9px; top: 9px; width: 22px; height: 22px; display: block; }
  .k-glow { position: absolute; border-radius: 50%; background: radial-gradient(closest-side, rgba(255,255,255,.95), rgba(255,255,255,0)); }
  .k-tag { position: absolute; height: 30px; padding: 0 12px; border-radius: 15px; background: #ffffff; box-shadow: inset 0 0 0 1.5px #d9e2f0; font: 700 12px/30px Poppins, sans-serif;
    letter-spacing: .14em; color: #5d6f8f; white-space: nowrap; }
  `;
  if (!document.getElementById("k-css")) { const st = document.createElement("style"); st.id = "k-css"; st.textContent = CSS; (document.head || document.documentElement).appendChild(st); }

  // Claude Code app window. o: {x, y, w, h, tag, lines: [html...], ty: true, fs, lh, t0}
  const term = (p, o) => {
    const fs = o.fs || 23, lh = o.lh || 38, t0 = o.t0 == null ? 18 : o.t0, f = `font-size:${fs}px;line-height:${Math.round(fs * 1.48)}px`;
    const lines = (o.lines || []).map((l, i) => `<div class="ln" id="${p}-l${i}" style="top:${t0 + i * lh}px;${f}">${l}</div>`).join("");
    const ty = o.ty ? `<div class="ty" id="${p}-ty" style="top:${t0 + (o.lines || []).length * lh}px;${f}"></div>` : "";
    return `<div class="k-tm k-card" id="${p}-tm" style="left:${o.x}px;top:${o.y}px;width:${o.w}px;height:${o.h}px">` +
      `<div class="bar"></div><div class="dots"><i style="left:0"></i><i style="left:22px"></i><i style="left:44px"></i></div>` +
      `<div class="ti">${svg("square-terminal", 2.2)}Claude Code</div>${o.tag ? `<div class="tg" id="${p}-tg">${o.tag}</div>` : ""}` +
      `<div class="bd" id="${p}-bd">${lines}${ty}</div></div>`;
  };
  // tool title card. o: {x, y, w, h, icon, eb (eyebrow), t (tool name), s (maker line, html)}
  const head = (p, o) => `<div class="k-hd k-card" id="${p}-hd" style="left:${o.x}px;top:${o.y}px;width:${o.w}px;height:${o.h || 150}px">` +
    `<div class="ic" id="${p}-hdi">${svg(o.icon, 2)}</div><div class="nb" id="${p}-hde">${o.eb}</div><div class="tt k-grad" id="${p}-hdt">${o.t}</div><div class="ts" id="${p}-hds">${o.s}</div></div>`;
  // order page pieces
  const store = (p, x, y) => `<div class="k-st" id="${p}-st" style="left:${x}px;top:${y}px"><div class="lg">${svg("cake", 2)}</div><div class="nm">Toko Kue Rumahan</div><div class="sb">Pre-order · ambil di rumah</div></div>`;
  const item = (p, i, x, y, w, name, price, icon) => `<div class="k-it" id="${p}-it${i}" style="left:${x}px;top:${y}px;width:${w}px"><div class="ii">${svg(icon || "cake-slice", 2)}</div>` +
    `<div class="in">${name}</div><div class="ip">${price}</div><div class="ia">${svg("check", 2.6)}</div></div>`;
  const field = (p, i, x, y, w, label, val) => `<div class="k-fl" id="${p}-fl${i}" style="left:${x}px;top:${y}px;width:${w}px"><div class="fl">${label}</div><div class="fv" id="${p}-fv${i}">${val}</div></div>`;
  const button = (p, x, y, w, txt) => `<div class="k-bt" id="${p}-bt" style="left:${x}px;top:${y}px;width:${w}px">${txt}</div>`;
  // phone frame (screen box p-scr to fill). o: {x, y, w, h}
  const phone = (p, o) => `<div class="k-ph" id="${p}-ph" style="left:${o.x}px;top:${o.y}px;width:${o.w}px;height:${o.h}px"><div class="scr" id="${p}-scr">${o.html || ""}</div><div class="nt"></div></div>`;
  // pointer + label
  const cursor = (p, label) => `<div class="k-cur" id="${p}-cur"><div class="rp" id="${p}-rp"></div><div class="pt"><svg viewBox="0 0 24 24" fill="#fff" stroke="#0a0d2c" stroke-width="1.7" stroke-linejoin="round">${ICO["mouse-pointer-2"]}</svg></div>` +
    (label ? `<div class="lb" id="${p}-curl">${label}</div>` : "") + `</div>`;

  // the order web on a phone (s01 → s02 → s03 hand-overs use this exact markup). o: {x, y}; 364×560, screen 336×532.
  // ids: p-ph, p-scr, p-st, p-it0/1, p-wf0..2 (wireframe placeholders of the unbuilt half), p-fl0/1 + p-bt (the built half)
  const PH = { w: 364, h: 560, half: 14 + 281 };   // half: y of the "setengah jalan" line inside the phone
  const orderPhone = (p, o) => {
    const wf = (i, y, h) => `<div class="k-wf" id="${p}-wf${i}" style="left:18px;top:${y}px;width:300px;height:${h}px"><i style="position:absolute;left:18px;top:${h / 2 - 6}px;width:${[120, 150, 160][i]}px;height:12px;border-radius:6px;background:#d5deec"></i></div>`;
    const html = store(p, 22, 52) + item(p, 0, 18, 128, 300, "Bolu pandan", "Rp 85.000", "cake-slice") + item(p, 1, 18, 206, 300, "Brownies", "Rp 70.000", "cake") +
      wf(0, 286, 58) + wf(1, 356, 58) + wf(2, 428, 60) +
      field(p, 0, 18, 286, 300, "NAMA", "Tulis namamu") + field(p, 1, 18, 356, 300, "TANGGAL AMBIL", "Pilih tanggal") + button(p, 18, 428, 300, "Pesan sekarang");
    return phone(p, { x: o.x, y: o.y, w: PH.w, h: PH.h, html });
  };
  // the toolbox (s02 → s03 hand-over). o: {x, y}; 556×604. ids: p-tb, p-tbe, p-tbt, p-tile0..3, p-tic<i>
  const TOOLS = [
    { icon: "book-open-check", lab: "Kartu<br>perpustakaan", nm: "Context7" },
    { icon: "key-round", lab: "Kunci<br>gudang data", nm: "Supabase MCP" },
    { icon: "mouse-pointer-2", lab: "Pembeli<br>uji coba", nm: "Chrome DevTools MCP" },
    { icon: "rocket", lab: "Tombol<br>luncur", nm: "Vercel" },
  ];
  const TB = { w: 556, h: 604, tile: (i) => ({ x: 18 + (i % 2) * 268, y: 128 + Math.floor(i / 2) * 238, w: 252, h: 214 }) };
  const toolbox = (p, o) => {
    let h = `<div class="k-a k-card" id="${p}-tb" style="left:${o.x}px;top:${o.y}px;width:${TB.w}px;height:${TB.h}px;border-radius:34px"></div>`;
    h += `<div class="k-a" id="${p}-tbe" style="left:${o.x + 30}px;top:${o.y + 28}px;font:700 15px/22px Poppins,sans-serif;letter-spacing:.16em;color:#5d6f8f;white-space:nowrap">PASANG DI CLAUDE CODE</div>`;
    h += `<div class="k-a k-grad" id="${p}-tbt" style="left:${o.x + 28}px;top:${o.y + 50}px;font:700 46px/60px Poppins,sans-serif;white-space:nowrap;padding-right:6px">4 alat</div>`;
    TOOLS.forEach((t, i) => {
      const r = TB.tile(i);
      h += `<div class="k-a" id="${p}-tile${i}" style="left:${o.x + r.x}px;top:${o.y + r.y}px;width:${r.w}px;height:${r.h}px;border-radius:26px;background:#f4f7fc;box-shadow:inset 0 0 0 1.5px #e1e8f3;transform-origin:50% 50%">` +
        `<div class="k-a" id="${p}-tic${i}" style="left:20px;top:20px;width:66px;height:66px;border-radius:20px;background:linear-gradient(135deg,#0a0d2c,#294b77);color:#8fd8ff;box-shadow:0 12px 20px -12px rgba(10,13,44,.8)"><div style="position:absolute;left:16px;top:16px;width:34px;height:34px">${svg(t.icon, 2)}</div></div>` +
        `<div class="k-a" style="right:18px;top:20px;width:36px;height:36px;border-radius:50%;background:#ffffff;box-shadow:inset 0 0 0 2px #d5deec;font:700 18px/36px Poppins,sans-serif;text-align:center;color:#294b77">${i + 1}</div>` +
        `<div class="k-a" style="left:20px;top:100px;font:700 21px/27px Poppins,sans-serif;color:#0a0d2c;white-space:nowrap">${t.lab}</div>` +
        `<div class="k-a" style="left:20px;top:164px;height:30px;padding:0 12px;border-radius:15px;background:#ffffff;box-shadow:inset 0 0 0 1.5px #d9e2f0;font:700 15px/30px Poppins,sans-serif;color:#294b77;white-space:nowrap">${t.nm}</div></div>`;
    });
    return h;
  };

  // ---------------------------------------------------------------- timeline boilerplate (initial states nested at 0)
  const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
  const boot = (ID) => {
    const ST = window.SCN[ID][0], D = window.SCN[ID][1], VW = window.VO_WORDS;
    const tl = gsap.timeline({ paused: true });
    { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); const cq = (q) => (typeof q === "number" ? Math.max(0, q) : q);
      tl.set = (a, v, q) => s0(a, _sc(v), cq(q)); tl.fromTo = (a, x, y, q) => f0(a, _sc(x), _sc(y), cq(q)); tl.to = (a, v, q) => t0(a, _sc(v), cq(q)); }
    const P0 = gsap.timeline(); tl.add(P0, 0);                 // every initial state lives here: nested, first child at 0
    const I = (el, v) => { gsap.set(el, _sc(v)); P0.set(el, _sc(v), 0); };
    const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), t);
    const L = (txt, after) => { const w = VW.find((x) => x[0] === txt && x[1] >= ST + (after || 0) - 0.05); if (!w) throw new Error(ID + ": word not found " + txt); return w[1] - ST; };
    const $ = (id) => { const e = document.getElementById(id); if (!e) throw new Error(ID + ": element not found " + id); if (document.querySelectorAll("#" + id).length > 1) throw new Error(ID + ": duplicate id " + id); return e; };
    const shake = (el, t, amp = 6) => { [[amp, -amp * 0.6], [-amp * 0.8, amp * 0.4], [amp * 0.4, -amp * 0.2], [0, 0]].forEach(([x, y], k) => tl.set(el, { x, y }, t + k * 0.034)); };
    // pop in (hidden at 0)
    const pop = (el, t, from, dur, ease) => { const a = Object.assign({ opacity: 0, scale: 0.6, y: 20 }, from || {}); const b = {}; for (const k in a) b[k] = k === "opacity" ? 1 : (k === "scale" ? 1 : 0);
      I(el, a); ft(el, a, Object.assign(b, { duration: dur || 0.3, ease: ease || "back.out(1.9)" }), t); };
    // typed text that pushes an inline caret: letters are display:none until their time
    const typeD = (el, text, t0, t1, caret) => {
      el.innerHTML = text.split("").map((c) => `<span>${c === " " ? "&nbsp;" : c}</span>`).join("") + (caret ? `<i class="k-caret"></i>` : "");
      const sp = Array.from(el.querySelectorAll("span")), n = sp.length;
      sp.forEach((s, i) => { I(s, { display: "none" }); tl.set(s, { display: "inline" }, t0 + (t1 - t0) * (i / Math.max(1, n - 1))); });
      return sp;
    };
    const done = () => {
      tl.set({}, {}, D - 0.01);
      (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
      tl.render(0, true, true);
      window.__timelines = window.__timelines || {};
      window.__timelines[ID] = tl;
    };
    return { ST, D, L, tl, ft, I, $, shake, pop, typeD, done };
  };
  // shared exit: everything drops + fades
  const out = (S, els, tOut) => els.forEach((e, k) => S.ft(e, { opacity: 1, y: 0 }, { opacity: 0, y: 46, duration: 0.24, ease: "power2.in" }, tOut + k * 0.025));

  window.K = { svg, term, head, store, item, field, button, phone, cursor, orderPhone, PH, toolbox, TOOLS, TB, boot, out };
})();

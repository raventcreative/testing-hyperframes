/* Claude 42-stack carousel — shared kit: background, chrome (AI PRENEUR logo + pager), 3D Claude spark,
   tool icons, pixel mascots. Everything is static markup + pure functions of time (deterministic). */
(function () {
  const W = 1080, H = 1350;
  const clamp = (x, a, b) => Math.min(b, Math.max(a, x));
  const seg = (t, a, b) => clamp((t - a) / (b - a), 0, 1);
  const eo = (x) => 1 - Math.pow(1 - clamp(x, 0, 1), 3);
  const eo4 = (x) => 1 - Math.pow(1 - clamp(x, 0, 1), 4);
  const io = (x) => { x = clamp(x, 0, 1); return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
  const back = (x, s) => { x = clamp(x, 0, 1); s = s || 1.6; return 1 + (s + 1) * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2); };

  // ---------------------------------------------------------------- tool glyphs (white line icons, 24x24)
  const G = {
    bolt: '<path d="M13 2 4 14h7l-1 8 9-12h-7l1-8z" fill="#fff"/>',
    layers: '<path d="M12 3 2 8l10 5 10-5-10-5z M2 13l10 5 10-5 M2 17.5l10 5 10-5" fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round"/>',
    graph: '<circle cx="6" cy="12" r="2.6" fill="none" stroke="#fff" stroke-width="2"/><circle cx="18" cy="6" r="2.6" fill="none" stroke="#fff" stroke-width="2"/><circle cx="18" cy="18" r="2.6" fill="none" stroke="#fff" stroke-width="2"/><path d="M8.3 10.8l7.4-3.6M8.3 13.2l7.4 3.6" stroke="#fff" stroke-width="2"/>',
    masks: '<path d="M3 5c3 1.5 6 1.5 9 0v6c0 3-2 5-4.5 5S3 14 3 11V5z" fill="#e5484d"/><path d="M12 8c3 1.5 6 1.5 9 0v6c0 3-2 5-4.5 5S12 17 12 14V8z" fill="#fff"/><path d="M14.5 12.2h1.5M18 12.2h1.5M15 15.5c.8.8 2.6.8 3.6 0" stroke="#2ead33" stroke-width="1.4" fill="none" stroke-linecap="round"/>',
    terminal: '<path d="M5 8l4 4-4 4M11 17h8" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
    gauge: '<path d="M4 16a8 8 0 1 1 16 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/><path d="M12 16l4-5" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>',
    palette: '<path d="M12 3a9 9 0 0 0 0 18c1.4 0 2-1 1.6-2.2-.5-1.4.4-2.8 1.9-2.8H18a3 3 0 0 0 3-3c0-5.5-4-10-9-10z" fill="none" stroke="#fff" stroke-width="2"/><circle cx="7.5" cy="11" r="1.4" fill="#fff"/><circle cx="10" cy="7" r="1.4" fill="#fff"/><circle cx="15" cy="7.5" r="1.4" fill="#fff"/>',
    pen: '<path d="M4 20l3-8 9-9 5 5-9 9-8 3z M7 12l5 5 M15 4l5 5" fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round"/><circle cx="10.5" cy="13.5" r="1.4" fill="#fff"/>',
    wand: '<path d="M4 20 15 9" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/><path d="M17 2v4M15 4h4M20 9v3M18.5 10.5h3M10 3v2.6M8.7 4.3h2.6" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/>',
    cursor: '<path d="M5 3l14 7-6 2-2 6L5 3z" fill="none" stroke="#fff" stroke-width="2.2" stroke-linejoin="round"/>',
    hyper: '<path d="M3 12l7-6v12z" fill="#28d07d"/><path d="M21 12l-7 6V6z" fill="#3fa9f5"/>',
    play: '<path d="M7 4.5v15l12-7.5z" fill="#fff"/>',
    squiggle: '<path d="M4 16c3-8 6 4 9-4s5 6 7-1" fill="none" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
    flame: '<path d="M12 3c1 3.5 5 5.5 5 10a5 5 0 0 1-10 0c0-2 1-3.5 2-4.5.3 1.5 1 2.3 2 2.5-.5-3 0-5.5 1-8z" fill="#fff"/>',
    apify: '<path d="M4 19 9 5l3 7z" fill="#fff"/><path d="M12 12 15 5l5 14z" fill="#ff7a1a"/><path d="M9 19l3-7 3 7z" fill="#1d4ed8"/>',
    calendar: '<rect x="3.5" y="5" width="17" height="15" rx="3" fill="none" stroke="#fff" stroke-width="2"/><path d="M3.5 10h17M8 3v4M16 3v4" stroke="#fff" stroke-width="2" stroke-linecap="round"/>',
    person: '<circle cx="12" cy="8.5" r="4" fill="none" stroke="#fff" stroke-width="2"/><path d="M4.5 20c1.2-4 4-5.5 7.5-5.5s6.3 1.5 7.5 5.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>',
    infinity: '<path d="M7 8a4 4 0 1 0 0 8c3 0 7-8 10-8a4 4 0 1 1 0 8c-3 0-7-8-10-8z" fill="none" stroke="#111" stroke-width="2.6"/>',
    slack: '<rect x="10" y="2.5" width="4" height="9" rx="2" fill="#36c5f0"/><rect x="12.5" y="10" width="9" height="4" rx="2" fill="#2eb67d"/><rect x="10" y="12.5" width="4" height="9" rx="2" fill="#ecb22e"/><rect x="2.5" y="10" width="9" height="4" rx="2" fill="#e01e5a"/>',
    compress: '<path d="M14 10l6-6M14 10V5.5M14 10h4.5M10 14l-6 6M10 14v4.5M10 14H5.5" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>',
    search: '<circle cx="10.5" cy="10.5" r="6" fill="none" stroke="#fff" stroke-width="2.4"/><path d="M15 15l5 5" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>',
  };
  const lum = (hex) => { const n = parseInt(hex.slice(1), 16); const r = n >> 16, g = (n >> 8) & 255, b = n & 255; return (0.299 * r + 0.587 * g + 0.114 * b) / 255; };
  // icon tile: brand glyph on brand colour (dark brands → white tile, black glyph)
  function iconHTML(spec, size) {
    size = size || 76; const r = Math.round(size * 0.28);
    let bg, inner;
    if (spec.startsWith("b:")) {
      const k = spec.slice(2), b = window.BRAND_ICONS[k];
      const dark = lum(b.hex) < 0.2;
      bg = dark ? "#ffffff" : b.hex;
      inner = `<path d="${b.d}" fill="${dark ? "#0b0d14" : "#fff"}"/>`;
      if (k === "googlechrome" || k === "gmail" || k === "googlecalendar" || k === "googlegemini" || k === "figma") { bg = "#ffffff"; inner = `<path d="${b.d}" fill="${b.hex}"/>`; }
    } else {
      const [, k, col] = spec.split(":"); bg = col; inner = G[k];
    }
    const light = lum(bg) > 0.75;
    return `<div class="k-icon" style="width:${size}px;height:${size}px;border-radius:${r}px;background:${bg};${light ? "box-shadow:inset 0 0 0 1px rgba(10,13,44,0.08),0 10px 24px rgba(0,0,0,0.35)" : "box-shadow:inset 0 1px 0 rgba(255,255,255,0.25),0 10px 24px rgba(0,0,0,0.35)"}">
      <svg viewBox="0 0 24 24" style="width:${Math.round(size * 0.5)}px;height:${Math.round(size * 0.5)}px">${inner}</svg></div>`;
  }

  // ---------------------------------------------------------------- background: #0a0d2c → #294b77 + grid + soft spark glow
  function bgHTML(P, accent) {
    return `
<div id="${P}-bg" class="k-full" style="background:#0a0d2c url(assets/background/bg_user.png) center/1080px 1350px no-repeat">
  <div id="${P}-grid" class="k-full" style="opacity:0.55;background-image:linear-gradient(rgba(255,255,255,0.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.045) 1px,transparent 1px);background-size:54px 54px;background-position:-1px -1px"></div>
  <div class="k-full" style="background:radial-gradient(60% 45% at 85% 8%,${accent || "#d97757"}2e,transparent 70%),radial-gradient(70% 50% at 10% 100%,rgba(41,75,119,0.0),transparent 70%)"></div>
  <div id="${P}-bgspark" style="position:absolute;left:760px;top:-150px;width:520px;height:520px;opacity:0.10">${sparkSVG("#d97757")}</div>
  <div class="k-full" style="box-shadow:inset 0 0 160px rgba(4,6,24,0.35)"></div>
</div>`;
  }
  function sparkSVG(fill) {
    return `<svg viewBox="0 0 24 24" style="width:100%;height:100%;display:block"><path d="${window.BRAND_ICONS.claude.d}" fill="${fill}"/></svg>`;
  }
  // 3D Claude spark: stacked layers (thickness) inside a preserve-3d holder; rotate the holder with spark3d(ref,t)
  function spark3dHTML(P, size) {
    let layers = "";
    const N = 12;
    for (let i = 0; i < N; i++) {
      const k = i / (N - 1), col = i === N - 1 ? "#f0916b" : `rgb(${Math.round(150 + 60 * k)},${Math.round(68 + 28 * k)},${Math.round(40 + 18 * k)})`;
      layers += `<div style="position:absolute;inset:0;transform:translateZ(${(i - N / 2) * (size / 110)}px)">${sparkSVG(col)}</div>`;
    }
    return `<div id="${P}" style="position:absolute;width:${size}px;height:${size}px;perspective:${size * 5}px">
      <div id="${P}-glow" style="position:absolute;inset:-35%;border-radius:50%;background:radial-gradient(closest-side,rgba(217,119,87,0.45),rgba(217,119,87,0))"></div>
      <div id="${P}-rot" style="position:absolute;inset:0;transform-style:preserve-3d">${layers}</div></div>`;
  }
  function spark3d(P, t, o) {
    o = o || {};
    const rot = document.getElementById(P + "-rot"), glow = document.getElementById(P + "-glow");
    const ry = (o.ry0 || 0) + t * (o.spin === undefined ? 70 : o.spin), rx = 14 * Math.sin(t * 1.3), rz = t * (o.rz || 0);
    rot.style.transform = `rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) rotateZ(${rz.toFixed(2)}deg)`;
    glow.style.transform = `scale(${(1 + 0.08 * Math.sin(t * 3.1)).toFixed(3)})`;
  }

  // ---------------------------------------------------------------- chrome: AI PRENEUR logo (sheen) + slide pager
  function chromeHTML(P, slide, total) {
    let dots = "";
    for (let i = 0; i < total; i++) dots += `<span style="display:inline-block;height:10px;border-radius:5px;margin:0 5px;width:${i === slide ? 42 : 10}px;background:${i === slide ? "#ffffff" : "rgba(255,255,255,0.28)"}"></span>`;
    return `
<div id="${P}-chrome" class="k-full" style="pointer-events:none">
  <div id="${P}-logo" style="position:absolute;left:64px;top:62px;width:250px;height:24px">
    <img src="assets/branding/logo_aipreneur_white_user_crop.png" alt="AI PRENEUR" style="position:absolute;inset:0;width:250px;height:24px;filter:drop-shadow(0 3px 10px rgba(2,6,24,0.6))"/>
    <div id="${P}-sheen" style="position:absolute;inset:0;-webkit-mask:url(assets/branding/logo_aipreneur_white_user_crop.png) center/100% 100% no-repeat;mask:url(assets/branding/logo_aipreneur_white_user_crop.png) center/100% 100% no-repeat"></div>
  </div>
  <div style="position:absolute;left:0;right:0;top:1298px;text-align:center">${dots}</div>
</div>`;
  }
  function chrome(P, t) {
    const u = ((t + 1.2) % 4.5) / 1.4, p = Math.min(1.3, u) * 150 - 30;
    const sh = document.getElementById(P + "-sheen");
    if (sh) sh.style.background = `linear-gradient(105deg,rgba(0,201,255,0) ${(p - 18).toFixed(1)}%,rgba(140,225,255,0.95) ${p.toFixed(1)}%,rgba(0,201,255,0) ${(p + 18).toFixed(1)}%)`;
    const lg = document.getElementById(P + "-logo");
    if (lg) lg.style.transform = `translateY(${(Math.sin(t * 1.1) * 3).toFixed(2)}px)`;
  }
  function bg(P, t) {
    const sp = document.getElementById(P + "-bgspark"); if (sp) sp.style.transform = `rotate(${(t * 9).toFixed(2)}deg)`;
    const gr = document.getElementById(P + "-grid"); if (gr) gr.style.transform = `translate(${(-t * 6 % 54).toFixed(2)}px,${(-t * 4 % 54).toFixed(2)}px)`;
  }

  // ---------------------------------------------------------------- pixel mascot: stepped hop (keeps the pixel-art feel)
  function mascotHTML(id, file, w, extra) {
    return `<img id="${id}" class="k-pix" src="assets/mascots/${file}" alt="" style="position:absolute;width:${w}px;${extra || ""}"/>`;
  }
  // returns a translate/scale string for a mascot hop: period per, phase ph; 12 fps stepping
  function hop(t, per, ph, amp) {
    const ts = Math.floor(t * 12) / 12, u = ((ts + ph) % per) / per;
    const h = u < 0.35 ? Math.sin((u / 0.35) * Math.PI) : 0;
    const squash = u < 0.06 ? 0.94 : u > 0.33 && u < 0.4 ? 0.95 : 1;
    return { y: -(amp || 18) * h, sy: squash, sx: 2 - squash };
  }

  window.K = { W, H, clamp, seg, eo, eo4, io, back, iconHTML, bgHTML, bg, sparkSVG, spark3dHTML, spark3d, chromeHTML, chrome, mascotHTML, hop };
})();

/* AIpreneur 17-effects carousel — shared presenter (illustrated, front-facing bust) + studio backdrop.
   Everything is deterministic: call HFP.animate(R, t) from a timeline onUpdate with the composition's local time.

   Geometry (frame 1080x1350):
     figure box  left 220, top 380, 640x1000 (viewBox 0 0 640 1000), bottom runs off-frame
     face centre ≈ (540, 595) · eyes y ≈ 588 · chin y ≈ 732 · shoulders y ≈ 830 · chest centre ≈ (540, 980)
     free space: left of head x 60–360, right of head x 720–1020, above head y 140–400, chest y 860–1100
   Layers you build around it (z order): backdrop · BACK fx (behind body) · figure · FRONT fx · overlays.
   HFP.SIL is the body silhouette path in the figure's viewBox — use it for outlines (paper cut, doodle). */
(function () {
  const BOX = { x: 220, y: 380, w: 640, h: 1000 };
  const SIL =
    "M20 1000 L30 600 C34 520 70 462 150 440 L262 404 C268 390 270 370 270 345 C236 330 214 300 206 270 " +
    "C190 268 184 250 186 232 C188 214 198 208 206 214 C200 150 210 90 250 60 C290 28 350 24 392 50 " +
    "C436 78 448 140 434 214 C442 208 452 214 454 232 C456 250 450 268 434 270 C426 300 404 330 370 345 " +
    "C370 370 372 390 378 404 L490 440 C570 462 606 520 610 600 L620 1000 Z";

  function figureSVG(P) {
    return `
<svg id="${P}-fig" viewBox="0 0 640 1000" style="position:absolute;left:${BOX.x}px;top:${BOX.y}px;width:${BOX.w}px;height:${BOX.h}px;overflow:visible">
  <defs>
    <linearGradient id="${P}-tee" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#101217"/><stop offset="0.45" stop-color="#1c1f26"/><stop offset="1" stop-color="#0c0e12"/></linearGradient>
    <linearGradient id="${P}-skin" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#a86f4b"/><stop offset="0.4" stop-color="#c58c63"/><stop offset="1" stop-color="#9c6443"/></linearGradient>
    <linearGradient id="${P}-neck" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#8a5638"/><stop offset="0.5" stop-color="#a86f4b"/><stop offset="1" stop-color="#b47a54"/></linearGradient>
    <linearGradient id="${P}-hair" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#23262d"/><stop offset="1" stop-color="#0d0f13"/></linearGradient>
    <linearGradient id="${P}-rim" x1="1" y1="0" x2="0" y2="0">
      <stop offset="0" stop-color="#5fd0ff" stop-opacity="0.28"/><stop offset="0.07" stop-color="#5fd0ff" stop-opacity="0"/></linearGradient>
  </defs>
  <g id="${P}-body">
    <!-- tee -->
    <path d="M20 1000 L30 600 C34 520 70 462 150 440 L262 404 Q320 434 378 404 L490 440 C570 462 606 520 610 600 L620 1000 Z" fill="url(#${P}-tee)"/>
    <path d="M150 440 C110 452 74 480 56 528" fill="none" stroke="#2c3039" stroke-width="3" opacity="0.8"/>
    <path d="M490 440 C530 452 566 480 584 528" fill="none" stroke="#2c3039" stroke-width="3" opacity="0.8"/>
    <path d="M118 640 C130 760 128 880 120 1000 M522 640 C510 760 512 880 520 1000" fill="none" stroke="#07080b" stroke-width="10" opacity="0.5"/>
    <path d="M20 1000 L30 600 C34 520 70 462 150 440 L262 404 Q320 434 378 404 L490 440 C570 462 606 520 610 600 L620 1000 Z" fill="url(#${P}-rim)"/>
    <!-- neck -->
    <path d="M272 318 L270 404 Q320 440 370 404 L368 318 Z" fill="url(#${P}-neck)"/>
    <path d="M272 340 Q320 378 368 340 L368 360 Q320 392 272 360 Z" fill="#7a4a30" opacity="0.55"/>
    <!-- collar -->
    <path d="M258 402 Q320 446 382 402" fill="none" stroke="#2b2f37" stroke-width="12" stroke-linecap="round"/>
    <path d="M258 402 Q320 446 382 402" fill="none" stroke="#3a3f4a" stroke-width="3" stroke-linecap="round" transform="translate(0,-5)"/>
  </g>
  <g id="${P}-head">
    <!-- ears -->
    <ellipse cx="206" cy="238" rx="18" ry="30" fill="#a86f4b"/><ellipse cx="208" cy="238" rx="8" ry="16" fill="#8a5638"/>
    <ellipse cx="434" cy="238" rx="18" ry="30" fill="#9c6443"/><ellipse cx="432" cy="238" rx="8" ry="16" fill="#7f4f33"/>
    <!-- face -->
    <path d="M206 196 C204 296 250 352 320 352 C390 352 436 296 434 196 C434 118 386 82 320 82 C254 82 206 118 206 196 Z" fill="url(#${P}-skin)"/>
    <path d="M300 344 Q320 356 340 344" fill="none" stroke="#8a5638" stroke-width="3" opacity="0.5"/>
    <ellipse cx="256" cy="268" rx="22" ry="12" fill="#d9786a" opacity="0.14"/><ellipse cx="384" cy="268" rx="22" ry="12" fill="#d9786a" opacity="0.12"/>
    <!-- hair (short textured quiff) -->
    <path d="M200 226 C190 146 216 74 288 50 C340 32 412 42 442 100 C458 132 454 182 440 226 C434 192 426 164 408 150 C376 128 330 142 288 134 C248 128 222 152 214 192 Z" fill="url(#${P}-hair)"/>
    <path d="M250 84 C286 62 344 58 392 76 M240 104 C280 86 340 82 404 98 M300 64 C330 54 366 56 396 66" fill="none" stroke="#3a3f4a" stroke-width="3" stroke-linecap="round" opacity="0.8"/>
    <path d="M214 192 C216 214 214 222 208 228 M426 192 C426 212 430 222 436 228" fill="none" stroke="#15171c" stroke-width="7" stroke-linecap="round"/>
    <!-- brows -->
    <path d="M244 176 Q268 164 294 172" fill="none" stroke="#17191e" stroke-width="9" stroke-linecap="round"/>
    <path d="M346 172 Q372 164 396 176" fill="none" stroke="#17191e" stroke-width="9" stroke-linecap="round"/>
    <!-- eyes -->
    <g id="${P}-eyes">
      <ellipse cx="270" cy="210" rx="11" ry="12" fill="#1a1410"/><ellipse cx="370" cy="210" rx="11" ry="12" fill="#1a1410"/>
      <circle cx="274" cy="206" r="3.4" fill="#fff" opacity="0.9"/><circle cx="374" cy="206" r="3.4" fill="#fff" opacity="0.9"/>
    </g>
    <g id="${P}-lids" opacity="0">
      <path d="M254 210 Q270 216 286 210" fill="none" stroke="#5a3522" stroke-width="5" stroke-linecap="round"/>
      <path d="M354 210 Q370 216 386 210" fill="none" stroke="#5a3522" stroke-width="5" stroke-linecap="round"/>
    </g>
    <!-- glasses: round black frames -->
    <g fill="none" stroke="#0c0d10" stroke-width="10">
      <circle cx="270" cy="212" r="38"/><circle cx="370" cy="212" r="38"/>
      <path d="M308 206 Q320 198 332 206"/><path d="M232 204 L210 198 M408 204 L430 198" stroke-width="8"/>
    </g>
    <path d="M246 190 Q256 180 270 178" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" opacity="0.35"/>
    <path d="M346 190 Q356 180 370 178" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" opacity="0.35"/>
    <!-- nose -->
    <path d="M322 236 C320 256 316 272 304 280 Q320 290 338 280" fill="none" stroke="#7f4f33" stroke-width="5" stroke-linecap="round" opacity="0.75"/>
    <!-- mouth: closed smile + open mouth (talk) -->
    <path id="${P}-mClosed" d="M290 306 Q320 322 350 306" fill="none" stroke="#5a2f22" stroke-width="7" stroke-linecap="round"/>
    <g id="${P}-mOpen" opacity="0">
      <path d="M290 304 Q320 304 350 304 Q346 336 320 338 Q294 336 290 304 Z" fill="#4a1f19"/>
      <path d="M296 306 L344 306 L340 314 L300 314 Z" fill="#f4eee8"/>
      <ellipse cx="320" cy="330" rx="14" ry="5" fill="#c8605a"/>
    </g>
    <!-- right-side rim light on the head -->
    <path d="M434 196 C434 296 396 346 340 352" fill="none" stroke="#7fd8ff" stroke-width="4" opacity="0.45"/>
  </g>
</svg>`;
  }

  // studio backdrop for 1080x1350 (wall + window light + shelf + plant + floor) — sits behind everything
  function backdropHTML(P) {
    return `
<div id="${P}-bd" style="position:absolute;left:0;top:0;width:1080px;height:1350px;overflow:hidden">
  <img src="assets/background/plate.png" alt="" style="position:absolute;left:0;top:0;width:1080px;height:1350px"/>
  <div style="position:absolute;left:190px;top:330px;width:700px;height:700px;border-radius:50%;background:radial-gradient(closest-side,rgba(80,150,230,0.30),rgba(80,150,230,0))"></div>
  <svg viewBox="0 0 1080 1350" style="position:absolute;left:0;top:0;width:1080px;height:1350px">
    <defs>
      <linearGradient id="${P}-win" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9fd6ff" stop-opacity="0.55"/><stop offset="1" stop-color="#3f7fc8" stop-opacity="0.25"/></linearGradient>
      <linearGradient id="${P}-shelf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a5d92"/><stop offset="1" stop-color="#1a3060"/></linearGradient>
    </defs>
    <!-- window, left -->
    <rect x="60" y="300" width="250" height="330" rx="10" fill="#0b1836" stroke="#2b4a7e" stroke-width="10"/>
    <rect x="72" y="312" width="226" height="306" rx="4" fill="url(#${P}-win)"/>
    <path d="M185 312 V618 M72 465 H298" stroke="#2b4a7e" stroke-width="8"/>
    <path d="M90 600 L150 330 M140 600 L200 330" stroke="#ffffff" stroke-width="10" opacity="0.08"/>
    <path d="M72 618 L298 618 L330 660 L40 660 Z" fill="#1b3262"/>
    <!-- shelf, right -->
    <rect x="760" y="520" width="270" height="12" rx="3" fill="url(#${P}-shelf)"/>
    <rect x="776" y="452" width="20" height="68" rx="3" fill="#e8eef6"/><rect x="798" y="440" width="18" height="80" rx="3" fill="#2f6fae"/>
    <rect x="818" y="460" width="22" height="60" rx="3" fill="#a9c2de"/><rect x="842" y="468" width="14" height="52" rx="3" fill="#1d3f73"/>
    <rect x="872" y="466" width="62" height="54" rx="6" fill="#0f1e3e" stroke="#7fa7d6" stroke-width="3"/><circle cx="903" cy="493" r="11" fill="none" stroke="#00c9ff" stroke-width="3" opacity="0.7"/>
    <path d="M960 520 Q972 478 990 468 Q986 498 972 520 Z M978 520 Q994 484 1016 478 Q1004 506 988 520 Z" fill="#5c9a50"/><rect x="962" y="506" width="40" height="14" rx="3" fill="#e8eef6"/>
    <rect x="760" y="700" width="270" height="12" rx="3" fill="url(#${P}-shelf)"/>
    <rect x="790" y="640" width="70" height="60" rx="6" fill="#e8eef6" opacity="0.9"/><path d="M800 690 L820 662 L836 680 L850 668 L850 690 Z" fill="#2f6fae"/>
    <rect x="884" y="652" width="16" height="48" rx="3" fill="#a9c2de"/><rect x="902" y="644" width="20" height="56" rx="3" fill="#e8eef6"/>
    <!-- tall plant, left floor -->
    <path d="M110 1040 C70 960 60 880 90 820 C110 880 120 960 116 1040 Z M120 1040 C150 950 190 900 220 880 C200 950 160 1000 126 1040 Z M104 1040 C60 990 30 960 20 920 C64 940 92 990 108 1040 Z" fill="#3f7640"/>
    <path d="M70 1040 L160 1040 L150 1130 Q115 1142 80 1130 Z" fill="#e8eef6"/><path d="M140 1040 L160 1040 L150 1130 L134 1132 Z" fill="#9fb3cc" opacity="0.6"/>
    <!-- floor line -->
    <rect x="0" y="1130" width="1080" height="220" fill="#081333" opacity="0.55"/>
    <rect x="0" y="1128" width="1080" height="3" fill="#7fa7d6" opacity="0.18"/>
  </svg>
</div>`;
  }

  // label chip "01/17 · ORBIT" (top-right) + AIpreneur logo (top-left)
  function chromeHTML(P, n, name) {
    return `
<div id="${P}-chrome" style="position:absolute;left:0;top:0;width:1080px;height:1350px;pointer-events:none">
  <img id="${P}-logo" src="assets/branding/logo_aipreneur_white_user_crop.png" alt="AI PRENEUR"
    style="position:absolute;left:60px;top:66px;width:270px;height:26px;filter:drop-shadow(0 3px 10px rgba(2,8,26,0.55))"/>
  <div id="${P}-chip" style="position:absolute;right:60px;top:52px;height:54px;padding:0 24px 0 20px;border-radius:27px;display:flex;align-items:center;gap:14px;
    background:rgba(7,15,38,0.72);box-shadow:inset 0 0 0 1.5px rgba(127,216,255,0.35),0 8px 24px rgba(2,8,26,0.45);font-family:Poppins,sans-serif">
    <span style="font-weight:700;font-size:24px;color:#00c9ff;letter-spacing:0.02em">${String(n).padStart(2, "0")}<span style="color:#7f93b3">/17</span></span>
    <span style="width:2px;height:22px;background:rgba(169,194,222,0.35)"></span>
    <span style="font-weight:700;font-size:24px;color:#ffffff;letter-spacing:0.12em;text-transform:uppercase">${name}</span>
  </div>
</div>`;
  }

  function mount(host, P) {
    host.insertAdjacentHTML("beforeend", figureSVG(P));
    const $ = (id) => document.getElementById(P + "-" + id);
    return { fig: $("fig"), head: $("head"), body: $("body"), lids: $("lids"), eyes: $("eyes"), mOpen: $("mOpen"), mClosed: $("mClosed") };
  }

  // idle life: breathing, small head sway, blinks, talking mouth (all pure functions of t)
  const TALK = [0.0, 0.55, 0.9, 1.4, 1.7, 2.3, 2.6, 3.1, 3.5]; // syllable-ish rhythm, repeats every 3.6 s
  function animate(R, t, opts) {
    const o = opts || {};
    const TAU = Math.PI * 2, br = Math.sin((t / 3.4) * TAU);
    R.body.setAttribute("transform", "translate(0," + (br * 2.2).toFixed(2) + ")");
    const sway = Math.sin((t / 4.1) * TAU) * 1.6 + Math.sin((t / 1.7) * TAU) * 0.5;
    const nod = Math.sin((t / 2.3) * TAU) * 2.2;
    R.head.setAttribute("transform", "translate(0," + (br * 1.6 + nod).toFixed(2) + ") rotate(" + sway.toFixed(2) + " 320 330)");
    const bl = ((t + 0.7) % 3.3) < 0.12; // blink
    R.eyes.setAttribute("opacity", bl ? "0" : "1"); R.lids.setAttribute("opacity", bl ? "1" : "0");
    let open = 0;
    if (o.talk !== false) {
      const u = t % 3.6; let near = 9;
      for (const s of TALK) near = Math.min(near, Math.abs(u - s - 0.12));
      open = Math.max(0, 1 - near / 0.14);
    }
    R.mOpen.setAttribute("opacity", open.toFixed(2));
    R.mOpen.setAttribute("transform", "translate(0,304) scale(1," + (0.45 + 0.55 * open).toFixed(3) + ") translate(0,-304)");
    R.mClosed.setAttribute("opacity", (1 - open).toFixed(2));
  }

  window.HFP = { BOX, SIL, figureSVG, backdropHTML, chromeHTML, mount, animate };
})();

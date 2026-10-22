/* AI PRENEUR v3 — shared interview room (S01, S02, S06 build the identical room from here).
   Static markup only; every motion is driven by the scene's own timeline through HFRoom.cam()/HFRoom.light().
   Layers (differential parallax around the laptop screen centre 650,843):
     L0 wall  (f 0.55): window (user icon) + wall shelf + window light on the wall
     L1 set   (f 1.00): floor, rug, desk (user icon), laptop (user icon) + screen, lamp, plant, books, mug, light pools, shadows
     L2 front (f 1.35): applicant seen from behind (rim-lit silhouette)                                              */
(function () {
  if (window.HFRoom) return;
  const LAP = { x: 430, y: 736, w: 440, h: 349 };
  const SCR = { x: 477.5, y: 747, w: 345, h: 192.5 };
  const O = { x: 650, y: 843 };
  function svgPerson(P) {
    return `<svg id="${P}-person" viewBox="0 0 500 640" style="position:absolute;left:30px;top:968px;width:560px;height:717px;overflow:visible">
      <defs>
        <linearGradient id="${P}-jk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0d1730"/><stop offset="0.45" stop-color="#172848"/><stop offset="0.8" stop-color="#13213d"/><stop offset="1" stop-color="#1f3a63"/></linearGradient>
        <linearGradient id="${P}-hr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#26324d"/><stop offset="0.5" stop-color="#121a2c"/><stop offset="1" stop-color="#090e1b"/></linearGradient>
        <linearGradient id="${P}-nk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6e4a3b"/><stop offset="0.5" stop-color="#9c6d55"/><stop offset="1" stop-color="#7a5242"/></linearGradient>
        <linearGradient id="${P}-ch" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c2b4c"/><stop offset="1" stop-color="#070d1e"/></linearGradient>
        <radialGradient id="${P}-hrHi" cx="0.72" cy="0.3" r="0.6"><stop offset="0" stop-color="#4c6a9c" stop-opacity="0.55"/><stop offset="1" stop-color="#4c6a9c" stop-opacity="0"/></radialGradient>
      </defs>
      <g id="${P}-body">
        <path d="M18 900 L30 448 C32 392 62 352 118 334 C160 320 192 304 212 286 L288 286 C308 304 340 320 382 334 C438 352 468 392 470 448 L482 900 Z" fill="url(#${P}-jk)"/>
        <path d="M382 334 C438 352 468 392 470 448 L482 900" fill="none" stroke="#5fd0ff" stroke-width="3" opacity="0.38"/>
        <path d="M118 334 C62 352 32 392 30 448" fill="none" stroke="#f3b06a" stroke-width="3" opacity="0.32"/>
        <path d="M206 288 Q250 316 294 288 L300 300 Q250 330 200 300 Z" fill="#dfe6ef" opacity="0.92"/>
        <path d="M250 318 L250 900" stroke="#0a1326" stroke-width="3" opacity="0.7"/>
      </g>
      <g id="${P}-head">
        <path d="M218 200 L218 292 Q250 304 282 292 L282 200 Z" fill="url(#${P}-nk)"/>
        <path d="M218 262 Q250 280 282 262 L282 292 Q250 304 218 292 Z" fill="#000" opacity="0.22"/>
        <path d="M184 150 Q172 150 172 170 Q174 196 190 198 Z" fill="#9a6a54"/><path d="M316 150 Q328 150 328 170 Q326 196 310 198 Z" fill="#8a5f4b"/>
        <path d="M186 140 C182 84 212 56 250 56 C290 56 318 84 314 140 C312 176 304 206 292 222 Q272 214 262 224 Q250 232 238 224 Q228 214 208 222 C196 206 188 176 186 140 Z" fill="url(#${P}-hr)"/>
        <path d="M186 140 C182 84 212 56 250 56 C290 56 318 84 314 140 C312 176 304 206 292 222 L208 222 C196 206 188 176 186 140 Z" fill="url(#${P}-hrHi)"/>
        <path d="M290 70 C308 88 316 114 314 146" fill="none" stroke="#6fdcff" stroke-width="3" stroke-linecap="round" opacity="0.5"/>
        <path d="M204 76 C192 94 186 116 186 142" fill="none" stroke="#f3b06a" stroke-width="2.6" stroke-linecap="round" opacity="0.4"/>
        <path d="M216 100 Q250 86 286 98 M208 132 Q250 118 292 130 M212 166 Q250 154 288 164" fill="none" stroke="#3a4a6c" stroke-width="2.2" stroke-linecap="round" opacity="0.55"/>
      </g>
      <path d="M88 900 L98 452 Q100 418 138 412 L362 412 Q400 418 402 452 L412 900 Z" fill="url(#${P}-ch)"/>
      <path d="M138 414 L362 414" stroke="rgba(170,210,255,0.22)" stroke-width="3"/>
      <path d="M402 452 L412 900" stroke="#5fd0ff" stroke-width="2.5" opacity="0.3"/>
    </svg>`;
  }
  function svgLamp(P) {
    return `<svg id="${P}-lamp" viewBox="0 0 300 420" style="position:absolute;left:150px;top:742px;width:300px;height:420px;overflow:visible">
      <defs><linearGradient id="${P}-lm" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3f5f8f"/><stop offset="1" stop-color="#14254a"/></linearGradient>
        <radialGradient id="${P}-bulb" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#fff6e0"/><stop offset="0.5" stop-color="#ffd79a"/><stop offset="1" stop-color="#ffb860" stop-opacity="0"/></radialGradient></defs>
      <ellipse cx="78" cy="318" rx="62" ry="15" fill="#0a1328"/>
      <path d="M22 312 Q22 296 78 294 Q134 296 134 312 L134 318 Q78 334 22 318 Z" fill="url(#${P}-lm)"/>
      <path d="M74 300 L52 170" stroke="url(#${P}-lm)" stroke-width="13" stroke-linecap="round"/>
      <path d="M52 170 L172 74" stroke="url(#${P}-lm)" stroke-width="12" stroke-linecap="round"/>
      <circle cx="52" cy="170" r="11" fill="#2c4673"/><circle cx="74" cy="300" r="10" fill="#2c4673"/><circle cx="172" cy="74" r="10" fill="#2c4673"/>
      <g transform="rotate(-20 172 74)"><path d="M150 64 L208 64 L236 128 L122 128 Z" fill="url(#${P}-lm)"/><path d="M150 64 L208 64" stroke="#6f93c4" stroke-width="3"/>
        <ellipse id="${P}-bulbG" cx="179" cy="130" rx="52" ry="14" fill="url(#${P}-bulb)" opacity="0"/></g>
    </svg>`;
  }
  function svgPlant(P) {
    return `<svg id="${P}-plant" viewBox="0 0 160 260" style="position:absolute;left:868px;top:850px;width:150px;height:244px;overflow:visible">
      <g id="${P}-leaves" fill="#4f8a4a"><path d="M80 170 C40 140 20 90 34 40 C60 80 76 120 80 170 Z"/><path d="M82 170 C110 120 140 100 152 60 C150 110 120 150 82 170 Z" fill="#6aa65a"/>
        <path d="M78 170 C70 110 80 60 100 20 C108 70 96 120 78 170 Z" fill="#5c9a50"/><path d="M80 168 C50 160 18 150 4 122 C40 124 62 140 80 168 Z" fill="#3f7640"/></g>
      <path d="M44 166 L116 166 L106 246 Q80 254 54 246 Z" fill="#e8eef6"/><path d="M44 166 L116 166 L114 180 L46 180 Z" fill="#c9d6e6"/>
      <path d="M106 166 L116 166 L106 246 L96 246 Z" fill="#9fb3cc" opacity="0.6"/>
    </svg>`;
  }
  function build(host, P) {
    const html = `
    <div id="${P}-L0" class="hfr-L" style="position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:${O.x}px ${O.y}px">
      <div id="${P}-winGlow" style="position:absolute;left:30px;top:520px;width:560px;height:520px;border-radius:50%;background:radial-gradient(closest-side,rgba(190,235,255,0.35),rgba(190,235,255,0))"></div>
      <img id="${P}-win" src="assets/icons/window.png" alt="" style="position:absolute;left:78px;top:520px;width:470px;height:433px"/>
      <div id="${P}-winDim" style="position:absolute;left:78px;top:520px;width:470px;height:433px;background:linear-gradient(180deg,rgba(8,18,46,0.18),rgba(8,18,46,0.32));-webkit-mask:url(assets/icons/window.png) center/100% 100% no-repeat;mask:url(assets/icons/window.png) center/100% 100% no-repeat"></div>
      <svg style="position:absolute;left:0;top:0;width:1080px;height:1920px" viewBox="0 0 1080 1920">
        <defs><linearGradient id="${P}-shelf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a5d92"/><stop offset="1" stop-color="#1a3060"/></linearGradient></defs>
        <rect x="690" y="604" width="300" height="14" rx="3" fill="url(#${P}-shelf)"/><rect x="700" y="618" width="290" height="22" fill="#020818" opacity="0.28" style="filter:blur(6px)"/>
        <rect x="712" y="532" width="22" height="72" rx="3" fill="#e8eef6"/><rect x="736" y="520" width="18" height="84" rx="3" fill="#2f6fae"/>
        <rect x="756" y="540" width="24" height="64" rx="3" fill="#a9c2de"/><rect x="782" y="548" width="16" height="56" rx="3" fill="#1d3f73"/>
        <rect x="800" y="548" width="68" height="56" rx="6" fill="#0f1e3e" stroke="#7fa7d6" stroke-width="3"/><circle cx="834" cy="576" r="12" fill="none" stroke="#00c9ff" stroke-width="3" opacity="0.7"/>
        <path d="M900 604 Q912 560 930 550 Q926 580 912 604 Z M918 604 Q934 566 958 560 Q946 590 928 604 Z" fill="#5c9a50"/><rect x="902" y="590" width="40" height="14" rx="3" fill="#e8eef6"/>
      </svg>
    </div>
    <div id="${P}-L1" class="hfr-L" style="position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:${O.x}px ${O.y}px">
      <div style="position:absolute;left:-200px;top:1500px;width:1480px;height:620px;background:linear-gradient(180deg,#14244a 0%,#0b1633 40%,#060d22 100%)"></div>
      <div style="position:absolute;left:-200px;top:1498px;width:1480px;height:4px;background:rgba(160,200,245,0.18)"></div>
      <div style="position:absolute;left:150px;top:1560px;width:800px;height:150px;border-radius:50%;background:radial-gradient(closest-side,rgba(60,96,160,0.55),rgba(60,96,160,0))"></div>
      <div style="position:absolute;left:90px;top:1500px;width:960px;height:90px;border-radius:50%;background:radial-gradient(closest-side,rgba(2,8,26,0.75),rgba(2,8,26,0))"></div>
      <div id="${P}-shaft" style="position:absolute;left:0;top:0;width:1080px;height:1920px;mix-blend-mode:screen;opacity:0.9;
        background:linear-gradient(115deg,rgba(0,0,0,0) 0%,rgba(0,0,0,0) 0%);"></div>
      <svg id="${P}-dust" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible;pointer-events:none;mix-blend-mode:screen;filter:blur(0.8px)">${Array.from({length:14},(_,i)=>`<circle id="${P}-d${i}" r="${(1.6+(i*7%5)*0.5).toFixed(1)}" fill="#e6f4ff" opacity="0"/>`).join("")}</svg>
      <img id="${P}-desk" src="assets/icons/desk.png" alt="" style="position:absolute;left:80px;top:1000px;width:920px;height:541px"/>
      <div style="position:absolute;left:80px;top:1097px;width:920px;height:40px;background:linear-gradient(180deg,rgba(2,8,26,0.35),rgba(2,8,26,0));pointer-events:none"></div>
      <div id="${P}-deskTone" style="position:absolute;left:80px;top:1000px;width:920px;height:541px;background:linear-gradient(90deg,rgba(10,22,52,0.15),rgba(10,22,52,0.45));-webkit-mask:url(assets/icons/desk.png) center/100% 100% no-repeat;mask:url(assets/icons/desk.png) center/100% 100% no-repeat"></div>
      <div id="${P}-lampPool" style="position:absolute;left:200px;top:1028px;width:450px;height:92px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,214,150,0.75),rgba(255,196,124,0.26) 58%,rgba(255,190,120,0));mix-blend-mode:screen;opacity:0"></div>
      <div style="position:absolute;left:470px;top:1062px;width:470px;height:44px;border-radius:50%;background:radial-gradient(closest-side,rgba(2,8,26,0.6),rgba(2,8,26,0))"></div>
      <div style="position:absolute;left:440px;top:1072px;width:420px;height:22px;border-radius:50%;background:radial-gradient(closest-side,rgba(2,8,26,0.85),rgba(2,8,26,0))"></div>
      <svg style="position:absolute;left:0;top:0;width:1080px;height:1920px" viewBox="0 0 1080 1920">
        <rect x="205" y="1050" width="150" height="16" rx="3" fill="#e8eef6"/><rect x="215" y="1036" width="130" height="16" rx="3" fill="#2f6fae"/><rect x="225" y="1024" width="112" height="14" rx="3" fill="#a9c2de"/>
        <ellipse cx="402" cy="1074" rx="26" ry="6" fill="#020818" opacity="0.5"/><path d="M380 1030 L424 1030 L420 1072 Q402 1078 384 1072 Z" fill="#e8eef6"/><path d="M424 1040 Q440 1042 438 1054 Q436 1064 421 1062" fill="none" stroke="#e8eef6" stroke-width="5"/>
        <ellipse cx="402" cy="1032" rx="22" ry="5" fill="#5a3a2a"/>
      </svg>
      ${svgPlant(P)}
      <div style="position:absolute;left:880px;top:1078px;width:150px;height:26px;border-radius:50%;background:radial-gradient(closest-side,rgba(2,8,26,0.55),rgba(2,8,26,0))"></div>
      <div id="${P}-lap" style="position:absolute;left:${LAP.x}px;top:${LAP.y}px;width:${LAP.w}px;height:${LAP.h}px"><img id="${P}-lapImg" src="assets/icons/laptop.png" alt="" style="width:100%;height:100%;display:block"/></div>
      <div id="${P}-scr" style="position:absolute;left:${SCR.x}px;top:${SCR.y}px;width:${SCR.w}px;height:${SCR.h}px;border-radius:4px;overflow:hidden"></div>
      <div id="${P}-scrGlow" style="position:absolute;left:400px;top:690px;width:500px;height:330px;border-radius:50%;background:radial-gradient(closest-side,rgba(110,190,255,0.22),rgba(110,190,255,0));mix-blend-mode:screen"></div>
      ${svgLamp(P)}
      <svg id="${P}-lampCone" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0;width:1080px;height:1920px;mix-blend-mode:screen;opacity:0;overflow:visible">
        <defs><linearGradient id="${P}-beam" gradientUnits="userSpaceOnUse" x1="348" y1="866" x2="420" y2="1075"><stop offset="0" stop-color="#ffe2b0" stop-opacity="0.55"/><stop offset="0.55" stop-color="#ffcf96" stop-opacity="0.22"/><stop offset="1" stop-color="#ffc488" stop-opacity="0.05"/></linearGradient>
          <filter id="${P}-beamBlur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="9"/></filter></defs>
        <polygon points="298,880 398,848 610,1080 236,1094" fill="url(#${P}-beam)" filter="url(#${P}-beamBlur)"/>
      </svg>
      <div id="${P}-bulbHalo" style="position:absolute;left:278px;top:796px;width:140px;height:140px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,236,196,0.55),rgba(255,210,150,0.16) 55%,rgba(255,200,140,0));mix-blend-mode:screen;opacity:0"></div>
      <svg id="${P}-steam" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible;pointer-events:none">
        <path id="${P}-st1" d="M396 1024 C384 1004 410 990 398 968 C388 950 408 936 400 918" fill="none" stroke="#dfeaf8" stroke-width="4" stroke-linecap="round" stroke-dasharray="40 200" opacity="0"/>
        <path id="${P}-st2" d="M408 1024 C420 1004 396 988 410 966 C422 946 402 932 412 912" fill="none" stroke="#dfeaf8" stroke-width="3" stroke-linecap="round" stroke-dasharray="34 200" opacity="0"/>
      </svg>
    </div>
    <div id="${P}-L2" class="hfr-L" style="position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:${O.x}px ${O.y}px">${svgPerson(P)}</div>`;
    host.insertAdjacentHTML("afterbegin", html);
    const $ = (id) => document.getElementById(P + "-" + id);
    // window light falling to the right and down onto the desk (two soft shafts)
    $("shaft").style.background =
      "linear-gradient(118deg, rgba(0,0,0,0) 34%, rgba(200,236,255,0.10) 40%, rgba(200,236,255,0.0) 47%, rgba(200,236,255,0.08) 52%, rgba(0,0,0,0) 60%)";
    $("shaft").style.clipPath = "polygon(110px 560px, 540px 560px, 1080px 1500px, 380px 1500px)";
    return { L0: $("L0"), L1: $("L1"), L2: $("L2"), scr: $("scr"), lapImg: $("lapImg"), head: $("head"), body: $("body"),
      lampPool: $("lampPool"), lampCone: $("lampCone"), bulb: $("bulbG"), halo: $("bulbHalo"), leaves: $("leaves"), st: [$("st1"), $("st2")], dust: Array.from({length:14},(_, i) => $("d" + i)), lampK: 0, shaftK: 1, shaft: $("shaft"), winGlow: $("winGlow"), scrGlow: $("scrGlow") };
  }
  // camera: scale s about the screen centre + vertical tilt y + lateral x, applied with differential parallax
  function cam(R, s, x, y, extraFrontY) {
    const L = (f, dy) => "translate(" + (x * f).toFixed(2) + "px," + (y * f + (dy || 0)).toFixed(2) + "px) scale(" + (1 + (s - 1) * f).toFixed(4) + ")";
    R.L0.style.transform = L(0.55); R.L1.style.transform = L(1.0); R.L2.style.transform = L(1.35, extraFrontY || 0);
  }
  // lamp: 0 = off, 1 = on (bulb, cone, desk pool)
  function light(R, lamp, shaft) {
    R.lampPool.style.opacity = String(lamp); R.lampCone.style.opacity = String(lamp); R.bulb.setAttribute("opacity", String(lamp));
    R.halo.style.opacity = String(lamp); R.lampK = lamp;
    if (shaft !== undefined) { R.shaft.style.opacity = String(0.9 * shaft); R.winGlow.style.opacity = String(shaft); R.shaftK = shaft; }
  }
  // applicant acting: breathing only (closed form of global time g) + a small shoulder settle `k` (0..1)
  function act(R, g, k) {
    const br = Math.sin((g / 3.6) * Math.PI * 2);
    R.body.setAttribute("transform", "translate(0," + (br * 1.2).toFixed(2) + ")");
    R.head.setAttribute("transform", "translate(0," + (br * 1.0 + (k || 0) * 5).toFixed(2) + ")");
    ambient(R, g);
  }
  // ambient life, pure function of global time g: plant sway, mug steam, dust drifting in the window light, warm lamp breathing
  function ambient(R, g) {
    const TAU = Math.PI * 2;
    R.leaves.setAttribute("transform", "rotate(" + (Math.sin(g / 4.2 * TAU) * 1.6 + Math.sin(g / 1.9 * TAU) * 0.4).toFixed(2) + " 80 170)");
    R.st.forEach((el, i) => {
      const per = 2.6 + i * 0.5, u = ((g + i * 1.3) / per) % 1;
      el.setAttribute("stroke-dashoffset", (40 - u * 150).toFixed(1));
      el.setAttribute("opacity", (0.38 * Math.sin(u * Math.PI)).toFixed(3));
      el.setAttribute("transform", "translate(" + (Math.sin(g * 0.9 + i) * 3).toFixed(1) + ",0)");
    });
    R.dust.forEach((el, i) => {
      const per = 9 + (i % 5) * 1.7, u = ((g / per) + i * 0.137) % 1;
      // drift down the window shaft (from the window towards the desk), slight sideways wobble
      const x0 = 180 + ((i * 97) % 360), x = x0 + u * 230 + Math.sin(g * 0.7 + i) * 10, y = 600 + u * 520 + Math.cos(g * 0.5 + i * 2) * 8;
      el.setAttribute("cx", x.toFixed(1)); el.setAttribute("cy", y.toFixed(1));
      el.setAttribute("opacity", (0.45 * R.shaftK * Math.sin(u * Math.PI) * (0.5 + 0.5 * Math.sin(g * 1.3 + i * 1.7))).toFixed(3));
    });
    const warm = 0.96 + 0.04 * Math.sin(g / 3.1 * TAU);
    R.lampPool.style.opacity = String((R.lampK * warm).toFixed(3));
  }
  window.HFRoom = { build, cam, light, act, LAP, SCR, O };
})();

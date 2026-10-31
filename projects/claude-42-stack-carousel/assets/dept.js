/* Department slide template (Build / Design / Grow / Run). Re-laid-out vs the reference: two-line title left,
   mascots right, department rail under the header, add-ons as a 2-column grid of 3D-flipping glass tiles,
   then a highlight that walks through the tiles. render(t) is a pure function of the slide's local time. */
(function () {
  const K = window.K;
  function build(host, P, key, slide, total) {
    const D = window.STACK.depts[key], A = D.accent, A2 = D.accent2, items = D.items, n = items.length;
    const odd = n % 2 === 1, rows = Math.ceil(n / 2);
    const GX = 60, GY = 574, GW = 960, GH = 690, GAP = 16, CW = (GW - GAP) / 2, RH = (GH - GAP * (rows - 1)) / rows;
    const big = RH > 140, icon = big ? 72 : 62;
    const fsN = big ? 29 : 26, fsR = big ? 20 : 18, fsD = big ? 19 : 17;
    let tiles = "";
    items.forEach((it, i) => {
      const [num, name, role, desc, calls, ic] = it;
      const wide = odd && i === n - 1;
      const col = wide ? 0 : i % 2, row = Math.floor(i / 2);
      const x = GX + col * (CW + GAP), y = GY + row * (RH + GAP), w = wide ? GW : CW;
      tiles += `
      <div id="${P}-tw${i}" style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${RH}px;perspective:1100px">
        <div id="${P}-t${i}" style="position:absolute;inset:0;border-radius:22px;background:linear-gradient(160deg,rgba(255,255,255,0.10),rgba(255,255,255,0.035));
          box-shadow:inset 0 0 0 1px rgba(255,255,255,0.12),0 18px 40px rgba(2,6,24,0.35);overflow:hidden">
          <div id="${P}-tg${i}" style="position:absolute;inset:0;border-radius:22px;box-shadow:inset 0 0 0 2px ${A};background:radial-gradient(80% 120% at 0% 0%,${A}33,transparent 60%);opacity:0"></div>
          <div id="${P}-ti${i}" style="position:absolute;left:20px;top:${(RH - icon) / 2}px">${K.iconHTML(ic, icon)}</div>
          <div class="k-txt" style="position:absolute;left:${20 + icon + 18}px;top:${big ? 22 : 14}px;right:${calls ? 120 : 66}px">
            <div style="font-weight:700;font-size:${fsN}px;line-height:1.1;color:#fff;letter-spacing:-0.01em;white-space:nowrap">${name}</div>
            <div style="font-weight:700;font-size:${fsR}px;line-height:1.3;color:${A};margin-top:${big ? 3 : 1}px">${role}</div>
            <div style="font-weight:400;font-size:${fsD}px;line-height:1.32;color:rgba(222,232,255,0.74);margin-top:${big ? 6 : 3}px">${desc}</div>
          </div>
          <div class="k-txt" style="position:absolute;right:20px;top:${big ? 18 : 12}px;font-weight:700;font-size:${big ? 30 : 26}px;color:${A};opacity:0.55">${num}</div>
          ${calls ? `<div class="k-txt" id="${P}-c${i}" style="position:absolute;right:18px;bottom:${big ? 16 : 12}px;padding:5px 12px;border-radius:999px;background:${A}26;box-shadow:inset 0 0 0 1px ${A}66;font-weight:700;font-size:15px;letter-spacing:0.12em;color:${A2}">${calls} CALLS</div>` : ""}
        </div>
      </div>`;
    });
    // department rail
    const rail = ["CEO"].concat(window.STACK.order.map((k) => window.STACK.depts[k].key));
    let pills = "";
    const PW = (GW - 5 * 12) / 6;
    rail.forEach((r, i) => {
      const on = r === D.key;
      const dk = i === 0 ? null : window.STACK.depts[window.STACK.order[i - 1]];
      pills += `<div id="${P}-p${i}" class="k-txt" style="position:absolute;left:${GX + i * (PW + 12)}px;top:504px;width:${PW}px;height:48px;border-radius:14px;display:flex;align-items:center;justify-content:center;gap:9px;
        font-weight:700;font-size:17px;letter-spacing:0.16em;color:${on ? "#fff" : "rgba(220,230,255,0.5)"};
        background:${on ? A + "33" : "rgba(255,255,255,0.05)"};box-shadow:inset 0 0 0 1px ${on ? A : "rgba(255,255,255,0.1)"}">
        ${i === 0 ? `<img class="k-pix" src="assets/mascots/10_default_mascot.png" style="width:34px"/>` : `<span style="width:8px;height:8px;border-radius:50%;background:${on ? A : dk.accent};opacity:${on ? 1 : 0.6}"></span>`}${r}</div>`;
    });
    host.innerHTML = `
      ${K.bgHTML(P + "b", A)}
      <div id="${P}-chip" class="k-txt" style="position:absolute;right:64px;top:50px;height:50px;padding:0 22px;border-radius:25px;display:flex;align-items:center;gap:12px;
        background:rgba(255,255,255,0.07);box-shadow:inset 0 0 0 1px rgba(255,255,255,0.14);font-weight:700;font-size:17px;letter-spacing:0.18em;color:rgba(230,238,255,0.85)">
        <span style="width:9px;height:9px;border-radius:50%;background:${A};box-shadow:0 0 12px ${A}"></span>DEPARTMENT ${D.n} OF 5</div>
      <div id="${P}-kick" class="k-txt" style="position:absolute;left:64px;top:150px;font-weight:700;font-size:21px;letter-spacing:0.22em;color:${A};white-space:nowrap;overflow:hidden">${D.key} · ${D.count} ADD-ONS</div>
      <div id="${P}-l1" class="k-txt" style="position:absolute;left:60px;top:186px;font-weight:700;font-size:100px;line-height:1;letter-spacing:-0.035em;color:#fff">${D.title[0]}</div>
      <div id="${P}-l2" class="k-txt" style="position:absolute;left:60px;top:290px;font-weight:700;font-size:100px;line-height:1.02;letter-spacing:-0.035em;padding-bottom:8px;
        background:linear-gradient(100deg,${A} 0%,${A2} 45%,${A} 90%);background-size:200% 100%;-webkit-background-clip:text;background-clip:text;color:transparent">${D.title[1]}</div>
      <div id="${P}-sub" class="k-txt" style="position:absolute;left:64px;top:412px;width:560px;font-weight:400;font-size:26px;line-height:1.35;color:rgba(222,232,255,0.78)">${D.sub}</div>
      <div id="${P}-mglow" style="position:absolute;left:640px;top:150px;width:420px;height:360px;border-radius:50%;background:radial-gradient(closest-side,${A}40,transparent)"></div>
      <div id="${P}-shad1" style="position:absolute;left:700px;top:462px;width:230px;height:26px;border-radius:50%;background:radial-gradient(closest-side,rgba(0,0,0,0.45),transparent)"></div>
      ${K.mascotHTML(P + "-m1", D.mascots[0], 270, "left:680px;top:200px")}
      ${K.mascotHTML(P + "-m2", D.mascots[1], 210, "left:850px;top:300px")}
      ${pills}
      ${tiles}
      ${K.chromeHTML(P + "c", slide, total)}`;
    const $ = (s) => document.getElementById(P + "-" + s);
    const T = items.map((_, i) => ({ w: $("tw" + i), t: $("t" + i), g: $("tg" + i), ic: $("ti" + i), c: $("c" + i) }));
    return function render(t) {
      K.bg(P + "b", t); K.chrome(P + "c", t);
      const { seg, eo, eo4, back } = K;
      // header
      const kk = seg(t, 0.1, 0.55); $("kick").style.clipPath = `inset(0 ${(100 - 100 * eo(kk)).toFixed(1)}% 0 0)`;
      const a1 = eo4(seg(t, 0.12, 0.62)), a2 = eo4(seg(t, 0.26, 0.78));
      $("l1").style.transform = `translateY(${((1 - a1) * 70).toFixed(1)}px)`; $("l1").style.opacity = a1.toFixed(3);
      $("l2").style.transform = `translateY(${((1 - a2) * 70).toFixed(1)}px)`; $("l2").style.opacity = a2.toFixed(3);
      $("l2").style.backgroundPosition = `${(100 - ((t * 22) % 200)).toFixed(1)}% 0`;
      const as = eo(seg(t, 0.45, 0.95)); $("sub").style.opacity = as.toFixed(3); $("sub").style.transform = `translateY(${((1 - as) * 24).toFixed(1)}px)`;
      const ac = eo(seg(t, 0.05, 0.45)); $("chip").style.opacity = ac.toFixed(3); $("chip").style.transform = `translateY(${((1 - ac) * -16).toFixed(1)}px)`;
      // mascots: drop in on 12 fps steps, then hop
      [["m1", 0.3, 2.0, 0, 16], ["m2", 0.48, 1.7, 0.6, 20]].forEach(([id, t0, per, ph, amp]) => {
        const ts = Math.floor(t * 12) / 12, d = back(seg(ts, t0, t0 + 0.42), 2.2);
        const hp = t > t0 + 0.5 ? K.hop(t, per, ph, amp) : { y: 0, sx: 1, sy: 1 };
        $(id).style.transform = `translateY(${((1 - d) * -260 + hp.y).toFixed(1)}px) scale(${hp.sx.toFixed(3)},${hp.sy.toFixed(3)})`;
        $(id).style.opacity = (seg(ts, t0, t0 + 0.08)).toFixed(2);
      });
      $("mglow").style.opacity = (eo(seg(t, 0.3, 1.0)) * (0.85 + 0.15 * Math.sin(t * 2.4))).toFixed(3);
      $("shad1").style.opacity = eo(seg(t, 0.6, 0.9)).toFixed(3);
      // rail
      for (let i = 0; i < 6; i++) { const p = $("p" + i), a = eo(seg(t, 0.62 + i * 0.05, 0.92 + i * 0.05)); p.style.opacity = a.toFixed(3); p.style.transform = `translateY(${((1 - a) * 18).toFixed(1)}px)`; }
      // tiles: 3D flip-in, icon pop, calls count-up, then a highlight walks through them
      T.forEach((o, i) => {
        const t0 = 0.85 + i * 0.085, f = eo4(seg(t, t0, t0 + 0.6));
        o.t.style.transform = `rotateX(${((1 - f) * -72).toFixed(2)}deg) translateY(${((1 - f) * 50).toFixed(1)}px)`;
        o.t.style.opacity = seg(t, t0, t0 + 0.2).toFixed(3);
        const ip = back(seg(t, t0 + 0.15, t0 + 0.55), 2.4);
        o.ic.style.transform = `scale(${(0.3 + 0.7 * ip).toFixed(3)}) rotate(${((1 - ip) * -20).toFixed(1)}deg)`;
        if (o.c) {
          const target = parseInt(items[i][4], 10), cu = eo(seg(t, t0 + 0.35, t0 + 1.1));
          o.c.textContent = Math.round(target * cu) + " CALLS";
        }
        const h0 = 2.7 + i * 0.3, hl = Math.max(0, Math.sin(Math.PI * seg(t, h0, h0 + 0.55)));
        o.g.style.opacity = hl.toFixed(3);
        o.w.style.transform = `translateY(${(-6 * hl).toFixed(2)}px)`;
      });
    };
  }
  window.HFD = { build };
})();

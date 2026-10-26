/* =====================================================================================
 * SMART MOTION DIRECTOR — effect library (AI PRENEUR house style)          window.MD
 * -------------------------------------------------------------------------------------
 * Deterministic GSAP effects for HyperFrames compositions. Every effect:
 *   MD.fx.<name>(ctx, opts)   ctx = { tl, root }   (root = composition #root element)
 * Common opts (all optional):
 *   at        start time (composition-local seconds)
 *   dur       main duration (scaled by preset.time)
 *   preset    "SUBTLE" | "STANDARD" | "HIGH"  (intensity + timing feel)
 *   intensity extra multiplier on amplitudes (scale deltas, angles, blur)
 *   ease      GSAP ease for the main move
 *   dir       "L" | "R" | "U" | "D" (where it comes from / goes to)
 *   theme     { ink, glass, accent }   (defaults: AI PRENEUR navy / ice glass / electric blue)
 *   sfx       cue name (pop | click | whoosh | sparkle) -> recorded in MD.cues; the root adds the audio
 * Rules baked in: no Math.random / Date / rAF; initial states with gsap.set; tweens are
 * fromTo + immediateRender:false so any seek order gives the same frame; filters never use
 * overshooting eases (a negative blur is invalid CSS).
 * ===================================================================================== */
(function () {
  const PRESETS = {
    SUBTLE: { amp: 0.55, time: 1.2, blur: 0.6 },
    STANDARD: { amp: 1.0, time: 1.0, blur: 1.0 },
    HIGH: { amp: 1.5, time: 0.85, blur: 1.3 },
  };
  const THEME = { ink: "#0a0d2c", ink2: "#294b77", glass: "rgba(236,243,252,0.62)", accent: "#3d7cff", ice: "#f7faff" };
  const cues = [];
  const P = (o) => {
    const p = PRESETS[(o && o.preset) || "STANDARD"] || PRESETS.STANDARD;
    const k = (o && o.intensity) || 1;
    return { amp: p.amp * k, time: p.time, blur: p.blur * k };
  };
  const r3 = (x) => Math.round(x * 1000) / 1000;
  let uid = 0;
  const id = (p) => (p || "md") + "-" + ++uid;
  function el(root, tag, attrs, html) {
    const e = document.createElement(tag);
    for (const k in attrs || {}) e.setAttribute(k, attrs[k]);
    if (html != null) e.innerHTML = html;
    root.appendChild(e);
    return e;
  }
  const css = (o) => Object.entries(o).map(([k, v]) => k + ":" + v).join(";");
  function cue(o, t) { if (o && o.sfx) cues.push({ cue: o.sfx, t: r3(t) }); }

  // ---------------------------------------------------------------- shared building blocks
  // Liquid-glass panel: translucent body, inner rim, top specular, slow moving highlight.
  function glassPanel(root, o) {
    const T = Object.assign({}, THEME, o.theme || {});
    const g = el(root, "div", { id: o.id || id("glass"), class: "md-glass", "data-layout-ignore": "" });
    g.style.cssText = css({
      position: "absolute", left: o.x + "px", top: o.y + "px", width: o.w + "px", height: o.h + "px",
      "border-radius": (o.r || 40) + "px", overflow: "hidden",
      background: `linear-gradient(160deg, rgba(255,255,255,.78) 0%, ${T.glass} 46%, rgba(205,222,245,.55) 100%)`,
      "box-shadow": `0 34px 70px rgba(10,13,44,.22), 0 8px 18px rgba(10,13,44,.10), inset 0 1.5px 0 rgba(255,255,255,.95), inset 0 -10px 24px rgba(41,75,119,.10), inset 0 0 0 1.5px rgba(255,255,255,.65)`,
      "transform-origin": "50% 50%",
    });
    el(g, "div", { class: "md-glass-spec" }).style.cssText = css({
      position: "absolute", left: "-10%", top: "-40%", width: "120%", height: "70%",
      background: "radial-gradient(ellipse at 50% 100%, rgba(255,255,255,.55), rgba(255,255,255,0) 62%)", opacity: 0.9,
    });
    const band = el(g, "div", { class: "md-glass-band" });
    band.style.cssText = css({ position: "absolute", top: "-30%", left: "-60%", width: "38%", height: "160%", background: "linear-gradient(100deg, rgba(255,255,255,0), rgba(255,255,255,.42), rgba(255,255,255,0))", transform: "rotate(18deg)" });
    const body = el(g, "div", { class: "md-glass-body" });
    body.style.cssText = css({ position: "absolute", inset: "0" });
    if (o.html) body.innerHTML = o.html;
    return { g, band, body };
  }
  function enter3d(tl, target, at, o, from) {
    const p = P(o), d = (o.dur || 0.7) * p.time;
    const f = Object.assign({ opacity: 0, rotationY: (o.dir === "R" ? 70 : -70) * Math.min(1.2, p.amp), rotationX: 16, scale: 0.74, y: 40 }, from || {});
    gsap.set(target, Object.assign({ transformPerspective: 1100 }, f));
    tl.fromTo(target, f, { opacity: 1, rotationY: o.restY || 0, rotationX: o.restX || 0, scale: 1, y: 0, transformPerspective: 1100, duration: d, ease: o.ease || "expo.out", immediateRender: false }, at);
    gsap.set(target, { filter: `blur(${14 * p.blur}px)` });
    tl.fromTo(target, { filter: `blur(${14 * p.blur}px)` }, { filter: "blur(0px)", duration: d * 0.7, ease: "power2.out", immediateRender: false }, at);
    return d;
  }
  function exitBlur(tl, target, at, o) {
    const p = P(o), d = (o.outDur || 0.3) * p.time;
    const dx = o.dir === "L" ? -700 : o.dir === "U" ? 0 : 700, dy = o.dir === "U" ? -500 : 0;
    tl.fromTo(target, { opacity: 1, x: 0, y: 0 }, { opacity: 0, x: dx * p.amp, y: dy, duration: d, ease: "power3.in", immediateRender: false }, at);
    tl.fromTo(target, { filter: "blur(0px)" }, { filter: `blur(${18 * p.blur}px)`, duration: d, ease: "power2.in", immediateRender: false }, at);
  }
  function sparkle(root, tl, x, y, at, o) {
    const p = P(o), n = 6, ring = el(root, "div", { class: "md-ring", "data-layout-ignore": "" });
    ring.style.cssText = css({ position: "absolute", left: x - 90 + "px", top: y - 90 + "px", width: "180px", height: "180px", "border-radius": "50%", border: "5px solid rgba(255,255,255,.95)", "box-shadow": "0 0 26px rgba(61,124,255,.7)" });
    gsap.set(ring, { opacity: 0, scale: 0.3 });
    tl.fromTo(ring, { opacity: 0.95, scale: 0.3 }, { opacity: 0, scale: 1.9 * p.amp, duration: 0.5, ease: "power3.out", immediateRender: false }, at);
    for (let k = 0; k < n; k++) {
      const s = el(root, "div", { class: "md-spk", "data-layout-ignore": "" });
      s.style.cssText = css({ position: "absolute", left: x - 15 + "px", top: y - 15 + "px", width: "30px", height: "30px", background: "#fff", "clip-path": "polygon(50% 0,61% 39%,100% 50%,61% 61%,50% 100%,39% 61%,0 50%,39% 39%)", filter: "drop-shadow(0 0 7px rgba(61,124,255,.95))" });
      const a = (k / n) * Math.PI * 2 + 0.4, r = (k % 2 ? 95 : 140) * p.amp;
      gsap.set(s, { opacity: 0, scale: 0 });
      tl.fromTo(s, { x: 0, y: 0, scale: 0.2, opacity: 1, rotation: 0 }, { x: Math.cos(a) * r, y: Math.sin(a) * r, scale: k % 2 ? 0.7 : 1.1, opacity: 0, rotation: 90, duration: 0.55, ease: "power2.out", immediateRender: false }, at + 0.02);
    }
  }

  // ================================================================== THE 20 EFFECTS
  const fx = {};

  // 1. Liquid Glass — translucent card, restrained highlight drift, 3D hinge entrance.
  fx.liquidGlass = function (ctx, o) {
    const { g, band, body } = glassPanel(ctx.root, o);
    const d = enter3d(ctx.tl, g, o.at, o);
    gsap.set(band, { xPercent: 0 });
    ctx.tl.fromTo(band, { xPercent: 0 }, { xPercent: 520, duration: 1.1, ease: "power2.inOut", immediateRender: false }, o.at + d * 0.35);
    if (o.until) exitBlur(ctx.tl, g, o.until, o);
    cue(o, o.at);
    return { el: g, body, ready: o.at + d };
  };

  // 2. Frame Escape — an element sits inside a framed card, then lifts out past the border.
  //    Two synced copies (clipped inside / free outside) swap on one frame -> seamless.
  fx.frameEscape = function (ctx, o) {
    const p = P(o), fr = o.frame; // {x,y,w,h,r}
    const frame = el(ctx.root, "div", { id: id("frame"), "data-layout-ignore": "" });
    frame.style.cssText = css({ position: "absolute", left: fr.x + "px", top: fr.y + "px", width: fr.w + "px", height: fr.h + "px", "border-radius": (fr.r || 36) + "px", overflow: "hidden", background: "linear-gradient(160deg,#ffffff,#e4edf9)", "box-shadow": "inset 0 0 0 3px rgba(255,255,255,.9), 0 24px 50px rgba(10,13,44,.18)" });
    const inner = el(frame, "img", { src: o.src, alt: "" });
    inner.style.cssText = css({ position: "absolute", left: o.x - fr.x + "px", top: o.y - fr.y + "px", width: o.w + "px", height: o.h + "px", "object-fit": "contain" });
    const free = el(ctx.root, "img", { src: o.src, alt: "", "data-layout-ignore": "" });
    free.style.cssText = css({ position: "absolute", left: o.x + "px", top: o.y + "px", width: o.w + "px", height: o.h + "px", "object-fit": "contain", filter: "drop-shadow(0 26px 30px rgba(10,13,44,.35))" });
    gsap.set(free, { opacity: 0 });
    enter3d(ctx.tl, frame, o.at, Object.assign({}, o, { dur: 0.6 }));
    const t = o.escapeAt;
    ctx.tl.set(inner, { opacity: 0 }, t);
    ctx.tl.set(free, { opacity: 1 }, t);
    ctx.tl.fromTo(free, { y: 0, scale: 1, rotation: 0 }, { y: -(o.lift || 160) * p.amp, scale: 1 + 0.25 * p.amp, rotation: (o.dir === "L" ? -6 : 6) * p.amp, duration: 0.55 * p.time, ease: "back.out(1.7)", immediateRender: false }, t);
    sparkle(ctx.root, ctx.tl, o.x + o.w / 2, o.y + o.h * 0.2 - (o.lift || 160) * p.amp, t + 0.25, o);
    if (o.until) { exitBlur(ctx.tl, frame, o.until, o); exitBlur(ctx.tl, free, o.until, o); }
    cue(o, t);
    return { frame, free };
  };

  // 3. Snap Zoom — fast punch-in on a camera wrapper, short hold, eased release.
  fx.snapZoom = function (ctx, o) {
    const p = P(o), s = 1 + (o.amount || 0.12) * p.amp, t = o.at;
    if (o.origin) gsap.set(o.target, { transformOrigin: o.origin });
    ctx.tl.fromTo(o.target, { scale: 1 }, { scale: s, duration: 0.11 * p.time, ease: "expo.out", immediateRender: false }, t);
    ctx.tl.fromTo(o.target, { scale: s }, { scale: 1, duration: (o.release || 0.55) * p.time, ease: "power3.inOut", immediateRender: false }, t + (o.hold || 0.35));
    cue(o, t);
  };

  // 4. Zoom Through Cut — camera accelerates through a foreground object into the next shot.
  fx.zoomThroughCut = function (ctx, o) {
    const p = P(o), d = (o.dur || 0.32) * p.time;
    if (o.origin) gsap.set(o.target, { transformOrigin: o.origin });
    ctx.tl.fromTo(o.target, { scale: 1 }, { scale: 1 + 3.2 * p.amp, duration: d, ease: "power4.in", immediateRender: false }, o.at - d);
    ctx.tl.fromTo(o.target, { filter: "blur(0px)", opacity: 1 }, { filter: `blur(${12 * p.blur}px)`, opacity: 0, duration: d, ease: "power2.in", immediateRender: false }, o.at - d);
    if (o.next) {
      gsap.set(o.next, { scale: 1.6, filter: `blur(${12 * p.blur}px)` });
      ctx.tl.fromTo(o.next, { scale: 1.6, filter: `blur(${12 * p.blur}px)` }, { scale: 1, filter: "blur(0px)", duration: 0.5 * p.time, ease: "expo.out", immediateRender: false }, o.at);
    }
    cue(o, o.at - d * 0.5);
  };

  // 5. Chat Takeover — a glass chat thread; messages arrive on the VO, then the thread expands
  //    into the main visual (it becomes the agent's workspace).
  fx.chatTakeover = function (ctx, o) {
    const p = P(o), T = Object.assign({}, THEME, o.theme || {});
    const { g, body } = glassPanel(ctx.root, o);
    enter3d(ctx.tl, g, o.at, o);
    // header: agent avatar dot + status lines (no text)
    const hdr = el(body, "div", {});
    hdr.style.cssText = css({ position: "absolute", left: "28px", top: "24px", right: "28px", height: "44px" });
    hdr.innerHTML = `<div style="position:absolute;left:0;top:0;width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,${T.ink},${T.ink2});box-shadow:0 4px 10px rgba(10,13,44,.25)"></div>
      <div style="position:absolute;left:60px;top:8px;width:160px;height:10px;border-radius:6px;background:${T.ink2};opacity:.55"></div>
      <div style="position:absolute;left:60px;top:26px;width:96px;height:8px;border-radius:6px;background:${T.ink2};opacity:.25"></div>`;
    let y = 92;
    for (const m of o.messages || []) {
      const mine = m.side !== "L";
      const bw = m.w || (m.type === "video" ? 300 : m.type === "typing" ? 120 : 260), bh = m.h || (m.type === "video" ? 190 : m.type === "typing" ? 56 : 64);
      const b = el(body, "div", { class: "md-bubble" });
      b.style.cssText = css({ position: "absolute", top: y + "px", [mine ? "right" : "left"]: "28px", width: bw + "px", height: bh + "px", "border-radius": mine ? "26px 26px 8px 26px" : "26px 26px 26px 8px",
        background: mine || m.type === "code" ? `linear-gradient(120deg, ${T.ink}, ${T.ink2})` : "rgba(255,255,255,.92)", "box-shadow": "0 10px 22px rgba(10,13,44,.16)", overflow: "hidden", "transform-origin": mine ? "100% 100%" : "0% 100%" });
      if (m.type === "video") b.innerHTML = `<img src="${m.src}" alt="" style="position:absolute;inset:10px;width:calc(100% - 20px);height:calc(100% - 20px);object-fit:contain" />`;
      else if (m.type === "typing") b.innerHTML = [0, 1, 2].map((i) => `<span class="md-dot" style="position:absolute;top:22px;left:${26 + i * 26}px;width:13px;height:13px;border-radius:50%;background:${T.ink2}"></span>`).join("");
      else if (m.type === "code") b.innerHTML = `<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="34" height="34" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 7L3.5 12l5 5M15.5 7l5 5-5 5M13.5 5l-3 14"/></svg></div>`;
      else b.innerHTML = `<div style="position:absolute;left:22px;right:22px;top:20px;height:9px;border-radius:5px;background:${mine ? "rgba(255,255,255,.75)" : T.ink2};opacity:.6"></div><div style="position:absolute;left:22px;width:55%;top:36px;height:8px;border-radius:5px;background:${mine ? "rgba(255,255,255,.5)" : T.ink2};opacity:.35"></div>`;
      gsap.set(b, { opacity: 0, scale: 0.4, y: 30 });
      ctx.tl.fromTo(b, { opacity: 0, scale: 0.4, y: 30 }, { opacity: 1, scale: 1, y: 0, duration: 0.38, ease: "back.out(2)", immediateRender: false }, m.at);
      if (m.type === "typing") b.querySelectorAll(".md-dot").forEach((d, i) => {
        ctx.tl.fromTo(d, { y: 0 }, { y: -8, duration: 0.18, ease: "sine.inOut", yoyo: true, repeat: 5, immediateRender: false }, m.at + 0.2 + i * 0.09);
      });
      if (m.sfx) cues.push({ cue: m.sfx, t: r3(m.at) });
      y += bh + 18;
    }
    // takeover: the thread grows to fill the frame and its content gives way to the main visual
    if (o.takeoverAt != null) {
      const tk = o.takeover; // {x,y,w,h, src}
      const vis = el(g, "img", { src: tk.src, alt: "" });
      vis.style.cssText = css({ position: "absolute", left: "50%", top: "50%", width: tk.imgW || "86%", transform: "translate(-50%,-50%)", "object-fit": "contain" });
      gsap.set(vis, { opacity: 0, scale: 0.6 });
      const t = o.takeoverAt, d = 0.6 * p.time;
      ctx.tl.fromTo(g, { left: o.x, top: o.y, width: o.w, height: o.h }, { left: tk.x, top: tk.y, width: tk.w, height: tk.h, duration: d, ease: "expo.inOut", immediateRender: false }, t);
      ctx.tl.fromTo(body, { opacity: 1, scale: 1 }, { opacity: 0, scale: 0.92, duration: d * 0.5, ease: "power2.in", immediateRender: false }, t);
      ctx.tl.fromTo(vis, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: d, ease: "expo.out", immediateRender: false }, t + d * 0.35);
      cue({ sfx: o.takeoverSfx }, t);
    }
    if (o.until) exitBlur(ctx.tl, g, o.until, o);
    return { el: g };
  };

  // 6. B-Roll Overlay — layered contextual cards with depth parallax (near moves more).
  fx.bRollOverlay = function (ctx, o) {
    const p = P(o);
    (o.items || []).forEach((it, i) => {
      const c = el(ctx.root, "div", { class: "md-broll", "data-layout-ignore": "" });
      c.style.cssText = css({ position: "absolute", left: it.x + "px", top: it.y + "px", width: it.w + "px", height: it.h + "px", "border-radius": "26px", overflow: "hidden", background: "#fff", "box-shadow": `0 ${18 + i * 8}px ${36 + i * 10}px rgba(10,13,44,.${2 + i})` });
      c.innerHTML = `<img src="${it.src}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:${it.fit || "cover"}" />`;
      const depth = it.depth == null ? 1 : it.depth;
      enter3d(ctx.tl, c, it.at, Object.assign({}, o, { dir: it.dir || (i % 2 ? "R" : "L"), restY: (i % 2 ? -8 : 8), restX: 4 }));
      ctx.tl.fromTo(c, { x: 0 }, { x: (o.drift || 40) * depth * p.amp * (i % 2 ? -1 : 1), duration: (o.until || it.at + 3) - it.at, ease: "none", immediateRender: false }, it.at + 0.01);
      if (o.until) exitBlur(ctx.tl, c, o.until + i * 0.05, Object.assign({}, o, { dir: i % 2 ? "R" : "L" }));
      cue(it, it.at);
    });
  };

  // 7. Cinematic Orbit — controlled perspective sweep around an object (parallax children optional).
  fx.cinematicOrbit = function (ctx, o) {
    const p = P(o), a = (o.angle || 14) * p.amp;
    gsap.set(o.target, { transformPerspective: o.perspective || 1400 });
    ctx.tl.fromTo(o.target, { rotationY: -a, rotationX: 4 * p.amp }, { rotationY: a, rotationX: -2 * p.amp, transformPerspective: o.perspective || 1400, duration: o.dur, ease: o.ease || "sine.inOut", immediateRender: false }, o.at);
    (o.parallax || []).forEach((sel, i) => ctx.tl.fromTo(sel, { x: -20 * (i + 1) * p.amp }, { x: 20 * (i + 1) * p.amp, duration: o.dur, ease: "sine.inOut", immediateRender: false }, o.at));
  };

  // 8. Dynamic Headline — VO words only, each in a navy box with white text, snapping in.
  fx.dynamicHeadline = function (ctx, o) {
    const p = P(o), T = Object.assign({}, THEME, o.theme || {});
    const wrap = el(ctx.root, "div", { class: "md-headline", "data-layout-ignore": "" });
    wrap.style.cssText = css({ position: "absolute", left: o.x + "px", top: o.y + "px", width: o.w + "px", "text-align": o.align || "center", "font-family": "Poppins, sans-serif" });
    (o.words || []).forEach((w, i) => {
      const big = w.big ? 1 : 0;
      const s = el(wrap, "span", {});
      s.style.cssText = css({ display: "inline-block", margin: "8px 8px", padding: big ? "8px 26px 14px" : "6px 18px 10px", "border-radius": "16px", background: `linear-gradient(105deg, ${T.ink} 0%, ${T.ink2} 100%)`, color: "#fff", "font-weight": big ? 800 : 700, "font-size": (big ? 96 : 54) + "px", "line-height": 1.1, "box-shadow": "0 14px 30px rgba(10,13,44,.25)", "letter-spacing": "-0.02em" });
      s.textContent = w.text;
      gsap.set(s, { opacity: 0, scale: 1.8, rotation: (i % 2 ? 4 : -4) * p.amp, filter: "blur(10px)" });
      ctx.tl.fromTo(s, { opacity: 0, scale: 1.8, rotation: (i % 2 ? 4 : -4) * p.amp }, { opacity: 1, scale: 1, rotation: 0, duration: 0.3 * p.time, ease: "expo.out", immediateRender: false }, w.at);
      ctx.tl.fromTo(s, { filter: "blur(10px)" }, { filter: "blur(0px)", duration: 0.22, ease: "power2.out", immediateRender: false }, w.at);
    });
    if (o.until) exitBlur(ctx.tl, wrap, o.until, Object.assign({}, o, { dir: "U" }));
    return wrap;
  };

  // 9. Growth Curve — progressive line + area reveal with a travelling marker (no invented numbers).
  fx.growthCurve = function (ctx, o) {
    const p = P(o), T = Object.assign({}, THEME, o.theme || {});
    const { g, body } = glassPanel(ctx.root, o);
    enter3d(ctx.tl, g, o.at, o);
    const W = o.w - 70, H = o.h - 90, pts = o.points || [0.04, 0.06, 0.1, 0.13, 0.2, 0.3, 0.46, 0.66, 0.92];
    const xy = pts.map((v, i) => [35 + (i / (pts.length - 1)) * W, 30 + H - v * H]);
    let d = `M ${xy[0][0]} ${xy[0][1]}`;
    for (let i = 1; i < xy.length; i++) { const [x0, y0] = xy[i - 1], [x1, y1] = xy[i], cx = (x0 + x1) / 2; d += ` C ${cx} ${y0}, ${cx} ${y1}, ${x1} ${y1}`; }
    const area = d + ` L ${xy[xy.length - 1][0]} ${30 + H} L ${xy[0][0]} ${30 + H} Z`;
    const gid = id("gc");
    body.innerHTML = `<svg width="${o.w}" height="${o.h}" style="position:absolute;inset:0">
      <defs><linearGradient id="${gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${T.accent}" stop-opacity=".35"/><stop offset="1" stop-color="${T.accent}" stop-opacity="0"/></linearGradient>
      <clipPath id="${gid}c"><rect id="${gid}r" x="0" y="0" width="0" height="${o.h}"/></clipPath></defs>
      ${[0.25, 0.5, 0.75].map((f) => `<line x1="35" x2="${35 + W}" y1="${30 + H * f}" y2="${30 + H * f}" stroke="${T.ink2}" stroke-opacity=".12" stroke-width="2"/>`).join("")}
      <path d="${area}" fill="url(#${gid})" clip-path="url(#${gid}c)"/>
      <path id="${gid}p" d="${d}" fill="none" stroke="${T.ink2}" stroke-width="7" stroke-linecap="round"/>
      <circle id="${gid}m" r="11" fill="#fff" stroke="${T.accent}" stroke-width="5" cx="${xy[0][0]}" cy="${xy[0][1]}"/></svg>`;
    const path = body.querySelector("#" + gid + "p"), rect = body.querySelector("#" + gid + "r"), mk = body.querySelector("#" + gid + "m");
    const len = 3000;
    gsap.set(path, { strokeDasharray: len, strokeDashoffset: len });
    const t0 = o.at + 0.45, dur = (o.drawDur || 1.2) * p.time;
    ctx.tl.fromTo(path, { strokeDashoffset: len }, { strokeDashoffset: 0, duration: dur, ease: "power2.inOut", immediateRender: false }, t0);
    ctx.tl.fromTo(rect, { attr: { width: 0 } }, { attr: { width: o.w }, duration: dur, ease: "power2.inOut", immediateRender: false }, t0);
    // marker follows the sampled points (piecewise, deterministic)
    const seg = dur / (xy.length - 1);
    for (let i = 1; i < xy.length; i++) ctx.tl.fromTo(mk, { attr: { cx: xy[i - 1][0], cy: xy[i - 1][1] } }, { attr: { cx: xy[i][0], cy: xy[i][1] }, duration: seg, ease: "none", immediateRender: false }, t0 + (i - 1) * seg);
    if (o.icon) {
      const ic = el(body, "img", { src: o.icon, alt: "" });
      ic.style.cssText = css({ position: "absolute", width: "64px", height: "64px", left: xy[xy.length - 1][0] - 32 + "px", top: xy[xy.length - 1][1] - 84 + "px" });
      gsap.set(ic, { opacity: 0, scale: 0 });
      ctx.tl.fromTo(ic, { opacity: 0, scale: 0, rotation: -40 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2.4)", immediateRender: false }, t0 + dur - 0.05);
    }
    if (o.until) exitBlur(ctx.tl, g, o.until, o);
    cue(o, t0 + dur);
    return { el: g };
  };

  // 10. Paper Cutout — tactile paper edge + lift shadow + small hand-placed wobble.
  fx.paperCutout = function (ctx, o) {
    const p = P(o);
    gsap.set(o.target, { filter: "drop-shadow(0 0 0 #fff) drop-shadow(0 6px 3px rgba(10,13,44,.18)) drop-shadow(0 20px 22px rgba(10,13,44,.18))" });
    ctx.tl.fromTo(o.target, { rotation: -10 * p.amp, y: -60 * p.amp, scale: 1.1 }, { rotation: 2 * p.amp, y: 0, scale: 1, duration: 0.42 * p.time, ease: "back.out(2.2)", immediateRender: false }, o.at);
    if (o.wobbleUntil) ctx.tl.fromTo(o.target, { rotation: 2 * p.amp }, { rotation: -1.5 * p.amp, duration: 0.9, ease: "sine.inOut", yoyo: true, repeat: Math.max(0, Math.floor((o.wobbleUntil - o.at - 0.45) / 0.9) - 1), immediateRender: false }, o.at + 0.45);
    cue(o, o.at);
  };

  // 11. Checklist Pop — glass list; each row lands and ticks on its VO word.
  fx.checklistPop = function (ctx, o) {
    const p = P(o), T = Object.assign({}, THEME, o.theme || {});
    const { g, body } = glassPanel(ctx.root, o);
    enter3d(ctx.tl, g, o.at, o);
    const rh = o.rowH || 78;
    (o.items || []).forEach((it, i) => {
      const row = el(body, "div", {});
      row.style.cssText = css({ position: "absolute", left: "26px", right: "26px", top: 30 + i * (rh + 12) + "px", height: rh + "px", "border-radius": "20px", background: "rgba(255,255,255,.88)", "box-shadow": "0 8px 18px rgba(10,13,44,.10)" });
      row.innerHTML = `<div class="md-box" style="position:absolute;left:18px;top:${(rh - 44) / 2}px;width:44px;height:44px;border-radius:13px;border:3px solid ${T.ink2};background:#fff"></div>
        <svg class="md-tick" viewBox="0 0 24 24" style="position:absolute;left:22px;top:${(rh - 36) / 2}px;width:36px;height:36px"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="30" stroke-dashoffset="30"/></svg>
        <span style="position:absolute;left:84px;top:${(rh - 54) / 2}px;font:700 38px/54px Poppins,sans-serif;color:${T.ink};letter-spacing:-0.01em">${it.label}</span>`;
      const box = row.querySelector(".md-box"), tick = row.querySelector(".md-tick path");
      gsap.set(row, { opacity: 0, x: 60, scale: 0.9 });
      ctx.tl.fromTo(row, { opacity: 0, x: 60, scale: 0.9 }, { opacity: 1, x: 0, scale: 1, duration: 0.32, ease: "back.out(1.8)", immediateRender: false }, it.at - 0.12);
      ctx.tl.fromTo(box, { background: "#ffffff", scale: 1 }, { background: T.ink2, scale: 1.15, duration: 0.12, ease: "power2.out", immediateRender: false }, it.at);
      ctx.tl.fromTo(box, { scale: 1.15 }, { scale: 1, duration: 0.2, ease: "back.out(2)", immediateRender: false }, it.at + 0.12);
      ctx.tl.fromTo(tick, { attr: { "stroke-dashoffset": 30 } }, { attr: { "stroke-dashoffset": 0 }, duration: 0.2, ease: "power2.out", immediateRender: false }, it.at + 0.04);
      if (it.sfx) cues.push({ cue: it.sfx, t: r3(it.at) });
    });
    if (o.until) exitBlur(ctx.tl, g, o.until, o);
    return { el: g };
  };

  // 12. Studio Reveal — light sweeps across the set while the camera settles in.
  fx.studioReveal = function (ctx, o) {
    const p = P(o);
    const L = el(ctx.root, "div", { class: "md-studio", "data-layout-ignore": "" });
    L.style.cssText = css({ position: "absolute", inset: "0", "pointer-events": "none", overflow: "hidden" });
    L.innerHTML = `<div class="md-cone" style="position:absolute;left:-60%;top:-20%;width:70%;height:140%;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,.55),rgba(255,255,255,0));transform:rotate(14deg)"></div>
      <div class="md-shade" style="position:absolute;inset:0;background:radial-gradient(ellipse 70% 55% at 50% 55%, rgba(10,13,44,0) 40%, rgba(10,13,44,.55) 100%)"></div>`;
    const cone = L.querySelector(".md-cone"), shade = L.querySelector(".md-shade");
    gsap.set(shade, { opacity: 1 });
    ctx.tl.fromTo(shade, { opacity: 1 }, { opacity: 0, duration: (o.dur || 1.0) * p.time, ease: "power2.out", immediateRender: false }, o.at);
    ctx.tl.fromTo(cone, { xPercent: 0 }, { xPercent: 330, duration: (o.dur || 1.0) * 1.1 * p.time, ease: "power2.inOut", immediateRender: false }, o.at + 0.05);
    if (o.target) ctx.tl.fromTo(o.target, { scale: 1 + 0.12 * p.amp }, { scale: 1, duration: (o.dur || 1.0) * 1.2 * p.time, ease: "expo.out", immediateRender: false }, o.at);
    cue(o, o.at);
  };

  // 13. Zoom Portal — a circular window opens on a point and the next shot arrives through it.
  fx.zoomPortal = function (ctx, o) {
    const p = P(o), d = (o.dur || 0.55) * p.time;
    gsap.set(o.next, { clipPath: `circle(0px at ${o.x}px ${o.y}px)` });
    ctx.tl.fromTo(o.next, { clipPath: `circle(0px at ${o.x}px ${o.y}px)` }, { clipPath: `circle(1500px at ${o.x}px ${o.y}px)`, duration: d, ease: "power3.in", immediateRender: false }, o.at - d * 0.5);
    const ring = el(ctx.root, "div", { "data-layout-ignore": "" });
    ring.style.cssText = css({ position: "absolute", left: o.x - 60 + "px", top: o.y - 60 + "px", width: "120px", height: "120px", "border-radius": "50%", border: "8px solid rgba(255,255,255,.95)", "box-shadow": "0 0 40px rgba(61,124,255,.8), inset 0 0 30px rgba(61,124,255,.6)" });
    gsap.set(ring, { opacity: 0, scale: 0.2 });
    ctx.tl.fromTo(ring, { opacity: 1, scale: 0.2 }, { opacity: 0, scale: 14, duration: d, ease: "power3.in", immediateRender: false }, o.at - d * 0.5);
    cue(o, o.at - d * 0.5);
  };

  // 14. Magazine Cover — editorial frame: big image, masthead word (VO), rules and folio marks.
  fx.magazineCover = function (ctx, o) {
    const p = P(o), T = Object.assign({}, THEME, o.theme || {});
    const c = el(ctx.root, "div", { class: "md-cover", "data-layout-ignore": "" });
    c.style.cssText = css({ position: "absolute", left: o.x + "px", top: o.y + "px", width: o.w + "px", height: o.h + "px", background: "#fbfdff", "border-radius": "10px", overflow: "hidden", "box-shadow": "0 40px 80px rgba(10,13,44,.28)" });
    c.innerHTML = `<img src="${o.src}" alt="" style="position:absolute;left:6%;top:22%;width:88%;height:66%;object-fit:cover;border-radius:6px" />
      <div style="position:absolute;left:6%;right:6%;top:5%;font:800 ${o.mastSize || 92}px/1 Poppins,sans-serif;letter-spacing:-0.04em;color:${T.ink}">${o.title || ""}</div>
      <div style="position:absolute;left:6%;right:6%;top:18.5%;height:3px;background:${T.ink}"></div>
      <div style="position:absolute;left:6%;width:30%;bottom:5%;height:8px;border-radius:4px;background:${T.ink2};opacity:.5"></div>
      <div style="position:absolute;right:6%;width:14%;bottom:5%;height:8px;border-radius:4px;background:${T.ink2};opacity:.3"></div>`;
    enter3d(ctx.tl, c, o.at, Object.assign({}, o, { restY: o.dir === "R" ? -10 : 10, restX: 5 }));
    if (o.until) exitBlur(ctx.tl, c, o.until, o);
    cue(o, o.at);
    return c;
  };

  // 15. Dolly Zoom — background scale changes while the subject keeps its size (use rarely).
  fx.dollyZoom = function (ctx, o) {
    const p = P(o);
    ctx.tl.fromTo(o.background, { scale: 1 + 0.3 * p.amp }, { scale: 1, duration: o.dur || 0.9, ease: "power2.inOut", immediateRender: false }, o.at);
    if (o.subject) ctx.tl.fromTo(o.subject, { scale: 1 }, { scale: 1.02, duration: o.dur || 0.9, ease: "power2.inOut", immediateRender: false }, o.at);
    cue(o, o.at);
  };

  // 16. Phone Mockup — CSS device with real screen content, glass reflection, 3D tilt-in.
  fx.phoneMockup = function (ctx, o) {
    const ph = el(ctx.root, "div", { class: "md-phone", "data-layout-ignore": "" });
    ph.style.cssText = css({ position: "absolute", left: o.x + "px", top: o.y + "px", width: o.w + "px", height: o.h + "px", "border-radius": o.w * 0.16 + "px", background: "linear-gradient(145deg,#1b2340,#0a0d2c)", "box-shadow": "0 40px 70px rgba(10,13,44,.35), inset 0 0 0 3px #3b4a72" });
    ph.innerHTML = `<div style="position:absolute;inset:${o.w * 0.045}px;border-radius:${o.w * 0.12}px;overflow:hidden;background:#eef3fb">
        <img src="${o.src}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:${o.fit || "cover"}" /></div>
      <div style="position:absolute;left:50%;top:${o.w * 0.07}px;width:${o.w * 0.28}px;height:${o.w * 0.07}px;margin-left:-${o.w * 0.14}px;border-radius:999px;background:#0a0d2c"></div>
      <div style="position:absolute;inset:0;border-radius:inherit;background:linear-gradient(115deg,rgba(255,255,255,.22) 0%,rgba(255,255,255,0) 38%)"></div>`;
    enter3d(ctx.tl, ph, o.at, Object.assign({}, o, { restY: o.dir === "R" ? -14 : 14, restX: 6 }));
    if (o.until) exitBlur(ctx.tl, ph, o.until, o);
    cue(o, o.at);
    return ph;
  };

  // 17. Frame Break — a framed card's border shatters as the subject pushes through it.
  fx.frameBreak = function (ctx, o) {
    const p = P(o), fr = o.frame;
    const f = el(ctx.root, "div", { "data-layout-ignore": "" });
    f.style.cssText = css({ position: "absolute", left: fr.x + "px", top: fr.y + "px", width: fr.w + "px", height: fr.h + "px", "border-radius": "34px", border: "6px solid rgba(255,255,255,.95)", "box-shadow": "0 0 0 2px rgba(41,75,119,.25), 0 20px 50px rgba(10,13,44,.18)" });
    enter3d(ctx.tl, f, o.at, Object.assign({}, o, { dur: 0.5 }));
    const t = o.breakAt, n = 7;
    for (let k = 0; k < n; k++) {
      const s = el(ctx.root, "div", { "data-layout-ignore": "" });
      const sx = fr.x + fr.w * (0.25 + 0.5 * (k / (n - 1))), sy = fr.y;
      s.style.cssText = css({ position: "absolute", left: sx + "px", top: sy - 6 + "px", width: 18 + (k % 3) * 10 + "px", height: "8px", background: "rgba(255,255,255,.95)", "border-radius": "2px", "box-shadow": "0 0 10px rgba(61,124,255,.6)" });
      gsap.set(s, { opacity: 0 });
      ctx.tl.fromTo(s, { opacity: 1, x: 0, y: 0, rotation: 0 }, { opacity: 0, x: (k - n / 2) * 30 * p.amp, y: -(120 + (k % 3) * 60) * p.amp, rotation: (k % 2 ? 1 : -1) * 200, duration: 0.7, ease: "power2.out", immediateRender: false }, t);
    }
    // the top edge gets a gap where the subject breaks through
    const gap = el(ctx.root, "div", { "data-layout-ignore": "" });
    gap.style.cssText = css({ position: "absolute", left: fr.x + fr.w * 0.25 + "px", top: fr.y - 8 + "px", width: fr.w * 0.5 + "px", height: "14px", background: o.gapColor || "#eef3fb" });
    gsap.set(gap, { opacity: 0 });
    ctx.tl.set(gap, { opacity: 1 }, t);
    if (o.until) { exitBlur(ctx.tl, f, o.until, o); ctx.tl.set(gap, { opacity: 0 }, o.until + 0.3); }
    cue(o, t);
    return f;
  };

  // 18. Digital Zoom — restrained editorial reframe (slow scale + offset).
  fx.digitalZoom = function (ctx, o) {
    const p = P(o);
    ctx.tl.fromTo(o.target, { scale: 1, x: 0, y: 0 }, { scale: 1 + (o.amount || 0.1) * p.amp, x: (o.dx || 0) * p.amp, y: (o.dy || 0) * p.amp, duration: o.dur || 1.2, ease: o.ease || "power2.inOut", immediateRender: false }, o.at);
    if (o.releaseAt) ctx.tl.fromTo(o.target, { scale: 1 + (o.amount || 0.1) * p.amp, x: (o.dx || 0) * p.amp, y: (o.dy || 0) * p.amp }, { scale: 1, x: 0, y: 0, duration: 0.6, ease: "power2.inOut", immediateRender: false }, o.releaseAt);
  };

  // 19. Green Screen Compositing — integrate a cut-out layer (mascot / footage) into the plate:
  //     contact shadow, cool light wrap from the set, and a tiny colour match.
  fx.greenScreen = function (ctx, o) {
    const s = o.strength == null ? 1 : o.strength;
    gsap.set(o.target, { filter: `drop-shadow(0 0 ${2 * s}px rgba(220,232,246,.9)) drop-shadow(0 ${16 * s}px ${26 * s}px rgba(10,13,44,${0.22 * s})) saturate(${1 - 0.04 * s})` });
  };

  // 20. Orbit Reveal — an object turns into view (half orbit), catches a glint, settles.
  fx.orbitReveal = function (ctx, o) {
    const p = P(o), d = (o.dur || 0.9) * p.time;
    gsap.set(o.target, { opacity: 0, rotationY: -160, scale: 0.55, transformPerspective: 1000 });
    ctx.tl.fromTo(o.target, { opacity: 0, rotationY: -160, scale: 0.55 }, { opacity: 1, rotationY: o.restY || 12, scale: 1, transformPerspective: 1000, duration: d, ease: "expo.out", immediateRender: false }, o.at);
    if (o.glint) {
      gsap.set(o.glint, { xPercent: -120, opacity: 0.0 });
      ctx.tl.fromTo(o.glint, { xPercent: -120, opacity: 0.9 }, { xPercent: 220, opacity: 0.9, duration: 0.6, ease: "power2.inOut", immediateRender: false }, o.at + d * 0.55);
    }
    if (o.until) exitBlur(ctx.tl, o.target, o.until, o);
    cue(o, o.at);
  };

  window.MD = { fx, PRESETS, THEME, cues, glassPanel, sparkle, enter3d, exitBlur };
})();

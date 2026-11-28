/* R38 host (batch 10 staging, client rule 2026-11-28): the client's 3D chibi mascot comes FORWARD, half-body (waist-up, cropped by the
   frame bottom on purpose), on the explaining beats (hook, "Caranya gini", "masih beta", privacy + CTA) and is FULLY hidden on every
   example / demo beat. The move is a closed-form spring from the small bottom-left corner pose to the big half-body pose (push-in +
   rise, never a pop); the exit shrinks it back toward the corner and drops it out of frame before the example lands. Live WebGL,
   lip sync from the VO phones (R-series runtime). The explain windows come from vendor/r38.js (window.R38_STAGE). */
(function () {
  const M3 = window.Mascot3D;
  const { buildPerformance, buildLipTrack, syllableAccents, vnoise, bump } = M3;
  const VW = window.VO_WORDS, D = window.TOTAL;
  const canvas = document.getElementById("ms");
  const mouthAt = buildLipTrack(window.VO_PHONES, window.VO_ENV, D, { smooth: 1 });
  const ACC = syllableAccents(window.VO_ENV, VW, window.VO_PHONES, D);
  const one = (x) => Math.max(0, Math.min(1, x));
  const lin = (t, a, b) => one((t - a) / (b - a));
  const eio = (t, a, b) => { const u = lin(t, a, b); return u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2; };
  const spr = (t, t0, w = 13, z = 0.78) => { const u = t - t0; if (u <= 0) return 0; const wd = w * Math.sqrt(1 - z * z); return 1 - Math.exp(-z * w * u) * (Math.cos(wd * u) + (z * w / wd) * Math.sin(wd * u)); };
  const L = (a, b, u) => a + (b - a) * u;
  const add = (...ds) => { const o = {}; for (const d of ds) for (const [k, v] of Object.entries(d || {})) { const a = o[k] || [0, 0, 0]; o[k] = [a[0] + v[0], a[1] + v[1], a[2] + v[2]]; } return o; };
  function accents(t) { let n = 0; for (const a of ACC) { const d = t - a[0]; if (d > -0.25 && d < 0.35) n += bump(t, a[0] + 0.05, 0.17) * a[1]; } return Math.min(1.3, n); }
  // ---------------------------------------------------------------- framing (canvas = full frame 1080x1920)
  const BIG = (() => { const q = new URLSearchParams(location.search); return { fx: 540, fy: +(q.get("fy") || 2230), h: +(q.get("h") || 1600) }; })();   // half body: waist at the frame bottom
  const SMALL = { fx: 190, fy: 1760, h: 430 };    // the corner pose it grows from / shrinks back to
  const STAGE = window.R38_STAGE;                 // [[tIn, tOut, fxBig], ...] (tOut = 1e9 for the last window)
  function pose(t) {
    for (const [a, b, fxb] of STAGE) {
      if (t < a - 0.02 || t > b + 0.45) continue;
      const u = spr(t, a, 12, 0.8), v = eio(t, b, b + 0.32);
      const big = { fx: fxb || BIG.fx, fy: BIG.fy, h: BIG.h };
      let fx = L(SMALL.fx, big.fx, u), fy = L(SMALL.fy, big.fy, u), h = L(SMALL.h, big.h, u);
      // exit: shrink toward the corner and sink out of frame
      fx = L(fx, SMALL.fx - 40, v); fy = L(fy, SMALL.fy + 700, v); h = L(h, SMALL.h * 0.9, v);
      const o = Math.min(1, u * 5) * (1 - lin(v, 0.55, 0.95));
      return { o, fx, fy, h, yaw: 6 * (1 - u) - 10 * v, u, v };
    }
    return null;
  }
  // ---------------------------------------------------------------- acting (only matters while shown)
  const intents = [];
  const ACTS = ["present", "explain", "emphasize", "point"];
  STAGE.forEach(([a, b], k) => {
    intents.push({ t: a + 0.05, action: k === 0 ? "present" : "reveal", side: k % 2 ? "left" : "right" });
    let n = 0;
    for (const w of VW) if (w[1] > a + 0.5 && w[1] < Math.min(b, D) - 0.3 && w[3]) { intents.push({ t: w[1] - 0.08, action: ACTS[(k + n) % ACTS.length], side: n % 2 ? "left" : "right" }); n++; }
  });
  const komen = VW.find((w) => w[0] === "Komen"); if (komen) intents.push({ t: komen[1] - 0.1, action: "cta", side: "right" });
  intents.push({ t: D - 0.5, action: "idle" });
  intents.sort((p, q) => p.t - q.t);
  const DIR = M3.direct(VW, D, { intents, seed: 38, quiet: 0.3, look: 0 });
  const PERF = buildPerformance(DIR.tracks, D + 0.05, { smooth: 1 });
  const FACE = window.MASCOT_FACE, DECALS = window.MASCOT_DECALS;
  let mascot = null;
  function apply(t) {
    const p = pose(t);
    if (!p || p.o <= 0.002) { canvas.style.visibility = "hidden"; return; }
    canvas.style.visibility = "visible"; canvas.style.opacity = p.o.toFixed(3);
    // a light motion blur on the fast part of the exit (CSS blur on the canvas)
    canvas.style.filter = (p.v > 0.05 && p.v < 0.9) ? `blur(${(3 * Math.sin(Math.PI * p.v)).toFixed(2)}px)` : "none";
    const id = M3.micro(t, 17, vnoise), Pf = PERF(t), acc = accents(t);
    const bones = add(Pf.bones, id, { head: [0.03 * acc, 0, 0], neck: [0.012 * acc, 0, 0] });
    const root = { x: Pf.root.x, y: Pf.root.y, ry: Pf.root.ry + 0.012 * vnoise(t, 26, 0.18), rz: Pf.root.rz, rx: 0, s: Pf.root.s };
    const bl = M3.blink(t, 0, D, 3, DIR.blinks);
    const gz = DIR.gaze(t);
    if (mascot.shadow) mascot.shadow.visible = false;
    mascot.setView({ fx: p.fx, fy: p.fy, h: p.h, pitch: 4, yaw: p.yaw });
    mascot.setState({ root, bones, face: { blink: [bl, bl], gaze: [gz[0], gz[1]], mouthMix: 1, mouth: mouthAt(t), brow: [0, 0] } });
    mascot.render();
  }
  window.__hf = window.__hf || {};
  window.__hf.buildReady = window.__hf.buildReady || {};
  const ready = M3.Mascot.create(canvas, { url: "assets/mascot3d/mascot_biz_rigged.glb", face: FACE, decals: DECALS, width: 1080, height: 1920, envIntensity: 0.6 })
    .then((m) => {
      mascot = m;
      for (const o of m.scene.children) if (o.isDirectionalLight && o.position.z < 0) { o.intensity = 1.6; o.color.setRGB(0.72, 0.84, 1.0); o.position.set(1.6, 1.5, -1.4); }
      apply(0);
    });
  window.__hf.buildReady["mascot"] = ready;
  window.R38_hostPose = pose;
  window.addEventListener("hf-seek", (e) => {
    const t = e.detail.time;
    if (mascot) apply(t);
    else if (e.detail.waitUntil) e.detail.waitUntil(ready.then(() => apply(t)));
  });
})();

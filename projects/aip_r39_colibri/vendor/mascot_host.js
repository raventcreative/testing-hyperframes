/* R39 · the client's 3D chibi mascot with the batch-10 staging (client 2026-11-28):
   - explaining beats (window.STAGE windows from vendor/r39.js): the mascot comes FORWARD, half-body (waist-up, cropped by the
     frame bottom on purpose), lip-synced, under the spoken headline. Entry = rises small in the bottom-left corner, then a spring
     push-in to the half-body pose (log-space size, no pop). Exit = the reverse (shrinks back to the corner and drops out).
   - example / demo beats: fully hidden (canvas opacity 0 + not rendered).
   Glances disabled (they made the eyes read blank in earlier renders). Live WebGL, lip sync from the VO phones. */
(function () {
  const M3 = window.Mascot3D;
  const { buildPerformance, buildLipTrack, syllableAccents, vnoise, bump } = M3;
  const VW = window.VO_WORDS, D = window.TOTAL, STAGE = window.STAGE || [];
  const canvas = document.getElementById("ms");
  const mouthAt = buildLipTrack(window.VO_PHONES, window.VO_ENV, D, { smooth: 1 });
  const ACC = syllableAccents(window.VO_ENV, VW, window.VO_PHONES, D);
  const one = (x) => Math.max(0, Math.min(1, x));
  const e3 = (u) => { u = one(u); return 1 - Math.pow(1 - u, 3); };
  const ei3 = (u) => { u = one(u); return u * u * u; };
  const L = (a, b, u) => a + (b - a) * u;
  const spr = (u, f = 1.9, z = 0.7) => { if (u <= 0) return 0; const w = 2 * Math.PI * f, wd = w * Math.sqrt(1 - z * z); return 1 - Math.exp(-z * w * u) * (Math.cos(wd * u) + (z * w / wd) * Math.sin(wd * u)); };
  const add = (...ds) => { const o = {}; for (const d of ds) for (const [k, v] of Object.entries(d || {})) { const a = o[k] || [0, 0, 0]; o[k] = [a[0] + v[0], a[1] + v[1], a[2] + v[2]]; } return o; };
  function accents(t) { let n = 0; for (const a of ACC) { const d = t - a[0]; if (d > -0.25 && d < 0.35) n += bump(t, a[0] + 0.05, 0.17) * a[1]; } return Math.min(1.3, n); }
  // ---------------------------------------------------------------- framing (canvas 1080 x 1240 at y 680 of the frame)
  const CW = window.MS_W, CH = window.MS_H;
  const SMALL = { fx: 190, fy: CH - 16, h: 440 };                                   // whole body, bottom-left corner
  const HALF = (w) => ({ fx: w.fx || 540, fy: (w.head || 150) + (w.h || 1380), h: w.h || 1380 });   // waist-up: head top at w.head (canvas px)
  // stage(t): k = 0 hidden … 1 half-body; returns the view + canvas opacity + speed (for the motion blur)
  function pose(t) {
    for (const w of STAGE) {
      if (t < w.a - 0.02 || t > w.b + 0.62) continue;
      const H = HALF(w);
      // in: 0..0.22 s rise in the corner (small), then spring push-in to half-body
      const rise = e3((t - w.a) / 0.22), push = spr(t - w.a - 0.16, 1.55, 0.74);
      // out: shrink back to the corner (0.3 s), then drop out (0.22 s)
      const back = t > w.b ? e3((t - w.b) / 0.26) : 0, drop = t > w.b + 0.2 ? ei3((t - w.b - 0.2) / 0.2) : 0;
      const k = one(push) * (1 - back) + (push > 1 ? (push - 1) * (1 - back) : 0);
      const lh = Math.log(SMALL.h) + (Math.log(H.h) - Math.log(SMALL.h)) * k;
      const v = { fx: L(SMALL.fx, H.fx, Math.min(1.05, k)), fy: L(SMALL.fy, H.fy, k), h: Math.exp(lh), pitch: 6, yaw: 0 };
      v.fy += (1 - rise) * (SMALL.h + 60) + drop * (SMALL.h + 80);
      return { v, o: one(rise * 4) * (1 - one(drop * 1.4)), w };
    }
    return null;
  }
  // ---------------------------------------------------------------- acting: one gesture per explaining beat, CTA at "Komen"
  const ACTS = [["welcome", null], ["explain", "right"], ["explain", "right"], ["emphasize", "right"], ["point", "left"]];
  const intents = [];
  STAGE.forEach((w, i) => { const a = ACTS[i % ACTS.length]; const it = { t: w.a + 0.2, action: a[0] }; if (a[1]) it.side = a[1]; intents.push(it);
    (w.acts || []).forEach((x) => intents.push(x)); });
  intents.push({ t: D - 0.5, action: "idle" });
  intents.sort((p, q) => p.t - q.t);
  const DIR = M3.direct(VW, D, { intents, seed: 39, quiet: 0.3, look: 0 });
  const PERF = buildPerformance(DIR.tracks, D + 0.05, { smooth: 1 });
  const FACE = window.MASCOT_FACE, DECALS = window.MASCOT_DECALS;
  let mascot = null;
  function apply(t) {
    const P = pose(t);
    if (!P || P.o <= 0.001) { canvas.style.opacity = "0"; canvas.style.filter = "none"; mascot.setState({ visible: false }); mascot.render(); return; }
    const P0 = pose(t - 1 / 30); const sp = P0 ? Math.abs(Math.log(P.v.h) - Math.log(P0.v.h)) * 900 + Math.hypot(P.v.fx - P0.v.fx, P.v.fy - P0.v.fy) * 0.5 : 0;
    const bl = sp > 10 ? Math.min(8, (sp - 10) * 0.08) : 0;     // motion blur proportional to speed on the fast push/exit
    canvas.style.opacity = P.o.toFixed(3); canvas.style.filter = bl > 0.25 ? `blur(${bl.toFixed(2)}px)` : "none";
    const id = M3.micro(t, 17, vnoise), Pf = PERF(t), acc = accents(t);
    const bones = add(Pf.bones, id, { head: [0.03 * acc, 0, 0], neck: [0.012 * acc, 0, 0] });
    const root = { x: Pf.root.x, y: Pf.root.y, ry: Pf.root.ry + 0.012 * vnoise(t, 26, 0.18), rz: Pf.root.rz, rx: 0, s: Pf.root.s };
    const bl2 = M3.blink(t, 0, D, 3, DIR.blinks), gz = DIR.gaze(t);
    if (mascot.shadow) mascot.shadow.visible = false;
    mascot.setView(P.v);
    mascot.setState({ root, bones, face: { blink: [bl2, bl2], gaze: [gz[0], gz[1]], mouthMix: 1, mouth: mouthAt(t), brow: [0, 0] } });
    mascot.render();
  }
  window.__mascotPose = pose;
  window.__hf = window.__hf || {};
  window.__hf.buildReady = window.__hf.buildReady || {};
  const ready = M3.Mascot.create(canvas, { url: "assets/mascot3d/mascot_biz_rigged.glb", face: FACE, decals: DECALS, width: CW, height: CH, envIntensity: 0.6 })
    .then((m) => {
      mascot = m;
      for (const o of m.scene.children) if (o.isDirectionalLight && o.position.z < 0) { o.intensity = 1.6; o.color.setRGB(0.72, 0.84, 1.0); o.position.set(1.6, 1.5, -1.4); }
      apply(0);
    });
  window.__hf.buildReady["mascot"] = ready;
  window.addEventListener("hf-seek", (e) => {
    const t = e.detail.time + (window.__T0 || 0);
    if (mascot) apply(t);
    else if (e.detail.waitUntil) e.detail.waitUntil(ready.then(() => apply(t)));
  });
})();

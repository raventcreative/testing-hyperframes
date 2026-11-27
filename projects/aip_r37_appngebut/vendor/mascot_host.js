/* the client's 3D mascot as the HOST (R-series runtime: lip sync from VO_PHONES/VO_ENV, acting from intents) */
(function () {
      // AI PRENEUR chibi businessman = the corner HOST of R37 (whole body, bottom-left), reacting on every beat. Based on the R35 runtime;
      // glances disabled (they made the eyes read blank in the R12/R13 renders). Live WebGL, lip sync from the VO phones.
      const M3 = window.Mascot3D;
      const { buildPerformance, buildLipTrack, syllableAccents, vnoise, bump } = M3;
      const VW = window.VO_WORDS, SC = window.VO_SCENES, D = window.TOTAL;
      const canvas = document.getElementById("ms");
      const mouthAt = buildLipTrack(window.VO_PHONES, window.VO_ENV, D, { smooth: 1 });
      const ACC = syllableAccents(window.VO_ENV, VW, window.VO_PHONES, D);
      const one = (x) => Math.max(0, Math.min(1, x));
      const sm = (u) => { u = one(u); return u * u * (3 - 2 * u); };
      const e3 = (u) => { u = one(u); return 1 - Math.pow(1 - u, 3); };
      const ei3 = (u) => { u = one(u); return u * u * u; };
      const io3 = (u) => { u = one(u); return u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2; };
      const L = (a, b, u) => a + (b - a) * u;
      const add = (...ds) => { const o = {}; for (const d of ds) for (const [k, v] of Object.entries(d || {})) { const a = o[k] || [0, 0, 0]; o[k] = [a[0] + v[0], a[1] + v[1], a[2] + v[2]]; } return o; };
      const S = (id) => SC.find((s) => s.id === id);
      const wt = (txt, after = 0) => { const w = VW.find((x) => x[0] === txt && x[1] >= after); if (!w) throw new Error("mascot: word not found " + txt); return w[1]; };
      function accents(t) { let n = 0; for (const a of ACC) { const d = t - a[0]; if (d > -0.25 && d < 0.35) n += bump(t, a[0] + 0.05, 0.17) * a[1]; } return Math.min(1.3, n); }
      // ---------------------------------------------------------------- framing
      // R37: the mascot is the small corner HOST (bottom-left), WHOLE body, never cropped. Small canvas (MS_W x MS_H) placed by CSS.
      const CW = window.MS_W, CH = window.MS_H;
      const HOST = { fx: CW / 2, fy: CH - 22, h: CH - 70, pitch: 6 };
      function view(t) {   // hops in from below at 0.05-0.6 s, then a small hop on every beat change
        const u = one((t - 0.05) / 0.55), dy = (CH + 40) * (1 - e3(u)) - 22 * Math.sin(Math.PI * one((t - 0.45) / 0.3));
        let hop = 0; for (const b of (window.BEATS || [])) { const d = t - (b - 0.12); if (d > 0 && d < 0.34) hop = Math.max(hop, 16 * Math.sin(Math.PI * d / 0.34)); }
        return { fx: HOST.fx, fy: HOST.fy + dy - hop, h: HOST.h, pitch: HOST.pitch, yaw: 0 };
      }
      const shown = (t) => t >= 0.04;
      // ---------------------------------------------------------------- acting
      // one reaction on every beat (the first word of every VO line), never the same twice in a row; CTA at "Komen".
      const ACTS = [["present", "right"], ["explain", "right"], ["point", "right"], ["emphasize", "left"], ["reveal", null], ["present", "right"], ["point", "right"], ["explain", "left"], ["emphasize", "right"]];
      const intents = [{ t: 0.1, action: "welcome" }];
      (window.BEATS || []).forEach((b, i, arr) => {
        if (i === 0) return;
        if (i === arr.length - 1) { intents.push({ t: b - 0.12, action: "cta", side: "right" }); return; }
        const a = ACTS[i % ACTS.length]; const it = { t: b - 0.14, action: a[0] }; if (a[1]) it.side = a[1]; intents.push(it);
      });
      intents.push({ t: wt("DM.") - 0.2, action: "point", side: "right" });
      intents.push({ t: D - 0.5, action: "idle" });
      intents.sort((p, q) => p.t - q.t);
      const DIR = M3.direct(VW, D, { intents, seed: 35, quiet: 0.3, look: 0 });
      const PERF = buildPerformance(DIR.tracks, D + 0.05, { smooth: 1 });
      const lookUp = () => 0;
      // glances at the robot (small turn: a bigger yaw turns the face decal away and one eye reads blank in the render)
      const glance = (t) => 0;   // glances disabled: in the render a glance made the eyes read blank (big white disc)
      const FACE = window.MASCOT_FACE;
      const DECALS = window.MASCOT_DECALS;
      let mascot = null;
      function apply(t) {
        if (!shown(t)) { mascot.setState({ visible: false }); mascot.render(); return; }
        const id = M3.micro(t, 17, vnoise), Pf = PERF(t), acc = accents(t);
        const lu = lookUp(t), gl = glance(t);
        const bones = add(Pf.bones, id, { head: [0.03 * acc - 0.3 * lu - 0.02 * gl, -0.28 * lu + 0.14 * gl, 0.06 * lu + 0.04 * gl], neck: [0.012 * acc - 0.12 * lu, -0.1 * lu + 0.05 * gl, 0], spine: [-0.05 * lu, 0, 0] });
        const root = { x: Pf.root.x, y: Pf.root.y, ry: Pf.root.ry + 0.012 * vnoise(t, 26, 0.18) + 0.1 * gl, rz: Pf.root.rz, rx: 0, s: Pf.root.s };
        const bl = M3.blink(t, 0, D, 3, DIR.blinks);
        const gz = DIR.gaze(t);
        const gaze = [L(gz[0], 0.08, gl), gz[1]];   // the head turns; the eyes follow only a little (0.24 pushed the iris off the eye)
        if (mascot.shadow) mascot.shadow.visible = false;
        mascot.setView(view(t));
        mascot.setState({ root, bones, face: { blink: [bl, bl], gaze, mouthMix: 1, mouth: mouthAt(t), brow: [0.25 * lu, 0.25 * lu] } });
        mascot.render();
      }
      window.__hf = window.__hf || {};
      window.__hf.buildReady = window.__hf.buildReady || {};
      const ready = M3.Mascot.create(canvas, { url: "assets/mascot3d/mascot_biz_rigged.glb", face: FACE, decals: DECALS, width: window.MS_W, height: window.MS_H, envIntensity: 0.6 })
        .then((m) => {
          mascot = m;
          // navy stage: brand-cyan rim light from behind-right
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

/* the client's 3D mascot as the HOST (R-series runtime: lip sync from VO_PHONES/VO_ENV, acting from intents) */
(function () {
      // AI PRENEUR chibi businessman = the HOST: half body, left of centre (the robot co-hosts at screen right). Already in frame at
      // 0 s, delivers the hook, introduces each tool, gets serious on the production caution, delivers the CTA (no glances at the
      // robot: they made the eyes read blank in the R12/R13 renders). Live WebGL, lip sync from the VO phones.
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
      const HOST = { fx: 300, fy: 2170, h: 1000, pitch: 4 };
      function view(t) {   // off screen until the voxel world has zoomed out, then rises in (6.1 -> 6.7 s) and settles
        const u = one((t - 3.6) / 0.6), dy = 1000 * (1 - e3(u)) - 36 * Math.sin(Math.PI * one((t - 3.95) / 0.4));
        return { fx: HOST.fx, fy: HOST.fy + dy, h: HOST.h, pitch: HOST.pitch, yaw: 0 };
      }
      const shown = (t) => t >= 3.58;
      // ---------------------------------------------------------------- acting

      const intents = [
        { t: 3.62, action: "welcome" },
        { t: wt("Hormozi:") - 0.12, action: "present", side: "right" },
        { t: wt("dipotong") - 0.1, action: "emphasize", side: "right" },
        { t: wt("CTA.") - 0.1, action: "point", side: "right" },
        { t: wt("Bikin") - 0.1, action: "reveal" },
        { t: wt("isi,", 11) - 0.12, action: "explain", side: "left" },
        { t: wt("kombinasikan.") - 0.1, action: "point", side: "right" },
        { t: wt("seratus") - 0.12, action: "emphasize", side: "right" },
        { t: wt("tujuh") - 0.12, action: "emphasize", side: "left" },
        { t: wt("Hook-nya") - 0.1, action: "reveal" },
        { t: wt("menang,") - 0.12, action: "point", side: "right" },
        { t: wt("laris.") - 0.12, action: "emphasize", side: "right" },
        { t: wt("Sebar") - 0.1, action: "present", side: "right" },
        { t: wt("solusi,") - 0.1, action: "explain", side: "left" },
        { t: wt("produkmu.") - 0.12, action: "point", side: "right" },
        { t: wt("Isinya") - 0.1, action: "reveal" },
        { t: wt("edukasi,") - 0.1, action: "compare" },
        { t: wt("CTA-nya") - 0.1, action: "present", side: "right" },
        { t: wt("kapan,") - 0.1, action: "explain", side: "left" },
        { t: wt("dapat") - 0.12, action: "emphasize", side: "right" },
        { t: wt("berat") - 0.12, action: "emphasize", side: "left" },
        { t: wt("AI") - 0.1, action: "reveal" },
        { t: wt("puluhan") - 0.1, action: "point", side: "right" },
        { t: wt("pilih.") - 0.12, action: "point", side: "right" },
        { t: wt("Komen") - 0.1, action: "cta", side: "right" },
        { t: wt("DM.") - 0.2, action: "point", side: "left" },
        { t: D - 0.5, action: "idle" },
      ];
      intents.sort((p, q) => p.t - q.t);
      const DIR = M3.direct(VW, D, { intents, seed: 71, quiet: 0.3, look: 0 });
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
      const ready = M3.Mascot.create(canvas, { url: "assets/mascot3d/mascot_biz_rigged.glb", face: FACE, decals: DECALS, width: 1080, height: 1920, envIntensity: 0.6 })
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

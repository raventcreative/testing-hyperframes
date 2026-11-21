/* AI PRENEUR ROBOT = the CO-HOST (ported from projects/aip_r25_prompt3d/compositions/robot.html, Robot3D GLB runtime).
   Stands whole at screen right beside the mascot, flies in after the world reveal, reacts on the VO words: waves, points,
   types the prompt on a holo keyboard, scans the reply, shows the AI voice as talk bars on its face screen, shakes its head
   at "bukan jaminan", cheers the CTA. Pure function of time (hf-seek). */
(function () {
  const VW = window.VO_WORDS, D = window.TOTAL, M3 = window.Mascot3D;
  const one = (x) => Math.max(0, Math.min(1, x));
  const sm = (u) => { u = one(u); return u * u * (3 - 2 * u); };
  const io3 = (u) => { u = one(u); return u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2; };
  const L = (a, b, u) => a + (b - a) * u;
  const vn = M3.vnoise;
  const wt = (txt, after = 0) => { const w = VW.find((x) => x[0] === txt && x[1] >= after); if (!w) throw new Error("robot: word not found " + txt); return w[1]; };
  const env = (t) => { const E = window.VO_ENV; const i = Math.floor(t * 100); return i >= 0 && i < E.length ? E[i] / 99 : 0; };
  const HEAD_FIX = [-0.0775, -0.227, -0.1287];
  const STAND = { fx: 862, fy: 1700, h: 340, ry: -0.42 };
  const T_IN = 7.25;
  const HOPS = ["Satu.", "Dua.", "Hook", "Tiga.", "Empat.", "Tapi", "Komen"].map((x) => wt(x) - 0.05);
  function frame(t) {
    if (t < T_IN) return null;
    const u = io3((t - T_IN) / 0.8), arc = Math.sin(Math.PI * u) * 170;
    const f = { fx: L(1360, STAND.fx, u), fy: L(1480, STAND.fy, u) - arc, h: L(300, STAND.h, u), ry: L(-1.1, STAND.ry, u), fly: u };
    for (const s0 of HOPS) { const k = t - s0; if (k > 0 && k < 0.5) f.fy -= 30 * Math.sin(Math.PI * k / 0.5); }
    return f;
  }
  const G = [];
  const add = (t, k, d = 0.9, x) => { if (t > T_IN + 0.5) G.push(Object.assign({ t, k, d }, x || {})); };
  add(T_IN + 0.55, "wave", 1.0); add(wt("UMKM,") - 0.05, "point", 0.6, { up: 1 }); add(wt("online") - 0.05, "nod", 0.5); add(wt("affiliator.") - 0.05, "happy", 0.6);
  add(wt("terang:") - 0.05, "happy", 0.6); add(wt("depan,") - 0.05, "scan", 0.5); add(wt("samping,") - 0.05, "scan", 0.6); add(wt("detail") - 0.05, "point", 0.7, { up: 1 });
  add(wt("Dua.") + 0.08, "type", wt("Kirim") + 0.45 - wt("Dua.") - 0.08); add(wt("asisten") - 0.1, "point", 0.5, { up: 1 }); add(wt("nulis") - 0.05, "scan", 1.4); add(wt("detik.") - 0.05, "nod", 0.5);
  add(wt("harga,") - 0.05, "point", 0.5, { up: 1 }); add(wt("ukuran,") - 0.05, "nod", 0.5); add(wt("siapa") - 0.05, "think", 0.8);
  add(wt("Hook") - 0.05, "happy", 0.5); add(wt("manfaat") - 0.05, "nod", 0.6); add(wt("ajakan") - 0.05, "point", 0.6, { up: 1 }); add(wt("keranjang") - 0.05, "cheer", 0.8);
  add(wt("Naskah") - 0.1, "talk", wt("jualan.") + 0.55 - wt("Naskah") + 0.1); add(wt("marketer", 30) - 0.05, "happy", 0.6); add(wt("jualan.") - 0.05, "cheer", 0.6);
  add(wt("Adegan,") - 0.05, "scan", 1.2); add(wt("dirender") - 0.05, "type", 0.8); add(wt("video", 36) - 0.05, "happy", 0.6); add(wt("diunggah.") - 0.05, "clap", 0.7);
  add(wt("kamu") - 0.05, "point", 0.7, { up: 1 }); add(wt("dibikin") - 0.05, "happy", 0.7); add(wt("mirip.") - 0.05, "nod", 0.5);
  add(wt("Tapi") - 0.05, "think", 0.8); add(wt("bukan") - 0.05, "no", 0.9); add(wt("Cek") - 0.05, "scan", 1.4); add(wt("posting.") - 0.05, "nod", 0.5);
  add(wt("Komen") - 0.08, "cheer", 0.9); add(wt("DM.") - 0.1, "point", 0.7, { up: 1 }); add(D - 1.05, "wave", 0.95);
  const envG = (t, g) => sm((t - g.t + 0.16) / 0.2) * (1 - sm((t - (g.t + g.d)) / 0.26));
  const BL = []; { let x = T_IN + 1.2, h = 13; while (x < D) { BL.push(x); h = (h * 9301 + 49297) % 233280; x += 2.1 + (h / 233280) * 2.3; } }
  const blinkAt = (t) => { let v = 0; for (const b of BL) { const d = t - b; if (d > -0.06 && d < 0.18) v = Math.max(v, d < 0 ? 1 + d / 0.06 : 1 - sm((d - 0.04) / 0.14)); } return Math.max(0, v); };
  function perf(t) {
    const fr = frame(t); if (!fr) return null;
    const root = { x: 0, y: 0, z: 0, rx: 0, ry: fr.ry, rz: 0, s: 1 };
    const bones = { body: [0, 0, 0], head: [0, 0, 0], hand_L: [0, 0, 0], hand_R: [0, 0, 0] };
    const offs = { hand_L: [0, 0, 0], hand_R: [0, 0, 0], head: [0, 0, 0] };
    const face = { blink: blinkAt(t), gaze: [0, 0.03], happy: 0, squint: 0, talk: 0, bars: [0, 0, 0, 0, 0], glow: 1 };
    root.y = 0.014 * Math.sin(2 * Math.PI * 0.55 * t) + 0.006 * Math.sin(2 * Math.PI * 1.27 * t + 1.1);
    root.rz = 0.03 * Math.sin(2 * Math.PI * 0.41 * t + 0.4);
    root.rx = 0.018 * Math.sin(2 * Math.PI * 0.5 * t + 1.7);
    bones.head = [HEAD_FIX[0] + 0.02 * vn(t, 5, 0.25), HEAD_FIX[1] + 0.05 * vn(t, 6, 0.18), HEAD_FIX[2] + 0.03 * vn(t, 7, 0.2)];
    offs.hand_L = [-0.07 + 0.006 * vn(t, 11, 0.4), 0.018 * Math.sin(2 * Math.PI * 0.55 * t + 1.3), 0.008 * vn(t, 12, 0.35)];
    offs.hand_R = [0.07 + 0.006 * vn(t, 13, 0.4), 0.018 * Math.sin(2 * Math.PI * 0.55 * t + 2.4), 0.008 * vn(t, 14, 0.35)];
    bones.hand_L = [0.08 * Math.sin(2 * Math.PI * 0.5 * t), 0, 0.06 * vn(t, 15, 0.3)];
    bones.hand_R = [0.08 * Math.sin(2 * Math.PI * 0.5 * t + 1), 0, 0.06 * vn(t, 16, 0.3)];
    face.gaze = [-0.06 + 0.05 * vn(t, 21, 0.22), 0.05 + 0.04 * vn(t, 22, 0.2)];
    if (fr.fly < 1) { const k = 1 - fr.fly; root.rz += 0.3 * Math.sin(Math.PI * fr.fly) * k; root.rx += 0.15 * k; offs.hand_L[0] += 0.08 * k; offs.hand_R[0] += 0.08 * k; offs.hand_L[1] += 0.06 * k; offs.hand_R[1] += 0.06 * k; }
    let ring = 1, kb = 0;
    for (const g of G) {
      const w = envG(t, g); if (w < 1e-3) continue;
      const lt = t - g.t;
      switch (g.k) {
        case "type": { kb = Math.max(kb, w);
          const a = Math.sin(lt * 2 * Math.PI * 5.2), b = Math.sin(lt * 2 * Math.PI * 4.6 + 1.7);
          offs.hand_L = [L(offs.hand_L[0], -0.09, w), L(offs.hand_L[1], -0.07 + 0.016 * Math.max(0, a), w), L(offs.hand_L[2], 0.15, w)];
          offs.hand_R = [L(offs.hand_R[0], 0.09, w), L(offs.hand_R[1], -0.07 + 0.016 * Math.max(0, b), w), L(offs.hand_R[2], 0.15, w)];
          bones.hand_L[0] += 0.55 * w; bones.hand_R[0] += 0.55 * w; bones.head[0] += 0.14 * w;
          root.ry = L(root.ry, -0.04, w); root.rx += 0.05 * w;
          face.gaze = [L(face.gaze[0], -0.05, w), L(face.gaze[1], -0.2, w)]; ring += 0.4 * w; break; }
        case "talk": { const e = env(t); face.talk = Math.max(face.talk, w); face.bars = [0, 1, 2, 3, 4].map((i) => Math.min(1, env(t - i * 0.06) * (0.7 + 0.3 * Math.abs(Math.sin(i * 1.7 + t * 3))) * 1.3));
          face.happy = Math.max(face.happy, 0.35 * w); ring += 0.6 * w * e; bones.head[0] += 0.03 * w * e; break; }
        case "scan": { const sw = Math.sin(lt * 2 * Math.PI * 1.1);
          bones.head[1] += 0.26 * w * sw; face.gaze = [L(face.gaze[0], 0.28 * sw, w), L(face.gaze[1], 0.12, w)]; face.squint = Math.max(face.squint, 0.45 * w); ring += 0.3 * w; break; }
        case "no": bones.head[1] += 0.22 * w * Math.sin(lt * 2 * Math.PI * 2.6); face.squint = Math.max(face.squint, 0.6 * w); break;
        case "nod": bones.head[0] += 0.12 * w * Math.max(0, Math.sin(lt * 2 * Math.PI * 1.6)); break;
        case "happy": face.happy = Math.max(face.happy, w); ring += 0.5 * w; break;
        case "think": face.squint = Math.max(face.squint, 0.45 * w); face.gaze = [L(face.gaze[0], 0.16, w), L(face.gaze[1], 0.24, w)]; bones.head[2] += 0.14 * w;
          offs.hand_R = [L(offs.hand_R[0], 0.16, w), L(offs.hand_R[1], 0.17, w), L(offs.hand_R[2], 0.14, w)]; bones.hand_R[0] -= 0.4 * w; break;
        case "cheer": face.happy = Math.max(face.happy, w); ring += 0.7 * w; { const b = 0.5 + 0.5 * Math.sin(lt * 2 * Math.PI * 3);
          offs.hand_L = [L(offs.hand_L[0], -0.13, w), L(offs.hand_L[1], 0.24 + 0.04 * b, w), L(offs.hand_L[2], 0.06, w)];
          offs.hand_R = [L(offs.hand_R[0], 0.13, w), L(offs.hand_R[1], 0.24 + 0.04 * (1 - b), w), L(offs.hand_R[2], 0.06, w)]; root.y += 0.02 * w * b; } break;
        case "clap": { const c = 0.5 + 0.5 * Math.cos(lt * 2 * Math.PI * 4.5); const k = w * (0.65 + 0.35 * c);
          offs.hand_L = [L(offs.hand_L[0], -0.24, k), L(offs.hand_L[1], 0.09, w), L(offs.hand_L[2], 0.16, w)];
          offs.hand_R = [L(offs.hand_R[0], 0.24, k), L(offs.hand_R[1], 0.05, w), L(offs.hand_R[2], 0.1, w)]; face.happy = Math.max(face.happy, w); break; }
        case "point": { const up = g.up ? 0.14 : 0;
          offs.hand_R = [L(offs.hand_R[0], 0.02, w), L(offs.hand_R[1], 0.12 + up, w), L(offs.hand_R[2], 0.25, w)];
          bones.hand_R = [L(bones.hand_R[0], -0.35 - up, w), 0, L(bones.hand_R[2], 0.3, w)]; face.gaze = [L(face.gaze[0], -0.2, w), L(face.gaze[1], 0.1 + up, w)]; bones.head[0] -= 0.06 * w; break; }
        case "wave": { const k = w;
          offs.hand_L = [L(offs.hand_L[0], 0.04, k), L(offs.hand_L[1], 0.30, k), L(offs.hand_L[2], 0.1, k)];
          bones.hand_L = [L(bones.hand_L[0], -0.3, k), 0, L(bones.hand_L[2], -0.35, k) + 0.45 * k * Math.sin(lt * 2 * Math.PI * 2.2)];
          face.happy = Math.max(face.happy, 0.7 * k); break; }
      }
    }
    face.blink *= 1 - face.happy;
    return { fr, kb, state: { root, bones, offs, face, ring, shadow: false } };
  }
  const cv = document.getElementById("rb"), kbEl = document.getElementById("rb-kb"), KEYS = [];
  document.getElementById("rb-keys").innerHTML = Array.from({ length: 30 }, (_, i) => `<i id="rb-k${i}"></i>`).join("");
  for (let i = 0; i < 30; i++) KEYS.push(document.getElementById("rb-k" + i));
  const hash = (n) => { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };
  let robot = null;
  function apply(t) {
    const p = perf(t);
    if (!p) { robot.setState({ visible: false }); robot.render(); kbEl.style.opacity = "0"; return; }
    robot.setView({ fx: p.fr.fx, fy: p.fr.fy, h: p.fr.h, pitch: 5 });
    robot.setState(p.state); robot.render();
    const o = (0.9 * p.kb).toFixed(3); if (kbEl.style.opacity !== o) kbEl.style.opacity = o;
    if (p.kb > 0.001) {
      const x = p.fr.fx - 0.06 * p.fr.h, y = p.fr.fy - 0.1 * p.fr.h;
      kbEl.style.transform = `translate(${x.toFixed(1)}px, ${y.toFixed(1)}px) perspective(600px) rotateX(52deg) scale(${(0.75 + 0.25 * p.kb).toFixed(3)})`;
      const f = Math.floor(t * 14);
      for (let i = 0; i < 30; i++) KEYS[i].classList.toggle("on", hash(f * 31 + i) > 0.82);
    }
  }
  window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {};
  const ready = window.Robot3D.Robot.create(cv, { url: "assets/robot3d/robot_aipreneur.glb", width: 1080, height: 1920, envIntensity: 0.55 })
    .then((r) => { robot = r; apply(0); });
  window.__hf.buildReady["robot"] = ready;
  window.addEventListener("hf-seek", (e) => { const t = e.detail.time + (window.__T0 || 0); if (robot) apply(t); else if (e.detail.waitUntil) e.detail.waitUntil(ready.then(() => apply(t))); });
})();

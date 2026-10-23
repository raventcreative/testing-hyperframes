// Acting helpers: every function is a pure function of time (seek-safe, no randomness).
export const E = {
  lin: (t) => t,
  io: (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
  sine: (t) => -(Math.cos(Math.PI * t) - 1) / 2,
  out: (t) => 1 - Math.pow(1 - t, 3),
  out4: (t) => 1 - Math.pow(1 - t, 4),
  in: (t) => t * t * t,
  back: (t) => { const c1 = 1.9, c3 = c1 + 1; return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2); },
  el: (t) => (t === 0 ? 0 : t === 1 ? 1 : Math.pow(2, -9 * t) * Math.sin((t * 9 - 0.75) * ((2 * Math.PI) / 3.2)) + 1),
  hold: () => 0,
};
// keys: [[time, value(number|array), easeIntoThisKey], ...]
export function track(keys) {
  return (t) => {
    if (t <= keys[0][0]) return keys[0][1];
    for (let i = 1; i < keys.length; i++) {
      const [t1, v1, e] = keys[i];
      if (t <= t1) {
        const [t0, v0] = keys[i - 1];
        const u = (E[e || 'io'])((t - t0) / Math.max(1e-6, t1 - t0));
        return Array.isArray(v0) ? v0.map((a, j) => a + (v1[j] - a) * u) : v0 + (v1 - v0) * u;
      }
    }
    return keys[keys.length - 1][1];
  };
}
// enveloped oscillation (finite, eases in/out)
export function osc(t, t0, t1, hz, amp, phase = 0, attack = 0.15, release = 0.2) {
  if (t < t0 || t > t1) return 0;
  const env = Math.min(1, (t - t0) / attack) * Math.min(1, (t1 - t) / release);
  return Math.sin((t - t0) * hz * 2 * Math.PI + phase) * amp * E.sine(Math.max(0, Math.min(1, env)));
}
// deterministic blink schedule inside [t0,t1]: returns lid closure 0..1
export function blink(t, t0, t1, seed = 1, extra = []) {
  const times = [...extra];
  let h = seed * 9301 + 49297;
  for (let k = t0 + 0.6 + (seed % 5) * 0.13; k < t1 - 0.2; ) {
    times.push(k);
    h = (h * 9301 + 49297) % 233280;
    k += 2.1 + (h / 233280) * 1.6;
  }
  let v = 0;
  for (const b of times) {
    const d = t - b;
    if (d >= 0 && d < 0.07) v = Math.max(v, E.in(d / 0.07));
    else if (d >= 0.07 && d < 0.1) v = 1;
    else if (d >= 0.1 && d < 0.2) v = Math.max(v, 1 - E.out((d - 0.1) / 0.1));
  }
  return v;
}
// walk cycle between t0..t1 with n steps; returns bone rotations + root bob
export function walk(t, t0, t1, n = 2, stride = 0.42) {
  if (t < t0 || t > t1) return { bones: {}, bob: 0 };
  const u = (t - t0) / (t1 - t0);
  const ph = u * n * Math.PI;           // one step per half cycle
  const env = Math.sin(Math.PI * Math.min(1, u * 1.15));
  const s = Math.sin(ph) * stride * env;
  return {
    bones: {
      thigh_L: [-s, 0, 0], thigh_R: [s, 0, 0],
      shin_L: [Math.max(0, s) * 0.9, 0, 0], shin_R: [Math.max(0, -s) * 0.9, 0, 0],
      upperarm_L: [s * 0.55, 0, 0], upperarm_R: [-s * 0.55, 0, 0],
      spine: [0, s * 0.12, 0],
    },
    bob: Math.abs(Math.sin(ph)) * 0.012 * env,
  };
}
// ---- Indonesian grapheme → viseme lip sync ----
const V = {
  rest: [0.03, 0.0, 0.007, 0.0],
  MBP: [0.028, 0.0, 0.003, 0.0],
  AA: [0.038, 0.034, 0.005, 0.7],
  E: [0.043, 0.017, 0.004, 0.35],
  I: [0.044, 0.012, 0.005, 0.25],
  O: [0.024, 0.029, 0.0, 0.5],
  U: [0.019, 0.019, 0.0, 0.35],
  FV: [0.034, 0.006, 0.003, 0.0],
  C: [0.033, 0.012, 0.004, 0.3],
};
function g2v(word) {
  const w = word.toLowerCase().replace(/[^a-z]/g, '');
  const out = [];
  for (let i = 0; i < w.length; i++) {
    const c = w[i], nx = w[i + 1];
    if (c === 'n' && nx === 'g') { out.push(['C', 0.6]); i++; continue; }
    if ('a'.includes(c)) out.push(['AA', 1]);
    else if (c === 'e') out.push(['E', 1]);
    else if (c === 'i') out.push(['I', 1]);
    else if (c === 'o') out.push(['O', 1]);
    else if (c === 'u' || c === 'w') out.push(['U', c === 'u' ? 1 : 0.6]);
    else if ('mbp'.includes(c)) out.push(['MBP', 0.7]);
    else if ('fv'.includes(c)) out.push(['FV', 0.6]);
    else out.push(['C', 0.55]);
  }
  return out;
}
// words: [{text, phon?, start, end}] (global seconds). Returns {mix, mouth}.
export function lipsync(t, words) {
  const pts = [];
  for (const wd of words) {
    const ph = g2v(wd.phon || wd.text);
    const tot = ph.reduce((a, p) => a + p[1], 0);
    let c = wd.start;
    pts.push([wd.start - 0.05, V.rest]);
    for (const [v, w] of ph) {
      const d = ((wd.end - wd.start) * w) / tot;
      pts.push([c + d * 0.5, V[v]]);
      c += d;
    }
    pts.push([wd.end + 0.04, V.rest]);
  }
  pts.sort((a, b) => a[0] - b[0]);
  if (!pts.length || t <= pts[0][0] || t >= pts[pts.length - 1][0]) return V.rest.slice();
  for (let i = 1; i < pts.length; i++) {
    if (t <= pts[i][0]) {
      const [t0, a] = pts[i - 1], [t1, b] = pts[i];
      const u = E.sine((t - t0) / Math.max(1e-4, t1 - t0));
      return a.map((x, j) => x + (b[j] - x) * u);
    }
  }
  return V.rest.slice();
}
export const VISEMES = V;
// merge bone dictionaries by adding rotations
export function addBones(...dicts) {
  const out = {};
  for (const d of dicts) for (const [k, v] of Object.entries(d || {})) {
    const o = out[k] || [0, 0, 0];
    out[k] = [o[0] + v[0], o[1] + v[1], o[2] + v[2]];
  }
  return out;
}

// =====================================================================================
// v3 SPEECH ENGINE — the mascot narrates the whole VO.
// All curves are smooth (smoothstep / raised-cosine), pure functions of time.
// =====================================================================================
export const clamp01 = (x) => Math.max(0, Math.min(1, x));
export const ss = (a, b, t) => { const u = clamp01((t - a) / Math.max(1e-6, b - a)); return u * u * (3 - 2 * u); };
// 0 → 1 over [a, a+ri], hold, 1 → 0 over [b-ro, b]
export const env = (t, a, b, ri = 0.25, ro = 0.3) => ss(a, a + ri, t) * (1 - ss(b - ro, b, t));
// raised-cosine bump centred at c, half-width w
export const bump = (t, c, w) => { const u = (t - c) / w; return Math.abs(u) >= 1 ? 0 : 0.5 + 0.5 * Math.cos(Math.PI * u); };

// words: [[text, start, end, keyword, phon?], ...] (vendor/vo_words.js)
export function buildSpeech(raw) {
  const words = raw.map((w, i) => ({ i, text: w[0], s: w[1], e: w[2], key: !!w[3], phon: w[4] }));
  const phrases = [];
  let cur = null;
  for (const w of words) {
    if (!cur || w.s - cur.e > 0.12) { cur = { s: w.s, e: w.e, words: [] }; phrases.push(cur); }
    cur.words.push(w); cur.e = w.e;
  }
  // hand pattern per phrase: R = his right arm (screen-left), L = his left (screen-right), B = both
  const PAT = ['R', 'L', 'B', 'L', 'R', 'B'];
  phrases.forEach((p, i) => { p.i = i; p.hand = PAT[i % PAT.length]; });
  // lip-sync key points (coarticulated; mouth only closes in real gaps)
  const pts = [];
  for (let k = 0; k < words.length; k++) {
    const wd = words[k], prev = words[k - 1], next = words[k + 1];
    const ph = g2v(wd.phon || wd.text);
    const tot = ph.reduce((a, p) => a + p[1], 0);
    if (!prev || wd.s - prev.e > 0.07) pts.push([wd.s - 0.06, V.rest]);
    let c = wd.s;
    for (const [v, wt] of ph) { const d = ((wd.e - wd.s) * wt) / tot; pts.push([c + d * 0.5, V[v]]); c += d; }
    if (!next || next.s - wd.e > 0.07) pts.push([wd.e + 0.05, V.rest]);
  }
  pts.sort((a, b) => a[0] - b[0]);
  return { words, phrases, pts };
}
function findIdx(arr, t, key) { // last index with arr[i][key] <= t
  let lo = 0, hi = arr.length - 1, r = -1;
  while (lo <= hi) { const m = (lo + hi) >> 1; if (key(arr[m]) <= t) { r = m; lo = m + 1; } else hi = m - 1; }
  return r;
}
export function lipAt(S, t) {
  const P = S.pts;
  const i = findIdx(P, t, (p) => p[0]);
  if (i < 0 || i >= P.length - 1) return V.rest.slice();
  const [t0, a] = P[i], [t1, b] = P[i + 1];
  if (t1 - t0 > 0.6) { // long silence: ease to rest and stay
    const u = E.sine(clamp01((t - t0) / 0.12)), w = E.sine(clamp01((t - (t1 - 0.12)) / 0.12));
    const m = a.map((x, j) => x + (V.rest[j] - x) * u);
    return m.map((x, j) => x + (b[j] - x) * w);
  }
  const u = E.sine((t - t0) / Math.max(1e-4, t1 - t0));
  return a.map((x, j) => x + (b[j] - x) * u);
}
export function speakingAt(S, t) {
  let v = 0;
  const i = findIdx(S.phrases, t + 0.3, (p) => p.s);
  for (let k = Math.max(0, i - 1); k <= i && k >= 0; k++) { const p = S.phrases[k]; v = Math.max(v, env(t, p.s - 0.15, p.e + 0.35, 0.25, 0.35)); }
  return v;
}
// Talking body language: alternating hand gestures per phrase with beats on every word
// (stronger on caption keywords), keyword head nods, syllable head bob, body sway.
// o: { amp, wL(0..1), wR(0..1), head, sway }
export function talk(S, t, o = {}) {
  const amp = o.amp == null ? 1 : o.amp, wL = o.wL == null ? 1 : clamp01(o.wL), wR = o.wR == null ? 1 : clamp01(o.wR);
  const head = o.head == null ? 1 : o.head, sway = o.sway == null ? 1 : o.sway;
  let gL = 0, gR = 0, beatL = 0, beatR = 0, nod = 0;
  const i = findIdx(S.phrases, t + 0.35, (p) => p.s);
  for (let k = Math.max(0, i - 2); k <= i && k >= 0; k++) {
    const p = S.phrases[k];
    const g = env(t, p.s - 0.28, p.e + 0.45, 0.3, 0.42);
    if (g <= 0) continue;
    const L = p.hand !== 'R', R = p.hand !== 'L';
    if (L) gL = Math.max(gL, g * (p.hand === 'B' ? 0.85 : 1));
    if (R) gR = Math.max(gR, g * (p.hand === 'B' ? 0.85 : 1));
    for (const w of p.words) {
      const b = bump(t, w.s + 0.07, w.key ? 0.2 : 0.15) * (w.key ? 1 : 0.5);
      if (L) beatL = Math.max(beatL, b); if (R) beatR = Math.max(beatR, b);
      if (w.key) nod += bump(t, w.s + 0.06, 0.2);
    }
  }
  const sp = speakingAt(S, t);
  gL *= amp * wL; gR *= amp * wR; beatL *= gL; beatR *= gR;
  const dL = Math.sin(t * 2 * Math.PI * 0.55 + 1.3), dR = Math.sin(t * 2 * Math.PI * 0.6);
  const bones = {
    // his right arm (screen-left)
    upperarm_R: [(-0.42 - 0.14 * beatR) * gR, 0.1 * gR, (-0.5 - 0.1 * beatR - 0.07 * dR) * gR],
    forearm_R: [(-0.95 - 0.4 * beatR) * gR, 0.18 * gR, -0.12 * gR],
    hand_R: [0.1 * gR, (0.3 + 0.12 * dR) * gR, (-0.2 - 0.38 * beatR) * gR],
    // his left arm (screen-right)
    upperarm_L: [(-0.42 - 0.14 * beatL) * gL, -0.1 * gL, (0.5 + 0.1 * beatL + 0.07 * dL) * gL],
    forearm_L: [(-0.95 - 0.4 * beatL) * gL, -0.18 * gL, 0.12 * gL],
    hand_L: [0.1 * gL, (-0.3 - 0.12 * dL) * gL, (0.2 + 0.38 * beatL) * gL],
    head: [(0.1 * Math.min(1.4, nod) + 0.022 * sp * Math.sin(t * 2 * Math.PI * 2.4)) * head,
           0.08 * sp * Math.sin(t * 2 * Math.PI * 0.17 + 0.4) * head,
           0.065 * sp * Math.sin(t * 2 * Math.PI * 0.23 + 1.0) * head],
    neck: [0.03 * Math.min(1.4, nod) * head, 0, 0],
    chest: [(0.035 * (beatL + beatR) * 0.5 + 0.02 * sp) * sway, 0.05 * (gL - gR) * sway, 0],
    spine: [0, 0.03 * sp * Math.sin(t * 2 * Math.PI * 0.21) * sway, 0.032 * sp * Math.sin(t * 2 * Math.PI * 0.29 + 0.7) * sway],
  };
  return { bones, sp, ry: 0.06 * sp * Math.sin(t * 2 * Math.PI * 0.13 + 0.5) * sway };
}

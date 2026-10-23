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

// Motion toolkit: custom cubic-bezier curves, damped springs, velocity profiles,
// keyframe tracks and layered float. Everything is a pure function of time so
// any frame can be rendered independently (deterministic, seekable).

export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lerp = (a, b, t) => a + (b - a) * t;
export const remap = (t, a, b) => clamp((t - a) / (b - a));
export const smooth = (t) => t * t * (3 - 2 * t);
export const smoother = (t) => t * t * t * (t * (t * 6 - 15) + 10);
export const mixArr = (a, b, t) => a.map((v, i) => lerp(v, b[i], t));
export const DEG = Math.PI / 180;

// --- cubic bezier (CSS semantics), solved with Newton + bisection fallback ---
export function bezier(x1, y1, x2, y2) {
  const cx = 3 * x1, bx = 3 * (x2 - x1) - cx, ax = 1 - cx - bx;
  const cy = 3 * y1, by = 3 * (y2 - y1) - cy, ay = 1 - cy - by;
  const sx = (t) => ((ax * t + bx) * t + cx) * t;
  const sy = (t) => ((ay * t + by) * t + cy) * t;
  const dx = (t) => (3 * ax * t + 2 * bx) * t + cx;
  return (x) => {
    if (x <= 0) return 0;
    if (x >= 1) return 1;
    let t = x;
    for (let i = 0; i < 8; i++) {
      const e = sx(t) - x;
      const d = dx(t);
      if (Math.abs(e) < 1e-7) return sy(t);
      if (Math.abs(d) < 1e-6) break;
      t -= e / d;
    }
    let lo = 0, hi = 1;
    t = x;
    for (let i = 0; i < 40; i++) {
      const v = sx(t);
      if (Math.abs(v - x) < 1e-7) break;
      if (v < x) lo = t; else hi = t;
      t = (lo + hi) / 2;
    }
    return sy(t);
  };
}

// Hand-tuned curve set. Long, soft tails = "expensive" deceleration.
export const EASE = {
  linear: (t) => t,
  // arrival: confident launch, long graceful deceleration (cubic-out family)
  arrive: bezier(0.215, 0.61, 0.355, 1.0),
  // hero move: weighted start, graceful landing
  glide: bezier(0.55, 0.05, 0.18, 1.0),
  // symmetric, heavy object
  inOut: bezier(0.62, 0.0, 0.32, 1.0),
  // gentle start for things that "lift off"
  lift: bezier(0.45, 0.0, 0.85, 0.4),
  // quick out (UI-like accents: marker wipes)
  marker: bezier(0.3, 0.0, 0.1, 1.0),
  soft: bezier(0.33, 0.0, 0.2, 1.0),
};

// Damped spring step response 0 -> 1 (underdamped when zeta < 1).
// freq in Hz, zeta = damping ratio. Physically correct overshoot + settle.
export function spring(t, freq = 1.6, zeta = 0.55) {
  if (t <= 0) return 0;
  const w = 2 * Math.PI * freq;
  if (zeta >= 1) {
    return 1 - Math.exp(-w * t) * (1 + w * t);
  }
  const wd = w * Math.sqrt(1 - zeta * zeta);
  return 1 - Math.exp(-zeta * w * t) * (Math.cos(wd * t) + (zeta * w / wd) * Math.sin(wd * t));
}

// Spring that reaches the target with a guaranteed soft landing (blend to 1 at the end)
export function springTo(t, t0, dur, freq = 1.6, zeta = 0.55) {
  const local = t - t0;
  if (local <= 0) return 0;
  const s = spring(local, freq, zeta);
  const tail = smoother(remap(local, dur * 0.7, dur));
  return lerp(s, 1, tail);
}

// Keyframe track: keys = [[t, value, ease?], ...]; value number or array.
// Ease on key i applies to the segment arriving at key i.
export function track(keys) {
  return (t) => {
    if (t <= keys[0][0]) return keys[0][1];
    for (let i = 1; i < keys.length; i++) {
      const [t1, v1, e] = keys[i];
      const [t0, v0] = keys[i - 1];
      if (t <= t1) {
        const k = (e || EASE.inOut)(remap(t, t0, t1));
        return Array.isArray(v0) ? mixArr(v0, v1, k) : lerp(v0, v1, k);
      }
    }
    return keys[keys.length - 1][1];
  };
}

// Velocity-profile integrator: smooth acceleration, cruise, smooth deceleration.
// Returns position p(t) in [0, total] over [t0, t1]. Velocity is C1-continuous.
export function cruise(t0, t1, total, accel = 0.3, decel = 0.35) {
  const N = 4000;
  const table = new Float64Array(N + 1);
  const vel = (u) => {
    const a = u < accel ? smoother(u / accel) : 1;
    const d = u > 1 - decel ? smoother((1 - u) / decel) : 1;
    return Math.min(a, d);
  };
  let acc = 0;
  table[0] = 0;
  for (let i = 1; i <= N; i++) {
    const u = (i - 0.5) / N;
    acc += vel(u) / N;
    table[i] = acc;
  }
  const norm = total / acc;
  return (t) => {
    const u = remap(t, t0, t1) * N;
    const i = Math.floor(u);
    if (i >= N) return total;
    const f = u - i;
    return lerp(table[i], table[i + 1], f) * norm;
  };
}

// Layered, non-repeating float: sum of incommensurate sines (golden-ratio spaced).
export function drift(t, seed = 0, amp = 1, base = 0.21) {
  const phi = 1.61803398875;
  let v = 0;
  let a = 1;
  let f = base;
  for (let i = 0; i < 3; i++) {
    v += a * Math.sin(2 * Math.PI * f * t + seed * (i + 1) * 2.399 + i * 1.3);
    a *= 0.45;
    f *= phi * 1.17;
  }
  return (v / 1.65) * amp;
}

// Envelope: 0 before a, rises smoothly to 1 at b, stays 1 until c, falls to 0 at d
export function envelope(t, a, b, c = Infinity, d = Infinity) {
  if (t <= a || t >= d) return 0;
  if (t < b) return smoother((t - a) / (b - a));
  if (t <= c) return 1;
  return smoother((d - t) / (d - c));
}

// Monotone cubic Hermite spline through [t, v] keys (Fritsch–Carlson):
// C1-continuous velocity through every key, never overshoots between keys.
// Ideal for camera dolly curves (no stop-start at intermediate keys).
export function smoothTrack(keys) {
  const n = keys.length;
  const ts = keys.map((k) => k[0]), vs = keys.map((k) => k[1]);
  const d = [], m = new Array(n).fill(0);
  for (let i = 0; i < n - 1; i++) d.push((vs[i + 1] - vs[i]) / (ts[i + 1] - ts[i]));
  for (let i = 1; i < n - 1; i++) m[i] = d[i - 1] * d[i] <= 0 ? 0 : (d[i - 1] + d[i]) / 2;
  for (let i = 0; i < n - 1; i++) {
    if (d[i] === 0) { m[i] = m[i + 1] = 0; continue; }
    const a = m[i] / d[i], b = m[i + 1] / d[i];
    const s = a * a + b * b;
    if (s > 9) { const k = 3 / Math.sqrt(s); m[i] = k * a * d[i]; m[i + 1] = k * b * d[i]; }
  }
  return (t) => {
    if (t <= ts[0]) return vs[0];
    if (t >= ts[n - 1]) return vs[n - 1];
    let i = 0;
    while (t > ts[i + 1]) i++;
    const h = ts[i + 1] - ts[i], u = (t - ts[i]) / h;
    const h00 = 2 * u * u * u - 3 * u * u + 1, h10 = u * u * u - 2 * u * u + u;
    const h01 = -2 * u * u * u + 3 * u * u, h11 = u * u * u - u * u;
    return h00 * vs[i] + h10 * h * m[i] + h01 * vs[i + 1] + h11 * h * m[i + 1];
  };
}

// v4 PERFORMANCE ENGINE — layered, physically-settled character animation (deterministic).
//
// Layer 1  primary acting   : key poses per body track (armL, armR, torso, head, root) authored on
//                              word timings, eased between holds (with automatic anticipation).
// Layer 2  follow-through   : every bone channel is driven by its own damped spring that chases the
//                              key-pose target (shoulders lead, forearms lag, hands overshoot & settle).
// Layer 3  dialogue head    : small nods on stressed syllables measured from the VO energy.
// Layer 4  lip sync         : audio-driven mouth (phone visemes x VO energy envelope, low-passed).
// Layer 5  secondary/idle   : breathing + slow value-noise weight shift, blinks.
// Everything is precomputed once at load at 120 Hz and sampled by time -> seek-safe & reproducible.

const HZ = 120;
const clamp01 = (x) => Math.max(0, Math.min(1, x));
const smoother = (u) => u * u * u * (u * (u * 6 - 15) + 10);
const anticK = (k) => (u) => smoother(u) - (u < 0.32 ? k * Math.sin((Math.PI * u) / 0.32) : 0);

// ------------------------------------------------------------------ value noise (smooth, seeded)
function hash(i, seed) {
  let h = (i * 374761393 + seed * 668265263) | 0;
  h = Math.imul(h ^ (h >>> 13), 1274126177);
  return ((h ^ (h >>> 16)) >>> 0) / 4294967295;
}
export function vnoise(t, seed = 1, freq = 0.35) {
  const x = t * freq, i = Math.floor(x), f = x - i;
  const a = hash(i, seed) * 2 - 1, b = hash(i + 1, seed) * 2 - 1;
  return a + (b - a) * smoother(f);
}

// ------------------------------------------------------------------ pose library (added to REST)
export const REST = {
  upperarm_L: [0.02, 0, -0.16], upperarm_R: [0.02, 0, 0.16],
  forearm_L: [-0.32, 0, 0.06], forearm_R: [-0.32, 0, -0.06],
  hand_L: [0, -0.1, 0.05], hand_R: [0, 0.1, -0.05],
};
// arm poses are written for his RIGHT arm (screen-left); mirror() makes the left-arm version
export const ARM = {
  rest: { upperarm: [0, 0, 0], forearm: [0, 0, 0], hand: [0, 0, 0] },
  low: { upperarm: [-0.08, 0, 0.04], forearm: [-0.18, 0, 0.05], hand: [0, 0.1, 0] },
  explain: { upperarm: [-0.6, 0, 0.15], forearm: [-1.3, 0, 0.4], hand: [0, 0.15, 0] },
  explainHi: { upperarm: [-0.85, 0, 0.05], forearm: [-1.45, 0, 0.45], hand: [0.2, 0.1, 0] },
  together: { upperarm: [-0.7, 0.2, 0.1], forearm: [-1.4, 0.3, 0.5], hand: [0.2, 0.3, 0] },
  palmUp: { upperarm: [-0.6, 0.3, -0.1], forearm: [-1.2, 0.4, 0], hand: [0, 0.4, 0] },
  open: { upperarm: [-0.6, 0.3, -0.1], forearm: [-1.2, 0.4, 0], hand: [0, 0.4, 0] },
  point: { upperarm: [-0.95, -0.05, -0.45], forearm: [-0.35, 0, -0.15], hand: [0, 0, -0.1] },     // v6: forward-side (no wide abduction: suit seam)
  pointUp: { upperarm: [-1.1, 0, -0.35], forearm: [-0.95, 0, -0.25], hand: [0, 0, -0.15] },
  present: { upperarm: [-0.75, 0.05, -0.45], forearm: [-0.55, 0.2, -0.2], hand: [0.05, 0.55, -0.35] },
  stop: { upperarm: [-0.8, 0, -0.4], forearm: [-0.7, 0, -0.6], hand: [0, 0.2, -0.1] },
  wave: { upperarm: [-0.85, 0, -0.25], forearm: [-1.45, 0, -0.35], hand: [0, 0, 0.15] },
  chin: { upperarm: [-0.85, 0, 0.05], forearm: [-1.45, 0, 0.45], hand: [0.2, 0.1, 0] },
  shrug: { upperarm: [-0.6, 0.3, -0.1], forearm: [-1.2, 0.4, 0], hand: [0, 0.5, 0] },
  fist: { upperarm: [-0.35, 0.1, -0.35], forearm: [-1.35, 0.2, -0.15], hand: [0.3, 0.2, -0.1] },
};
const mirror = (v) => [v[0], -v[1], -v[2]];
function armBones(side, name, w = 1) {
  const p = typeof name === 'string' ? ARM[name] : name;
  const m = side === 'L' ? mirror : (v) => v;
  return {
    ['upperarm_' + side]: m(p.upperarm).map((x) => x * w),
    ['forearm_' + side]: m(p.forearm).map((x) => x * w),
    ['hand_' + side]: m(p.hand).map((x) => x * w),
  };
}

// ------------------------------------------------------------------ springs per bone (ω rad/s, ζ)
const SPRING = {
  hips: [7, 0.9], spine: [6.5, 0.85], chest: [7.5, 0.8], neck: [9, 0.85], head: [10, 0.72],
  shoulder_L: [12, 0.85], shoulder_R: [12, 0.85],
  upperarm_L: [13, 0.78], upperarm_R: [13, 0.78], forearm_L: [11.5, 0.62], forearm_R: [11.5, 0.62],
  hand_L: [10, 0.5], hand_R: [10, 0.5],
  root: [13, 0.9],
};
const ROOT_KEYS = ['x', 'y', 'ry', 'rz', 's'];

// tracks: { armL:[[t, pose, dur?]], armR:[...], torso:[[t, {spine,chest,hips}, dur]], head:[[t,[rx,ry,rz],dur]], root:[[t,{x,y,ry,rz,s},dur]] }
// returns sampler(t) -> { bones, root }
export function buildPerformance(tracks, D, opts = {}) {
  const N = Math.ceil(D * HZ) + 2;
  // opts.smooth 0..1: softer, better-damped springs (less overshoot / wobble), longer eased transitions and a
  // smaller anticipation dip -> calmer, silkier acting. 0 = original v4 behaviour.
  const SM = Math.max(0, Math.min(1, opts.smooth || 0));
  const antic = anticK(0.1 * (1 - 0.7 * SM));
  const soft = (sp) => [sp[0] * (1 - 0.28 * SM), Math.min(1, sp[1] + (1 - sp[1]) * 0.6 * SM)];
  const ch = new Map(); // name -> { tgt: Float32Array, out: Float32Array, spring }
  const chan = (name, spring) => {
    if (!ch.has(name)) ch.set(name, { tgt: new Float32Array(N), out: new Float32Array(N), spring });
    return ch.get(name);
  };
  // generic eased-hold evaluator for one track: keys [[t, valueDict, dur, ease?]]
  function fillTrack(keys, toDict, base) {
    keys = keys.slice().sort((a, b) => a[0] - b[0]);
    // automatic anticipation: a short counter-move before big changes (arms only)
    const names = new Set();
    for (const k of keys) for (const n of Object.keys(toDict(k[1]))) names.add(n);
    for (const n of names) {
      const bone = n.split('.')[0];
      const sp = SPRING[bone] || SPRING.root;
      const c = chan(n, soft(sp));
      let prevV = base(n), kk = 0;
      let curFrom = prevV, curTo = prevV, t0 = -1, t1 = -1, ease = smoother;
      const isArm = /^(upperarm|forearm)_/.test(bone);
      for (let i = 0; i < N; i++) {
        const t = i / HZ;
        while (kk < keys.length && keys[kk][0] <= t) {
          const v = toDict(keys[kk][1])[n];
          const val = v === undefined ? base(n) : v;
          const now = t1 > t0 && t < t1 ? curFrom + (curTo - curFrom) * ease(clamp01((t - t0) / (t1 - t0))) : curTo;
          curFrom = now; curTo = val; t0 = keys[kk][0]; t1 = t0 + (keys[kk][2] || 0.35) * (1 + 0.4 * SM);
          // anticipation: big arm moves start with a small counter-move (10%) before committing
          ease = isArm && Math.abs(curTo - curFrom) > 0.4 ? antic : smoother;
          kk++;
        }
        const v = t1 > t0 && t < t1 ? curFrom + (curTo - curFrom) * ease(clamp01((t - t0) / (t1 - t0))) : curTo;
        c.tgt[i] = v;
      }
    }
  }
  const flat = (bones) => {
    const o = {};
    for (const [b, v] of Object.entries(bones)) { o[b + '.x'] = v[0]; o[b + '.y'] = v[1]; o[b + '.z'] = v[2]; }
    return o;
  };
  const restBase = (n) => {
    const [b, a] = n.split('.');
    const r = REST[b];
    return r ? r['xyz'.indexOf(a)] : 0;
  };
  const withRest = (dict) => {
    const o = {};
    for (const [k, v] of Object.entries(dict)) o[k] = v + restBase(k);
    return o;
  };
  if (tracks.armL) fillTrack(tracks.armL, (p) => withRest(flat(armBones('L', p))), restBase);
  if (tracks.armR) fillTrack(tracks.armR, (p) => withRest(flat(armBones('R', p))), restBase);
  if (tracks.torso) fillTrack(tracks.torso, (p) => flat(p), () => 0);
  if (tracks.head) fillTrack(tracks.head, (p) => flat({ head: p, neck: [p[0] * 0.35, p[1] * 0.35, p[2] * 0.25] }), () => 0);
  if (tracks.root) fillTrack(tracks.root, (p) => { const o = {}; for (const k of ROOT_KEYS) if (p[k] !== undefined) o['root.' + k] = p[k]; return o; }, (n) => (n === 'root.s' ? 1 : 0));
  // springs (semi-implicit Euler, 4 substeps per sample)
  for (const [name, c] of ch) {
    const [w, z] = c.spring;
    let x = c.tgt[0], v = 0;
    const dt = 1 / HZ / 4;
    for (let i = 0; i < N; i++) {
      const g = c.tgt[i];
      for (let s = 0; s < 4; s++) { v += (w * w * (g - x) - 2 * z * w * v) * dt; x += v * dt; }
      c.out[i] = x;
    }
  }
  const names = [...ch.keys()];
  return function sample(t) {
    const f = Math.max(0, Math.min(N - 1.001, t * HZ)), i = Math.floor(f), u = f - i;
    const bones = {}, root = { x: 0, y: 0, ry: 0, rz: 0, s: 1 };
    for (const n of names) {
      const c = ch.get(n), v = c.out[i] + (c.out[i + 1] - c.out[i]) * u;
      const [b, a] = n.split('.');
      if (b === 'root') { root[a] = v; continue; }
      const bb = bones[b] || (bones[b] = [restBase(b + '.x'), restBase(b + '.y'), restBase(b + '.z')]);
      bb['xyz'.indexOf(a)] = v;
    }
    for (const b of Object.keys(REST)) if (!bones[b]) bones[b] = REST[b].slice();
    return { bones, root };
  };
}

// ------------------------------------------------------------------ audio-driven lip sync
// phones: [[char, start, end, wordIdx]] (CTC forced alignment), env: 100 Hz 0..99 (= -60..0 dB)
// Mouth = (halfWidth, open, smile, tongue). Openness follows the real audio energy (cannot run ahead
// of the VO), shape follows the aligned vowel / closure phones with ~50 ms coarticulation, then a
// critically-damped low-pass removes jitter so the jaw never flaps faster than syllables.
const VIS = {
  rest: [0.03, 0.0, 0.007, 0.0],
  a: [0.04, 0.034, 0.005, 0.55], e: [0.044, 0.019, 0.005, 0.3], i: [0.045, 0.012, 0.006, 0.2],
  o: [0.025, 0.03, 0.001, 0.35], u: [0.02, 0.02, 0.0, 0.25],
};
const CLOSE = new Set(['m', 'b', 'p']);
const ROUND = new Set(['w', 'u', 'o']);
export function buildLipTrack(phones, env, D, opts = {}) {
  const N = Math.ceil(D * HZ) + 2;
  const SM = Math.max(0, Math.min(1, opts.smooth || 0));   // 1 = softer, rounder lip motion (lower low-pass corners)
  const W = new Float32Array(N), O = new Float32Array(N), Sm = new Float32Array(N), T = new Float32Array(N);
  const envAt = (t) => {
    const f = t * 100, i = Math.max(0, Math.min(env.length - 2, Math.floor(f))), u = f - i;
    return (env[i] + (env[i + 1] - env[i]) * u) / 99; // 0..1 (-60..0 dB)
  };
  // speech energy -> openness 0..1 (gate below ~-42 dB, saturate near -14 dB)
  const openFromEnv = (t) => clamp01((envAt(t) * 60 - 60 + 42) / 28);
  const vowels = phones.filter((p) => 'aeiou'.includes(p[0]));
  const closures = phones.filter((p) => CLOSE.has(p[0]));
  let vi = 0;
  for (let k = 0; k < N; k++) {
    const t = k / HZ;
    // shape: gaussian-weighted blend of nearby vowels (coarticulation)
    while (vi < vowels.length - 1 && vowels[vi + 1][1] < t - 0.25) vi++;
    let ws = 0, acc = [0, 0, 0, 0];
    for (let j = Math.max(0, vi - 2); j < Math.min(vowels.length, vi + 6); j++) {
      const p = vowels[j], c = (p[1] + Math.min(p[2], p[1] + 0.16)) / 2;
      const w = Math.exp(-((t - c) ** 2) / (2 * 0.055 ** 2));
      if (w < 1e-4) continue;
      const v = VIS[p[0]];
      for (let q = 0; q < 4; q++) acc[q] += v[q] * w;
      ws += w;
    }
    let shape = ws > 1e-3 ? acc.map((x) => x / ws) : VIS.rest.slice();
    const sp = clamp01(ws * 1.5);
    shape = shape.map((x, q) => VIS.rest[q] + (x - VIS.rest[q]) * sp);
    // openness: vowel shape opening x measured audio energy
    let open = shape[1] * (0.25 + 1.0 * openFromEnv(t));
    // bilabial closures press the lips together (only while the phone is actually sounding)
    for (const c of closures) {
      if (t > c[1] - 0.05 && t < c[2] + 0.02) { const m = Math.min(1, (t - (c[1] - 0.05)) / 0.04, (c[2] + 0.02 - t) / 0.04); open *= 1 - 0.9 * clamp01(m); }
    }
    if (openFromEnv(t) < 0.02 && ws < 0.15) open = 0;
    W[k] = shape[0]; O[k] = open; Sm[k] = shape[2]; T[k] = shape[3];
  }
  // critically-damped low-pass (ω≈34 rad/s ≈ 5.4 Hz) on openness/width: no flapping, no lag > 1 frame
  const lp = (arr, w) => {
    let x = arr[0], v = 0; const dt = 1 / HZ;
    for (let k = 0; k < arr.length; k++) { v += (w * w * (arr[k] - x) - 2 * w * v) * dt; x += v * dt; arr[k] = x; }
  };
  // zero-phase: forward + backward pass (no time shift relative to the audio)
  const zp = (arr, w) => { lp(arr, w); arr.reverse(); lp(arr, w); arr.reverse(); };
  zp(O, 60 - 22 * SM); zp(W, 44 - 14 * SM); zp(Sm, 30 - 8 * SM); zp(T, 30 - 8 * SM);
  return function mouthAt(t) {
    const f = Math.max(0, Math.min(N - 1.001, t * HZ)), i = Math.floor(f), u = f - i;
    const g = (a) => a[i] + (a[i + 1] - a[i]) * u;
    return [g(W), Math.max(0, g(O)), g(Sm), g(T)];
  };
}

// stressed-syllable accents from the VO energy (for head nods / hand beats): returns [[t, strength]]
export function syllableAccents(env, words, phones, D) {
  const out = [];
  const keyWords = new Set(words.filter((w) => w[3]).map((w) => w[1]));
  for (const w of words) {
    const my = phones.filter((p) => p[1] >= w[1] - 0.01 && p[1] < w[2] && 'aeiou'.includes(p[0]));
    if (!my.length) continue;
    // stress ~ first vowel of keywords, strongest-energy vowel otherwise
    let best = my[0], be = -1;
    for (const p of my) { const e = env[Math.min(env.length - 1, Math.round((p[1] + 0.03) * 100))]; if (e > be) { be = e; best = p; } }
    const isKey = keyWords.has(w[1]);
    out.push([isKey ? my[0][1] : best[1], isKey ? 1 : 0.35 * clamp01((be - 55) / 25)]);
  }
  return out.filter((a) => a[1] > 0.05 && a[0] < D);
}

// v7 ACTING DIRECTOR — reusable, deterministic character acting for the AI PRENEUR suit mascot.
//
// Why: the old talk pattern changed a both-hands-up pose every 2 words and turned the head left/right on every
// word -> floating arms, waving silhouettes, metronome head. Measured on the rig: elbow flexion alone swings the
// forearm sideways in the camera plane (palm to camera = "waving"); a believable explaining hand needs humeral
// twist (upperarm y ~ +1.2..1.5) so the forearm comes FORWARD in front of the body, palm turned up (hand y < 0).
//
// Model: one intentional gesture per spoken phrase (not per word), usually ONE hand with the other relaxed,
// chosen from the line's meaning, never the same action twice in a row, alternating the leading hand.
// Every gesture: eyes lead (-0.22 s) -> head (-0.14 s) -> chest -> arm (spring chain: shoulder leads, forearm lags,
// hand overshoots) -> apex on the stressed word -> settle (60 %) -> rest if the next idea is > 1 s away.
// Some phrases deliberately get no arm move (stillness reads as confidence).
// Output feeds buildPerformance(); gaze(t) feeds the eye shader; blinks are placed on big head turns.
//
// Directions are in SCREEN terms: 'left' = screen-left = his right arm (R).

// ---------------------------------------------------------------- pose library (his RIGHT arm, added to REST)
// u = upperarm [flex(-)=raise, twist(+)=forearm forward, abduct(-)=out], f = forearm [x=-flex], h = hand
// [x: +flex/-extend, y: -=palm up, z: +=toward body]. Mirrored for the left arm by perform.js.
const P = (u, f, h) => ({ upperarm: u, forearm: f, hand: h });
export const POSE = {
  rest: P([0, 0.45, 0.02], [-0.32, 0, 0], [0, 0.15, 0]),
  restIn: P([-0.05, 0.9, 0.12], [-0.62, 0, 0], [0, 0.05, 0.12]),           // hand relaxed in front of the hip
  explain: P([-0.15, 1.3, -0.12], [-1.35, 0, 0], [0, -0.6, 0]),            // forearm forward, palm up-in
  explain2: P([-0.22, 1.18, -0.24], [-1.15, 0, 0], [0.12, -0.8, -0.05]),   // same idea, opened a little
  open: P([-0.25, 1.1, -0.35], [-1.2, 0, 0], [0, -0.9, -0.1]),             // open palm to the side
  present: P([-0.35, 0.9, -0.5], [-0.6, 0, 0], [0, -0.9, -0.2]),           // arm extended, offering
  presentLow: P([-0.2, 0.85, -0.45], [-0.45, 0, 0], [0.1, -0.9, -0.2]),    // offering toward lower screen (CTA)
  point: P([-0.95, -0.05, -0.45], [-0.35, 0, -0.15], [-0.1, 0, -0.1]),     // directing to his side
  pointFwd: P([-0.7, 0.9, -0.25], [-0.5, 0, 0], [-0.25, 0, 0]),            // directing forward-up
  think: P([-0.5, 1.4, 0.3], [-2.15, 0, 0], [-0.2, 0, 0.2]),               // hand up near the chin
  beat: P([-0.1, 1.3, -0.05], [-1.6, 0, 0], [0.3, -0.3, 0]),               // emphasis: forearm forward, wrist down
  heart: P([-0.1, 1.5, 0.35], [-1.9, 0, 0], [0, 0, 0.5]),                  // hand on chest
  shrug: P([-0.05, 0.9, -0.35], [-1.4, 0, 0], [0, -1.0, -0.2]),            // palm up, elbow tucked
  welcome: P([-0.4, 0.8, -0.55], [-0.9, 0, 0], [0, -0.8, -0.2]),           // open arm, welcoming
  hold: P([-0.25, 1.45, 0.1], [-1.5, 0, 0], [0, -0.4, 0.3]),               // both hands framing an object
};
const scale = (p, k, base = POSE.rest) => {
  const o = {};
  for (const b of ['upperarm', 'forearm', 'hand']) o[b] = p[b].map((v, i) => base[b][i] + (v - base[b][i]) * k);
  return o;
};

// ---------------------------------------------------------------- action library
// dom: arm poses for the leading hand: [[dt, pose, dur]] relative to the apex time; off: the other hand
// head: [rx(nod-), ryTowardSide, rz(tilt)] ; chest: y toward side ; gaze: [x toward side, y up]
export const ACTIONS = {
  idle: { dom: [], off: [], head: [0, 0, 0], chest: 0, gaze: [0, 0] },
  explain: { dom: [[-0.3, 'explain', 0.42], [0.55, 'explain2', 0.5]], off: [[-0.2, 'restIn', 0.55]], head: [-0.03, 0.05, 0.03], chest: 0.05, gaze: [0, 0] },
  present: { dom: [[-0.32, 'present', 0.48]], off: [[-0.2, 'restIn', 0.5]], head: [0.0, 0.16, 0.04], chest: 0.08, gaze: [0.6, 0.1], look: 0.55 },
  point: { dom: [[-0.34, 'point', 0.42]], off: [[-0.25, 'rest', 0.5]], head: [0.02, 0.24, 0.02], chest: 0.1, gaze: [1, 0.15], look: 0.6 },
  pointFwd: { dom: [[-0.3, 'pointFwd', 0.42]], off: [[-0.25, 'restIn', 0.5]], head: [0.04, 0.08, 0.02], chest: 0.05, gaze: [0.4, 0.4], look: 0.5 },
  thinking: { dom: [[-0.4, 'think', 0.55]], off: [[-0.3, 'restIn', 0.55]], head: [0.05, -0.08, 0.09], chest: -0.03, gaze: [-0.5, 0.7], look: 0.7 },
  emphasize: { dom: [[-0.28, 'explain', 0.32], [0.0, 'beat', 0.16], [0.3, 'explain2', 0.4]], off: [[-0.2, 'restIn', 0.5]], head: [-0.07, 0.03, 0], chest: 0.06, gaze: [0, 0], nod: 1 },
  compare: { dom: [[-0.3, 'open', 0.42]], off: [[0.75, 'open', 0.45]], offFirst: [[-0.2, 'restIn', 0.4]], head: [0, 0.14, 0.03], chest: 0.08, gaze: [0.5, 0], swap: 0.75 },
  question: { dom: [[-0.3, 'shrug', 0.45]], off: [[-0.18, 'shrug', 0.5, 0.75]], head: [0.03, 0.04, 0.11], chest: 0, gaze: [0.2, 0.25] },
  reveal: { dom: [[-0.55, 'hold', 0.3], [-0.1, 'welcome', 0.38]], off: [[-0.5, 'hold', 0.32], [-0.04, 'present', 0.42, 0.85]], head: [0.04, 0.03, 0], chest: 0.02, gaze: [0, 0.1] },
  confident: { dom: [[-0.35, 'heart', 0.5]], off: [[-0.25, 'restIn', 0.5]], head: [-0.05, 0.02, -0.03], chest: -0.02, gaze: [0, 0], nod: 1 },
  welcome: { dom: [[-0.35, 'welcome', 0.48]], off: [[-0.2, 'restIn', 0.5]], head: [0.02, 0.1, 0.07], chest: 0.06, gaze: [0, 0] },
  cta: { dom: [[-0.35, 'presentLow', 0.5]], off: [[-0.2, 'restIn', 0.5]], head: [-0.04, 0.12, 0.03], chest: 0.07, gaze: [0.5, -0.5], look: 0.45, nod: 1 },
};

// ---------------------------------------------------------------- line -> action (Indonesian cues)
const CUE = [
  [/\b(kenapa|gimana|bagaimana|apakah|apa iya|masa)\b|\?/, 'question'],
  [/\b(jangan|bukan|belum|gak|nggak|tidak|tanpa)\b/, 'emphasize'],
  [/\b(pertama|kedua|ketiga|sementara|beda|dibanding|vs)\b/, 'compare'],
  [/\b(lihat|ini dia|perhatiin|cek|buka)\b/, 'present'],
  [/\b(komen|follow|klik|save|share|link|checklist|kirim)\b/, 'cta'],
  [/\b(jadi|intinya|kuncinya|ingat)\b/, 'confident'],
  [/\b(sebenarnya|ternyata|rahasia|dibedah)\b/, 'reveal'],
  [/\b(mikir|kira|mungkin|bayangin)\b/, 'thinking'],
];
const ROTATION = ['explain', 'present', 'explain', 'pointFwd', 'thinking', 'explain', 'welcome'];

const ss = (u) => { u = Math.max(0, Math.min(1, u)); return u * u * (3 - 2 * u); };

// words: [[text, start, end, keyword?], ...] (VO_WORDS). opts: { intents:[{t, action, side:'left'|'right', until?}],
// seed, quiet: 0..1 share of still phrases (default .28), headSign/gazeSign: rig yaw convention, energy: 0..1.3 }
export function direct(words, D, opts = {}) {
  const W = words.map((w) => ({ text: String(w[0]), s: w[1], e: w[2], key: !!w[3] }));
  const phrases = [];
  for (const w of W) {
    const last = phrases[phrases.length - 1];
    const endsSentence = last && /[.!?,;:]$/.test(last.words[last.words.length - 1].text);
    if (!last || w.s - last.e > 0.2 || (endsSentence && w.s - last.e > 0.08)) phrases.push({ s: w.s, e: w.e, words: [w] });
    else { last.words.push(w); last.e = w.e; }
  }
  const HS = opts.headSign ?? 1, GS = opts.gazeSign ?? 1, EN = opts.energy ?? 1;
  const quiet = opts.quiet ?? 0.28;
  const intents = (opts.intents || []).slice().sort((a, b) => a.t - b.t);
  const tracks = { armL: [[0, 'rest', 0.4]], armR: [[0, 'rest', 0.4]], head: [[0, [0, 0, 0], 0.4]], torso: [[0, {}, 0.4]], root: [[0, { x: 0, y: 0, ry: 0, rz: 0 }, 0.4]] };
  const gazeKeys = [[0, 0, 0]], blinks = [], plan = [];
  let lastAct = '', lastSide = 'right', rot = (opts.seed || 0) % ROTATION.length, quietAcc = 0.5, weight = 1;
  const armKey = (side, t, name, dur, k = 1) => tracks[side === 'left' ? 'armR' : 'armL'].push([t, typeof name === 'string' ? (k === 1 ? POSE[name] : scale(POSE[name], k)) : name, dur]);
  phrases.forEach((ph, pi) => {
    const text = ph.words.map((w) => w.text).join(' ').toLowerCase();
    const dur = ph.e - ph.s;
    // apex = the stressed word: first caption keyword, else the 2nd word (Indonesian stress lands early in the line)
    const kw = ph.words.find((w) => w.key) || ph.words[Math.min(1, ph.words.length - 1)];
    const apex = kw.s + 0.06;
    const it = intents.find((x) => x.t <= ph.e && (x.until ?? x.t + 0.01) >= ph.s - 0.3);
    let act = it?.action;
    if (!act) {
      for (const [re, a] of CUE) if (re.test(text)) { act = a; break; }
      if (pi === 0 && !act) act = 'welcome';
      if (pi === phrases.length - 1 && !act) act = 'confident';
      if (!act) { act = ROTATION[rot % ROTATION.length]; rot++; }
      if (act === lastAct) { act = ROTATION[rot % ROTATION.length]; rot++; if (act === lastAct) { act = ROTATION[rot % ROTATION.length]; rot++; } }
      // stillness: short lines and a share of plain explanatory lines keep the hands down (head + face only)
      quietAcc += quiet;
      if (dur < 0.55 || (act === 'explain' && quietAcc >= 1 && pi > 0)) { act = 'idle'; quietAcc -= 1; }
    }
    let side = it?.side || (lastSide === 'left' ? 'right' : 'left');
    if (!it?.side && (pi % 5 === 3)) side = lastSide;   // sometimes the same hand twice (people have a favourite hand)
    const A = ACTIONS[act] || ACTIONS.explain;
    const sgn = side === 'left' ? -1 : 1;              // screen direction of the gesture
    const offSide = side === 'left' ? 'right' : 'left';
    const k = Math.min(1.15, (0.82 + 0.18 * Math.min(1, dur / 2.2)) * EN);
    // arms
    for (const [dt, name, d, kk] of A.dom) armKey(side, apex + dt, name, d, k * (kk || 1));
    const offList = act === 'compare' ? [...(A.offFirst || []), ...A.off] : A.off;
    for (const [dt, name, d, kk] of offList) armKey(offSide, apex + dt, name, d, (kk || 1) * (name === 'restIn' ? 1 : k));
    const end = Math.max(ph.e, apex + 0.6);
    const next = phrases[pi + 1];
    const gap = next ? next.s - end : D - end;
    if (act !== 'idle') {
      // settle: the hand drops to 55-65% of the gesture while the line finishes, then rests if there is room
      const lastDom = A.dom[A.dom.length - 1];
      armKey(side, end + 0.1, lastDom[1], 0.5, 0.6 * k);
      if (gap > 1.0 || !next) { armKey(side, end + 0.55, 'rest', 0.6); armKey(offSide, end + 0.5, 'rest', 0.6); }
    } else if (gap > 1.2) { armKey('left', end + 0.3, 'rest', 0.6); armKey('right', end + 0.35, 'rest', 0.6); }
    // head leads the arm; nods on keywords; returns toward camera while still talking
    const [hx, hy, hz] = A.head;
    const lead = apex - 0.42;
    tracks.head.push([lead, [hx * EN, HS * sgn * hy * EN, sgn * hz * EN], 0.38]);
    if (A.look) tracks.head.push([apex + A.look, [hx * 0.4, HS * sgn * hy * 0.3, sgn * hz * 0.5], 0.5]);
    for (const w of ph.words) if (w.key || A.nod) {
      if (w.s < apex - 0.1) continue;
      tracks.head.push([w.s - 0.05, [hx + 0.07 * (A.nod ? 1 : 0.6), HS * sgn * hy * 0.5, sgn * hz * 0.6], 0.16]);
      tracks.head.push([w.s + 0.16, [hx * 0.6, HS * sgn * hy * 0.45, sgn * hz * 0.5], 0.3]);
      if (!A.nod) break;
    }
    if (act === 'emphasize' && /\b(jangan|bukan|gak|nggak|tidak)\b/.test(text)) {   // small "no" head shake
      const t0 = apex - 0.05;
      [[0, 0.07], [0.16, -0.07], [0.32, 0.04], [0.46, 0]].forEach(([d, y]) => tracks.head.push([t0 + d, [hx, HS * y, 0], 0.15]));
    }
    if (gap > 0.7) tracks.head.push([end + 0.2, [0, 0, 0], 0.6]);
    if (Math.abs(hy) > 0.12) blinks.push(lead + 0.02);                          // people blink on big head turns
    // eyes lead the head
    const [gx, gy] = A.gaze;
    gazeKeys.push([lead - 0.12, GS * sgn * gx, gy]);
    if (A.look) gazeKeys.push([apex + A.look - 0.1, 0, 0]);
    if (A.swap) { gazeKeys.push([apex + A.swap - 0.12, -GS * sgn * gx, gy]); tracks.head.push([apex + A.swap - 0.08, [hx, -HS * sgn * hy * 0.8, -sgn * hz], 0.4]); }
    if (gap > 0.6) gazeKeys.push([end + 0.1, 0, 0]);
    // torso follows the arm (chest toward the gesture), weight shifts between lines
    const ch = A.chest * EN;
    tracks.torso.push([apex - 0.3, { chest: [0.02 * EN, HS * sgn * ch, sgn * 0.015], spine: [0.015, HS * sgn * ch * 0.4, 0], hips: [0, 0, 0] }, 0.5]);
    if (A.swap) tracks.torso.push([apex + A.swap - 0.1, { chest: [0.02, -HS * sgn * ch, -sgn * 0.015], spine: [0.015, -HS * sgn * ch * 0.4, 0] }, 0.5]);
    if (gap > 0.7) tracks.torso.push([end + 0.25, {}, 0.7]);
    if (pi % 3 === 0 && dur > 1.2) { weight = -weight; tracks.root.push([ph.s + 0.1, { x: 0.004 * weight, y: 0, ry: 0, rz: 0.012 * weight }, 1.1]); }
    plan.push({ t: +ph.s.toFixed(2), apex: +apex.toFixed(2), act, side, text });
    lastAct = act; if (act !== 'idle') lastSide = side;
  });
  tracks.root.push([Math.max(0, D - 1.2), { x: 0, y: 0, ry: 0, rz: 0 }, 1]);
  for (const k of Object.keys(tracks)) tracks[k].sort((a, b) => a[0] - b[0]);
  // gaze: smooth eased steps; eye radius units -> shader offset (x 0.006 max, y 0.004)
  gazeKeys.sort((a, b) => a[0] - b[0]);
  function gaze(t) {
    let i = 0; while (i < gazeKeys.length - 1 && gazeKeys[i + 1][0] <= t) i++;
    const a = gazeKeys[i], prev = gazeKeys[i - 1] || a;
    const u = ss((t - a[0]) / 0.14);
    const x = prev[1] + (a[1] - prev[1]) * u, y = prev[2] + (a[2] - prev[2]) * u;
    return [0.0036 * x, 0.0026 * y];
  }
  return { tracks, gaze, blinks, plan };
}

// restrained always-on life: breathing, shoulder settle, slow weight shift (amplitudes small on purpose)
export function micro(t, seed = 7, vnoise) {
  const br = Math.sin(t * 2 * Math.PI * 0.23);
  const n = (s, f) => (vnoise ? vnoise(t, seed + s, f) : 0);
  return {
    chest: [0.014 * br, 0.01 * n(1, 0.17), 0],
    spine: [0.006 * br, 0.012 * n(2, 0.13), 0.01 * n(3, 0.11)],
    shoulder_L: [0, 0, -0.012 * br], shoulder_R: [0, 0, 0.012 * br],
    head: [0.008 * n(4, 0.21), 0.018 * n(5, 0.15), 0.01 * n(6, 0.19)],
  };
}

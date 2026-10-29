// MasterPajak AI — website preview walkthrough. 10.0 s @ 60 fps, 1920x1080.
// Everything is a pure function of time: seek(t) sets every style, so any frame renders identically.
import { EASE, bezier, smoothTrack, springTo, spring, remap, lerp, clamp, smoother, drift, envelope } from './motion.js';

const $ = (id) => document.getElementById(id);
const DUR = 10.0;
const CHROME = 44;
const SCROLL_MAX = 430;

// ---------------- timing (seconds) ----------------
const T = {
  enter: [0.0, 1.35],
  f1: { click: 2.1, out: 3.3 },
  f2: { click: 4.2, out: 5.15 },
  scroll: [5.2, 6.55],
  f3: { click: 7.15, out: 8.25 },
  cta: 9.1,
};

const FEATURES = {
  f1: { tag: 'FITUR 01', title: 'Hitung pajak gratis', desc: 'Coba kalkulator pajak MasterPajak AI langsung dari website, gratis.' },
  f2: { tag: 'FITUR 02', title: 'Foto nota → siap Coretax', desc: 'Unggah foto nota. AI membukukan, menghitung pajak, dan menyiapkan laporan siap unggah ke Coretax, 24/7.' },
  f3: { tag: 'FITUR 03', title: 'Master, asisten pajak AI', desc: 'Konsultan pajak 24 jam dengan harga ratusan ribu, siap menjawab kapan saja.' },
};

let R = {}; // page-space rects measured once

function measure() {
  const page = $('page').getBoundingClientRect();
  const nav = $('nav').getBoundingClientRect();
  const rel = (id, base = page) => { const r = $(id).getBoundingClientRect(); return { x: r.left - base.left, y: r.top - base.top, w: r.width, h: r.height }; };
  R.calc = rel('b-calc');
  R.c2 = rel('c2');
  R.robot = { x: 555, y: 878, w: 330, h: 400 };
  R.nav = rel('b-nav', nav);
}

// window-space point of a page-space point at scroll s
const W = (x, y, s) => ({ x, y: CHROME + y - s });

const scrollEase = bezier(0.38, 0.0, 0.12, 1.0); // momentum: brisk start, long settle
const scrollAt = (t) => SCROLL_MAX * scrollEase(remap(t, T.scroll[0], T.scroll[1]));

// ---------------- camera (one continuous spline per channel) ----------------
// keys: [t, focusX, focusY, focusAmount, zoom, rotX, rotY]
const CAM = [
  [0.0, 720, 472, 0, 1.0, 4, -6],
  [1.25, 720, 470, 0.1, 1.02, 3, -4],
  [2.05, 560, 498, 0.9, 1.42, 2, -2.5],
  [3.15, 566, 496, 0.9, 1.46, 2, -1.5],
  [3.95, 520, 590, 0.9, 1.42, 2.5, -3],
  [5.0, 526, 588, 0.9, 1.46, 2.5, -2.5],
  [5.85, 720, 520, 0.45, 1.06, 4, 1.5],
  [6.95, 760, 660, 0.88, 1.3, 2, 3],
  [8.15, 764, 658, 0.88, 1.34, 2, 3.5],
  [8.95, 880, 360, 0.38, 1.14, 3, 4],
  [10.0, 884, 362, 0.38, 1.16, 2.6, 3.6],
];
const camTracks = [1, 2, 3, 4, 5, 6].map((k) => smoothTrack(CAM.map((row) => [row[0], row[k]])));

// ---------------- cursor ----------------
// segments: [t0, t1, from, to]; holds between segments
const CUR = [
  [1.35, 2.02, [760, 760], [548, 503]],
  [3.35, 4.12, [548, 503], null],          // -> Siap Coretax (resolved after measure)
  [6.45, 7.07, null, [742, 668]],          // -> Master
  [8.35, 9.03, [742, 668], [1162, 74]],    // -> nav CTA
];
const clicks = [T.f1.click, T.f2.click, T.f3.click, T.cta];

function cursorPos(t) {
  if (t < CUR[0][0]) return { p: CUR[0][2], vis: 0 };
  for (let i = 0; i < CUR.length; i++) {
    const [t0, t1, a, b] = CUR[i];
    if (t < t0) return { p: CUR[i - 1][3], vis: 1 };
    if (t <= t1) {
      const k = EASE.glide(remap(t, t0, t1));
      // gentle arc: control point offset perpendicular to the path
      const mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2;
      const dx = b[0] - a[0], dy = b[1] - a[1];
      const cx = mx - dy * 0.18, cy = my + dx * 0.18;
      const x = (1 - k) * (1 - k) * a[0] + 2 * (1 - k) * k * cx + k * k * b[0];
      const y = (1 - k) * (1 - k) * a[1] + 2 * (1 - k) * k * cy + k * k * b[1];
      return { p: [x, y], vis: 1 };
    }
  }
  return { p: CUR[CUR.length - 1][3], vis: 1 };
}

// press: quick dip and spring back (0 = rest, 1 = fully pressed)
const press = (t, tc) => (t < tc - 0.06 ? 0 : t < tc ? smoother(remap(t, tc - 0.06, tc)) : 1 - springTo(t, tc, 0.5, 2.6, 0.5));

// ---------------- feature lift + callout ----------------
let liftEl = null, liftKey = null;
function setLift(key, srcId, rect, s, amount) {
  if (amount <= 0.001) {
    if (liftEl) { liftEl.remove(); liftEl = null; liftKey = null; }
    return;
  }
  if (liftKey !== key) {
    if (liftEl) liftEl.remove();
    liftEl = $(srcId).cloneNode(true);
    liftEl.removeAttribute('id');
    liftEl.setAttribute('class', (liftEl.getAttribute('class') || '') + ' lift');
    liftEl.style.left = '0px'; liftEl.style.top = '0px';
    liftEl.style.width = rect.w + 'px'; liftEl.style.height = rect.h + 'px';
    if (key === 'f2') { liftEl.style.background = '#fff'; liftEl.style.borderRadius = '999px'; liftEl.style.padding = '0 2px'; }
    $('liftLayer').appendChild(liftEl);
    liftKey = key;
  }
  $(srcId).style.visibility = 'hidden';
  const p = W(rect.x, rect.y, s);
  const z = 90 * amount;
  const sc = 1 + 0.07 * amount;
  liftEl.style.transformOrigin = `${rect.w / 2}px ${rect.h / 2}px`;
  liftEl.style.transform = `translate3d(${p.x}px, ${p.y}px, ${z}px) scale(${sc})`;
  const sh = key === 'f3' ? 'none' : `0 ${18 * amount}px ${44 * amount}px rgba(19,27,64,${0.28 * amount}), 0 0 0 ${1.5 * amount}px rgba(254,209,17,${amount})`;
  liftEl.style.boxShadow = sh;
  if (key === 'f3') liftEl.style.filter = `drop-shadow(0 ${16 * amount}px ${22 * amount}px rgba(19,27,64,${0.25 * amount}))`;
}

function setCallout(f, appear, gone, pos, anchor, readK) {
  const c = $('callout');
  const vis = appear * (1 - gone);
  if (vis <= 0.001) { c.style.opacity = 0; $('conn').style.opacity = 0; return; }
  $('cTag').textContent = f.tag; $('cTitle').textContent = f.title; $('cDesc').textContent = f.desc;
  c.style.opacity = Math.min(1, appear * 1.4) * (1 - gone);
  const y = 26 * (1 - appear) - 14 * gone;
  const sc = 0.93 + 0.07 * appear;
  c.style.transformOrigin = '0 50%';
  c.style.transform = `translate3d(${pos[0]}px, ${pos[1] + y}px, 0) scale(${sc})`;
  c.querySelector('.bar i').style.width = `${100 * readK}%`;
  // connector: anchor (on the lifted element) -> callout left edge middle
  const ex = pos[0], ey = pos[1] + 66;
  const draw = clamp((appear - 0.15) / 0.85);
  const path = `M${anchor[0]},${anchor[1]} C${anchor[0] + 70},${anchor[1]} ${ex - 70},${ey} ${ex},${ey}`;
  const cp = $('connPath');
  cp.setAttribute('d', path);
  const L = cp.getTotalLength();
  cp.style.strokeDasharray = `${L}`;
  cp.style.strokeDashoffset = `${L * (1 - draw)}`;
  $('conn').style.opacity = 1 - gone;
  const dot = $('connDot');
  dot.setAttribute('cx', anchor[0]); dot.setAttribute('cy', anchor[1]);
  dot.setAttribute('r', 6 * smoother(clamp(appear * 2)));
}

// ---------------- reveal helpers ----------------
const rise = (id, t0, t1, dy = 44) => {
  const k = EASE.arrive(remap(window.__t, t0, t1));
  const el = $(id);
  el.style.opacity = clamp(k * 1.6);
  el.style.transform = `translateY(${dy * (1 - k)}px)`;
};

function seek(t) {
  window.__t = t;
  const s = scrollAt(t);

  // ---- window entrance + camera ----
  const ek = EASE.arrive(remap(t, T.enter[0], T.enter[1]));
  const [fx, fy, fa, zoom, rx, ry] = camTracks.map((f) => f(t));
  const base = 0.98;
  const S = base * zoom * lerp(0.9, 1, ek);
  const tx = -(fx - 720) * S * fa;
  const ty = -(fy - 472) * S * fa + 360 * (1 - ek);
  const tz = -260 * (1 - ek);
  const RX = rx + 22 * (1 - ek) + drift(t, 1.7, 0.35, 0.11);
  const RY = ry - 12 * (1 - ek) + drift(t, 2.9, 0.45, 0.09);
  $('win').style.transform = `translate3d(${tx}px, ${ty}px, ${tz}px) rotateX(${RX}deg) rotateY(${RY}deg) scale(${S})`;
  $('win').style.opacity = clamp(ek * 3);

  // ---- page scroll ----
  $('page').style.transform = `translateY(${-s}px)`;

  // ---- hero reveal (staggered, rises with long tails) ----
  rise('nav', 0.15, 0.85, -16);
  rise('h-l1', 0.3, 1.05); rise('h-l2', 0.4, 1.15); rise('h-l3', 0.5, 1.25);
  $('m1').style.transform = `scaleX(${EASE.marker(remap(t, 0.95, 1.4))})`;
  $('m2').style.transform = `scaleX(${EASE.marker(remap(t, 1.08, 1.55))})`;
  rise('lead', 0.62, 1.3, 30); rise('b-buy', 0.72, 1.35, 26); rise('b-calc', 0.78, 1.4, 26);
  rise('hr', 0.85, 1.4, 16); rise('checks', 0.9, 1.45, 18);
  const vk = EASE.arrive(remap(t, 0.55, 1.45));
  $('video').style.opacity = clamp(vk * 1.5);
  $('video').style.transform = `translateY(${30 * (1 - vk)}px) scale(${0.95 + 0.05 * vk})`;
  $('play').style.transform = `scale(${1 + 0.05 * Math.sin(t * 3.2) * envelope(t, 1.2, 1.8)})`;

  // ---- section 2 reveal as it scrolls in ----
  rise('eyebrow', 5.55, 6.3, 24); rise('h2', 5.65, 6.45, 34);
  $('m3').style.transform = `scaleX(${EASE.marker(remap(t, 6.25, 6.8))})`;
  const mk = springTo(t, 5.8, 1.1, 1.3, 0.55);
  const bob = Math.sin((t - 5.8) * 2.4) * 5 * envelope(t, 6.3, 7.0);
  $('mascotWrap').style.opacity = clamp(mk * 2);
  $('mascotWrap').style.transform = `translateY(${40 * (1 - mk) + bob}px) scale(${0.86 + 0.14 * mk})`;
  $('mascotWrap').style.transformOrigin = '165px 300px';
  $('antenna').setAttribute('r', 8.5 + 1.6 * Math.max(0, Math.sin(t * 5.0)));
  const bk = springTo(t, 6.45, 0.9, 1.6, 0.5);
  $('bubble').style.opacity = clamp(bk * 2);
  $('bubble').style.transformOrigin = '0 70%';
  $('bubble').style.transform = `scale(${0.7 + 0.3 * bk})`;
  // arms wave on click
  const wave = Math.sin(clamp(remap(t, T.f3.click, T.f3.click + 0.9)) * Math.PI * 3) * (1 - remap(t, T.f3.click, T.f3.click + 0.9));
  $('armR').setAttribute('transform', `rotate(${-28 * wave} 237 205)`);

  // ---- presses on clicked targets ----
  $('b-calc').style.transform += ` scale(${1 - 0.05 * press(t, T.f1.click)})`;
  $('b-nav').style.transform = `scale(${1 - 0.06 * press(t, T.cta)})`;
  const ctaGlow = envelope(t, T.cta, T.cta + 0.25, T.cta + 0.6, DUR + 1);
  $('b-nav').style.boxShadow = `0 0 0 ${4 * ctaGlow}px rgba(254,209,17,${0.9 * ctaGlow})`;

  // ---- lifts + callouts ----
  const liftAmt = (tc, tout) => springTo(t, tc + 0.04, 0.9, 1.5, 0.62) * (1 - EASE.inOut(remap(t, tout + 0.05, tout + 0.45)));
  const cIn = (tc) => springTo(t, tc + 0.12, 0.8, 1.7, 0.66);
  const cOut = (tout) => EASE.inOut(remap(t, tout, tout + 0.32));
  const readK = (tc, tout) => EASE.linear(remap(t, tc + 0.3, tout));

  ['b-calc', 'c2', 'robot'].forEach((id) => { $(id).style.visibility = ''; }); // originals visible unless lifted this frame
  const l1 = liftAmt(T.f1.click, T.f1.out), l2 = liftAmt(T.f2.click, T.f2.out), l3 = liftAmt(T.f3.click, T.f3.out);
  if (t < T.f1.out + 0.6) setLift('f1', 'b-calc', R.calc, s, l1);
  else if (t < T.f2.out + 0.6) setLift('f2', 'c2', R.c2, s, l2);
  else setLift('f3', 'robot', R.robot, s, l3);

  const calcW = W(R.calc.x + R.calc.w, R.calc.y + R.calc.h / 2, s);
  const c2W = W(R.c2.x + R.c2.w, R.c2.y + R.c2.h / 2, s);
  const robW = W(R.robot.x + 255, R.robot.y + 230, s);
  if (t < T.f1.out + 0.5) setCallout(FEATURES.f1, cIn(T.f1.click), cOut(T.f1.out), [calcW.x + 70, calcW.y - 70], [calcW.x + 6, calcW.y], readK(T.f1.click, T.f1.out));
  else if (t < T.f2.out + 0.5) setCallout(FEATURES.f2, cIn(T.f2.click), cOut(T.f2.out), [c2W.x + 90, c2W.y + 26], [c2W.x + 8, c2W.y], readK(T.f2.click, T.f2.out));
  else setCallout(FEATURES.f3, cIn(T.f3.click), cOut(T.f3.out), [robW.x + 150, robW.y - 30], [robW.x + 8, robW.y], readK(T.f3.click, T.f3.out));

  // ---- cursor + click ring ----
  const cp = cursorPos(t);
  const cvis = clamp(remap(t, CUR[0][0], CUR[0][0] + 0.25));
  let pr = 0;
  clicks.forEach((tc) => { pr = Math.max(pr, press(t, tc)); });
  $('cursor').style.opacity = cvis;
  $('cursor').style.transform = `translate3d(${cp.p[0] - 4}px, ${cp.p[1] - 3}px, 140px) scale(${1 - 0.14 * pr})`;
  let ring = null;
  clicks.forEach((tc) => { if (t >= tc && t < tc + 0.6) ring = tc; });
  const rg = $('ring');
  if (ring !== null) {
    const k = remap(t, ring, ring + 0.6);
    const size = 18 + 74 * EASE.arrive(k);
    rg.style.opacity = 1 - smoother(k);
    rg.style.width = rg.style.height = `${size}px`;
    rg.style.transform = `translate3d(${cp.p[0] - size / 2}px, ${cp.p[1] - size / 2}px, 120px)`;
  } else rg.style.opacity = 0;
}

async function boot() {
  await document.fonts.ready;
  await Promise.all(['400', '500', '600', '700', '800'].map((w) => document.fonts.load(`${w} 20px Rubik`)));
  measure();
  // resolve cursor targets that depend on measured layout
  const c2c = [R.c2.x + R.c2.w * 0.55, CHROME + R.c2.y + R.c2.h * 0.62];
  CUR[1][3] = c2c; CUR[2][2] = c2c;
  if (new URLSearchParams(location.search).get('green') === '1') document.body.classList.add('green');
  window.seek = seek;
  window.DURATION = DUR;
  seek(0);
  window.__ready = true;
}
boot().catch((e) => { window.__error = String(e && e.stack || e); });

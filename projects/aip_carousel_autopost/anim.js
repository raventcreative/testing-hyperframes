// Every frame is a pure function of t (seconds). render.cjs calls setT(t) then screenshots.
const cl = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const ease = x => { x = cl(x); return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
const outB = x => { x = cl(x); const c = 1.6; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const seg = (t, a, b) => cl((t - a) / (b - a));

// ---------- slide 1
const S1 = document.getElementById('s1');
const src = S1.querySelector('#src'), trunk = S1.querySelector('#trunk'), pulse = S1.querySelector('#pulse'), cnt = S1.querySelector('#cnt');
const tiles = [...S1.querySelectorAll('.tile')], dist = S1.querySelector('.dist');
const A = i => 1.05 + i * 0.42;
function s1(t) {
  const p0 = ease(seg(t, 0, .5));
  src.style.opacity = p0; src.style.transform = `translateY(${(1 - p0) * 24}px)`;
  const pd = ease(seg(t, .35, .75)); dist.style.opacity = pd; dist.style.transform = `translateY(${(1 - pd) * 20}px)`;
  trunk.style.transform = `scaleY(${ease(seg(t, .45, .85))})`;
  let n = 0, pv = 0;
  tiles.forEach((el, i) => {
    const appear = ease(seg(t, .55 + i * .04, .95 + i * .04));
    const p = ease(seg(t, A(i), A(i) + .32));
    if (p >= .5) n++;
    el.style.opacity = appear;
    el.style.transform = `translateY(${(1 - appear) * 18}px) scale(${1 + .06 * Math.sin(Math.PI * p)})`;
    el.style.borderColor = p > .5 ? '#294b77' : '';
    el.style.background = p > .5 ? '#fff' : '';
    el.style.boxShadow = p > .5 ? '0 10px 26px rgba(41,75,119,.14)' : 'none';
    const app = el.querySelector('.app');
    app.style.filter = `grayscale(${1 - p})`; app.style.opacity = .35 + .65 * p;
    el.querySelector('.wait').style.opacity = 1 - p;
    el.querySelector('.ok').style.opacity = p;
    const w = seg(t, A(i) - .34, A(i));
    if (w > 0 && w < 1) pv = w;
  });
  pulse.style.opacity = pv > 0 ? 1 : 0;
  pulse.style.top = (-8 + pv * 46) + 'px';
  cnt.textContent = n;
}

// ---------- slide 2
const S2 = document.getElementById('s2');
const rows = [...S2.querySelectorAll('.row')], cur = S2.querySelector('#cur');
let P, START = [940, 1120], REST;
window.reflow = () => { const sr = S2.querySelector('.content').getBoundingClientRect();
  P = rows.map(r => { const b = r.querySelector('.tg').getBoundingClientRect(); return [b.left - sr.left + 40, b.top - sr.top + 16]; });
  REST = [P[7][0] - 90, P[7][1] + 28]; };
window.reflow();
const C = i => .75 + i * .52;               // click times, last ≈ 4.4 s
function curPos(t) {
  const pts = [START, ...P, REST];
  const arr = [0, ...P.map((_, i) => C(i) - .06), C(7) + .9];
  const dep = [0, .15, ...P.map((_, i) => C(i) + .1)];
  for (let k = 1; k < pts.length; k++) {
    if (t < arr[k]) {
      const e = ease(seg(t, dep[k], arr[k]));
      return [pts[k - 1][0] + (pts[k][0] - pts[k - 1][0]) * e, pts[k - 1][1] + (pts[k][1] - pts[k - 1][1]) * e];
    }
  }
  return REST;
}
function s2(t) {
  const [x, y] = curPos(t);
  let sc = 1;
  rows.forEach((r, i) => {
    const on = t >= C(i);
    r.querySelector('.tg').classList.toggle('on', on);
    const k = seg(t, C(i), C(i) + .7);
    r.style.setProperty('--hl', on ? (k < .2 ? k / .2 : 1 - (k - .2) / .8) * .9 : 0);
    r.querySelector('.tm').style.opacity = on ? 1 : .3;
    r.querySelector('.cap').style.opacity = on ? 1 : .55;
    const d = Math.abs(t - C(i)); if (d < .08) sc = .82 + d * 2.2;
  });
  cur.style.transform = `translate(${x - 8}px, ${y - 8}px) scale(${sc})`;
  cur.style.transformOrigin = '8px 8px';
}

const clips = [...document.querySelectorAll('img.clipf')];
window.setT = t => { const n = String(Math.min(180, Math.floor(t * 30) + 1)).padStart(3, '0');
  clips.forEach(im => { const u = `assets/clip/f_${n}.jpg`; if (!im.src.endsWith(u)) im.src = u; }); s1(t); s2(t); };
window.ready = () => Promise.all(clips.map(im => im.decode().catch(() => 0)));
window.setT(6);

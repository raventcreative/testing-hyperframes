// Declarative, time-pure animation. setT(t) sets every frame from t (s).
const cl = x => Math.min(1, Math.max(0, x)), ease = x => { x = cl(x); return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
const seg = (t, a, b) => cl((t - a) / (b - a)), $ = (q, r = document) => [...r.querySelectorAll(q)];
const nums = s => s.split(',').map(Number);
const IN = $('[data-in]'), SHOW = $('[data-show]'), TYPE = $('[data-type]'), CNT = $('[data-cnt]'), ON = $('[data-on]'),
      GROW = $('[data-grow]'), RING = $('[data-ring]'), DRAW = $('[data-draw]'), PH = $('[data-ph]'), CUR = $('.cursor');
const FLOWS = $('path.flow'), FD = $('.fd');
function setT(t) {
  IN.forEach(e => { const p = ease(seg(t, +e.dataset.in, +e.dataset.in + .35)); e.style.opacity = p;
    e.style.transform = `translateY(${(1 - p) * 14}px) scale(${.96 + .04 * p})`; });
  SHOW.forEach(e => { const [a, b] = nums(e.dataset.show); e.style.opacity = Math.min(a <= 0 ? 1 : seg(t, a, a + .2), 1 - seg(t, b - .05, b + .15)); });
  TYPE.forEach(e => { const [a, d] = nums(e.dataset.type), f = e.dataset.full, n = Math.round(f.length * seg(t, a, a + d));
    e.textContent = f.slice(0, n) + (n > 0 && n < f.length ? '▍' : ''); });
  CNT.forEach(e => { const [a, b, x, y] = nums(e.dataset.cnt); const v = Math.round(x + (y - x) * ease(seg(t, a, b)));
    e.textContent = v >= 1000 ? (v / 1000).toFixed(1).replace('.', ',') + 'rb' : v; });
  ON.forEach(e => e.classList.toggle('on', t >= +e.dataset.on));
  GROW.forEach(e => { const [a, b] = nums(e.dataset.grow); e.style.transform = `scaleX(${ease(seg(t, a, b))})`; });
  RING.forEach(e => { const [a, b, x, y] = nums(e.dataset.ring), C = 2 * Math.PI * 40, v = x + (y - x) * ease(seg(t, a, b));
    e.style.strokeDasharray = C; e.style.strokeDashoffset = C * (1 - v / 100); });
  DRAW.forEach(e => { const [a, b] = nums(e.dataset.draw), L = e.getTotalLength(); e.style.strokeDasharray = L; e.style.strokeDashoffset = L * (1 - ease(seg(t, a, b))); });
  PH.forEach(e => { const [a, b] = nums(e.dataset.ph), w = e.parentElement.clientWidth; e.style.left = (72 + (w - 76) * seg(t, a, b)) + 'px'; });
  FLOWS.forEach((p, i) => { p.style.strokeDashoffset = -t * 30; const L = p.getTotalLength(), u = ((t * .45 + i * .17) % 1);
    const q = p.getPointAtLength(L * u); FD[i].setAttribute('cx', q.x); FD[i].setAttribute('cy', q.y); FD[i].style.opacity = t > .6 ? 1 : 0; });
  CUR.forEach(c => { const keys = JSON.parse(c.dataset.keys), sl = c.closest('.slide').getBoundingClientRect();
    const P = keys.map(([kt, sel, dx = 0, dy = 0]) => { const b = document.querySelector(sel).getBoundingClientRect();
      return [kt, b.left - sl.left + b.width / 2 + dx, b.top - sl.top + b.height / 2 + dy]; });
    let x = P[0][1], y = P[0][2];
    for (let k = 1; k < P.length; k++) if (t >= P[k - 1][0]) { const e = ease(seg(t, P[k - 1][0] + .1, P[k][0])); x = P[k - 1][1] + (P[k][1] - P[k - 1][1]) * e; y = P[k - 1][2] + (P[k][2] - P[k - 1][2]) * e; }
    const clk = P[P.length - 2][0], d = Math.abs(t - clk);
    c.style.opacity = seg(t, P[0][0] - .3, P[0][0]) * (1 - seg(t, P[P.length - 1][0] + .3, P[P.length - 1][0] + .6));
    c.style.transform = `translate(${x - 8}px,${y - 8}px) scale(${d < .08 ? .82 + d * 2.2 : 1})`; c.style.transformOrigin = '8px 8px'; });
}
window.setT = setT; window.ready = () => Promise.resolve(); window.reflow = () => {};
setT(99);

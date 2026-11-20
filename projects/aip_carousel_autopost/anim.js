// Every frame is a pure function of t (seconds, 0..6). render.cjs calls setT(t) then screenshots.
const cl = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const ease = x => { x = cl(x); return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
const seg = (t, a, b) => cl((t - a) / (b - a));
const pop = p => 1 + .12 * Math.sin(Math.PI * cl(p));
const $ = (r, q) => [...r.querySelectorAll(q)];

// ---------- clip frames (video previews)
const clips = $(document, 'img.clipf');
function frames(t) { const n = String(Math.min(180, Math.floor(t * 30) + 1)).padStart(3, '0');
  clips.forEach(im => { const u = `assets/${im.dataset.clip}/f_${n}.jpg`; if (!im.getAttribute('src').endsWith(u)) im.setAttribute('src', u); }); }
window.ready = () => Promise.all(clips.map(im => im.decode().catch(() => 0)));

// ---------- slide 1: hub & spokes
const S1 = document.getElementById('s1');
const sp = $(S1, 'path.sp').sort((a, b) => a.dataset.i - b.dataset.i), dots = $(S1, '.pdot').sort((a, b) => a.dataset.i - b.dataset.i);
const papps = $(S1, '.papp').sort((a, b) => a.dataset.i - b.dataset.i), live = S1.querySelector('#live');
const post = S1.querySelector('.post'), hub = S1.querySelector('.hub'), apil = S1.querySelector('.apil'), trunk1 = S1.querySelector('.trunk1');
const A1 = i => 1.3 + i * .38;
function s1(t) {
  const a = ease(seg(t, 0, .5)); post.style.opacity = a; post.style.transform = `translateY(${(1 - a) * 20}px)`;
  apil.style.opacity = ease(seg(t, .3, .7));
  const tl = trunk1.getTotalLength(); trunk1.style.strokeDasharray = `${tl}`; trunk1.style.strokeDashoffset = tl * (1 - ease(seg(t, .45, .85)));
  const h = seg(t, .75, 1.15); hub.style.opacity = ease(h); hub.style.transform = `scale(${(.7 + .3 * ease(h)) * pop(seg(t, 1.0, 1.3) * .6)})`;
  let n = 0;
  sp.forEach((p, i) => {
    const L = p.getTotalLength(), w = seg(t, A1(i) - .38, A1(i)), on = t >= A1(i);
    if (w > 0 && w < 1) { const q = p.getPointAtLength(L * ease(w)); dots[i].setAttribute('cx', q.x); dots[i].setAttribute('cy', q.y); dots[i].style.opacity = 1; }
    else dots[i].style.opacity = 0;
    p.classList.toggle('on', on);
    p.style.strokeDashoffset = on ? -t * 26 : 0;
    const ap = papps[i], pp = seg(t, A1(i), A1(i) + .35);
    ap.style.opacity = .25 + .75 * ease(seg(t, .2 + i * .05, .6 + i * .05));
    ap.querySelector('.app').style.transform = `scale(${pop(pp)})`;
    ap.querySelector('.app').style.filter = `grayscale(${on ? 0 : 1})`;
    ap.querySelector('.lv').style.opacity = ease(pp); ap.querySelector('.lv').style.transform = `scale(${.5 + .5 * ease(pp)})`;
    if (on) n++;
  });
  live.textContent = n;
}

// ---------- slide 2: cards + cursor
const S2 = document.getElementById('s2');
const pcs = $(S2, '.pc'), cur = S2.querySelector('#cur');
let P, START = [940, 1120], REST;
const C2 = i => .8 + i * .48;
window.reflow = () => { const sr = S2.querySelector('.content').getBoundingClientRect();
  P = pcs.map(c => { const b = c.querySelector('.tg').getBoundingClientRect(); return [b.left - sr.left + 36, b.top - sr.top + 15]; });
  REST = [P[7][0] - 110, P[7][1] + 70]; };
function curPos(t) {
  const pts = [START, ...P, REST], arr = [0, ...P.map((_, i) => C2(i) - .05), C2(7) + .8], dep = [0, .2, ...P.map((_, i) => C2(i) + .08)];
  for (let k = 1; k < pts.length; k++) if (t < arr[k]) { const e = ease(seg(t, dep[k], arr[k]));
    return [pts[k - 1][0] + (pts[k][0] - pts[k - 1][0]) * e, pts[k - 1][1] + (pts[k][1] - pts[k - 1][1]) * e]; }
  return REST;
}
function s2(t) {
  let sc = 1;
  pcs.forEach((c, i) => {
    const on = t >= C2(i), k = seg(t, C2(i), C2(i) + .55);
    const ap = ease(seg(t, i * .06, .4 + i * .06)); c.style.opacity = ap; c.style.transform = `translateY(${(1 - ap) * 16}px)`;
    c.querySelector('.tg').classList.toggle('on', on);
    c.style.borderColor = on && k < 1 ? '#294b77' : ''; c.style.boxShadow = on && k < 1 ? '0 0 0 4px rgba(41,75,119,.12),0 12px 28px rgba(41,75,119,.16)' : '';
    c.querySelector('.autot').style.opacity = on ? 1 : .35;
    const d = Math.abs(t - C2(i)); if (d < .08) sc = .82 + d * 2.2;
  });
  const [x, y] = curPos(t); cur.style.transform = `translate(${x - 8}px,${y - 8}px) scale(${sc})`; cur.style.transformOrigin = '8px 8px';
}

// ---------- slide 3: connect + toggles
const S3 = document.getElementById('s3'), conns = $(S3, '.conn'), mtg = $(S3, '.minis .tg');
function s3(t) {
  conns.forEach((c, i) => { const a = seg(t, .1 + i * .1, .5 + i * .1), d = seg(t, 1.1 + i * .28, 1.35 + i * .28);
    c.style.opacity = ease(a); c.style.transform = `translateY(${(1 - ease(a)) * 18}px) scale(${pop(d) * .99 + .01})`;
    c.querySelector('.app').style.filter = `grayscale(${1 - d})`;
    c.querySelector('.w').style.opacity = 1 - d; c.querySelector('.dn').style.opacity = d;
    c.style.borderColor = d > .5 ? '#294b77' : ''; });
  mtg.forEach((g, i) => g.classList.toggle('on', t >= 3.6 + i * .14));
}

// ---------- slide 4: calendar fills
const S4 = document.getElementById('s4'), ccs = $(S4, '.cc').sort((a, b) => a.dataset.i - b.dataset.i), q = S4.querySelector('#queued');
function s4(t) {
  let n = 0;
  ccs.forEach((c, i) => { const a = seg(t, .5 + i * .085, .75 + i * .085); c.style.opacity = ease(a);
    c.style.transform = `scale(${.4 + .6 * ease(a)})`; c.style.display = 'inline-block'; if (a >= .5) n++; });
  q.textContent = n;
}

// ---------- slide 5: "now" sweeps the day
const S5 = document.getElementById('s5'), evs = $(S5, '.ev'), now = S5.querySelector('#now'), nowt = S5.querySelector('#nowt');
function s5(t) {
  const hrs = 6 + (21.5 - 6) * ease(seg(t, .4, 5.0));
  const ys = evs.map(e => e.offsetTop + e.offsetHeight / 2), hs = evs.map(e => +e.dataset.h);
  const H = [6, ...hs, 21.5], Y = [ys[0] - 32, ...ys, ys[ys.length - 1] + 32];
  let y = Y[Y.length - 1];
  for (let k = 1; k < H.length; k++) if (hrs <= H[k]) { y = Y[k - 1] + (Y[k] - Y[k - 1]) * (hrs - H[k - 1]) / (H[k] - H[k - 1]); break; }
  now.style.top = y + 'px';
  const hh = Math.floor(hrs), mm = Math.floor((hrs - hh) * 60);
  nowt.textContent = `Sekarang · ${String(hh).padStart(2, '0')}.${String(mm).padStart(2, '0')}`;
  evs.forEach((e, i) => { const d = seg(hrs, hs[i], hs[i] + .35);
    e.querySelector('.q').style.opacity = 1 - d; e.querySelector('.ok').style.opacity = d;
    e.querySelector('i').style.background = d > .5 ? '#294b77' : '#fff';
    e.querySelector('.app').style.transform = `scale(${pop(d)})`; });
}

window.setT = t => { frames(t); s1(t); s2(t); s3(t); s4(t); s5(t); };
window.reflow(); window.setT(6);

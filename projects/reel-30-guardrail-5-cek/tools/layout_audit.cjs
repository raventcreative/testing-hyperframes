const { chromium } = require('playwright');
const path = require('path'), http = require('http'), fs = require('fs');
const MT = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.glb': 'model/gltf-binary', '.mp3': 'audio/mpeg', '.wav': 'audio/wav' };
(async () => {
  const file = process.argv[2];
  const times = process.argv[3].split(',').map(Number);
  const root = path.dirname(path.resolve(file));
  const srv = http.createServer((rq, rs) => {
    const f = path.join(root, decodeURIComponent(rq.url.split('?')[0]));
    fs.readFile(f, (e, d) => { if (e) { rs.statusCode = 404; return rs.end(); }
      rs.setHeader('content-type', MT[path.extname(f).toLowerCase()] || 'application/octet-stream'); rs.end(d); });
  });
  await new Promise((r) => srv.listen(0, '127.0.0.1', r));
  const port = srv.address().port;
  const b = await chromium.launch({ args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  p.on('pageerror', (e) => console.log('PAGEERROR ' + e.message));
  await p.goto(`http://127.0.0.1:${port}/${path.basename(file)}`);
  await p.waitForFunction(() => window.__timelines && window.__timelines.main, null, { timeout: 60000 });
  for (const t of times) {
    await p.evaluate((t) => { const tl = window.__timelines.main; tl.pause(); tl.time(t); }, t);
    await p.waitForTimeout(90);
    const out = await p.evaluate(() => {
      const eff = (el) => { let o = 1, n = el;
        while (n && n.nodeType === 1) { const cs = getComputedStyle(n);
          if (cs.display === 'none' || cs.visibility === 'hidden') return 0;
          o *= parseFloat(cs.opacity);
          const m = /opacity\(([\d.]+)\)/.exec(cs.filter || ''); if (m) o *= parseFloat(m[1]);
          n = n.parentElement; }
        return o; };
      const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 2 && r.height > 2 && eff(el) > 0.12; };
      const BOX = '.gd, .gd .it, #gdAg, #gdEnd, .ln, #lpMid, .gt, #hCard, #hStop, #hTahan > span, #hRailK, .pcard, .sheet, #izOk, #izNo, .fn, .res, #ruleC, #diaT, #waitC, #gaTop, #gaLimT, #swLbl, #stopBar, #notif, .kg, #kPuck, #kKey, .kc, #fbtn, #tbar, .ahd, #lpHd';
      const over = [], cut = [];
      // 1. text overflowing its own styled box
      const boxes = Array.from(document.querySelectorAll(BOX)).filter(vis);
      const walk = (root) => { const out = [];
        const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
        let n; while ((n = w.nextNode())) if (n.nodeValue.trim()) out.push(n); return out; };
      for (const el of boxes) {
        const cs = getComputedStyle(el);
        const r = el.getBoundingClientRect();
        const bl = parseFloat(cs.borderLeftWidth), br = parseFloat(cs.borderRightWidth);
        const bt = parseFloat(cs.borderTopWidth), bb = parseFloat(cs.borderBottomWidth);
        const pad = { l: r.left + bl, r: r.right - br, t: r.top + bt, b: r.bottom - bb };
        for (const tn of walk(el)) {
          const rg = document.createRange(); rg.selectNodeContents(tn);
          const tr = rg.getBoundingClientRect();
          if (tr.width < 1) continue;
          const d = Math.max(pad.l - tr.left, tr.right - pad.r, pad.t - tr.top, tr.bottom - pad.b);
          if (d > 1.5) cut.push({ box: el.id || el.className, text: tn.nodeValue.trim().slice(0, 34), by: Math.round(d) });
        }
      }
      // 2. element-vs-element overlap
      for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
        const a = boxes[i], c = boxes[j];
        if (a.contains(c) || c.contains(a)) continue;
        const ra = a.getBoundingClientRect(), rc = c.getBoundingClientRect();
        const ox = Math.min(ra.right, rc.right) - Math.max(ra.left, rc.left);
        const oy = Math.min(ra.bottom, rc.bottom) - Math.max(ra.top, rc.top);
        if (ox > 2 && oy > 2) over.push({ a: a.id || a.className, b: c.id || c.className, ox: Math.round(ox), oy: Math.round(oy) });
      }
      // 3. labels off-centre inside flex-centred boxes
      const off = [];
      for (const el of boxes) {
        const cs = getComputedStyle(el);
        if (cs.display !== 'flex' || cs.justifyContent !== 'center') continue;
        const r = el.getBoundingClientRect(); const tns = walk(el); if (!tns.length) continue;
        let l = Infinity, rr = -Infinity;
        for (const tn of tns) { const rg = document.createRange(); rg.selectNodeContents(tn); const b = rg.getBoundingClientRect(); if (b.width < 1) continue; l = Math.min(l, b.left); rr = Math.max(rr, b.right); }
        if (!isFinite(l)) continue;
        const d = ((l + rr) / 2) - ((r.left + r.right) / 2);
        if (Math.abs(d) > 14) off.push({ box: el.id || el.className, text: tns.map(x=>x.nodeValue.trim()).join(' ').slice(0,28), off: Math.round(d) });
      }
      return { cut, over, off };
    });
    const lines = [];
    out.cut.forEach(x => lines.push(`  CUT   ${x.box} :: "${x.text}" past edge by ${x.by}px`));
    out.over.forEach(x => lines.push(`  OVER  ${x.a} x ${x.b} (${x.ox}x${x.oy}px)`));
    out.off.forEach(x => lines.push(`  OFF   ${x.box} :: "${x.text}" off-centre ${x.off}px`));
    console.log(`t=${t}s  ${lines.length ? '' : 'clean'}`);
    lines.forEach(l => console.log(l));
  }
  await b.close(); srv.close();
})();

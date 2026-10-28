// Browser entry: builds the requested shot and exposes a deterministic frame renderer.
import * as THREE from 'three';
import { Stage } from './lib/stage.js';
import { loadFonts } from './docs/draw.js';
import { OUTPUT } from './tokens.js';

const params = new URLSearchParams(location.search);
const shotName = params.get('shot') || 'v1';
const quality = params.get('q') || 'draft';

async function exportTextures() {
  const { drawReceipt } = await import('./docs/receipt.js');
  const { drawStatement, drawStatementPage2 } = await import('./docs/statement.js');
  const { drawReport, drawReportBack } = await import('./docs/report.js');
  const { paperBump } = await import('./docs/draw.js');
  const r = drawReceipt(2.4), s = drawStatement(2.4), s2 = drawStatementPage2(1.6), p = drawReport(2.8), pb = drawReportBack(2.4);
  const set = {
    receipt_front: r.front, receipt_back: r.back,
    statement_p1_front: s.front, statement_p1_back: s.back,
    statement_p2_front: s2.front,
    report_front: p.front, report_back_cover: pb.back, report_back_roughness: pb.backRough,
    paper_bump: paperBump(512, 11),
  };
  window.TEXTURES = Object.fromEntries(Object.entries(set).map(([k, c]) => [k, c.toDataURL('image/png')]));
  window.REGIONS = { receipt: r.regions, statement: s.regions, report: p.regions };
}

async function boot() {
  await loadFonts();
  if (params.get('mode') === 'textures') { await exportTextures(); window.__ready = true; return; }
  const stage = new Stage({
    size: OUTPUT.width,
    ssaa: Number(params.get('ssaa') || OUTPUT.ssaa[quality]),
    subframes: Number(params.get('sub') || OUTPUT.subframes[quality]),
    shutter: OUTPUT.shutter,
    fps: OUTPUT.fps,
    msaa: quality === 'draft' ? 4 : 0,
  });
  const mod = await import(`./shots/${shotName}.js`);
  const shot = mod.createShot(stage, quality);
  window.SHOT = { name: shotName, duration: shot.duration, fps: OUTPUT.fps, frames: Math.round(shot.duration * OUTPUT.fps) };
  window.renderFrame = (i) => {
    stage.render(i / OUTPUT.fps, shot.update);
    return stage.readBase64();
  };
  // motion QC: projected centre (px) of every visible document at frame i, no rendering
  window.probe = (i) => {
    const t = i / OUTPUT.fps;
    shot.update(t);
    stage.scene.updateMatrixWorld(true);
    stage.camera.updateMatrixWorld(true);
    const out = {};
    stage.scene.traverse((o) => {
      if (!o.isPaperSheet) return;
      let vis = true;
      o.traverseAncestors((a) => { if (!a.visible) vis = false; });
      if (!vis || !o.visible) return;
      const a = o.gFront.attributes.position.array;
      const n = a.length / 3;
      let cx = 0, cy = 0, c = 0;
      for (let k = 0; k < n; k += 97) {
        const v = new THREE.Vector3(a[k * 3], a[k * 3 + 1], a[k * 3 + 2]);
        o.mFront.localToWorld(v);
        v.project(stage.camera);
        cx += (v.x + 1) * 540; cy += (1 - v.y) * 540; c++;
      }
      out[o.name] = [cx / c, cy / c];
    });
    out.cam = stage.camera.position.toArray();
    return out;
  };
  window.__ready = true;
}
boot().catch((e) => { window.__error = String(e && e.stack || e); console.error(e); });

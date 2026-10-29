// Reusable 3D document assets — the SAME builders are used by all three films.
import * as THREE from 'three';
import { PaperSheet } from './PaperSheet.js';
import { DOC, BRAND } from '../tokens.js';
import { paperBump } from '../docs/draw.js';
import { drawReceipt } from '../docs/receipt.js';
import { drawStatement, drawStatementPage2 } from '../docs/statement.js';
import { drawReport, drawReportBack } from '../docs/report.js';

let _bump = null;
function bump() {
  if (_bump) return _bump;
  const t = new THREE.CanvasTexture(paperBump(512, 11));
  t.wrapS = t.wrapT = THREE.RepeatWrapping;
  t.repeat.set(4, 6);
  t.colorSpace = THREE.NoColorSpace;
  _bump = t;
  return t;
}

function tex(canvas, renderer, srgb = true) {
  const t = new THREE.CanvasTexture(canvas);
  t.colorSpace = srgb ? THREE.SRGBColorSpace : THREE.NoColorSpace;
  t.anisotropy = renderer.capabilities.getMaxAnisotropy();
  t.minFilter = THREE.LinearMipmapLinearFilter;
  t.generateMipmaps = true;
  return t;
}

export function createReceipt(stage, quality = 'final') {
  const art = drawReceipt(quality === 'final' ? 2.4 : 1.6);
  const { w, h, t } = DOC.receipt;
  const sheet = new PaperSheet({
    w, h, t, nx: 60, ny: 150, radius: 0.016,
    zigzag: { teeth: 30, depth: 0.011 },
    front: tex(art.front, stage.renderer), back: tex(art.back, stage.renderer),
    edgeColor: '#EEECE6', roughness: 0.66, bump: bump(), bumpScale: 0.35, paperHex: BRAND.thermal,
  });
  sheet.art = art;
  sheet.name = 'receipt';
  return sheet;
}

export function createStatement(stage, quality = 'final') {
  const art = drawStatement(quality === 'final' ? 2.4 : 1.6);
  const { w, h, t } = DOC.statement;
  const sheet = new PaperSheet({
    w, h, t, nx: 56, ny: 180, radius: 0.012,
    front: tex(art.front, stage.renderer), back: tex(art.back, stage.renderer),
    edgeColor: '#ECEAE4', roughness: 0.8, bump: bump(), bumpScale: 0.45, paperHex: BRAND.paper,
  });
  sheet.art = art;
  sheet.name = 'statement';
  return sheet;
}

export function createStatementPage2(stage, quality = 'final') {
  const art = drawStatementPage2(quality === 'final' ? 1.6 : 1.0);
  const { w, h, t } = DOC.statement;
  const sheet = new PaperSheet({
    w, h, t, nx: 24, ny: 36, radius: 0.012,
    front: tex(art.front, stage.renderer), back: tex(art.back, stage.renderer),
    edgeColor: '#E8E6E0', roughness: 0.82, bump: bump(), bumpScale: 0.45, paperHex: '#F9F8F5',
  });
  sheet.name = 'statementP2';
  return sheet;
}

export function createReport(stage, quality = 'final') {
  const art = drawReport(quality === 'final' ? 2.8 : 1.6);
  const backArt = drawReportBack(quality === 'final' ? 2.4 : 1.4);
  const { w, h, t } = DOC.report;
  const sheet = new PaperSheet({
    w, h, t, nx: 56, ny: 210, radius: 0.012,
    front: tex(art.front, stage.renderer), back: tex(backArt.back, stage.renderer),
    backRoughnessMap: tex(backArt.backRough, stage.renderer, false),
    edgeColor: '#E9EAF0', roughness: 0.74, bump: bump(), bumpScale: 0.3, paperHex: BRAND.paperCool,
  });
  sheet.art = art;
  sheet.name = 'report';
  return sheet;
}

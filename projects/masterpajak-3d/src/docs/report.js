// LAPORAN KEUANGAN — financial report (fictional illustrative figures, internally consistent)
import { BRAND } from '../tokens.js';
import { Doc, rupiah, makeCanvas } from './draw.js';

export const REPORT = {
  months: ['Jan', 'Feb', 'Mar'],
  revenue: [76.2, 81.9, 90.5],   // juta
  expense: [51.8, 53.7, 57.7],   // juta (HPP + operasional + lain-lain)
  pl: [
    ['Pendapatan usaha', 248600000, 0],
    ['Harga pokok penjualan', -121400000, 0],
    ['Laba kotor', 127200000, 1],
    ['Beban operasional', -38950000, 0],
    ['Beban lain-lain', -2850000, 0],
    ['Laba sebelum pajak', 85400000, 1],
    ['PPh Final 0,5% (PP 55/2022)', -1243000, 0],
    ['Laba bersih', 84157000, 2],
  ],
};

const fmt = (n) => (n < 0 ? `(${rupiah(-n)})` : rupiah(n));

export function drawReport(scale = 2.4) {
  const d = new Doc(860, 1216, scale, BRAND.paperCool);
  const M = 56, R = 860 - 56;

  // top bar
  d.wordmark(M, 70, 21);
  d.text('Dibuat otomatis  ·  31 Maret 2026', R, 66, { size: 12.5, color: BRAND.muted, align: 'right' });
  d.hline(M, R, 96, BRAND.line, 1.5);

  // title + animated marker band (shader region)
  const tw = d.measure('LAPORAN KEUANGAN', 58, 800, 'Rubik', 1);
  d.region('titleMarker', M - 8, 150, tw + 16, 30);
  d.text('LAPORAN KEUANGAN', M, 170, { size: 58, weight: 800, color: BRAND.navyInk, spacing: 1 });
  d.text('Laporan Laba Rugi  ·  1 Januari – 31 Maret 2026', M, 212, { size: 17, color: BRAND.muted });
  d.text('CV Contoh Usaha', R, 212, { size: 17, weight: 600, color: BRAND.navyInk, align: 'right' });

  // KPI cards
  const kpis = [
    ['PENDAPATAN', 'Rp 248,6 jt', 'Jan – Mar 2026', false],
    ['TOTAL BEBAN', 'Rp 163,2 jt', 'HPP + operasional', false],
    ['LABA BERSIH', 'Rp 84,2 jt', 'Setelah PPh Final', true],
  ];
  const gap = 14, cw = (R - M - gap * 2) / 3, ky = 244, kh = 124;
  kpis.forEach(([k, v, s, hero], i) => {
    const x = M + i * (cw + gap);
    d.rrect(x, ky, cw, kh, 16, hero ? BRAND.navy : BRAND.surface);
    d.text(k, x + 20, ky + 34, { size: 11.5, weight: 600, color: hero ? BRAND.yellowSoft : BRAND.muted, spacing: 1.8 });
    d.text(v, x + 20, ky + 78, { size: 30, weight: 700, color: hero ? BRAND.yellow : BRAND.navyInk });
    d.text(s, x + 20, ky + 104, { size: 12.5, color: hero ? 'rgba(255,255,255,0.72)' : BRAND.muted });
    d.region(`kpi${i}`, x + 12, ky + 46, cw - 24, 42);
  });

  // chart panel
  const cy = 394, ch = 330;
  d.rrect(M, cy, R - M, ch, 16, '#FFFFFF', BRAND.line, 1.5);
  d.text('Pendapatan vs Beban per Bulan', M + 24, cy + 38, { size: 16, weight: 600, color: BRAND.navyInk });
  // legend
  let lx = R - 24;
  const legend = [['Laba', BRAND.yellow, true], ['Beban', '#C5CBDD'], ['Pendapatan', BRAND.navy]];
  legend.forEach(([name, col, line]) => {
    const w = d.measure(name, 12.5);
    d.text(name, lx, cy + 37, { size: 12.5, color: BRAND.muted, align: 'right' });
    lx -= w + 10;
    if (line) d.rect(lx - 18, cy + 31, 18, 4, col);
    else d.rrect(lx - 12, cy + 26, 12, 12, 3, col);
    lx -= 34;
  });
  const px0 = M + 70, px1 = R - 28, py0 = cy + 74, py1 = cy + ch - 46;
  const maxV = 100;
  const Y = (v) => py1 - (v / maxV) * (py1 - py0);
  [0, 25, 50, 75, 100].forEach((v) => {
    d.hline(px0, px1, Y(v), v === 0 ? '#AEB4C8' : '#EDEFF5', v === 0 ? 2 : 1.5);
    d.text(v === 0 ? '0' : `${v} jt`, px0 - 12, Y(v) + 4, { size: 11.5, color: '#9AA1B8', align: 'right' });
  });
  const groupW = (px1 - px0) / 3;
  const bw = 42;
  const pts = [];
  REPORT.months.forEach((m, i) => {
    const gx = px0 + groupW * (i + 0.5);
    d.rrect(gx - bw - 5, Y(REPORT.revenue[i]), bw, py1 - Y(REPORT.revenue[i]), [7, 7, 0, 0], BRAND.navy);
    d.rrect(gx + 5, Y(REPORT.expense[i]), bw, py1 - Y(REPORT.expense[i]), [7, 7, 0, 0], '#C5CBDD');
    d.text(m, gx, py1 + 26, { size: 13, weight: 500, color: BRAND.muted, align: 'center' });
    pts.push([gx, Y(REPORT.revenue[i] - REPORT.expense[i])]);
    // growth column (bottom -> top reveal), slightly wider than the bars
    d.region(`col${i}`, px0 + groupW * i + 2, py0 - 14, groupW - 4, py1 - py0 + 14);
  });
  const g = d.g;
  g.save();
  g.strokeStyle = BRAND.yellow; g.lineWidth = 4.5; g.lineJoin = 'round'; g.lineCap = 'round';
  g.beginPath();
  pts.forEach(([x, y], i) => (i ? g.lineTo(x, y) : g.moveTo(x, y)));
  g.stroke();
  pts.forEach(([x, y]) => {
    g.beginPath(); g.arc(x, y, 7, 0, Math.PI * 2);
    g.fillStyle = '#FFFFFF'; g.fill();
    g.lineWidth = 3.5; g.strokeStyle = BRAND.navy; g.stroke();
  });
  g.restore();

  // P&L table
  let y = cy + ch + 46;
  d.text('Rincian Laba Rugi', M, y, { size: 16, weight: 600, color: BRAND.navyInk });
  d.text('(Rupiah)', R, y, { size: 12.5, color: BRAND.muted, align: 'right' });
  y += 16;
  REPORT.pl.forEach(([label, val, kind], i) => {
    const rh = 38;
    if (kind === 1) d.rect(M, y, R - M, rh, '#F1F3F8');
    const base = y + 25;
    const bold = kind > 0;
    d.text(label, M + 14, base, { size: 15.5, weight: bold ? 700 : 400, color: BRAND.navyInk });
    d.text(fmt(val), R - 14, base, { size: kind === 2 ? 17 : 15.5, weight: bold ? 700 : 500, color: kind === 2 ? BRAND.navy : BRAND.navyInk, align: 'right' });
    if (kind === 2) {
      d.region('profitMarker', M + 4, y + 16, R - M - 8, 16);
    }
    d.region(`pl${i}`, M, y, R - M, rh);
    if (kind !== 1) d.hline(M, R, y + rh, BRAND.line, 1.2);
    y += rh;
  });
  d.hline(M, R, y, BRAND.navy, 2);

  // footer chips
  const fy = 1150;
  d.rrect(M, fy - 26, 236, 38, 19, BRAND.surface);
  d.check(M + 16, fy - 15, 15, BRAND.navy);
  d.text('Siap unggah ke Coretax', M + 42, fy - 1, { size: 13.5, weight: 600, color: BRAND.navy });
  d.text('Disusun dari: Resi INV/2026/03/0187  ·  Rekening Koran Mar 2026', M + 252, fy - 1, { size: 12, color: BRAND.muted });
  d.text('Data ilustrasi — bukan hasil pelanggan', R, fy + 34, { size: 11, color: '#A3A9BE', align: 'right' });

  return { front: d.canvas, regions: d.regions };
}

// Back side. When letter-folded, the top panel's back becomes the COVER.
// Fold maths: the top panel is rotated 180deg about the crease, which renders
// its back rotated 180deg -> we print the cover content rotated 180deg.
export function drawReportBack(scale = 2.4) {
  const d = new Doc(860, 1216, scale, '#F3F4F8');
  const third = 1216 / 3;
  const g = d.g;

  const rotated = (y0, fn) => {
    g.save();
    g.translate(860 / 2, y0 + third / 2);
    g.rotate(Math.PI);
    g.translate(-860 / 2, -third / 2);
    fn();
    g.restore();
  };

  // cover = top third
  rotated(0, () => {
    d.rect(0, 0, 860, third + 2, BRAND.navy);
    // subtle tonal band
    const grd = g.createLinearGradient(0, 0, 860, third);
    grd.addColorStop(0, 'rgba(255,255,255,0.06)');
    grd.addColorStop(1, 'rgba(0,0,0,0.10)');
    g.fillStyle = grd; g.fillRect(0, 0, 860, third + 2);
    d.mark(60, 52, 54, '#FFFFFF', BRAND.yellow);
    d.text('MasterPajak AI', 128, 92, { size: 22, weight: 600, color: '#FFFFFF' });
    d.text('LAPORAN', 60, 222, { size: 62, weight: 800, color: '#FFFFFF', spacing: 2 });
    d.text('KEUANGAN', 60, 290, { size: 62, weight: 800, color: '#FFFFFF', spacing: 2 });
    d.rect(60, 312, 96, 7, BRAND.yellow);
    d.text('Q1 2026  ·  CV Contoh Usaha', 60, 360, { size: 18, weight: 500, color: BRAND.yellowSoft });
    d.text('DATA ILUSTRASI', 800, 360, { size: 11, weight: 600, color: 'rgba(255,255,255,0.5)', align: 'right', spacing: 2 });
  });
  // inner flap = bottom third (seen briefly while unfolding)
  rotated(third * 2, () => {
    d.rect(0, 0, 860, third + 2, BRAND.surface);
    g.globalAlpha = 0.07;
    d.mark(860 / 2 - 110, third / 2 - 110, 220, BRAND.navy, BRAND.navy);
    g.globalAlpha = 1;
    d.text('Ringkasan otomatis', 430, third - 52, { size: 15, weight: 500, color: BRAND.muted, align: 'center', spacing: 1 });
  });

  // roughness: glossy laminate on the navy cover, matte stock elsewhere (G channel)
  const rough = makeCanvas(256, 256);
  const rg = rough.getContext('2d');
  rg.fillStyle = 'rgb(205,205,205)'; rg.fillRect(0, 0, 256, 256);
  rg.fillStyle = 'rgb(92,92,92)'; rg.fillRect(0, 0, 256, Math.round(256 / 3));
  return { back: d.canvas, backRough: rough };
}

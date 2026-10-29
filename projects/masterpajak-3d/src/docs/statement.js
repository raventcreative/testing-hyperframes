// REKENING KORAN — bank statement (fictional account, no real bank branding)
import { BRAND, FONTS } from '../tokens.js';
import { Doc, rupiah, backWithGhost } from './draw.js';

export const OPENING = 152340000;
// [date, description, debit, credit]
export const ROWS = [
  ['01/03', 'Saldo awal', 0, 0],
  ['02/03', 'TRF MASUK PT ARUNA JAYA', 0, 18500000],
  ['04/03', 'PEMBAYARAN LISTRIK', 2315000, 0],
  ['05/03', 'TRF MASUK CV BINTANG TIMUR', 0, 9750000],
  ['07/03', 'GAJI KARYAWAN MARET', 24600000, 0],
  ['09/03', 'QRIS PENJUALAN', 0, 6425000],
  ['11/03', 'SEWA RUKO MARET', 12000000, 0],
  ['14/03', 'TRF KE TOKO SUMBER MAKMUR', 721500, 0],
  ['16/03', 'TRF MASUK PT SINAR ABADI', 0, 21300000],
  ['19/03', 'BIAYA ADMIN', 15000, 0],
  ['21/03', 'QRIS PENJUALAN', 0, 7880000],
  ['24/03', 'PEMBELIAN BAHAN BAKU', 13450000, 0],
  ['27/03', 'TRF MASUK UD MAJU BERSAMA', 0, 11200000],
  ['31/03', 'BUNGA JASA GIRO', 0, 182500],
];
export const MATCH_ROW = 7;           // pairs with receipt TOTAL in video 3
export const HIGHLIGHT_ROWS = [1, 5, 8]; // credits lit in sequence in video 2

function header(d, M, R, title, sub, pageLabel) {
  // brand chip (top-right)
  const chipW = 232;
  d.rrect(R - chipW, 34, chipW, 40, 20, BRAND.surface);
  d.mark(R - chipW + 14, 44, 20);
  d.text('Diimpor ke MasterPajak AI', R - chipW + 42, 60, { size: 13.5, weight: 500, color: BRAND.navy });
  d.text(pageLabel, M, 58, { size: 12, weight: 600, color: BRAND.muted, spacing: 2 });
  d.text(title, M, 116, { size: 54, weight: 800, color: BRAND.navy, spacing: 1 });
  d.text(sub, M, 148, { size: 17, color: BRAND.muted });
  d.rect(M, 170, R - M, 2.5, BRAND.navy);
  d.rect(M, 168, 92, 6.5, BRAND.yellow);
}

export function drawStatement(scale = 2) {
  const d = new Doc(860, 1216, scale, BRAND.paper);
  const M = 56, R = 860 - 56;
  header(d, M, R, 'REKENING KORAN', 'Mutasi Rekening Giro  ·  Periode 01–31 Maret 2026', 'HALAMAN 1 / 2');

  // account info
  const info = [
    ['NAMA REKENING', 'CV Contoh Usaha'],
    ['NO. REKENING', '1234 •••• 5678'],
    ['MATA UANG', 'IDR'],
    ['JENIS', 'Giro Usaha'],
  ];
  const colW = (R - M) / 4;
  info.forEach(([k, v], i) => {
    const x = M + i * colW;
    d.text(k, x, 210, { size: 11, weight: 600, color: BRAND.muted, spacing: 1.6 });
    d.text(v, x, 238, { size: 17, weight: 600, color: BRAND.navyInk });
  });

  // running balance
  let bal = OPENING;
  let tDebit = 0, tCredit = 0;
  const balances = ROWS.map(([, , de, cr], i) => {
    if (i > 0) { bal = bal - de + cr; tDebit += de; tCredit += cr; }
    return bal;
  });
  const closing = bal;

  // summary cards
  const cards = [
    ['SALDO AWAL', rupiah(OPENING), false],
    ['TOTAL KREDIT', rupiah(tCredit), false],
    ['TOTAL DEBIT', rupiah(tDebit), false],
    ['SALDO AKHIR', rupiah(closing), true],
  ];
  const gap = 12, cw = (R - M - gap * 3) / 4;
  cards.forEach(([k, v, hero], i) => {
    const x = M + i * (cw + gap);
    d.rrect(x, 270, cw, 74, 12, hero ? BRAND.navy : BRAND.surface);
    d.text(k, x + 16, 298, { size: 10.5, weight: 600, color: hero ? BRAND.yellowSoft : BRAND.muted, spacing: 1.4 });
    d.text(`Rp ${v}`, x + 16, 328, { size: 16.5, weight: 700, color: hero ? BRAND.yellow : BRAND.navyInk });
  });

  // table
  const cx = { date: M + 14, desc: M + 96, debit: 548, credit: 664, bal: R - 14 };
  const th = 372;
  d.rrect(M, th, R - M, 38, 9, BRAND.navy);
  const hs = { size: 11.5, weight: 600, color: '#FFFFFF', spacing: 1.6 };
  d.text('TANGGAL', cx.date, th + 24, hs);
  d.text('KETERANGAN', cx.desc, th + 24, hs);
  d.text('DEBIT', cx.debit, th + 24, { ...hs, align: 'right' });
  d.text('KREDIT', cx.credit, th + 24, { ...hs, align: 'right' });
  d.text('SALDO', cx.bal, th + 24, { ...hs, align: 'right' });

  const rh = 46;
  let y = th + 38;
  ROWS.forEach(([date, desc, de, cr], i) => {
    if (i % 2 === 1) d.rect(M, y, R - M, rh, '#F3F4F8');
    const base = y + 29;
    d.text(date, cx.date, base, { size: 14.5, color: BRAND.muted });
    d.text(desc, cx.desc, base, { size: 14.5, weight: i === 0 ? 400 : 500, color: BRAND.navyInk });
    d.text(de ? rupiah(de) : '—', cx.debit, base, { size: 14.5, weight: 500, color: de ? BRAND.navyInk : '#B5BACB', align: 'right' });
    d.text(cr ? rupiah(cr) : '—', cx.credit, base, { size: 14.5, weight: 500, color: cr ? BRAND.navySoft : '#B5BACB', align: 'right' });
    d.text(rupiah(balances[i]), cx.bal, base, { size: 14.5, weight: 600, color: BRAND.navyInk, align: 'right' });
    d.region(`row${i}`, M, y + 6, R - M, rh - 12);
    y += rh;
  });
  d.hline(M, R, y, BRAND.navy, 2);

  // footer
  d.text('Saldo akhir per 31/03/2026', M, y + 40, { size: 14, color: BRAND.muted });
  d.text(`Rp ${rupiah(closing)}`, R, y + 40, { size: 20, weight: 700, color: BRAND.navy, align: 'right' });
  d.hline(M, R, 1160, BRAND.line, 1.5);
  d.text('Dokumen ilustrasi — data fiktif', M, 1186, { size: 11.5, color: '#A3A9BE', spacing: 0.5 });
  d.text('Halaman 1 dari 2', R, 1186, { size: 11.5, color: '#A3A9BE', align: 'right' });

  const back = backWithGhost(d.canvas, '#F4F3EF', 0.028);
  return { front: d.canvas, back, regions: d.regions, closing, tDebit, tCredit };
}

export function drawStatementPage2(scale = 1.5) {
  const d = new Doc(860, 1216, scale, '#F9F8F5');
  const M = 56, R = 860 - 56;
  header(d, M, R, 'REKENING KORAN', 'Ringkasan Mutasi  ·  Maret 2026', 'HALAMAN 2 / 2');
  d.text('RINGKASAN', M, 222, { size: 12, weight: 600, color: BRAND.muted, spacing: 2 });
  let b = OPENING;
  const bals = ROWS.map(([, , de, cr], i) => (i > 0 ? (b = b - de + cr) : b));
  const nCr = ROWS.filter((r, i) => i > 0 && r[3]).length;
  const nDe = ROWS.filter((r, i) => i > 0 && r[2]).length;
  const avg = Math.round(bals.reduce((a, v) => a + v, 0) / bals.length / 100) * 100;
  const lo = Math.min(...bals), hi = Math.max(...bals);
  const lines = [
    ['Jumlah transaksi kredit', String(nCr)],
    ['Jumlah transaksi debit', String(nDe)],
    ['Rata-rata saldo', `Rp ${rupiah(avg)}`],
    ['Saldo terendah', `Rp ${rupiah(lo)}`],
    ['Saldo tertinggi', `Rp ${rupiah(hi)}`],
  ];
  lines.forEach(([k, v], i) => {
    const y = 264 + i * 48;
    d.text(k, M, y, { size: 17, color: BRAND.navyInk });
    d.text(v, R, y, { size: 17, weight: 600, color: BRAND.navyInk, align: 'right' });
    d.hline(M, R, y + 16, BRAND.line, 1.5);
  });
  // balance sparkline
  const top = 540, hgt = 230;
  d.rrect(M, top, R - M, hgt + 60, 14, BRAND.surface);
  d.text('Pergerakan saldo', M + 22, top + 36, { size: 15, weight: 600, color: BRAND.navy });
  const g = d.g;
  g.beginPath();
  bals.forEach((v, i) => {
    const p = (v - lo) / (hi - lo);
    const x = M + 30 + (i * (R - M - 60)) / (bals.length - 1);
    const y = top + hgt + 30 - p * (hgt - 50);
    if (i === 0) g.moveTo(x, y); else g.lineTo(x, y);
  });
  g.strokeStyle = BRAND.navy; g.lineWidth = 3.5; g.lineJoin = 'round'; g.stroke();
  d.text('Catatan: dokumen ilustrasi, data fiktif untuk keperluan visual.', M, 900, { size: 14, color: BRAND.muted });
  return { front: d.canvas, back: backWithGhost(d.canvas, '#F4F3EF', 0.02) };
}

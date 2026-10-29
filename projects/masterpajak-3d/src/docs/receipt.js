// RESI — transaction receipt (fictional sample data only)
import { BRAND, FONTS } from '../tokens.js';
import { Doc, rng, rupiah, backWithGhost } from './draw.js';

export const RECEIPT_DATA = {
  merchant: 'TOKO SUMBER MAKMUR',
  address: 'Jl. Kenanga Raya No. 18, Jakarta',
  no: 'INV/2026/03/0187',
  date: '14/03/2026  10:42',
  cashier: 'Dina',
  items: [
    ['Kertas HVS A4 70gr', 5, 54000],
    ['Tinta Printer Hitam', 2, 125000],
    ['Map Dokumen Plastik', 12, 8500],
    ['Jasa Pengiriman', 1, 28000],
  ],
  vat: 0.11,
};

export function drawReceipt(scale = 2) {
  // base layout 600 x 1300 (matches 0.60 x 1.30 scene units), rendered at `scale`
  const d = new Doc(600, 1300, scale, BRAND.thermal);
  const M = 46, R = 600 - 46;
  const mono = FONTS.mono;
  const ink = '#1A2147';
  const muted = '#424A6A';

  // brand row
  d.mark(M, 40, 30);
  d.text('MasterPajak AI', M + 40, 64, { size: 17, weight: 600, color: BRAND.navy });
  d.text('STRUK DIGITAL', R, 63, { size: 13, weight: 600, color: muted, align: 'right', spacing: 2 });

  // heading
  d.text('RESI', 300, 172, { size: 92, weight: 800, color: BRAND.navy, align: 'center', spacing: 10 });
  d.rect(300 - 34, 194, 68, 7, BRAND.yellow);

  d.text(RECEIPT_DATA.merchant, 300, 252, { size: 21, weight: 700, fam: mono, color: ink, align: 'center', spacing: 1 });
  d.text(RECEIPT_DATA.address, 300, 280, { size: 16, weight: 400, fam: mono, color: muted, align: 'center' });

  const dash = (y) => d.hline(M, R, y, '#B9BED0', 2, [7, 6]);
  dash(312);
  const kv = (k, v, y, opt = {}) => {
    d.text(k, M, y, { size: 17.5, fam: mono, color: muted, weight: 500, ...opt });
    d.text(v, R, y, { size: 17.5, fam: mono, color: ink, align: 'right', weight: 500, ...opt });
  };
  kv('No. Resi', RECEIPT_DATA.no, 346);
  kv('Tanggal', RECEIPT_DATA.date, 374);
  kv('Kasir', RECEIPT_DATA.cashier, 402);
  dash(428);

  // items
  let y = 470;
  let subtotal = 0;
  RECEIPT_DATA.items.forEach(([name, q, p], i) => {
    const line = q * p;
    subtotal += line;
    d.text(name, M, y, { size: 20, weight: 500, fam: mono, color: ink });
    d.text(`${q} x ${rupiah(p)}`, M + 18, y + 27, { size: 17.5, weight: 500, fam: mono, color: muted });
    d.text(rupiah(line), R, y + 27, { size: 19, weight: 500, fam: mono, color: ink, align: 'right' });
    d.region(`item${i}`, M - 10, y - 22, R - M + 20, 58);
    y += 72;
  });
  dash(y - 14);
  y += 22;
  const vat = Math.round(subtotal * RECEIPT_DATA.vat);
  const total = subtotal + vat;
  kv('Subtotal', rupiah(subtotal), y);
  y += 34;
  d.region('vat', M - 10, y - 24, R - M + 20, 34);
  kv('PPN 11%', rupiah(vat), y);
  y += 22;
  d.hline(M, R, y, ink, 2);
  d.hline(M, R, y + 6, ink, 2);
  y += 62;
  d.text('TOTAL', M, y, { size: 26, weight: 700, color: BRAND.navy, spacing: 3 });
  d.text(`Rp ${rupiah(total)}`, R, y, { size: 36, weight: 800, color: BRAND.navy, align: 'right' });
  d.region('total', M - 12, y - 40, R - M + 24, 54);
  y += 44;
  kv('Pembayaran', 'Transfer Bank', y);
  y += 30;
  d.text('Status', M, y, { size: 17.5, weight: 500, fam: mono, color: muted });
  const pw = 92;
  d.rrect(R - pw, y - 20, pw, 28, 14, BRAND.navy);
  d.text('LUNAS', R - pw / 2, y - 0.5, { size: 14, weight: 700, color: '#FFFFFF', align: 'center', spacing: 2 });
  y += 26;
  dash(y);

  // barcode (pseudo-random, fictional)
  const r = rng(187);
  let bx = M + 40;
  const by = y + 26, bh = 74;
  while (bx < R - 40) {
    const w = 1.6 + Math.floor(r() * 3) * 1.6;
    if (r() > 0.38) d.rect(bx, by, w, bh, ink);
    bx += w + 1.6;
  }
  d.text('0187 2026 0314 1042', 300, by + bh + 26, { size: 14, fam: mono, color: muted, align: 'center', spacing: 3 });

  d.text('Terima kasih atas kunjungan Anda', 300, by + bh + 66, { size: 15, fam: mono, color: ink, align: 'center' });

  // brand chip
  const cy = by + bh + 96;
  d.rrect(M, cy, R - M, 58, 16, BRAND.surface);
  d.mark(M + 18, cy + 15, 28);
  d.text('Tercatat otomatis di MasterPajak AI', M + 58, cy + 36, { size: 16, weight: 500, color: BRAND.navy });
  d.text('Data ilustrasi', 300, cy + 80,{ size: 12, color: '#A3A9BE', align: 'center', spacing: 1 });

  const back = backWithGhost(d.canvas, '#F6F5F1', 0.03);
  return { front: d.canvas, back, regions: d.regions, total, vat, subtotal };
}

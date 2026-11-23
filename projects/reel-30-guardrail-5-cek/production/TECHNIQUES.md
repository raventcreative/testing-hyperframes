# reel-30 — 5 pagar buat agent AI (blue)

Reference: a static "Guardrails for AI Agents" card — five checks in order (01 feedback loop, 02 corrective
action, 03 human in the loop, 04 emergency stop, 05 input/output guards) with a flow diagram per check.
Beats kept in that order; every example re-cast into a local fashion/e-commerce shop. No product names,
no logos, no reference UI, no "comment X" CTA.

## Elements borrowed from the reference, then re-shaped
- Its numbered badge per check -> our "PAGAR 01…05" gate rail in the hook.
- Its per-card flow diagrams -> one DIFFERENT object per gate instead of five look-alike panels:
  1. **ring** — work travels a closed loop, score climbs 62 -> 88 in the middle
  2. **draft sheet that flips** — Draft 1 breaks the rule, turns over as Draft 2
  3. **forked path** — a decision diamond splits small-value (auto) from big-value (waits)
  4. **meter + throw switch** — spend runs into a hard limit, the knob throws, owner is paged
  5. **corridor** — gate, agent, gate, answer
- Its "result" line per card -> the green result strip under gates 1 and 2, and the closer's verdict cards.

## Transitions — a different one on every beat
zoom punch-through the first gate (hook -> app) · **sweep** · zoom punch-in on the fixed sheet ·
**doors** · content zoom-out reveal (opens on a close-up of the input gate, pulls back to the corridor) ·
**slats** · zoom-through into the CTA. Plus the in-scene card flip and two window swings.
No wipe is used twice, and each one clears before the line that opens the next scene.

## Client rules applied
- Hook shows the problem (an unchecked refund one step from sending) instead of stating it on a slogan card.
- No red or yellow anywhere: #01ccf7 is the accent, a muted slate carries "held", green only on result ticks.
- Hands alternate: the robot crosses the stage between gates so `FX.point` swaps arms, and `FX.beat` alternates.
- Two side rises, each beside a card on the opposite half (approval card left / filter card right).
- Captions carry a dark halo so they stay readable while the robot passes behind them.
- Pauses between VO lines are 0.32–0.48 s as recorded — no padding was added.

## Revisi 1 — 4 cacat layout dari klien (render v1)

| # | Beat | Cacat | Perbaikan |
|---|------|-------|-----------|
| 1 | hook, "INI LIMA PAGAR…" | blok DITAHAN + 5 kartu pagar + label nempel ke bawah, ruang nggak seimbang | kartu aksi dibungkus `#hTop`, mengecil ke `scale 0.72` + turun 50 px saat `tLima`; pill 430→446, rail 532→548 dan tinggi 212→262, label 812→836 dan muncul `tLima+0.78` (dulu `+1.25`, nyaris nggak kebaca); `.gt .gq` ("?") jadi `position:absolute; inset:0` biar center di kartu; origin zoom punch 678→679 px mengikuti pusat `#gt0` |
| 2 | feedback loop, ring skor | kartu "Dikasih skor" / "Instruksi baru" nabrak kartu "SKOR BALASAN 88" | ring bulat → elips: `#lpRing` 480×380 di left 220, node kiri/kanan x 270/650 → 220/700, `.ln` 196→240 px (margin −120), `#lpMid` 176→160 px di left 380. Jarak bersih 40 px di kedua sisi; dot ikut elips (`RX 240 / RY 190`) |
| 3 | kartu approve "Refund ke Bu Rina" | label "Setujui" nggak center di tombol | ikon check di dalam tombol dibuang (yang mendorong teks ke kanan sampai lewat tepi) + rule `.ic` tombol dihapus |
| 4 | koridor saringan | teks item dan pill hijau keluar dari kotaknya | `.gd` 252→272 px lebar, 330→350 px tinggi, posisi left 32/636 → 20/628; `#gdAg` 260→220 px (left 350), panah 290/594 → 298/576; `#gdEnd` 252→320 px di left 580, font 23→20; copy dipendekin: "Nomor & alamat" + "disensor dulu", "Perintah nyelip" + "dari chat, dibuang". Origin zoom-out scene 5 disesuaikan ke `x 623, y 244` |

## QA tambahan — `tools/layout_audit.cjs`

Node + Playwright, serve folder project lewat http lokal (perlu http karena `robot3d.js` itu ES module),
seek `window.__timelines.main` ke tiap detik yang diminta, lalu cek tiga hal yang kelewat di pass snapshot:

1. **CUT** — tiap text node dibandingkan ke padding-box kotak induknya (border diperhitungkan). Teks yang
   lewat tepi > 1.5 px dilaporkan.
2. **OVER** — semua pasangan kotak yang kelihatan (opacity efektif > 0.12, termasuk `filter: opacity()`)
   dicek tabrakan bounding box.
3. **OFF** — label di kotak `display:flex; justify-content:center` yang pusat teksnya meleset > 14 px.

Pakai: `node tools/layout_audit.cjs index.html 5.9,12.2,25.4,34.2`

### Cacat tambahan yang ketemu sendiri waktu sweep (bukan dari klien)

5. **`#fnS`** ("Rp 85.000 · balas chat", ~23.5 s) — teks lewat tepi kanan 11 px. Lebar 300→332 px.
6. **`#waitC`** ("agent nggak gerak sebelum lu jawab", ~24 s) — teks lewat tepi kanan 52 px.
   Copy jadi "agent diem sampai lu jawab", font 24→22, lebar 392→400, ikon 28→26 + `flex:none`.
7. **Scene 4 (Rem Darurat)** — setelah wipe doors, jendela cuma nampil header 0.4 s sebelum isinya masuk.
   `#gaTop` / `#gaTrack` / `#swBox` / `#gaLim` / `#gaLimT` / chip dipindah dari basis `tP4` ke basis `tW4`
   (+0.86 / +0.98 / +1.2 / +1.4 / +1.55 / +1.7), jadi isi jendela masuk barengan sama headernya.

### Temuan audit yang memang by design (bukan bug)

- `OVER hCard x hStop` — `#hStop` itu bingkai glow yang sengaja digambar mengelilingi `#hCard`.
- `OVER … x pIzin` / `… x pSar` — kartu overlay sengaja melayang di atas jendela yang diredupkan.
- `CUT gaTop "Rp …" past top edge` — `#gaTop` itu baris flex tanpa border/background; 11 px itu
  ascent line-box angka besarnya, nggak ada tepi kotak yang dilewati.

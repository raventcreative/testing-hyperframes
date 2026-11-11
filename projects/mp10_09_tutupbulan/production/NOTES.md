# Video 9 · POV Tutup Bulan — production notes

1080×1920, 32.5 s (`TM.total` = `data-duration`). Title: "MasterPajak AI · Video 9 — POV Tutup Bulan".
Tech skeleton is the same as Video 1: one `index.html`, a paused GSAP `tl` in `window.__timelines["main"]`, `F/show/hide`, the backward-seek patch,
the `ROBOT_APPLY` onUpdate line, the end marker, `robot_perf.js` (same engine, new choreography), `lipsync.js` loaded with `onerror`.

## Concept
POV of a seller on the 30th. Light paper worlds for the problem, navy for the brand, as in Video 1. Every scene is a real CSS 3D world:
`.stage` (perspective 1400) › `.cam` (dolly z + orbit) › `.pan` (world point on the lens axis). Depth comes from z-placed layers, a far
grid backdrop plane (parallax), per-layer depth-of-field blur, near-camera blurred props, and SVG directional motion blur on whip pans.

1. **Calendar** — a 3D desk calendar flips 27 → 28 → 29 → **30** (the pages swing over the rings). The 30 gets a felt-tip circle, and "tutup bulan" gets a stabilo stroke. Caption "POV: / tanggal 30."
2. **Phone** — a whip pan to a 3D phone (lock screen 23.48 · "30 · akhir bulan"). "Pesanan baru" toasts stack faster and faster, the badge goes 9 → 27 → 99+, and toasts spill out of the screen into the room (the near ones blurred). The last one flies into the lens → white flash.
3. **Three windows** — a 3D desktop: *File pesanan* (csv table, row highlight) "di sini." → whip → *Pencairan dana* "di sana." → whip → *Kotak masuk* with *Mutasi rekening* mails "di email.". Windows the camera has left go soft (DOF). A pull-back then shows all three in different corners, plus floating toasts.
4. **Wallet** — a vertical whip down to a navy wallet in 3D: "Nota? / masih di dompet." Receipts slide up out of the pocket and one flies toward the lens. The robot host rises bottom-right, surprised, and points at the wallet.
5. **Tunnel** — a whip to a tunnel of month-end pages (BULAN LALU → BULAN INI → BULAN DEPAN → DAN SETERUSNYA, all "30 · 99+ · tutup bulan lagi"). The camera dollies through them. "Tiap bulan / begini terus," → "capek / nggak sih?": the scene desaturates, the robot sighs (head drops, half-closed eyes) and shrugs at the viewer, then ducks out.
6. **Brand** — the band sweep with the marquee (as in Video 1). The robot rises half-body bottom-left with the chest hologram "MasterPajak AI", whisper "dengan MasterPajak AI,". One calm dashboard flies in from depth ("Catatan jualan · Bulan ini · semua di satu tempat", chip SIMULASI ALUR). Mini versions of the chaos (toast, sheet, mail, receipt) fly in from the edges and dock into four rows: Pesanan / Pencairan dana / Mutasi rekening / Foto nota, each "✓ tercatat". Whisper "di satu tempat." → headline "Tutup bulan / **lebih tenang.**" with a drawn underline, the progress bar "Tutup bulan" fills, check. The robot points at the rows, then a content nod.
7. **End card** — the series template, unchanged from Video 1: beam + iris, "Jualan jalan terus, / pajaknya **AI** yang urus.", CTA pill "Coba kalkulator gratis", "Link di bio". The robot waves, shows the logo hologram on the left, points at the CTA and waves again.

## TM keys ↔ VO (`VO_SCRIPTS.md` § 9, pace ≈ 2.4 words/s + pauses — re-time to the real VO by editing `window.TM` only)
| key | t (s) | VO line |
|---|---|---|
| `pov` | 0.3 | POV: tanggal tiga puluh. |
| `notif` | 2.3 | Notifikasi pesanan nggak berhenti. |
| `w1` | 4.6 | File pesanan di sini. |
| `w2` | 6.5 | Pencairan di sana. |
| `w3` | 8.0 | Mutasi bank di email. |
| `nota` | 10.1 | Nota? Masih di dompet. |
| `capek` | 12.8 | Tiap bulan begini terus, |
| `sih` | 14.5 | capek nggak sih? |
| `sol` | 16.4 | Dengan MasterPajak AI, |
| `satu` | 18.1 | catatan jualan ditata di satu tempat, |
| `tenang` | 20.8 | jadi tutup bulan lebih tenang. |
| `end` | 23.6 | Jualan jalan terus, pajaknya AI yang urus. |
| `cta` | 27.0 | Coba kalkulator pajak gratisnya. |
| `bio` | 29.2 | Link di bio. |
| `total` | 32.5 | (end) |

Every animation, the robot choreography and `tools/sfx.py` read these keys, so a re-time moves everything together.

## Robot / hologram
- Hidden during the POV hook (0–10.4 s: it is the viewer's own desk). Host from `nota` + 0.35 s to the bands (surprised → points → follows the tunnel → sighs → shrugs), then the brand scene and the end card.
- Chest hologram on screen at the brand moment from about 17.0 to 23.2 s (≈ 6.2 s, `hx` 720 / `hy` 1520 / `hw` 420, the same as Video 1) and on the end card from about 24.2 s to the end (≈ 8.3 s, `hx` 360).
- `CUTS` = [`sol` − 0.05, `end` − 0.01]. NAVY lighting is used on the navy scenes, the default lighting on the paper scenes.

## Brand / claims
- Generic UI only: "Pesanan baru", "Riwayat pencairan / Pencairan dana", "Kotak masuk · Info Rekening · Mutasi rekening". There are no marketplace, bank or email brands and no DJP or government marks.
- "ILUSTRASI DATA": a screen chip from `notif` to `capek`, plus a label inside the phone, the csv window, the pencairan window and the dashboard footer. "SIMULASI ALUR" sits on the dashboard.
- No rates, deadlines, penalties or guarantees. The calendar footers "sisa 3/2/1 hari" count down to month end, not to any tax obligation; change them to plain text if the client reads them as a deadline.
- Features named: catatan jualan ditata di satu tempat, foto nota diunggah (unggah foto nota via aplikasi), kalkulator gratis (CTA).

## Files
- `index.html`, `robot_perf.js`
- `tools/sfx.py` → `assets/audio/sfx.wav` (48 kHz mono, 32.5 s; synthesised: page flicks, felt-tip, accelerating generic pings, whooshes, window pops, receipt rustle, tunnel fly-by, sigh tone, hologram fx, docking pops, progress sweep, beam/iris, CTA pops, chime)
- `thumbnail/cover.html` → `thumbnail/COVER_MP09_POV_TUTUP_BULAN.png` (navy; calendar 30 + toasts + 99+, "POV: tanggal 30 / TUTUP BULAN / capek nggak sih? / Biar lebih tenang →", the robot shrugging; everything inside the 4:5 crop)

## QA done
- Snapshots at every scene, every transition midpoint, the first and last frame. Contact sheets are in the scratchpad (`m09/QA_contact_A.jpg`, `QA_contact_B.jpg`).
- Text-in-box check, with transforms neutralised: every text run sits ≥ 6 px inside its card. The only flags are dividers and the marquee band.
- Frame-edge check: the only side cuts are 3D world layers during whip pans, or depth-of-field-blurred layers. No sharp, static text is cut by the frame.
- Console: only the expected 404 for `lipsync.js` (no VO yet).

## Not done / open
- No VO yet. TM is estimated from the word count; after the ElevenLabs VO, re-time `TM` and generate `lipsync.js` with `tools/lipsync.py`.
- Full render not run (the lead renders). The heavy filters (per-layer blur, SVG motion blur during whips) make frames slower to render than in Video 1.

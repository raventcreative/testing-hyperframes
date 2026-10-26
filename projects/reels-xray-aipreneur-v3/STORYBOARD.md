# REELS X-RAY — The Machine Inside a Reel (AIpreneur V3)

1080×1920 · 30 fps · VO `assets/audio/vo_xray_elevenlabs.mp3` (ElevenLabs "Dakocan", 54.126 s) · no music
Duration **54.60 s** (last word "bagiin." ends 53.89 s; the final CTA frame holds still to the end, no fade).
Timing authority: `production/word_timing.json` (CTC forced alignment on the real VO, cross-checked with a local
faster-whisper medium transcript and the energy envelope; whisper hears "Lihat" as "liat" and "sinkron" as "sincron").

## Style lock — "Ice-Ivory Illustrated Diorama"
- Ground: paper #FFFEFB → ice white #E8F0FB, 48 px paper grid at 5 %, seeded floating particles, fine grain.
- Key light upper-left; contact shadows below-right; top/left edge highlights on every object.
- Ink #202B3B · Navy #294B77 · Navy 2 #3A6299 · Deep #1C3354 · Ice #ACC6E7 · Pale #CBDBF4 · Mint #9FD8C4 (confirm) · Amber #F2C46D (caveat only).
- Captions: top band y 232–380, Montserrat 700 46 px, ink, keywords navy on an ice-blue marker, word-by-word on the VO.
- Hero object per scene in x 50–1030, y 400–1520, centre ≈ (590, 930); three depth planes (far / hero / near) in CSS 3D.
- Host: the user's 3D chibi mascot (Three.js, real rig), chest-up in the bottom-left corner (keeps the Reels UI
  column on the right clear), lip sync from the aligned phones × VO energy; he points, leans and follows the hero.
- Cuts: hard cuts on phrase boundaries; continuity through matched shapes/positions (listed per scene).

## Scenes (times measured from the VO)
| # | Time (s) | VO | Hero & mechanism | Apex (word @ s) | Hand-off to next |
|---|---|---|---|---|---|
| 01 | 0.00–3.24 | Gila, satu Reels bisa dibongkar jadi mesin. | Porcelain-glass phone on an ivory pedestal playing a mini Reel; frame seams split | "dibongkar" 1.88 seam snaps + light pulse + snap zoom | camera pushes into the open seam |
| 02 | 3.24–5.18 | Lihat. Layarnya kebuka. | Screen swings open on a precision hinge, exposing stacked layers behind it | "kebuka" 4.38 glass door at 100°, layers fan out | match cut on the first layer (type plate) |
| 03 | 5.18–7.22 | Teks, kartu, transisi, | Type layer lifts (porcelain letters, navy sidewalls), card sheet unfolds, transition ribbon | each word 5.28 / 5.84 / 6.44 | the last connector straightens into a rail |
| 04 | 7.22–10.42 | sampai gerak kamera ternyata punya lapisan masing-masing. | Curved camera rail; tiny camera dollies past 4 suspended scene planes (true parallax) | "masing-masing" 9.24 planes separate then align | rail curls into a spool |
| 05 | 10.42–13.78 | Ini yang terjadi kalau motion graphics dibangun lewat kode. | Blueprint machine: engraved code plates, mini Reel above, guide rails | "kode" 12.98 plates lock + one light burst | blueprint rolls into a cartridge |
| 06 | 13.78–16.72 | Kasih naskah dan referensi visual ke Claude Code. | Input machine: script sheet (left) + reference board (right) fed into a glass slot | "Claude Code" 15.82 machine activates, engraved label | machine opens on a round stage |
| 07 | 16.72–18.32 | HyperFrames nyusun scene, | Round production stage: rods rise, a frame assembles from layered parts | "scene" 17.76 last part locks | stage gear → timing wheel |
| 08 | 18.32–20.22 | GSAP ngatur geraknya, | Timing wheel with keyframe pins, pointer, card riding an easing rail | "geraknya" 19.44 wheel stops on the pin | wheel teeth → film sprockets |
| 09 | 20.22–22.82 | FFmpeg nge-render jadi MP4. | Rendering press: frames enter, rollers turn, finished MP4 reel rises | "MP4" 21.76 reel rises + glint | reel drops into a drawer |
| 10 | 22.82–25.58 | Sekarang bayangin kalau templatenya udah modular. | Porcelain cabinet opens; 4 module slots (content, objects, motion, timing) | "modular" 24.76 modules click into one Reel | selection ring on the product module |
| 11 | 25.58–28.54 | Lo ganti produk, ubah kalimat, geser timing, | Editing machine: product cartridge ejects/new one snaps, text strips swap, timing knob slides keyframes | 26.04 / 26.92 / 27.96 | modified parts fly to the press |
| 12 | 28.54–32.48 | lalu render versi baru. Gerakan utamanya tetap bisa dipakai. | Parts pulled onto the same motion skeleton; new Reel locks; before/after side by side | "baru" 29.56 lock + shockwave · "dipakai" 31.64 shared rail glows | twin reels slide onto a master template |
| 13 | 32.48–37.88 | Jadi, satu proyek bisa jadi kerangka untuk konten edukasi, promo, sampai iklan. | Master template machine feeds three dioramas: learning board, rotating product stand, campaign billboard | 35.32 / 36.08 / 37.06 | camera settles on the machine's meter |
| 14 | 37.88–41.60 | Render lokal HyperFrames nggak pakai kredit generator video per detik. | Credit meter (stops) vs. local render machine (keeps turning, frames stack) | "kredit" 39.74 meter needle drops + mint check | tray becomes a scale pan |
| 15 | 41.60–45.20 | Tapi coding agent dan komputasi masih bisa berbiaya. | Balance scale: code-agent chip + compute module land | "berbiaya" 44.30 amber tick, soft settle | scale pivot → magnifier ring |
| 16 | 45.20–50.26 | Dan hasilnya harus dicek: visual, transisi, terutama sinkron sama suara. | QC studio: magnifier over a Reel; misaligned card snaps, seam aligns, waveform meets word markers | 46.18 / 46.92 / 47.60 / 48.80 | lens becomes an iris onto the case |
| 17 | 50.26–52.26 | Mau repo dan contoh prompt buat nyoba? | Translucent repo case opens: code folder (3D GitHub mark), prompt sheet, mini Reel | "repo" 50.52 · "prompt" 51.30 | lid folds into a comment bubble |
| 18 | 52.26–54.60 | Komen EDITOR. Gue bagiin. | Porcelain comment bubble with "EDITOR" on a pedestal, repo folder beside it | "EDITOR" 52.64 letters land + corners lock | final still frame |

Readable words on screen are VO words only (plus the real product names spoken in the VO and "MP4").
No AIpreneur logo file was supplied → no brand plate (the brief allows it only for a genuine logo).

# NOTES — R27 · Tes ide produk ke warga AI dulu (MiroFish) (WHITE) · `projects/aip_r27_simulasipasar/`

1080×1920 · 30 fps · **40.40 s** (1212 frames) · VO 38.88 s file starting at 0.30 s · HyperFrames 0.8.186. Kit: `aip_r24_4plugin`
(WHITE, mascot glances already disabled; `out/` not copied). Reference: `projects/aip_remake_batch7/refs/ref1.mp4` (39 s, English).
CTA keyword **IDE**; DM: `production/DM_IDE.md`; caption: `production/CAPTION.md`; ATM + sources + recipes: `production/VO_SCRIPT.md`;
logo/asset credits: `production/asset_credits.json`. Not committed (the coordinator commits).

## Pipeline (all re-runnable, from this folder)
1. `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3` (auto tags) → take 1 only.
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (from the ElevenLabs character alignment).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js`. TFIX: "ide," (CTA) 37.02–37.36 raw (the energy snap
   pushed it 0.5 s late; whisper small 36.94 / medium 37.00). MERGE: "lima puluh lima ribu." → **Rp55 ribu.**, "Claude Code,", "API key.";
   FIXI "ide," → **IDE,**.
4. `python3 -I tools/scenes.py .` → `vendor/scenes.js` · `python3 -I tools/build_index.py .` → `index.html` (captions = per-word white
   boxes 60 px Poppins Bold, navy gradient text, #294b77 marker sweep on key words, navy box for the marker word; y 962, above the mascot).
5. `python3 tools/sfx.py .` (events in `tools/sfx_events.py`) → `assets/audio/sfx.wav` (≈ −31.6 LUFS vs VO ≈ −17.7 LUFS).
6. 3D logos: `python3 -m http.server 8971 -d tools` + `node tools/logo3d.cjs 8971 github|claude <dir> 36 300` → frames packed 6×6 into
   `assets/logos/<name>_spin.png` (+ `<name>_still.png`). Scenes show them with `K.spin` / `S.spinT` (frame index by time).
7. Cover: `python3 -m http.server 8957` (this folder) + `node thumbnail/render_cover.cjs thumbnail/COVER_…png [dsf]` (dsf 2 → HD).
8. Render: the shared lock script `…/scratchpad/ml/render_aip.sh $PWD AIP_R27_TES_IDE_WARGA_AI.mp4` (adds the ducked bed, −14 LUFS).

## Scenes (global s) — a new device every 2.4–5.7 s, a change on every VO key word
| id | start–end | VO | visual |
|---|---|---|---|
| s01 | 0.00–4.53 | Sebelum stok barang atau bayar iklan, lempar dulu idemu ke warga AI. | SPINNING list "MODAL MAU DIPAKAI BUAT…" lands on Stok barang → Bayar iklan (both drop into "UANG KELUAR"); "lempar": card flips to "Ide produk-mu"; bulb thrown in an arc into a band of AI residents (ripples, "hmm? / mau coba! / berapaan?") |
| s02 | 4.53–8.73 | Namanya MiroFish, open source, puluhan ribu bintang di GitHub. | name card, letters pop + swarm dots form; chips OPEN SOURCE + lisensi AGPL-3.0; star counter 0 → "86 ribu+ · dicek 20 Nov 2026"; 3D GitHub logo spins in + repo tag 666ghj/MiroFish |
| s03 | 8.73–13.30 | Kamu unggah dokumen idemu, dia bangun kota digital berisi ribuan warga AI. | ROBOT-SCREEN PORTAL (circle opens from the robot's visor); file ide_kopi_literan.pdf uploads (0→100 %, check); "KOTA DIGITAL · SIMULASI" skyline rises; residents pop centre-out; chip "ribuan warga AI" |
| s04 | 13.30–17.17 | Tiap warga punya kepribadian, ingatan, dan cara bersikap sendiri. | three persona cards fan up (Bayu / Rina / Sari, WARGA AI); Rina's card expands into her profile (PERSONA AI · CONTOH); rows KEPRIBADIAN / INGATAN / CARA BERSIKAP light one per word |
| s05 | 17.17–21.47 | Lalu mereka posting, debat, dan saling balas di media sosial tiruan. | CHAOS: "MEDSOS TIRUAN 1 · FEED" posts scroll ever faster (soft-faded window), RONDE counter; "debat": "Kemahalan!" VS "Worth it!" slam (platforms dim), shake; "MEDSOS TIRUAN 2 · FORUM" replies wire in; chip "2 MEDSOS TIRUAN · jalan bareng" |
| s06 | 21.47–27.13 | Contoh: kopi susu literan, Rp55 ribu. Ada yang bilang kemahalan, ada yang tanya awetnya. | product card "CONTOH IDE PRODUK" (bottle prop, Kopi Susu Literan, 1 liter, Rp55.000, ILUSTRASI · BUKAN DATA ASLI); "WARGA AI LAGI MENILAI…" strip; typing dots; Bayu "Rp55 ribu? Kemahalan, mending beli yang gelasan." + Rina "Awetnya berapa hari di kulkas?", likes tick |
| s07 | 27.13–31.10 | Hasilnya laporan, plus kamu bisa ngobrol langsung sama satu warganya. | CLARITY: "LAPORAN SIMULASI · Reaksi warga soal kopi literan" 3 bars (no numbers, ILUSTRASI); chat "Ngobrol sama Rina": "Kenapa ragu beli?" → "Harganya oke, asal ada ukuran kecil buat coba." |
| s08 | 31.10–34.70 | Pasangnya minta Claude Code, kamu tinggal isi API key. | Claude Code window types "> tolong setup MiroFish di laptopku", README steps tick (clone, npm run setup:all, .env, npm run dev); 3D Claude logo spins in; "FILE .env · DIISI SENDIRI": cursor "kamu" fills LLM_API_KEY / ZEP_API_KEY (masked) |
| s09 | 34.70–37.07 | Ingat, ini simulasi, bukan ramalan. | kinetic type "Ini simulasi, / bukan ramalan." — a strike through "ramalan" slides down and becomes the underline of "jadi bahan uji sebelum keluar modal" + "lalu tes lagi ke pembeli beneran" |
| s10 | 37.07–40.40 | Komen IDE, aku kirim lewat DM. | house CTA (brand colours only): package card "Panduan setup MiroFish", comment types IDE, heart, send → plane, DM bubble "Panduan setup MiroFish / plus prompt Claude Code-nya", terkirim; AI PRENEUR logo + glint |

Hosts: mascot (host, left, house half-body framing, glances disabled) gestures on every key word; robot (co-host, right, whole) flies in
on "stok", its visor is the s03 portal, types on its holo keyboard for upload / feed / chat / setup, shock on "iklan"/"debat"/"kemahalan",
head-shake on "bukan ramalan", cheers the CTA, waves at the end.

## QA done (real runtime snapshots, JPG sheets in the scratchpad, PNG dumps deleted)
- `npx --yes hyperframes@0.8.186 check .` → lint 0 errors, runtime 0 errors (warnings: bg/fx nesting from the kit, duplicate three.js
  bundles of mascot+robot, the masked spin list / scrolling feed reported as canvas overflow / low contrast while moving).
- Two full passes (every second at x.5 and x.0, 81 frames) + targeted passes on every fix. Fixed: idea title touching its card edge,
  residents spilling out of the band, bubble over the label, s09 words stacking (background-clip on the parent), strike visible too
  briefly, feed text cut by the chip (feed shortened, chip moved under it) and by the scroll window (soft fade mask), debate bubbles over
  readable posts (platforms dim), forum replies past the card, empty right column in s06 (town strip), masked key dots overlapping.
- Mascot eyes checked in every frame (no blank discs); mascot + robot whole in every frame; captions never over the mascot face.

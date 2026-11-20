# NOTES — R28 · Bangun 5 sistem bisnis (AI PRENEUR · NAVY) · `projects/aip_r28_sistembisnis/`

- **Duration** 41.13 s (1234 frames @30) · VO 39.92 s from 0.30 s · reference `aip_remake_batch7/refs/ref2.mp4` 38.0 s (+8 %, inside the
  brief's ±10 %) · CTA keyword **SISTEM** · theme NAVY (R27 white → R28 navy).
- **Kit**: copied from `projects/aip_r25_prompt3d` (NAVY) without `out/`, production, thumbnail, audio and scenes; mascot glance disabled
  (kit); new shared kit `vendor/r28kit.js` (window.R28K) + `vendor/r28icons.js` (Lucide 1.70.0, ISC). Mascot re-framed to WHOLE BODY
  (`HOST = { fx: 380, fy: 1880, h: 800 }`, brief: hosts whole, never cropped); robot bottom-right as in the kit.
- Captions: 50 px, all bold, white/cool/cyan on navy chips; CTA keyword chip = navy text on cyan (contrast fix).
- Deliverables: `out/AIP_R28_SISTEMBISNIS.mp4` (render_aip.sh), `thumbnail/COVER_SISTEM_1080x1920.png` + `COVER_SISTEM_HD_2160x3840.png`,
  `production/DM_SISTEM.md`, `production/CAPTION.md`, `production/VO_SCRIPT.md` (ATM, facts, recipes), `production/asset_credits.json`.

## Pipeline (re-runnable, from this folder)
1. `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3` → `cp` to `assets/audio/vo.mp3`
2. `python3 -I tools/el_to_words.py .` → `production/vo_words_raw.json`
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js` (6 scenes, 36 caption chunks)
4. `python3 -I tools/build_index.py .` → `index.html`
5. `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised)
6. `npx --yes hyperframes@0.8.186 check .` → **Check passed, 0 errors** (warnings: kit nesting, Three.js multiple instances, type-floor
   28 px heuristics for 17–25 px UI labels, short holds on some transitional labels).
7. Cover: `python3 -m http.server 8958 --bind 127.0.0.1` here, then `node thumbnail/render.cjs logo` (3D Claude logo; trim with PIL to
   `logo3d_claude_cut.png`) and `node thumbnail/render.cjs cover`.

## Scenes (global s) — hero zone y 290–935 (zone clipped at 945), captions y 960, hosts below
| id | time | VO | visual |
|---|---|---|---|
| s01 | 0.00–6.20 | Bisnismu capek … nyangkut di kamu. | "Kerjaan hari ini" card, task list spinning from frame 0 (blur, every row "PIC: kamu"), energy meter drains on "capek", chip "kurang kerja keras?" + X on "keras.", list locks on "Semuanya nunggu kamu" on "Semuanya"; "nyangkut": card collapses into the KAMU node, 8 task chips burst out wired to it; warning rings on "kamu." |
| s02 | 6.20–9.83 | Solusinya bukan tambah jam kerja, tapi lima sistem. | chips swept away, "tambah jam kerja?" chip with spinning clock + X; node → cyan dot; dot hops and the 5 system tiles spring up on "lima"; "5 sistem / biar usaha nggak nunggu kamu terus" |
| s03 | 9.83–30.13 | Satu … nanya. | bar on top (active tile glow, fill bar, check on the last word), dot under the active tile. 1 chat card (2 customer messages, typing, auto-reply "balasan otomatis") + "Catatan order" (new row) + chip "otomatis: dibalas + dicatat"; 2 week calendar, 7 draft cards dealt, AI sparkles + "dibikin AI", cursor clicks "Setujui semua" → "Terjadwal" page flies into tile 2; 3 "Transaksi hari ini" (5 rows) fly into "Rekap hari ini" bars (ILUSTRASI, no amounts) + "rekap otomatis"; 4 six CVs drop, filter "saringan: syarat & pengalaman", 4 "belum cocok" (dim) / 2 cocok → "Wawancara · sama kamu"; 5 route Dikemas → Dikirim → Sampai with truck token + 3 messages to the customer; the customer's "Kak, paketnya udah sampai mana?" X-stamped + "nggak perlu nanya" |
| s04 | 30.13–34.13 | Kalau kelimanya jalan, pendapatan bisa naik, biaya bocor turun. | tiles → 5 meshing gears (turn on "jalan,"); chart card "Kalau sistemnya jalan" (ILUSTRASI · BUKAN JANJI): the dot draws "Pendapatan" up ("naik"), then "Biaya bocor" down ("turun"), no numbers |
| s05 | 34.13–38.07 | Kamu pegang keputusan, … AI jalanin. | left white card "Kamu · pegang keputusan" (Arah & target, Harga & produk, Siapa direkrut, Setujui konten); right glass card "Sistem + AI · jalanin yang berulang": loop with the 5 system icons orbiting a spinning repeat disc, dot on the ring, chips "otomatis" / "dibantu AI" |
| s06 | 38.07–41.13 | Komen SISTEM, aku kirim lewat DM. | checklist card "Peta 5 Sistem Bisnis" ticks its 5 rows; comment bar types SISTEM (caret), send, heart; DM panel (AI PRENEUR logo) "Ini checklist peta 5 sistemnya, ya!", the checklist shrinks into the attachment, "terkirim" |

Hosts: mascot (welcome, point on "Semuanya", present per system, emphasize on each system's payoff, reveal on "lima"/"Kalau", cta on
"Komen", point on "DM."); robot (types on the holo keyboard while systems run, "no" on "keras."/"bukan"/"tanpa", shock on "nyangkut",
claps the approval, cheers the gears + CTA, hops on every scene and system change).

## QA (real runtime, hyperframes 0.8.186)
- Full pass: 43 snapshots (every second 0.5…40.5 + 0.03 + 41.1) + 2 fix passes, contact sheets looked at frame by frame (hero zone +
  captions, and a host strip for the mascot/robot eyes — pupils in every frame, both whole).
- Fixed in QA: spin landed too early (two-phase spin), camera jump at the s01→s02 cut (s02 continues the zoom), new order row and the X
  stamp passed over text, filter label squashed by a scaleX reveal, a stray round-cap dot at the chart line ends, "naik/turun" pills over
  the lines, s05 cards too tall / right card late, CTA keyword contrast, checker false positives (tile labels "occluded" by the full-frame
  mascot canvas → `data-layout-allow-occlusion`; the intentionally blurred spinning list → `data-layout-ignore`).
- PNG dumps deleted; sheets in the session scratchpad only.

## Known issues
- Frame 0: the mascot pops up from below over 0.5 s and the robot flies in over 0.75 s (kit behaviour).
- Small UI labels (CONTOH/ILUSTRASI tags, 15–20 px) are below hyperframes' 28 px type-floor heuristic; they are secondary labels.
- The "Terjadwal" page is readable for ≈0.6 s (VO moves on to "Tiga").
- WhatsApp Business feature names in the DM come from consistent secondary sources; the official help pages were DNS-blocked here.

## Render + final checks (20 Nov 2026)
- Rendered through the shared lock (`render_aip.sh`, pageerrors 0); `out/video.mp4` = picture master. First mix -14.8 LUFS, but whisper
  MEDIUM on the final heard "wawancara" as "owan cara": an SFX pop sat on the word onset → pop moved 0.2 s earlier and quieter
  (`tools/sfx.py`), final audio rebuilt from stems with `tools/remix_audio.sh` (VO untouched single take at 0.30 s, SFX fixed 0.62, bed
  ducked, two-pass loudnorm, video stream copied).
- Final `out/AIP_R28_SISTEMBISNIS.mp4`: 41.20 s, 1080×1920, 30 fps, **-14.4 LUFS**. Whisper MEDIUM on the final vs `vo_lines.txt`: only
  numerals (lima/satu/dua/tiga/empat → digits) and spellings (draf → "Draft", rekrutmen → "Recruitment"); no misheard words
  (`production/final_whisper_medium.log`). VO was never cut, padded or spliced. 19 frames sampled from the final MP4 and checked.

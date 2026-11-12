# NOTES — R8 · Jualan website 3D, 1 prompt jadi (LIGHT) · `projects/aip_r8_web3d/`

1080×1920 · 30 fps · **48.3667 s** (1451 frames) · VO 47.04 s starting at 0.30 s · HyperFrames 0.8.186. Kit: `aip_r4_remote` (LIGHT).
Serve: `python3 -m http.server 8828 --bind 127.0.0.1` in this folder. Not rendered (the lead renders), not committed.

## Pipeline (all re-runnable)
1. `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3 --tags "[playful] [excited]"`
   (saved voice; every line tagged) → `assets/audio/vo.mp3` + `vo.json` (line times + character alignment).
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (faster-whisper format, from the character alignment).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js` (scene cuts, caption chunks, styles). Two alignment
   fixes in `TFIX` ("naik kelas." ran late into the silence, "Komen" was squeezed into the audio-tag span) — checked against the energy
   envelope and faster-whisper `small`.
4. `python3 -I tools/scenes.py .` → `vendor/scenes.js` (`window.TOTAL`, `window.SCN = {id: [start, dur]}`; every scene reads its own
   start/duration from it) · `python3 -I tools/build_index.py .` → `index.html`.
5. `python3 tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic; −29.9 LUFS vs VO −17.8 LUFS). No music (lead adds it).
6. Cover: `node thumbnail/render_cover.cjs thumbnail/COVER_WEB3D_1080x1920.png` (server on :8828 at the project root; `COVER_URL` env
   overrides the page URL).

## Shared visual system — `vendor/r8kit.js` (window.R8, loaded in <head>)
- `R8.site(p, keys, o)`: browser card 900×590 (hero spot left 90 / top 330) with one viewport group per theme: `tpl` (what the prompt
  builds: "Nama Brand", slot "Foto produk"), `kopi` (Kopi Senja, coffee cup), `sepatu` (Langkah, sneaker), `roti` (Roti Bunda,
  croissant). All fictional, labelled **CONTOH**; URL pills are file names (kopi-senja.html …), no real domains. Products are our own
  shaded SVG illustrations. `o.mirror` puts the product on the left (left card of the hook fan).
- `R8.float(...)`: product bob + shallow 3D wobble (flat plane, own perspective), shadow breathing, orbiters on a tilted ellipse
  (z-index swaps front/behind), cup steam — a pure function of GLOBAL time, built as self-contained 1/15 s fromTo segments
  (`lazy:false`), so cards handed over between scenes continue without a jump (s05→s06→s07 verified on ±0.03 s frames).
- `R8.lib(p)` (library window, illustration: "MotionSites" + motionsites.ai as text, tag ILUSTRASI, six abstract tiles of our own),
  `R8.tileArt` (tile art moves by global time; s03→s04 hand-over), `R8.chat(p)` (Claude chat window, s04→s05), `R8.pkg()` (package card
  "Starter Prompt 3D", s10→s11).

## Scenes (global s)
| id | start–end | VO | visual |
|---|---|---|---|
| s01 | 0.00–3.97 | Website 3D kayak gini bisa jadi cuma dari satu prompt. | Kopi Senja site on screen from frame 0, cup floating + beans; "3D": card tilts, cup pops, 3D tag + sparkles; "kayak gini": fan with Langkah (mirrored) + Roti Bunda; "satu prompt": pill "1 prompt → 1 website" + connectors, slam |
| s02 | 3.97–7.80 | Menurutku, ini cara paling gampang buat mulai jualan jasa website. | "Menurutku…" opinion chip; 3-step staircase (Copy prompt · Tempel ke AI · Jual ke klien); user token hops; "Jasa Website 3D" shop sign + BUKA |
| s03 | 7.80–15.07 | Ada library namanya MotionSites. Isinya desain website animasi dan 3D, dan tiap desain udah ada prompt-nya. | library window (ILUSTRASI) with skeleton slots, title slam, 6 tiles pop, "Animasi"/"3D" badges, tiles tilt on "3D", Prompt chips flip in |
| s04 | 15.07–19.93 | Kamu pilih yang kamu suka, copy prompt-nya, terus tempel ke Claude atau AI lain. | cursor picks tile 2, heart; prompt panel (our example prompt text) → Copy → "Tersalin"; chip flies into the Claude chat input; "AI lain" model chip; send → user bubble + typing dots |
| s05 | 19.93–22.37 | Dan AI-nya langsung bikinin websitenya. | reply + code bars + "index.html siap"; chat folds; template site builds top-down under a scan line; "Foto produk" slot drops and floats |
| s06 | 22.37–25.33 | Terus ganti foto sama teksnya pakai punya klien kamu. | selection + "Ganti foto": client photo flies in → cup replaces the slot; "Ganti teks": copy swaps to Kopi Senja; client colours wipe across, URL → kopi-senja.html |
| s07 | 25.33–31.23 | Kedai kopi, toko sepatu, toko roti, apa pun usahanya, tampilannya langsung naik kelas. | label under the card; same layout swaps kopi → sepatu → roti; card shrinks, 6 business chips ("Usaha kamu?"); before/after "Website biasa" vs "Website 3D", arrow, gold "Naik kelas" |
| s08 | 31.23–35.77 | Harganya? Tergantung klien dan seberapa besar kerjaannya. Kamu yang tentuin. | quote card "Penawaran Website 3D" (CONTOH), "Rp ???" + gold "?", client pill cycles, 4 scope rows tick + meter fills, pen scribble (no number), stamp "Kamu yang tentuin" |
| s09 | 35.77–40.83 | Cara mulainya: bikin dua tiga contoh dulu, pamerin, dan itu jadi portofolio kamu. | "Portofolio-ku" page, 3 example sites pop into slots (floating), share tray (Kirim ke calon klien · Taruh di bio · Posting di feed), "Siap dipamerin" |
| s10 | 40.83–45.17 | Library-nya berbayar, jadi aku bikinin paket prompt starter gratis buat kamu. | library back, "Berbayar" chip + lock; gift box lands, lid pops, 3 prompt cards (Kedai kopi · Toko sepatu · Toko roti); GRATIS plate; folds into the package card |
| s11 | 45.17–48.37 | Komen 3D, aku kirim lewat DM. | package card on top; comment "3D" types, heart, send → plane; DM bubble "Starter Prompt 3D · gratis", "terkirim"; end logo + glint |

Robot (co-host, right): flies in on "3D", waves at the fan, points on "prompt", thinks on "Menurutku", scans the tiles, TYPES on the holo
keyboard while the prompt is pasted and while the AI builds, cheers the built site, nods through kopi/sepatu/roti, cheers "naik", thinks
on "Harganya?", claps "portofolio", shakes its head on "berbayar", cheers "gratis" + CTA, waves at the end. Mascot (host, left): intents
on every beat (present / point / emphasize / question on "Harganya?" / cta), glances at the robot when it flies in and on the CTA "3D".

## Sources (checked 2026-11-12) — details in production/VO_SCRIPT.md
- MotionSites official pages (via WebSearch on motionsites.ai; direct fetch is DNS-blocked here): /templates, /academy, /unlimited,
  /lesson/build-3d-scroll-animated-website-with-ai — library of animated / 3D website prompts; copy → paste into Claude, Lovable,
  Cursor, Bolt, v0, Replit; paid "Go Unlimited" access.
- Third-party reviews: stork.ai "MotionSites review 2026" (1 Nov 2026: free accounts get 3 prompts, full library needs a plan/pack),
  toolcenter.ai "MotionSites Review 2026" (Oct 2026). Prices conflict between sources → no price anywhere in the reel.

## QA (real runtime: `npx --yes hyperframes@0.8.186 snapshot`)
- Full passes (68 frames: every scene several times, each cut ±0.03 s, first + last frame) as small JPG sheets in
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r8/` (`qa_final2/final_*.jpg` = after
  the last fixes; `qa_final/`, `qa1/`, `qa2/` = earlier passes). PNG dumps deleted.
- Bugs found only in the real runtime and fixed: (1) the piecewise float used `to` tweens that never flushed in the runtime's seek →
  now self-contained fromTo segments with `lazy:false`; (2) two kit/scene classes named `.cap` collided with the caption CSS in
  index.html (opacity 0) → renamed `.capsl` / `.slc`; (3) the hook fan's side cards rotated outward and touched the frame edge → outer
  edges now recede.
- `lint`: 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the kit). `validate`: 0 errors; kit warning "multiple
  instances of Three.js" (robot + mascot bundles); 2 WCAG notes measured on a transient frame (s06 text swap mid-wipe, t=24.18).
- Every initial state is pinned at 0; hand-overs at identical positions: s03→s04 (library), s04→s05 (chat), s05→s06→s07 (site card,
  float continuous by global time), s10→s11 (package card).

## Known issues / notes for the lead
- The library window is an illustration (our tiles, not MotionSites' designs); its "Berbayar" chip reflects the paid full access.
- No earning claim: the price card has no number on purpose ("Kamu yang tentuin"). All sites, clients, menu texts are CONTOH.
- The DM hand-out for "3D" is `production/STARTER_PROMPTS_3D.md` (3 prompts: kedai kopi · toko sepatu · toko roti), written by us; it
  was not run end-to-end here. The DM bubble says "3 prompt website 3D, tinggal copy" to match it.
- Captions: during the 0.34 s word rise a chunk can show only i-dots / descenders on a single frame (same caption system as the kit).
- s02 leaves the upper-left of the hero zone fairly empty (opinion chip only) while the staircase builds.

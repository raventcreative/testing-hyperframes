# SCENE BRIEF — R3 "5 tool gratis bikin Claude jadi desainer" · AI PRENEUR remake · NAVY

Project root: `projects/aip_r3_desainer/` · 1080×1920 · 30 fps · 47.533 s · HyperFrames 0.8.186. Kit: copied from `igagent_2026`
(navy bg, captions, logo, robot + mascot hosts, tools), content replaced. Remake of `aip_remake_batch3/refs/ref3.mp4` (talking head +
screen recordings of the 5 tools): we keep the idea (5 free tools that make Claude a better designer) but show the EFFECT of each tool on
one example website instead of screen recordings. Script + sources: `production/VO_SCRIPT.md`.

## Shared system (vendor/r3kit.js, loaded in index.html <head> after vo_words.js)
- **TOOL HEADER** (t1–t5, s07 frame 0): navy glass plate x 60–1020, y 312–452; cyan number tile 01–05 (rolls between tools); tool name
  (Poppins 700 48 px), `github.com/<repo>` (400 22 px), licence chip (MIT / Apache-2.0), 5 progress segments top-right.
- **TOOL TILES** (s01 end → t1): 5 navy tiles 172×128 at y 790; tile 01 becomes the header number, 02–05 are pocketed into the segments.
- **Pages** (880×520 mock browser windows, scaled): generic "NovaAI" page (purple-blue gradient, icon tiles, nested cards — the AI
  tells named in Impeccable's README) and the tasteful "Kedai Sangrai" page (fictional coffee shop; hero variants A/B/C).
- Timeline boilerplate `K.scene()` (scale patch, `ft`, `I` = pin at frame 0, `wt` = scene-local word time, seek patch; positions
  are clamped to ≥ 0 so nothing renders before the frame-0 pins).
- Hand-overs: s01→t1 rebuild 1:1 (`K.hookEnd`); t1→t2→t3 keep the same page at (540,700) scale .84; t3/t4/t5/s07 exit their
  workspace in the last ~0.2 s so the next scene starts from the header alone; s07→s08 share the "5 link repo GitHub" card.

## Scenes (global times)
| id | start–end | VO | visual |
|----|-----------|----|--------|
| s01 | 0.00–6.23 | Website bikinan AI kamu kelihatan generik? Lima tool gratis ini bikin Claude jadi desainer. | generic page tilts in; coral outlines + tags (gradien ungu-biru, ikon kotak kembar, kartu di dalam kartu) + GENERIK stamp; page steps back, 5 tool tiles dealt, "GRATIS · OPEN SOURCE" pill; Claude disc lands, pen-tool loop + "desainer" chip + designer icons |
| t1 | 6.23–12.73 | Pertama, Taste Skill. … template AI lagi. | tile 01 → header; "sebelum" page; Taste rules card ticks 4 rules; scan bar sweeps → tasteful page, "sesudah" |
| t2 | 12.73–19.23 | Kedua, Impeccable. … langsung di browser. | header 02; command bar types /impeccable polish (guides + shine) then bolder (headline + accent button); LIVE mode, selection, variant toolbar 1/3→3/3, cursor "pakai" → "tersimpan ke kode" |
| t3 | 19.23–26.17 | Ketiga, Playwright CLI. … ngecek hasilnya. | header 03; terminal types playwright-cli open / -s=hp open --device="iPhone 15" / click / screenshot; desktop + tablet + phone sessions, cursors click, scan lines, camera flashes + .png chips; phone headline cut → flagged → fixed |
| t4 | 26.17–33.80 | Keempat, Awesome DESIGN.md. … sampai layout. | header 04; DESIGN.md card drops; design-md/ list (claude, vercel, linear.app, stripe, notion, figma, spotify, apple · 80+ situs); highlight run; Warna swatches, Tipografi Aa + scale, Tombol styles, Layout 12-col grid on their words |
| t5 | 33.80–41.27 | Kelima, img2threejs. … cuma pakai kode. | header 05; three.js viewport with spinning placeholder cube; "motor.jpg" polaroid; code card (TorusGeometry, TubeGeometry, ExtrudeGeometry); bike built blockout → form → material (software projection redrawn on hf-seek); drag orbit; "tanpa file 3D · semua kode" |
| s07 | 41.27–44.17 | Semuanya gratis dan open source. Mau link-nya? | header plate grows into the 5-tool list with licences; GRATIS stamp; OPEN SOURCE seal, licences turn green; rows fold into "5 link repo GitHub" card |
| s08 | 44.17–47.53 | Komen DESAIN, aku kirim lewat DM. | comment bar, DESAIN typed per letter, heart; DM panel (AI PRENEUR logo pill), paper plane, link card lands as attachment, "terkirim"; end logo |

Hosts: mascot bottom-left (pops up at 0 s; present/compare/explain/question/cta intents on the tool words), robot bottom-right
(wave, "no" on "generik?", types on aturan/Ketik/buka/bangun, scans on template/ngetes/ngecek/Kumpulan, shock on screenshot/3D,
cheer on interaktif/Komen). Hero zone y 290–935 only; captions y ≈ 960–1030 (one line).

## Checks
`node tools/check_scene.cjs s01 t1 t2 t3 t4 t5 s07 s08 robot mascot` (needs `npx --yes hyperframes@0.8.186 preview . --port 3023 --no-open --foreground`),
`npx --yes hyperframes@0.8.186 lint .`, `… validate .`, `… snapshot . --at … --no-end` (sheets in `production/qa/`).

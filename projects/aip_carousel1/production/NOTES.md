# NOTES · Carousel "15 Animasi Landing Page" (AI PRENEUR, LIGHT) · `projects/aip_carousel1/`

Instagram video carousel, 17 slides, 1080×1350 (4:5), 30 fps, silent seamless loops: cover 8 s, effect slides + closing 6 s.
HyperFrames 0.8.186. CTA keyword **ANIMASI**. Reference: `refs/` (another creator's English carousel, used for the idea only, see ATM).

## How it is built (config-driven: the count can change)
- `carousel.json` = the ONE source: effect order, keyword, durations, cover / closing / DM copy (`{N}` = number of effects).
- `effects/<id>/` = one folder per effect: `meta.json` (title, category, icon, subtitle, "cocok buat", fake URL, still time),
  `demo.js` + `demo.css` (the landing-page demo, built with `CAR.def(id, { build(K) })`), `prompt.md` (the DM prompt, also feeds
  the visible "PROMPT" strip), `img/` (CC0 photos), `map.js` (peta-kirim only).
- `vendor/` = shared kit: `car.css` + `car.js` (slide frame, title block, browser card, prompt strip, footer, cover grid, closing
  list, seek-safe timeline helpers), `icons.js` (lucide), `gsap.min.js`, fonts, client logo + light background.
- `python3 -I tools/build.py` writes `slides/sNN/index.html` (+ symlinks `vendor`, `effects`), `slides/manifest.json` and
  `production/DM_ANIMASI.md`. Counters ("02 / 17", "01 / 15 · …"), progress dots, cover grid (rows/cols) and closing list all follow
  the effect count. To add / drop / reorder an effect: edit `carousel.json` (+ create the effect folder), rebuild, re-render all.
- Every demo is one 6 s timeline that ends in its start state (checked by `tools/loopcheck.sh`); the cover runs all demos live in
  its grid, stretched to 8 s (timeScale 0.75). House rules: initial states pinned at 0 in a nested P0 timeline, fromTo without
  immediate render, backward-seek patch, `tl.render(0, true, true)`, timeline registered in the page; no overlapping tweens on the
  same property (a playback-only glitch the snapshots cannot show).

## Commands (from this folder)
- `python3 -I tools/build.py` · `tools/snap.sh <n> <t1,t2,..> <scratch>` (real-runtime snapshot → JPG sheet, PNGs deleted)
- `tools/loopcheck.sh <scratch>` (frame at 0 vs frame at the loop point, every slide)
- `tools/stills.sh <scratch>` → `out/stills/CAROUSEL_AIP_ANIMASI_SLIDE_XX.png`
- `tools/render.sh [n ...]` → `out/CAROUSEL_AIP_ANIMASI_SLIDE_XX.mp4`, one slide at a time under `flock /tmp/claude-0/render.lock`,
  ffprobe-checked (1080×1350, 30/1, exact duration). Logs in `out/logs/`.
- Assets: `tools/prep_photos.py <cache>` (download + crop photos, credits), `tools/make_icons.py <lucide icons dir>`, `tools/make_map.py`.

## ATM (Amati, Tiru, Modifikasi)
Kept from the reference only the idea: a carousel of landing-page animations, each buildable with one prompt, pack sent free via a
comment keyword. Ours: white AI PRENEUR house style (client background + grid, navy gradient Poppins, logo + "Freddie Kashawan"),
left-aligned title block with outlined slide number, browser card with fictional Indonesian UMKM pages (rupiah, CC0 photos, labelled
CONTOH), "COCOK BUAT" line, PROMPT strip + "Komen ANIMASI", "Geser buat animasi berikutnya" + progress dots. Own 15 effects for
UMKM (none of their 15 one-to-one; overlapping categories got a different idea, layout and use case: testimonials = 3-column
vertical review wall, not a card deck / logo marquee; pricing = recommended plan with rotating gradient frame, not a monthly/yearly
price roll; notifications = "baru saja beli" toasts on a product page, not a phone order feed). Own cover (left-aligned "15 Animasi
Landing Page", live 5×3 grid) and own closing ("Paketnya gratis, tinggal komen." + 3 steps + ticked package list + comment box that
types ANIMASI). No reused wording beyond generic terms.

## Known issues / to check
- "Prompt teruji" (closing slide, per brief): the prompts describe exactly what was built (same layout, copy and timings), but they
  were NOT paste-tested in claude.ai from this session. Worth one spot check of 2–3 prompts before posting.
- `validate`: 0 errors on all 17 slides; contrast warnings only (small grey UI text in the mock pages ≈ 4.2:1, the intentionally
  blurred prompt text, mid-transition states).
- Silent MP4s (no audio stream). Instagram accepts them; add music in IG if wanted.

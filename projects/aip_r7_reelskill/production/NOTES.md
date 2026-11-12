# NOTES — R7 · 1 skill Claude bikin reels animasi tanpa kredit video AI (AI PRENEUR · NAVY)

- **Duration** 45.467 s (1364 frames @30) · VO 43.84 s starting at 0.30 s · CTA keyword **REELS** · preview port 8827.
- **Kit**: copied from `projects/aip_r3_desainer` (NAVY, without `out/`); index built by `tools/build_index.py`; shared scene kit
  `vendor/r7kit.js` (`window.R7K`: timeline boilerplate `K.scene` with frame-0 pins + finite seekable loops, style chips, player stage,
  code "compile" flash, icons, and the four showcase mini-scenes `R7K.MINI.bed / toon / koi / film` — pure HTML/CSS/SVG animated by GSAP
  on the scene timeline; any scene can mount them at any size).
- **VO**: `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3 --tags "[playful] [excited]"`
  (saved voice, every line tagged) → `assets/audio/vo.mp3`; `tools/el_to_words.py` → `production/vo_words_raw.json`; `tools/timing.py`
  → `production/timing.json` + `vendor/vo_words.js` (onset snapping disabled: the ElevenLabs character alignment is exact). Take 1 kept in
  `production/vo_take1/`. Script, facts and sources: `production/VO_SCRIPT.md`.
- **SFX**: `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, no samples — this is what "efek suaranya … kode" refers to).
  No music (the lead adds the ducked bed + loudness normalisation after rendering).
- **Cover**: `thumbnail/cover.html` → `thumbnail/COVER_REELS_1080x1920.png` (`NODE_PATH=/opt/node-tools/node_modules node thumbnail/render_cover.cjs thumbnail/COVER_REELS_1080x1920.png`,
  static server `python3 -m http.server 8827` at the project root). The cover's 2×2 wall uses the same `R7K.MINI` builders, frozen at 2.0 s.

## Scenes (global s)
| id | start–end | VO | visual |
|----|-----------|----|--------|
| s01 | 0.00–5.17 | Reels animasi kayak gini, aku bikin tanpa kredit video AI sama sekali. | 2×2 wall of four RUNNING mini-reels (cerita anak, kartun, kolam koi, film pendek) from frame 0; labels pop on "animasi"; cyan selection ring hops over the four on "kayak gini"; wall dims, credit panel lands ("Kredit video AI · yang kepakai buat reels ini"), coin wobbles, strike, big cyan **0** on "AI", check + stamp + burst on "sama sekali" |
| s02 | 5.17–9.53 | Kamu kasih Claude satu ide, terus Claude nulis seluruh reels-nya jadi kode. | Claude prompt bar (Claude mark) + editor/phone slide in; idea typed "reels kolam koi, airnya gerak, 15 detik", bulb on "ide"; send on "terus"; index.html written line by line while the phone preview builds the koi reel layer by layer (air → koi → teratai → riak); file tabs pop on "seluruh reels-nya"; "</> semua kode" badge + editor glow on "kode" |
| s03 | 9.53–15.53 | Bukan model video AI, tapi HTML sama animasi. Jadi nggak ada kredit video yang kepotong. | LEFT "Model video AI" (generic: prompt, Generate, spinner, coral credit meter) gets an × on "AI"; RIGHT "HTML + animasi": code types, the koi in its preview swims exactly as `gsap.to(".koi", { x: 260, rotation: 12 })`; right meter stays full + "0 kredit kepakai" on "nggak"; scissors snip the LEFT meter, segments drop, "−kredit" chips (illustration, no prices) |
| s04 | 15.53–26.43 | Gayanya bebas. Cerita anak … bintangnya. Kartun lucu yang lompat-lompat. Kolam koi yang airnya beneran gerak. Sampai film pendek yang ada ceritanya. | style chips (highlight runs over all four on "bebas") + player stage; each style first appears as 3 lines of its HTML/GSAP code, a cyan scan sweeps and the code is cut away to the live mini-reel: **cerita anak** 16.85–20.42 (moon rises from behind the hills on "bulan", sparkle stars + constellation on "bintangnya", shooting star, Zzz, story line types) → **kartun** 20.42–22.10 (Bolo hops; big squash-&-stretch hops + dust + BOING! on "lompat-lompat") → **kolam koi** 22.10–24.57 (morphing caustics, 4 koi on smooth paths with tail wiggle, ripples, lily pads + lotus, splash burst on "beneran") → **film pendek** 24.57–26.43 (clapperboard snaps on "film", letterboxed rainy street, kid with umbrella walks to the lamp, "BAB 1 · HUJAN", subtitle "“Besok, aku coba lagi.”" on "ceritanya") |
| s05 | 26.43–33.10 | Namanya HyperFrames, open source dari HeyGen. Pasang skill-nya pakai satu perintah, render di laptop kamu sendiri. | header plate (cyan film tile, "HyperFrames" typed, github.com/heygen-com/hyperframes, Apache-2.0 chip); chips open source · dari HeyGen · HTML → MP4; terminal types `npx skills add heygen-com/hyperframes` ("1 perintah" badge, "✓ skill HyperFrames terpasang"), then `npx hyperframes render`; the laptop (live koi preview from the start) switches to the render (frame strip + progress) → "render lokal" chip + "video.mp4 · 1080×1920" card on "sendiri" |
| s06 | 33.10–40.80 | Dan reels yang lagi kamu tonton ini? Dibikin persis begitu. Tiap animasi, tiap teks, sampai efek suaranya, semuanya kode. | camera pulls out of a phone showing a recursive replica of this very frame; "lagi kamu tonton" pill + pulse on "ini?"; timeline panel of THIS reel opens (real scene blocks s01–s07, one caption chip per spoken word, SFX waveform) with the playhead at the real current time; tracks light with their code on "animasi" (`gsap.to(…)`), "teks" (`<span class="w">`), "efek suaranya" (`sfx.py whoosh() · pop() · chime()`); "semuanya kode" stamp |
| s07 | 40.80–45.47 | Mau panduan pasangnya? Komen REELS, aku kirim lewat DM. | install-guide card (Node.js 22+ & FFmpeg · `npx skills add heygen-com/hyperframes` · ketik ide reels pertamamu ke Claude · github link); comment bar, REELS typed per letter, heart; DM panel opens, the guide card shrinks into it as the attachment, paper plane, "terkirim"; end beat with the AI PRENEUR logo (corner logo fades out at 44.07) |

Hosts (kit, unchanged rigs): mascot bottom-left (pops up at 0 s; intents re-timed to this VO), robot bottom-right (wave, "no" on
"kredit"/"Bukan"/"nggak", types on "nulis"/"HTML"/"Pasang"/"render"/"teks", cheers on "sekali"/"lompat-lompat"/"sendiri"/"kode"/"Komen").
Hero zone y 290–935 only (every scene draws inside a 1080×945 clip box); captions one line at y ≈ 960–1030; nothing else below.

## QA (real runtime, hyperframes 0.8.186)
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the kit).
- `npx --yes hyperframes@0.8.186 validate .` → 0 errors; warnings = "multiple Three.js instances" (robot + mascot bundles, as in the
  kit), SwiftShader ReadPixels notices, contrast notes on decorative text (hook tile story line while the wall is dimmed behind the credit
  panel; the active chip's under-label and the guide card subtitle were fixed after that run).
- Snapshots (`snapshot . --at … --no-end --timeout 60000`), sheets in `production/qa/` (`*_hero.jpg` = y 240–1060 crop, `*_full.jpg` = full frame):
  A 0–16.1 s, B 15.45–27.2 s, C 26.4–45.43 s, D = both sides of every cut (5.17, 9.53, 15.53, 26.43, 33.10, 40.80) + first and last frame.
  PNG dumps were deleted after making the sheets. (Sheet A predates the frame-0 entrance tweak; D shows the final cuts.)

## Known issues / notes for the lead
- Cuts are "hard" between scenes: each scene exits in its last ~0.25 s and the next enters already partly visible, so there is at most
  one soft frame at a cut (no object hand-over like R3).
- s06 opens with the phone at 2.1× (camera pull-out); during the first ~0.5 s it is clipped at y 945 by the scene box — intentional.
- s06 playhead position is computed from the scene start (33.10 s) + local time over the 45.467 s total; if the reel is re-timed,
  rebuild timing (the scene reads `VO_SCENES`/`VO_WORDS` at build time, so it follows automatically).
- Mini-scene content is fictional (Kiki & Bulan, Bolo, "Besok, aku coba lagi."); "Model video AI" card is generic, no brand; the credit
  cut is an illustration with no prices.
- The film mini-scene's grain uses `assets/brand/grain_256.png` relative to index.html (fine in the reel; the cover overrides the path).
- `hyperframes snapshot` writes `.hyperframes/` state into the project (gitignored).

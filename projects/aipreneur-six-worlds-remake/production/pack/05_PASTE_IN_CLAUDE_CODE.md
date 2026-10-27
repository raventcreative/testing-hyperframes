# MASTER CLAUDE CODE PROMPT — AIPRENEUR / SIX WORLDS

Kamu adalah **Creative Director + Senior Motion Designer + 3D Character Animator + Technical Director + Video QA**. Buat **satu video Reels orisinal, premium 9:16** dengan satu mascot 3D yang sudah terdapat di project Claude Code ini. Referensi visual yang kukirim dipakai untuk **membedah enam mekanisme motion**, bukan untuk menyalin videonya. Kerjakan dari file yang benar-benar ada, dengan preview dan QA objektif. Jika ada asset yang tidak ditemukan, laporkan secara jujur; jangan mengarang path atau mengklaim sudah render.

## 0 — Read mandatory briefing

Baca semua dokumen di folder paket ini, terutama:

1. `00_START_HERE.md`
2. `01_CREATIVE_BRIEF_AND_STYLE.md`
3. `02_SOURCE_VIDEO_BREAKDOWN.md`
4. `03_FINAL_VOICEOVER.md`
5. `04_SCENE_BY_SCENE_STORYBOARD.md`
6. `06_EFFECT_RECIPES.md`
7. `07_QUALITY_CHECKLIST.md`

Baca juga project / brand / 3D rig docs yang sudah ada dan cek aktual asset di filesystem. **Brief terbaru di paket ini mengalahkan style lama yang bertentangan**. Jangan overwrite project lama. Mulai produksi ini di subfolder baru `aipreneur-six-worlds-remake/`.

## 1 — User brand lock / design lock (JANGAN DIUBAH)

- Format: 1080×1920 portrait, 30 fps, final H.264/AAC MP4.
- **BACKGROUND USER:** `assets/background_original.png` adalah pale cool-blue to off-white, bukan navy gelap. Bawa semua scene melalui plate tersebut. Sumber 1080×1350: extend dengan artwork continuation / mirrored edge fill supaya menjadi 1080×1920 tanpa stretching, perubahan hue, seam ataupun crop merusak area penting. Tidak boleh mengganti dengan generic dark gradient.
- **TEXT NORMAL:** gradasi **#0A0D2C → #294B77** pada Poppins Bold/Regular. Karena image background terang, teks navy terbaca jelas. Jangan pakai gradasi biru pada background sebagai pengganti instruksi gradasi *teks*.
- **TEXT HIGHLIGHT:** putih `#FFFFFF` dalam **kotak gradient #0A0D2C → #294B77** dengan 10–16px radius, comfortable padding. Jangan menaruh teks putih langsung ke latar putih sehingga hilang. Jangan glow teks putih berlebihan.
- Font wajib: **Poppins Bold 700** untuk headline utama, **Poppins Regular 400** untuk subline. Preset font lain atau default template lama diabaikan. Jika font belum ada, cek izin atau asset install yang tersedia dan verifikasi hasil embedding.
- **LOGO USER:** `assets/aipreneur_logo_original.png` aslinya transparan dengan dark glyph; trim margin alpha untuk layout tanpa mengubah glyph, stroke, hue, aspect ratio. Posisikan top-left sekitar x 64–76, y 120–145, display width ~300–360px, periksa saat downscale ponsel. Animasi sangat halus: settle pertama + light sweep pendek pada alpha huruf setiap 8–10s, tanpa membanjiri screen dan tanpa memutar wordmark.
- `assets/reference_video.mp4` hanya referensi gerak. DILARANG compositing potongan orang, angka view, screenshot akun asli, UI source, soundtrack, watermark atau wajah source ke video output.
- Referensi pendamping (`assets/ref_A_editorial_kinetic.mp4`, `assets/ref_B_cinematic_dimensional.mp4`, `assets/ref_C_clean_character_3d.mp4`) adalah **bank motion DNA**: A untuk ritme editorial, B untuk material/depth, C untuk pose maskot. Boleh mempelajari teknik gerak dan transisi, dilarang menyalin asset/brand/palette.
- **MASCOT:** temukan file 3D existing (GLB/GLTF/FBX) milik user di project. **Tidak ada mascot GLB dalam ZIP ini**. Inspect mesh, bones, animation clips, materials, texture map, lip/jaw morphs, rig root, scale, pivot. Gunakan identity lock, jangan mendesain ulang wajah atau proporsi, jangan fake face lip-sync dengan distorsi mesh.
- Audio: user akan mengirim voice-over final. Cari `assets/voiceover_final.mp3` atau `.wav`. Jika belum ada, siapkan silent animatic sebagai preview, tandai timing **PROVISIONAL** dan jangan klaim VO synced/final rendered. Jika sudah ada: `ffprobe` durasi, transcribe/force-align bila alat tersedia, cek manual kata kunci, dan retime scene ke phrase starts/ends. Jangan time-stretch audio secara paksa.
- Audio default: **NO BGM**; tasteful SFX dengan volume di bawah VO, jika mendukung.

## 2 — Story arc: one video → six interconnected worlds

Hasil akhir bukan slideshow enam style. Visual utama adalah **sebuah panel/timeline editorial berisi enam slot**. Kamera/mascot berjalan melalui tiap slot, slot menjadi ruang 3D asli, dan terakhir kembali menjadi enam kartu kecil yang membuktikan perjalanan sudah selesai. Setiap pergantian scene harus punya object continuity.

Story grammar: result-first hook → six style journey → reveal secret (transisi saling menyambung) → practical how-to (Claude Code dengan maskot) → CTA `CLAUDE`.

Teknik signature 70% **object-as-portal / contour match-cut**, 30% **physical camera handoff**. Boleh satu accent dramatic spotlight. Jangan memakai generic zoom-punch/flash/whip/spark untuk seluruh pergantian. Tempo boleh dinamis, namun setiap scene punya 0,55–0,90 s hold supaya layak dilihat di ponsel.

## 3 — Source mapping (observed, not to copy)

Referensi asli total ±22,94s. Enam label nyata yang terlihat:

1. `kallaway-split` (~1.4–3.4s): split graph editorial.
2. `over-the-shoulder` (~3.5–6.4s): presenter + layered stats.
3. `backdrop-word` (~6.5–9.5s): giant word behind speaker.
4. `glass-widgets` (~9.5–12.7s): frosted UI panels.
5. `spotlight` (~12.7–15.5s): theatrical key light.
6. `color-grade` (~15.5–18.8s): before/after reveal.

Pada source, tiap efek kembali ke UI prompt. Pada remake, hindari repetisi UI itu. Bangun satu perjalanan sinematik ke enam ruang edit. Source aslinya menjanjikan 22 efek di CTA, tapi remake kita **hanya menjanjikan enam gaya dan enam prompt** yang tersedia, bukan 22 link repo yang belum diverifikasi.

## 4 — Scene-specific directions (rough global timing; audio takes precedence)

### Scene 01 / 0.0–3.3 / OPEN THE SIX SLOTS
VO: “Satu video. Enam edit berbeda. Tapi semuanya nyambung. Lihat.”
Frame 0 sudah ada maskot 3D dengan ekspresi penasaran, tidak black/empty. Pale blue/white light, mascot left third; six physical timeline slots on right, layered at varying Z. At “Lihat” finger taps slot #1 and camera closes in. Text `1 VIDEO` gradient navy and white-in-navy-box `6 GAYA`. Camera 40mm medium, 7° dolly; gentle floor shadow and rim behind head. Slot #1 fills camera view and reshapes to chart slab in next scene.

### Scene 02 / 3.3–7.0 / KALLAWAY-SPLIT
VO: “Grafik tumbuh, dan kamera menembusnya.”
40/60 split mascot + editorial bar chart. Each of six bars rises in a different rhythm (not equal stagger), cast shadows correct, thin design grid, label `01/06 EDITORIAL`; avoid false views/counters. Camera speeds through bar #3 (it becomes a monitor frame edge). Word “menembusnya” aligns to optical portal apex.

### Scene 03 / 7.0–11.8 / OVER THE SHOULDER
VO: “Sekarang kita di belakang karakter. Layar di depannya berubah jadi huruf raksasa.”
One physically plausible right-shoulder camera path. Mascot shoulder enters near foreground with believable foreshortening and occlusion. A monitor shows the original editorial design as new artwork. Mascot gestures toward its edge; the rectangular edge expands to the C-shaped first stroke of giant lettering. Foreground near shoulder moves faster than background. Avoid a fake 2D profile cutout.

### Scene 04 / 11.8–16.1 / BACKDROP WORD
VO: “Huruf itu terbuka, memperlihatkan panel kaca yang bergerak mengikuti kamera.”
3D matte navy `CLAUDE` letters behind character; physical thickness, coherent key-light from upper left, true cast shadow, legibility. C and L mechanically part to reveal an aperture. The camera passes between letters, which become rim of translucent glass layer. Contrast caption on pale background, not over face.

### Scene 05 / 16.1–20.4 / GLASS WIDGETS
VO: “Panelnya menangkap cahaya.”
Three frosted panels traverse Z rails with varied motion mass; thick readable glass edge, specular glint, soft contact/occlusion, no plastic. Text labels illustration only. One bright edge glint travels left-to-right and extends into the beam for scene 06. Keep avatar silhouette clear and do not over-stack cards.

### Scene 06 / 20.4–23.7 / SPOTLIGHT
VO: “Panggung spotlight muncul.”
The same glint physically becomes a cone of stage light; room slightly dims locally with vignette but light supplied BG remains recognizable at margins. Mascot turns head into beam, posture opens; floor shadow and beam geometry agree. Hold hero pose. At beat end, lifted palm catches light and forms circular optical iris.

### Scene 07 / 23.7–27.8 / COLOR GRADE
VO: “Satu gerakan tangan, warnanya berubah total.”
A physical circular filter dial is turned by avatar hand. Show one shot before/after using grading split: before low-contrast desaturated, after balanced soft-white/cool-blue and refined navy shadows. No orange/teal cliché and do not change mascot identity. Keep both states clear enough to compare. Dial becomes a round path guiding six small scene cards in scene 08.

### Scene 08 / 27.8–33.3 / THE HIDDEN SECRET
VO: “Rahasia transisi yang terasa mahal ada di sambungannya. Satu objek membawa kita ke adegan berikutnya.”
Pull back to a connected mechanical editorial course tracing the same six objects in order: bar→screen→letter→glass→light→dial. Object handoffs are highlighted in a single long camera travel; not six disjoint cuts. Text briefly: `BUKAN BANYAK EFEK` normal gradient navy becomes white-on-navy badge `TAPI NYAMBUNG`. Visible payoff to hook.

### Scene 09 / 33.3–38.0 / CODE + QUALITY
VO: “Semua bisa dirancang di Claude Code pakai maskot tiga dimensi. Timing dan detailnya tetap harus dicek.”
Creative editor-like scene constructed from original SVG/HTML, not a product screenshot impersonation. Timeline 6 scene blocks and waveform placeholder; mascot in left foreground, labelled small `STORY / CAMERA / TIMING / QA`. Show realistic mouse scrubbing or clip snapping, not lines of random code. The flat ruler lowers into preview gallery.

### Scene 10 / 38.0–42.0 / CTA
VO: “Mau enam prompt dan storyboard lengkapnya? Komen CLAUDE. Gue kirim.”
Six original preview compositions in a 3x2 grid, each shows one recognizable effect. Wordmark persistent top left. Headline normal navy gradient `MAU PROMPTNYA?`; highlight box gradient navy with white text `KOMEN CLAUDE`. Mascot down-left gestures toward CTA, not concealing cards. 0.5s still held brand lock at end. No fade to black.

**IMPORTANT:** These times are storyboard anchors, not a mandate to force speech into 42s. When real audio arrives, recompute all scene starts from verified utterance boundaries and last word, preserve meaning, maintain no silent dead zones and no off-script fake narration.

## 5 — Mascot animation quality lock

Before animating, inspect actual model with static neutral pose rendered front/side/3-quarter, AABB/pivot, joints, morph targets, mouth topology. If rig available, produce planned upper body, neck, eye-line and natural hand movement with clean damping. If non-rigged, stage it with valid bone-free transformations (head group if safely separated, torso pivot, prop/camera choreography). **Never auto-warp UV/face or hallucinate lip-sync.**

Personality: curious at start, controlled focus OTS, confident reveal at spotlight, precise gesture for color dial, inviting CTA. Never repeat identical arm wave in all scenes. Character identity/eye placement/neck/head proportions remain fixed. Feet/torso grounded in stage when visible.

## 6 — Engineering / render framework

First inspect the *existing* Claude Code project for its actual toolchain. Prefer existing HyperFrames + GSAP for code-driven editorial components, and Three.js for true GLB mascot + physical camera. **Do not install or switch frameworks without checking what already works.** Verify current HyperFrames CLI commands before using them; don't invent flags. CSS/SVG 2.5D can do UI and labels, but any object that needs real occlusion/physical perspective should use Three.js or true pre-rendered 3D passes.

For HyperFrames (if installed), follow its currently installed composition contract: unique composition IDs, explicit 1080x1920 size, correct start/duration/track index, registered paused finite GSAP timelines, no `Math.random()`/`Date.now()` timing, no `repeat:-1`, no unsynced `requestAnimationFrame`, no independent media.play. Entrance animation every scene, **do not fade outgoing content before the object transition handles the exit**. Use audio file as an actual separate track; video source reference must never end up in final output.

If GLB renderer / HyperFrames compatibility fails, report the precise blockage. Suggest a tested deterministic fallback before changing engine, but do not claim success from an untested pipeline.

## 7 — Work checkpoints — actually perform, don't just describe

**Phase A: Inventory.** Print actual asset manifest including filenames/dimensions/audio duration; identify mascot rig capability and any limitations. Create an explicit `production/asset_audit.md`.

**Phase B: Lookdev.** Build three polished 1–3s test clips or still-motion samples: editorial→monitor matchcut, type→glass portal, spotlight→color dial. Check logo top-left legibility and correct BG on mobile. Provide screenshots at motion midpoints. Run appearance and alpha tests. Ask for one lookdev approval if user is available.

**Phase C: Whole preview.** Implement storyboard with all six styles and transitions. Create beat sheet aligned to actual VO (if not yet provided, mark silent preview). Add just enough SFX for tactile material. Inspect screenshots at scene midpoints **and each transition midframe** (not just freeze-frame starts). Run lint/validate/check/inspect according to installed CLI.

**Phase D: User approval.** Show **draft preview** and note any remaining visible defects. The user must approve the preview before spending time on delivery-quality final render.

**Phase E: Final QA/export (only after approval).** Render final H.264/AAC MP4 1080×1920 30fps. Verify ffprobe codec/duration/frames and video contains user VO until the last word. Inspect bottom safe area, no mask clipping, no white-on-white captions, no banding, no material tearing or face mesh deformation, no black first frames, logo visible and not distorted. Report actual files and test outcomes, not guesses.

## 8 — Pass/fail gate

This is NOT done if: maskot looks like 2D sticker, face morphs between camera cuts, overlaid floating cards all have same bounce, all transitions are white flash/zoom, typography has wrong font/colors, background is replaced by navy, logo lies in the center or is distorted, animation opens on black, any important label is unreadable on phone, original source person's pixels appear, CTA promises 22 undocumented effects, or missing VO is reported as synced.

This IS ready for review if: six styles are immediately recognizable; at least five object-led transitions are spatially coherent; mascot identity persists; shadows/light/camera parallax are internally consistent; each effect has a distinct physical gesture, source logo and palette exact; mobile readable; CTA resource exists; preview can be demonstrated and independently inspected.

Work as a top-tier motion studio, but be truthful about what is and isn't completed. **Start with the asset inventory and 3D capability audit, then show the initial 3 lookdev samples.**

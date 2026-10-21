---
message: "Motion AI premium itu mungkin — asal arahan/prompt-nya jelas."
mode: autonomous
canvas: 1080x1920
fps: 30
duration: 48
concept: "Satu garis arahan navy yang tidak pernah putus menjahit seluruh film — rel, baseline, spine, underline input, sampai underline endcard."
---

Monolithic build: semua scene adalah `<section class="clip">` di `index.html` dengan satu timeline, karena garis arahan (`#thread`) dan elemen handoff berpindah lintas scene.

## Frame 1
status: built
src: index.html#s1
rules: svg-path-draw (thread draw), mask reveals (diagonal clip + offset word groups)
beat: "BANYAK ORANG BILANG / AI HASILNYA MASIH BIASA AJA." — hook, monolith tipografi kiri, logo kecil atas.

## Frame 2
status: built
src: index.html#s2
rules: split-tilt-cards (hinge), grid-card-assemble (wireframe → grid)
beat: "PADAHAL MASALAHNYA / SERING BUKAN DI AI-NYA." — split before/after, rel jadi divider.

## Frame 3
status: built
rules: waterfall-entry (word masks 0.07s), control-target-sync (node snap)
src: index.html#s3
beat: "MASALAHNYA ADA DI / ARAHAN YANG DIBERIKAN." — garis panduan + 3 node kontrol.

## Frame 4
status: built
src: index.html#s4
rules: center-outward-expansion (unfold), card-morph-anchor (module 3 → prompt field)
beat: "AI ITU CEPAT. / TAPI HASILNYA MENGIKUTI / SEBERAPA JELAS BRIEF-NYA." — tangga presisi 3 modul.

## Frame 5
status: built
src: index.html#s5
rules: discrete-text-sequence (typing), context-sensitive-cursor
beat: "BUKAN CUMA SURUH / ‘BIKIN YANG KEREN’" — panel prompt kosong, quote dock ke kiri atas.

## Frame 6
status: built
src: index.html#s6
rules: svg-icon-enrichment (mini graphics), anchored traveling node
beat: "TAPI MENJELASKAN / STYLE / RITME / KOMPOSISI / TRANSISI / HIERARKI" — spine 5 parameter sinkron VO.

## Frame 7
status: built
src: index.html#s7
rules: control-target-sync (sweep → mutate), viewport-change (camera shift)
beat: "PROMPT YANG TEPAT / MENGUBAH OUTPUT" — komposisi sama berubah dari sempit ke rapi.

## Frame 8
status: built
src: index.html#s8
rules: svg-path-draw, multi-phase-camera (drift <3%), nested frame
beat: "DARI TEKS BIASA / JADI MOTION YANG TERLIHAT MAHAL." — hero showcase.

## Frame 9
status: built
src: index.html#s9
rules: logo mask reveal (pixel asli), svg-path-draw
beat: "INILAH CARA / AI PRENEUR MENGARAHKAN AI." — brand reveal.

## Frame 10
status: built
src: index.html#s10
rules: svg-path-draw, center-outward snap, border highlight sweep
beat: "LEBIH CEPAT. / LEBIH TERARAH. / LEBIH PREMIUM." — tiga klaim desain.

## Frame 11
status: built
src: index.html#s11
rules: titlecard-reveal (tiered masks, letter-group stagger)
beat: "AI BISA MEMBUAT / MOTION SELEVEL INI. / ASAL PROMPT-NYA TEPAT." — endcard, hold diam ≥0.82s.

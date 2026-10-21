# QA ACCEPTANCE — KONTEN AI PRENEUR

**PASS hanya setelah Claude Code benar-benar membangun dan memeriksa MP4 final. ZIP ini adalah paket eksekusi, bukan hasil render.**

1. **Asset source**: Semua relative path resolvable pada Windows. Background original/portrait visible. Logo trimmed persis sama glif original; scaling dan alpha benar. Reference video tidak dipakai dalam output.
2. **Timing**: 11 beats berurutan frame ranges 0–1439; 30 fps × 48.0s = 1440 frames. Voice starts respect `05_AUDIO_TIMING.csv`; tidak terpotong; tidak ada overlapping VO. Audio master stream sekitar 48s.
3. **Voice**: Satu VO MASTER track saja, tanpa duplikasi sebelas MP3. Cocokkan apa yang DIUCAPKAN dengan on-screen copy; gunakan file suara, bukan memaksa TTS/draft yang beda.
4. **Storyline**: Hook → problem → thesis → clear briefing → vague example → 5 concrete prompt directions → direct transformation demo → premium hero → actual AI PRENEUR logo → three benefits → elegant CTA.
5. **Copy**: Setiap teks yang terlihat termasuk kategori/copy harus persis yang dikunci. No placeholder lorem ipsum, extra fake UI brands/stats, misspelled logos/VO.
6. **Visual and fonts**: Background supplied visible entire runtime (with deliberate covered UI overlays only); gradient typography `#0a0d2c` and `#294b77` on hero text, solid navy for body. All newly created text MUST use real **Poppins Regular 400 + Poppins Bold 700** with scene-aware hierarchy, verified font loading inside the actual rendered MP4, no mixed-in typefaces, no synthetic-bold, no unintended fallback, no clipped Poppins ascenders/descenders after mask motion. The AI PRENEUR logo image stays unmodified. Avoid overdone effects and repetitive entrances.
7. **Mobile safe & readability**: Key text/logo in conservative x≈90–900, y≈220–1540 where practical; ensure clarity at phone size and with Instagram interface risk. Motion intermediary frames also tested for clipping/collision.
8. **Motion**: Scene-specific mechanism works, transitions are connected, no unearned black frames, no frozen unexpected gaps, no bounce/fade template repetition, no detached/teleported components.
9. **Seek**: Pause/scrub/check in arbitrary order and compare identical timestamp to identical visual state. No independent rAF timing, unseeded randomness, media currentTime hacks, or GSAP timeline drift.
10. **Pipeline**: Inspect official installed router and commands (`/hyperframes:hyperframes` or `/hyperframes` where available). `npx hyperframes lint`; `npx hyperframes check --snapshots` (or verified installed equivalents). Review opener, each beat midpoint, boundaries, 47.5s ending, and transitions. Preview full sequence.
11. **Export file**: Actual MP4 exists nonempty, 1080×1920, 30fps, exactly approx 48.0 seconds within frame/codec tolerance, plays correctly with one audible Indonesian VO. Inspect with media probe + exported keyframes, not only in-browser preview. No abrupt audio cut/black tail.
12. **Report**: Output path verified; actual metadata; checks and snapshots outcomes; repairs; residual issues. Never claim QA passed if not inspected. Respect mandatory official final-render approval if present.

**Blocking FAIL**: no source files, missing logo, unreadable type, clipped or truncated voice, wrong scene order, 11 sounds doubled by master, damaged brand asset, false use of stock/claims, HyperFrames check failures, final MP4 absent, exported runtime wrong, or unverified claimed PASS.

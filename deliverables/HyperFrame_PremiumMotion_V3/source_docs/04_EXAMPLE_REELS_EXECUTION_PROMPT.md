> **V3.0 note:** this is the older minimal-typography example (V1/V2). For the default house style see `04B_EXAMPLE_AIPRENEUR_V3_EXECUTION_PROMPT.md`.

# CONTOH PROMPT JADI — 15s Instagram Reels 9:16

> **V2.1 NOTICE:** This 15-second example intentionally demonstrates a minimalist flat/editorial design. It is **not** the default for user requests that require premium glass, cinematic shadows or 3D depth. For style-specific requirements use source 06/07 and the optional lookdev calibration in 08.

> Ini contoh **prompt final yang siap ditempel ke Claude Code** untuk menguji Project HyperFrame Prompt. Contoh ini sengaja tidak membutuhkan footage eksternal, logo, atau asset berlisensi. Jangan gunakan ini sebagai desain wajib untuk semua video.

---

Using the official installed **HyperFrames** skill router (versioned Claude Code plugin `/hyperframes:hyperframes` if available; otherwise the installed standalone `/hyperframes` skill), CREATE, VALIDATE, PREVIEW, and — subject to any mandatory installed final-render approval gate — RENDER this video. We already have working HyperFrames on Windows. Do not ask for another creative brief; execute the locked concept below.

### ROUTE
Choose official `motion-graphics` or `general-video` as determined by the official router. Use HyperFrames-native HTML/CSS/JS, seekable timelines, and CLI. Inspect installed skill versions and CLI help before using commands.

### SPEC
- Format: Instagram Reels, portrait **1080 × 1920, 9:16**, 30fps
- Runtime: **15.0 seconds**
- Export: actual MP4; high quality when supported
- Language: Indonesian
- Style: premium black / off-white / restrained lime-green highlights, contemporary editorial typography, precise movements, minimal but alive; not a PowerPoint slideshow, not futuristic neon wallpaper.
- No need for stock imagery, brand logo, voiceover, or proprietary assets.

### ONE MESSAGE
"Satu ide konten bisa dikembangkan menjadi beberapa format, bukan dibuat ulang dari nol."

### STORYBOARD — ALL TIMECODES LOCKED

**S01 — Hook (0.0–2.5s)**
- On-screen EXACT COPY: `"SATU IDE."` line 1 and `"BANYAK KONTEN."` line 2.
- Giant clean bold white typography, left aligned around middle-left on deep-black background. `"BANYAK KONTEN."` gains a restrained green underline. Text stays clear of Reels interface overlays.
- Motion: first line rapidly reveals by a small vertical wipe (~0.45s), second appears with deliberate stagger (~0.5s), underline draws in under last words by ~1.5s. Slow ambient texture motion continues until end of scene. At 2.5s transition directly into the next scene.

**S02 — One input (2.5–5.0s)**
- On-screen EXACT COPY: `"1 IDE UTAMA"`.
- Center-left outlined large editorial card, prominent numeral 1; a thin branching line begins to grow from its right edge. Avoid putting key words near right engagement rail.
- Motion: card scales subtly 0.97→1.0, line draws during the second half. Never allow the main card to fade into illegibility.

**S03 — Format expansion (5.0–10.5s)**
- On-screen EXACT COPY: `"REELS"`, `"CAROUSEL"`, `"STORIES"`, `"CAPTION"`, and `"EMAIL"`.
- Visual: one clean primary card expands into a balanced vertical network/stack of five labeled small cards. Layout is appropriate for a 1080×1920 portrait frame. Max 3 simultaneously dominant items; reveal content in a rhythmic sequence so everything is readable.
- Motion: cards enter one-by-one at approximately 0.65–0.85s intervals, connected by clean line animations. Deliberately retain the parent idea visually. No random shattering or camera spin. All five labels readable in the final 0.8s of this beat.

**S04 — Payoff (10.5–13.2s)**
- On-screen EXACT COPY: `"BUKAN 5 IDE BARU."` then `"CUKUP 1 IDE YANG DIKEMBANGKAN."`.
- Visual: network elegantly contracts into typographic payoff, first line lighter weight, second line bold; green emphasis on `"1 IDE"`. Composition left-biased with comfortable spacing and contrast.
- Motion: clear first line followed by second line; smooth ~0.4s motion, then subtle idle.

**S05 — Close (13.2–15.0s)**
- On-screen EXACT COPY: `"SAVE UNTUK COBA NANTI."`.
- Visual: minimal calm closing treatment on high contrast dark background; visually continuous with prior beat.
- Motion: text appears by ~13.6s; subtle underline and 0.8s readability hold. Finish cleanly at exactly 15s (no unintended black tail).

### AUDIO
No voiceover. Use restrained SFX on meaningful reveals only if legally/source-verifiably available, otherwise export clean silence. Do NOT invent BGM sources. Silence is acceptable. No auto captions are needed because all communication is designed typography.

### DESIGN RULES
Mobile-first text hierarchy; use a conservative critical-copy zone away from typical Reels header, right rail, and bottom controls (confirm during review). 1080×1920 native layout. Never use tiny text, stock-logo imitation, endless zooms, fake camera DOF, excessive shadow/glow, or illegible kinetic typography. Make the motion premium, not hyperactive.

### TECHNICAL & QUALITY CONTRACT
- Use official installed HyperFrames schema, proper composition ID/width/height/duration, timed clip properties, and finite seek-safe timeline(s).
- When using GSAP, register a paused synchronous timeline by exact composition ID in `window.__timelines`.
- Render deterministically; no unseeded randomness, real-time timers or independently controlled media playback.
- Confirm `npx hyperframes --help` and relevant command help rather than assuming flags.
- Build in a fresh folder, preserve existing project data; no public uploads or paid operations.
- Run `npx hyperframes lint` during initial iteration; then `npx hyperframes check --snapshots` before export. Inspect snapshots at t=1, 3.5, 6, 8.5, 11.5, 14.2 (adapt CLI syntax after checking supported flags). Fix layout/motion issues.
- Preview assembled timeline after successful checks; follow mandatory skill-specific final-render approval when required; otherwise render directly.
- A typical export command, if the CLI supports these flags, is `npx hyperframes render --output renders\one-idea-five-formats.mp4 --fps 30 --quality high`.
- Inspect the actual MP4 with available media tools and review important frames/scene cuts. Verify portrait 1080×1920, 30fps, duration ~15s, all text present, no clipped copy, no black frames, correct animation seeking, usable mobile safe zone.
- If a blocker remains, report it explicitly instead of marking PASS.

### DELIVERY
Return a concise report: output file verified path, actual technical specs, actual verification actions/result, any repairs, and any remaining warnings. Do not claim PASS without checks.

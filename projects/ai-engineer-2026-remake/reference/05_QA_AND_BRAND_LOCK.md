# Brand & Quality Acceptance — AIpreneur AI Engineer 2026

## Visual brand — LOCKED

| Element | Aturan pasti |
| --- | --- |
| Canvas | 1080×1920 portrait, 9:16, 30 fps |
| Background | **User PNG:** `assets/background_pale_ice.png`, 1080×1350, aspect-preserving crop/edge extension, no stretch |
| Font | **Poppins Bold 700 + Poppins Regular 400**. No Montserrat in this project |
| Regular text | Dark navy gradient `#0A0D2C` → `#294B77`, high contrast on pale background |
| Highlights | **White text** on rounded filled navy gradient rectangle; balanced padding 12–19 px vertical/20–28 px horizontal |
| Logo | Original dark AIpreneur PNG, persistent top-left; small entry and masked sweep every 7–9 seconds; letters never altered |
| Mascot | EXACT already-existing 3D character from Claude Code project, no identity changes/new generation |
| SFX / music | No BGM. Allowed: user-owned/licensed subtle mechanical SFX. Never overpower narration |
| Endcard | Full working machine + mascot + logo; final still hold, no black fade |

## Visual criteria (target 10/10)

- [ ] A viewer can identify the physical meaning of each scene without reading a paragraph.
- [ ] Camera, lighting, character identity and workbench location remain coherent across cuts.
- [ ] Mascot has believable contact shadows, hand reach/eye gaze only if rig supports it; no floating feet or fake moving fingers.
- [ ] 3D heroes show thickness, bevels, material reflection, contact and occlusion; not flat boxes with cartoon drop shadow.
- [ ] All major changes have a cause in the story (piece attached, cable followed, switch turned, drawer opened).
- [ ] SC01, SC09, SC10 and SC12 are distinctive lookdev/animation moments, not reused animation presets.
- [ ] At least 15 scenes but not 15 unrelated “animated slides”; props hand off between adjacent scenes.
- [ ] No useless spinning, random camera shakes, giant neon glows, soft-blurred everything, or visual noise.
- [ ] Reading priority: logo left-top, one short caption, one dominant hero.
- [ ] Highlights legible: WHITE text on navy-gradient card. Normal letters navy-gradient on pale background.
- [ ] All background cropping is aspect-preserving, with no stretched image.

## Audio and timing

- [ ] User's exact recorded VO is loaded as a single track from time=0, without artificial speed modification.
- [ ] Every stage is mentioned in audio (Python, software, ML, DL, LLM, app, RAG, agent, eval, production).
- [ ] No fabricated narration or extra claims printed on screen.
- [ ] Word-synced visual apex is within ±2 frames of verified onset (where alignment permits).
- [ ] Pauses feel intentional (0.1–0.4sec rests between peaks), final word fully audible.
- [ ] No copyrighted background music or unlicensed source audio reused.

## Editorial accuracy

- [ ] The 10 steps are presented as a **practical learning roadmap**, not a universal job requirement or guaranteed hiring route.
- [ ] Retrieval/RAG physically shows retrieval **before** model answer; no claim that retrieval makes answers automatically true.
- [ ] Agent action has allowed tools and visible checks; no promise of perfect/full autonomy.
- [ ] Evaluation distinguishes tests from improvement, and avoids an invented performance percentage.
- [ ] Production shows cost, latency, security and monitoring as work to be managed, not solved forever.
- [ ] “Build product” vs “go deeper into models” explicitly presented as **two possible specializations**.

## Render verification

- [ ] HyperFrames scene mount, lint and check pass genuinely. If check unavailable, documented equivalent validates timeline and layout.
- [ ] Deterministic screenshot at same timestamp across shuffled requests (pixel match if fully deterministic engine).
- [ ] 1080×1920, 30 fps, H.264/AAC final streams verified with ffprobe.
- [ ] Video has no unexpected black flash, frozen middle frames, alpha fringe, missing 3D texture or silent tail.
- [ ] Exported MP4 inspected at start, every major transition, midpoint, and last frame.
- [ ] Draft preview has been shown to Freddie and final render gate approved before expensive export.

## Devil's advocate / tradeoff penting

1. **Kecepatan edit vs pelajaran teknis:** 10 tahap dalam ~100 detik membuat semua materi terasa cepat. Solusi: hook cepat, langkah 1–6 singkat, RAG/agent lebih panjang, satu diagram hero per frase. Jangan paksa seluruh terminologi teknis muncul sekaligus.
2. **3D mascot vs render resources:** GLB berkualitas tinggi bisa berat pada GPU rendah. Solusi: cache rendering/transparent pass bila perlu; jangan mengganti mascot dengan generative still atau downgrade tanpa cek kualitas.
3. **Logo motion vs distraksi:** glow konstan menarik perhatian dari pelajaran. Solusi: light sweep sangat halus 7–9 detik dan tetap idle antar-sweep.
4. **Reference similarity vs originality:** struktur 10 skill boleh dipertahankan sebagai materi edukasi; UI kota, presenter source, SFX dan objek/source footage tidak perlu dan tidak boleh dijiplak.

**Status paket sekarang:** Storyboard/prompt/VO siap; belum ada audio rekaman terbaru, build Claude Code, render, atau quality check video final. Jangan mengklaim semuanya sudah selesai.

---
name: business-explainer-30s
description: 30-second animated business explainer as a single HTML page (expert motion-designer role) — 5 scenes: the customer's problem, what the business does, how it works in 3 steps, one proof point, the name at the end; bold type, smooth transitions, the brand's colours. Renders to MP4 (HyperFrames) when a video is needed. Use for "/business-explainer-30s", "explainer 30 detik untuk bisnis", "video penjelasan bisnis", for AIpreneur, SKINKU, Rave Tailor, Raveloux, Ravent Creative or any client business.
---
# /business-explainer-30s

Client prompt (verbatim): "Adopt the role of an expert motion designer. Build a 30-second animated explainer for my
business as a single HTML page. 5 scenes. The customer's problem, what I do, how it works in 3 steps, one proof point,
and my name at the end. Bold text, smooth transitions, my brand colours. My business [DESCRIBE WHAT YOU SELL, WHO IT'S
FOR AND YOUR COLOURS]"

## Start
- Ask (only for what's missing): what is sold, for whom, brand colours, the one proof point (must be TRUE — a real
  number, testimonial or result the client can stand behind; never invent stats), name/logo, format (16:9, 9:16 or 1:1),
  language (default Bahasa Indonesia), VO or music-only.
- Known brands — use these defaults and brand rules from `aipreneur-reels-studio/references/brand.md`:
  AIpreneur (navy/white, cyan #01ccf7, Poppins, 3D mascot host allowed), SKINKU (Japanese soap / "Produk Jepang glownya
  emang beda level", affiliate/TikTok Shop/Shopee), Rave Tailor (custom men's suits: fit, cutting, confidence — elegant,
  premium), Raveloux (custom dresses: elegance, sketch → fitting — premium, emotional). Ask for their exact colours if unknown.

## Structure (30 s)
| scene | time | content |
|---|---|---|
| 1 Problem | 0–6 s | the customer's pain in one bold line + one visual metaphor (hook in the first 1.5 s) |
| 2 What we do | 6–12 s | the promise in one line, product/service visual |
| 3 How it works | 12–22 s | 3 numbered steps, ~3 s each, each with its own icon/visual |
| 4 Proof | 22–26 s | one real proof point (big number counting up / testimonial quote + name) |
| 5 Name | 26–30 s | logo + name + one-line CTA, hold ≥1.5 s |

## Build
- Single HTML file; every style computed from time in `window.seek(t)` (GSAP paused timeline registered in
  `window.__timelines` for HyperFrames, or a pure seek function). No timers/state between frames. Also autoplays in a
  browser (requestAnimationFrame calling seek) so the page itself is the deliverable.
- Bold type (Poppins/Geist 700–800, tight tracking), masked line reveals, shared-element transitions between scenes
  (an element of scene N becomes the frame of scene N+1), one camera language, easing power3/expo (no bounce unless the brand is playful).
- Brand colours only; one accent. Real brand logos from Simple Icons (CC0) if any appear; product photos only if the
  client supplies or licences them.
- Optional VO via ElevenLabs (`aipreneur-reels-studio/scripts/vo/el_tts_ts.py`, Freddie's voice Dakocan for his brands)
  + quiet SFX on transitions + music bed, −14 LUFS.

## QA + deliver
Snapshot every second, check no cut/overlapping text and readable sizes at the target format, then render MP4
(`npx --yes hyperframes@0.8.186 render . -o out/<name>.mp4`) if a video is wanted. Deliver: the HTML page (+ MP4),
plus a short scene list. Commit + push.

---
name: throughline-explainer
description: 30-second product explainer (1920×1080, 60 fps, 120 BPM) built around ONE through-line object taken from the product (its cursor, a key button, the logo mark, one data point) that transforms in every scene and becomes the logo on the end card; real UI rebuilt as vector layers, cursor-driven clicks/drags, screen-studio zoom camera, code-composed soundtrack. Use for "/throughline-explainer", "explainer produk 30 detik", for the client's own products (AIpreneur classes/community/agency, SKINKU, Rave Tailor, Raveloux, MasterPajak AI…).
---
# /throughline-explainer

Technique extracted from a client-supplied brief (originally written for someone else's product). Apply it ONLY to the
client's own products/brands — never copy another company's product, UI or brand.

## Inputs (ask only what's missing; defaults in brackets)
Product + link; 3–6 screenshots of the real interface [capture them yourself with Playwright]; logo [from the site];
brand colours + font [the product's own; AIpreneur → brand.md]; music with a clear beat [compose it in code].
Research first: what it does, for whom, real interface, brand. Never invent screens, features or numbers.

## Through-line object
Pick one object from the product itself and NAME it before storyboarding. Every scene is a transformation of it: it starts
in the UI, changes shape/role each scene, ends as the logo on the end card. One typeface, ONE accent colour used only on
the through-line object and the key word, lots of empty space.

## Structure (120 BPM, beat = 0.5 s, 15 bars = 30 s)
- Hook (bar 1): the problem in 3–5 words, big type, interrupted by the through-line object.
- Middle: 3–4 product moments; each starts with the object turning into the next UI element and lands one readable idea.
- Payoff (last bars): strongest moment on the biggest beat → object becomes the logo → end card: name + one-line CTA.
Write a timed storyboard beat by beat first; then build exactly that. Show findings + object + storyboard, then build
without further questions and deliver the MP4.

## Motion rules
- Real UI rebuilt as vector/DOM layers (parts move on their own); never slide a flat screenshot.
- A cursor drives every interaction (real clicks/drags); screen-studio zoom so each moment fills the frame.
- Springs with at most a small overshoot; exponential easing; nothing appears from nothing (grows, unfolds, mask reveal).
- Camera never still: push 1.0 → 1.04 across a scene; each scene starts at the zoom the last one ended on.
- Something changes on every beat; no hold > 0.5 s.
- Banned: particle bursts, glows, lens flares, camera shake, RGB split, crossfades, generic gradients, bouncy easing, template looks.

## Build
1. One HTML, 1920×1080, all styles from time in `window.seek(t)`; no CSS animations/timers/state.
2. Spring/exponential easing as functions of t; directional blur proportional to speed on fast moves.
3. Soundtrack in code (Web Audio OfflineAudioContext): kick every beat, a hit on each scene change → WAV.
4. Playwright 60 fps, 3 subframes/frame blended with ffmpeg `tmix`, mux the audio.
5. Before the full render, render one frame per beat and look; fix clutter, off-beat changes, overlaps, unreadable text.

## Gotchas
Measure positions at runtime for match cuts; a shape that fills the frame must scale past all four corners; outgoing and
incoming text get separate timing (letters never overlap); never `will-change` on anything the camera scales (blurry text).

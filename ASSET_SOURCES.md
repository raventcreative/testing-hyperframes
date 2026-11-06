# Asset rules for AI PRENEUR video remakes

Client feedback (Nov 2026): keep the animation, transition and motion quality of the latest reels (or better),
but **nothing may look AI-generated**. Use real, open-source / openly licensed assets instead of invented visuals.

## Priority of sources
1. **Real footage the client supplies** (screen recordings, product pages, photos) — always the hero.
2. **Official brand assets** — logos from the brand's own site/GitHub avatar, or **Simple Icons** (`simple-icons` on npm, CC0, official brand marks).
3. **Open-source icon sets** (npm): Lucide (`lucide-static`, ISC), Tabler (`@tabler/icons`, MIT), Phosphor (`@phosphor-icons/core`, MIT), Iconoir (MIT), Heroicons (MIT).
4. **Openly licensed photos / illustrations**: Openverse API (`api.openverse.org`, filter `license_type=commercial`), Wikimedia Commons (`upload.wikimedia.org`). Record source URL, author and licence for every file in the project's `production/asset_credits.json`; add attribution where the licence requires it (CC BY).
5. **Open-source Lottie** animations only from packages with an explicit open licence (npm), played with `lottie-web` (seek-safe, frame-driven).
6. Fonts: Poppins / Montserrat via `@fontsource/*` (OFL).

## Avoid
- AI-generated images or "AI-looking" illustrations (plastic 3D blobs, generic glowing brains/robots, fake UI, fake dashboards).
- Invented logos, fake screenshots, fake terminal output or fake results.
- Over-decorated porcelain/glossy props when a real asset or a clean icon would read better.

## Environment
Session environment `testing-hyperframes` allows: api.openverse.org, upload.wikimedia.org, commons.wikimedia.org,
cdn.jsdelivr.net, unpkg.com, huggingface.co (+ its CDN hosts, for local Whisper transcription / exact word timing).

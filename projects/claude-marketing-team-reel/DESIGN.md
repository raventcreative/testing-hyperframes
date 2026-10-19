# DESIGN.md — claude-marketing-team-reel

**Style prompt:** Premium editorial social explainer. Clean off-white grid paper, italic editorial
headlines, bold sans UI labels, modular rounded cards, thin connector arrows, and a voxel 3D character.
Navy + burgundy derived from the character's suit and tie. Clean, tactile, contemporary — never a clone
of the reference account. No neon, glassmorphism, glow, fake 3D UI, rainbow gradients, or centered
PowerPoint stacks.

## Colors
| Token | Hex | Use |
|---|---|---|
| canvas | `#F4F1EA` | Off-white paper ground |
| grid | `#D9D6CF` | 1px grid lines, 60px pitch, low opacity |
| ink | `#111318` | Headlines, body |
| navy | `#18213A` | Cards, structure, S08/S09 dark ground |
| burgundy | `#7B1834` | Highlights, arrows, active nodes, underline, CTA |
| white | `#FFFFFF` | Card surfaces, text on navy only |

## Typography
- Editorial: **Fraunces** 600 italic / 700 italic (local woff2 from `@fontsource/fraunces@5.3.0`).
- UI / numerals / bold headline: **IBM Plex Sans** 300 / 400 / 600 / 700 (`@fontsource/ibm-plex-sans@5.3.0`).
- **Substitution (documented before layout):** brief asks Plex 350/800/900. IBM Plex Sans ships no 350,
  800, or 900 weight. Mapping: 350 → 300/400, 800/900 → 700 with tight tracking (-0.02em) for heft.
- Numerals: `font-variant-numeric: tabular-nums`.

## Layout
- Canvas 1080×1920. Critical copy x 90–900, y 210–1540.
- Headline zone y 210–470 · visual/diagram zone y 490–1280 · caption pill lower-middle (top ≈ 1330, max 690px wide).
- Character may extend to y 1760; face/gesture kept readable.
- Right 180px reserved for Reels rail: no critical copy beyond x 900.

## Texture
Paper grid + static grain (SVG feTurbulence baked once, static). No motion noise.

## Character
- `assets/char-seated.png` (from `1.png`) — scale/position/subtle bob only.
- `assets/expr/{talk,quiet,smile,smile2,confused,smirk,talk2,confident,yapping}.png` — crops of `2.png`
  inside the tile borders (inset 5–6px). Labels and borders excluded and visually verified.
  Crops end on a flat cut at the chest → always shown inside a rounded "portrait window" card whose
  bottom edge coincides with the cut.

## Motion
Medium energy. Push slide 0.36s (primary), diagonal paper wipe for topic changes (S03→S04, S07→S08),
card-stack cover (S04→S05), color dip outro. Entrances via gsap.from/fromTo, varied direction/ease.
No pre-transition exits. Finite only.

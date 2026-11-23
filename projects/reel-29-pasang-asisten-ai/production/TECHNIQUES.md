# reel-29 — techniques applied

White-theme software demo of a 13-skill AI content team (reference f34038fc, 115 s → 58.4 s VO).
Beat order follows the reference: hook → the team → what each skill does (writer / auditor / planner) →
the standout (trend research) → two ways to install → you still approve → CTA.

From `.claude/skills/aipreneur-reels-studio/references/technique_bank.md`:

1. **Hook shows the problem, never states it** — 00:12 on the clock, seven dashed day cards empty and a caption
   box with a blinking cursor and nothing typed. No slogan card, no badge.
2. **Process fill** — the same seven day cards are what the 13 skills fill, so the hook's problem and the
   payoff are the same object.
3. **One shape per scene, never repeated**: week strip → 13-tile roster + tick rows → draft document with
   strength bars → score ring + 12 criteria grid → 7-column planner + draft chips → ranked table that re-sorts
   → half-width terminal card → three CSS device shapes → toggle switches → approve card.
4. **A different transition on every beat** — zoom punch-through (hook → app), view cross-fade + camera move,
   camera close-up on the flagged line, 3D swing pop-out (bio card), blocks, shutter, card flip (terminal →
   devices), zoom-out reveal (approve), zoom-through (CTA). No wipe type used twice.
5. **Camera never still, never sliced** — one eased move per scene; the trend-table push is held at 1.04× so
   whole rows stay in frame (a 1.3× close-up sliced the account column and the no-cut guard blanked it).
6. **Hands alternate** (client rule 2026-11-23) — `point` uses the arm opposite the robot's side, so the robot
   is moved left/right between beats to force alternation: R, L, R, L, R, L, R, L, R, L arms across the reel,
   plus `beat` (auto-alternating) and a left-hand `wave` before the right-arm CTA point.
7. **Even VO, short pauses** — the raw ElevenLabs take already had its longest gap at 0.37 s, so nothing was
   padded or trimmed (`tools/fix_pauses.py` verified it); the visuals were timed to the VO instead.

Colour: white theme only — #294b77 accent, a muted amber (#b4731a) for the weak-opener bar and green (#1f9d6b)
for confirmations inside the app. No red, no yellow headline, no brand logos.

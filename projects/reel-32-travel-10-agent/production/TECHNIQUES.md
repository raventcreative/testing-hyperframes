# reel-32 — travel & tour operator, 10 AI agents (blue)

Reference: `1cca2a25-10_AI_Agent_for_Real_Estate.mp4` (43 s). Its structure is kept — hook naming "10 agents every
business needs" + "number 8 is my favourite", a roll-call of all ten, then "they work 24/7 without an extra
employee", then CTA — but the vertical is moved from property to a travel & tour operator (reel-27 keeps property).

## v2 — the structural rework (client: "elemen-elemennya monoton")

v1 is kept as `index_v1_panels.src.txt`. There, each of the ten agents was a panel that replaced the previous one
in the same window, at the same size, in the same place — ten beats that watched identically however different
each panel's internals were. v2 (route A) keeps the roll-call and changes what it builds.

**The window is no longer a panel holder, it is a viewport.** `#wcam` is a 1840 x 1900 operations floor inside a
920 x 950 window, so scale 0.5 shows the whole floor and anything above that is a travelling camera over it.

**The ten agents accumulate instead of replacing each other.** Each has a fixed place on the floor, in a loop
rather than a grid, at a deliberately different size and aspect:

| # | agent | floor x, y | w x h |
|---|-------|-----------|-------|
| 01 | Bales chat | 100, 110 | 600 x 340 |
| 02 | Follow up | 820, 110 | 560 x 300 |
| 03 | Booking | 1400, 110 | 400 x 430 |
| 04 | Itinerary | 1190, 660 | 570 x 300 |
| 05 | Vendor lokal | 640, 560 | 520 x 340 |
| 06 | Konten | 100, 540 | 460 x 400 |
| 07 | Harga | 100, 1020 | 540 x 300 |
| 08 | Invoice & DP | 680, 960 | 560 x 340 |
| 09 | Review | 1340, 1040 | 420 x 320 |
| 10 | Laporan | 980, 1400 | 700 x 360 |

The window opens on the **dark floor**, all ten stations drawn but unlit, joined by a faint route. Each named agent
lights its own station — border, number, icon plate and a "jalan" badge take the station's colour — and **stays
lit**, while the bright route segment draws to it. By number ten the screen is a full picture the viewer watched
get built, and the toolbar counter has climbed 0/10 → 10/10.

**The camera travels, it never cuts panels into the centre.** One eased move per beat, a different direction,
distance and scale each time, verified against the viewport clamp so the target is always fully inside:

`0.50 wide` → `1.45 (400,280)` → `1.28 (1100,260)` → `1.66 (1600,325)` → `1.22 (1500,810)` → `1.52 (900,730)` →
`1.40 (330,740)` → `1.38 (350,1170)` → `1.30 (960,1130)` + a slow 1.44 push inside that beat → `1.58 (1550,1200)`
→ `1.12 (1330,1580)` → **`0.50` wide payoff** → `2.40` punch into station 08.

A station's detail (`.sd`) rises from 0.08 to 1 when the camera arrives and recedes to 0.12 when it leaves, so the
floor stays legible at every scale and nothing is ever caught half-faded.

**The payoff.** After station ten, the camera pulls back to the whole lit floor, the route complete, and every
station answers in a staggered glow — ~1 s of the finished picture before the punch into station 08.

## Beats that break the container (so consecutive beats never sit in the same box)
- **Hook** — full-bleed on the stage, no window at all: a 2 x 5 board of the ten jobs filling up over one worker
  bar ("Lu sendiri") with a waiting counter. Shows the problem instead of stating it: no slogan card, no red badge.
- **06 Konten** — a pop-out card on the LEFT half, outside the window, window dimmed, robot risen on the right.
- **Transition to 04** — a full-width accent strip (#01ccf7, navy type) breaking both window edges, carried under
  the blocks wipe, which on its own covered on an almost empty navy frame.
- **08 Invoice (favourite)** — a phone held in frame on the RIGHT half, robot risen on the left; the window behind
  is blurred to depth. The frame pushes in on the phone as its steps land, so the six-second beat keeps moving.
- **24/7** — full-bleed again: a conic dial counting to 24, two plates (1 orang / 10 agent) and ten agent chips.

## Transitions — a different one on every beat
zoom punch-through (the hook's board punches into the floor) · slats · camera travel ·
blocks + accent strip · iris · pop-out + dim · camera pull-back to the wide · zoom punch-in (into station 08) ·
zoom-out reveal (window shrinks away, dial lands) · zoom-out recede to the CTA. No wipe type is used twice.

## From the technique bank
- **Hook shows the problem, never states it** (ten jobs land on one person).
- **Shared element / match cut**: the hook's job board becomes the floor the camera punches into.
- **Accumulating composition**: the subject of the scene is the picture being built, not the current panel.
- **Camera never still**: one eased move per beat, never two identical pushes in a row.
- **Never a blank window**: the floor is already drawn when the window opens; the no-cut guard hides sliced *text*
  only, never the station it sits in, so a station travelling into frame is visible the whole way.

## Client rules checked
- **Hands alternate**: 20 gestures, strictly R/L/R/L… re-verified by replaying `side()` against the v2 pose track.
- **Robot**: never centred over the element being explained (it leaves the raised pose for the right half while the
  price card builds centre-left); two side rises (upR beside the konten card on the left, upL beside the phone on
  the right); no low poses, never zoomed; whole and centred at the CTA.
- **No cut text**: guard measures each text unit and fades it for any shot — and any sampled point of any eased
  camera move — where it is sliced by the viewport.
- **VO**: tags kept in a narrow band; every pause already <= 0.42 s, so no padding was added.
- **Length**: 53.4 s (target 45–60 s); VO 52.72 s.

## Known, accepted
- `GSAP target #dots not found` (4x): the shared `brand/fx/reel_fx.js` theme expects a `#dots` background layer;
  this reel uses `#grid`. Harmless, and the shared file is in use by other reels, so it was left alone.

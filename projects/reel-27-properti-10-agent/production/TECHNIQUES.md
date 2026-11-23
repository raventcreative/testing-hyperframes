# reel-27 — properti, 10 agent AI (blue)

Reference: `e2b400d7` "Complete Real Estate AI Automation System — 10 AI Agents that work 24/7" (95 s),
condensed to 57.6 s. Beats kept in the reference's order; its product names, logos and UI are not reused.

## One shape per scene (never repeated)
night clock + chat bubble -> orbiting agent ring -> valuation card + donut stopwatch + comparable rows ->
three-way fork with its own detail per branch (week calendar / month strip / day-2+day-5 timeline) ->
photo grid collapsing into a written description sheet -> rule checklist + strike-through rewrite card ->
one listing fanning out to three lanes -> buyer chat + slot card + flipping DIJUAL/TERJUAL board ->
review stars + monthly value bars -> circular flywheel + stat chip row -> CTA.

## A different transition on every beat
zoom punch-through (hook) · element punch through the agent node · slats · iris · 3D swing + pop-out ·
blocks · slide swap · sweep · zoom-out reveal into the flywheel · zoom-through into the CTA.
Four of these are zooms, and `FX.iris` + `FX.slats` are the two the brief asked for.

## Robot
Hands alternate: `FX.point` uses the arm *opposite* the robot's side, `FX.wave` the arm *on* its side and
`FX.beat` alternates internally — so poses are varied deliberately (home/center/right/upL) to spread the work
across both arms rather than pointing right-handed all reel. Three bottom-band stretches, two fully visible
peeks, and two side rises (`upL` beside the right-hand fork column, `upL` beside the monthly-value card).
It is never zoomed and never stands over the element the VO is naming.

## Fixes worth carrying to the next reel
- **The no-cut guard hides full-width wrappers.** An element with `left:0;right:0` can never satisfy the
  "fully inside the frame" test, so it is hidden for the whole reel. Target the inner `span` in `UNIT`
  (`#orb24 > span`, not `#orb24`). Two chips were invisible until this was found.
- **Don't zoom a row that spans the full view width.** The three fork columns and the comparable rows span
  28..892; any zoom above ~1.06 slices them and the guard then blanks them. Those scenes stay at 1x and get
  their life from element motion instead.
- **A camera zoom-out reveal right after a view swap blanks the window**, because everything is "cut" at the
  start of the move. Use an element-level scale, or a slide swap, instead.
- **`rotationY` flips show both faces at once** (mirrored text) without `preserve-3d` + `backface-visibility`.
  A `scaleX` 1 -> 0 -> 1 swap reads as a card flip and is robust.
- SFX lanes are allocated by first-free-track so no two overlapping clips share one.

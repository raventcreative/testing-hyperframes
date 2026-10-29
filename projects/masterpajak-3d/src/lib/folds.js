// Fold profiles (bend angle as a function of position s along the sheet's vertical axis).
import { crease } from './PaperSheet.js';

// Z-fold (accordion) anchored on the TOP panel: header stays readable while folded.
// a1: top crease (middle panel goes behind), a2: bottom crease (folds back the other way)
export function zFold(h, a1, a2, band = 0.026) {
  const c1 = h / 6, c2 = -h / 6;
  return (s) => crease(-s, -c1, a1, band) - crease(-s, -c2, a2, band);
}

// Letter fold (C-fold) anchored on the MIDDLE panel. Bottom panel folds up in front first
// (tight crease), top panel folds down over it (looser crease so it wraps around).
// Folded, the viewer sees the BACK of the top panel = the report cover.
export function letterFold(h, aTop, aBottom, bandTop = 0.05, bandBottom = 0.022) {
  const c1 = h / 6, c2 = -h / 6;
  return (s) => crease(s, c1, aTop, bandTop) - crease(-s, -c2, aBottom, bandBottom);
}

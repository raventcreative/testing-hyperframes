// v4 scene re-timing shim (tools/retime_v4.py + tools/apply_warp.py).
// Scene timelines were authored on the v3 estimated word timing. __warpTL re-maps every numeric
// position argument of a scene timeline through the measured VO timing (window.VO_WARP: old word
// start -> new word start), so each visual hit lands on the word as it is actually spoken.
// In/out transition zones (first 0.45 s, last 0.3 s of the scene) are pinned; durations are unchanged.
// Pure function of the inputs -> deterministic.
(function () {
  function makeWarp(s0, s1) {
    const a = s0 + 0.45, b = s1 - 0.3;
    const pts = [[a, a]];
    for (const [o, n] of window.VO_WARP || []) if (o > a + 0.02 && o < b - 0.02 && n > a + 0.02 && n < b - 0.02 && n > pts[pts.length - 1][1] && o > pts[pts.length - 1][0]) pts.push([o, n]);
    pts.push([b, b]);
    return function (g) {
      if (g <= a || g >= b) return g;
      for (let i = 1; i < pts.length; i++) {
        if (g <= pts[i][0]) {
          const [x0, y0] = pts[i - 1], [x1, y1] = pts[i];
          return y0 + ((g - x0) * (y1 - y0)) / (x1 - x0);
        }
      }
      return g;
    };
  }
  const IDX = { to: 2, from: 2, fromTo: 3, set: 2, call: 2, add: 1 };
  window.__warpTL = function (tl, s0, s1) {
    const W = makeWarp(s0, s1);
    for (const name of Object.keys(IDX)) {
      const orig = tl[name].bind(tl), k = IDX[name];
      tl[name] = function () {
        const args = Array.prototype.slice.call(arguments);
        if (typeof args[k] === "number") args[k] = +(W(s0 + args[k]) - s0).toFixed(4);
        return orig.apply(null, args);
      };
    }
    return tl;
  };
})();

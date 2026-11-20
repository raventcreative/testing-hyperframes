// R29 time helpers (global time, VO offset included): word starts by text (+ "after" for repeats) and scene windows.
(function () {
  const VW = window.VO_WORDS, SC = window.VO_SCENES;
  const W = (txt, after = 0) => { const w = VW.find((x) => x[0] === txt && x[1] >= after - 1e-6); if (!w) throw new Error("R29: word not found " + txt + " after " + after); return w[1]; };
  const WE = (txt, after = 0) => { const w = VW.find((x) => x[0] === txt && x[1] >= after - 1e-6); if (!w) throw new Error("R29: word not found " + txt); return w[2]; };
  const S = (n) => SC[n - 1].start, E = (n) => SC[n - 1].start + SC[n - 1].dur;
  window.R29 = { W, WE, S, E, D: window.TOTAL };
})();

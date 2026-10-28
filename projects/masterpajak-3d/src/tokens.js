// Brand + production tokens. Every colour, font and export setting lives here.
// Colours were sampled from the supplied masterpajak.ai screenshot (site itself was
// not reachable from the render machine), so treat them as screenshot-accurate.

export const BRAND = {
  navy: '#212C5F',      // logo left stroke, primary buttons
  navyInk: '#161D3A',   // headline / body ink
  navyDeep: '#131B40',  // dark panels (video card)
  navySoft: '#26367A',  // lighter navy accent
  yellow: '#FED111',    // accent, marker highlight
  yellowSoft: '#FFE888',
  surface: '#EDEFF5',   // light UI surface
  line: '#E1E5EE',      // hairlines
  paper: '#FBFAF7',     // warm off-white paper (never pure white: keeps highlights alive)
  paperCool: '#F7F8FB', // report stock, slightly cooler / more premium
  thermal: '#FCFBF8',   // receipt thermal paper
  muted: '#6B7391',     // secondary ink
};

export const FONTS = {
  display: 'Rubik',        // visually matched to the site headline / wordmark
  mono: 'JetBrains Mono',  // receipt printing
};

export const OUTPUT = {
  width: 1080,
  height: 1080,
  fps: 60,
  greenHex: '#00FF00',
  // internal supersampling factor (render at 2x, box-filter down)
  ssaa: { draft: 1, final: 2 },
  // motion-blur sub-frames per output frame, shutter in fraction of frame time
  subframes: { draft: 1, final: 8 },
  shutter: 0.5, // 180 degree shutter
};

// Physical document sizes in scene units (1 unit ~ 25 cm)
export const DOC = {
  receipt: { w: 0.60, h: 1.30, t: 0.006 },
  statement: { w: 0.86, h: 1.216, t: 0.005 },
  report: { w: 0.86, h: 1.216, t: 0.007 },
};

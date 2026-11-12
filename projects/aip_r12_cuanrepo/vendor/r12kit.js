// Shared visual system of R12 ("5 alat gratis di GitHub jadi 5 menu jasa"), loaded in <head> before every scene.
// Metaphor of the reel: open-source code = a free RECIPE, the paid thing = the dish / the SERVICE ("menu jasa").
// Everything here is our own design (no screenshots, no third-party UI, no brand logos: platforms are text + generic icons).
// Icons: lucide 0.460 (ISC licence, assets/icons/LICENSE-lucide.txt), inlined so they take currentColor.
// - K.svg(k, sw)          : lucide icon markup
// - K.R                   : the five verified repos (name, path, licence chip, menu ticket text) — see production/VO_SCRIPT.md
// - K.head(p, i)          : the "recipe" header card of repo i (940×146 at 70,318); ids p-hd, p-lc (licence chip)
// - K.ticket(p, i)        : the "menu jasa" ticket of repo i (860×124 at 110,800); id p-tk
// - K.boot(ID)            : scene boilerplate → { ST, D, L, tl, ft, I, $, shake, done }
(function () {
  const ICO = {
    chef: '<path d="M17 21a1 1 0 0 0 1-1v-5.35c0-.457.316-.844.727-1.041a4 4 0 0 0-2.134-7.589 5 5 0 0 0-9.186 0 4 4 0 0 0-2.134 7.588c.411.198.727.585.727 1.041V20a1 1 0 0 0 1 1Z"/><path d="M6 17h12"/>',
    utensils: '<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/>',
    calendarClock: '<path d="M21 7.5V6a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h3.5"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h5"/><path d="M17.5 17.5 16 16.3V14"/><circle cx="16" cy="16" r="6"/>',
    camera: '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/>',
    music: '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
    briefcase: '<path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
    play: '<polygon points="6 3 20 12 6 21 6 3"/>',
    thumb: '<path d="M7 10v12"/><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z"/>',
    scissors: '<circle cx="6" cy="6" r="3"/><path d="M8.12 8.12 12 12"/><path d="M20 4 8.12 15.88"/><circle cx="6" cy="18" r="3"/><path d="M14.8 14.8 20 20"/>',
    film: '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 3v18"/><path d="M3 7.5h4"/><path d="M3 12h18"/><path d="M3 16.5h4"/><path d="M17 3v18"/><path d="M17 7.5h4"/><path d="M17 16.5h4"/>',
    mic: '<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/>',
    inbox: '<polyline points="22 12 16 12 14 15 10 15 8 12 2 12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/>',
    bot: '<path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/>',
    code: '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    braces: '<path d="M8 3H7a2 2 0 0 0-2 2v5a2 2 0 0 1-2 2 2 2 0 0 1 2 2v5c0 1.1.9 2 2 2h1"/><path d="M16 21h1a2 2 0 0 0 2-2v-5c0-1.1.9-2 2-2a2 2 0 0 1-2-2V5a2 2 0 0 0-2-2h-1"/>',
    shield: '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    scale: '<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
    search: '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    users: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    sheet: '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><line x1="3" x2="21" y1="9" y2="9"/><line x1="3" x2="21" y1="15" y2="15"/><line x1="9" x2="9" y1="9" y2="21"/><line x1="15" x2="15" y1="9" y2="21"/>',
    clapper: '<path d="M20.2 6 3 11l-.9-2.4c-.3-1.1.3-2.2 1.3-2.5l13.5-4c1.1-.3 2.2.3 2.5 1.3Z"/><path d="m6.2 5.3 3.1 3.9"/><path d="m12.4 3.4 3.1 4"/><path d="M3 11h18v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/>',
    wrench: '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    git: '<line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>',
    alert: '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    radio: '<path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"/><path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"/><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"/><path d="M19.1 4.9C23 8.8 23 15.1 19.1 19"/>',
    smile: '<circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" x2="9.01" y1="9" y2="9"/><line x1="15" x2="15.01" y1="9" y2="9"/>',
    pin: '<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
    phone: '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    listChecks: '<path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8"/><path d="M13 12h8"/><path d="M13 18h8"/>',
    book: '<path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/>',
    badge: '<path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"/><path d="m9 12 2 2 4-4"/>',
    help: '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
    layers: '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
    copy: '<rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>',
    sparkles: '<path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/>',
    gift: '<path d="M12 7v14"/><path d="M20 11v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8"/><path d="M7.5 7a1 1 0 0 1 0-5A4.8 8 0 0 1 12 7a4.8 8 0 0 1 4.5-5 1 1 0 0 1 0 5"/><rect x="3" y="7" width="18" height="4" rx="1"/>',
    pencil: '<path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/><path d="m15 5 4 4"/>',
    type: '<path d="M12 4v16"/><path d="M4 7V5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2"/><path d="M9 20h6"/>',
    pointer: '<path d="M4.037 4.688a.495.495 0 0 1 .651-.651l16 6.5a.5.5 0 0 1-.063.947l-6.124 1.58a2 2 0 0 0-1.438 1.435l-1.579 6.126a.5.5 0 0 1-.947.063z"/>',
    circleCheck: '<circle cx="12" cy="12" r="10"/><path d="m16 9-5.5 5.5L8 12"/>',
    check: '<path d="M20 6 9 17l-5-5"/>',
    x: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    send: '<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/>',
    heart: '<path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5"/>',
    msg: '<path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/>',
    user: '<circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/>',
    lock: '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    store: '<path d="m2 7 4.41-4.41A2 2 0 0 1 7.83 2h8.34a2 2 0 0 1 1.42.59L22 7"/><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><path d="M15 22v-4a2 2 0 0 0-2-2h-2a2 2 0 0 0-2 2v4"/><path d="M2 7h20"/><path d="M22 7v3a2 2 0 0 1-2 2 2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 16 12a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 12 12a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 8 12a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 4 12a2 2 0 0 1-2-2V7"/>',
    image: '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>',
    globe: '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
    file: '<path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/><path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    arrow: '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    bag: '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
    clock: '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    star: '<path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"/>',
  };
  const svg = (k, sw, cls) => `<svg class="${cls || ""}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[k]}</svg>`;

  // the five repos, in OUR order (easiest service to start → most technical; Remotion last because its licence leads into the caution)
  // licence facts checked 2026-11-12 on github.com (see production/VO_SCRIPT.md)
  const R = [
    { n: "Postiz", path: "gitroomhq/postiz-app", lic: "AGPL-3.0", tone: "info", ic: "calendarClock", job: "Jasa kelola sosmed", who: "buat toko & UMKM yang nggak sempat posting" },
    { n: "AutoClip", path: "zhouxiaoka/autoclip", lic: "MIT", tone: "ok", ic: "scissors", job: "Jasa potong klip", who: "buat podcaster & seller yang rutin live" },
    { n: "Chatwoot", path: "chatwoot/chatwoot", lic: "MIT*", tone: "ok", ic: "inbox", job: "Jasa admin chat", who: "buat toko online yang chat-nya banyak" },
    { n: "OpenHands", path: "OpenHands/OpenHands", lic: "MIT", tone: "ok", ic: "bot", job: "Jasa website UMKM", who: "AI yang ngoding, kamu yang arahkan & cek" },
    { n: "Remotion", path: "remotion-dev/remotion", lic: "Lisensi khusus", tone: "warn", ic: "clapper", job: "Jasa video produk", who: "satu template, video buat tiap produk" },
  ];

  const CSS = `
  .k-grad { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .k-card { background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 40px 70px -40px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); }
  .k-hd { position: absolute; left: 70px; top: 318px; width: 940px; height: 146px; border-radius: 30px; font-family: Poppins, sans-serif; transform-origin: 50% 50%; }
  .k-hd > * { position: absolute; }
  .k-hd-ic { left: 25px; top: 25px; width: 96px; height: 96px; border-radius: 28px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff; box-shadow: 0 14px 24px -14px rgba(10,13,44,.8); }
  .k-hd-ic svg { position: absolute; left: 24px; top: 24px; width: 48px; height: 48px; display: block; }
  .k-hd-eb { left: 148px; top: 22px; font: 700 15px/22px Poppins, sans-serif; letter-spacing: .16em; color: #5d6f8f; white-space: nowrap; }
  .k-hd-nm { left: 146px; top: 42px; font: 700 52px/64px Poppins, sans-serif; letter-spacing: -.01em; white-space: nowrap; padding-right: 4px; }
  .k-hd-pt { left: 148px; top: 106px; height: 24px; display: flex; align-items: center; gap: 7px; font: 400 18px/24px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .k-hd-pt svg { width: 18px; height: 18px; display: block; color: #294b77; flex: none; }
  .k-hd-lc { right: 26px; top: 26px; height: 46px; padding: 0 18px 0 48px; border-radius: 23px; font: 700 19px/46px Poppins, sans-serif; white-space: nowrap; transform-origin: 50% 50%; }
  .k-hd-lc svg { position: absolute; left: 16px; top: 12px; width: 22px; height: 22px; display: block; }
  .k-hd-lc.ok { background: #e8f6ed; color: #1f7a3a; box-shadow: inset 0 0 0 1.5px rgba(31,122,58,.2); }
  .k-hd-lc.info { background: #eaf0fe; color: #2a55c4; box-shadow: inset 0 0 0 1.5px rgba(42,85,196,.2); }
  .k-hd-lc.warn { background: #fff3dc; color: #94540a; box-shadow: inset 0 0 0 1.5px rgba(148,84,10,.25); }
  .k-hd-pg { right: 28px; top: 84px; font: 700 30px/38px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .k-hd-pg span { font: 400 20px/38px Poppins, sans-serif; color: #8a97b0; margin-left: 2px; }
  .k-tkw { position: absolute; left: 110px; top: 800px; width: 860px; height: 124px; filter: drop-shadow(0 20px 22px rgba(10,13,44,.2)); transform-origin: 50% 50%; }
  .k-tk { position: absolute; left: 0; top: 0; width: 860px; height: 124px; border-radius: 24px; overflow: hidden; font-family: Poppins, sans-serif; background: linear-gradient(180deg, #ffffff, #f6f8fd);
    -webkit-mask: radial-gradient(circle at 170px 0, transparent 15px, #000 16px) top / 100% 51% no-repeat, radial-gradient(circle at 170px 100%, transparent 15px, #000 16px) bottom / 100% 51% no-repeat;
    mask: radial-gradient(circle at 170px 0, transparent 15px, #000 16px) top / 100% 51% no-repeat, radial-gradient(circle at 170px 100%, transparent 15px, #000 16px) bottom / 100% 51% no-repeat; }
  .k-tk > * { position: absolute; }
  .k-tk-st { left: 0; top: 0; width: 170px; height: 124px; background: linear-gradient(150deg, #294b77, #0a0d2c); color: #ffffff; }
  .k-tk-st i { position: absolute; left: 63px; top: 14px; width: 44px; height: 44px; }
  .k-tk-st i svg { width: 44px; height: 44px; display: block; }
  .k-tk-st b { position: absolute; left: 0; top: 62px; width: 170px; text-align: center; font: 700 16px/22px Poppins, sans-serif; letter-spacing: .22em; text-indent: .22em; }
  .k-tk-st span { position: absolute; left: 0; top: 84px; width: 170px; text-align: center; font: 700 24px/28px Poppins, sans-serif; color: #8fd8ff; }
  .k-tk-pf { left: 169px; top: 20px; width: 0; height: 84px; border-left: 3px dashed #c9d4e6; }
  .k-tk-eb { left: 204px; top: 16px; font: 700 15px/22px Poppins, sans-serif; letter-spacing: .16em; color: #5d6f8f; white-space: nowrap; }
  .k-tk-nm { left: 202px; top: 36px; font: 700 40px/52px Poppins, sans-serif; white-space: nowrap; padding-right: 4px; }
  .k-tk-who { left: 204px; top: 86px; font: 400 20px/26px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .k-tk-ar { right: 26px; top: 38px; width: 48px; height: 48px; border-radius: 50%; background: #eef2f9; color: #294b77; }
  .k-tk-ar svg { position: absolute; left: 12px; top: 12px; width: 24px; height: 24px; display: block; }
  .k-chip { position: absolute; height: 54px; padding: 0 20px 0 54px; border-radius: 27px; background: #ffffff; color: #0a0d2c; white-space: nowrap; font: 700 22px/54px Poppins, sans-serif;
    box-shadow: 0 16px 26px -16px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); transform-origin: 50% 50%; }
  .k-chip svg { position: absolute; left: 18px; top: 14px; width: 26px; height: 26px; display: block; color: #294b77; }
  .k-ex { position: absolute; height: 30px; padding: 0 12px; border-radius: 15px; background: #ffffff; box-shadow: inset 0 0 0 1.5px #d9e2f0; font: 700 12px/30px Poppins, sans-serif; letter-spacing: .14em; color: #5d6f8f; white-space: nowrap; }
  `;
  if (!document.getElementById("k-css")) { const st = document.createElement("style"); st.id = "k-css"; st.textContent = CSS; (document.head || document.documentElement).appendChild(st); }

  const head = (p, i) => {
    const r = R[i];
    return `<div class="k-hd k-card" id="${p}-hd"><div class="k-hd-ic">${svg(r.ic, 2)}</div><div class="k-hd-eb">RESEP #${i + 1} · GRATIS DI GITHUB</div>` +
      `<div class="k-hd-nm k-grad">${r.n}</div><div class="k-hd-pt">${svg("git", 2.2)}github.com/${r.path}</div>` +
      `<div class="k-hd-lc ${r.tone}" id="${p}-lc">${svg(r.tone === "warn" ? "alert" : "shield", 2.2)}${r.lic}</div><div class="k-hd-pg">${i + 1}<span>/5</span></div></div>`;
  };
  const ticket = (p, i) => {
    const r = R[i];
    return `<div class="k-tkw" id="${p}-tk"><div class="k-tk"><div class="k-tk-st"><i>${svg("chef", 2)}</i><b>MENU</b><span>#${i + 1}</span></div><div class="k-tk-pf"></div>` +
      `<div class="k-tk-eb">MENU JASA</div><div class="k-tk-nm k-grad">${r.job}</div><div class="k-tk-who">${r.who}</div><div class="k-tk-ar">${svg("arrow", 2.4)}</div></div></div>`;
  };

  // scene boilerplate (identical in every scene): seek-safe scale shorthand, fromTo without immediate render, initial states pinned at 0
  const boot = (ID) => {
    const ST = window.SCN[ID][0], D = window.SCN[ID][1], VW = window.VO_WORDS;
    const L = (txt, after = 0) => { const w = VW.find((x) => x[0] === txt && x[1] >= ST + after - 0.05); if (!w) { console.error(ID + ": word not found " + txt); return 0; } return w[1] - ST; };
    const tl = gsap.timeline({ paused: true });
    const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
    { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); tl.set = (a, v, p) => s0(a, _sc(v), p); tl.fromTo = (a, x, y, p) => f0(a, _sc(x), _sc(y), p); tl.to = (a, v, p) => t0(a, _sc(v), p); }
    const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), t);
    const I = (el, v) => { gsap.set(el, _sc(v)); tl.set(el, v, 0); };
    const $ = (id) => document.getElementById(id);
    const shake = (el, t, amp = 6) => { [[amp, -amp * 0.6], [-amp * 0.8, amp * 0.4], [amp * 0.4, -amp * 0.2], [0, 0]].forEach(([x, y], k) => tl.set(el, { x, y }, t + k * 0.034)); };
    const done = () => {
      tl.set({}, {}, D - 0.01);
      (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
      window.__timelines = window.__timelines || {};
      window.__timelines[ID] = tl;
    };
    return { ST, D, L, tl, ft, I, $, shake, done };
  };

  window.K = { svg, ICO, R, head, ticket, boot };
})();

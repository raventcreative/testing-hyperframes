// Shared visual system of the WEB3D reel ("Jualan website 3D, 1 prompt jadi"), loaded in <head> before every scene.
// Everything here is our own design: the three example client sites (Kopi Senja · Langkah · Roti Bunda) and their floating
// products are SVG illustrations drawn here (no screenshots, no third-party site designs). Icons: lucide (ISC), inlined so they
// can be coloured with currentColor. Claude mark: assets/icons/lobe-claude-color.svg (lobehub, MIT).
// - R8.svg(k, sw)            : lucide icon
// - R8.TH                    : site themes (tpl = what the prompt builds before the client swap, kopi, sepatu, roti)
// - R8.site(p, keys, o)      : a browser card (900×590) holding one viewport group per theme key; ids:
//     p-card · p-u{k} (url pill per group) · p-ex ("CONTOH") · p-vp (viewport) · p-bg{k} (background) · p-g{k} (content group)
//     p-g{k}-{nav,mark,name,menu,nb,eb,h1,sub,ctas,cta,feat,ring,ring2,sh,pw,pi,o0..o2,steam}
// - R8.float(tl, p, k, ST, D): floating product + shadow + orbiters + steam of group k for one scene, as a pure function of GLOBAL
//                              time (piecewise, 15 steps/s) so a card handed over between scenes continues without a jump
// - R8.lib(p)                : the prompt-library window (illustration, 940×600 at 70,320) with 6 tiles (p-t{i}) + prompt chips
// - R8.miniTile(i)           : abstract tile art (own designs) for the library grid
(function () {
  const ICO = {
    copy: '<rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>',
    paste: '<path d="M11 14h10"/><path d="M16 4h2a2 2 0 0 1 2 2v1.344"/><path d="m17 18 4-4-4-4"/><path d="M8 4H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 1.793-1.113"/><rect x="8" y="2" width="8" height="4" rx="1"/>',
    sparkles: '<path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/>',
    tag: '<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r=".5" fill="currentColor"/>',
    gift: '<path d="M12 7v14"/><path d="M20 11v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8"/><path d="M7.5 7a1 1 0 0 1 0-5A4.8 8 0 0 1 12 7a4.8 8 0 0 1 4.5-5 1 1 0 0 1 0 5"/><rect x="3" y="7" width="18" height="4" rx="1"/>',
    pencil: '<path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/><path d="m15 5 4 4"/>',
    type: '<path d="M12 4v16"/><path d="M4 7V5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2"/><path d="M9 20h6"/>',
    wand: '<path d="m21.64 3.64-1.28-1.28a1.21 1.21 0 0 0-1.72 0L2.36 18.64a1.21 1.21 0 0 0 0 1.72l1.28 1.28a1.2 1.2 0 0 0 1.72 0L21.64 5.36a1.2 1.2 0 0 0 0-1.72"/><path d="m14 7 3 3"/><path d="M5 6v4"/><path d="M19 14v4"/><path d="M10 2v2"/><path d="M7 8H3"/><path d="M21 16h-4"/><path d="M11 3H9"/>',
    pkg: '<path d="M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z"/><path d="M12 22V12"/><polyline points="3.29 7 12 12 20.71 7"/><path d="m7.5 4.27 9 5.15"/>',
    layout: '<rect width="18" height="7" x="3" y="3" rx="1"/><rect width="9" height="7" x="3" y="14" rx="1"/><rect width="5" height="7" x="16" y="14" rx="1"/>',
    pointer: '<path d="M4.037 4.688a.495.495 0 0 1 .651-.651l16 6.5a.5.5 0 0 1-.063.947l-6.124 1.58a2 2 0 0 0-1.438 1.435l-1.579 6.126a.5.5 0 0 1-.947.063z"/>',
    listChecks: '<path d="M13 5h8"/><path d="M13 12h8"/><path d="M13 19h8"/><path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/>',
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
    eye: '<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>',
    share: '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.59 13.51 6.83 3.98"/><path d="m15.41 6.51-6.82 3.98"/>',
    up: '<path d="m5 12 7-7 7 7"/><path d="M12 19V5"/>',
    plus: '<path d="M5 12h14"/><path d="M12 5v14"/>',
    star: '<path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"/>',
    globe: '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
    file: '<path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/><path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    arrow: '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    coffee: '<path d="M10 2v2"/><path d="M14 2v2"/><path d="M16 8a1 1 0 0 1 1 1v8a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V9a1 1 0 0 1 1-1h14a4 4 0 1 1 0 8h-1"/><path d="M6 2v2"/>',
    bag: '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
    cookie: '<path d="M12 2a10 10 0 1 0 10 10 4 4 0 0 1-5-5 4 4 0 0 1-5-5"/><path d="M8.5 8.5v.01"/><path d="M16 15.5v.01"/><path d="M12 12v.01"/><path d="M11 17v.01"/><path d="M7 14v.01"/>',
    clock: '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    droplet: '<path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"/>',
    box: '<path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
    trend: '<path d="M16 7h6v6"/><path d="m22 7-8.5 8.5-5-5L2 17"/>',
    receipt: '<path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"/><path d="M8 7h8"/><path d="M8 11h8"/><path d="M8 15h5"/>',
    loader: '<path d="M21 12a9 9 0 1 1-6.219-8.56"/>',
  };
  const svg = (k, sw, cls) => `<svg class="${cls || ""}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[k]}</svg>`;

  // ---------------------------------------------------------------- PRODUCT ILLUSTRATIONS (own designs, shaded SVG)
  // each returns [svg markup, width, height] at display size; gradient ids are prefixed (several cards share one document)
  const PROD = {
    cup: (q) => [`<svg viewBox="0 -64 200 330" width="236" height="390" overflow="visible">
      <defs>
        <linearGradient id="${q}cb" x1="0" x2="1"><stop offset="0" stop-color="#d4cbbf"/><stop offset=".2" stop-color="#f3eee7"/><stop offset=".4" stop-color="#ffffff"/><stop offset=".72" stop-color="#ebe3d9"/><stop offset="1" stop-color="#b3a796"/></linearGradient>
        <linearGradient id="${q}sl" x1="0" x2="1"><stop offset="0" stop-color="#7c4820"/><stop offset=".36" stop-color="#d39a5c"/><stop offset=".7" stop-color="#b3733a"/><stop offset="1" stop-color="#5f3415"/></linearGradient>
        <linearGradient id="${q}ld" x1="0" x2="1"><stop offset="0" stop-color="#1e110b"/><stop offset=".38" stop-color="#5b3b29"/><stop offset=".66" stop-color="#3a2418"/><stop offset="1" stop-color="#150b07"/></linearGradient>
        <radialGradient id="${q}lt" cx=".38" cy=".3" r=".8"><stop offset="0" stop-color="#7d5641"/><stop offset="1" stop-color="#24150e"/></radialGradient>
      </defs>
      <g id="${q}steam" fill="none" stroke="#ffffff" stroke-width="7" stroke-linecap="round" opacity=".5">
        <path class="st" d="M76 28 q-12 -14 0 -28 q12 -14 0 -28 q-12 -14 0 -28" pathLength="1" stroke-dasharray=".42 .58"/>
        <path class="st" d="M102 22 q-12 -14 0 -28 q12 -14 0 -28 q-12 -14 0 -28" pathLength="1" stroke-dasharray=".38 .62"/>
        <path class="st" d="M128 28 q-12 -14 0 -28 q12 -14 0 -28 q-12 -14 0 -28" pathLength="1" stroke-dasharray=".44 .56"/>
      </g>
      <path d="M40 76 L160 76 L144 246 Q143 256 133 256 L67 256 Q57 256 56 246 Z" fill="url(#${q}cb)"/>
      <path d="M44.9 128 L155.1 128 L148.7 196 L51.3 196 Z" fill="url(#${q}sl)"/>
      <circle cx="100" cy="162" r="21" fill="#2a1a12"/>
      <g transform="rotate(28 100 162)"><ellipse cx="100" cy="162" rx="9" ry="13" fill="#e8b07a"/><path d="M100 150 q-5 12 0 24" stroke="#2a1a12" stroke-width="2.6" fill="none"/></g>
      <path d="M64 84 L75 84 L71 246 L66 246 Z" fill="#ffffff" opacity=".6"/>
      <rect x="30" y="62" width="140" height="21" rx="9" fill="url(#${q}ld)"/>
      <path d="M46 64 Q50 38 100 36 Q150 38 154 64 Z" fill="url(#${q}lt)"/>
      <ellipse cx="126" cy="49" rx="9" ry="4" fill="#0e0704"/>
      <path d="M60 58 Q66 45 94 42" stroke="#ffffff" stroke-opacity=".35" stroke-width="4" fill="none" stroke-linecap="round"/>
    </svg>`, 236, 390],
    shoe: (q) => {
      const lace = [0, 0.25, 0.5, 0.75, 1].map((t) => { const x = 140 + 70 * t, y = 72 + 44 * t; return `<path d="M${(x - 5.3).toFixed(1)} ${(y + 8.5).toFixed(1)} L${(x + 5.3).toFixed(1)} ${(y - 8.5).toFixed(1)}"/>`; }).join("");
      return [`<svg viewBox="0 0 340 200" width="390" height="230" overflow="visible">
      <defs>
        <linearGradient id="${q}up" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".68" stop-color="#e9eef9"/><stop offset="1" stop-color="#c3cde6"/></linearGradient>
        <linearGradient id="${q}pn" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ecff6e"/><stop offset="1" stop-color="#9fc40e"/></linearGradient>
        <linearGradient id="${q}so" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d9e0ee"/></linearGradient>
      </defs>
      <path d="M40 136 C34 112 30 88 34 66 C36 54 46 48 58 48 L104 46 C116 46 124 52 130 62 L158 98 C172 114 196 118 222 120 L280 124 C306 126 318 134 320 146 L320 150 L40 150 Z" fill="url(#${q}up)"/>
      <path d="M58 48 L104 46 C116 46 124 52 130 62 L121 66 C113 57 105 55 97 56 L62 58 Z" fill="#14206b" opacity=".9"/>
      <path d="M70 142 C92 104 140 96 176 112 C204 124 240 128 292 130 C262 139 214 143 170 133 C136 125 104 129 86 148 Z" fill="url(#${q}pn)"/>
      <path d="M34 70 C30 90 32 116 38 138 L52 138 C46 114 45 92 49 72 Z" fill="#1f3fd1"/>
      <circle cx="98" cy="112" r="15" fill="#14206b"/><circle cx="98" cy="112" r="8" fill="none" stroke="#d7f53b" stroke-width="3.4"/>
      <g stroke="#14206b" stroke-width="4.4" stroke-linecap="round">${lace}</g>
      <ellipse cx="292" cy="134" rx="20" ry="5" fill="#ffffff" opacity=".7"/>
      <path d="M30 146 L326 146 C334 146 336 152 334 160 L330 170 C328 176 322 178 314 178 L44 178 C34 178 28 172 28 164 Z" fill="url(#${q}so)"/>
      <path d="M60 161 L300 161" stroke="#c9d3ea" stroke-width="3" stroke-linecap="round"/>
      <path d="M29 171 L333 171 L331 176 C329 181 323 183 315 183 L44 183 C35 183 30 179 29 173 Z" fill="#14206b"/>
    </svg>`, 390, 230];
    },
    croissant: (q) => [`<svg viewBox="0 0 300 190" width="350" height="222" overflow="visible">
      <defs>
        <radialGradient id="${q}cr" cx=".45" cy=".32" r=".78"><stop offset="0" stop-color="#ffe6a8"/><stop offset=".42" stop-color="#f3b55a"/><stop offset=".84" stop-color="#c8761e"/><stop offset="1" stop-color="#93500f"/></radialGradient>
      </defs>
      <g fill="url(#${q}cr)">
        <ellipse cx="46" cy="122" rx="36" ry="21" transform="rotate(36 46 122)"/><ellipse cx="254" cy="122" rx="36" ry="21" transform="rotate(-36 254 122)"/>
        <ellipse cx="94" cy="100" rx="46" ry="41" transform="rotate(25 94 100)"/><ellipse cx="206" cy="100" rx="46" ry="41" transform="rotate(-25 206 100)"/>
        <ellipse cx="150" cy="90" rx="54" ry="58"/>
      </g>
      <g fill="none" stroke="#9c5612" stroke-opacity=".55" stroke-width="3.2" stroke-linecap="round">
        <path d="M112 58 Q100 96 114 134"/><path d="M188 58 Q200 96 186 134"/><path d="M66 90 Q58 114 70 138"/><path d="M234 90 Q242 114 230 138"/>
      </g>
      <ellipse cx="136" cy="60" rx="24" ry="10" fill="#ffffff" opacity=".38"/><ellipse cx="84" cy="80" rx="14" ry="6" fill="#ffffff" opacity=".25" transform="rotate(-20 84 80)"/>
    </svg>`, 350, 222],
  };
  const BEAN = `<svg viewBox="0 0 24 32" width="26" height="34"><ellipse cx="12" cy="16" rx="10" ry="14" fill="#5a3522"/><ellipse cx="9" cy="11" rx="3" ry="5" fill="#8a5a3c" opacity=".7"/><path d="M12 3 q-6 13 0 26" stroke="#2a160c" stroke-width="2.2" fill="none"/></svg>`;
  const ORB = {
    bean: () => BEAN,
    ball: () => `<i style="display:block;width:28px;height:28px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#f6ffb0,#d7f53b 45%,#86a30a)"></i>`,
    sugar: () => `<i style="display:block;width:24px;height:24px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff8de,#ffd77a 50%,#d39a2a)"></i>`,
    ph: () => `<i style="display:block;width:22px;height:22px;border-radius:7px;background:rgba(255,255,255,.35)"></i>`,
  };

  // ---------------------------------------------------------------- THEMES (example client sites — illustrative, labelled CONTOH)
  const TH = {
    tpl: { n: "Nama Brand", f: "website-baru.html", L: "B", bg: "radial-gradient(120% 90% at 78% 40%, #67739f 0%, #3a4470 48%, #232a4a 100%)", ac: "#c9d2ee", at: "#1c2340",
      eb: "TEMPLATE DARI PROMPT", h: ["Judul besar", "di sini."], sub: "Deskripsi singkat usaha klien kamu, nanti diganti.", cta: "Tombol utama", cta2: "Tombol kedua",
      nav: ["Menu", "Tentang", "Kontak"], nb: "Pesan", prod: "ph", orb: "ph", feat: [["image", "Foto"], ["type", "Teks"], ["sparkles", "Animasi"]] },
    kopi: { n: "Kopi Senja", f: "kopi-senja.html", L: "K", bg: "radial-gradient(120% 90% at 78% 40%, #7a4d34 0%, #3e2619 46%, #1d120c 100%)", ac: "#e8b07a", at: "#2a1a12",
      eb: "KEDAI KOPI LOKAL", h: ["Kopi sore,", "bikin betah."], sub: "Kopi susu gula aren, diseduh tiap ada pesanan.", cta: "Pesan sekarang", cta2: "Lihat menu",
      nav: ["Menu", "Tentang", "Lokasi"], nb: "Pesan", prod: "cup", orb: "bean", feat: [["coffee", "Biji lokal"], ["droplet", "Gula aren"], ["send", "Antar cepat"]] },
    sepatu: { n: "Langkah", f: "langkah-sneakers.html", L: "L", bg: "radial-gradient(120% 90% at 78% 40%, #5a85ff 0%, #2448d8 50%, #13237f 100%)", ac: "#d7f53b", at: "#14206b",
      eb: "SNEAKERS LOKAL", h: ["Melangkah", "lebih ringan."], sub: "Desain lokal, nyaman dipakai seharian.", cta: "Belanja sekarang", cta2: "Lihat koleksi",
      nav: ["Koleksi", "Ukuran", "Kontak"], nb: "Belanja", prod: "shoe", orb: "ball", feat: [["star", "Desain lokal"], ["heart", "Nyaman"], ["send", "Kirim cepat"]] },
    roti: { n: "Roti Bunda", f: "roti-bunda.html", L: "R", bg: "radial-gradient(120% 90% at 78% 40%, #f2845a 0%, #c9452d 52%, #8a2516 100%)", ac: "#ffd77a", at: "#5a1a0e",
      eb: "TOKO ROTI RUMAHAN", h: ["Hangat dari", "oven tiap pagi."], sub: "Croissant mentega dan roti manis, dipanggang harian.", cta: "Pesan antar", cta2: "Lihat menu",
      nav: ["Menu", "Tentang", "Lokasi"], nb: "Pesan", prod: "croissant", orb: "sugar", feat: [["clock", "Fresh tiap pagi"], ["heart", "Resep rumahan"], ["send", "Pesan antar"]] },
  };
  // product placement inside the 880×524 viewport (centre of the floating product)
  const PCN = { x: 664, y: 236 };
  const ORBIT = { kopi: [0.0, 2.1, 4.2], sepatu: [0.6, 2.7, 4.8], roti: [1.1, 3.2, 5.3], tpl: [0.3, 2.4, 4.5] };

  const group = (p, k, i, mir) => {
    const t = TH[k], q = `${p}-g${i}`, PC = mir ? { x: 880 - PCN.x, y: PCN.y } : PCN;
    let pr;
    if (t.prod === "ph") pr = [`<div class="r8-ph"><div class="ic">${svg("image", 1.8)}</div><b>Foto produk</b><span>ganti nanti</span></div>`, 230, 230];
    else pr = PROD[t.prod](q + "-");
    const [ps, pw, ph] = pr;
    return `<div class="r8-g${mir ? " mir" : ""}" id="${q}" style="--ac:${t.ac};--at:${t.at}">` +
      `<div class="r8-ring" id="${q}-ring" style="left:${PC.x - 170}px;top:${PC.y - 170}px"></div><div class="r8-ring2" id="${q}-ring2" style="left:${PC.x - 118}px;top:${PC.y - 118}px"></div>` +
      `<div class="r8-sh" id="${q}-sh" style="left:${PC.x - 120}px;top:${PC.y + 178}px"></div>` +
      `<div class="r8-nav" id="${q}-nav"><div class="mk" id="${q}-mark">${t.L}</div><b class="nm" id="${q}-name">${t.n}</b>` +
      `<div class="mn" id="${q}-menu">${t.nav.map((m) => `<span>${m}</span>`).join("")}</div><div class="nb" id="${q}-nb">${t.nb}</div></div>` +
      `<div class="r8-eb" id="${q}-eb">${t.eb}</div>` +
      `<div class="r8-h1" id="${q}-h1"><span>${t.h[0]}</span><span>${t.h[1]}</span></div>` +
      `<div class="r8-sub" id="${q}-sub">${t.sub}</div>` +
      `<div class="r8-ctas" id="${q}-ctas"><div class="c1" id="${q}-cta">${t.cta}${svg("arrow", 2.6)}</div><div class="c2" id="${q}-cta2">${t.cta2}</div></div>` +
      `<div class="r8-feat" id="${q}-feat">${t.feat.map((f) => `<div>${svg(f[0], 2.2)}${f[1]}</div>`).join("")}</div>` +
      [0, 1, 2].map((j) => `<div class="r8-orb" id="${q}-o${j}" style="left:${PC.x}px;top:${PC.y}px">${ORB[t.orb]()}</div>`).join("") +
      `<div class="r8-pw" id="${q}-pw" style="left:${PC.x - pw / 2}px;top:${PC.y - ph / 2}px;width:${pw}px;height:${ph}px"><div class="r8-pi" id="${q}-pi">${ps}</div></div>` +
      `</div>`;
  };
  // the browser card: 900×590; keys = theme keys stacked (index i = order); o.badge adds a "1 prompt" badge (id p-badge)
  const site = (p, keys, o) => {
    o = o || {};
    let h = `<div class="r8-card" id="${p}-card"${o.style ? ` style="${o.style}"` : ""}><div class="cb"></div><div class="dots"><i></i><i></i><i></i></div>` +
      keys.map((k, i) => `<div class="url" id="${p}-u${i}">${svg("lock", 2.4)}<span>${TH[k].f}</span></div>`).join("") +
      `<div class="ex" id="${p}-ex">CONTOH</div><div class="r8-vp" id="${p}-vp">` +
      keys.map((k, i) => `<div class="r8-bg" id="${p}-bg${i}" style="background:${TH[k].bg}"></div>`).join("") +
      `<div class="r8-gl"></div>` + keys.map((k, i) => group(p, k, i, o.mirror)).join("") + `</div>` +
      (o.badge ? `<div class="r8-badge" id="${p}-badge">${svg("sparkles", 2.4)}<b>1 prompt</b></div>` : "") + `</div>`;
    return h;
  };

  // float: product bob + 3D wobble (flat plane, own perspective), shadow breathing, orbiters on a tilted ellipse (in front of /
  // behind the product by z-index), steam drift. Pure function of GLOBAL time g.
  const fAt = (g, s) => ({
    y: -16 * Math.sin(2 * Math.PI * g / 2.7 + s), rotation: 3 * Math.sin(2 * Math.PI * g / 3.5 + 1.7 * s),
    rotationY: 18 * Math.sin(2 * Math.PI * g / 4.4 + 0.6 * s), rotationX: 6 * Math.sin(2 * Math.PI * g / 3.1 + s),
  });
  const oAt = (g, ph, k) => { const a = 2 * Math.PI * g / 3.8 + ph; const s = Math.sin(a); return { x: 196 * Math.cos(a), y: 54 * s - 20 * Math.cos(a) + (k === 1 ? -40 : 0), scale: 0.78 + 0.32 * s, z: s > 0 ? 6 : 1 }; };
  const float = (tl, p, i, key, ST, D, o) => {
    o = o || {};
    const q = `${p}-g${i}`, pi = document.getElementById(q + "-pi"), sh = document.getElementById(q + "-sh");
    const seed = { kopi: 0.2, sepatu: 1.3, roti: 2.4, tpl: 3.1 }[key] || 0;
    const step = 1 / 15, n = Math.ceil(D / step);
    const f0 = fAt(ST, seed);
    tl.set(pi, Object.assign({ transformPerspective: 720 }, f0), 0);
    tl.set(sh, { scaleX: 1 + f0.y / 90, scaleY: 1 + f0.y / 90, opacity: 0.9 + f0.y / 60 }, 0);
    const orbs = o.noOrb ? [] : [0, 1, 2].map((j) => document.getElementById(`${q}-o${j}`));
    const PH = ORBIT[key] || [0, 2.1, 4.2];
    orbs.forEach((e, j) => { const v = oAt(ST, PH[j], j); tl.set(e, { x: v.x, y: v.y, scale: v.scale, zIndex: v.z }, 0); });
    for (let k = 0; k < n; k++) {
      const t0 = k * step, d = Math.min(step, D - t0), g1 = ST + t0 + d, f = fAt(g1, seed);
      tl.to(pi, Object.assign({ duration: d, ease: "none" }, f), t0);
      tl.to(sh, { scaleX: 1 + f.y / 90, scaleY: 1 + f.y / 90, opacity: 0.9 + f.y / 60, duration: d, ease: "none" }, t0);
      orbs.forEach((e, j) => {
        const a = oAt(ST + t0, PH[j], j), b = oAt(g1, PH[j], j);
        tl.to(e, { x: b.x, y: b.y, scale: b.scale, duration: d, ease: "none" }, t0);
        if (a.z !== b.z) tl.set(e, { zIndex: b.z }, t0 + d / 2);
      });
    }
    // steam (cup only): dash offset linear in global time
    if (key === "kopi") document.querySelectorAll(`#${q}-steam .st`).forEach((e, j) => {
      const off = (g) => -((g * 0.45 + j * 0.31) % 1000);
      tl.fromTo(e, { attr: { "stroke-dashoffset": off(ST) } }, { attr: { "stroke-dashoffset": off(ST + D) }, duration: D, ease: "none", immediateRender: false }, 0);
      tl.set(e, { attr: { "stroke-dashoffset": off(ST) } }, 0);
    });
  };

  // generic piecewise animation of el by a pure function of GLOBAL time fn(g) -> vars (continuous across scene cuts)
  const wave = (tl, el, ST, D, fn, rate) => {
    const step = 1 / (rate || 15), n = Math.ceil(D / step);
    tl.set(el, fn(ST), 0);
    for (let k = 0; k < n; k++) { const t0 = k * step, d = Math.min(step, D - t0); tl.to(el, Object.assign({ duration: d, ease: "none" }, fn(ST + t0 + d)), t0); }
  };
  // the library tiles' art: each moves by a function of global time (same in s03 / s04 / s10, so the window hands over cleanly)
  const tileArt = (tl, p, ST, D) => {
    const F = [
      (g) => ({ y: -8 * Math.sin(2 * Math.PI * g / 2.4), scale: 1 + 0.03 * Math.sin(2 * Math.PI * g / 2.4 + 1) }),
      (g) => ({ rotation: g * 40, y: -5 * Math.sin(2 * Math.PI * g / 3) }),
      (g) => ({ y: -9 * Math.sin(2 * Math.PI * g / 2.8 + 1.5), rotation: 6 * Math.sin(2 * Math.PI * g / 3.6) }),
      (g) => ({ y: -7 * Math.sin(2 * Math.PI * g / 2.2 + 0.7), rotation: 4 * Math.sin(2 * Math.PI * g / 2.9) }),
      (g) => ({ rotation: g * -28, scale: 1 + 0.05 * Math.sin(2 * Math.PI * g / 2.6) }),
      (g) => ({ x: -10 * Math.sin(2 * Math.PI * g / 3.2), y: 3 * Math.sin(2 * Math.PI * g / 1.6) }),
    ];
    for (let i = 0; i < 6; i++) {
      const art = document.getElementById(`${p}-t${i}a`); if (!art) continue;
      const el = i === 3 ? art : art.firstElementChild; wave(tl, el, ST, D, F[i], 10);
    }
  };
  // ---------------------------------------------------------------- THE PROMPT LIBRARY window (illustration of the idea; our own tiles)
  const TILE = [
    { bg: "linear-gradient(150deg,#5b3df5,#2a1a8f)", art: `<i class="sph" style="left:150px;top:30px;width:104px;height:104px;background:radial-gradient(circle at 34% 30%,#ffffff,#b9a8ff 30%,#6a4cf0 62%,#2b1a8a)"></i>` },
    { bg: "linear-gradient(150deg,#0f9b8e,#0b4f63)", art: `<i class="tor" style="left:146px;top:26px;width:110px;height:110px"></i>` },
    { bg: "linear-gradient(150deg,#ff8a1f,#d1460f)", art: `<svg class="cube" style="left:150px;top:22px" width="110" height="118" viewBox="0 0 110 118"><path d="M55 4 L104 30 L55 56 L6 30 Z" fill="#ffd7a6"/><path d="M6 30 L55 56 L55 114 L6 88 Z" fill="#ff9d4d"/><path d="M104 30 L55 56 L55 114 L104 88 Z" fill="#c2410c"/></svg>` },
    { bg: "linear-gradient(150deg,#1d6cf2,#0b2f86)", art: `<i class="cap" style="left:142px;top:34px"></i><i class="cap c2" style="left:182px;top:52px"></i>` },
    { bg: "linear-gradient(150deg,#22a35a,#0d5a33)", art: `<i class="blob" style="left:150px;top:28px;width:110px;height:104px"></i>` },
    { bg: "linear-gradient(160deg,#151a3f,#2a3470)", art: `<svg class="wav" style="left:120px;top:40px" width="150" height="96" viewBox="0 0 150 96" fill="none" stroke="#7fd0ff" stroke-width="2.4" stroke-linecap="round">${[0, 1, 2, 3, 4, 5].map((r) => `<path opacity="${(0.35 + r * 0.12).toFixed(2)}" d="M0 ${18 + r * 13} C30 ${4 + r * 13} 50 ${32 + r * 13} 75 ${18 + r * 13} S120 ${4 + r * 13} 150 ${18 + r * 13}"/>`).join("")}</svg>` },
  ];
  const miniTile = (i, id) => {
    const t = TILE[i];
    return `<div class="r8-tile" id="${id}" style="background:${t.bg}"><div class="tn"><i></i><i></i><i></i></div><div class="tl1"></div><div class="tl2"></div><div class="tb"></div>` +
      `<div class="art" id="${id}a">${t.art}</div><div class="pc" id="${id}p">${svg("copy", 2.4)}Prompt</div></div>`;
  };
  const LIB = { x: 70, y: 320, w: 940, h: 600, tx: (c) => 34 + c * 296, ty: (r) => 166 + r * 206 };
  const lib = (p) => {
    let h = `<div class="r8-lib" id="${p}-lib"><div class="cb"></div><div class="dots"><i></i><i></i><i></i></div>` +
      `<div class="url" id="${p}-lurl">${svg("lock", 2.4)}<span>motionsites.ai</span></div><div class="ex">ILUSTRASI</div>` +
      `<div class="hd"><b class="r8-grad" id="${p}-lt">MotionSites</b><span id="${p}-ls">Library prompt website animasi &amp; 3D</span></div>` +
      `<div class="pm" id="${p}-lpm">${svg("lock", 2.4)}Berbayar</div>`;
    for (let i = 0; i < 6; i++) h += `<div class="r8-tw" id="${p}-tw${i}" style="left:${LIB.tx(i % 3)}px;top:${LIB.ty(Math.floor(i / 3))}px">${miniTile(i, `${p}-t${i}`)}</div>`;
    return h + `</div>`;
  };

  // ---------------------------------------------------------------- THE CLAUDE CHAT window (s04 · s05): 940×590 at 70,330
  // ids: p-chat · p-cmk (Claude mark) · p-mc0 / p-mc1 (model chips Claude / AI lain) · p-greet · p-in (field) · p-ph (placeholder)
  // · p-pst (pasted prompt in the field) · p-send · p-ub (user bubble in the thread) · p-dots (typing) · p-ab (assistant bubble)
  // · p-cl{0..5} (code bars) · p-ok (done row)
  const PROMPT1 = "Buat landing page 3D untuk [nama brand]: produk melayang, berputar pelan, tombol pesan, rapi di HP.";
  const chat = (p) => {
    const bars = [[0, 160, "#7c5cff"], [24, 230, "#3a6fe0"], [24, 180, "#2da44e"], [48, 250, "#e8b07a"], [24, 140, "#3a6fe0"], [0, 120, "#7c5cff"]];
    return `<div class="r8-chat" id="${p}-chat"><div class="cb"></div>` +
      `<div class="cmk" id="${p}-cmk"><i></i></div><b class="cnm">Claude</b>` +
      `<div class="mc on" id="${p}-mc0">${svg("check", 3)}Claude</div><div class="mc" id="${p}-mc1">${svg("sparkles", 2.2)}AI lain</div><div class="dv"></div>` +
      `<div class="greet" id="${p}-greet">Halo! Mau bikin apa hari ini?</div>` +
      `<div class="ub" id="${p}-ub"><div class="tg">${svg("paste", 2.2)}Prompt website 3D</div><div class="tx">${PROMPT1}</div></div>` +
      `<div class="dots" id="${p}-dots"><i></i><i></i><i></i></div>` +
      `<div class="ab" id="${p}-ab"><div class="am"><i></i></div><b>Siap, aku bikinin websitenya.</b><div class="code">` +
      bars.map((b, i) => `<i id="${p}-cl${i}" style="left:${b[0] + 20}px;top:${14 + i * 20}px;width:${b[1]}px;background:${b[2]}"></i>`).join("") + `</div>` +
      `<div class="ok" id="${p}-ok">${svg("circleCheck", 2.4)}index.html siap</div></div>` +
      `<div class="in" id="${p}-in"></div><div class="ph" id="${p}-ph">Tempel prompt di sini…</div>` +
      `<div class="pst" id="${p}-pst"><div class="tg">${svg("paste", 2.2)}Prompt website 3D</div><div class="tx">${PROMPT1}</div></div>` +
      `<div class="snd" id="${p}-send">${svg("send", 2.2)}</div></div>`;
  };
  const ccss = `
  .r8-chat { position: absolute; left: 70px; top: 330px; width: 940px; height: 590px; transform-origin: 50% 50%; font-family: Poppins, sans-serif; }
  .r8-chat .cb { position: absolute; inset: 0; border-radius: 32px; background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 56px 90px -42px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); }
  .r8-chat .cmk { position: absolute; left: 26px; top: 18px; width: 52px; height: 52px; border-radius: 50%; background: #fff4ee; box-shadow: inset 0 0 0 2px #f3d9cc; transform-origin: 50% 50%; }
  .r8-chat .cmk i, .r8-chat .am i { position: absolute; left: 11px; top: 11px; width: 30px; height: 30px; background: url(assets/icons/lobe-claude-color.svg) center / contain no-repeat; }
  .r8-chat .cnm { position: absolute; left: 92px; top: 18px; font: 700 26px/52px Poppins, sans-serif; color: #0a0d2c; }
  .r8-chat .mc { position: absolute; top: 24px; height: 40px; padding: 0 16px 0 40px; border-radius: 20px; background: #eef2f9; color: #5d6f8f; font: 700 16px/40px Poppins, sans-serif; white-space: nowrap; transform-origin: 50% 50%; }
  .r8-chat .mc svg { position: absolute; left: 14px; top: 11px; width: 18px; height: 18px; display: block; }
  .r8-chat .mc.on { left: 620px; background: #0a0d2c; color: #ffffff; }
  .r8-chat .mc:not(.on) { left: 774px; }
  .r8-chat .dv { position: absolute; left: 0; right: 0; top: 86px; height: 1.5px; background: #e6ecf6; }
  .r8-chat .greet { position: absolute; left: 0; right: 0; top: 230px; text-align: center; font: 400 22px/32px Poppins, sans-serif; color: #9aa7c0; }
  .r8-chat .ub { position: absolute; left: 352px; top: 108px; width: 560px; height: 124px; border-radius: 26px 26px 8px 26px; background: linear-gradient(150deg, #294b77, #0a0d2c); color: #ffffff; transform-origin: 100% 100%;
    box-shadow: 0 18px 30px -18px rgba(10,13,44,.85); }
  .r8-chat .ub .tg { position: absolute; left: 22px; top: 14px; height: 34px; padding: 0 14px 0 38px; border-radius: 17px; background: rgba(255,255,255,.14); font: 700 16px/34px Poppins, sans-serif; white-space: nowrap; }
  .r8-chat .ub .tg svg { position: absolute; left: 12px; top: 8px; width: 18px; height: 18px; display: block; color: #8fd8ff; }
  .r8-chat .ub .tx { position: absolute; left: 24px; top: 56px; width: 512px; font: 400 16px/24px Poppins, sans-serif; color: rgba(255,255,255,.85); }
  .r8-chat .dots { position: absolute; left: 28px; top: 256px; width: 96px; height: 50px; border-radius: 25px; background: #eef2f9; }
  .r8-chat .dots i { position: absolute; top: 19px; width: 12px; height: 12px; border-radius: 50%; background: #5d6f8f; }
  .r8-chat .dots i:nth-child(1) { left: 22px; } .r8-chat .dots i:nth-child(2) { left: 42px; } .r8-chat .dots i:nth-child(3) { left: 62px; }
  .r8-chat .ab { position: absolute; left: 28px; top: 252px; width: 600px; height: 196px; border-radius: 26px 26px 26px 8px; background: #ffffff; box-shadow: 0 16px 30px -18px rgba(10,13,44,.5), 0 0 0 1.5px #e3eaf5; transform-origin: 0% 100%; }
  .r8-chat .am { position: absolute; left: 16px; top: 14px; width: 52px; height: 52px; border-radius: 50%; background: #fff4ee; }
  .r8-chat .ab b { position: absolute; left: 80px; top: 14px; font: 700 20px/52px Poppins, sans-serif; color: #0a0d2c; white-space: nowrap; }
  .r8-chat .code { position: absolute; left: 16px; top: 76px; width: 568px; height: 132px; }
  .r8-chat .code i { position: absolute; height: 10px; border-radius: 5px; opacity: .85; transform-origin: 0% 50%; }
  .r8-chat .ok { position: absolute; right: 18px; bottom: 16px; height: 34px; padding: 0 14px 0 38px; border-radius: 17px; background: #eaf7ee; color: #1a7434; font: 700 15px/34px Poppins, sans-serif; white-space: nowrap; }
  .r8-chat .ok svg { position: absolute; left: 12px; top: 8px; width: 18px; height: 18px; display: block; }
  .r8-chat .in { position: absolute; left: 26px; top: 470px; width: 776px; height: 94px; border-radius: 28px; background: #f3f6fc; box-shadow: inset 0 0 0 2px #dbe4f3; }
  .r8-chat .ph { position: absolute; left: 56px; top: 470px; font: 400 22px/94px Poppins, sans-serif; color: #9aa7c0; white-space: nowrap; }
  .r8-chat .pst { position: absolute; left: 40px; top: 480px; width: 748px; height: 74px; }
  .r8-chat .pst .tg { position: absolute; left: 0; top: 2px; height: 32px; padding: 0 14px 0 38px; border-radius: 16px; background: #0a0d2c; color: #ffffff; font: 700 15px/32px Poppins, sans-serif; white-space: nowrap; }
  .r8-chat .pst .tg svg { position: absolute; left: 12px; top: 7px; width: 18px; height: 18px; display: block; color: #8fd8ff; }
  .r8-chat .pst .tx { position: absolute; left: 4px; top: 42px; width: 740px; font: 400 16px/26px Poppins, sans-serif; color: #294b77; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .r8-chat .snd { position: absolute; left: 818px; top: 470px; width: 94px; height: 94px; border-radius: 50%; background: linear-gradient(150deg, #4a7ff0, #294b77); color: #ffffff; transform-origin: 50% 50%;
    box-shadow: 0 14px 24px -12px rgba(58,111,224,.95); }
  .r8-chat .snd svg { position: absolute; left: 26px; top: 28px; width: 40px; height: 40px; display: block; }
  `;
  const css = `
  .r8-grad { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .r8-card { position: absolute; left: 90px; top: 330px; width: 900px; height: 590px; transform-origin: 50% 50%; font-family: Poppins, sans-serif; }
  .r8-card .cb { position: absolute; inset: 0; border-radius: 30px; background: linear-gradient(180deg, #ffffff, #f4f7fc);
    box-shadow: 0 56px 90px -42px rgba(10,13,44,.6), 0 0 0 1.5px rgba(10,13,44,.07); }
  .r8-card .dots { position: absolute; left: 26px; top: 22px; display: flex; gap: 9px; }
  .r8-card .dots i { display: block; width: 12px; height: 12px; border-radius: 50%; background: #c9d4e6; }
  .r8-card .url { position: absolute; left: 96px; top: 11px; width: 360px; height: 34px; border-radius: 17px; background: #eef2f9; }
  .r8-card .url svg { position: absolute; left: 14px; top: 9px; width: 16px; height: 16px; color: #5d6f8f; display: block; }
  .r8-card .url span { position: absolute; left: 38px; top: 0; font: 400 16px/34px Poppins, sans-serif; color: #294b77; white-space: nowrap; }
  .r8-card .ex { position: absolute; right: 22px; top: 12px; height: 32px; padding: 0 14px; border-radius: 16px; background: #ffffff; box-shadow: inset 0 0 0 1.5px #d9e2f0;
    font: 700 13px/32px Poppins, sans-serif; letter-spacing: .14em; color: #5d6f8f; white-space: nowrap; }
  .r8-vp { position: absolute; left: 10px; top: 56px; width: 880px; height: 524px; border-radius: 6px 6px 22px 22px; overflow: hidden; }
  .r8-bg { position: absolute; inset: 0; }
  .r8-gl { position: absolute; inset: 0; background-image: linear-gradient(90deg, rgba(255,255,255,.05) 1px, transparent 1px), linear-gradient(0deg, rgba(255,255,255,.05) 1px, transparent 1px); background-size: 44px 44px; }
  .r8-g { position: absolute; inset: 0; }
  .r8-ring { position: absolute; width: 340px; height: 340px; border-radius: 50%; box-shadow: inset 0 0 0 2px rgba(255,255,255,.16); background: radial-gradient(closest-side, rgba(255,255,255,.14), rgba(255,255,255,0)); }
  .r8-ring2 { position: absolute; width: 236px; height: 236px; border-radius: 50%; border: 2px dashed rgba(255,255,255,.18); }
  .r8-sh { position: absolute; width: 240px; height: 40px; border-radius: 50%; background: radial-gradient(closest-side, rgba(0,0,0,.42), rgba(0,0,0,0)); transform-origin: 50% 50%; }
  .r8-nav .mk { position: absolute; left: 30px; top: 20px; width: 40px; height: 40px; border-radius: 50%; background: var(--ac); color: var(--at); font: 700 19px/40px Poppins, sans-serif; text-align: center; }
  .r8-nav .nm { position: absolute; left: 82px; top: 20px; font: 700 21px/40px Poppins, sans-serif; color: #ffffff; white-space: nowrap; }
  .r8-nav .mn { position: absolute; left: 448px; top: 20px; display: flex; gap: 30px; font: 400 15px/40px Poppins, sans-serif; color: rgba(255,255,255,.72); white-space: nowrap; }
  .r8-nav .nb { position: absolute; right: 30px; top: 20px; height: 40px; padding: 0 20px; border-radius: 20px; background: var(--ac); color: var(--at); font: 700 15px/40px Poppins, sans-serif; white-space: nowrap; }
  .r8-eb { position: absolute; left: 34px; top: 108px; height: 30px; padding: 0 14px; border-radius: 15px; box-shadow: inset 0 0 0 1.5px var(--ac); color: var(--ac);
    font: 700 12px/30px Poppins, sans-serif; letter-spacing: .16em; white-space: nowrap; }
  .r8-h1 { position: absolute; left: 32px; top: 150px; width: 470px; font: 700 46px/54px Poppins, sans-serif; color: #ffffff; letter-spacing: -.01em; }
  .r8-h1 span { display: block; white-space: nowrap; }
  .r8-sub { position: absolute; left: 34px; top: 270px; width: 360px; font: 400 17px/26px Poppins, sans-serif; color: rgba(255,255,255,.78); }
  .r8-ctas { position: absolute; left: 34px; top: 340px; display: flex; gap: 12px; }
  .r8-ctas .c1 { height: 54px; padding: 0 22px; border-radius: 27px; background: var(--ac); color: var(--at); font: 700 17px/54px Poppins, sans-serif; white-space: nowrap; display: flex; align-items: center; gap: 8px; transform-origin: 50% 50%; }
  .r8-ctas .c1 svg { width: 18px; height: 18px; display: block; }
  .r8-ctas .c2 { height: 54px; padding: 0 20px; border-radius: 27px; box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.4); color: #ffffff; font: 400 16px/54px Poppins, sans-serif; white-space: nowrap; }
  .r8-feat { position: absolute; left: 34px; top: 434px; display: flex; gap: 10px; }
  .r8-feat div { position: relative; height: 38px; padding: 0 14px 0 38px; border-radius: 19px; background: rgba(255,255,255,.1); color: rgba(255,255,255,.88); font: 400 14px/38px Poppins, sans-serif; white-space: nowrap; }
  .r8-feat svg { position: absolute; left: 13px; top: 10px; width: 18px; height: 18px; color: var(--ac); display: block; }
  .r8-g.mir .r8-eb, .r8-g.mir .r8-h1, .r8-g.mir .r8-sub, .r8-g.mir .r8-ctas, .r8-g.mir .r8-feat { left: 466px; }
  .r8-pw { position: absolute; z-index: 4; }
  .r8-pi { position: absolute; inset: 0; transform-origin: 50% 55%; }
  .r8-pi svg { display: block; }
  .r8-orb { position: absolute; width: 0; height: 0; z-index: 1; }
  .r8-orb > * { position: absolute; left: -14px; top: -16px; }
  .r8-ph { position: absolute; inset: 0; border-radius: 30px; background: rgba(255,255,255,.12); box-shadow: inset 0 0 0 3px rgba(255,255,255,.4); border: 0; }
  .r8-ph .ic { position: absolute; left: 75px; top: 52px; width: 80px; height: 80px; color: rgba(255,255,255,.85); }
  .r8-ph .ic svg { width: 80px; height: 80px; display: block; }
  .r8-ph b { position: absolute; left: 0; right: 0; top: 146px; text-align: center; font: 700 20px/28px Poppins, sans-serif; color: #ffffff; }
  .r8-ph span { position: absolute; left: 0; right: 0; top: 176px; text-align: center; font: 400 15px/22px Poppins, sans-serif; color: rgba(255,255,255,.7); }
  .r8-badge { position: absolute; left: 640px; top: -26px; height: 54px; padding: 0 22px 0 52px; border-radius: 27px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff;
    box-shadow: 0 16px 30px -14px rgba(10,13,44,.8); transform-origin: 50% 50%; white-space: nowrap; }
  .r8-badge svg { position: absolute; left: 18px; top: 15px; width: 24px; height: 24px; display: block; color: #8fd8ff; }
  .r8-badge b { font: 700 22px/54px Poppins, sans-serif; }
  /* library window */
  .r8-lib { position: absolute; left: 70px; top: 320px; width: 940px; height: 600px; transform-origin: 50% 50%; font-family: Poppins, sans-serif; }
  .r8-lib .cb { position: absolute; inset: 0; border-radius: 32px; background: linear-gradient(180deg, #ffffff, #f4f7fc); box-shadow: 0 56px 90px -42px rgba(10,13,44,.55), 0 0 0 1.5px rgba(10,13,44,.07); }
  .r8-lib .dots { position: absolute; left: 26px; top: 22px; display: flex; gap: 9px; }
  .r8-lib .dots i { display: block; width: 12px; height: 12px; border-radius: 50%; background: #c9d4e6; }
  .r8-lib .url { position: absolute; left: 96px; top: 11px; width: 330px; height: 34px; border-radius: 17px; background: #eef2f9; transform-origin: 50% 50%; }
  .r8-lib .url svg { position: absolute; left: 14px; top: 9px; width: 16px; height: 16px; color: #5d6f8f; display: block; }
  .r8-lib .url span { position: absolute; left: 38px; top: 0; font: 400 16px/34px Poppins, sans-serif; color: #294b77; white-space: nowrap; }
  .r8-lib .ex { position: absolute; right: 22px; top: 12px; height: 32px; padding: 0 14px; border-radius: 16px; background: #ffffff; box-shadow: inset 0 0 0 1.5px #d9e2f0;
    font: 700 13px/32px Poppins, sans-serif; letter-spacing: .14em; color: #5d6f8f; white-space: nowrap; }
  .r8-lib .hd { position: absolute; left: 34px; top: 68px; }
  .r8-lib .hd b { display: block; font: 700 40px/48px Poppins, sans-serif; letter-spacing: -.01em; white-space: nowrap; }
  .r8-lib .hd span { display: block; font: 400 18px/26px Poppins, sans-serif; color: #5d6f8f; white-space: nowrap; }
  .r8-lib .pm { position: absolute; right: 34px; top: 82px; height: 42px; padding: 0 18px 0 44px; border-radius: 21px; background: #0a0d2c; color: #ffffff; font: 700 16px/42px Poppins, sans-serif; white-space: nowrap; transform-origin: 50% 50%; }
  .r8-lib .pm svg { position: absolute; left: 16px; top: 11px; width: 19px; height: 19px; display: block; color: #8fd8ff; }
  .r8-tw { position: absolute; width: 276px; height: 186px; transform-origin: 50% 50%; }
  .r8-tile { position: absolute; inset: 0; border-radius: 20px; overflow: hidden; box-shadow: 0 18px 30px -20px rgba(10,13,44,.7); }
  .r8-tile .tn { position: absolute; left: 16px; top: 14px; display: flex; gap: 5px; }
  .r8-tile .tn i { display: block; width: 22px; height: 5px; border-radius: 3px; background: rgba(255,255,255,.45); }
  .r8-tile .tl1 { position: absolute; left: 16px; top: 62px; width: 104px; height: 12px; border-radius: 6px; background: rgba(255,255,255,.92); }
  .r8-tile .tl2 { position: absolute; left: 16px; top: 82px; width: 76px; height: 12px; border-radius: 6px; background: rgba(255,255,255,.7); }
  .r8-tile .tb { position: absolute; left: 16px; top: 108px; width: 64px; height: 20px; border-radius: 10px; background: rgba(255,255,255,.95); }
  .r8-tile .art { position: absolute; inset: 0; }
  .r8-tile .art > * { position: absolute; }
  .r8-tile .sph, .r8-tile .tor, .r8-tile .blob { display: block; border-radius: 50%; }
  .r8-tile .tor { background: conic-gradient(from 30deg, #b8fff2, #19c2ae, #0b6e72, #6ff0dc, #b8fff2); -webkit-mask: radial-gradient(closest-side, transparent 52%, #000 54%); mask: radial-gradient(closest-side, transparent 52%, #000 54%); }
  .r8-tile .cap { display: block; width: 46px; height: 100px; border-radius: 23px; background: linear-gradient(90deg, #7fb2ff, #ffffff 40%, #4d8bff 80%, #1f4fcf); transform: rotate(-24deg); }
  .r8-tile .cap.c2 { height: 84px; background: linear-gradient(90deg, #ffd36b, #fff6d6 40%, #ffbf2e 80%, #c98a00); transform: rotate(18deg); }
  .r8-tile .blob { border-radius: 46% 54% 58% 42% / 52% 40% 60% 48%; background: radial-gradient(circle at 34% 30%, #eaffef, #6fe39a 40%, #1d9c55 75%, #0d5a33); }
  .r8-tile .pc { position: absolute; right: 12px; bottom: 12px; height: 34px; padding: 0 14px 0 36px; border-radius: 17px; background: #ffffff; color: #0a0d2c; font: 700 14px/34px Poppins, sans-serif; white-space: nowrap; box-shadow: 0 8px 14px -8px rgba(0,0,0,.6); transform-origin: 70% 50%; }
  .r8-tile .pc svg { position: absolute; left: 12px; top: 9px; width: 16px; height: 16px; display: block; color: #294b77; }
  `;
  const st = document.createElement("style"); st.textContent = css + ccss; (document.head || document.documentElement).appendChild(st);
  window.R8 = { ICO, svg, TH, PROD, site, float, fAt, lib, LIB, miniTile, PC: PCN, wave, tileArt, chat, PROMPT1 };
})();

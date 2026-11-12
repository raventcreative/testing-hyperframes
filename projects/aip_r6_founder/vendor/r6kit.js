// Shared visual system of the FOUNDER reel (R6 "Tes ide bisnis ke 100 pembeli AI sebelum keluar modal"), loaded in <head> before
// every scene. Icons: lucide (ISC), inlined so they take currentColor. Claude mark: assets/icons/lobe-claude-color.svg (lobehub, MIT).
// - R6.svg(name, strokeWidth)      : inline lucide icon
// - R6.SK                          : the 3 featured Founder skills (board / cfo / consumer) — name, command, colour, icon
// - R6.CMDS                        : the 11 commands of the Founder skill pack (README order)
// - R6.crowd(p, x, y)              : the PANEL = 100 AI buyers, 20 x 5 avatars (ids p-a0 … p-a99), same look in every scene
// - R6.BUY                         : the 18 avatars that "buy" in the example (18 / 100)
// - R6.EX                          : the EXAMPLE numbers (illustrative, labelled "contoh simulasi" wherever they are shown)
// - R6.PEOPLE                      : three example AI-buyer personas (fictional)
(function () {
  const ICO = {
    bulb: '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>',
    users: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    user: '<circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/>',
    wallet: '<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/>',
    utensils: '<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/>',
    clock: '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    shieldCheck: '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    crown: '<path d="M11.562 3.266a.5.5 0 0 1 .876 0L15.39 8.87a1 1 0 0 0 1.516.294L21.183 5.5a.5.5 0 0 1 .798.519l-2.834 10.246a1 1 0 0 1-.956.734H5.81a1 1 0 0 1-.957-.734L2.02 6.02a.5.5 0 0 1 .798-.519l4.276 3.664a1 1 0 0 0 1.516-.294z"/><path d="M5 21h14"/>',
    gift: '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13"/><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5A4.8 8 0 0 1 12 8a4.8 8 0 0 1 4.5-5 2.5 2.5 0 0 1 0 5"/>',
    box: '<path d="M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z"/><path d="M12 22V12"/><path d="m3.3 7 7.703 4.734a2 2 0 0 0 1.994 0L20.7 7"/><path d="m7.5 4.27 9 5.15"/>',
    spark: '<path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/>',
    calc: '<rect width="16" height="20" x="4" y="2" rx="2"/><path d="M8 6h8"/><path d="M16 14v4"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/>',
    trend: '<path d="M16 7h6v6"/><path d="m22 7-8.5 8.5-5-5L2 17"/>',
    msg: '<path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/>',
    send: '<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/>',
    check: '<path d="M20 6 9 17l-5-5"/>',
    x: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    flask: '<path d="M14 2v6a2 2 0 0 0 .245.96l5.51 10.08A2 2 0 0 1 18 22H6a2 2 0 0 1-1.755-2.96l5.51-10.08A2 2 0 0 0 10 8V2"/><path d="M6.453 15h11.094"/><path d="M8.5 2h7"/>',
    cart: '<circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/>',
    repeat: '<path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/>',
    help: '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
    folder: '<path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/>',
    code: '<path d="m16 18 6-6-6-6"/><path d="m8 6-6 6 6 6"/>',
    target: '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    flame: '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
    truck: '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
    pause: '<rect x="14" y="4" width="4" height="16" rx="1"/><rect x="6" y="4" width="4" height="16" rx="1"/>',
    store: '<path d="m2 7 4.41-4.41A2 2 0 0 1 7.83 2h8.34a2 2 0 0 1 1.42.59L22 7"/><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><path d="M15 22v-4a2 2 0 0 0-2-2h-2a2 2 0 0 0-2 2v4"/><path d="M2 7h20"/>',
    heart: '<path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5"/>',
    star: '<path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"/>',
    out: '<path d="M7 7h10v10"/><path d="M7 17 17 7"/>',
    arrowR: '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    arrowD: '<path d="M12 5v14"/><path d="m19 12-7 7-7-7"/>',
    minus: '<path d="M5 12h14"/>',
    lock: '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    coins: '<circle cx="8" cy="8" r="6"/><path d="M18.09 10.37A6 6 0 1 1 10.34 18"/><path d="M7 6h1v4"/><path d="m16.71 13.88.7.71-2.82 2.82"/>',
  };
  const svg = (k, sw, cls) => `<svg class="${cls || ""}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[k]}</svg>`;
  // the 3 featured skills (semantic colours used across the reel)
  const SK = {
    board: { cmd: "/founder-board", n: "Dewan Direksi", c: "#7c5cff", d: "#6141e8", soft: "#efebff", ic: "crown" },
    cfo: { cmd: "/founder-cfo", n: "CFO", c: "#3a6fe0", d: "#2a57c2", soft: "#e8effd", ic: "calc" },
    panel: { cmd: "/founder-consumer", n: "Panel Konsumen", c: "#294b77", d: "#1c3658", soft: "#e7edf6", ic: "users" },
  };
  // README order of the 11 commands (github.com/Jakeschincariol/founder-skill)
  const CMDS = ["board", "competitors", "consumer", "pricing", "offer", "cfo", "marketing", "brand", "ops", "launch", "plan"];
  // EXAMPLE (illustrative only, consistent): katering makan siang kantor, Rp25.000 / porsi
  //  bahan 11.000 + kemasan 2.000 + kurir 3.000 = 16.000 → sisa 9.000 / porsi (36 %) · biaya tetap 3,6 jt / bulan, 20 hari kerja
  //  → balik modal 3.600.000 / 9.000 = 400 porsi / bulan = 20 porsi / hari · panel: 18 / 100 mau beli; 82 belum = 34 + 29 + 19
  const EX = { price: 25000, bahan: 11000, kemasan: 2000, kurir: 3000, sisa: 9000, margin: 36, tetap: 3600000, hari: 20, bep: 20,
    buy: 18, no: 82, why: [["Bawa bekal dari rumah", 34], ["Warteg lebih murah", 29], ["Takut telat sampai", 19]] };
  const rp = (n) => "Rp" + String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  // the panel: 20 x 5 avatars, pitch 44.4, size 36
  const CROWD = { cols: 20, rows: 5, pitch: 44.4, size: 36, w: 880, h: 214 };
  const BUY = [3, 11, 17, 24, 29, 36, 42, 48, 53, 57, 64, 69, 71, 78, 84, 88, 93, 97];
  const TONES = [["#e8effd", "#3a6fe0"], ["#efebff", "#7c5cff"], ["#e7edf6", "#294b77"], ["#fff3d6", "#b7791f"], ["#fdecec", "#c2410c"], ["#eef2f9", "#5d6f8f"]];
  const hash = (n) => { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };
  const avatar = (id, i, x, y, sz) => {
    const t = TONES[Math.floor(hash(i + 3) * TONES.length)];
    return `<div class="r6-av" id="${id}" style="left:${x.toFixed(1)}px;top:${y.toFixed(1)}px;width:${sz}px;height:${sz}px;--bg:${t[0]};--fg:${t[1]}"><i class="hd"></i><i class="sh"></i><i class="ok"></i></div>`;
  };
  const crowd = (p, x, y) => {
    let h = `<div class="r6-crowd" id="${p}-cr" style="left:${x}px;top:${y}px">`;
    for (let i = 0; i < 100; i++) h += avatar(`${p}-a${i}`, i, (i % CROWD.cols) * CROWD.pitch, Math.floor(i / CROWD.cols) * CROWD.pitch, CROWD.size);
    return h + `</div>`;
  };
  const PEOPLE = [
    { nm: "Rina, 27", job: "Staf admin · Jakarta", inc: "Rp5,5 jt / bulan", hab: "Bawa bekal 4× seminggu", dbt: "“Bekal dari rumah lebih hemat.”", buy: false, i: 27 },
    { nm: "Dimas, 31", job: "Sales lapangan · Bekasi", inc: "Rp7 jt / bulan", hab: "Makan di warteg dekat kantor", dbt: "“Warteg lebih murah.”", buy: false, i: 62 },
    { nm: "Sari, 35", job: "Manajer · Jakarta", inc: "Rp14 jt / bulan", hab: "Pesan makan online tiap hari", dbt: "“Mau, asal sampai sebelum jam 12.”", buy: true, i: 48 },
  ];
  const css = `
  .r6-grad { background: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .r6-card { position: absolute; border-radius: 30px; background: linear-gradient(180deg, #ffffff, #f6f8fd); box-shadow: 0 40px 76px -36px rgba(10,13,44,.5), 0 0 0 1.5px rgba(10,13,44,.07); transform-origin: 50% 50%; }
  .r6-ex { position: absolute; height: 30px; padding: 0 14px 0 34px; border-radius: 15px; background: #ffffff; box-shadow: inset 0 0 0 1.5px #d9e2f0;
    font: 700 13px/30px Poppins, sans-serif; letter-spacing: .14em; color: #5d6f8f; white-space: nowrap; transform-origin: 50% 50%; }
  .r6-ex svg { position: absolute; left: 12px; top: 7px; width: 16px; height: 16px; display: block; color: #7c5cff; }
  .r6-cmd { position: absolute; height: 44px; padding: 0 18px 0 50px; border-radius: 22px; background: linear-gradient(135deg, #0a0d2c, #294b77); color: #ffffff;
    font: 700 19px/44px Poppins, sans-serif; white-space: nowrap; box-shadow: 0 14px 24px -14px rgba(10,13,44,.8); transform-origin: 50% 50%; }
  .r6-cmd i { position: absolute; left: 7px; top: 7px; width: 30px; height: 30px; border-radius: 50%; background: #ffffff; }
  .r6-cmd i::after { content: ""; position: absolute; left: 6px; top: 6px; width: 18px; height: 18px; background: url(assets/icons/lobe-claude-color.svg) center / contain no-repeat; }
  .r6-crowd { position: absolute; width: 880px; height: 214px; }
  .r6-av { position: absolute; border-radius: 50%; background: var(--bg); box-shadow: inset 0 0 0 1.5px rgba(10,13,44,.06); transform-origin: 50% 50%; overflow: hidden; }
  .r6-av .hd { position: absolute; left: 32%; top: 18%; width: 36%; height: 36%; border-radius: 50%; background: var(--fg); }
  .r6-av .sh { position: absolute; left: 16%; top: 60%; width: 68%; height: 60%; border-radius: 50%; background: var(--fg); }
  .r6-av .ok { position: absolute; inset: 0; border-radius: 50%; box-shadow: inset 0 0 0 3px #2da44e; background: rgba(45,164,78,.16); opacity: 0; }
  .r6-big { position: absolute; transform-origin: 50% 50%; }
  `;
  const st = document.createElement("style"); st.textContent = css; (document.head || document.documentElement).appendChild(st);
  window.R6 = { ICO, svg, SK, CMDS, EX, rp, CROWD, BUY, crowd, avatar, PEOPLE, hash };
})();

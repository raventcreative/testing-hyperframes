// R13 TRADER — shared scene kit (loaded in index.html <head> after vo_words.js; every scene uses window.R13K).
// Components (identical in every scene that shows them): the LAYER HEADER (icon/number roll, title, one-line job, layer chip,
// 3 layer segments), the 11 SKILL CHIPS sorted into 3 shelves (CARI / RENCANA / REM), lucide icons (ISC), the Claude mark, the
// timeline boilerplate (scale patch, ft, I, wt, seek patch, per-letter typing). Deterministic: no Math.random, no Date, no rAF.
(function () {
  const K = (window.R13K = {});
  // ------------------------------------------------------------------ icons (lucide, ISC)
  const SH = '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>';
  K.IC = {
    search: '<path d="m21 21-4.34-4.34"/><circle cx="11" cy="11" r="8"/>',
    scan: '<path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/><path d="M7 21H5a2 2 0 0 1-2-2v-2"/><circle cx="12" cy="12" r="3"/><path d="m16 16-1.9-1.9"/>',
    news: '<path d="M15 18h-5"/><path d="M18 14h-8"/><path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-4 0v-9a2 2 0 0 1 2-2h2"/><rect width="8" height="4" x="10" y="6" rx="1"/>',
    report: '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    landmark: '<path d="M3 22h18"/><path d="M6 18v-7"/><path d="M10 18v-7"/><path d="M14 18v-7"/><path d="M18 18v-7"/><path d="M12 2 20 7H4z"/>',
    login: '<path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><path d="m10 17 5-5-5-5"/><path d="M15 12H3"/>',
    target: '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    history: '<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l4 2"/>',
    wallet: '<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/>',
    shield: SH,
    shieldok: SH + '<path d="m9 12 2 2 4-4"/>',
    shieldx: SH + '<path d="m14.5 9.5-5 5"/><path d="m9.5 9.5 5 5"/>',
    send: '<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/>',
    bell: '<path d="M10.268 21a2 2 0 0 0 3.464 0"/><path d="M3.262 15.326A1 1 0 0 0 4 17h16a1 1 0 0 0 .74-1.673C19.41 13.956 18 12.499 18 8A6 6 0 0 0 6 8c0 4.499-1.411 5.956-2.738 7.326"/>',
    lock: '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    unlock: '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/>',
    globe: '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
    grad: '<path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
    hand: '<path d="M18 11V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2"/><path d="M14 10V4a2 2 0 0 0-2-2a2 2 0 0 0-2 2v2"/><path d="M10 10.5V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"/>',
    candle: '<path d="M9 5v4"/><rect width="4" height="6" x="7" y="9" rx="1"/><path d="M9 15v2"/><path d="M17 3v2"/><rect width="4" height="8" x="15" y="5" rx="1"/><path d="M17 13v3"/><path d="M3 3v16a2 2 0 0 0 2 2h16"/>',
    layers: '<path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z"/><path d="M2 12a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 12"/><path d="M2 17a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 17"/>',
    folder: '<path d="m6 14 1.5-2.9A2 2 0 0 1 9.24 10H20a2 2 0 0 1 1.94 2.5l-1.54 6a2 2 0 0 1-1.95 1.5H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h3.9a2 2 0 0 1 1.69.9l.81 1.2a2 2 0 0 0 1.67.9H18a2 2 0 0 1 2 2v2"/>',
    terminal: '<path d="M12 19h8"/><path d="m4 17 6-6-6-6"/>',
    check: '<path d="M20 6 9 17l-5-5"/>',
    x: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    user: '<circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/>',
    bot: '<path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/>',
    link: '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
    heart: '<path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5"/>',
    alert: '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    info: '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
    message: '<path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/>',
    clock: '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    trend: '<path d="M16 7h6v6"/><path d="m22 7-8.5 8.5-5-5L2 17"/>',
    pointer: '<path d="M4.037 4.688a.495.495 0 0 1 .651-.651l16 6.5a.5.5 0 0 1-.063.947l-6.124 1.58a2 2 0 0 0-1.438 1.435l-1.579 6.126a.5.5 0 0 1-.947.063z"/>',
    coins: '<circle cx="8" cy="8" r="6"/><path d="M18.09 10.37A6 6 0 1 1 10.34 18"/><path d="M7 6h1v4"/><path d="m16.71 13.88.7.71-2.82 2.82"/>',
    sparkles: '<path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/>',
  };
  K.svg = (n, cls = "", extra = "") =>
    `<svg class="${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ${extra}>${K.IC[n]}</svg>`;
  K.CLAUDE_D = "M4.709 15.955l4.72-2.647.08-.23-.08-.128H9.2l-.79-.048-2.698-.073-2.339-.097-2.266-.122-.571-.121L0 11.784l.055-.352.48-.321.686.06 1.52.103 2.278.158 1.652.097 2.449.255h.389l.055-.157-.134-.098-.103-.097-2.358-1.596-2.552-1.688-1.336-.972-.724-.491-.364-.462-.158-1.008.656-.722.881.06.225.061.893.686 1.908 1.476 2.491 1.833.365.304.145-.103.019-.073-.164-.274-1.355-2.446-1.446-2.49-.644-1.032-.17-.619a2.97 2.97 0 01-.104-.729L6.283.134 6.696 0l.996.134.42.364.62 1.414 1.002 2.229 1.555 3.03.456.898.243.832.091.255h.158V9.01l.128-1.706.237-2.095.23-2.695.08-.76.376-.91.747-.492.584.28.48.685-.067.444-.286 1.851-.559 2.903-.364 1.942h.212l.243-.242.985-1.306 1.652-2.064.73-.82.85-.904.547-.431h1.033l.76 1.129-.34 1.166-1.064 1.347-.881 1.142-1.264 1.7-.79 1.36.073.11.188-.02 2.856-.606 1.543-.28 1.841-.315.833.388.091.395-.328.807-1.969.486-2.309.462-3.439.813-.042.03.049.061 1.549.146.662.036h1.622l3.02.225.79.522.474.638-.079.485-1.215.62-1.64-.389-3.829-.91-1.312-.329h-.182v.11l1.093 1.068 2.006 1.81 2.509 2.33.127.578-.322.455-.34-.049-2.205-1.657-.851-.747-1.926-1.62h-.128v.17l.444.649 2.345 3.521.122 1.08-.17.353-.608.213-.668-.122-1.374-1.925-1.415-2.167-1.143-1.943-.14.08-.674 7.254-.316.37-.729.28-.607-.461-.322-.747.322-1.476.389-1.924.315-1.53.286-1.9.17-.632-.012-.042-.14.018-1.434 1.967-2.18 2.945-1.726 1.845-.414.164-.717-.37.067-.662.401-.589 2.388-3.036 1.44-1.882.93-1.086-.006-.158h-.055L4.132 18.56l-1.13.146-.487-.456.061-.746.231-.243 1.908-1.312-.006.006z";
  K.claude = (cls = "") => `<svg class="${cls}" viewBox="0 0 24 24"><path d="${K.CLAUDE_D}" fill="#D97757"/></svg>`;

  // ------------------------------------------------------------------ the eleven skills (README of Jakeschincariol/day-trader-skill,
  // "The eleven" table, checked 12 Nov 2026), grouped into OUR three layers: 0 CARI (find), 1 RENCANA (plan), 2 REM (brake)
  K.SK = [
    { n: "scanner", l: "ribuan grafik", ic: "scan", L: 0 },
    { n: "news", l: "berita pemicu", ic: "news", L: 0 },
    { n: "analyst", l: "laporan kuartal", ic: "report", L: 0 },
    { n: "pelosi", l: "Kongres AS", ic: "landmark", L: 0 },
    { n: "entry", l: "titik masuk", ic: "login", L: 1 },
    { n: "exit", l: "stop loss · target", ic: "target", L: 1 },
    { n: "time machine", l: "10.000 simulasi", ic: "history", L: 1 },
    { n: "budget", l: "ukuran posisi", ic: "wallet", L: 2 },
    { n: "risk", l: "PASS / BLOCK", ic: "shield", L: 2 },
    { n: "broker", l: "tunggu 'ya' kamu", ic: "send", L: 2 },
    { n: "alerts", l: "alarm posisi", ic: "bell", L: 2 },
  ];
  K.LAYERS = [
    { n: "CARI", ic: "search" },
    { n: "RENCANA", ic: "target" },
    { n: "REM", ic: "hand" },
  ];
  // shelf geometry (global px): three glass bands, label block on the left, chips on the right
  K.SHELF = { x: 60, w: 960, h: 132, ys: [484, 630, 776] };
  // chip k of layer L: 4 chips of 176 px (layers 0, 2) or 3 chips of 241 px (layer 1), 10 px gaps, from x 264
  K.chipXY = (i) => {
    const s = K.SK[i], L = s.L, k = K.SK.filter((x, j) => x.L === L && j < i).length, w = L === 1 ? 241 : 176;
    return { x: 264 + k * (w + 10), y: K.SHELF.ys[L] + 16, w };
  };

  // header items: 0 repo · 1 lapis cari · 2 lapis rencana · 3 time machine · 4 lapis rem · 5 broker · 6 catatan · 7 cara pasang
  K.HD = [
    { tile: "folder", name: "day-trader-skill", sub: "<i>github.com/</i>Jakeschincariol", chip: "MIT", chipIc: "unlock" },
    { tile: "01", name: "Lapis cari", sub: "scanner &middot; news &middot; analyst &middot; pelosi", chip: "CARI", chipIc: "search" },
    { tile: "02", name: "Lapis rencana", sub: "entry &middot; exit &middot; time machine", chip: "RENCANA", chipIc: "target" },
    { tile: "history", name: "/trader-timemachine", sub: "simulasi dulu, uang belakangan", chip: "RENCANA", chipIc: "target" },
    { tile: "03", name: "Lapis rem", sub: "budget &middot; risk &middot; broker &middot; alerts", chip: "REM", chipIc: "hand" },
    { tile: "lock", name: "/trader-broker", sub: "order cuma lewat persetujuan kamu", chip: "REM", chipIc: "hand" },
    { tile: "alert", name: "Catatan jujur", sub: "baca ini sebelum nyoba", chip: "EDUKASI", chipIc: "grad" },
    { tile: "terminal", name: "Cara pasang", sub: "1 link GitHub &middot; tempel ke Claude", chip: "GRATIS", chipIc: "unlock" },
  ];
  // which layer segments are lit for header item k
  K.HSEG = [0, 1, 2, 2, 3, 3, 3, 3];

  // ------------------------------------------------------------------ geometry (global px)
  K.HDR = { x: 60, y: 312, w: 960, h: 140 };
  K.SEG = (k) => ({ x: 866 + (k - 1) * 48, y: 342 });

  // ------------------------------------------------------------------ shared CSS (injected once)
  const CSS = `
  .k-ab{position:absolute;left:0;top:0}
  .k-glass{position:absolute;left:0;top:0;border-radius:28px;background:rgba(12,22,64,.84);box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.10),0 22px 46px rgba(2,6,26,.5)}
  .k-white{position:absolute;left:0;top:0;border-radius:28px;background:linear-gradient(180deg,#ffffff,#f4f7fc);box-shadow:0 26px 56px rgba(2,6,26,.55)}
  .k-lab{position:absolute;font:700 19px/26px Poppins;letter-spacing:2.5px;color:#6adfff;white-space:nowrap}
  .k-hplate{position:absolute;left:60px;top:312px;width:960px;height:140px;border-radius:30px;background:rgba(12,22,64,.84);
    box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.10),0 18px 40px rgba(3,6,24,.35);transform-origin:50% 50%}
  .k-hglow{position:absolute;left:60px;top:312px;width:960px;height:140px;border-radius:30px;box-shadow:inset 0 0 0 2px rgba(106,223,255,.9),0 0 34px rgba(1,204,247,.35);opacity:0}
  .k-hnum{position:absolute;left:78px;top:326px;width:112px;height:112px;border-radius:24px;overflow:hidden;
    background:linear-gradient(160deg,#9cecff 0%,#01ccf7 52%,#0aa7d6 100%);box-shadow:0 0 26px rgba(1,204,247,.45),inset 0 1px 0 rgba(255,255,255,.5)}
  .k-hroll{position:absolute;left:0;top:0;width:112px}
  .k-hroll b{display:block;position:relative;height:112px;text-align:center;font:700 54px/112px Poppins;color:#0b1440;letter-spacing:-1px}
  .k-hroll b svg{position:absolute;left:30px;top:30px;width:52px;height:52px;color:#0b1440}
  .k-hbox{position:absolute;overflow:hidden}
  .k-hname{position:absolute;left:0;top:0;white-space:nowrap;font:700 46px/66px Poppins;color:#fff;letter-spacing:-.5px}
  .k-hsub{position:absolute;left:0;top:0;white-space:nowrap;font:400 22px/40px Poppins;color:#9fdcf2}
  .k-hsub i{font-style:normal;color:#86a9c9}
  .k-hseg{position:absolute;top:342px;width:40px;height:8px;border-radius:4px;background:rgba(255,255,255,.16);overflow:hidden}
  .k-hseg b{position:absolute;left:0;top:0;width:40px;height:8px;background:#01ccf7;border-radius:4px;transform-origin:0 50%;box-shadow:0 0 10px rgba(1,204,247,.8)}
  .k-hchip{position:absolute;right:0;top:0;height:40px;padding:0 16px 0 12px;border-radius:20px;display:flex;align-items:center;gap:8px;
    font:700 18px/1 Poppins;letter-spacing:1.5px;color:#6adfff;background:rgba(1,204,247,.10);box-shadow:inset 0 0 0 1.5px rgba(1,204,247,.5);white-space:nowrap}
  .k-hchip svg{width:20px;height:20px}
  .k-shelf{position:absolute;left:0;top:0;width:960px;height:132px;border-radius:26px;background:rgba(12,22,64,.80);
    box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.10),0 16px 34px rgba(3,6,24,.4)}
  .k-shelf .no{position:absolute;left:20px;top:22px;width:48px;height:48px;border-radius:14px;background:linear-gradient(160deg,#9cecff,#01ccf7 55%,#0aa7d6);color:#0b1440;
    box-shadow:0 0 18px rgba(1,204,247,.4)}
  .k-shelf .no svg{position:absolute;left:11px;top:11px;width:26px;height:26px}
  .k-shelf .nm{position:absolute;left:80px;top:34px;font:700 15px/22px Poppins;letter-spacing:2px;color:#6adfff;white-space:nowrap}
  .k-shelf .ct{position:absolute;left:20px;top:76px;font:700 31px/40px Poppins;color:#fff;white-space:nowrap;letter-spacing:-.3px}
  .k-chip{position:absolute;left:0;top:0;height:100px;border-radius:20px;background:#ffffff;box-shadow:0 12px 26px rgba(3,6,24,.42)}
  .k-chip .ib{position:absolute;left:12px;top:12px;width:40px;height:40px;border-radius:12px;background:#e6f8fe;color:#0a7ea4}
  .k-chip .ib svg{position:absolute;left:9px;top:9px;width:22px;height:22px}
  .k-chip .c{position:absolute;left:60px;top:14px;font:700 22px/36px Poppins;color:#0a0d2c;white-space:nowrap}
  .k-chip .l{position:absolute;left:14px;top:62px;font:400 16px/24px Poppins;color:#5d6f8f;white-space:nowrap}
  .k-chip .f{position:absolute;inset:0;border-radius:20px;box-shadow:inset 0 0 0 3px #01ccf7,0 0 24px rgba(1,204,247,.6);opacity:0}
  .k-stamp{position:absolute;left:0;top:0;height:50px;padding:0 20px 0 14px;border-radius:14px;display:flex;align-items:center;gap:8px;font:700 24px/1 Poppins;letter-spacing:2px;
    white-space:nowrap;color:#fff;transform-origin:50% 50%}
  .k-stamp svg{width:26px;height:26px}
  .k-ok{background:#2da44e;box-shadow:0 10px 24px rgba(20,90,40,.45)}
  .k-no{background:#e5484d;box-shadow:0 10px 24px rgba(120,10,20,.45)}
  .k-demo{position:absolute;height:30px;padding:0 12px;border-radius:15px;font:700 15px/30px Poppins;letter-spacing:1.5px;color:#b8c7dd;
    background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 1.2px rgba(255,255,255,.22);white-space:nowrap}
  `;
  if (!document.getElementById("r13kit-css")) {
    const st = document.createElement("style"); st.id = "r13kit-css"; st.textContent = CSS; document.head.appendChild(st);
  }

  // ------------------------------------------------------------------ timeline boilerplate
  K.scene = (id, D) => {
    const tl = gsap.timeline({ paused: true });
    const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
    // positions are clamped to >= 0 (a child placed before 0 would render BEFORE the frame-0 pins and be overridden by them)
    const cl = (p) => (typeof p === "number" ? Math.max(0, p) : p);
    { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); tl.set = (a, v, p) => s0(a, _sc(v), cl(p)); tl.fromTo = (a, x, y, p) => f0(a, _sc(x), _sc(y), cl(p)); tl.to = (a, v, p) => t0(a, _sc(v), cl(p)); }
    const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), typeof t === "number" ? Math.max(0.005, t) : t);
    const I = (el, v) => { gsap.set(el, _sc(v)); tl.set(el, v, 0); };
    const SC = (window.VO_SCENES || []).find((s) => s.id === id) || { start: 0 };
    const T0 = SC.start;
    // scene-local time of a spoken word (first match at/after `after`, global seconds)
    const wt = (txt, after = 0) => { const w = (window.VO_WORDS || []).find((x) => x[0] === txt && x[1] >= after - 1e-6); if (!w) throw new Error(id + ": word not found " + txt); return w[1] - T0; };
    const $ = (x) => document.getElementById(x);
    const finish = () => {
      tl.set({}, {}, D - 0.01);
      (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
      window.__timelines = window.__timelines || {};
      window.__timelines[id] = tl;
    };
    // per-letter typing: letter spans whose opacity is set at times (no onUpdate). Words are wrapped in nowrap spans separated by real
    // spaces, so a long line still wraps at word boundaries (layout is fixed from frame 0: hidden letters keep their space).
    const esc = (c) => c.replace(/&/g, "&amp;").replace(/</g, "&lt;");
    const type = (el, text, t0, cps, cls = "") => {
      el.innerHTML = text.split(" ").map((w) => `<span style="white-space:nowrap">${Array.from(w).map((c) => `<span class="${cls}">${esc(c)}</span>`).join("")}</span>`).join(" ");
      const sp = el.querySelectorAll("span > span"); let k = 0, ci = 0;
      Array.from(text).forEach((c) => { if (c === " ") { ci++; return; } const s = sp[k++]; I(s, { opacity: 0 }); tl.set(s, { opacity: 1 }, t0 + ci / cps); ci++; });
      return t0 + text.length / cps;
    };
    const popIn = (el, t, from = 0.4, dur = 0.3) => { I(el, { scale: from, opacity: 0, transformOrigin: "50% 50%" }); ft(el, { scale: from, opacity: 0 }, { scale: 1, opacity: 1, duration: dur, ease: "back.out(2.4)" }, t); };
    // workspace exit in the scene's last 0.22 s: the wrapper drops + fades (the next scene starts from the header alone)
    const exitWs = (ws, dy = 60) => { I(ws, { y: 0, opacity: 1 }); ft(ws, { y: 0, opacity: 1 }, { y: dy, opacity: 0, duration: 0.18, ease: "power2.in" }, D - 0.22); };
    return { tl, ft, I, wt, $, finish, type, popIn, exitWs, T0, D };
  };

  // ------------------------------------------------------------------ LAYER HEADER
  K.headerHTML = (P) => {
    let h = `<div class="k-hplate" id="${P}-hplate"></div><div class="k-hglow" id="${P}-hglow"></div>`;
    h += `<div class="k-hnum" id="${P}-hnum"><div class="k-hroll" id="${P}-hroll">` +
      K.HD.map((d) => `<b>${/^\d/.test(d.tile) ? d.tile : K.svg(d.tile)}</b>`).join("") + `</div></div>`;
    h += `<div class="k-hbox" id="${P}-hnb" style="left:214px;top:328px;width:640px;height:66px">` + K.HD.map((d, k) => `<div class="k-hname" id="${P}-hn${k}">${d.name}</div>`).join("") + `</div>`;
    h += `<div class="k-hbox" id="${P}-hsb" style="left:214px;top:396px;width:520px;height:40px">` + K.HD.map((d, k) => `<div class="k-hsub" id="${P}-hs${k}">${d.sub}</div>`).join("") + `</div>`;
    h += `<div class="k-hbox" id="${P}-hlb" style="left:744px;top:384px;width:258px;height:40px">` + K.HD.map((d, k) => `<div class="k-hchip" id="${P}-hl${k}">${K.svg(d.chipIc)}${d.chip}</div>`).join("") + `</div>`;
    h += [1, 2, 3].map((k) => `<div class="k-hseg" id="${P}-ht${k}" style="left:${K.SEG(k).x}px"><b id="${P}-hg${k}"></b></div>`).join("");
    return `<div class="k-ab" id="${P}-hdr" style="width:1080px;height:1920px">${h}</div>`;
  };
  // state at frame 0: item k shown
  K.headerSet = (S, P, k) => {
    const { I, $ } = S;
    I($(`${P}-hroll`), { y: -k * 112 });
    for (let j = 0; j < K.HD.length; j++) {
      I($(`${P}-hn${j}`), { y: j === k ? 0 : 66, opacity: j === k ? 1 : 0 });
      I($(`${P}-hs${j}`), { y: j === k ? 0 : 40, opacity: j === k ? 1 : 0 });
      I($(`${P}-hl${j}`), { y: j === k ? 0 : 40, opacity: j === k ? 1 : 0 });
    }
    for (let j = 1; j <= 3; j++) I($(`${P}-hg${j}`), { scaleX: j <= K.HSEG[k] ? 1 : 0 });
    I($(`${P}-hglow`), { opacity: 0 });
  };
  // animated switch a → b starting at local time t
  K.headerSwap = (S, P, a, b, t) => {
    const { ft, $ } = S;
    ft($(`${P}-hroll`), { y: -a * 112 }, { y: -b * 112, duration: 0.5, ease: "power3.inOut" }, t);
    const out = (el, d) => ft(el, { y: 0, opacity: 1 }, { y: -d, opacity: 0, duration: 0.26, ease: "power2.in" }, t);
    const inn = (el, d, dt) => ft(el, { y: d, opacity: 0 }, { y: 0, opacity: 1, duration: 0.42, ease: "power3.out" }, t + dt);
    out($(`${P}-hn${a}`), 66); inn($(`${P}-hn${b}`), 66, 0.16);
    out($(`${P}-hs${a}`), 40); inn($(`${P}-hs${b}`), 40, 0.24);
    if (K.HD[a].chip !== K.HD[b].chip) { out($(`${P}-hl${a}`), 40); inn($(`${P}-hl${b}`), 40, 0.3); }
    else { S.tl.set($(`${P}-hl${a}`), { opacity: 0 }, t + 0.3); S.tl.set($(`${P}-hl${b}`), { y: 0, opacity: 1 }, t + 0.3); }
    const A = K.HSEG[a], B = K.HSEG[b];
    for (let j = A + 1; j <= B; j++) ft($(`${P}-hg${j}`), { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: "power2.out" }, t + 0.22 + (j - A - 1) * 0.05);
    ft($(`${P}-hglow`), { opacity: 0 }, { opacity: 1, duration: 0.14, ease: "power2.out" }, t + 0.05);
    ft($(`${P}-hglow`), { opacity: 1 }, { opacity: 0, duration: 0.5, ease: "power2.inOut" }, t + 0.19);
  };

  // ------------------------------------------------------------------ SHELVES + SKILL CHIPS
  K.shelfHTML = (P, L) => {
    const ly = K.LAYERS[L], cnt = K.SK.filter((s) => s.L === L).length;
    return `<div class="k-shelf" id="${P}-sh${L}"><div class="no">${K.svg(ly.ic)}</div><div class="nm">LAPIS ${L + 1}</div><div class="ct">${ly.n}</div></div>`;
  };
  K.chipHTML = (P, i) => {
    const s = K.SK[i], w = s.L === 1 ? 241 : 176;
    return `<div class="k-chip" id="${P}-ch${i}" style="width:${w}px"><div class="ib">${K.svg(s.ic)}</div><div class="c">${s.n}</div><div class="l">${s.l}</div><i class="f" id="${P}-cf${i}"></i></div>`;
  };
})();

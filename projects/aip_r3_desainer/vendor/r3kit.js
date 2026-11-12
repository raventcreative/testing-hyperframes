// R3 DESAINER — shared scene kit (loaded in index.html <head> after vo_words.js; every scene uses window.R3K).
// Components (identical in every scene that shows them): the TOOL HEADER (number roll 01–05, name, repo, licence chip, 5 progress
// segments), the 5 TOOL TILES row (s01 → t1), the GENERIC "AI-looking" page and the TASTEFUL page ("Kedai Sangrai", fictional),
// the photo illustration, lucide icons (ISC), the Claude mark, and the timeline boilerplate (scale patch, ft, I, wt, seek patch).
// Deterministic: no Math.random, no Date, no rAF.
(function () {
  const K = (window.R3K = {});
  // ------------------------------------------------------------------ icons (lucide-static 1.70, ISC)
  K.IC = {
    palette: '<path d="M12 22a1 1 0 0 1 0-20 10 9 0 0 1 10 9 5 5 0 0 1-5 5h-2.25a1.75 1.75 0 0 0-1.4 2.8l.3.4a1.75 1.75 0 0 1-1.4 2.8z"/><circle cx="13.5" cy="6.5" r=".5" fill="currentColor"/><circle cx="17.5" cy="10.5" r=".5" fill="currentColor"/><circle cx="6.5" cy="12.5" r=".5" fill="currentColor"/><circle cx="8.5" cy="7.5" r=".5" fill="currentColor"/>',
    wand: '<path d="m21.64 3.64-1.28-1.28a1.21 1.21 0 0 0-1.72 0L2.36 18.64a1.21 1.21 0 0 0 0 1.72l1.28 1.28a1.2 1.2 0 0 0 1.72 0L21.64 5.36a1.2 1.2 0 0 0 0-1.72"/><path d="m14 7 3 3"/><path d="M5 6v4"/><path d="M19 14v4"/><path d="M10 2v2"/><path d="M7 8H3"/><path d="M21 16h-4"/><path d="M11 3H9"/>',
    pen: '<path d="m18 13-.654-4.736a4 4 0 00-2.756-3.266l-9.163-2.9a2 2 0 00-2.017.493l-.82.819a2 2 0 00-.492 2.017l2.9 9.163a4 4 0 003.266 2.756L13 18"/><path d="M18.648 12.352a1.205 1.205 0 011.704 0l1.296 1.296a1.205 1.205 0 010 1.704l-6.296 6.296a1.205 1.205 0 01-1.704 0l-1.296-1.296a1.205 1.205 0 010-1.704z"/><path d="m3 3 6.586 6.586"/><circle cx="11" cy="11" r="2"/>',
    camera: '<path d="M13.997 4a2 2 0 0 1 1.76 1.05l.486.9A2 2 0 0 0 18.003 7H20a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2h1.997a2 2 0 0 0 1.759-1.048l.489-.904A2 2 0 0 1 10.004 4z"/><circle cx="12" cy="13" r="3"/>',
    file: '<path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/><path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    box: '<path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
    terminal: '<path d="M12 19h8"/><path d="m4 17 6-6-6-6"/>',
    pointer: '<path d="M4.037 4.688a.495.495 0 0 1 .651-.651l16 6.5a.5.5 0 0 1-.063.947l-6.124 1.58a2 2 0 0 0-1.438 1.435l-1.579 6.126a.5.5 0 0 1-.947.063z"/>',
    check: '<path d="M20 6 9 17l-5-5"/>',
    x: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    code: '<path d="m18 16 4-4-4-4"/><path d="m6 8-4 4 4 4"/><path d="m14.5 4-5 16"/>',
    rotate: '<path d="m15.194 13.707 3.814 1.86-1.86 3.814"/><path d="M16.47214 7.52786 A 5 10 0 1 0 13 21.79796"/><path d="M21.79796 11 A 10 5 0 1 0 19 15.57071"/>',
    image: '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>',
    phone: '<rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/>',
    laptop: '<path d="M18 5a2 2 0 0 1 2 2v8.526a2 2 0 0 0 .212.897l1.068 2.127a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45l1.068-2.127A2 2 0 0 0 4 15.526V7a2 2 0 0 1 2-2z"/><path d="M20.054 15.987H3.946"/>',
    tablet: '<rect width="16" height="20" x="4" y="2" rx="2" ry="2"/><line x1="12" x2="12.01" y1="18" y2="18"/>',
    sparkles: '<path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/>',
    type: '<path d="M12 4v16"/><path d="M4 7V5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2"/><path d="M9 20h6"/>',
    grid: '<rect width="7" height="7" x="3" y="3" rx="1"/><rect width="7" height="7" x="14" y="3" rx="1"/><rect width="7" height="7" x="14" y="14" rx="1"/><rect width="7" height="7" x="3" y="14" rx="1"/>',
    folder: '<path d="m6 14 1.5-2.9A2 2 0 0 1 9.24 10H20a2 2 0 0 1 1.94 2.5l-1.54 6a2 2 0 0 1-1.95 1.5H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h3.9a2 2 0 0 1 1.69.9l.81 1.2a2 2 0 0 0 1.67.9H18a2 2 0 0 1 2 2v2"/>',
    heart: '<path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5"/>',
    send: '<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/>',
    user: '<circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/>',
    link: '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
    unlock: '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/>',
    alert: '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    ccheck: '<circle cx="12" cy="12" r="10"/><path d="m16 9-5.5 5.5L8 12"/>',
    lock: '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    zap: '<path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/>',
    shield: '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>',
  };
  K.svg = (n, cls = "", extra = "") =>
    `<svg class="${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ${extra}>${K.IC[n]}</svg>`;
  K.CLAUDE_D = "M4.709 15.955l4.72-2.647.08-.23-.08-.128H9.2l-.79-.048-2.698-.073-2.339-.097-2.266-.122-.571-.121L0 11.784l.055-.352.48-.321.686.06 1.52.103 2.278.158 1.652.097 2.449.255h.389l.055-.157-.134-.098-.103-.097-2.358-1.596-2.552-1.688-1.336-.972-.724-.491-.364-.462-.158-1.008.656-.722.881.06.225.061.893.686 1.908 1.476 2.491 1.833.365.304.145-.103.019-.073-.164-.274-1.355-2.446-1.446-2.49-.644-1.032-.17-.619a2.97 2.97 0 01-.104-.729L6.283.134 6.696 0l.996.134.42.364.62 1.414 1.002 2.229 1.555 3.03.456.898.243.832.091.255h.158V9.01l.128-1.706.237-2.095.23-2.695.08-.76.376-.91.747-.492.584.28.48.685-.067.444-.286 1.851-.559 2.903-.364 1.942h.212l.243-.242.985-1.306 1.652-2.064.73-.82.85-.904.547-.431h1.033l.76 1.129-.34 1.166-1.064 1.347-.881 1.142-1.264 1.7-.79 1.36.073.11.188-.02 2.856-.606 1.543-.28 1.841-.315.833.388.091.395-.328.807-1.969.486-2.309.462-3.439.813-.042.03.049.061 1.549.146.662.036h1.622l3.02.225.79.522.474.638-.079.485-1.215.62-1.64-.389-3.829-.91-1.312-.329h-.182v.11l1.093 1.068 2.006 1.81 2.509 2.33.127.578-.322.455-.34-.049-2.205-1.657-.851-.747-1.926-1.62h-.128v.17l.444.649 2.345 3.521.122 1.08-.17.353-.608.213-.668-.122-1.374-1.925-1.415-2.167-1.143-1.943-.14.08-.674 7.254-.316.37-.729.28-.607-.461-.322-.747.322-1.476.389-1.924.315-1.53.286-1.9.17-.632-.012-.042-.14.018-1.434 1.967-2.18 2.945-1.726 1.845-.414.164-.717-.37.067-.662.401-.589 2.388-3.036 1.44-1.882.93-1.086-.006-.158h-.055L4.132 18.56l-1.13.146-.487-.456.061-.746.231-.243 1.908-1.312-.006.006z";
  K.claude = (cls = "") => `<svg class="${cls}" viewBox="0 0 24 24"><path d="${K.CLAUDE_D}" fill="#D97757"/></svg>`;

  // ------------------------------------------------------------------ the five tools (verified 12 Nov 2026, official READMEs)
  K.TOOLS = [null,
    { n: "01", name: "Taste Skill", short: "Taste", repo: "Leonxlnx/taste-skill", lic: "MIT", ic: "palette" },
    { n: "02", name: "Impeccable", short: "Impeccable", repo: "pbakaus/impeccable", lic: "Apache-2.0", ic: "wand" },
    { n: "03", name: "Playwright CLI", short: "Playwright", repo: "microsoft/playwright-cli", lic: "Apache-2.0", ic: "camera" },
    { n: "04", name: "Awesome DESIGN.md", short: "DESIGN.md", repo: "VoltAgent/awesome-design-md", lic: "MIT", ic: "file" },
    { n: "05", name: "img2threejs", short: "img2threejs", repo: "img2threejs/img2threejs", lic: "Apache-2.0", ic: "box" }];

  // ------------------------------------------------------------------ geometry (global px; shared by every scene)
  K.HDR = { x: 60, y: 312, w: 960, h: 140, num: { x: 78, y: 326, s: 112 } };
  K.SEG = (k) => ({ x: 822 + (k - 1) * 35, y: 342, w: 28, h: 8 });
  K.TILE = { w: 172, h: 128, y: 790, xs: [0, 66, 256, 446, 636, 826] };
  K.PAGE = { w: 880, h: 520 };

  // ------------------------------------------------------------------ shared CSS (injected once)
  const CSS = `
  .k-ab{position:absolute;left:0;top:0}
  .k-hplate{position:absolute;left:60px;top:312px;width:960px;height:140px;border-radius:30px;background:rgba(12,22,64,.82);
    box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.10),0 18px 40px rgba(3,6,24,.35);transform-origin:0 50%}
  .k-hglow{position:absolute;left:60px;top:312px;width:960px;height:140px;border-radius:30px;box-shadow:inset 0 0 0 2px rgba(106,223,255,.9),0 0 34px rgba(1,204,247,.35);opacity:0}
  .k-hnum{position:absolute;left:78px;top:326px;width:112px;height:112px;border-radius:24px;overflow:hidden;
    background:linear-gradient(160deg,#9cecff 0%,#01ccf7 52%,#0aa7d6 100%);box-shadow:0 0 26px rgba(1,204,247,.45),inset 0 1px 0 rgba(255,255,255,.5)}
  .k-hroll{position:absolute;left:0;top:0;width:112px}
  .k-hroll b{display:block;height:112px;text-align:center;font:700 54px/112px Poppins;color:#0b1440;letter-spacing:-1px}
  .k-hbox{position:absolute;overflow:hidden}
  .k-hname{position:absolute;left:0;top:0;white-space:nowrap;font:700 48px/66px Poppins;color:#fff;letter-spacing:-.5px}
  .k-hsub{position:absolute;left:0;top:0;white-space:nowrap;font:400 22px/40px Poppins;color:#9fdcf2}
  .k-hsub i{font-style:normal;color:#5d86a8}
  .k-hseg{position:absolute;top:342px;width:28px;height:8px;border-radius:4px;background:rgba(255,255,255,.16);overflow:hidden}
  .k-hseg b{position:absolute;left:0;top:0;width:28px;height:8px;background:#01ccf7;border-radius:4px;transform-origin:0 50%;box-shadow:0 0 10px rgba(1,204,247,.8)}
  .k-hlic{position:absolute;right:0;top:0;height:40px;padding:0 16px 0 12px;border-radius:20px;display:flex;align-items:center;gap:8px;
    font:700 20px/1 Poppins;color:#6adfff;background:rgba(1,204,247,.10);box-shadow:inset 0 0 0 1.5px rgba(1,204,247,.5);white-space:nowrap}
  .k-hlic svg{width:20px;height:20px}
  .k-tile{position:absolute;left:0;top:0;width:172px;height:128px;border-radius:24px;background:rgba(12,22,64,.88);
    box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.12),0 14px 30px rgba(3,6,24,.4)}
  .k-tile .n{position:absolute;left:16px;top:14px;font:700 26px/1 Poppins;color:#01ccf7}
  .k-tile svg{position:absolute;right:16px;top:14px;width:32px;height:32px;color:#e3edfa}
  .k-tile .t{position:absolute;left:16px;right:8px;bottom:18px;font:700 22px/1.1 Poppins;color:#fff;white-space:nowrap}
  .k-tile .f{position:absolute;inset:0;border-radius:24px;background:linear-gradient(160deg,#9cecff 0%,#01ccf7 52%,#0aa7d6 100%);opacity:0}
  /* ---------------- mock pages (UI illustrations; 880x520 native) */
  .k-page{position:absolute;left:0;top:0;width:880px;height:520px;border-radius:22px;overflow:hidden;background:#fff;transform-origin:50% 50%;
    box-shadow:0 30px 70px rgba(2,6,26,.55),0 0 0 1.5px rgba(255,255,255,.18)}
  .k-chrome{position:absolute;left:0;top:0;width:880px;height:40px;background:#eceff5}
  .k-chrome i{position:absolute;top:15px;width:11px;height:11px;border-radius:50%}
  .k-url{position:absolute;left:290px;top:8px;width:300px;height:24px;border-radius:12px;background:#fff;font:400 14px/24px Poppins;color:#7b849a;text-align:center}
  .k-gen .nav{position:absolute;left:0;top:40px;width:880px;height:56px;background:#fff}
  .k-gen .logo{position:absolute;left:32px;top:56px;width:24px;height:24px;border-radius:7px;transform:rotate(45deg);background:linear-gradient(135deg,#a855f7,#3b82f6)}
  .k-gen .lname{position:absolute;left:68px;top:52px;font:700 22px/32px Poppins;color:#1f2340}
  .k-gen .lk{position:absolute;top:63px;height:10px;border-radius:5px;background:#d6d9e6}
  .k-gen .cta{position:absolute;left:716px;top:50px;width:136px;height:36px;border-radius:18px;background:linear-gradient(90deg,#8b5cf6,#3b82f6);font:700 15px/36px Poppins;color:#fff;text-align:center}
  .k-gen .hero{position:absolute;left:0;top:96px;width:880px;height:208px;background:linear-gradient(120deg,#8b5cf6 0%,#6366f1 45%,#3b82f6 100%)}
  .k-gen .h1{position:absolute;left:0;top:124px;width:880px;text-align:center;font:700 38px/48px Poppins;color:#fff}
  .k-gen .h1 svg{width:30px;height:30px;vertical-align:-3px;margin-left:8px}
  .k-gen .h2{position:absolute;left:0;top:178px;width:880px;text-align:center;font:400 17px/26px Poppins;color:rgba(255,255,255,.86)}
  .k-gen .b1,.k-gen .b2{position:absolute;top:226px;height:42px;border-radius:21px;font:700 16px/42px Poppins;text-align:center}
  .k-gen .b1{left:256px;width:176px;background:#fff;color:#6d28d9}
  .k-gen .b2{left:448px;width:204px;box-shadow:inset 0 0 0 2px rgba(255,255,255,.85);color:#fff}
  .k-gen .outer{position:absolute;left:24px;top:322px;width:832px;height:180px;border-radius:20px;background:#f3f4fa;box-shadow:inset 0 0 0 1px #e3e6f0}
  .k-gen .card{position:absolute;top:338px;width:248px;height:148px;border-radius:16px;background:#fff;box-shadow:0 8px 20px rgba(60,64,110,.12)}
  .k-gen .tile{position:absolute;left:18px;top:16px;width:46px;height:46px;border-radius:13px;background:linear-gradient(135deg,#a855f7,#3b82f6);color:#fff}
  .k-gen .tile svg{position:absolute;left:12px;top:12px;width:22px;height:22px}
  .k-gen .ct{position:absolute;left:18px;top:74px;font:700 20px/26px Poppins;color:#1f2340}
  .k-gen .cl{position:absolute;left:18px;height:9px;border-radius:5px;background:#dfe2ee}
  /* tasteful page "Kedai Sangrai" (fictional) */
  .k-tas{background:#f3efe7}
  .k-tas .wm{position:absolute;left:44px;top:56px;font:700 20px/26px Poppins;color:#1d1a16;letter-spacing:-.3px}
  .k-tas .nl{position:absolute;top:58px;font:400 16px/22px Poppins;color:#1d1a16}
  .k-tas .rule{position:absolute;left:44px;top:96px;width:792px;height:1.5px;background:rgba(29,26,22,.16)}
  .k-tas .eb{position:absolute;font:700 13px/18px Poppins;letter-spacing:3px;color:#b4532a;white-space:nowrap}
  .k-tas .hl{position:absolute;font:700 52px/52px Poppins;letter-spacing:-2px;color:#1d1a16;white-space:nowrap;transform-origin:0 0}
  .k-tas .bd{position:absolute;font:400 17px/25px Poppins;color:#4a4239}
  .k-tas .btn{position:absolute;height:44px;padding:0 20px;border-radius:6px;background:#1d1a16;font:700 16px/44px Poppins;color:#f3efe7;white-space:nowrap}
  .k-tas .tl{position:absolute;font:400 16px/44px Poppins;color:#1d1a16;text-decoration:underline;text-underline-offset:4px}
  .k-tas .col{position:absolute;top:424px;height:76px;border-left:1.5px solid rgba(29,26,22,.16);padding-left:16px}
  .k-tas .col b{display:block;font:700 18px/26px Poppins;color:#1d1a16}
  .k-tas .col span{display:block;font:400 15px/22px Poppins;color:#6b6157}
  .k-photo{position:absolute;overflow:hidden;border-radius:8px;background:radial-gradient(120% 90% at 30% 20%,#6b4a32 0%,#3b271a 55%,#22160e 100%)}
  .k-photo .gr{position:absolute;inset:0;background:url(assets/brand/grain_256.png);opacity:.22;mix-blend-mode:overlay}
  .k-photo .sau{position:absolute;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fbf8f2 0%,#e9e2d6 60%,#cfc5b6 100%);box-shadow:0 18px 30px rgba(0,0,0,.45)}
  .k-photo .cup{position:absolute;border-radius:50%;background:radial-gradient(circle at 42% 38%,#fffdf8 0%,#f1ebe1 70%,#d8cfc1 100%)}
  .k-photo .cof{position:absolute;border-radius:50%;background:radial-gradient(circle at 50% 50%,#d9a46e 0%,#b0703f 45%,#6e3d1d 85%,#4a2610 100%)}
  .k-photo .art{position:absolute;border-radius:50%;background:radial-gradient(circle at 50% 55%,#f6e7cf 0%,#ead2ad 55%,rgba(234,210,173,0) 72%)}
  .k-photo .hdl{position:absolute;border-radius:10px;background:linear-gradient(90deg,#e7e0d4,#cfc6b8)}
  .k-photo .bean{position:absolute;width:22px;height:15px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#7a4a2a,#3a1f0f);box-shadow:0 3px 5px rgba(0,0,0,.4)}
  .k-photo .bean:after{content:"";position:absolute;left:4px;right:4px;top:7px;height:1.5px;background:rgba(20,10,4,.75);border-radius:1px}
  /* ---------------- hook (s01 end state, rebuilt by t1) */
    .k-hk-wrap { position: absolute; left: 0; top: 0; width: 880px; height: 520px; transform-origin: 50% 50%; }
    .k-hk-ol { position: absolute; border-radius: 14px; box-shadow: 0 0 0 3px #e5484d, 0 0 18px rgba(229,72,77,.55); }
    .k-hk-tag { position: absolute; height: 40px; padding: 0 16px 0 12px; border-radius: 20px; background: #e5484d; color: #fff; font: 700 22px/40px Poppins;
      white-space: nowrap; display: flex; align-items: center; gap: 8px; box-shadow: 0 10px 24px rgba(120,10,20,.4); }
    .k-hk-tag svg { width: 22px; height: 22px; }
    .k-hk-stamp { position: absolute; left: 0; top: 0; padding: 4px 28px 8px; border-radius: 18px; font: 700 84px/1 Poppins; letter-spacing: 2px; color: #e5484d;
      background: rgba(255,255,255,.93); box-shadow: inset 0 0 0 7px #e5484d, 0 20px 40px rgba(60,0,10,.35); white-space: nowrap; transform-origin: 50% 50%; }
    .k-hk-disc { position: absolute; left: 458px; top: 448px; width: 164px; height: 164px; border-radius: 50%; background: #fbf4ec; transform-origin: 50% 50%;
      box-shadow: 0 0 0 8px rgba(217,119,87,.22), 0 0 50px rgba(217,119,87,.6), 0 18px 40px rgba(0,0,0,.4); }
    .k-hk-disc svg { position: absolute; left: 30px; top: 30px; width: 104px; height: 104px; }
    .k-hk-rip { position: absolute; left: 458px; top: 448px; width: 164px; height: 164px; border-radius: 50%; box-shadow: 0 0 0 4px rgba(255,190,160,.9); transform-origin: 50% 50%; }
    .k-hk-chip { position: absolute; left: 0; top: 0; height: 56px; padding: 0 24px 0 14px; border-radius: 28px; background: #ffffff; color: #0b1440;
      font: 700 30px/56px Poppins; white-space: nowrap; display: flex; align-items: center; gap: 10px; box-shadow: 0 14px 30px rgba(2,6,26,.45); transform-origin: 50% 50%; }
    .k-hk-chip svg { width: 30px; height: 30px; color: #01a9d6; }
    .k-hk-ib { position: absolute; left: 0; top: 0; width: 60px; height: 60px; margin: -30px 0 0 -30px; border-radius: 18px; background: rgba(12,22,64,.86);
      box-shadow: inset 0 0 0 1.5px rgba(106,223,255,.45), 0 10px 22px rgba(2,6,26,.4); color: #6adfff; transform-origin: 50% 50%; }
    .k-hk-ib svg { position: absolute; left: 15px; top: 15px; width: 30px; height: 30px; }
    .k-hk-pill { position: absolute; left: 0; top: 0; height: 44px; padding: 0 22px; border-radius: 22px; background: #01ccf7; color: #0b1440;
      font: 700 22px/44px Poppins; letter-spacing: 2px; white-space: nowrap; box-shadow: 0 0 24px rgba(1,204,247,.5); transform-origin: 50% 50%; }
    .k-hk-pensvg { position: absolute; left: 0; top: 0; width: 1080px; height: 945px; overflow: visible; }
    .k-hk-anc { position: absolute; left: 0; top: 0; width: 16px; height: 16px; margin: -8px 0 0 -8px; background: #fff; box-shadow: 0 0 0 2.5px #01ccf7; }
    .k-hk-knob { position: absolute; left: 0; top: 0; width: 14px; height: 14px; margin: -7px 0 0 -7px; border-radius: 50%; background: #01ccf7; }
  `;
  if (!document.getElementById("r3kit-css")) {
    const st = document.createElement("style"); st.id = "r3kit-css"; st.textContent = CSS; document.head.appendChild(st);
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
    // deterministic PRNG
    let seed = 7; const rnd = () => { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; };
    // per-letter typing: spans with opacity set at times (no onUpdate)
    const type = (el, text, t0, cps, cls = "") => {
      el.innerHTML = Array.from(text).map((c) => `<span class="${cls}">${c === " " ? "&nbsp;" : c.replace(/</g, "&lt;")}</span>`).join("");
      const sp = el.querySelectorAll("span"); sp.forEach((s, i) => { I(s, { opacity: 0 }); tl.set(s, { opacity: 1 }, t0 + i / cps); });
      return t0 + sp.length / cps;
    };
    return { tl, ft, I, wt, $, finish, rnd, type, T0, D };
  };

  // ------------------------------------------------------------------ TOOL HEADER
  K.headerHTML = (P) => {
    let h = `<div class="k-hplate" id="${P}-hplate"></div><div class="k-hglow" id="${P}-hglow"></div>`;
    h += `<div class="k-hnum" id="${P}-hnum"><div class="k-hroll" id="${P}-hroll">` + [1, 2, 3, 4, 5].map((k) => `<b>${K.TOOLS[k].n}</b>`).join("") + `</div></div>`;
    h += `<div class="k-hbox" id="${P}-hnb" style="left:214px;top:328px;width:590px;height:66px">` + [1, 2, 3, 4, 5].map((k) => `<div class="k-hname" id="${P}-hn${k}">${K.TOOLS[k].name}</div>`).join("") + `</div>`;
    h += `<div class="k-hbox" id="${P}-hsb" style="left:214px;top:396px;width:556px;height:40px">` + [1, 2, 3, 4, 5].map((k) => `<div class="k-hsub" id="${P}-hs${k}"><i>github.com/</i>${K.TOOLS[k].repo}</div>`).join("") + `</div>`;
    h += `<div class="k-hbox" id="${P}-hlb" style="left:770px;top:384px;width:228px;height:40px">` + [1, 2, 3, 4, 5].map((k) => `<div class="k-hlic" id="${P}-hl${k}">${K.svg("unlock")}${K.TOOLS[k].lic}</div>`).join("") + `</div>`;
    h += [1, 2, 3, 4, 5].map((k) => `<div class="k-hseg" id="${P}-ht${k}" style="left:${K.SEG(k).x}px"><b id="${P}-hg${k}"></b></div>`).join("");
    return `<div class="k-ab" id="${P}-hdr" style="width:1080px;height:1920px">${h}</div>`;
  };
  // state at frame 0: tool k shown (k = 0: nothing lit, names hidden)
  K.headerSet = (S, P, k) => {
    const { I, $ } = S;
    I($(`${P}-hroll`), { y: -(Math.max(1, k) - 1) * 112 });
    for (let j = 1; j <= 5; j++) {
      I($(`${P}-hn${j}`), { y: j === k ? 0 : 66, opacity: j === k ? 1 : 0 });
      I($(`${P}-hs${j}`), { y: j === k ? 0 : 40, opacity: j === k ? 1 : 0 });
      I($(`${P}-hl${j}`), { y: j === k ? 0 : 40, opacity: j === k ? 1 : 0 });
      I($(`${P}-hg${j}`), { scaleX: j <= k ? 1 : 0 });
    }
    I($(`${P}-hglow`), { opacity: 0 });
  };
  // animated switch a → b starting at local time t
  K.headerSwap = (S, P, a, b, t) => {
    const { ft, $ } = S;
    ft($(`${P}-hroll`), { y: -(a - 1) * 112 }, { y: -(b - 1) * 112, duration: 0.5, ease: "power3.inOut" }, t);
    const out = (el, d) => ft(el, { y: 0, opacity: 1 }, { y: -d, opacity: 0, duration: 0.26, ease: "power2.in" }, t);
    const inn = (el, d, dt) => ft(el, { y: d, opacity: 0 }, { y: 0, opacity: 1, duration: 0.42, ease: "power3.out" }, t + dt);
    out($(`${P}-hn${a}`), 66); inn($(`${P}-hn${b}`), 66, 0.16);
    out($(`${P}-hs${a}`), 40); inn($(`${P}-hs${b}`), 40, 0.24);
    out($(`${P}-hl${a}`), 40); inn($(`${P}-hl${b}`), 40, 0.3);
    ft($(`${P}-hg${b}`), { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: "power2.out" }, t + 0.22);
    ft($(`${P}-hglow`), { opacity: 0 }, { opacity: 1, duration: 0.14, ease: "power2.out" }, t + 0.05);
    ft($(`${P}-hglow`), { opacity: 1 }, { opacity: 0, duration: 0.5, ease: "power2.inOut" }, t + 0.19);
  };

  // ------------------------------------------------------------------ TOOL TILES (s01 → t1)
  K.tilesHTML = (P) => [1, 2, 3, 4, 5].map((k) => `<div class="k-tile" id="${P}-tile${k}"><div class="f" id="${P}-tilef${k}"></div><div class="n">${K.TOOLS[k].n}</div>${K.svg(K.TOOLS[k].ic)}<div class="t">${K.TOOLS[k].short}</div></div>`).join("");

  // ------------------------------------------------------------------ the photo illustration (warm table, latte from above, beans)
  K.photoHTML = (id, w, h, o = {}) => {
    const cx = o.cx != null ? o.cx : w * 0.5, cy = o.cy != null ? o.cy : h * 0.52, r = o.r || Math.min(w, h) * 0.3;
    const beans = (o.beans || [[0.14, 0.2, 20], [0.2, 0.78, -30], [0.86, 0.18, 60], [0.82, 0.84, 10], [0.1, 0.5, 80], [0.9, 0.55, -50]])
      .map(([bx, by, rot]) => `<i class="bean" style="left:${(bx * w - 11).toFixed(0)}px;top:${(by * h - 7).toFixed(0)}px;transform:rotate(${rot}deg)"></i>`).join("");
    const s = (k) => (r * k).toFixed(1);
    const pos = o.left != null ? `left:${o.left}px;top:${o.top}px;` : "";
    return `<div class="k-photo" id="${id}" style="${pos}width:${w}px;height:${h}px">${beans}` +
      `<i class="sau" style="left:${(cx - r * 1.38).toFixed(1)}px;top:${(cy - r * 1.38).toFixed(1)}px;width:${s(2.76)}px;height:${s(2.76)}px"></i>` +
      `<i class="hdl" style="left:${(cx + r * 0.9).toFixed(1)}px;top:${(cy - r * 0.2).toFixed(1)}px;width:${s(0.62)}px;height:${s(0.4)}px"></i>` +
      `<i class="cup" style="left:${(cx - r).toFixed(1)}px;top:${(cy - r).toFixed(1)}px;width:${s(2)}px;height:${s(2)}px"></i>` +
      `<i class="cof" style="left:${(cx - r * 0.8).toFixed(1)}px;top:${(cy - r * 0.8).toFixed(1)}px;width:${s(1.6)}px;height:${s(1.6)}px"></i>` +
      `<i class="art" style="left:${(cx - r * 0.5).toFixed(1)}px;top:${(cy - r * 0.46).toFixed(1)}px;width:${s(1)}px;height:${s(0.92)}px"></i>` +
      `<i class="gr"></i></div>`;
  };

  // ------------------------------------------------------------------ pages
  const chrome = (url) => `<div class="k-chrome"><i style="left:16px;background:#ff6159"></i><i style="left:34px;background:#ffbd2e"></i><i style="left:52px;background:#28c941"></i><div class="k-url">${url}</div></div>`;
  K.pageGenericHTML = (P) => {
    let h = chrome("novaai.app") + `<div class="nav"></div><i class="logo"></i><div class="lname">NovaAI</div>` +
      [[430, 54], [500, 62], [578, 50], [644, 44]].map(([x, w]) => `<i class="lk" style="left:${x}px;width:${w}px"></i>`).join("") +
      `<div class="cta">Mulai Gratis</div><div class="hero" id="${P}-ghero"></div>` +
      `<div class="h1">Revolusi Bisnis Anda dengan AI${K.svg("sparkles")}</div>` +
      `<div class="h2">Solusi inovatif, cepat, dan terpercaya untuk masa depan.</div>` +
      `<div class="b1">Mulai Sekarang</div><div class="b2">Pelajari Lebih Lanjut</div><div class="outer" id="${P}-gouter"></div>`;
    [["zap", "Cepat"], ["shield", "Aman"], ["sparkles", "Pintar"]].forEach(([ic, t], i) => {
      h += `<div class="card" id="${P}-gcard${i}" style="left:${44 + i * 272}px"><div class="tile">${K.svg(ic)}</div><div class="ct">${t}</div>` +
        `<i class="cl" style="top:110px;width:190px"></i><i class="cl" style="top:126px;width:140px"></i></div>`;
    });
    return `<div class="k-page k-gen" id="${P}-gpage">${h}</div>`;
  };
  // tasteful page; hero variant A (split). The hero parts are separate ids so t2 can re-lay them out.
  K.pageTasteHTML = (P) => {
    let h = chrome("kedaisangrai.id") + `<div class="wm">Kedai Sangrai</div>` +
      [["Menu", 658], ["Biji", 726], ["Lokasi", 780]].map(([t, x]) => `<div class="nl" style="left:${x}px">${t}</div>`).join("") + `<i class="rule"></i>`;
    h += `<div class="k-ab" id="${P}-tA" style="width:880px;height:520px">` +
      `<div class="eb" style="left:44px;top:128px">SANGRAI MINGGU INI</div>` +
      `<div class="hl" id="${P}-thl" style="left:42px;top:156px">Disangrai Senin.<br>Habis Jumat.</div>` +
      `<div class="bd" style="left:44px;top:278px;width:360px">Biji Gayo &amp; Toraja, sangrai kecil tiap pekan.</div>` +
      `<div class="btn" id="${P}-tbtn" style="left:44px;top:344px">Lihat menu &rarr;</div><div class="tl" style="left:216px;top:344px">Jam buka</div>` +
      K.photoHTML(`${P}-tph`, 366, 284, { left: 470, top: 118 }) + `</div>`;
    h += [["Gayo", "fruity, floral", 44], ["Toraja", "cokelat, rempah", 318], ["Kintamani", "jeruk, manis", 592]]
      .map(([b, s, x], i) => `<div class="col" id="${P}-tcol${i}" style="left:${x}px;width:244px"><b>${b}</b><span>${s}</span></div>`).join("");
    return `<div class="k-page k-tas" id="${P}-tpage">${h}</div>`;
  };
  // hero variants B (centred + photo strip) and C (full-bleed photo), page coordinates (Impeccable live mode, t2/t3)
  K.heroVariantsHTML = (P) =>
    `<div class="k-ab" id="${P}-tB" style="width:880px;height:520px"><div class="eb" style="left:0;top:118px;width:880px;text-align:center">SANGRAI MINGGU INI</div>` +
        `<div class="hl" style="left:0;top:142px;width:880px;text-align:center;font-size:44px;line-height:48px">Disangrai Senin. Habis Jumat.</div>` +
        `<div class="btn" style="left:362px;top:204px;background:#c2410c">Lihat menu &rarr;</div>` + K.photoHTML(`${P}-phB`, 792, 150, { left: 44, top: 262, cx: 560, cy: 75, r: 52, beans: [[0.1, 0.3, 20], [0.2, 0.7, -30], [0.36, 0.4, 60], [0.88, 0.3, 10], [0.94, 0.72, 80]] }) + `</div>` +
        `<div class="k-ab" id="${P}-tC" style="width:880px;height:520px">` + K.photoHTML(`${P}-phC`, 880, 314, { left: 0, top: 98, cx: 640, cy: 160, r: 92 }) +
        `<i class="k-ab" style="left:0;top:98px;width:880px;height:314px;background:linear-gradient(90deg,rgba(20,12,6,.88) 0%,rgba(20,12,6,.55) 45%,rgba(20,12,6,0) 70%)"></i>` +
        `<div class="eb" style="left:44px;top:150px;color:#f1b68c">SANGRAI MINGGU INI</div>` +
        `<div class="hl" style="left:42px;top:178px;color:#f3efe7;font-size:56px;line-height:56px">Disangrai Senin.<br>Habis Jumat.</div>` +
        `<div class="btn" style="left:44px;top:322px;background:#f3efe7;color:#1d1a16">Lihat menu &rarr;</div></div>`;
  K.HK_IB = [["palette", 292, 470], ["type", 788, 470], ["grid", 292, 596], ["image", 788, 596]];
  K.hookHTML = (P) => {
    let h = `<div class="k-hk-wrap" id="${P}-wrap">${K.pageGenericHTML(P)}` +
      `<i class="k-hk-ol" id="${P}-ol0" style="left:6px;top:100px;width:868px;height:200px"></i>` +
      [0, 1, 2].map((i) => `<i class="k-hk-ol" id="${P}-ol${i + 1}" style="left:${56 + i * 272}px;top:348px;width:58px;height:58px"></i>`).join("") +
      `<i class="k-hk-ol" id="${P}-ol4" style="left:20px;top:318px;width:840px;height:188px"></i>` +
      `<div class="k-hk-tag" id="${P}-tagA" style="left:590px;top:70px">${K.svg("alert")}gradien ungu-biru</div>` +
      `<div class="k-hk-tag" id="${P}-tagB" style="left:30px;top:496px">${K.svg("alert")}ikon kotak kembar</div>` +
      `<div class="k-hk-tag" id="${P}-tagC" style="left:560px;top:496px">${K.svg("alert")}kartu di dalam kartu</div>` +
      `<div class="k-hk-stamp" id="${P}-stamp">GENERIK</div></div>`;
    h += `<svg class="k-hk-pensvg" id="${P}-pen" viewBox="0 0 1080 945"><path id="${P}-loop" d="M408 530 C408 404 672 404 672 530 C672 656 408 656 408 530" fill="none" stroke="#01ccf7" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="1200" stroke-dashoffset="1200"/>` +
      `<line id="${P}-hd1" x1="672" y1="530" x2="672" y2="436" stroke="#6adfff" stroke-width="2.5"/><line id="${P}-hd2" x1="672" y1="530" x2="672" y2="624" stroke="#6adfff" stroke-width="2.5"/></svg>`;
    h += `<i class="k-hk-anc" id="${P}-anc0"></i><i class="k-hk-anc" id="${P}-anc1"></i><i class="k-hk-knob" id="${P}-kn1"></i><i class="k-hk-knob" id="${P}-kn2"></i>`;
    h += `<i class="k-hk-rip" id="${P}-rip"></i><div class="k-hk-disc" id="${P}-disc">${K.claude()}</div>`;
    h += `<div class="k-hk-chip" id="${P}-chip">${K.svg("pen")}desainer</div>`;
    h += K.HK_IB.map(([ic], i) => `<div class="k-hk-ib" id="${P}-ib${i}">${K.svg(ic)}</div>`).join("");
    h += `<div class="k-hk-pill" id="${P}-pill">GRATIS · OPEN SOURCE</div>` + K.tilesHTML(P);
    return h;
  };
  // s01's END STATE, pinned at frame 0 of the next scene (t1)
  K.hookEnd = (S, P) => {
    const { I, $ } = S;
    I($(`${P}-wrap`), Object.assign(K.pageAt(540, 530, 0.72), { rotationX: 0, rotationY: 0, transformPerspective: 1400 }));
    I($(`${P}-gpage`), { opacity: 0.5, x: 0, y: 0 });
    I($(`${P}-gpage`).querySelector(".h1 svg"), { scale: 1, rotation: 90, transformOrigin: "50% 50%" });
    [0, 1, 2, 3, 4].forEach((i) => I($(`${P}-ol${i}`), { opacity: 0 }));
    ["A", "B", "C"].forEach((x) => I($(`${P}-tag${x}`), { opacity: 0 }));
    I($(`${P}-stamp`), { opacity: 0 });
    I($(`${P}-disc`), { scale: 1, rotation: 0, opacity: 1 }); I($(`${P}-disc`).querySelector("svg"), { rotation: 30, transformOrigin: "50% 50%" });
    I($(`${P}-rip`), { opacity: 0 }); I($(`${P}-loop`), { strokeDashoffset: 0 });
    [[0, 408, 530], [1, 672, 530]].forEach(([i, x, y]) => I($(`${P}-anc${i}`), { x, y, scale: 1 }));
    [[1, 672, 436], [2, 672, 624]].forEach(([i, x, y]) => { I($(`${P}-kn${i}`), { x, y, scale: 1 }); I($(`${P}-hd${i}`), { opacity: 1 }); });
    I($(`${P}-chip`), { x: 540, xPercent: -50, y: 642, scale: 1, opacity: 1 });
    K.HK_IB.forEach(([, x, y], i) => I($(`${P}-ib${i}`), { x, y, scale: 1, opacity: 1 }));
    I($(`${P}-pill`), { x: 540, xPercent: -50, y: 732, scale: 1, opacity: 1 });
    for (let k = 1; k <= 5; k++) I($(`${P}-tile${k}`), { x: K.TILE.xs[k], y: K.TILE.y, rotation: 0, opacity: 1, scale: 1, transformOrigin: "50% 50%" });
  };
  // place a page (or any 880x520 box) by its centre and scale
  K.pageAt = (cx, cy, s) => ({ x: cx - 440, y: cy - 260, scale: s, transformOrigin: "50% 50%" });
})();

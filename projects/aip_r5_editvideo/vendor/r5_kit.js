// R5 "Edit video pakai Claude" — shared scene kit (loaded in index.html <head>, before the compositions).
// - IC / svg(): lucide-static icons (ISC, see assets/icons/LICENSE-lucide.txt), inlined, stroke currentColor
// - CLAUDE: the Claude mark (assets/icons/lobe-claude-color.svg)
// - shared CSS (r5-*): the generic Claude desktop window used by st1 · st2 · st4 (identical geometry in every scene → seamless hand-offs)
// - scene(id): timeline boilerplate (scale shorthand patch, ft/I helpers, word-time lookup, seek-order patch, registration)
(function () {
  const IC = {
    "folder": '<path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/>',
    "folder-open": '<path d="m6 14 1.5-2.9A2 2 0 0 1 9.24 10H20a2 2 0 0 1 1.94 2.5l-1.54 6a2 2 0 0 1-1.95 1.5H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h3.9a2 2 0 0 1 1.69.9l.81 1.2a2 2 0 0 0 1.67.9H18a2 2 0 0 1 2 2v2"/>',
    "folder-plus": '<path d="M12 10v6"/><path d="M9 13h6"/><path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/>',
    "download": '<path d="M12 15V3"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/>',
    "scissors": '<circle cx="6" cy="6" r="3"/><path d="M8.12 8.12 12 12"/><path d="M20 4 8.12 15.88"/><circle cx="6" cy="18" r="3"/><path d="M14.8 14.8 20 20"/>',
    "captions": '<rect width="18" height="14" x="3" y="5" rx="2" ry="2"/><path d="M7 15h4M15 15h2M7 11h2M13 11h4"/>',
    "sparkles": '<path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/>',
    "layers": '<path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z"/><path d="M2 12a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 12"/><path d="M2 17a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 17"/>',
    "link": '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "terminal": '<path d="M12 19h8"/><path d="m4 17 6-6-6-6"/>',
    "film": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 3v18"/><path d="M3 7.5h4"/><path d="M3 12h18"/><path d="M3 16.5h4"/><path d="M17 3v18"/><path d="M17 7.5h4"/><path d="M17 16.5h4"/>',
    "palette": '<path d="M12 22a1 1 0 0 1 0-20 10 9 0 0 1 10 9 5 5 0 0 1-5 5h-2.25a1.75 1.75 0 0 0-1.4 2.8l.3.4a1.75 1.75 0 0 1-1.4 2.8z"/><circle cx="13.5" cy="6.5" r=".5" fill="currentColor"/><circle cx="17.5" cy="10.5" r=".5" fill="currentColor"/><circle cx="6.5" cy="12.5" r=".5" fill="currentColor"/><circle cx="8.5" cy="7.5" r=".5" fill="currentColor"/>',
    "type": '<path d="M12 4v16"/><path d="M4 7V5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2"/><path d="M9 20h6"/>',
    "audio-waveform": '<path d="M2 13a2 2 0 0 0 2-2V7a2 2 0 0 1 4 0v13a2 2 0 0 0 4 0V4a2 2 0 0 1 4 0v13a2 2 0 0 0 4 0v-4a2 2 0 0 1 2-2"/>',
    "arrow-right-left": '<path d="m16 3 4 4-4 4"/><path d="M20 7H4"/><path d="m8 21-4-4 4-4"/><path d="M4 17h16"/>',
    "layout-grid": '<rect width="7" height="7" x="3" y="3" rx="1"/><rect width="7" height="7" x="14" y="3" rx="1"/><rect width="7" height="7" x="14" y="14" rx="1"/><rect width="7" height="7" x="3" y="14" rx="1"/>',
    "send": '<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/>',
    "play": '<path d="M5 5a2 2 0 0 1 3.008-1.728l11.997 6.998a2 2 0 0 1 .003 3.458l-12 7A2 2 0 0 1 5 19z"/>',
    "file-video": '<path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/><path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="M15.033 13.44a.647.647 0 0 1 0 1.12l-4.065 2.352a.645.645 0 0 1-.968-.56v-4.704a.645.645 0 0 1 .967-.56z"/>',
    "heart": '<path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5"/>',
    "user-round": '<circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/>',
    "key-round": '<path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/>',
    "mouse-pointer-2": '<path d="M4.037 4.688a.495.495 0 0 1 .651-.651l16 6.5a.5.5 0 0 1-.063.947l-6.124 1.58a2 2 0 0 0-1.438 1.435l-1.579 6.126a.5.5 0 0 1-.947.063z"/>',
    "upload": '<path d="M12 3v12"/><path d="m17 8-5-5-5 5"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>',
    "bookmark": '<path d="M17 3a2 2 0 0 1 2 2v15a1 1 0 0 1-1.496.868l-4.512-2.578a2 2 0 0 0-1.984 0l-4.512 2.578A1 1 0 0 1 5 20V5a2 2 0 0 1 2-2z"/>',
    "paperclip": '<path d="m16 6-8.414 8.586a2 2 0 0 0 2.829 2.829l8.414-8.586a4 4 0 1 0-5.657-5.657l-8.379 8.551a6 6 0 1 0 8.485 8.485l8.379-8.551"/>',
    "arrow-up": '<path d="m5 12 7-7 7 7"/><path d="M12 19V5"/>',
    "file-text": '<path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/><path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    "badge-check": '<path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"/><path d="m16 9-5.5 5.5L8 12"/>',
    "zoom-in": '<circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/><line x1="11" x2="11" y1="8" y2="14"/><line x1="8" x2="14" y1="11" y2="11"/>',
    "plus": '<path d="M5 12h14"/><path d="M12 5v14"/>',
    "message-circle": '<path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/>',
    "video": '<path d="m16 13 5.223 3.482a.5.5 0 0 0 .777-.416V7.87a.5.5 0 0 0-.752-.432L16 10.5"/><rect x="2" y="6" width="14" height="12" rx="2"/>',
    "lock-open": '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/>',
  };
  const svg = (n, sw = 2) => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round">${IC[n]}</svg>`;
  const CLAUDE = '<svg viewBox="0 0 24 24"><path fill="#D97757" d="M4.709 15.955l4.72-2.647.08-.23-.08-.128H9.2l-.79-.048-2.698-.073-2.339-.097-2.266-.122-.571-.121L0 11.784l.055-.352.48-.321.686.06 1.52.103 2.278.158 1.652.097 2.449.255h.389l.055-.157-.134-.098-.103-.097-2.358-1.596-2.552-1.688-1.336-.972-.724-.491-.364-.462-.158-1.008.656-.722.881.06.225.061.893.686 1.908 1.476 2.491 1.833.365.304.145-.103.019-.073-.164-.274-1.355-2.446-1.446-2.49-.644-1.032-.17-.619a2.97 2.97 0 01-.104-.729L6.283.134 6.696 0l.996.134.42.364.62 1.414 1.002 2.229 1.555 3.03.456.898.243.832.091.255h.158V9.01l.128-1.706.237-2.095.23-2.695.08-.76.376-.91.747-.492.584.28.48.685-.067.444-.286 1.851-.559 2.903-.364 1.942h.212l.243-.242.985-1.306 1.652-2.064.73-.82.85-.904.547-.431h1.033l.76 1.129-.34 1.166-1.064 1.347-.881 1.142-1.264 1.7-.79 1.36.073.11.188-.02 2.856-.606 1.543-.28 1.841-.315.833.388.091.395-.328.807-1.969.486-2.309.462-3.439.813-.042.03.049.061 1.549.146.662.036h1.622l3.02.225.79.522.474.638-.079.485-1.215.62-1.64-.389-3.829-.91-1.312-.329h-.182v.11l1.093 1.068 2.006 1.81 2.509 2.33.127.578-.322.455-.34-.049-2.205-1.657-.851-.747-1.926-1.62h-.128v.17l.444.649 2.345 3.521.122 1.08-.17.353-.608.213-.668-.122-1.374-1.925-1.415-2.167-1.143-1.943-.14.08-.674 7.254-.316.37-.729.28-.607-.461-.322-.747.322-1.476.389-1.924.315-1.53.286-1.9.17-.632-.012-.042-.14.018-1.434 1.967-2.18 2.945-1.726 1.845-.414.164-.717-.37.067-.662.401-.589 2.388-3.036 1.44-1.882.93-1.086-.006-.158h-.055L4.132 18.56l-1.13.146-.487-.456.061-.746.231-.243 1.908-1.312-.006.006z"/></svg>';

  // ---------------------------------------------------------------- shared CSS (Claude window + small parts)
  const css = `
  .r5-a { position: absolute; }
  .r5-win { position: absolute; left: 60px; top: 404px; width: 960px; height: 528px; border-radius: 34px; overflow: hidden; transform-origin: 50% 50%;
    background: linear-gradient(180deg, rgba(20,33,88,.975), rgba(10,18,58,.965)); box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.10), 0 30px 60px -30px rgba(2,6,28,.9); }
  .r5-win-tb { position: absolute; left: 0; top: 0; width: 960px; height: 84px; border-bottom: 1.5px solid rgba(255,255,255,.08); }
  .r5-dot { position: absolute; top: 35px; width: 14px; height: 14px; border-radius: 50%; background: rgba(255,255,255,.2); }
  .r5-win-mk { position: absolute; left: 104px; top: 20px; width: 44px; height: 44px; }
  .r5-win-mk svg { width: 44px; height: 44px; display: block; }
  .r5-win-nm { position: absolute; left: 160px; top: 0; font: 700 32px/84px Poppins, sans-serif; color: #ffffff; white-space: nowrap; }
  .r5-win-slot { position: absolute; right: 24px; top: 20px; width: 300px; height: 44px; border-radius: 22px; box-shadow: inset 0 0 0 2px rgba(255,255,255,.18);
    font: 400 22px/44px Poppins, sans-serif; color: rgba(227,237,250,.55); text-align: center; white-space: nowrap; }
  .r5-fchip { position: absolute; height: 44px; padding: 0 18px 0 12px; border-radius: 22px; display: flex; align-items: center; gap: 10px; white-space: nowrap;
    background: rgba(1,204,247,.16); box-shadow: inset 0 0 0 1.5px rgba(1,204,247,.6); font: 700 22px/44px Poppins, sans-serif; color: #e3edfa; }
  .r5-fchip svg { width: 24px; height: 24px; color: #6adfff; flex: none; }
  .r5-win-in { position: absolute; left: 24px; top: 428px; width: 912px; height: 80px; border-radius: 26px; background: rgba(255,255,255,.06); box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.14); }
  .r5-win-ph { position: absolute; left: 28px; top: 0; font: 400 27px/80px Poppins, sans-serif; color: rgba(227,237,250,.5); white-space: nowrap; }
  .r5-win-sd { position: absolute; right: 12px; top: 12px; width: 56px; height: 56px; border-radius: 50%; background: rgba(255,255,255,.12); color: #b9c8e6; }
  .r5-win-sd svg { position: absolute; left: 14px; top: 14px; width: 28px; height: 28px; }
  .r5-win-sd .on { position: absolute; inset: 0; border-radius: 50%; opacity: 0; background: linear-gradient(180deg, #4fe0ff, #01ccf7); box-shadow: 0 0 22px rgba(1,204,247,.55); color: #0b1440; }
  .r5-chip { display: inline-flex; align-items: center; gap: 8px; height: 44px; padding: 0 18px; border-radius: 22px; white-space: nowrap; font: 700 22px/44px Poppins, sans-serif; }
  .r5-chip svg { width: 22px; height: 22px; flex: none; }
  .r5-tree { position: absolute; left: 48px; top: 34px; width: 864px; height: 260px; }
  .r5-tr { position: absolute; height: 56px; display: flex; align-items: center; gap: 14px; font: 400 28px/56px Poppins, sans-serif; color: #e3edfa; white-space: nowrap; }
  .r5-tr.h { font-weight: 700; color: #ffffff; }
  .r5-tr svg { width: 30px; height: 30px; color: #6adfff; flex: none; }
  .r5-tr em { font-style: normal; font-size: 23px; color: #8fa3c8; margin-left: 6px; }
  .r5-tr .ln { position: absolute; left: -26px; top: -28px; width: 18px; height: 56px; border-left: 2px solid rgba(255,255,255,.16); border-bottom: 2px solid rgba(255,255,255,.16); border-radius: 0 0 0 8px; }
  .r5-fin { position: absolute; left: 396px; top: 412px; width: 288px; height: 512px; border-radius: 30px; overflow: hidden; transform-origin: 50% 50%;
    background: linear-gradient(170deg, #1a2f73, #2a6fd6 70%, #3f8ee6); box-shadow: inset 0 0 0 2px rgba(255,255,255,.22), 0 0 0 4px rgba(1,204,247,.35), 0 0 60px rgba(1,204,247,.35), 0 30px 60px -24px rgba(2,6,28,.9); }
  .r5-fin .hd { position: absolute; left: 96px; top: 92px; width: 96px; height: 96px; border-radius: 50%; background: rgba(255,255,255,.26); }
  .r5-fin .sh { position: absolute; left: 50px; top: 198px; width: 188px; height: 170px; border-radius: 94px 94px 0 0; background: rgba(255,255,255,.18); }
  .r5-fin .cp { position: absolute; left: 0; width: 288px; display: flex; justify-content: center; }
  .r5-fin .cp span { height: 50px; padding: 0 14px; border-radius: 12px; background: rgba(8,14,46,.86); font: 700 31px/50px Poppins, sans-serif; color: #ffffff; white-space: nowrap; }
  .r5-fin .cp span.c { color: #01ccf7; }
  .r5-fin .pb { position: absolute; left: 104px; top: 106px; width: 80px; height: 80px; border-radius: 50%; background: rgba(255,255,255,.95); color: #0b1440; box-shadow: 0 10px 24px -8px rgba(2,6,28,.7); }
  .r5-fin .pb svg { position: absolute; left: 24px; top: 21px; width: 38px; height: 38px; fill: #0b1440; stroke-width: 1.5; }
  .r5-fin .bt { position: absolute; left: 0; top: 446px; width: 288px; height: 66px; background: linear-gradient(180deg, rgba(8,14,46,0), rgba(8,14,46,.85)); }
  .r5-fin .bt i { position: absolute; left: 20px; top: 16px; width: 248px; height: 4px; border-radius: 2px; background: rgba(255,255,255,.3); }
  .r5-fin .bt i b { position: absolute; left: 0; top: 0; width: 248px; height: 4px; border-radius: 2px; background: #01ccf7; transform-origin: 0 50%; }
  .r5-fin .bt span { position: absolute; left: 20px; top: 26px; font: 700 21px/34px Poppins, sans-serif; color: #e3edfa; white-space: nowrap; }
  .r5-cursor { position: absolute; left: 0; top: 0; width: 46px; height: 46px; color: #0b1440; filter: drop-shadow(0 4px 8px rgba(2,6,28,.6)); }
  .r5-cursor svg { width: 46px; height: 46px; fill: #ffffff; stroke-width: 1.6; }
  `;
  const st = document.createElement("style"); st.id = "r5-kit-css"; st.textContent = css; (document.head || document.documentElement).appendChild(st);

  // the Claude desktop window (geometry fixed: x 60–1020, y 404–932). P = scene prefix. Parts: P-win, P-tb, P-slot, P-fd (folder chip),
  // P-body, P-in, P-ph, P-sd (send) — o.slot: show the empty "Pilih folder" slot instead of the folder chip
  const win = (P, o = {}) => `<div class="r5-win" id="${P}-win">
      <div class="r5-win-tb" id="${P}-tb"><i class="r5-dot" style="left:28px"></i><i class="r5-dot" style="left:50px"></i><i class="r5-dot" style="left:72px"></i>
        <div class="r5-win-mk" id="${P}-mk">${CLAUDE}</div><div class="r5-win-nm">Claude</div>
        <div class="r5-win-slot" id="${P}-slot">Pilih folder</div>
        <div class="r5-fchip" id="${P}-fd" style="right:24px;top:20px;width:270px;justify-content:center">${svg("folder", 2.2)}<span>AI Video Editor</span></div></div>
      <div class="r5-a" id="${P}-body" style="left:0;top:86px;width:960px;height:340px"></div>
      <div class="r5-win-in" id="${P}-in"><div class="r5-win-ph" id="${P}-ph">Tulis pesan…</div><div class="r5-win-sd" id="${P}-sd">${svg("arrow-up", 2.6)}<i class="on">${svg("arrow-up", 2.6)}</i></div></div>
    </div>`;

  // the project folder as Claude sees it (inside the window body): header + 3 sub-folders. Rows: P-tr0..P-tr3
  const TREE = [["folder-open", "AI Video Editor", ""], ["film", "raw-footage", "video mentah"], ["bookmark", "referensi", "reel contoh"], ["upload", "export", "video jadi"]];
  const tree = (P) => `<div class="r5-tree" id="${P}-tree">` + TREE.map(([ic, nm, ds], i) =>
      `<div class="r5-tr${i ? "" : " h"}" id="${P}-tr${i}" style="left:${i ? 52 : 0}px;top:${i * 58}px">${i ? '<i class="ln"></i>' : ""}${svg(ic, 2.2)}<span>${nm}${i ? "/" : ""}</span>${ds ? `<em>${ds}</em>` : ""}</div>`).join("") + "</div>";

  // the finished reel (st4 end state → s06 frame 0): 9:16 card x 396–684, y 412–924
  const fin = (P) => `<div class="r5-fin" id="${P}-fin"><i class="hd"></i><i class="sh"></i><div class="pb" id="${P}-pb">${svg("play", 1.5)}</div>` +
    `<div class="cp" style="top:300px"><span>edit pakai</span></div><div class="cp" style="top:356px"><span class="c">Claude</span></div>` +
    `<div class="bt"><i><b id="${P}-fbar"></b></i><span>final.mp4 · 1080×1920</span></div></div>`;

  // ---------------------------------------------------------------- timeline boilerplate
  function scene(id) {
    const SC = window.VO_SCENES.find((s) => s.id === id), VW = window.VO_WORDS;
    const LAST = window.VO_SCENES[window.VO_SCENES.length - 1].id;
    const D = SC.dur, ST = SC.start, SLOT = D + (id === LAST ? 0 : 0.4);
    // local time of the n-th (0-based) occurrence of a word inside this scene
    const L = (txt, n = 0) => { const ws = VW.filter((w, i) => w[0] === txt && i >= SC.w0 && i <= SC.w1); if (!ws[n]) throw new Error(id + ": no word " + txt + "#" + n); return ws[n][1] - ST; };
    const tl = gsap.timeline({ paused: true });
    const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
    { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); tl.set = (a, v, p) => s0(a, _sc(v), p); tl.fromTo = (a, x, y, p) => f0(a, _sc(x), _sc(y), p); tl.to = (a, v, p) => t0(a, _sc(v), p); }
    const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), t);
    const I = (el, v) => { gsap.set(el, _sc(v)); tl.set(el, v, 0); };
    const $ = (x) => document.getElementById(x);
    const WJ = "⁠";   // word joiner: keeps GSAP from parsing numeric textContent
    // typewriter: spans per character, shown one by one between t0 and t1
    const type = (el, text, t0, t1) => {
      el.innerHTML = ""; const n = text.length, out = [];
      for (let i = 0; i < n; i++) { const s = document.createElement("span"); s.textContent = text[i]; el.appendChild(s); out.push(s); I(s, { display: "none" }); tl.set(s, { display: "inline" }, t0 + (t1 - t0) * (i / n)); }
      return out;
    };
    // counter: per-value sets (no onUpdate)
    const count = (el, a, b, t0, t1, fmt = (v) => String(v), steps = 0) => {
      const n = steps || Math.max(1, Math.abs(b - a));
      tl.set(el, { textContent: fmt(a) + WJ }, 0);
      for (let j = 1; j <= n; j++) { const u = j / n, e = 1 - Math.pow(1 - u, 2); tl.set(el, { textContent: fmt(Math.round(a + (b - a) * e)) + WJ }, t0 + (t1 - t0) * u); }
    };
    const done = () => {
      tl.set({}, {}, SLOT - 0.01);
      (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
      window.__timelines = window.__timelines || {};
      window.__timelines[id] = tl;
    };
    return { tl, D, ST, SLOT, L, ft, I, $, type, count, done, WJ };
  }
  window.R5 = { IC, svg, CLAUDE, win, tree, fin, scene };
})();

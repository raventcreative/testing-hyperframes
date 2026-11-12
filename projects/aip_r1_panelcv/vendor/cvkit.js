// CV KIT (AI PRENEUR R1 · panel rekrutmen 7 Claude): the shared CV document + the 7 reviewers + icons, used by every scene so the hero
// objects stay identical across cuts. Pure markup/CSS builders (no animation). Loaded in index.html <head> before the compositions.
(function () {
  const ICO = {   // lucide-static 1.70 (ISC) — https://lucide.dev
    "scan-text": '<path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/><path d="M7 21H5a2 2 0 0 1-2-2v-2"/><path d="M7 8h8"/><path d="M7 12h10"/><path d="M7 16h6"/>',
    "briefcase-business": '<path d="M12 12h.01"/><path d="M16 6V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><path d="M22 13a18.15 18.15 0 0 1-20 0"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
    "user-round-check": '<path d="M2 21a8 8 0 0 1 13.292-6"/><circle cx="10" cy="8" r="5"/><path d="m16 19 2 2 4-4"/>',
    "users-round": '<path d="M18 21a8 8 0 0 0-16 0"/><circle cx="10" cy="8" r="5"/><path d="M22 20c0-3.37-2-6.5-4-8a5 5 0 0 0-.45-8.3"/>',
    "crown": '<path d="M11.562 3.266a.5.5 0 0 1 .876 0L15.39 8.87a1 1 0 0 0 1.516.294L21.183 5.5a.5.5 0 0 1 .798.519l-2.834 10.246a1 1 0 0 1-.956.734H5.81a1 1 0 0 1-.957-.734L2.02 6.02a.5.5 0 0 1 .798-.519l4.276 3.664a1 1 0 0 0 1.516-.294z"/><path d="M5 21h14"/>',
    "handshake": '<path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.88-3.88a3 3 0 0 0-4.24 0l-.88.88a1 1 0 1 1-3-3l2.81-2.81a5.790 5.790 0 0 1 7.06-.87l.47.28a2 2 0 0 0 1.42.25L21 4"/><path d="m21 3 1 11h-2"/><path d="M3 3 2 14l6.5 6.5a1 1 0 1 0 3-3"/><path d="M3 4h8"/>',
    "timer": '<line x1="10" x2="14" y1="2" y2="2"/><line x1="12" x2="15" y1="14" y2="11"/><circle cx="12" cy="14" r="8"/>',
    "glasses": '<circle cx="6" cy="15" r="4"/><circle cx="18" cy="15" r="4"/><path d="M14 15a2 2 0 0 0-2-2 2 2 0 0 0-2 2"/><path d="M2.5 13 5 7c.7-1.3 1.4-2 3-2"/><path d="M21.5 13 19 7c-.7-1.3-1.5-2-3-2"/>',
    "user-round": '<circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "mail-x": '<path d="M22 12.532V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8.792"/><path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"/><path d="m16.5 16.5 5 5"/><path d="m21.5 16.5-5 5"/>',
    "mail": '<path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"/><rect x="2" y="4" width="20" height="16" rx="2"/>',
    "send": '<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/>',
    "door-closed": '<path d="M19 21V5a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v16"/><path d="M2 21h20"/><path d="M9 12h.01"/>',
    "lock": '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "circle-help": '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
    "list-checks": '<path d="M13 5h8"/><path d="M13 12h8"/><path d="M13 19h8"/><path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/>',
    "file-check": '<path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/><path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="m9 15 2 2 4-4"/>',
    "file-user": '<path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/><path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="M16 22a4 4 0 0 0-8 0"/><circle cx="12" cy="15" r="3"/>',
    "hourglass": '<path d="M5 22h14"/><path d="M5 2h14"/><path d="M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22"/><path d="M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2"/>',
    "message-circle": '<path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/>',
    "pen-line": '<path d="M13 21h8"/><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/>',
    "sparkles": '<path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/>',
    "search": '<path d="m21 21-4.34-4.34"/><circle cx="11" cy="11" r="8"/>',
    "arrow-right": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "link": '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>' };
  const isvg = (n, sw) => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round">${ICO[n]}</svg>`;
  // the Claude mark — @lobehub/icons-static-svg 1.102.0 (MIT), assets/icons/lobe-claude-color.svg, unmodified path
  const CLAUDE = '<svg viewBox="0 0 24 24"><path fill="#D97757" d="M4.709 15.955l4.72-2.647.08-.23-.08-.128H9.2l-.79-.048-2.698-.073-2.339-.097-2.266-.122-.571-.121L0 11.784l.055-.352.48-.321.686.06 1.52.103 2.278.158 1.652.097 2.449.255h.389l.055-.157-.134-.098-.103-.097-2.358-1.596-2.552-1.688-1.336-.972-.724-.491-.364-.462-.158-1.008.656-.722.881.06.225.061.893.686 1.908 1.476 2.491 1.833.365.304.145-.103.019-.073-.164-.274-1.355-2.446-1.446-2.49-.644-1.032-.17-.619a2.97 2.97 0 01-.104-.729L6.283.134 6.696 0l.996.134.42.364.62 1.414 1.002 2.229 1.555 3.03.456.898.243.832.091.255h.158V9.01l.128-1.706.237-2.095.23-2.695.08-.76.376-.91.747-.492.584.28.48.685-.067.444-.286 1.851-.559 2.903-.364 1.942h.212l.243-.242.985-1.306 1.652-2.064.73-.82.85-.904.547-.431h1.033l.76 1.129-.34 1.166-1.064 1.347-.881 1.142-1.264 1.7-.79 1.36.073.11.188-.02 2.856-.606 1.543-.28 1.841-.315.833.388.091.395-.328.807-1.969.486-2.309.462-3.439.813-.042.03.049.061 1.549.146.662.036h1.622l3.02.225.79.522.474.638-.079.485-1.215.62-1.64-.389-3.829-.91-1.312-.329h-.182v.11l1.093 1.068 2.006 1.81 2.509 2.33.127.578-.322.455-.34-.049-2.205-1.657-.851-.747-1.926-1.62h-.128v.17l.444.649 2.345 3.521.122 1.08-.17.353-.608.213-.668-.122-1.374-1.925-1.415-2.167-1.143-1.943-.14.08-.674 7.254-.316.37-.729.28-.607-.461-.322-.747.322-1.476.389-1.924.315-1.53.286-1.9.17-.632-.012-.042-.14.018-1.434 1.967-2.18 2.945-1.726 1.845-.414.164-.717-.37.067-.662.401-.589 2.388-3.036 1.44-1.882.93-1.086-.006-.158h-.055L4.132 18.56l-1.13.146-.487-.456.061-.746.231-.243 1.908-1.312-.006.006z"/></svg>';
  // the 7 reviewers: [role, icon, colour]  (same as compositions/panel.html)
  const JUDGES = [null,
    ["Sistem ATS", "scan-text", "#01ccf7"], ["Hiring Manager", "briefcase-business", "#ffb35c"], ["Calon Atasan", "user-round-check", "#9d8cff"],
    ["Sesama Pelamar", "users-round", "#ff8f6b"], ["CEO", "crown", "#ffd66b"], ["Rekan Setim", "handshake", "#3ddc97"], ["Rekruter Sibuk", "timer", "#ff5c8a"]];
  const SEAT_X = (k) => 540 + (k - 4) * 134, CMP_X = (k) => 540 + (k - 4) * 76;
  // the 7 notes (one per reviewer), shown in s06 and the stamps' order in s01
  const NOTES = [null, "Kata kunci kurang", "Nggak ada angka", "Kurang inisiatif", "Kalah spesifik", "Dampak bisnis?", "Kerja tim cuma klaim", "Ringkasan klise"];

  // ------------------------------------------------------------------ THE CV (base 460×560; position the wrapper by its CENTRE with x/y)
  const css = (P) => `
    .${P}-cv { position: absolute; left: 0; top: 0; width: 460px; height: 560px; margin: -280px 0 0 -230px; transform-origin: 50% 50%; }
    .${P}-cv * { position: absolute; }
    .${P}-cv-pg { left: 0; top: 0; width: 460px; height: 560px; border-radius: 26px; background: linear-gradient(180deg, #ffffff, #f1f5fc);
      box-shadow: 0 44px 70px -30px rgba(0,0,0,.8), inset 0 0 0 1px rgba(255,255,255,.8); overflow: hidden; }
    .${P}-cv-av { left: 32px; top: 30px; width: 76px; height: 76px; border-radius: 50%; background: linear-gradient(180deg, #e3ecfb, #c9d8f0); color: #294b77; }
    .${P}-cv-av svg { left: 18px; top: 16px; width: 40px; height: 40px; }
    .${P}-cv-nm { left: 126px; top: 30px; font: 700 32px/40px Poppins, sans-serif; color: #0a0d2c; letter-spacing: -.015em; white-space: nowrap; }
    .${P}-cv-ps { left: 126px; top: 72px; font: 400 22px/30px Poppins, sans-serif; color: #294b77; white-space: nowrap; }
    .${P}-cv-hr { left: 32px; top: 124px; width: 396px; height: 2px; background: #e1e8f3; }
    .${P}-cv-h { left: 32px; font: 700 16px/20px Poppins, sans-serif; letter-spacing: .16em; color: #0878a3; white-space: nowrap; }
    .${P}-cv-t { left: 32px; width: 396px; font: 400 21px/29px Poppins, sans-serif; color: #0a0d2c; }
    .${P}-cv-t.n { white-space: nowrap; }
    .${P}-cv-t.b { font-weight: 700; }
    .${P}-cv-t .ph { position: relative; display: inline-block; padding: 0 9px; margin: 0 2px; border-radius: 9px; background: rgba(1,204,247,.16); box-shadow: inset 0 0 0 1.5px #01ccf7;
      color: #0a87b5; font-weight: 700; font-size: 18px; line-height: 26px; vertical-align: 1px; }
    .${P}-cv-ks { left: 32px; top: 478px; width: 396px; height: 38px; }
    .${P}-cv-k { top: 0; height: 38px; padding: 0 14px; border-radius: 19px; background: #e9f0fa; color: #294b77; font: 400 18px/38px Poppins, sans-serif; white-space: nowrap; }
    .${P}-cv-k.nw { background: rgba(45,164,78,.13); color: #1f7a3a; font-weight: 700; box-shadow: inset 0 0 0 1.5px rgba(45,164,78,.55); }
    .${P}-cv-v2 { left: 356px; top: 16px; height: 34px; padding: 0 13px; border-radius: 17px; background: #2da44e; color: #fff; font: 700 17px/34px Poppins, sans-serif; letter-spacing: .06em; white-space: nowrap; }
    .${P}-cv-st { left: 0; top: 0; width: 460px; height: 560px; }
    .${P}-stamp { left: 0; top: 0; width: 220px; height: 76px; margin: -38px 0 0 -110px; border-radius: 14px; border: 5px solid #e5484d; color: #e5484d;
      font: 700 42px/66px Poppins, sans-serif; letter-spacing: .1em; text-align: center; background: rgba(255,240,240,.55); box-shadow: 0 0 0 2px rgba(229,72,77,.18); }
  `;
  // the content rows (v1 = the CV you send, v2 = rewritten in s06). [id, top, cls, v1 text, v2 text]
  const ROWS = [
    ["ps", 72, "", "Staf Marketing", "Digital Marketing"],
    ["sum", 166, "t", "Pekerja keras, cepat belajar, bisa kerja tim.", "2 tahun pegang konten &amp; iklan 3 brand, bareng tim sales."],
    ["job", 278, "t n b", "Staf Marketing · PT Contoh", null],
    ["b1", 308, "t n", "• Mengurus media sosial kantor", '• IG 3 brand: reach naik <span class="ph">angka</span>%'],
    ["b2", 338, "t n", "• Membantu acara kantor", '• Usul event, leads naik <span class="ph">angka</span>%'],
    ["edu", 408, "t n", "S1 Manajemen · 2021", null]];
  const KS1 = [["Ms Office", 0], ["Canva", 124], ["Komunikasi", 224]], KS2 = [["Meta Ads", 0], ["Canva", 124], ["Copywriting", 224]];
  const cv = (P, id, ver) => {
    const v2 = ver === 2, X = `${P}-${id}`;
    let h = `<div class="${P}-cv" id="${X}"><div class="${P}-cv-pg" id="${X}-pg">` +
      `<div class="${P}-cv-av">${isvg("user-round", 2.2)}</div><div class="${P}-cv-nm">Nama Kamu</div><div class="${P}-cv-hr"></div>` +
      `<div class="${P}-cv-h" style="top:142px">RINGKASAN</div><div class="${P}-cv-h" style="top:254px">PENGALAMAN</div>` +
      `<div class="${P}-cv-h" style="top:384px">PENDIDIKAN</div><div class="${P}-cv-h" style="top:452px">SKILL</div>`;
    for (const [rid, top, cls, t1, t2] of ROWS) {
      const c = rid === "ps" ? `${P}-cv-ps` : cls.split(" ").map((q) => q === "t" ? `${P}-cv-t` : q).join(" ");
      h += `<div class="${c}" id="${X}-${rid}" style="top:${top}px;opacity:${t2 && v2 ? 0 : 1}">${t1}</div>`;
      if (t2) h += `<div class="${c}" id="${X}-${rid}2" style="top:${top}px;opacity:${v2 ? 1 : 0}">${t2}</div>`;
    }
    h += `<div class="${P}-cv-ks">` + KS1.map(([t, x], i) => `<div class="${P}-cv-k" id="${X}-k${i + 1}" style="left:${x}px;opacity:${v2 && i !== 1 ? 0 : 1}">${t}</div>`).join("") +
      KS2.map(([t, x], i) => i === 1 ? "" : `<div class="${P}-cv-k nw" id="${X}-k${i + 1}b" style="left:${x}px;opacity:${v2 ? 1 : 0}">${t}</div>`).join("") + `</div>`;
    h += `<div class="${P}-cv-v2" id="${X}-v2" style="opacity:${v2 ? 1 : 0}">CV v2</div>`;
    h += `<div class="${P}-cv-st" id="${X}-st"></div></div></div>`;
    return h;
  };
  // the 7 "TOLAK" stamps of s01 (CV-local coordinates; s01 adds them, s02 shows them stamped)
  const STAMPS = [[118, 196, -14], [330, 150, 11], [206, 318, -6], [336, 392, -17], [118, 444, 8], [262, 496, -9], [236, 240, 15]];
  const STAMP_ORDER = [4, 2, 6, 1, 5, 3, 7];   // reviewer k of stamp i
  const stamps = (P, id) => STAMPS.map(([x, y, r], i) => `<div class="${P}-stamp" id="${P}-${id}-s${i}" style="transform:translate(${x}px,${y}px) rotate(${r}deg)">TOLAK</div>`).join("");
  // pin the v1/v2 visibility of a CV instance on a scene timeline at 0 (never rely on inline CSS alone in the real renderer)
  const pin = (tl, P, id, ver) => { const X = `${P}-${id}`, v2 = ver === 2, g = (q) => document.getElementById(X + q);
    for (const [rid, , , , t2] of ROWS) { tl.set(g("-" + rid), { opacity: t2 && v2 ? 0 : 1 }, 0); if (t2) tl.set(g("-" + rid + "2"), { opacity: v2 ? 1 : 0 }, 0); }
    [1, 2, 3].forEach((i) => tl.set(g("-k" + i), { opacity: v2 && i !== 2 ? 0 : 1 }, 0));
    [1, 3].forEach((i) => tl.set(g("-k" + i + "b"), { opacity: v2 ? 1 : 0 }, 0));
    tl.set(g("-v2"), { opacity: v2 ? 1 : 0 }, 0); };
  window.CVK = { ICO, isvg, CLAUDE, JUDGES, SEAT_X, CMP_X, NOTES, css, cv, ROWS, STAMPS, STAMP_ORDER, stamps, pin };
})();

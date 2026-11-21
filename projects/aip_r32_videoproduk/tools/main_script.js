      (function () {
        const OFF = 0.3, DUR = 55.6;
        const WORDS = /*WORDS*/;
        const W = (txt, after = 0) => { const w = WORDS.find((x) => x[0] === txt && x[1] + OFF >= after); if (!w) throw new Error("ui: word not found " + txt); return w[1] + OFF; };
        const KEYW = new Set(["foto", "produk", "ai", "video", "promo", "suara", "marketer", "contoh", "alurnya", "umkm", "online", "shop", "affiliator", "terang", "depan", "samping", "detail", "kemasan",
          "naskah", "adegan", "detik", "harga", "ukuran", "target", "pembelinya", "hook", "manfaat", "ajakan", "beli", "keranjang", "kuning", "dibacakan", "jualan", "dirender", "vertikal", "diunggah",
          "tonton", "mirip", "alat", "bantu", "produksi", "jaminan", "laku", "klaim", "posting", "komen", "prompt", "checklist", "dm", "satu", "dua", "tiga", "empat"]);
        const bare = (w) => w.toLowerCase().replace(/[^a-z]/g, "");
        const KOMEN = W("Komen");
        const disp = (w, t) => (t >= KOMEN - 0.01 && bare(w) === "promo" ? w.toUpperCase() : w);
        // chunks: break after , . : ? or at 4 words
        const CHUNKS = []; { let a = 0; for (let i = 0; i < WORDS.length; i++) { const end = /[,.:?]$/.test(WORDS[i][0]) || i - a === 3 || i === WORDS.length - 1; if (end) { CHUNKS.push([a, i + 1]); a = i + 1; } } }
        const tl = gsap.timeline({ paused: true });
        const _sc = (v) => { if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; };
        { const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); tl.set = (a, v, p) => s0(a, _sc(v), p); tl.fromTo = (a, x, y, p) => f0(a, _sc(x), _sc(y), p); tl.to = (a, v, p) => t0(a, _sc(v), p); }
        const P0 = gsap.timeline(); tl.add(P0, 0);
        const pin = (el, v) => { gsap.set(el, _sc(v)); P0.set(el, _sc(v), 0); };
        const ft = (el, a, b, t) => tl.fromTo(el, a, Object.assign({ immediateRender: false }, b), t);
        // captions (per-word boxes; bottom while the world is full screen, above the hosts afterwards)
        const caps = document.getElementById("caps");
        CHUNKS.forEach(([a, b], ci) => {
          const d = document.createElement("div"); d.className = "cap"; const t0 = WORDS[a][1] + OFF; d.style.top = (t0 < 6.95 ? 1430 : 1000) + "px"; caps.appendChild(d);
          const ws = [];
          for (let i = a; i < b; i++) { const m = document.createElement("span"); m.className = "m"; const w = document.createElement("span"); const key = KEYW.has(bare(WORDS[i][0]));
            w.className = "w" + (key ? " k" : ""); w.textContent = disp(WORDS[i][0], WORDS[i][1] + OFF); if (key) { const h = document.createElement("span"); h.className = "hl"; w.appendChild(h); }
            m.appendChild(w); d.appendChild(m); if (i < b - 1) d.appendChild(document.createTextNode(" ")); ws.push([w, WORDS[i][1] + OFF]); }
          const tIn = ws[0][1] - 0.06, next = CHUNKS[ci + 1], tOut = next ? WORDS[next[0]][1] + OFF - 0.08 : DUR - 0.3;
          pin(d, { opacity: 0 }); ft(d, { opacity: 0 }, { opacity: 1, duration: 0.1, ease: "none" }, tIn); ft(d, { opacity: 1, y: 0 }, { opacity: 0, y: -10, duration: 0.12, ease: "power2.in" }, Math.max(tIn + 0.2, tOut - 0.12));
          ws.forEach(([w, t]) => { pin(w.parentNode, { opacity: 0 }); ft(w.parentNode, { opacity: 0 }, { opacity: 1, duration: 0.08, ease: "none" }, Math.max(tIn, t - 0.06));
            pin(w, { yPercent: 118 }); ft(w, { yPercent: 118 }, { yPercent: 0, duration: 0.3, ease: "power4.out" }, Math.max(tIn, t - 0.05));
            const h = w.querySelector(".hl"); if (h) { pin(h, { scaleX: 0 }); ft(h, { scaleX: 0 }, { scaleX: 1, duration: 0.26, ease: "power2.out" }, t + 0.08); } });
        });
        // section titles (flip down from the top)
        const title = (id, a, b) => { const e = document.getElementById(id); pin(e, { xPercent: -50, opacity: 0 });
          ft(e, { opacity: 0, rotationX: -88, y: -20, transformPerspective: 900, transformOrigin: "50% 0%" }, { opacity: 1, rotationX: 0, y: 0, duration: 0.45, ease: "back.out(1.6)" }, a);
          ft(e, { opacity: 1, y: 0 }, { opacity: 0, y: -24, duration: 0.22, ease: "power2.in" }, b); };
        const TT = [["t1", 0.45, 5.15], ["t2", W("Ini") - 0.05, 10.5], ["t3", W("Satu.") - 0.05, W("Dua.") - 0.4], ["t4", W("Dua.") + 0.05, W("Hook") - 0.5], ["t5", W("Hook") - 0.05, W("Tiga.") - 0.35],
          ["t6", W("Tiga.") + 0.05, W("Empat.") - 0.35], ["t7", W("Empat.") + 0.05, W("Video") - 0.3], ["t8", W("Video") + 0.05, W("Tapi") - 0.35], ["t9", W("Tapi") + 0.05, KOMEN - 0.35]];
        TT.forEach((x) => title(...x));
        // counter chip windows
        const CHIP = [[W("UMKM,") - 0.2, 10.5, "COCOK UNTUK", [W("UMKM,"), W("online"), W("sampai")]], [W("Adegan,") - 0.25, W("video", 36) - 0.3, "BAHAN RENDER", [W("Adegan,"), W("foto,", 30), W("suara", 36)]]];
        pin("#chip", { opacity: 0, scale: 0.6 });
        CHIP.forEach(([a, b]) => { ft("#chip", { opacity: 0, scale: 0.6, x: -30 }, { opacity: 1, scale: 1, x: 0, duration: 0.38, ease: "back.out(2)" }, a);
          ft("#chip", { opacity: 1, scale: 1 }, { opacity: 0, scale: 0.8, duration: 0.18, ease: "power2.in" }, b); });
        const TAGS = [[0.5, W("AI") - 0.1, "PRODUK CONTOH"]];
        pin("#tag", { opacity: 0 }); TAGS.forEach(([a, b]) => { ft("#tag", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.25, ease: "back.out(2)" }, a); ft("#tag", { opacity: 1 }, { opacity: 0, duration: 0.12 }, b - 0.12); });
        // page-level transitions: shutter flash, dive flash (match cut), whip blur, iris, shockwave
        const DUA = W("Dua."), TIGA = W("Tiga."), TAPI = W("Tapi"), PRODUK = W("produk,");
        pin("#flashW", { opacity: 0 });
        ft("#flashW", { opacity: 0 }, { opacity: 0.4, duration: 0.05 }, PRODUK - 0.02); ft("#flashW", { opacity: 0.4 }, { opacity: 0, duration: 0.3 }, PRODUK + 0.03);
        ft("#flashW", { opacity: 0 }, { opacity: 1, duration: 0.12, ease: "power2.in" }, DUA - 0.12); ft("#flashW", { opacity: 1 }, { opacity: 0, duration: 0.32, ease: "power2.out" }, DUA + 0.01);
        pin("#vx", { filter: "blur(0px)" }); ft("#vx", { filter: "blur(0px)" }, { filter: "blur(14px)", duration: 0.2, ease: "power2.in" }, TIGA - 0.24); ft("#vx", { filter: "blur(14px)" }, { filter: "blur(0px)", duration: 0.3, ease: "power2.out" }, TIGA - 0.02);
        pin("#iris", { "--r": "1600px", autoAlpha: 0 }); tl.set("#iris", { autoAlpha: 1 }, TAPI - 0.5); tl.set("#iris", { autoAlpha: 0 }, TAPI + 0.5);
        ft("#iris", { "--r": "1600px" }, { "--r": "0px", duration: 0.4, ease: "power3.in" }, TAPI - 0.46); ft("#iris", { "--r": "0px" }, { "--r": "1600px", duration: 0.45, ease: "power3.out" }, TAPI - 0.03);
        pin("#ring", { opacity: 0, scale: 0.1 }); ft("#ring", { opacity: 1, scale: 0.1 }, { opacity: 0, scale: 6, duration: 0.6, ease: "power2.out" }, KOMEN - 0.25);
        // CTA: comment box types PROMO, send, the DM arrives with the photo card (through-line) dropping into it
        const PROMO = W("promo,"), KIRIM = W("kirim", 50);
        pin("#ctaveil", { opacity: 0 }); ft("#ctaveil", { opacity: 0 }, { opacity: 1, duration: 0.3 }, KOMEN - 0.1);
        pin("#cbox", { opacity: 0, y: 40 }); ft("#cbox", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "back.out(1.6)" }, KOMEN - 0.05);
        ft("#send", { scale: 1 }, { scale: 0.88, duration: 0.08, yoyo: true, repeat: 1 }, KIRIM);
        pin("#dm", { opacity: 0, x: 120 }); ft("#dm", { opacity: 0, x: 120 }, { opacity: 1, x: 0, duration: 0.4, ease: "back.out(1.4)" }, KIRIM + 0.2);
        pin("#pol", { opacity: 0, x: -160, y: 520, rotation: -28 }); ft("#pol", { opacity: 0, x: -160, y: 520, rotation: -28 }, { opacity: 1, x: 180, y: 800, rotation: -6, duration: 0.55, ease: "back.out(1.5)" }, KIRIM + 0.4);
        tl.fromTo("#grain", { x: 0, y: 0 }, { x: 64, y: 40, duration: DUR, ease: "steps(1668)", immediateRender: false }, 0); pin("#grain", { x: 0, y: 0 });
        tl.set({}, {}, DUR - 0.01);
        (function (t) { const r = t.render; t.render = function (tt, se, f) { if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }; })(tl);
        tl.render(0, true, true);
        window.__timelines = window.__timelines || {}; window.__timelines["main"] = tl;
        // per-seek text (pure functions of time)
        const $ = (id) => document.getElementById(id);
        const cnt = (arr, t) => arr.filter((x) => t >= x).length;
        function texts(t) {
          const c = CHIP.find(([a, b]) => t >= a - 0.05 && t < b + 0.3) || CHIP[0]; $("cl").textContent = c[2]; $("ci").textContent = "";
          $("cn").textContent = cnt(c[3], t) + "/3";
          { const g = TAGS.find(([a, b]) => t >= a - 0.02 && t < b) || TAGS[0]; $("tg").textContent = g[2]; }
          const typed = "PROMO".slice(0, Math.max(0, Math.min(5, Math.floor((t - PROMO + 0.05) / 0.07) + 1)));
          $("ctx").textContent = t >= PROMO - 0.05 ? typed : ""; $("cph").style.display = t >= PROMO - 0.05 ? "none" : "inline";
          $("cur").style.opacity = Math.floor(t * 3) % 2 ? 1 : 0.2;
        }
        texts(0); window.addEventListener("hf-seek", (e) => texts(e.detail.time));
      })();

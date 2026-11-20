# DM untuk yang komen ALAT — Panduan 4 alat Claude Code (dari kode sampai online)
(dicek dari sumber resmi 13 Nov 2026; perintah bisa berubah — kalau gagal, cek README resminya)

Hai! Ini 4 alat yang aku bahas, urut sesuai alur bikin web: dokumentasi → data → tes → online.

**Cara paling gampang (di Claude Code):** ketik `/plugin`, buka tab **Discover**, cari namanya — atau langsung:
`/plugin install context7@claude-plugins-official`
`/plugin install supabase@claude-plugins-official`
`/plugin install chrome-devtools-mcp@claude-plugins-official`
`/plugin install vercel@claude-plugins-official`
Pasang hanya plugin yang kamu percaya, lalu restart Claude Code.

1. **Context7 (Upstash)** — Claude ambil dokumentasi resmi sesuai versi library di project-mu.
   - Alternatif: `npx ctx7 setup --claude` (butuh Node.js 22.13+; bikin API key gratis via login).
   - Cara pakai: tambahkan "use context7" di prompt, atau sebut versinya ("pakai Next.js 16").
   - Repo: github.com/upstash/context7

2. **Supabase MCP (resmi Supabase)** — Claude bisa bikin tabel, jalanin SQL, dan menyimpan perubahan sebagai migration.
   - Alternatif manual: server `https://mcp.supabase.com/mcp` (login Supabase lewat browser saat pertama dipakai).
   - AMAN: pakai project/branch khusus latihan, bukan production. Kalau terpaksa ke production: batasi ke satu project
     (`?project_ref=…`) dan mode baca saja (`&read_only=true`). Jangan matikan persetujuan per perintah.
   - Repo: github.com/supabase-community/supabase-mcp

3. **Chrome DevTools MCP (tim Chrome, Google)** — Claude buka webmu di Chrome, klik & isi form kayak pembeli, baca console,
   network, sampai performa.
   - Alternatif manual: `claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest`
   - Coba: "Buka localhost:3000, coba pesan 1 kue, lalu cek error di console dan network."
   - Catatan: isi browser itu bisa dibaca Claude — jangan login ke akun sensitif di browser yang dipakai.
   - Repo: github.com/ChromeDevTools/chrome-devtools-mcp

4. **Vercel (plugin resmi Vercel)** — deploy dari Claude Code: preview dulu, production setelah kamu konfirmasi.
   - Alternatif MCP saja: `claude mcp add --transport http vercel https://mcp.vercel.com`
   - Catatan: deploy PERTAMA di project baru bisa langsung jadi production — cek dulu sebelum menyetujui.
   - Repo: github.com/vercel/vercel-plugin

**Contoh prompt satu alur (web pesanan toko kue):**
"Bikin web pre-order kue pakai Next.js, use context7. Simpan pesanan di Supabase (project latihan), simpan perubahan sebagai migration.
Lalu tes form pesannya di Chrome dan cek console + network. Kalau sudah aman, deploy ke preview Vercel dulu."

**Catatan aman:** database & deploy itu nyentuh production. Latihan di project tes, baca tiap perintah sebelum klik izinkan
(apalagi DELETE / DROP), dan naik ke production hanya setelah kamu cek link preview-nya.

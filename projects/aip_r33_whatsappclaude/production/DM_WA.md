# DM untuk yang komen "WA" — Panduan setup WhatsApp MCP + checklist keamanan

Halo! Ini panduan yang aku janjiin di video. Proyeknya: **WhatsApp MCP** buatan Luke Harries (open source, lisensi MIT) —
https://github.com/lharries/whatsapp-mcp. Semua langkah di bawah diringkas dari README resminya; kalau ada beda, ikuti README.

> Penting: ini nyambung ke **akun WhatsApp pribadimu** (lewat WhatsApp Web multi-device). Baca bagian keamanan dulu sebelum mulai.

## A. Yang perlu disiapin
1. **Go** (bahasa pemrograman) — untuk menjalankan "bridge" WhatsApp.
2. **Python 3.6+**.
3. **UV** (package manager Python). Pasang dengan: `curl -LsSf https://astral.sh/uv/install.sh | sh`
4. **Claude Desktop** (atau Cursor).
5. **FFmpeg** — opsional, cuma kalau mau kirim audio sebagai pesan suara (format .ogg Opus).
6. Windows? Aktifkan CGO dan pasang C compiler (README menyarankan MSYS2), lalu `go env -w CGO_ENABLED=1`.

## B. Langkah setup
1. **Unduh repo-nya**
   ```
   git clone https://github.com/lharries/whatsapp-mcp.git
   cd whatsapp-mcp
   ```
2. **Jalankan bridge WhatsApp**
   ```
   cd whatsapp-bridge
   go run main.go
   ```
   Pertama kali, muncul **kode QR** di terminal → buka WhatsApp di HP → Perangkat Tertaut → scan.
   Biarkan bridge ini tetap jalan (bridge + server Python harus sama-sama hidup).
3. **Sambungkan ke Claude Desktop** — buat/isi file `claude_desktop_config.json`
   (Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`):
   ```json
   {
     "mcpServers": {
       "whatsapp": {
         "command": "{{PATH_TO_UV}}",
         "args": ["--directory", "{{PATH_TO_SRC}}/whatsapp-mcp/whatsapp-mcp-server", "run", "main.py"]
       }
     }
   }
   ```
   - `{{PATH_TO_UV}}` = hasil perintah `which uv`
   - `{{PATH_TO_SRC}}` = folder tempat kamu clone repo (cek dengan `pwd`)
   - Pakai Cursor? Simpan sebagai `~/.cursor/mcp.json`.
4. **Restart Claude Desktop** → WhatsApp muncul sebagai integrasi.
5. **Tunggu riwayat termuat** — setelah login pertama, riwayat chat bisa butuh beberapa menit untuk masuk.

## C. 12 tool yang tersedia (dikelompokkan seperti di video)
- **Laci CARI:** `search_contacts` (cari kontak pakai nama/nomor), `list_chats`, `get_chat`, `get_direct_chat_by_contact`
- **Laci BACA:** `list_messages` (pakai filter + konteks), `get_message_context`, `get_last_interaction`, `get_contact_chats`
- **Laci KIRIM:** `send_message` (ke nomor atau grup), `send_file` (gambar, video, dokumen, audio mentah), `send_audio_message` (pesan suara)
- **Laci UNDUH:** `download_media` (unduh media dari pesan, dapat lokasi file di komputermu)

Contoh pertanyaan ke Claude (tulis pakai bahasa sehari-hari):
- "Supplier kain kemarin kasih harga berapa? Tunjukin juga konteks obrolannya."
- "Kapan terakhir aku chat sama Bu Rina, dan dia minta apa?"
- "Rangkum chat grup reseller hari ini, mana yang perlu aku balas?"
(Nama di atas hanya contoh.)

## D. Checklist keamanan (wajib baca)
README-nya sendiri memberi peringatan: seperti banyak server MCP, WhatsApp MCP rentan **prompt injection** (README menyebutnya
"lethal trifecta") yang bisa membuat **data pribadi bocor**. Artinya: pesan dari orang lain bisa berisi perintah tersembunyi untuk AI-nya.
- [ ] Pahami dulu: Claude bisa **membaca** chat pribadimu dan **mengirim** pesan/file atas namamu.
- [ ] **Cek dulu sebelum Claude ngirim apa pun** — jangan setujui pengiriman pesan/file yang tidak kamu minta.
- [ ] Waspada kalau Claude tiba-tiba mau mengirim chat/data ke nomor yang tidak kamu kenal → tolak.
- [ ] Jangan suruh Claude "mengikuti instruksi" yang tertulis di dalam pesan orang lain.
- [ ] Hati-hati menggabungkan WhatsApp MCP dengan MCP/tool lain yang bisa mengirim data keluar (web, email, dll.) dalam satu sesi.
- [ ] Data riwayat pesan disimpan **lokal** di SQLite (`whatsapp-bridge/store/`) — jaga komputermu (kunci layar, jangan dibagi).
- [ ] Pesan hanya dikirim ke Claude saat tool dipakai — matikan integrasi saat tidak dipakai.
- [ ] Kira-kira **tiap ±20 hari** kamu mungkin perlu scan QR ulang (login ulang).
- [ ] Kalau perangkat tertaut penuh: hapus salah satu di WhatsApp → Settings → Linked Devices.
- [ ] Chat tidak sinkron? Hapus `whatsapp-bridge/store/messages.db` dan `whatsapp.db`, lalu jalankan ulang bridge (login ulang).
- [ ] Ini proyek komunitas (bukan produk resmi WhatsApp/Anthropic). Pakai dengan risiko sendiri.

Kalau mentok di salah satu langkah, balas DM ini dan sebutkan error-nya — nanti aku bantu cek. — AIpreneur

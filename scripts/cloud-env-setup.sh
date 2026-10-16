#!/usr/bin/env bash
# Claude Code cloud environment setup script — HyperFrames global setup for Freddie.
# Paste the whole file into: cloud environment menu (session title bar) → Edit → Setup script.
set -e
# 1) HyperFrames skills, user-level (available in every repo/session)
npx -y skills add heygen-com/hyperframes -g --agent claude-code -y >/dev/null 2>&1 || echo "WARN: skills install failed"
# 2) Chrome for local rendering
npx -y hyperframes browser ensure >/dev/null 2>&1 || echo "WARN: browser ensure failed"
# 3) CDN vendoring helper
mkdir -p "$HOME/.local/bin"
cat > "$HOME/.local/bin/hf-vendor-libs" <<'VENDOR'
#!/usr/bin/env bash
# Replace cdn.jsdelivr.net / unpkg.com <script src> URLs in a HyperFrames project with local copies
# fetched through npm (works when the network policy blocks the CDNs but allows the npm registry).
# Usage: scripts/hf-vendor-libs.sh <project-dir>
set -euo pipefail
PROJECT="${1:?usage: hf-vendor-libs.sh <project-dir>}"
cd "$PROJECT"
mkdir -p vendor

URLS=$(grep -rhoE 'https://(cdn\.jsdelivr\.net/npm|unpkg\.com)/[^"'"'"' )]+' --include='*.html' . | sort -u || true)
[ -z "$URLS" ] && { echo "Tidak ada library CDN yang perlu di-vendor."; exit 0; }

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
for url in $URLS; do
  spec=${url#https://cdn.jsdelivr.net/npm/}
  spec=${spec#https://unpkg.com/}
  # spec = [@scope/]name@version/path/to/file
  if [[ $spec == @* ]]; then pkg=$(cut -d/ -f1-2 <<<"$spec"); file=$(cut -d/ -f3- <<<"$spec")
  else pkg=$(cut -d/ -f1 <<<"$spec"); file=$(cut -d/ -f2- <<<"$spec"); fi
  name=${pkg%@*}
  [ -z "$file" ] && { echo "Lewati (tanpa path file): $url"; continue; }
  local_path="vendor/${name//\//_}/$file"
  if [ ! -f "$local_path" ]; then
    (cd "$TMP" && npm pack "$pkg" --silent >/dev/null && tar -xzf ./*.tgz && rm -f ./*.tgz)
    mkdir -p "$(dirname "$local_path")"
    cp "$TMP/package/$file" "$local_path"
    rm -rf "$TMP/package"
  fi
  grep -rlF "$url" --include='*.html' . | xargs sed -i "s#$url#$local_path#g"
  echo "OK: $url -> $local_path"
done
VENDOR
chmod +x "$HOME/.local/bin/hf-vendor-libs"
ln -sf "$HOME/.local/bin/hf-vendor-libs" /usr/local/bin/hf-vendor-libs 2>/dev/null || true
# 4) Global rules (user-level CLAUDE.md)
mkdir -p "$HOME/.claude"
cat > "$HOME/.claude/CLAUDE.md" <<'RULES'
# HyperFrames workspace — Freddie Kashawan

Skill HyperFrames (dari `heygen-com/hyperframes`) terpasang global di `~/.claude/skills/`.
Jangan edit file skill-nya langsung; aturan lokal ada di sini.

## Environment (wajib diikuti setiap kali skill hyperframes dipakai)

- Chrome render disiapkan otomatis oleh setup script environment.
  Sebelum render pertama, pastikan siap dengan `npx hyperframes browser ensure` (idempotent, cepat kalau sudah ada).
- Network cloud bisa memblokir `cdn.jsdelivr.net` / `unpkg.com`. Setelah `hyperframes init` atau `hyperframes add`,
  dan sebelum `preview`/`render`, SELALU jalankan:
  `hf-vendor-libs <project-dir>` — mengganti URL CDN di HTML dengan file lokal dari npm.
  Kalau render gagal dengan `sub_timeline_script_failure` atau `connect_rejected`, jalankan script ini dulu, lalu render ulang.
- Saat `init` di sini, set `HYPERFRAMES_SKIP_SKILLS=1` (skill sudah terpasang global) dan pakai `--non-interactive`.
- Project video taruh di `projects/<nama-project>/`. Output MP4 final taruh di `projects/<nama-project>/out/`.

## Kebijakan credit HeyGen (WAJIB)

Prinsip: **lokal & gratis dulu, HeyGen hanya kalau memang tidak bisa diganti dan sudah disetujui user.**

GRATIS — jalankan tanpa tanya:
- Authoring komposisi (HTML/GSAP), `catalog`/`add` registry (pencarian lokal), `lint`/`check`/`snapshot`/`preview`.
- Render lokal: `npx hyperframes render` (Chrome + FFmpeg di container). JANGAN pernah pakai `cloud render` sebagai default.
- Logo (theSVG/favicon), color grade/LUT, SFX dari library bawaan, transkripsi lokal (whisper), Kokoro TTS / mflux / LTX lokal kalau terpasang.
- MCP HyperFrames by HeyGen: hanya tool baca (`list_projects`, `get_project`, `get_project_status`, `get_render_status`).

BERBAYAR / pakai kuota HeyGen — WAJIB minta izin dulu:
- `npx hyperframes cloud render` / `cloudrun` / `lambda` (per credit; 4K = 1.5×).
- MCP `compose` dan `render_video` (bikin project & render di cloud HeyGen).
- `media-use resolve --type video` (avatar video HeyGen) — paling mahal.
- TTS voiceover HeyGen, BGM/image/icon dari katalog HeyGen. Via OAuth = kuota gratis bulanan (tetap terbatas);
  via API key = langsung potong API credits. Login HeyGen CLI selalu pakai `--oauth`, bukan API key.

Format minta izin (satu pesan, singkat): fitur apa, kenapa butuh HeyGen, alternatif gratisnya apa
(dan kekurangannya), perkiraan pemakaian (durasi/jumlah). Tanpa "ya" eksplisit → pakai alternatif gratis.

Default otomatis:
- Pakai `resolve --local-only` kecuali user sudah setuju pakai HeyGen untuk project itu.
- Musik/voice: tanya dulu apakah user punya file sendiri (rekaman suara Freddie / musik lisensi) sebelum generate.
- Sebelum & sesudah aksi berbayar, cek `npx hyperframes auth status` / `usage --json` dan laporkan sisa kuota.
- Render draft (`--quality draft`) untuk review, render final sekali saja setelah approve.

## Default kreatif (kalau user tidak menyebut lain)

- Format: 9:16 portrait 1080x1920 (`--resolution portrait`) — untuk Reels / TikTok / Shorts.
- Bahasa teks on-screen: Bahasa Indonesia, gaya Freddie: tajam, cepat, Gen Z tapi profesional.
- Struktur short-form: hook kuat di 1–2 detik pertama, isi padat, CTA jelas di akhir.
- Brand: AIpreneur (default), SKINKU, Rave Tailor, Raveloux — sesuaikan tone per brand (lihat preferensi user).
- Caption/teks harus terbaca di safe zone (hindari area UI Reels/TikTok di bawah & kanan).
- Pertanyaan intent interview dari skill tetap boleh, tapi ringkas; jangan tanya hal yang sudah dijawab default di atas.
RULES
echo "HyperFrames global setup done"

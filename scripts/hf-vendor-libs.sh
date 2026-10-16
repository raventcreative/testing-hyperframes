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

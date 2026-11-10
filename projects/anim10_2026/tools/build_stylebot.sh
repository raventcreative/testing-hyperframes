#!/usr/bin/env bash
# Bundles src/stylebot.js (+ src/sb/*) -> vendor/stylebot3d.js (IIFE, window.StyleBot).
# Uses three 0.170 + esbuild installed in ../mascot-bizman/tools/node_modules (resolved through NODE_PATH).
set -euo pipefail
cd "$(dirname "$0")/.."
NM="${STYLEBOT_NODE_MODULES:-$(cd ../mascot-bizman/tools/node_modules && pwd)}"
NODE_PATH="$NM" "$NM/.bin/esbuild" src/stylebot.js --bundle --format=iife --minify --target=es2020 \
  --legal-comments=none --outfile=vendor/stylebot3d.js "$@"
ls -la vendor/stylebot3d.js

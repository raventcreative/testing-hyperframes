#!/usr/bin/env bash
# SessionStart hook: prepare HyperFrames rendering in the background so the session isn't blocked.
LOG="${TMPDIR:-/tmp}/hf-session-setup.log"
(
  echo "[$(date -Is)] hyperframes setup start"
  npx -y hyperframes browser ensure
  echo "[$(date -Is)] hyperframes setup done (exit $?)"
) >"$LOG" 2>&1 </dev/null &
disown
echo "HyperFrames: Chrome render sedang disiapkan di background (log: $LOG)."
exit 0

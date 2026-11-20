# Snapshot queue — run when the CPU lock is free again

Paused mid-QA for the delivery render. The build is complete and `check` passed on the previous revision;
only the chip sub-label size (16→22 px) and the R-scene camera landing changed after that pass.

## 1. Re-run the check (clears the one outstanding warning)
```bash
flock /tmp/claude-0/cpu.lock npx --yes hyperframes@0.8.186 check .
```
Expect 0 errors. The previous run's only non-caption warning was
`text_below_floor` on the chip's "angka ilustrasi" at 14 px — the 22 px bump should clear it.
The ~29 `line_unread` warnings are the usual short-caption ones in this series.

## 2. Verify what changed since its last snapshot
```
40.56, 40.62, 40.70, 40.85, 41.05   # whip landing (R entry now starts at aim y 15 and tilts down by 41.08)
3.5, 12.0, 22.5, 33.0, 42.5, 51.5   # the counter chip at its new 22 px sub-label
41.5, 43.8, 45.6                    # radar dish framing after the scale/offset change
```

## 3. The client's every-second audit (`references/client_rules.md`: "audit every second before rendering")
Covered so far by scene/transition sampling (~70 frames); still owed as one continuous sweep:
```
0.5,1.5,2.5,…,68.5      # 69 frames, 6 contact sheets
```
Build with `--no-end --timeout 60000 --describe false` and read every sheet.
Watch for: text sliced by the frame or by a texture edge, text behind the tab/chip/captions,
an empty stage mid-transition, the robot cropped anywhere but the very bottom edge, off-brand UI colour.

## 4. Known-good moments (already audited, re-check only if something upstream changes)
hook 0.5–9.5 · portal 9.9–10.6 · agents 11–19.4 · island hop 20.1–21.2 · stalls 21.6–26.5 ·
gaps + both side rises 27.9–30.3 · iris 30.9–31.8 · review wall 32–39.5 · demand rows 44.8–48.8 ·
match cut 50.1–51.2 · Monday page 53–59.8 · CTA 61.2–67.5

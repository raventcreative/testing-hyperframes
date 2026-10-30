# Source-screen recording analysis & privacy handling

## Verified original recording properties

- User filename: **Google - Google Chrome 2026-10-30 10-54-11.mp4**
- 1920×1032 pixel wide desktop capture
- Approximately 59.94 fps, **35.276 seconds**
- Original file **is deliberately excluded from this ZIP** due to sensitive visible account/project material. A rebuilt safe interface is the recommended final output.

## Observed narrative timeline (approximate)

| Source timestamp | Actual observed content | Use in final |
| --- | --- | --- |
| 0–~7 sec | Dark Google page, click into search field, suggestions and search | Recreate clean search, typed Claude, no search-history suggestions |
| ~7–12 sec | Results about Claude | Recreate search result and key click position; use supplied cursor/ripple |
| ~12–22 sec | Claude home / dashboard; personal account context, Recent and project/artifact sections can appear | Recreate sanitized public-looking home layout, no personal details |
| ~22–35 sec | Dark Claude Code workspace, environment/processing UI | Recreate neutral Code workspace and type new 3D demo prompt; raw file does **not** show actual generated 3D result |
| Not in original | Prompt resulting in astronaut/cube animation, mascot half-body, synchronized blur + sharp panel | Build separately as new original content, with transparent storytelling |

## Non-negotiable redaction

**Never display or encode original readable personal UI**:

- Claude **Recent** conversation names, **Projects** sidebar or project names.
- Center-screen recent artifact/project thumbnails and labels.
- Browser suggestions and search-history terms.
- Personal account details, profile photo, file paths, repository names, private chats, private prompts or private developer status names.
- Partially unmasked private content during intermediate keyframes, zoom, slide, crossfade, corner reflections, or transition blur.

**Technique priority:**

1. Preferred: **privacy-safe UI recreation** using generic design motifs and only public product brand elements. This is exactly what the present ZIP instructs.
2. If user later supplies a pre-redacted source clip: use only the validated scrubbed clip.
3. If a raw capture must be handled: apply **solid, opaque region replacement/crop before any camera transforms**, then visually review the processed input and the full rendered output. Blurring alone is NOT sufficient when text is confidential. Do not publish any raw still or contact sheet with real project names.

## Native wide recording vs portrait final

The original is 1920×1032 landscape-like; final is 1080×1920 portrait. Direct scaling would make UI unreadable. Reconstruct into a 9:16 composition with animated tight zoom into the search field, relevant result, click location and Code prompt. The camera path, not the raw full desktop, gives continuity.

## Truthfulness

The original recording **does not document** a full prompt → working 3D result generation. The typing/loading/result sequence is a deliberately rebuilt motion sequence; the astronaut/miniature-world output must be created as a real animated asset in the project. Do not caption the screen recording as authentic evidence of a completed generation it did not record.

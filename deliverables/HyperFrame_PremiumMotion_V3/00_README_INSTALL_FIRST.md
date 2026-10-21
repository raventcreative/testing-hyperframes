# HYPERFRAME PROMPT V3.0 — HOUSE STYLE REF-H · SETUP & FILE MAP
**Dibuat:** 21 Oktober 2026. Upgrade dari V2.1 berdasarkan Reel AI PRENEUR v3 yang sudah di-approve ("nice aku suka").

## APA YANG BERUBAH DARI V2.1
- **Default look baru = REF-H "Ice-Ivory Illustrated Diorama"**: visual-first, tanpa headline besar, caption kecil 1 baris di atas, satu scene ilustrasi detail per frasa VO, palet terang ice/ivory/navy, dan apex tepat di kata kunci. REF-A/B/C sekarang hanya perpustakaan motif pelengkap.
- **Dokumen baru:**
  - `11_HOUSE_STYLE_BIBLE.md` — token persis, resep material/FX CSS, motion grammar, katalog metafora.
  - `12_SCENE_CONTRACT_CLAUDE.md` — kontrak untuk tiap scene builder.
  - `13_PRODUCTION_PIPELINE.md` — proses persis yang menghasilkan v3.
  - `04B_EXAMPLE_AIPRENEUR_V3_EXECUTION_PROMPT.md` — contoh prompt terisi penuh.
- **`02_MASTER_PROMPT_CLAUDE_CODE_V3.md`** menggantikan V2. Isinya blok HOUSE STYLE LOCK + SCENE CONTRACT yang wajib di-inline ke prompt Claude, plus arsitektur sub-composition per scene.
- **`house_style_kit/`** (baru, untuk workspace Claude Code):
  - `starter/` — template siap pakai, sudah diuji: lint 0 error, snapshot benar.
  - `example_aipreneur_v3/` — source lengkap v3 (index + 15 scene + transkrip + VO + logo), bisa langsung di-render ulang.
  - `tools/` — script opsional untuk alignment kata.
- **`golden_frames/`** (19 still dari v3) + `style_references/ref_H_house_style_aipreneur_v3.mp4` + `reference_contact_sheets/ref_H_house_style_overview.jpg`.
- Diperbarui: `01` (Project Instructions V3, 5.4k karakter), `03` V3, `06` (bagian 0 REF-H), `07` (§11 gate REF-H), `08` (tes kalibrasi REF-H), `09` (handoff V3).

## CARA PASANG — CHATGPT PROJECT "HyperFrame Prompt"
1. **Project Instructions:** ganti seluruh isinya dengan `source_docs/01_PROJECT_INSTRUCTIONS_PASTE.md`.
2. **Hapus/arsipkan** source lama: `02_MASTER_PROMPT_CLAUDE_CODE_V2.md`, `03_EXTENDED_PROJECT_RULES_REFERENCE_V2.md` (dan V1 jika masih ada).
3. **Upload** sebagai Project sources: `02_…_V3.md`, `03_…_V3.md`, `04B_…`, `06`, `07`, `11`, `12`, `13`. `04`, `05` dan `08` opsional.
4. **Upload juga** `reference_contact_sheets/ref_H_house_style_overview.jpg` + beberapa `golden_frames/` (mis. H03, H08, H12, H14, H15, H19), supaya ChatGPT bisa melihat look-nya.
5. Chat baru: paste blok **PROMPT PEMBUKA** dari `09_HANDOFF_CHAT_BARU.md`.

## CARA PASANG — WORKSPACE CLAUDE CODE (Windows)
1. Extract ZIP ini ke folder kerja HyperFrames lu (mis. `D:\HyperFrames\`). Pastikan folder ini satu level dengan `projects\`:
   - `house_style_kit\`
   - `golden_frames\`
   - `source_docs\`
   - `style_references\`
2. (Disarankan) Buka `house_style_kit\example_aipreneur_v3\` di Claude Code dan jalankan `npx hyperframes lint` + `npx hyperframes preview`, untuk memastikan semuanya jalan di mesin lu.
3. Untuk video baru: paste prompt dari ChatGPT. Prompt merujuk ke `house_style_kit/` dan `golden_frames/`, lalu Claude akan menyalin `starter/` ke project baru.
4. Opsional: jalankan tes `source_docs/08_OPTIONAL_LOOKDEV_CALIBRATION_TEST.md` (12 detik) untuk kalibrasi.

## PETA FILE
| Path | Peran |
|---|---|
| `source_docs/01…13` | instruksi & standar (lihat atas) |
| `house_style_kit/starter/` | `index.html` (BG + caption + slot scene + VO, berisi placeholder `{{…}}`), `compositions/_scene_template.html`, `assets/brand/` (plate pastel 1080×1920, grain), `vendor/gsap` |
| `house_style_kit/example_aipreneur_v3/` | source v3 lengkap yang bisa di-render ulang |
| `house_style_kit/tools/` | `asr_segments.py`, `probe_pauses.py`, `align_words.py` (opsional, butuh Python + sherpa-onnx) |
| `golden_frames/H01–H19` | still REF-H di momen hero (nama file = detik) |
| `style_references/` | REF-A/B/C (motif pelengkap) + **REF-H** (house style) |
| `reference_contact_sheets/` | contact sheet A/B/C + `ref_H_house_style_overview.jpg` |
| `REFERENCE_MEDIA_INVENTORY.json` | metadata + sha256 semua video referensi |

## BATASAN JUJUR
- Model AI tidak menghasilkan output yang identik 100% antar-run. Paket ini mengunci **token gaya, arsitektur, proses, kontrak scene, contoh source dan golden frames**, sehingga hasil berikutnya konsisten satu seri dengan v3. Tiap metafora baru tetap digambar ulang sesuai VO-nya.
- REF-A/B/C tetap hanya referensi gaya. Jangan dipakai sebagai footage.
- Logo AI PRENEUR di `example_aipreneur_v3` adalah aset milik user. Gunakan sesuai aturan (hanya set lebar).

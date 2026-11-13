# Checklist AMAN — sebelum agent AI nyentuh server klien

Contoh untuk server **Ubuntu/Debian**. Ganti `agent` dan `/var/www/toko` sesuai punyamu. Jalankan semua perintah dari **akun admin kamu**
(yang bisa `sudo`), bukan dari akun agent. Coba dulu di server latihan/staging, dan **backup database** sebelum mulai.

---

## SEBELUM agent mulai

**1. Akun sendiri buat agent — bukan admin, bukan sudo**
```bash
sudo adduser agent          # akun biasa
groups agent                # pastikan TIDAK ada "sudo" di daftar grupnya
# akses tulis cuma ke folder web klien (paket "acl")
sudo setfacl -R -m u:agent:rwX /var/www/toko
sudo setfacl -R -d -m u:agent:rwX /var/www/toko
```
Agent kerja pakai akun ini (login/SSH sebagai `agent`), jangan pakai akun admin atau root.

**2. Commit git = titik awal**
```bash
cd /var/www/toko
git init                                   # sekali saja, kalau belum ada repo
echo ".env" >> .gitignore                  # file rahasia jangan ikut di-commit
git add -A && git commit -m "sebelum agent"
```
Simpan juga salinannya di luar server (mis. push ke repo privat dari akun admin), biar snapshot-nya nggak bisa diutak-atik agent.

**3. Hermes Agent: approvals = manual (rem tangan)**
```bash
hermes config set approvals.mode manual
```
atau langsung di `~/.hermes/config.yaml`:
```yaml
approvals:
  mode: manual            # smart (bawaan) | manual | off
  deny:                   # diblok total, bahkan kalau yolo nyala
    - 'rm -rf *'
    - '*drop table*'
```
- `manual` = tiap perintah yang masuk daftar berbahaya **selalu nunggu izinmu** (pilih once / session / always / deny; bawaannya deny).
- **Jangan pernah**: `hermes --yolo`, `/yolo`, `HERMES_YOLO_MODE=1`, atau `approvals.mode: off` — semuanya melewati semua izin.
- Lebih aman: jalankan Hermes di laptopmu dan suruh dia kerja lewat SSH pakai akun agent (config-nya tetap di laptopmu, agent nggak bisa ubah):
  `~/.hermes/config.yaml` → `terminal: { backend: ssh }`, `~/.hermes/.env` → `TERMINAL_SSH_HOST=ip-server` dan `TERMINAL_SSH_USER=agent`.
- Catatan: kalau backend-nya docker/sandbox, cek perintah berbahaya dilewati (container-nya yang jadi batas).

**4. OpenCode: permission = ask (bawaannya hampir semua allow)**

Taruh di `/etc/opencode/opencode.json` (folder milik root → akun agent nggak bisa ngelonggarin sendiri, dan prioritasnya paling tinggi):
```bash
sudo mkdir -p /etc/opencode && sudo nano /etc/opencode/opencode.json
```
```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "bash": { "*": "ask", "rm *": "deny" },
    "edit": "ask",
    "webfetch": "ask",
    "external_directory": "ask"
  }
}
```
- Aturan yang **paling bawah menang** — taruh `"*"` dulu, pengecualian sesudahnya.
- **Jangan** jalankan `opencode --auto` / `opencode run --auto` (semua yang nggak di-deny langsung disetujui).
- Format di atas (V1) tetap dibaca OpenCode 2. Format asli V2 (opsional): `"permissions": [ { "action": "shell", "resource": "*", "effect": "ask" }, ... ]`.

---

## SELAMA agent kerja

**5. auditd: rekam semua perintah akun agent + jamnya**
```bash
sudo apt install auditd
sudo systemctl enable --now auditd
sudo nano /etc/audit/rules.d/agent.rules
```
Isi `agent.rules`:
```
-a always,exit -F arch=b64 -S execve -F uid=agent -k agent
-a always,exit -F arch=b32 -S execve -F uid=agent -k agent
```
```bash
sudo augenrules --load
sudo auditctl -l            # aturannya harus muncul, dan TIDAK ada baris "never,task"
```

**6. Log-nya milik root**
```bash
sudo ls -l /var/log/audit/  # pemilik: root
```
Akun agent nggak punya sudo → nggak bisa hapus/ubah log ini. (Opsional, kunci aturan audit sampai reboot: tambah `-e 2` sebagai baris
terakhir aturan.) Log Hermes sendiri ada di `~/.hermes/logs/` — kalau Hermes jalan pakai akun agent, log itu bisa dia hapus, jadi pegangan
utamamu tetap log auditd.

---

## SESUDAH agent selesai

**7. Cek perubahan — ini buktimu ke klien**
```bash
sudo ausearch -k agent -i --start today   # semua perintah akun agent hari ini + jamnya
cd /var/www/toko
git status                  # file apa yang berubah + file baru
git diff                    # baris apa yang diganti
git restore index.html      # batalkan perubahan yang nggak kamu minta
git clean -n                # lihat file baru yang belum ke-track (hapus pakai -f kalau yakin)
```

---

**Ingat:** larangan di prompt ("jangan hapus database ya") itu bukan pagar — AI bisa salah paham, atau ketipu perintah titipan di file/website
yang dia baca. Pagarnya harus di sistem: akun terbatas, izin (manual/ask/deny), log milik root, dan backup.

Sumber resmi: Ubuntu Server docs (User management) · man auditctl/augenrules/ausearch/auditd.conf (linux-audit) · man setfacl (Ubuntu) ·
dokumentasi git (git-status, git-diff, git-restore, git-clean) · Hermes Agent docs (Security, Configuration) · OpenCode docs (Permissions,
Config, Migrate from V1).

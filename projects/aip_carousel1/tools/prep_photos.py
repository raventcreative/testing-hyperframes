"""Download + crop the CC0 photos (WordPress Photo Directory via Openverse) used inside the demo landing pages.

Usage: python3 -I tools/prep_photos.py <cache_dir>   (run from the project folder; originals are cached in <cache_dir>)
Writes effects/<effect>/img/<name>.jpg and the "photos" list of production/asset_credits.json.
"""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/car1_photos")

# key: (effect, out name, url, out w, out h, focal x, focal y, creator, landing page)
PHOTOS = [
    ("harga-coret", "hampers", "https://pd.w.org/2025/09/47168d22457e28818.92430425-1536x2048.jpg", 480, 600, 0.5, 0.45, "Alina Kakshapati", "https://wordpress.org/photos/photo/47168d2245/"),
    ("tombol-wa", "nasi", "https://pd.w.org/2026/06/9966a2a857c41d0b8.53758714-1536x2048.jpg", 520, 560, 0.5, 0.62, "Vishnu Chandra", "https://wordpress.org/photos/photo/9966a2a857/"),
    ("notif-pembeli", "cabai", "https://pd.w.org/2022/10/382633b149b1f5189.15596979-2048x1360.jpg", 600, 560, 0.5, 0.5, "Abhishek Deshpande", "https://wordpress.org/photos/photo/382633b149/"),
    ("kartu-flip", "mie", "https://pd.w.org/2026/07/6976a6954dabbb2e0.03615637-1757x2048.jpg", 560, 440, 0.5, 0.5, "Noelia Segura", "https://wordpress.org/photos/photo/6976a6954d/"),
    ("kartu-flip", "nasgor", "https://pd.w.org/2025/05/655681f3f013286e8.95976799-2048x1376.jpg", 560, 440, 0.62, 0.5, "Dulcea Suresha", "https://wordpress.org/photos/photo/655681f3f0/"),
    ("kartu-flip", "esteh", "https://pd.w.org/2025/09/10368db8b751490e6.71123774-1536x2048.jpg", 560, 440, 0.5, 0.55, "Alina Kakshapati", "https://wordpress.org/photos/photo/10368db8b7/"),
    ("tab-menu", "kopisusu", "https://pd.w.org/2026/01/493697dce2a48e9c6.63631315-1536x2048.jpeg", 400, 400, 0.5, 0.52, "Bigul Malayi", "https://wordpress.org/photos/photo/493697dce2/"),
    ("tab-menu", "americano", "https://pd.w.org/2026/05/89169f61d97151f40.80882990-1536x2048.jpeg", 400, 400, 0.45, 0.62, "Uttkrista Chhetri", "https://wordpress.org/photos/photo/89169f61d9/"),
    ("tab-menu", "cappuccino", "https://pd.w.org/2026/01/72696f7e70326602.29454872-1536x2048.jpeg", 400, 400, 0.52, 0.66, "Preeti Shah", "https://wordpress.org/photos/photo/72696f7e70/"),
    ("tab-menu", "matcha", "https://pd.w.org/2026/03/1869c75f6aa641f8.65571191-1510x2048.jpeg", 400, 400, 0.55, 0.6, "Manjil Aryal", "https://wordpress.org/photos/photo/1869c75f6a/"),
    ("tab-menu", "cokelat", "https://pd.w.org/2025/04/53867ffd2d0c569d5.03944213-1536x2048.jpeg", 400, 400, 0.5, 0.5, "shirishpoudel07", "https://wordpress.org/photos/photo/53867ffd2d/"),
    ("tab-menu", "semangka", "https://pd.w.org/2026/06/4226a38d5c58e2a27.55500567-1536x2048.jpeg", 400, 400, 0.5, 0.45, "Yam B Chhetri", "https://wordpress.org/photos/photo/4226a38d5c/"),
    ("tab-menu", "donat", "https://pd.w.org/2022/06/1562be09ebbbcb74.64402380-2048x1536.jpg", 400, 400, 0.5, 0.5, "Faisal Ahammad", "https://wordpress.org/photos/photo/1562be09eb/"),
    ("tab-menu", "croissant", "https://pd.w.org/2022/03/210622cf2763dc374.65124722-2048x1365.jpg", 400, 400, 0.5, 0.5, "Reyes Martínez", "https://wordpress.org/photos/photo/210622cf27/"),
    ("tab-menu", "cookies", "https://pd.w.org/2022/03/133621d8743d97575.02359676-2048x1365.jpg", 400, 400, 0.55, 0.45, "mdburnette", "https://wordpress.org/photos/photo/133621d874/"),
    ("keranjang", "bonsai", "https://pd.w.org/2024/11/540674aa12b55d7d8.81731094-1536x2048.jpg", 440, 440, 0.5, 0.6, "Pratap Patil - Walstar Technologies Pvt Ltd", "https://wordpress.org/photos/photo/540674aa12/"),
    ("keranjang", "syngonium", "https://pd.w.org/2025/06/967685a74a0efbab5.29028570-1536x2048.jpeg", 440, 440, 0.5, 0.7, "Yam B Chhetri", "https://wordpress.org/photos/photo/967685a74a/"),
    ("keranjang", "palem", "https://pd.w.org/2025/03/17967d7b51f81a412.72657658-1536x2048.jpeg", 440, 440, 0.55, 0.62, "Yam B Chhetri", "https://wordpress.org/photos/photo/17967d7b51/"),
    ("popup-diskon", "buket", "https://pd.w.org/2026/06/3516a3909f567a506.98334299-1542x2048.jpg", 480, 600, 0.5, 0.5, "Shaddam Hossain", "https://wordpress.org/photos/photo/3516a3909f/"),
    ("menu-hp", "sepatu", "https://pd.w.org/2026/05/25469f71feaf1c929.07741303-1536x2048.jpg", 480, 420, 0.5, 0.42, "Vishnu Chandra", "https://wordpress.org/photos/photo/25469f71fe/"),
]


def crop(im, w, h, fx, fy):
    sw, sh = im.size
    s = max(w / sw, h / sh)
    nw, nh = round(sw * s), round(sh * s)
    im = im.resize((nw, nh), Image.LANCZOS)
    x = min(max(0, round(nw * fx - w / 2)), nw - w)
    y = min(max(0, round(nh * fy - h / 2)), nh - h)
    return im.crop((x, y, x + w, y + h))


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    credits = []
    for eff, name, url, w, h, fx, fy, creator, landing in PHOTOS:
        src = CACHE / url.rsplit("/", 1)[1]
        if not src.exists():
            subprocess.run(["curl", "-sS", "--max-time", "90", "-o", str(src), url], check=True)
        out = ROOT / "effects" / eff / "img" / f"{name}.jpg"
        out.parent.mkdir(parents=True, exist_ok=True)
        im = Image.open(src).convert("RGB")
        crop(im, w, h, fx, fy).save(out, quality=82, optimize=True, progressive=True)
        credits.append({"file": f"effects/{eff}/img/{name}.jpg", "source": landing, "original": url, "author": creator,
                        "licence": "CC0 1.0 (WordPress Photo Directory, found via Openverse)", "changes": f"cropped + resized to {w}x{h}"})
        print("ok", out.relative_to(ROOT), out.stat().st_size)
    f = ROOT / "production" / "asset_credits.json"
    data = json.loads(f.read_text()) if f.exists() else {}
    data["photos"] = credits
    f.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()

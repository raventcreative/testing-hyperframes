"""Wikimedia Commons photo acquisition for the Indonesia journey.

Step 1 - search + download candidates (needs commons.wikimedia.org + upload.wikimedia.org):
    python3 -I tools/commons_photos.py fetch [photo-id ...]
  -> assets/photos/_candidates/<id>/NN.jpg + candidates.json (title, author, licence, page URL)
  -> assets/photos/_candidates/<id>/sheet.jpg  (numbered contact sheet for visual inspection)

Step 2 - after looking at each sheet, pick one candidate per landmark:
    python3 -I tools/commons_photos.py pick <photo-id> <NN> [--label "..."] [--focus 0.5,0.4] [--note "..."]
  -> assets/photos/<id>.jpg (EXIF orientation applied, long side <= 1800 px), data/photos.json updated

Step 3 - python3 -I tools/commons_photos.py credits   -> CREDITS.md

Only free licences are accepted: CC0, Public domain, CC BY, CC BY-SA (no NC / ND).
"""
import html, json, os, re, sys, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTOS = os.path.join(ROOT, "data", "photos.json")
CAND = os.path.join(ROOT, "assets", "photos", "_candidates")
API = "https://commons.wikimedia.org/w/api.php"
UA = "IndonesiaMapJourney/1.0 (HyperFrames motion project; contact raventcreative2022@gmail.com)"

# extra search phrasings per landmark (Commons file search is literal)
EXTRA = {
    "sby-suroboyo": ["Suro dan Boyo", "Sura and Baya statue", "Monumen Suro Boyo"],
    "sby-tugu": ["Tugu Pahlawan", "Heroes Monument Surabaya"],
    "sby-alakbar": ["Al-Akbar Mosque Surabaya", "Masjid Nasional Al-Akbar"],
    "jkt-monas": ["Monas Jakarta", "National Monument Jakarta"],
    "jkt-fatahillah": ["Fatahillah Museum", "Jakarta History Museum Kota Tua"],
    "jkt-bundaranhi": ["Bundaran HI", "Selamat Datang Monument"],
    "mdn-maimun": ["Maimun Palace", "Istana Maimun"],
    "mdn-almashun": ["Great Mosque of Medan", "Masjid Raya Al Mashun"],
    "mdn-tjongafie": ["Tjong A Fie Mansion", "Rumah Tjong A Fie"],
    "bali-tanahlot": ["Tanah Lot", "Pura Tanah Lot"],
    "bali-ulundanu": ["Ulun Danu Beratan", "Pura Ulun Danu Bratan"],
    "bali-gwk": ["Garuda Wisnu Kencana statue", "GWK statue Bali"],
    "solo-keraton": ["Keraton Surakarta", "Kasunanan Surakarta palace"],
    "solo-mangkunegaran": ["Pura Mangkunegaran", "Mangkunegaran Palace"],
    "solo-pasargede": ["Pasar Gede Hardjonagoro", "Pasar Gede Solo"],
    "bdg-sate": ["Gedung Sate"],
    "bdg-merdeka": ["Gedung Merdeka Bandung", "Museum Konperensi Asia Afrika"],
    "bdg-braga": ["Jalan Braga", "Braga street Bandung"],
    "yog-tugu": ["Tugu Yogyakarta", "Tugu Jogja"],
    "yog-tamansari": ["Taman Sari Yogyakarta", "Tamansari water castle"],
    "yog-malioboro": ["Malioboro", "Jalan Malioboro"],
    "mks-rotterdam": ["Fort Rotterdam Makassar", "Benteng Ujung Pandang"],
    "mks-99kubah": ["Masjid 99 Kubah", "99 Domes Mosque Makassar"],
    "mks-losari": ["Pantai Losari", "Losari Beach Makassar"],
}
FREE = re.compile(r"^(cc0|public domain|pd\b|pd-|cc by(-sa)?( \d(\.\d)?)?)", re.I)
NONFREE = re.compile(r"\b(nc|nd)\b|noncommercial|noderiv", re.I)


def get(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    return data if binary else json.loads(data)


def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def search(q, limit=20):
    params = dict(action="query", format="json", generator="search", gsrsearch=f"{q} filetype:bitmap",
                  gsrnamespace=6, gsrlimit=limit, prop="imageinfo",
                  iiprop="url|size|mime|extmetadata", iiurlwidth=2000,
                  iiextmetadatafilter="LicenseShortName|LicenseUrl|Artist|ImageDescription|DateTimeOriginal")
    d = get(API + "?" + urllib.parse.urlencode(params))
    out = []
    for p in (d.get("query", {}).get("pages", {}) or {}).values():
        ii = (p.get("imageinfo") or [{}])[0]
        md = ii.get("extmetadata", {})
        lic = strip(md.get("LicenseShortName", {}).get("value"))
        out.append(dict(title=p["title"], index=p.get("index", 99), w=ii.get("width"), h=ii.get("height"), mime=ii.get("mime"),
                        thumb=ii.get("thumburl") or ii.get("url"), page=ii.get("descriptionurl"), license=lic,
                        licenseUrl=strip(md.get("LicenseUrl", {}).get("value")), author=strip(md.get("Artist", {}).get("value")),
                        desc=strip(md.get("ImageDescription", {}).get("value"))[:300]))
    return out


def fetch(ids):
    from PIL import Image, ImageDraw, ImageOps
    photos = json.load(open(PHOTOS))
    for p in photos:
        if ids and p["id"] not in ids:
            continue
        seen, cands = set(), []
        for q in [p["query"]] + EXTRA.get(p["id"], []):
            for c in sorted(search(q), key=lambda c: c["index"]):
                if c["title"] in seen or c["mime"] not in ("image/jpeg", "image/png"):
                    continue
                if not c["w"] or max(c["w"], c["h"]) < 1400 or not FREE.search(c["license"]) or NONFREE.search(c["license"]):
                    continue
                seen.add(c["title"]); cands.append(c)
        cands = cands[:9]
        d = os.path.join(CAND, p["id"]); os.makedirs(d, exist_ok=True)
        tiles = []
        for i, c in enumerate(cands):
            fn = os.path.join(d, f"{i:02d}.jpg")
            if not os.path.exists(fn):
                open(fn, "wb").write(get(c["thumb"], binary=True))
            c["file"] = os.path.relpath(fn, ROOT)
            im = ImageOps.exif_transpose(Image.open(fn)).convert("RGB"); im.thumbnail((420, 300))
            tile = Image.new("RGB", (430, 340), "white"); tile.paste(im, (5, 5))
            ImageDraw.Draw(tile).text((8, 310), f"{i:02d} {c['w']}x{c['h']} {c['license']}"[:60], fill="black")
            tiles.append(tile)
        json.dump(cands, open(os.path.join(d, "candidates.json"), "w"), indent=1, ensure_ascii=False)
        if tiles:
            sheet = Image.new("RGB", (430 * 3, 340 * ((len(tiles) + 2) // 3)), "white")
            for i, t in enumerate(tiles):
                sheet.paste(t, ((i % 3) * 430, (i // 3) * 340))
            sheet.save(os.path.join(d, "sheet.jpg"), quality=85)
        print(f"{p['id']:20s} {len(cands)} candidates")


def pick(pid, n, label=None, focus=None, note=None):
    from PIL import Image, ImageOps
    photos = json.load(open(PHOTOS))
    p = next(x for x in photos if x["id"] == pid)
    c = json.load(open(os.path.join(CAND, pid, "candidates.json")))[int(n)]
    im = ImageOps.exif_transpose(Image.open(os.path.join(ROOT, c["file"]))).convert("RGB")
    im.thumbnail((1800, 1800), Image.LANCZOS)
    out = os.path.join("assets", "photos", f"{pid}.jpg")
    im.save(os.path.join(ROOT, out), quality=90, optimize=True)
    p.update(file=out, w=im.width, h=im.height, author=c["author"] or "unknown", license=c["license"], licenseUrl=c["licenseUrl"],
             source=c["page"], commonsTitle=c["title"])
    if label: p["label"] = label
    if focus: p["focus"] = [float(v) for v in focus.split(",")]
    if note: p["note"] = note
    json.dump(photos, open(PHOTOS, "w"), indent=1, ensure_ascii=False)
    print(pid, "->", out, im.size, c["license"], c["author"])


def credits():
    photos = json.load(open(PHOTOS))
    L = ["# Credits", "", "## Map data", "", "- Natural Earth 10m (admin 0 countries, admin 1 provinces, populated places, bathymetry 200/1000/3000 m). Public domain. https://www.naturalearthdata.com/ (via github.com/nvkelso/natural-earth-vector)",
         "- Destination anchors: Natural Earth populated places (city points). Bali anchor: centroid of the main Bali island polygon (Natural Earth 10m), used as a regional anchor, not a landmark position.",
         "- Lines between destinations show the order of the video, not travel routes.", "", "## Photographs (Wikimedia Commons)", "",
         "| Destination | Landmark (on-screen label) | File | Author | Licence |", "|---|---|---|---|---|"]
    for p in photos:
        if p.get("file"):
            L.append(f"| {p['city']} | {p['label']} | [{p.get('commonsTitle', p['file'])}]({p['source']}) | {p['author']} | [{p['license']}]({p['licenseUrl']}) |")
        else:
            L.append(f"| {p['city']} | {p['label']} | NOT YET DOWNLOADED | - | - |")
    L += ["", "Photos were resized and cropped inside frames; no other changes. CC BY-SA photos remain under their licence.", "",
          "## Fonts", "", "- Montserrat (SIL Open Font License 1.1), via @fontsource/montserrat 5.3.0.", "", "## Sound", "", "- See assets/sfx/CREDITS.md if sound effects are included."]
    open(os.path.join(ROOT, "CREDITS.md"), "w").write("\n".join(L) + "\n")
    print("CREDITS.md written")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(0)
    if a[0] == "fetch":
        fetch(set(a[1:]))
    elif a[0] == "pick":
        kw = {}
        for flag in ("--label", "--focus", "--note"):
            if flag in a:
                i = a.index(flag); kw[flag[2:]] = a[i + 1]; del a[i:i + 2]
        pick(a[1], a[2], **kw)
    elif a[0] == "credits":
        credits()

# Make web-sized copies of files/favourite_photos for the home page cover.
# Originals are left untouched; copies go to images/photos/cover/.
# Run after adding a photo:  python3 make_cover_photos.py

from pathlib import Path

from PIL import Image, ImageOps

SRC = Path(__file__).parent / "files" / "favourite_photos"
DST = Path(__file__).parent / "images" / "photos" / "cover"
MAX_WIDTH = 2000
QUALITY = 80

DST.mkdir(parents=True, exist_ok=True)
for src in sorted(SRC.iterdir()):
    if src.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
        continue
    dst = DST / (src.stem + ".jpg")
    if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
        continue
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        if im.width > MAX_WIDTH:
            im = im.resize((MAX_WIDTH, round(im.height * MAX_WIDTH / im.width)), Image.LANCZOS)
        im.save(dst, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    print(f"{src.name} -> {dst.relative_to(Path(__file__).parent)} ({dst.stat().st_size // 1024} KB)")

"""Render readme-aura blocks to a PNG contact sheet for visual review.
The README uses animated SVGs; this PNG is a static QA artifact.
"""
from pathlib import Path
from io import BytesIO
import re
import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "README.md"
ASSETS = ROOT / ".github" / "assets"
OUTPUT = ROOT / "assets" / "portfolio-preview.png"
text = SOURCE.read_text(encoding="utf-8")
images = []
for index in range(11):
    match = re.search(rf"readme-aura-component-{index}-[a-f0-9]+\.svg", text)
    if not match:
        raise RuntimeError(f"Block {index} is missing from README")
    source = ASSETS / match.group(0)
    png = cairosvg.svg2png(url=str(source))
    images.append(Image.open(BytesIO(png)).convert("RGB"))

rows = [[0], [1], [2], [3, 4, 5], [6, 7], [8, 9], [10]]
W, PAD, GAP = 860, 15, 13
height = PAD * 2 + sum(max(images[i].height for i in row) for row in rows) + GAP * (len(rows) - 1)
out = Image.new("RGB", (W, height), "#080b11")
y = PAD
for row in rows:
    row_width = sum(images[i].width for i in row) + GAP * (len(row) - 1)
    x = (W - row_width) // 2
    for i in row:
        out.paste(images[i], (x, y))
        x += images[i].width + GAP
    y += max(images[i].height for i in row) + GAP

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
out.save(OUTPUT, optimize=True)
print(f"Saved {OUTPUT.relative_to(ROOT)} {W}x{height}")

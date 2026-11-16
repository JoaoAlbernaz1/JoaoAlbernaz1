"""Render readme-aura SVG blocks into a deterministic static preview.

Only visual QA assets. The README continues to use animated SVGs.
"""
from pathlib import Path
from io import BytesIO
import glob
import re
import cairosvg
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / ".github" / "assets"
DEST = ROOT / "assets" / "portfolio-preview.png"

blocks = []
readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
for idx in range(11):
    match = re.search(rf"readme-aura-component-{idx}-[a-f0-9]+\.svg", readme_text)
    if match is None:
        raise RuntimeError(f"README is missing generated SVG for block {idx}")
    raw = (ASSETS / match.group(0)).read_bytes()
    png = cairosvg.svg2png(bytestring=raw)
    blocks.append(Image.open(BytesIO(png)).convert("RGBA"))

width = 1000
spacing = 9
ordered_rows = [
    (0,), (1,), (2,), (3,), (4,), (5, 6), (7, 8), (9,), (10,)
]
total_height = 24 + sum(max(blocks[i].height for i in row) for row in ordered_rows) + spacing * (len(ordered_rows) - 1) + 24
canvas = Image.new("RGB", (width, total_height), "#000000")
y = 24
for row in ordered_rows:
    x = 0 if len(row) == 1 else 9
    for i in row:
        part = blocks[i]
        if len(row) == 1 and part.width != width:
            part.thumbnail((width, part.height))
        canvas.paste(part.convert("RGB"), (x, y))
        x += part.width + 10
    y += max(blocks[i].height for i in row) + spacing

DEST.parent.mkdir(exist_ok=True, parents=True)
canvas.save(DEST, optimize=True)
print(f"Built {DEST.relative_to(ROOT)} {canvas.width}x{canvas.height} ({DEST.stat().st_size} bytes)")

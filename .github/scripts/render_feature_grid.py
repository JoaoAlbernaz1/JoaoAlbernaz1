"""Render the profile feature cards as an animated GIF and a PNG fallback.

The SVG remains the editable source of truth. The GIF avoids limitations
of GitHub's SVG sanitization while keeping animation lightweight.
"""
from pathlib import Path
from io import BytesIO
import math
import cairosvg
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"
SVG = ASSETS / "feature-grid-chrome.svg"
PNG = ASSETS / "feature-grid-chrome.png"
GIF = ASSETS / "feature-grid-chrome.gif"

png_bytes = cairosvg.svg2png(url=str(SVG), output_width=1200, output_height=738)
source = Image.open(BytesIO(png_bytes)).convert("RGBA")
width, height = source.size

# A faded detail from the original angelic profile banner ties the
# capability cards to the overall metallic visual identity.
banner = ASSETS / "banner-github-anjo-flow.gif"
if banner.exists():
    try:
        angel = Image.open(banner).convert("RGB")
        crop_width = max(1, min(angel.width // 3, 300))
        angel = angel.crop((0, 0, crop_width, angel.height)).resize((285, 345), Image.Resampling.LANCZOS)
        angel = angel.convert("RGBA")
        mask = Image.new("L", angel.size)
        pixels = mask.load()
        for y in range(angel.height):
            for x in range(angel.width):
                fade_x = max(0.0, min(1, (angel.width - x) / 130))
                fade_y = max(0.0, min(1, (angel.height - y) / 165))
                pixels[x, y] = int(43 * fade_x * fade_y)
        angel.putalpha(mask)
        # Draw behind the cards, visible in the top-left introduction.
        backdrop = Image.new("RGBA", source.size, (0, 0, 0, 0))
        backdrop.alpha_composite(angel, (0, 0))
        source = Image.alpha_composite(backdrop, source)
    except (OSError, ValueError):
        pass

# Static readable fallback.
source.convert("RGB").save(PNG, optimize=True)

frames = []
count = 18
for i in range(count):
    phase = i / count
    frame = source.copy()
    sheen = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(sheen)
    # Moving soft spotlight: analogous to the pointer-follow glow in
    # Hirael's React component, but independent of browser JavaScript.
    xx = int(-90 + phase * (width + 180))
    draw.ellipse((xx - 170, 105, xx + 170, 510), fill=(162, 185, 214, 16))
    sheen = sheen.filter(ImageFilter.GaussianBlur(44))
    frame = Image.alpha_composite(frame, sheen)

    details = ImageDraw.Draw(frame)
    for j in range(6):
        x = 32 + (j % 3) * 390
        y = 206 + (j // 3) * 236
        p = (phase + j * 0.11) % 1
        gx = int(x + 20 + p * 276)
        alpha = int(48 + 95 * max(0, 1 - abs(p - 0.5) * 2))
        details.line((gx, y + 3, gx + 30, y + 3), fill=(234, 242, 250, alpha), width=2)

    frames.append(frame.convert("RGB"))

# Use a shared palette so letters and outlines do not flicker between frames.
master = frames[0].quantize(colors=144, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
quantized = [f.quantize(palette=master, dither=Image.Dither.NONE) for f in frames]
quantized[0].save(
    GIF, save_all=True, append_images=quantized[1:],
    duration=125, loop=0, disposal=2, optimize=True
)
print(f"Created {PNG} ({PNG.stat().st_size} bytes)")
print(f"Created {GIF} ({GIF.stat().st_size} bytes)")

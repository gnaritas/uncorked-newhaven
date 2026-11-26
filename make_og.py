#!/usr/bin/env python3
"""make_og.py — og.png 1200x630 for Uncorked Wine Bar demo host (t_69ac5b0e).
Flight-board share plate: amber kicker + rows on near-black, cream serif headline,
cork rule. Header-line width guards live (jeyas 2026-11-25 lesson: shorten the line,
never shrink tracking below 4)."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "public", "og.png")

W, H = 1200, 630
BOARD = (23, 19, 15)       # --board
AMBER = (232, 180, 76)     # --amber
AMBER_LT = (240, 198, 116)
CREAM = (242, 235, 221)
WINE = (140, 42, 68)       # --wine
CORK = (196, 161, 107)
MUTED = (141, 132, 116)

def F(size, bold=False, italic=False):
    cands = []
    if bold:
        cands += ["/System/Library/Fonts/Supplemental/Iowan Old Style Bold.ttf",
                  "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"]
    elif italic:
        cands += ["/System/Library/Fonts/Supplemental/Iowan Old Style Italic.ttf",
                  "/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf"]
    cands += ["/System/Library/Fonts/Supplemental/Iowan Old Style Roman.ttf",
              "/System/Library/Fonts/Supplemental/Times New Roman.ttf"]
    for c in cands:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except OSError:
                continue
    return ImageFont.load_default()

def MONO(size):
    for c in ["/System/Library/Fonts/Menlo.ttc", "/System/Library/Fonts/Monaco.ttf"]:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except OSError:
                continue
    return ImageFont.load_default()

def tracked_width(draw, text, font, tracking):
    total = 0
    for ch in text:
        total += draw.textlength(ch, font=font) + tracking
    return total - tracking

def center(draw, y, text, font, fill, tracking=0):
    tw = tracked_width(draw, text, font, tracking)
    x = (W - tw) // 2
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking
    return tw

os.makedirs(os.path.join(HERE, "public"), exist_ok=True)
img = Image.new("RGB", (W, H), BOARD)
d = ImageDraw.Draw(img)

# amber top strip + hairline frame (departure-sign motif)
d.rectangle((0, 0, W - 1, 7), fill=AMBER)
d.rectangle((24, 24, W - 25, H - 25), outline=(52, 48, 42), width=1)

hdr = "NEW WINE BAR \u00b7 975 STATE STREET \u00b7 NEW HAVEN, CT"
w = tracked_width(d, hdr, MONO(22), 8)
assert w <= 1088, "header line renders %dpx > 1088 (shorten line, keep tracking>=4)" % w
center(d, 64, hdr, MONO(22), AMBER, 8)

h1 = F(84, bold=True)
l1 = "The whole world,"
w1 = tracked_width(d, l1, h1, 0)
assert w1 <= 1120, "h1 line renders %dpx" % w1
center(d, 120, l1, h1, (255, 248, 238), 0)

l2 = "poured by the glass."
w2 = tracked_width(d, l2, h1, 0)
assert w2 <= 1120, "h1 line renders %dpx" % w2
center(d, 224, l2, h1, (255, 248, 238), 0)

d.rectangle((W // 2 - 150, 336, W // 2 + 150, 337), fill=WINE)
d.rectangle((W // 2 - 150, 341, W // 2 + 150, 342), fill=CORK)

r1 = "75 TO 80 WINES \u00b7 TEN WHITES AND TEN REDS BY THE GLASS"
w = tracked_width(d, r1, MONO(23), 6)
assert w <= 1100, "row1 renders %dpx" % w
center(d, 372, r1, MONO(23), AMBER_LT, 6)

r2 = "SMALL PLATES UNTIL LATE \u00b7 EVERY NIGHT OF THE WEEK"
w = tracked_width(d, r2, MONO(23), 6)
assert w <= 1100, "row2 renders %dpx" % w
center(d, 410, r2, MONO(23), CREAM, 6)

f1 = "EST. NOVEMBER 2026 \u00b7 FROM THE OWNERS OF BLUE TORTUGA"
w = tracked_width(d, f1, MONO(20), 6)
assert w <= 1100, "foot renders %dpx" % w
center(d, 500, f1, MONO(20), MUTED, 6)

img.save(OUT, "PNG")
print("wrote %s %s 1200x630 og: image done" % (OUT, os.path.getsize(OUT)))

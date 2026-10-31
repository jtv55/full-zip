"""Draws og.png, the 1200x630 link-preview image. Run: python make_og.py"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG, FG, ACC = (246, 243, 238), (29, 27, 24), (180, 68, 31)
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
serif = "C:/Windows/Fonts/georgiab.ttf"
sans = "C:/Windows/Fonts/segoeui.ttf"

# zipper down the right side
x0 = 960
for y in range(0, H, 14):
    d.rectangle([x0 - 6, y, x0 + 6, y + 7], fill=(60, 56, 50))
d.rounded_rectangle([x0 - 22, 90, x0 + 22, 190], radius=10, fill=ACC)
d.ellipse([x0 - 9, 150, x0 + 9, 168], fill=BG)

# color tiles, one per "world"
tiles = [(205, 226, 190), (226, 190, 190), (190, 190, 226), (226, 214, 180), (190, 218, 226), (214, 190, 226)]
for i, c in enumerate(tiles):
    col, row = i % 3, i // 3
    d.rounded_rectangle([x0 + 50 + col * 62, 240 + row * 100, x0 + 100 + col * 62, 320 + row * 100], radius=8, fill=c)

d.text((70, 150), "Full", font=ImageFont.truetype(serif, 190), fill=FG)
d.text((70, 330), "Zip", font=ImageFont.truetype(serif, 190), fill=ACC)
f = ImageFont.truetype(sans, 30)
d.text((70, 560), "Full-zip hoodies from brands that don't make clothes", font=f, fill=(107, 101, 92))
img.save("og.png", optimize=True)
print(img.size)

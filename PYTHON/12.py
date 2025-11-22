from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap
import os

# ---------- CONFIG ----------
OUT = "insta_story.png"
W, H = 1080, 1920

# Choose verse: "A" or "B"
VERSE_CHOICE = "A"

VERSE_A = "Aise tu lage ki gulaab hai,\nBaghon mein dil ke\nkhilke in fizaaon mein chhaye ho haaye."
VERSE_B = ("Haathon ko sambhaale mere haathon mein,\n"
           "Jab tak neend na aaye in lakeeron mein\n"
           "Baatein hon...")

VERSE = VERSE_A if VERSE_CHOICE.upper() == "A" else VERSE_B

# Font paths - adjust if necessary. If unavailable, Pillow uses default font.
# On Windows you might use: "C:/Windows/Fonts/arial.ttf"
FONT_PATH = None  # set to path string if you want a custom ttf
TITLE = "— song lyric"

# ---------- CREATE IMAGE ----------
img = Image.new("RGB", (W, H), "#111017")

# Gradient background (simple top->bottom)
top = Image.new("RGB", (W, H//2), "#2b1a3a")
bottom = Image.new("RGB", (W, H//2), "#e69dbf")
gradient = Image.new("RGB", (W, H))
gradient.paste(top, (0,0))
gradient.paste(bottom, (0,H//2))
gradient = gradient.filter(ImageFilter.GaussianBlur(18))
img.paste(gradient, (0,0))

draw = ImageDraw.Draw(img)

# Choose fonts
def load_font(size):
    try:
        if FONT_PATH and os.path.exists(FONT_PATH):
            return ImageFont.truetype(FONT_PATH, size)
        # Try common system fonts
        for f in [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/Library/Fonts/Arial.ttf",
            "C:/Windows/Fonts/arial.ttf"
        ]:
            if os.path.exists(f):
                return ImageFont.truetype(f, size)
    except Exception:
        pass
    return ImageFont.load_default()

title_font = load_font(36)
verse_font = load_font(56)

# Wrap verse text to fit width
max_text_width = int(W * 0.78)
lines = []
for paragraph in VERSE.split("\n"):
    wrapped = textwrap.wrap(paragraph, width=22)  # tune width if necessary
    if not wrapped:
        lines.append("")
    else:
        lines.extend(wrapped)

# Measure block height
line_height = verse_font.getsize("Ay")[1] + 8
block_height = line_height * len(lines)

# Positioning: center vertically a little above center
y0 = (H - block_height) // 2 - 80

# Draw translucent blurred rectangle behind text for contrast
padding = 48
rect_x0 = W*0.08
rect_x1 = W*0.92
rect_y0 = y0 - padding
rect_y1 = y0 + block_height + padding
overlay = Image.new("RGBA", (W, H), (0,0,0,0))
od = ImageDraw.Draw(overlay)
od.rounded_rectangle([rect_x0, rect_y0, rect_x1, rect_y1], radius=40, fill=(0,0,0,100))
img = Image.alpha_composite(img.convert("RGBA"), overlay)

draw = ImageDraw.Draw(img)

# Draw lines of text
x_center = W//2
y = y0
for ln in lines:
    w, h = draw.textsize(ln, font=verse_font)
    draw.text((x_center - w/2, y), ln, fill=(255,255,255), font=verse_font)
    y += line_height

# Draw title below
tw, th = draw.textsize(TITLE, font=title_font)
draw.text((x_center - tw/2, rect_y1 + 18), TITLE, fill=(255,255,255,200), font=title_font)

# Save
img.convert("RGB").save(OUT, quality=95)
print(f"Saved {OUT}")

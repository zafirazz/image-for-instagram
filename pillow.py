from PIL import Image, ImageFont, ImageDraw
import os

size = (1080, 1080)

for i in os.listdir('.'):
    if i.endswith('.png'):
        image = Image.open(i)

        cropped = image.resize(size)

        b_w_ef = cropped.convert("L")

        width, height = b_w_ef.size
        draw = ImageDraw.Draw(b_w_ef)
        text = "created by Z.I."
        font = ImageFont.truetype("Ubuntu-M.ttf", 40)
        text_w, text_h = draw.textsize(text, font)

        x = width - text_w - 10
        y = height - text_h - 15

        draw.text((x, y), text, font=font)
        f_n, f_ext = os.path.splitext(i)

        b_w_ef.save('img_edited/{}_img_edited{}'.format(f_n, f_ext))

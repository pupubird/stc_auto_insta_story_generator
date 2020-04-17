import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
TEXT_SIZE = 50
TEMPLATE_IMG = "Instagram.png"
NAME_LIST_TXT = "participants_name.txt"
FONT_TTF_FILE = "Arial.ttf"


def output_cert(title, val, line_length):
    img = Image.open(TEMPLATE_IMG)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype(FONT_TTF_FILE, TEXT_SIZE)
    # draw.text((x, y),"Sample Text",(r,g,b))
    img_width, img_height = img.size
    text_width, text_height = font.getsize(val)
    draw.text((100, (img_height/2)-(text_height*(line_length)/2)),
              val, (0, 0, 0), font=font)
    draw.text((60, 100),
              title, (171, 171, 171), font=font)
    img.save(f'output/{title}.png')
    print(f'Generated {title}')


if __name__ == "__main__":
    os.makedirs('output', exist_ok=True)
    names = []
    with open(NAME_LIST_TXT, 'r') as f:
        names = f.readlines()

    for name in names:
        name = name.replace("\n", "").replace("/", "")
        output_cert(name)

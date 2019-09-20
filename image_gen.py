#! /usr/bin/env python

import sys
from PIL import Image, ImageDraw, ImageFont

def old_main():
    args = sys.argv
    old_name = args[1]
    sizes = args[3].split('x')

    w, h = int(sizes[0]), int(sizes[1])

    new_name = 'maskable_' + old_name
    content = old_name + '\nmaskalbe'

    img = Image.new('RGB', (w, h), color = 'white')


    d = ImageDraw.Draw(img)
    d.text((0,0), content, fill='black', font=font)
    img.save(new_name)

def gen_image(filename, wh, color, text):
    img = Image.new('RGB', (wh, wh), color = color)    
    d = ImageDraw.Draw(img)
    
    f1 = ImageFont.truetype('Roboto-Regular.ttf', size=100)

    tx, ty = f1.getsize(text)
    mtxy = max(tx, ty)

    size_to_use = int(70 * wh * 1.0 / mtxy)
    f2 = ImageFont.truetype('Roboto-Regular.ttf', size=size_to_use)

    ax, ay = f2.getsize(text)
    x_empty, y_empty = wh-ax, wh-ay

    l, r = x_empty//2, y_empty//2


    d.text((l, r), text, fill='black', font=f2)

    img.save('images/' + filename+'.png')


def main():
    dp2px = {
        'mdpi' : 1,
        'hdpi': 1.5,
        'xhdpi': 2,
        'xxhdpi': 3,
        'xxxhdpi': 4,
        'splash-xxhdpi': 5,
        'splash-xxxhdpi': 6
    }

    app_dp = 48
    app = {}
    maskable_dp = 108
    maskable = {}

    for dpi, ratio in dp2px.items():
        app[dpi] = int(app_dp * ratio)
        maskable[dpi] = int(maskable_dp * ratio)

    img_data_arr = []
    for dpi, wh in app.items():
        data = []
        data.append(dpi)
        data.append(wh)
        data.append('red')
        data.append(dpi[:-3])

        img_data_arr.append(tuple(data))

    for dpi, wh in maskable.items():
        data = ('maskable-' + dpi, wh, 'blue', dpi[:-3])
        img_data_arr.append(data)

    for d in img_data_arr:

        gen_image(*d)

    

if __name__ == '__main__':
    main()
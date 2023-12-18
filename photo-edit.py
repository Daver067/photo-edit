from PIL import Image
import os
import json

def main():

    im = Image.open('pyramids.jpeg')
    print(im.format, im.size, im.mode)
    coord = (0,0)
    rgbValue = (255,255,255)
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if j < 2 or j > 955 or i < 3 or i > 1276:
                coord = (i,j)
                coord2 = (im.size[0] - 1 - i, im.size[1] - 1 - j)
                im.putpixel(coord, rgbValue)
                im.putpixel(coord2, rgbValue)
    im.save('pyramids2.jpeg')
    return

main()
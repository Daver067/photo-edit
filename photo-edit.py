from PIL import Image
import os
import json

def main():
    pathIn = './photosIn/'
    photoList = dict()
    pathOut = './photosOut/'
    count = 0
    for filename in os.listdir(pathIn):
            if filename == ".DS_Store":
                 continue
            photoList[str(count)] = filename
            count += 1
    for i in range(len(photoList)):
            currentPath = f"{pathIn}{photoList[str(i)]}"
            savePath = f"{pathOut}{photoList[str(i)]}"
            im = Image.open(currentPath)
            rgbValue = (255,255,255,1)
            for i in range(im.size[0]):
                for j in range(3):
                        coord = (i,j)
                        coord2 = (im.size[0] - 1 - i, im.size[1] - 1 - j)
                        im.putpixel(coord, rgbValue)
                        im.putpixel(coord2, rgbValue)
            for i in range(im.size[1]):
                for j in range(3):
                    coord = (j,i)
                    coord2 = (im.size[0] - 1 - j, im.size[1] - 1 - i)
                    im.putpixel(coord, rgbValue)
                    im.putpixel(coord2, rgbValue)
            im.save(savePath)
    return



main()
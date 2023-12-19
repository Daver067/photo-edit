from PIL import Image
import os
import easygui

def main():
    i = 0
    try:
        try:
            pathIn = easygui.diropenbox("Path containing photos:")
            photoList = dict()
            try:
                pathOut = os.path.realpath('./photosOut/')
            except:
                easygui.textbox("failed to path the dir")
            if 'photosOut' not in os.listdir():
                os.mkdir(pathOut)
            count = 0
        except:
            easygui.textbox("failed to do the first thing")
        try:
             
            for filename in os.listdir(pathIn):
                    if filename == ".DS_Store":
                        continue
                    photoList[str(count)] = filename
                    count += 1
        except:
            easygui.textbox("failed to do the second thing")
        try:
             
            for i in range(len(photoList)):
                    currentPath = f"{pathIn}/{photoList[str(i)]}"
                    savePath = f"{pathOut}/{photoList[str(i)]}"
                    try:
                        im = Image.open(currentPath)
                    except:
                        easygui.textbox(f"Issue opening file at {currentPath}")
                    rgbValue = (255,255,255,1)
                    while im.size[0] > 1024:
                        im = im.reduce(2)
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
                    try:
                        im.save(savePath)
                    except:
                        easygui.textbox("failed to save")
        except:
            easygui.textbox("failed to do the third thing")

        easygui.textbox(f"Your photos are at path: {pathOut}")
    except:
         easygui.textbox("failed to do stuff")
    return



main()
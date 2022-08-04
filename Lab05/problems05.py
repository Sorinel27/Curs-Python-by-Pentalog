# Fratean Sorin Problema lab 5
import PIL
import numpy as np
from numpy import array
import imageProcessor
import random
import cv2 as cv
import cv2
from PIL import Image

if __name__ == "__main__":
    print("Value for height: ")
    height = int(input())
    print("Value for lenght: ")
    length = int(input())
    picture = imageProcessor.MyImage(height, length)
    ok = 1
    for i in range(height):
        for j in range(length):
            print("Pixel " + str(ok))
            ok = ok + 1
            red = random.uniform(0, 255)
            green = random.uniform(0, 255)
            blue = random.uniform(0, 255)
            picture.getArray1()[i][j][0] = red
            picture.getArray1()[i][j][1] = green
            picture.getArray1()[i][j][2] = blue
            picture.getArray2()[i][j][0] = red
            picture.getArray2()[i][j][1] = green
            picture.getArray2()[i][j][2] = blue
            picture.getArray3()[i][j][0] = red
            picture.getArray3()[i][j][1] = green
            picture.getArray3()[i][j][2] = blue
            picture.getArray4()[i][j][0] = red
            picture.getArray4()[i][j][1] = green
            picture.getArray4()[i][j][2] = blue
    img = Image.fromarray(picture.getArray1())
    img.save('picture.png')
    print("Picture created!")
    print("Enter RGB components for elimination: ")
    r = int(input("R: "))
    g = int(input("G: "))
    b = int(input("B: "))
    img = Image.fromarray(picture.pixelElimination(r, g, b))
    img.save('pictureElimination.png')
    component = input("Choose a r, g or b component to be 0: ")
    img = Image.fromarray(picture.componentElimination(component))
    img.save('pictureComponentElimination.png')
    img = Image.fromarray(picture.colorInv())
    img.save('pictureInverted.png')
    img = Image.fromarray(picture.grayTone())
    img.save('pictureGraytone.png')
    pic = Image.open('photo.jpg')
    photo = PIL.Image.open('photo.jpg')
    pHeight, pLength = photo.size
    pixels = np.array(pic)
    photo1 = imageProcessor.MyImage(pHeight, pLength)
    for i in range(pHeight):
        for j in range(pLength):
            photo1.getArray5()[i][j] = pixels[i][j]
    img = Image.fromarray(photo1.grayTone())
    img.save('test.png')



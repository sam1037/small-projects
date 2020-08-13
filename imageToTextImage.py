from PIL import Image, ImageFilter
import sys
import os
import math

def get_images():
    if len(sys.argv) == 1:
        print("Usage: -input")
        return
    files = sys.argv[1:]
    files = [f for f in files if f in os.listdir()]
    return files   

def convert(image):
    code = "#Wo- "
    print(len(code))
    codePic = ""

    w, h = image.size
    image = image.resize((int(w*0.3), int(h*0.3*8/18)), Image.NEAREST)
    w, h = image.size

    for i in range(h):
        for j in range(w):
            avg = sum(image.getpixel((j,i)))
            avg = int(avg/3)
            codePic += code[int( (len(code)-1) * (avg/255) )]
        codePic += "\n"

    result = open("result.txt", "w")
    result.write(codePic)


image = Image.open("rgb.jpg")
convert(image)

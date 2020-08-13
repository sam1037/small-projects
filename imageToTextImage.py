from PIL import Image, ImageFilter
import sys
import os
import math

def get_images():
    if len(sys.argv) == 1:
        print("Usage: -input")
        exit()
    files = sys.argv[1:]
    files = [f for f in files if f in os.listdir()]
    for f in files:
        print(f)
    return files   

def convert(image, output_name):
    code = "#Wo- "
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

    output_name = output_name + ".txt"
    result = open(output_name, "w")
    result.write(codePic)


def main():
    images = get_images()
    print(images)
    for file in images:
        file_name, file_ext = file.split(".")
        image = Image.open(file)
        convert(image, file_name)

main()


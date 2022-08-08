import matplotlib.pyplot as plt
import numpy as np

def img2gray(image):
    lin = len(image)
    col = len(image[0])
    gray_image = np.zeros((lin,col))

    for i in range(lin):
        for j in range(col):
            gray_image[i,j] = np.mean(image[i,j])

    return gray_image


def gray2ascii(gimage):
    char_scale = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,"^`\'.  '
    lin = len(image)
    col = len(image[0])
    ascii_image = ""

    for i in range(lin):
        for j in range(col):
            ind = int(gimage[i,j]*69)
            ascii_image += char_scale[ind] + char_scale[ind]
        ascii_image += "\n"

    return ascii_image

image = plt.imread("image3.png")
gimg = img2gray(image)
aimg = gray2ascii(gimg)

f = open("teste3.txt", "w")
f.write(aimg)
f.close()

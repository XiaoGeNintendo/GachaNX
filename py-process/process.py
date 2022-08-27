from PIL import Image
import os

def tfh(it):
    s=hex(it)[2:]
    while len(s)<2:
        s="0"+s
    return s


dir=input("Dir:")

for i in os.listdir(dir):
    # print(i)
    im = Image.open(dir+"/"+i)
    pix=im.load()
    name=i[6:-4]
    print(name)
    print(name)
    print("C")
    print("Desc")
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            print(tfh(pix[i,j][2])+tfh(pix[i,j][1])+tfh(pix[i,j][0]),end="")
    print()
from PIL import Image
import os

def tfh(it):
    s=hex(it)[2:]
    while len(s)<2:
        s="0"+s
    return s


dir=input("Dir:")

for i in os.listdir(dir):
    if ".gif" in i:
        cmd=f"ffmpeg -i {dir}/{i} {dir}/{i.replace('.gif','.png')}"
        print(cmd)
        # input()
        os.system(cmd)
        os.system(f"rm {dir}/{i}")
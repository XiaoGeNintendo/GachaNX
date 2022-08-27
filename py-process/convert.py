with open("../gacha.txt",mode="r",encoding="utf-8") as f:
    ln=f.readlines()
    # print(ln)
    for i in range(0,len(ln),5):
        print(f'gachas["{ln[i].strip()}"]=newCB("{ln[i+1].strip()}","{ln[i+2].strip()}","{ln[i+3].strip()}",\n"{ln[i+4].strip()}");')
    
import os
from PIL import Image
import json
#0 255 1
def fps(it,x=128,y=64):
    l=[]
    for iy in range(y):
        for ix in range(x):
            if it[ix,iy]>150:
                if len(l)==0:
                    l.append([ix,iy,1])
                else:
                    if l[-1][1]==iy and l[-1][0]+l[-1][2]==ix:
                        l[-1][2]+=1
                    else:
                        l.append([ix,iy,1])
    return l
def image(f):
    fx=Image.open(f)
    fb=fx.convert('L')     
    it=fb.load()
    return fps(it)   

f=open("bad.data",'w')
for i in range(2190):
    ffmpeg="ffmpeg -i bad.mp4 -ss %s -f image2 -y %s" % (i/10,str(i)+".jpg")
    os.system(ffmpeg)
    file_name=str(i)+".jpg"
    lk=image(file_name)
    jsf=json.dumps(lk)
    # zz=file_name.split(".")
    os.remove(file_name)
    # with open(str(zz[0])+'.json','w') as f:
    f.write(jsf+"\n")
f.close()
from PIL import Image
import os
import sys
from os import listdir
from os.path import isfile, join
from os import walk
import glob

# take two paramter source and destination

def crop(infile,height,width):
    im = Image.open(infile)
    imgwidth, imgheight = im.size
    for i in range(imgheight//height):
        for j in range(imgwidth//width):
            box = (j*width, i*height, (j+1)*width, (i+1)*height)
            yield im.crop(box)
            

mypath=sys.argv[1]
destination = sys.argv[2]
width=height=28

start_num=1

#x = os.listdir(mypath)
#for (dirpath, dirnames, filenames) in walk(mypath):
for filenames in os.listdir(mypath):
     for k,piece in enumerate(crop(mypath+filenames,height,width),start_num):
        img=Image.new('RGB', (height,width), 255)
        img.paste(piece)
        path=os.path.join(destination,filenames+"IMG-%s.png" % k)
        img.save(path)
 #   print(filenames+"\n")


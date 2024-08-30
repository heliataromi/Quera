import sys
import os
from datetime import datetime

def scan(src,dst):
    ls = os.listdir(src)
    for obj in ls:
        if os.path.isdir(os.path.join(src,obj)):
            scan(os.path.join(src,obj),dst)
        elif os.path.isfile(os.path.join(src,obj)):
            extension = os.path.splitext(os.path.join(src,obj))[1].lower()[1:]
            year = str(datetime.fromtimestamp(os.path.getmtime(os.path.join(src,obj))).year)
            subdir = None
            if extension in photos:
                subdir = "photos"
            elif extension in videos:
                subdir = "videos"
            if not subdir==None:
                copy(os.path.join(src,obj),dst,year,subdir,obj)


def copy(src,dst,year,subdir,obj):
    folders = [dst,os.path.join(dst,year),os.path.join(dst,year,subdir)]
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)
    with open(src,"rb") as org,open(os.path.join(dst,year,subdir,obj),"wb") as cop:
        cop.write(org.read())
    print(src,sep="\n")


photos = ["jpg", "jpeg", "png","py"]
videos = ["mp4", "avi", "3gp", "mpeg", "mkv", "wmv", "mov","php"]
source = sys.argv[1]
destination = sys.argv[2]
try:
    test = int(sys.argv[3])
except:
    test = 0
scan(source,destination)

import sys
import os
import time

img_frmt = ['.jpg', '.jpeg', '.png']
vid_frmt = ['.mp4', '.avi', '.3gp', '.mpeg', '.mkv', '.wmv', '.mov']
file_path = os.getcwd()
filename, src_path, dst_path = sys.argv
#src_path = input()
os.chdir(src_path)
src_path = os.getcwd()
os.chdir(file_path)
#dst_path = input()
if (not os.path.exists(dst_path)):
    os.mkdir(dst_path)
os.chdir(dst_path)
dst_path = os.getcwd()
src_files = list(os.walk(src_path))
#for x in src_files:
#    print(x)
os.chdir(src_path)
for i in range(len(src_files)):
    for file in src_files[i][2]:
        address = src_files[i][0]
        file_full_path = os.path.join(address, file)
        mTimeSec = os.path.getmtime(file_full_path)
        year = time.strftime('%Y', time.localtime(mTimeSec))
        if (not os.path.exists(os.path.join(dst_path, year))):
            os.mkdir(os.path.join(dst_path, year))
        with open(file_full_path, 'rb') as fileo:
            file_stuff = fileo.readlines()
            if ('.' in file):
                if (file[file.rfind('.'):].lower() in img_frmt):
                    a_path = os.path.join(dst_path, year)
                    if (not os.path.exists(os.path.join(a_path, 'photos'))):
                        os.mkdir(os.path.join(a_path, 'photos'))
                    new_file_path = os.path.join(a_path, 'photos', file)
                    new_file = open(new_file_path, "wb")
                    for x in file_stuff:
                        new_file.write(x)
                    fileo.close()
                    new_file.close()
                elif(file[file.rfind('.'):].lower() in vid_frmt):
                    a_path = os.path.join(dst_path, year)
                    if (not os.path.exists(os.path.join(a_path, 'videos'))):
                        os.mkdir(os.path.join(a_path, 'videos'))
                    new_file_path = os.path.join(a_path, 'videos', file)
                    new_file = open(new_file_path, "wb")
                    for x in file_stuff:
                        new_file.write(x)
                    fileo.close()
                    new_file.close()

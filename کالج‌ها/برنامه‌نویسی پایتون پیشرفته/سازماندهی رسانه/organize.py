import sys
import os
import time


def copy_file(source_path, destination_path):
    with open(source_path, 'rb') as source_file:
        data = source_file.read()

    with open(destination_path, 'wb') as destination_file:
        destination_file.write(data)

def check_directory_existence(path):
    if not os.path.exists(path):
        os.makedirs(path)


IMAGE_FORMATS = ('jpg', 'jpeg', 'png')
VIDEO_FORMATS = ('mp4', 'avi', '3gp', 'mpeg', 'mkv', 'wmv', 'mov')

inputs = sys.argv
source = inputs[1]
destination = inputs[2]

check_directory_existence(destination)

for root, dirs, files in os.walk(source):
    for file in files:
        base_name, extension = os.path.splitext(file)
        file_ext = extension.lstrip('.')

        source_file_path = os.path.join(root, file)

        year = time.ctime(os.path.getmtime(source_file_path)).split()[-1]
        year_path = os.path.join(destination, year)

        if file_ext.lower() in IMAGE_FORMATS:
            check_directory_existence(year_path)

            photos_path = os.path.join(year_path, 'photos')
            check_directory_existence(photos_path)

            destination_file_path = os.path.join(photos_path, file)
            copy_file(source_file_path, destination_file_path)

        if file_ext.lower() in VIDEO_FORMATS:
            check_directory_existence(year_path)

            videos_path = os.path.join(year_path, 'videos')
            check_directory_existence(videos_path)

            destination_file_path = os.path.join(videos_path, file)
            copy_file(source_file_path, destination_file_path)

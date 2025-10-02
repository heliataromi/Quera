import os
from uuid import uuid4
from shutil import copyfile


class FileManager:
    deleted_files = []

    def find(self, name, address):
        found_files = []

        for root, dirs, files in os.walk(address):
            for file in files:
                if file == name:
                    found_files.append(os.path.join(root, file))

        return found_files

    def create_file(self, name, address):
        path = os.path.join(address, name)
        if not os.path.exists(path):
            file = open(path, 'w')
            file.close()

    def create_dir(self, name, address):
        path = os.path.join(address, name)
        if not os.path.exists(path):
            os.mkdir(path)

    def delete(self, name, address):
        if not os.path.exists('trash'):
            os.mkdir('trash')

        old_path = os.path.join(address, name)
        if os.path.exists(old_path):
            new_path = os.path.join('trash', str(uuid4()))
            copyfile(old_path, new_path)
            FileManager.deleted_files.insert(0, (name, old_path, new_path))
            os.remove(old_path)

    def restore(self, name):
        for original_name, old_path, new_path in FileManager.deleted_files:
            if original_name == name:
                copyfile(new_path, old_path)
                os.remove(new_path)
                FileManager.deleted_files.remove((original_name, old_path, new_path))
                break

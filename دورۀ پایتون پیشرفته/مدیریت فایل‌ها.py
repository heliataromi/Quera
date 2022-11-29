import os
from shutil import copyfile


class FileManager:
    def find(self, name, address):
        os.walk(address)

    def create_file(self, name, address):
        with open(os.path.join(address, name), 'w'):
            pass

    def create_dir(self, name, address):
        try:
            os.mkdir(os.path.join(address, name))
        except FileExistsError:
            pass

    def delete(self, name, address):
        try:
            os.remove(os.path.join(address, name))
        except FileNotFoundError:
            pass

    def restore(self, name):
        pass


fm = FileManager()
fm.create_dir('test', '.')
fm.create_dir('test1', 'test')
fm.create_dir('test2', 'test/test1/')

fm.create_file('test.txt', 'test')
fm.create_file('test.txt', 'test/test1')
fm.create_file('test.txt', 'test/test1/test2')

fm.delete('tes.txt', 'test')
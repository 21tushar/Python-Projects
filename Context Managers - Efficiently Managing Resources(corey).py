# class Open_File():
#
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with Open_File('sample.txt', 'w') as f:
#     f.write('I\'m very much interested in machine learning')
#
# print(f.closed)


# from contextlib import contextmanager


# @contextmanager
# def open_file(file,mode):
#     try:
#         f = open(file, mode)
#         yield f
#     finally:
#         f.close()
#
#
# with open_file('sample.txt', 'w') as f:
#     f.write('Game development is billion dollar industry')
#
# print(f.closed)


from contextlib import contextmanager
import os


# cwd = os.getcwd()
# os.chdir('/root/Python Projects/Sample-Dir-One')
# print(os.listdir())
# os.chdir(cwd)
#
# cwd = os.getcwd()
# os.chdir('/root/Python Projects/Sample-Dir-Two')
# print(os.listdir())
# os.chdir(cwd)


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('/root/Python Projects/Sample-Dir-One'):
    print(os.listdir())

with change_dir('/root/Python Projects/Sample-Dir-Two'):
    print(os.listdir())
import os

dir1 = os.getcwd()
print(dir1)

os.mkdir('newdir')

import time

time.sleep(5)

os.rename('newdir', 'newdir1')
time.sleep(5)

os.rmdir('newdir1')
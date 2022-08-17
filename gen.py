# make directory called test
from genericpath import isdir
import os


if not isdir('test'):
    os.makedirs('test')


for i in range(100):
    with open("test/{}.txt".format(i), 'w') as f:
        f.write(str(i))
        f.close()
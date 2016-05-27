import os

dir = '/home/logic/Documents/data'

for f in os.listdir(dir):
    if f.endswith(".old"):
        print f[:-4]
        x = f[:-4]
        if x != f:
            old = dir + '/' + f
            new = dir + '/' + x
            print old
            print new
            os.rename(old, new)
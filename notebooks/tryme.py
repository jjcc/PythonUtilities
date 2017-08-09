# !/usr/bin/python

import os
import numpy as np


def walk_dir( dir_name ):
    for root, dirs, files in os.walk(dir_name, topdown=True):
        print "inside files"
        for name in files:
            print os.path.join(root, name)
        print "inside dirs"
        for name in dirs:
            print os.path.join(root, name)



if  __name__ == "__main__":
    #print walk_dir("D:\\jchen")
    X = np.linspace(1,10,10)#np.linspace(-3, 3, 100)
    Xs = X[1:] - X[:-1]
    print X
    print X[ :10]


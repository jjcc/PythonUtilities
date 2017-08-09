#%%
import numpy as np
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0])
#print data
print data.values
print data[1:3]

#%%
def myfun():
    print "myfun"

myfun()
#%%

import os

def walk_dir( dir_name ):
    for root, dirs, files in os.walk(dir_name, topdown=True):
        print "inside files"
        for name in files:
            print os.path.join(root, name)
        print "inside dirs"
        for name in dirs:
            print os.path.join(root, name)

walk_dir("..")

#%%
import numpy as np
import matplotlib.pyplot as plt
def plot_slope(X, Y):
    Xs = X[1:] - X[:-1]
    Ys = Y[1:] - Y[:-1]
    plt.plot(X[1:], Ys / Xs)

X = np.linspace(-3, 3, 100)
Y = np.exp(-X ** 2)
plt.plot(X, Y)
plot_slope(X, Y)
plt.show()
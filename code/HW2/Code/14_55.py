# -- coding: utf-8 --
from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import pylab

df = pd.io.parsers.read_csv("gasvapor.txt")
cols = list(df)
for i in range(len(cols) - 1):
    for j in range(i+1, len(cols)):
        x = cols[i]
        y = cols[j]
        df.plot(x = x, y = y, style='o')
        plt.xlabel(x)
        plt.ylabel(y)
        pylab.savefig("%s_%s.png" %(x,y))
        # plt.show()

console = []

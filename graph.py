# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    data = pd.read_csv("2.csv", header=None)

    xs = data[0].tolist()
    ys = data[1].tolist()

    newX = [float(x.replace(",", ".")) for x in xs]
    newY = [float(y.replace(",", ".")) for y in ys]

    plt.plot(newY, newX, "-", lw=2)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    plt.show()

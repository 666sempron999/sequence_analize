# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
from numpy import array

from scipy.misc import electrocardiogram
from scipy.signal import find_peaks

def print_value(nValue):
    for i in range(0, len(nValue)):
        print(nValue[i])


if __name__ == '__main__':
    
    fig = plt.figure()
    g1 = 211
    g2 = 212

    data = pd.read_csv("2_otrits.csv", header=None)

    xs = data[0].tolist()
    ys = data[1].tolist()

    newX = [float(x.replace(",", ".")) for x in xs]
    newY = [float(y.replace(",", ".")) for y in ys]

    ax1 = fig.add_subplot(g1)
    ax1.set_title("С параметром")

    ax1.plot(newY, newX, "-", lw=2)

    # ax1.xlabel("X")
    # ax1.ylabel("Y")
    # ax1.grid(True)

    # plt.show()

    x = array(newX)
    # print("New tyoe of data is {}".format(type(x)))

    peaks, properties = find_peaks(x, width=1)
    properties["prominences"], properties["widths"]

    ax2 = fig.add_subplot(g2)
    ax2.set_title("Без параметра")

    ax2.plot(x)
    ax2.plot(peaks, x[peaks], "x")
    ax2.vlines(x=peaks, ymin=x[peaks] - properties["prominences"],
               ymax = x[peaks], color = "C1")
    ax2.hlines(y=properties["width_heights"], xmin=properties["left_ips"],
               xmax=properties["right_ips"], color = "C1")


    plt.show()

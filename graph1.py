# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
from numpy import array

from scipy.misc import electrocardiogram
from scipy.signal import find_peaks

def print_value(nValue):
    """
    """
    for i in range(0, len(nValue)):
        print(nValue[i])


def show_graphic(signalData, timeData):
    """
    """
    fig = plt.figure()
    g1 = 211
    g2 = 212

    ax1 = fig.add_subplot(g1)
    # ax2 = ax1.twiny()
    # ax2.set_ylim(0, 450)



    ax1.set_title("Оригинал")
    ax1.plot(timeData, signalData, "-", lw=2)
    # ax1.set_xlim(xmin=0)

    axn = ax1.twiny()
    axn.plot(timeData, signalData, "-", lw=2)
    axn.set_xlim(0, len(signalData))

    ax1.grid(True)
    
    #
    positivePeaks, positiveProperties = find_peaks(signalData, width=1)
    #
    negativePeaks, negativeProperties = find_peaks(-signalData, width=1)
    #
    ax2 = fig.add_subplot(g2)
    ax2.set_title("Информационная составляющая")
    ax2.plot(signalData)

    ax2.plot(x, "k")
    ax2.set_xlim(0, len(timeData))
    ax2.plot(positivePeaks, x[positivePeaks], "rx")
    ax2.plot(negativePeaks, x[negativePeaks], "bx")

    ax2.grid(True)

    ax2.vlines(x=positivePeaks, ymin=x[positivePeaks] - positiveProperties["prominences"],
               ymax = x[positivePeaks], color = "C1")

    ax2.hlines(y=positiveProperties["width_heights"], xmin=positiveProperties["left_ips"],
               xmax=positiveProperties["right_ips"], color = "C1")

    ax2.vlines(x=negativePeaks, ymin=x[negativePeaks] + negativeProperties["prominences"],
               ymax = x[negativePeaks], color = "C2")

    ax2.hlines(y=-negativeProperties["width_heights"], xmin=negativeProperties["left_ips"],
               xmax=negativeProperties["right_ips"], color = "C2")
    plt.tight_layout()
    plt.show()

    return positivePeaks, positiveProperties, negativePeaks, negativeProperties



if __name__ == '__main__':
    
    # fig = plt.figure()
    # g1 = 211
    # g2 = 212

    data = pd.read_csv("2_otrits.csv", header=None)

    xs = data[0].tolist()
    ys = data[1].tolist()

    newX = [float(x.replace(",", ".")) for x in xs]
    newY = [float(y.replace(",", ".")) for y in ys]


    # ax1 = fig.add_subplot(g1)
    # ax1.set_title("С параметром")

    # ax1.plot(newY, newX, "-", lw=2)

    # # ax1.xlabel("X")
    # # ax1.ylabel("Y")
    # # ax1.grid(True)

    # # plt.show()
    print("Обнаружено {} значений".format(len(newX)))
    border = int(input("Введие длинну границы от 0 до {} - ".format(len(newX))))
    x = array(newX[0:border])
    y = array(newY[0:border])
    # # print("New tyoe of data is {}".format(type(x)))

    # peaks, properties = find_peaks(x, width=1)
    # properties["prominences"], properties["widths"]

    # ax2 = fig.add_subplot(g2)
    # ax2.set_title("Без параметра")

    # ax2.plot(x)
    # ax2.plot(peaks, x[peaks], "x")
    # ax2.vlines(x=peaks, ymin=x[peaks] - properties["prominences"],
    #            ymax = x[peaks], color = "C1")
    # ax2.hlines(y=properties["width_heights"], xmin=properties["left_ips"],
    #            xmax=properties["right_ips"], color = "C1")


    # plt.show()



    positivePeaks, positiveProperties, negativePeaks, negativeProperties = show_graphic(x, y)

    print(positivePeaks)
    print_value(positiveProperties.get("widths"))

import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks


def print_value(nValue):
    """
    """
    for i in range(0, len(nValue)):
        print(nValue[i])


def show_graphic(signalData):
    """
    """
    #
    positivePeaks, positiveProperties = find_peaks(signalData, width=1)
    #
    negativePeaks, negativeProperties = find_peaks(-signalData, width=1)
    #
    fig = plt.figure(0)
    fig.canvas.set_window_title("Анализ графиков на минимум и максимум")
    plt.plot(x, "k",  linewidth=2, label = "График кардиограмы")
    plt.plot(positivePeaks, x[positivePeaks], "rx", label = "Локальный максимум")
    plt.plot(negativePeaks, x[negativePeaks], "bx", label = "Локальный минимум")

    plt.vlines(x=positivePeaks, ymin=x[positivePeaks] - positiveProperties["prominences"],
               ymax = x[positivePeaks], color = "C1", label = "Высота и ширина выпуклой функции")

    plt.hlines(y=positiveProperties["width_heights"], xmin=positiveProperties["left_ips"],
               xmax=positiveProperties["right_ips"], color = "C1")

    plt.vlines(x=negativePeaks, ymin=x[negativePeaks] + negativeProperties["prominences"],
               ymax = x[negativePeaks], color = "C2", label = "Высота и ширина вогнутой функции")

    plt.hlines(y=-negativeProperties["width_heights"], xmin=negativeProperties["left_ips"],
               xmax=negativeProperties["right_ips"], color = "C2")
    
    plt.tight_layout()

    plt.legend() 
    plt.show()

    return positivePeaks, positiveProperties, negativePeaks, negativeProperties
    
###############################################################


if __name__ == "__main__":


    x = electrocardiogram()[0:300]

    positivePeaks, positiveProperties, negativePeaks, negativeProperties = show_graphic(x)

    # print("widths positive")
    # print_value(positiveProperties.get("widths"))
    
    # print("=====================================")

    # print("Heigt positive")
    # print_value(positiveProperties.get("prominences"))
    # print("=====================================")
    # print("=====================================")
    # print("=====================================")

    # print("widths negative")

    # print_value(negativeProperties.get("widths"))
    # print("=====================================")
    # print("height positive")
    # print_value(negativeProperties.get("prominences"))

    print(len(positivePeaks))
    print(type(positiveProperties))
    print(positiveProperties.keys())

    # print(negativePeaks)
    print(len(positiveProperties.get("widths")))
    # right = positiveProperties.get("left_ips")
    # left = positiveProperties.get("right_ips")

    right = positiveProperties.get("right_ips")
    left = positiveProperties.get("left_ips")

    # up = positiveProperties.get("prominences")
    # down = positiveProperties.get("right_bases")

    for i in range(0, len(right)):
        print(left[i],"-", right[i])
        print("----------------------------------")

    positivePeaks, positiveProperties, negativePeaks, negativeProperties = show_graphic(x)

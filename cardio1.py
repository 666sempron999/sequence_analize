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
    plt.plot(x, "k")
    plt.plot(positivePeaks, x[positivePeaks], "rx")
    plt.plot(negativePeaks, x[negativePeaks], "bx")

    plt.vlines(x=positivePeaks, ymin=x[positivePeaks] - positiveProperties["prominences"],
               ymax = x[positivePeaks], color = "C1")

    plt.hlines(y=positiveProperties["width_heights"], xmin=positiveProperties["left_ips"],
               xmax=positiveProperties["right_ips"], color = "C1")

    plt.vlines(x=negativePeaks, ymin=x[negativePeaks] + negativeProperties["prominences"],
               ymax = x[negativePeaks], color = "C2")

    plt.hlines(y=-negativeProperties["width_heights"], xmin=negativeProperties["left_ips"],
               xmax=negativeProperties["right_ips"], color = "C2")

    plt.show()

    return positivePeaks, positiveProperties, negativePeaks, negativeProperties
    
###############################################################

x = electrocardiogram()[17900:18000]

positivePeaks, positiveProperties, negativePeaks, negativeProperties = show_graphic(x)

print("widths positive")
print_value(positiveProperties.get("widths"))
 
print("=====================================")

print("Heigt positive")
print_value(positiveProperties.get("prominences"))
print("=====================================")
print("=====================================")
print("=====================================")

print("widths negative")

print_value(negativeProperties.get("widths"))
print("=====================================")
print("height positive")
print_value(negativeProperties.get("prominences"))

print(positivePeaks)
print(negativePeaks)

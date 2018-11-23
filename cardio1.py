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
    # Получение положительных пиков и их параметров 
    positivePeaks, positiveProperties = find_peaks(signalData, width=1)

    #Получение отрицательных пиков и их параметров
    negativePeaks, negativeProperties = find_peaks(-signalData, width=1)

    # Определение заголовка окна рабочей области
    fig = plt.figure(0)
    fig.canvas.set_window_title("Анализ графиков на минимум и максимум")

    # Параметры для первой части графика
    plt.subplot(211).set_title("Анализ на максимумы")
    plt.grid(True, which="major", color="k", linestyle="dashed", alpha=0.5)
    plt.plot(x, "k",  linewidth=2, label = "График кардиограмы")
    plt.plot(positivePeaks, x[positivePeaks], "rx", label = "Локальный максимум")

    plt.vlines(x=positivePeaks, ymin=x[positivePeaks] - positiveProperties["prominences"],
               ymax = x[positivePeaks], color = "C1", label = "Высота и ширина выпуклой функции")

    plt.hlines(y=positiveProperties["width_heights"], xmin=positiveProperties["left_ips"],
               xmax=positiveProperties["right_ips"], color = "C1")

    # Прорисовка интервалов

    #=============================================================================
    plt.tight_layout()
    plt.legend() 

    # Параметры второй части графика

    plt.subplot(212).set_title("Анализ на минимумы")
    plt.grid(True, which="major", color="k", linestyle="dashed", alpha=0.5)
    plt.plot(x, "k",  linewidth=2, label = "График кардиограмы")

    plt.plot(negativePeaks, x[negativePeaks], "bx", label = "Локальный минимум")

    plt.vlines(x=negativePeaks, ymin=x[negativePeaks] + negativeProperties["prominences"],
               ymax = x[negativePeaks], color = "C2", label = "Высота и ширина вогнутой функции")

    plt.hlines(y=-negativeProperties["width_heights"], xmin=negativeProperties["left_ips"],
               xmax=negativeProperties["right_ips"], color = "C2")
    
    # Прорисовка интервалов

    #=============================================================================

    plt.tight_layout()
    plt.legend() 
    plt.show()

    return positivePeaks, positiveProperties, negativePeaks, negativeProperties
    
###############################################################


if __name__ == "__main__":


    x = electrocardiogram()[0:300]

    positivePeaks, positiveProperties, negativePeaks, negativeProperties = show_graphic(x)

    print(len(positiveProperties.get("widths")))

    right = positiveProperties.get("right_ips")
    left = positiveProperties.get("left_ips")

    for i in range(0, len(right)):
        print(left[i],"-", right[i])
        print("----------------------------------")

    # positivePeaks, positiveProperties, negativePeaks, negativeProperties = show_graphic(x)

import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks


def print_value(nValue):
    """
    """
    for i in range(0, len(nValue)):
        print(nValue[i])


def get_grafic_parametr(signalData):
    """
    """
    # Получение положительных пиков и их параметров 
    positivePeaks, positiveProperties = find_peaks(signalData, width=1)

    #Получение отрицательных пиков и их параметров
    negativePeaks, negativeProperties = find_peaks(-signalData, width=1)

    return positivePeaks, positiveProperties, negativePeaks, negativeProperties



def show_graphic(positivePeaks, positiveProperties, negativePeaks, negativeProperties, header):
    """
    """

    # Определение заголовка окна рабочей области
    fig = plt.figure(0)
    fig.canvas.set_window_title("Анализ графиков на минимум и максимум участака {}".format(header))

    # Список с цветами для закраски категорий графика
    colorList = ["silver", "darksalmon", "gold", "indigo", "cornflowerblue"]

    #--------------------------------------------------------------------------
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
    
    right = positiveProperties.get("right_ips")
    left = positiveProperties.get("left_ips")

    widthsParametr = positiveProperties.get("widths")
    prominencesParametr = positiveProperties.get("prominences")
    intervals = list(zip(left, right))
    intervalParemetrs = list(zip(prominencesParametr, widthsParametr))

    noiceIndex = []
    firstGroup = []
    secondGroup = []
    thirdGroup = []
    fourthGroup = []

    for i in range(0, len(intervalParemetrs)):
        if intervalParemetrs[i][0] <=0.025 and intervalParemetrs[i][1] <= 2:
            noiceIndex.append(intervals[i])
            plt.axvspan(intervals[i][0], intervals[i][1], \
                color=colorList[0], alpha=1, label="Потенциальный шум (h<=0.025; w<=2)" if len(noiceIndex) == 1 else "")

        elif intervalParemetrs[i][0] > 1 and (intervalParemetrs[i][1] > 6):
            firstGroup.append(intervals[i])
            plt.axvspan(intervals[i][0], intervals[i][1], \
                color=colorList[1], alpha=0.75, label="1-я группа (h<=0.025; w(2-3))" if len(firstGroup) == 1 else "")

        # elif ((intervalParemetrs[i][0] <=0.025) and (intervalParemetrs[i][1] > 3 and intervalParemetrs[i][1] <= 7)):
        #     secondGroup.append(intervals[i])
        #     plt.axvspan(intervals[i][0], intervals[i][1], \0
        #         color=colorList[2], alpha=0.5, label="2-я группа (h<=0.025; w(3-7)" if len(secondGroup) == 1 else "")

        # elif ((intervalParemetrs[i][0] <=0.3) and (intervalParemetrs[i][1] > 7 and intervalParemetrs[i][1] <= 20)):
        #     thirdGroup.append(intervals[i])
        #     plt.axvspan(intervals[i][0], intervals[i][1], \
        #         color=colorList[3], alpha=0.35, label="3-я группа (h<=0.3; w(7-20)" if len(thirdGroup) == 1 else "")
        else:
            fourthGroup.append(intervals[i])
            plt.axvspan(intervals[i][0], intervals[i][1], \
                color=colorList[4], alpha=0.9, linestyle="dashed", label="2-я группа (h>0.3; w>20)" if len(fourthGroup) == 1 else "")

    positiveData = []
    positiveData.append(noiceIndex)
    positiveData.append(firstGroup)
    positiveData.append(secondGroup)
    positiveData.append(thirdGroup)
    positiveData.append(fourthGroup)
    
    plt.tight_layout()
    plt.legend() 

    #=============================================================================
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

    right = negativeProperties.get("right_ips")
    left = negativeProperties.get("left_ips")

    widthsParametr = negativeProperties.get("widths")
    prominencesParametr = negativeProperties.get("prominences")
    intervals = list(zip(left, right))
    intervalParemetrs = list(zip(prominencesParametr, widthsParametr))

    noiceIndex = []
    firstGroup = []
    secondGroup = []
    thirdGroup = []
    fourthGroup = []

    for i in range(0, len(intervalParemetrs)):
        if intervalParemetrs[i][0] <=0.025 and intervalParemetrs[i][1] <= 2:
            noiceIndex.append(intervals[i])
            plt.axvspan(intervals[i][0], intervals[i][1], \
                color=colorList[0], alpha=1, label="Потенциальный шум (h<=0.025; w<=2)" if len(noiceIndex) == 1 else "")

        elif intervalParemetrs[i][0] > 1 and (intervalParemetrs[i][1] > 6):
            firstGroup.append(intervals[i])
            plt.axvspan(intervals[i][0], intervals[i][1], \
                color=colorList[1], alpha=0.75, label="1-я группа (h<=0.025; w(2-3))" if len(firstGroup) == 1 else "")

        # elif ((intervalParemetrs[i][0] <=0.025) and (intervalParemetrs[i][1] > 3 and intervalParemetrs[i][1] <= 7)):
        #     secondGroup.append(intervals[i])
        #     plt.axvspan(intervals[i][0], intervals[i][1], \
        #         color=colorList[2], alpha=0.5, label="2-я группа (h<=0.025; w(3-7)" if len(secondGroup) == 1 else "")

        # elif ((intervalParemetrs[i][0] <=0.3) and (intervalParemetrs[i][1] > 7 and intervalParemetrs[i][1] <= 20)):
        #     thirdGroup.append(intervals[i])
        #     plt.axvspan(intervals[i][0], intervals[i][1], \
        #         color=colorList[3], alpha=0.35, label="3-я группа (h<=0.3; w(7-20)" if len(thirdGroup) == 1 else "")
        else:
            fourthGroup.append(intervals[i])
            plt.axvspan(intervals[i][0], intervals[i][1], \
                color=colorList[4], alpha=0.15, label="2-я группа (h>0.3; w>20)" if len(fourthGroup) == 1 else "")

    negativeData = []
    negativeData.append(noiceIndex)
    negativeData.append(firstGroup)
    negativeData.append(secondGroup)
    negativeData.append(thirdGroup)
    negativeData.append(fourthGroup)

    plt.tight_layout()
    plt.legend() 
    plt.show()
    return positiveData, negativeData

def print_group_info(groupData):
    """
    Вывод информации о состоянии групп
    """
    print("Шум - {}".format(str(len(groupData[0]))))
    # print(groupData[0])
    for i, j in enumerate(groupData[0]):
        print(j)
    print("----------------------------------------")
    print("1-я группа - {}".format(str(len(groupData[1]))))
    print(groupData[1])
    print("----------------------------------------")
    print("2-я группа")
    print(groupData[2])
    print("----------------------------------------")
    print("3-я группа")
    print(groupData[3])
    print("----------------------------------------")
    print("4-я группа  - {}".format(str(len(groupData[4]))))
    # print(groupData[4])
    for i, j in enumerate(groupData[4]):
        print(j)
    print("===============================================================")

if __name__ == "__main__":

    print("Данная программа выполняет поиск и классификацию участков функции")
    print("В качестве примера выбран датасэт electrocardiogram библиотеки scipy")
    a = int(input("Введите начало оцениваемого участка - "))
    while a < 0:
        a = int(input("Введите начало оцениваемого участка - "))

    b = int(input("Введите конец оцениваемого участка - "))
    while b < 0 or b < a:
        b = int(input("Введите конец оцениваемого участка - "))

    x = electrocardiogram()[a:b]

    header = str(a) + "-" + str(b)

    positivePeaks, positiveProperties, negativePeaks, negativeProperties = get_grafic_parametr(x)


    positiveData, negativeData = show_graphic(positivePeaks, positiveProperties, negativePeaks, negativeProperties, header)
    print("Обнаружено {} пиков в положительной области".format(len(positivePeaks)))
    print_group_info(positiveData)

    print("Обнаружено {} пиков в отрицательной области".format(len(negativePeaks)))
    print_group_info(negativeData)

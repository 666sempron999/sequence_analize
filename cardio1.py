import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks

def print_dict(mydict):
    """
    """
    for key, value in mydic.items() :
        print(key, value)


def print_value(nValue):
    for i in range(0, len(nValue)):
        print(nValue[i])

###############################################################

x = electrocardiogram()[17900:18000]
peaks, properties = find_peaks(x, width=1)

peaks_negative, n_properties = find_peaks(-x, width=0, height = -3, threshold = None)

properties["prominences"], properties["widths"]

plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.plot(peaks_negative, x[peaks_negative], "o")

plt.vlines(x=peaks, ymin=x[peaks] - properties["prominences"],
           ymax = x[peaks], color = "C1")


plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"],
           xmax=properties["right_ips"], color = "C1")


plt.vlines(x=peaks_negative, ymin=x[peaks_negative] + n_properties["prominences"],
           ymax = x[peaks_negative], color = "C2")


plt.hlines(y=-n_properties["width_heights"], xmin=n_properties["left_ips"],
           xmax=n_properties["right_ips"], color = "C2")


print(type(properties))
print(properties.keys())
print("widths")
print_value(properties.get("widths"))
 
print("=====================================")

print("prominences")
print_value(properties.get("prominences"))
print("=====================================")
print("=====================================")
print("=====================================")

print_value(n_properties.get("widths"))
print("=====================================")
print_value(n_properties.get("prominences"))

plt.show()


'''
# find all the peaks that associated with the negative peaks
peaks_negative, _ = scipy.signal.find_peaks(-df_water_level.water_level, height = -3, threshold = None, distance=500)

plt.figure(figsize = (14, 8))
plt.plot_date(df_water_level.index, df_water_level.water_level, 'b-', linewidth = 2)

plt.plot_date(df_water_level.index[peaks_positive], df_water_level.water_level[peaks_positive], 'ro', label = 'positive peaks')
plt.plot_date(df_water_level.index[peaks_negative], df_water_level.water_level[peaks_negative], 'go', label = 'negative peaks')

plt.xlabel('Datetime')
plt.ylabel('Water level (m)')
plt.legend(loc = 4)
plt.show()
'''
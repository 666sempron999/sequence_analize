import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks

# def print_dict(mydict):
#     """
#     """
#     for key, value in mydic.items() :
#         print(key, value)


# def print_value(nValue):
#     for i in range(0, len(nValue)):
#         print(nValue[i])

# x = electrocardiogram()[2000:4000]
# peaks, _ = find_peaks(x)
# plt.plot(x)
# plt.plot(peaks, x[peaks], "x")
# plt.plot(np.zeros_like(x), "--", color="gray")
# plt.show()

# ###############################################################
# border = np.sin(np.linspace(0, 3 * np.pi, x.size))
# peaks, _ = find_peaks(x, height=(-border, border))
# plt.plot(x)
# plt.plot(-border, "--", color="gray")
# plt.plot(border, ":", color="gray")
# plt.plot(peaks, x[peaks], "x")
# plt.show()
# ###############################################################
# border = np.sin(np.linspace(0, 3 * np.pi, x.size))
# peaks, _ = find_peaks(x, height=(-border, border))
# plt.plot(x)
# plt.plot(-border, "--", color="gray")
# plt.plot(border, ":", color="gray")
# plt.plot(peaks, x[peaks], "x")
# plt.show()
# ###############################################################
# peaks, _ = find_peaks(x, distance=150)
# np.diff(peaks)

# plt.plot(x)
# plt.plot(peaks, x[peaks], "x")
# plt.show()
# ###############################################################
# peaks, properties = find_peaks(x, prominence=(None, 0.6))
# properties["prominences"].max()

# plt.plot(x)
# plt.plot(peaks, x[peaks], "x")
# plt.show()
###############################################################

x = electrocardiogram()[1300:3000]
peaks, properties = find_peaks(x, width=1)
properties["prominences"], properties["widths"]

plt.plot(x)
# plt.plot(peaks, x[peaks], "x")
# plt.vlines(x=peaks, ymin=x[peaks] - properties["prominences"],
#            ymax = x[peaks], color = "C1")
# plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"],
#            xmax=properties["right_ips"], color = "C1")

# print(type(properties))
# print(properties.keys())
# print("widths")
# print_value(properties.get("widths"))
# # print(properties.get("widths"))
# # print(type(properties.get("widths")))
# # print(len(properties.get("widths")))
# print("=====================================")

# print("prominences")
# print_value(properties.get("prominences"))
# print("=====================================")


'''
plt.vlines(x=peaks, ymin=x[peaks] - properties["prominences"],
           ymax = x[peaks], color = "C1")
plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"],
           xmax=properties["right_ips"], color = "C1")
'''
plt.tight_layout()
plt.show()
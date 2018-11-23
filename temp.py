# import numpy as np
# import matplotlib.pyplot as plt

# mean, amp = 40000, 20000
# t = np.arange(50)
# s1 = np.sin(t)*amp + mean #synthetic ts, but closer to my data 

# fig, ax1 = plt.subplots()
# ax1.plot(t, s1, 'b-')

# ax1.set_xlabel('time')
# mn, mx = ax1.set_ylim(mean-amp, mean+amp)
# ax1.set_ylabel('km$^3$/year')

# km3yearToSv = 31.6887646e-6

# ax2 = ax1.twinx()
# ax2.set_ylim(mn*km3yearToSv, mx*km3yearToSv)
# ax2.set_ylabel('Sv')

# plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi)
y1 = np.sin(x);
y2 = 0.01 * np.cos(x);

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x, y1)
ax1.set_ylabel('y1')

ax2 = ax1.twinx()
ax2.plot(x, y2, 'r-')
ax2.set_ylabel('y2', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')

plt.show()
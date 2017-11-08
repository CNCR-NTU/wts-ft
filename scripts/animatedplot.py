import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_line(num, line1, line2):

    tNow = time.time()

    t = np.linspace(tNow - 10.0, tNow, 200)

    f1 = 0.5 # Hz
    f2 = 0.3 # Hz

    line1.set_data(t - tNow, np.sin(2 * np.pi * f1 * t))
    line2.set_data(t - tNow, np.sin(2 * np.pi * f2 * t))

    return (line1, line2)

(fig, axes_list) = plt.subplots(2, 1)

axes1 = axes_list[0]
axes2 = axes_list[1]

line1, = axes1.plot([], [], 'r-')
line2, = axes2.plot([], [], 'b-')

for ax in [axes1, axes2]:
    ax.set_xlim(-10, 0)
    ax.set_ylim(-1, 1)
    #ax.set_xlabel('x')
    #ax.set_ylabel('y')
    #ax.set_title('test')

animation = animation.FuncAnimation(fig, update_line, 250, fargs = (line1, line2), interval = 0, blit = True)

# Enter the event loop
fig.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib import style

# Signal parameters
f = 20      # Hz
t = np.linspace(0, 0.5, 200)
x1 = np.sin(2*np.pi*f*t)

# Matplotlib style
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

# Figure layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,9))
plt.subplots_adjust(bottom=0.25)  # leave space for slider

# Continuous-time signal
ax1.plot(t, x1, linewidth=3)
ax1.set_xlabel('time')
ax1.set_ylabel('amplitude')

# Placeholder for discrete-time plot
#(line2,) = ax2.plot([], [], 'g-o')
(line2,) = ax2.plot([], [], 'g')
ax2.set_xlabel('time')
ax2.set_ylabel('amplitude')
ax2.set_xlim(0, 0.5)
ax2.set_ylim(-1.2, 1.2)

# Slider (position: [left, bottom, width, height])
ax_srate = plt.axes([0.25, 0.1, 0.5, 0.03])
slider_srate = Slider(ax_srate, 'srate', valmin=1, valmax=200, valinit=60, valstep=1)

# Slider callback
def update(val):
    srate = slider_srate.val
    T = 1 / srate

    n = np.arange(0, 0.5/T)
    nT = n*T
    x2 = np.sin(2 * np.pi * f * nT)

    # Update data of the discrete signal
    line2.set_xdata(nT)
    line2.set_ydata(x2)

    ax2.relim()
    ax2.autoscale_view()
    fig.canvas.draw_idle()

slider_srate.on_changed(update) # Link slider to update function
update(5) # Initialize first draw

plt.show()
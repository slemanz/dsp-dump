import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib import style

f = 20      #Hz
t = np.linspace(0, 0.5, 200)
x1 = np.sin(2*np.pi*f*t)

srate = 5
T = 1/srate
n = np.arange(0, 0.5/T)
nT = n*T
x2 = np.sin(2*np.pi*f*nT)

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

plt.figure(figsize=(16,9))
plt.subplot(1, 2, 1)

plt.plot(t, x1, linewidth=3)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.subplot(1, 2, 2)
plt.plot(nT, x2, 'g-', linewidth=3)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)
plt.show()

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

t = np.arange(0.0, 100.0, 0.1)
# s = np.sin(2*np.pi*t)
s = 0.1*t
l, = plt.plot(t,s)
plt.axis([0, 10, 0, 12])

axpos = plt.axes([0.2, 0.1, 0.65, 0.03])
slider_pos = Slider(axpos, 'Pos', 0.1, 200.0)

def update(val):
    srate = slider_pos.val
    T = 1/srate
    n = np.arange(0, 0.5/T)
    nT = n*T
    x2 = np.sin(2*np.pi*f*nT)

    
    fig.canvas.draw_idle()

slider_pos.on_changed(update)

plt.show()
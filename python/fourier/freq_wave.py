import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

srate = 1024  # Hz
t = np.arange(0., 1., 1/srate)    # time vector in seconds

x1 = 3*np.sin(2*np.pi*10*t)
x2 = 3*np.sin(2*np.pi*25*t)
x3 = 3*np.sin(2*np.pi*50*t)
x4 = 3*np.sin(2*np.pi*100*t)

xt = x1 + x2 + x3 + x4          # Combined sinewave 

# Plot every sine wave

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

plt.figure(figsize=(16, 9)) # set the size of figure

plt.plot(t, xt, linewidth=3) 
plt.title("Signal with Frequencies 10, 25, 50 and 100 Hz", fontsize=16)
plt.xlabel('time in sec', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)

plt.tight_layout() # prevent overlap
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

srate = 256  # Hz
t = np.arange(0.,1.,1/srate)    # time vector in seconds

x1 = 5*np.sin(2*np.pi*2*t)      # First sinewave
x2 = 2*np.sin(2*np.pi*4*t)      # Second sinewave
x3 = 7*np.sin(2*np.pi*6*t)      # Third sinewave

x4 = x1 + x2 + x3               # Combined sinewave

# Plot every sine wave

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

plt.figure(figsize=(16, 9)) # set the size of figure
plt.suptitle('Constructing a Wave with different Sine Waves', fontsize=30)


plt.subplot(2, 2, 1) 
plt.plot(t, x1, linewidth=3) 
plt.title("SineWave of amplitude '5' and frequency '2 Hz'", fontsize=16)
plt.xlabel('time in sec', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)

plt.subplot(2, 2, 2)
plt.plot(t, x2, linewidth=3)
plt.title("SineWave of amplitude '2' and frequency '4 Hz'", fontsize=16)
plt.xlabel('time in sec.', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)

plt.subplot(2, 2, 3)
plt.plot(t, x3, linewidth=3)
plt.title("SineWave of amplitude '7' and frequency '6 Hz'", fontsize=16)
plt.xlabel('time in sec', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)

plt.subplot(2, 2, 4)
plt.plot(t, x4, linewidth=3)
plt.title("Combined SineWave by adding above three sine waves", fontsize=16)
plt.xlabel('time in sec', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)

plt.tight_layout() # prevent overlap
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

srate = 256  # Hz
t = np.arange(0., 1., 1/srate) # time vector in seconds

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

SineWave = 3*np.sin(2*np.pi*5*t)
CosineWave  = 3*np.cos(2*np.pi*5*t)
plt.figure(figsize=(16, 9))


plt.plot(t, SineWave, 'y', linewidth=3, label='SineWave')
plt.plot(t, CosineWave, 'r', linewidth=3, label='CosineWave')

plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.title('Sine and Cosine waves comparison', fontsize=25)
plt.legend(fontsize=20, loc="upper right")
plt.xlim([0, 1])
plt.show()


srate = 256  # Hz
t = np.arange(0., 1., 1/srate) # time vector in seconds

x1 = np.sin(2*np.pi*2*t) #   sinewave
x2 = 2*np.cos(2*np.pi*4*t) # Cosinewave
x3 = x1 + x2  # sum of sine and cosine

DC = 2
x4 = DC + x1 + x2 # sum of sine, cosine and DC.

# Plotting
plt.figure(figsize=(16,9)) # set the size of figure
plt.suptitle('Constructing a Wave with Sine, cosine and DC', fontsize=40)

plt.subplot(2, 2, 1) 
plt.plot(t, x1, linewidth=3) 
plt.title("Sine Wave of amplitude '1' and frequency '2 Hz'", fontsize=20)
plt.xlabel('time in sec', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)

plt.subplot(2, 2, 2)
plt.plot(t, x2, linewidth=3)
plt.title("Cosine Wave of amplitude '2' and frequency '4 Hz'", fontsize=20)
plt.xlabel('time in sec.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)

plt.subplot(2, 2, 3)
plt.plot(t, x3, linewidth=3)
plt.title("Sum of Sine and Cosine wave", fontsize=20)
plt.xlabel('time in sec', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)

plt.subplot(2, 2, 4)
plt.plot(t, x4, linewidth=3)
plt.title("Sum of sine, Cosine and DC", fontsize=20)
plt.xlabel('time in sec', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)

plt.tight_layout() # prevent overlap
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Sampling Frequency less than twice the maximum frequency (fs < 2fmax)
f = 20      #Hz
t = np.linspace(0, 0.5, 200)
x1 = np.sin(2*np.pi*f*t)

srate = 35
T = 1/srate

n = np.arange(0, 0.5/T)

nT = n*T

x2 = np.sin(2*np.pi*f*nT)

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

plt.figure(figsize=(16,9))
plt.subplot(2, 2, 1)

plt.plot(t, x1, linewidth=3)
plt.title('SineWave of frequency 20 Hz', fontsize=15)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.subplot(2, 2, 2)
plt.plot(nT, x2, 'ro', linewidth=3)
plt.title('Sample marks after resampling at fs = 35Hz', fontsize=15)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.subplot(2, 2, 3)
plt.stem(nT, x2, 'm')
plt.title('Sample after resampling at fs = 35Hz', fontsize=15)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.subplot(2, 2, 4)
plt.plot(nT, x2, 'g-', linewidth=3)
plt.title('Reconstruted Sine wave', fontsize=15)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.show()

# Sampling Frequency greater than twcie the maximum frequency (fs > 2fmax)

f = 20      # Hz
t = np.linspace(0, 0.5, 200)
x1 = np.sin(2*np.pi*f*t)

srate = 50  # Hz
T = 1/srate

n = np.arange(0, 0.5/T)

nT = n*T
x2 = np.sin(2*np.pi*f*nT)

plt.figure(figsize=(16,9))
plt.subplot(2, 2, 1)

plt.plot(t, x1, linewidth=3)
plt.title('SineWave of frequency 20 Hz', fontsize=15)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.subplot(2, 2, 2)
plt.plot(nT, x2, 'ro', linewidth=3)
plt.title('Sample marks after resampling at fs = 50Hz', fontsize=15)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.subplot(2, 2, 3)
plt.stem(nT, x2, 'm')
plt.title('Sample after resampling at fs = 50Hz', fontsize=15)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.subplot(2, 2, 4)
plt.plot(nT, x2, 'g-', linewidth=3)
plt.title('Reconstruted Sine wave', fontsize=15)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.show()

# Sampling Frequency five times greater than the maximum frequency (fs > 5fmax)

f = 20      # hz
t = np.linspace(0, 0.5, 200)
x1 = np.sin(2*np.pi*f*t)

srate = 100 # hz

T = 1/srate

n = np.arange(0, 0.5/T)
nT = n*T
x2 = np.sin(2*np.pi*f*nT)

plt.figure(figsize=(16,9))
plt.subplot(2, 2, 1)

plt.plot(t, x1, linewidth=3)
plt.title('SineWave of frequency 20 Hz', fontsize=15)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.subplot(2, 2, 2)
plt.plot(nT, x2, 'ro', linewidth=3)
plt.title('Sample marks after resampling at fs = 50Hz', fontsize=15)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.subplot(2, 2, 3)
plt.stem(nT, x2, 'm')
plt.title('Sample after resampling at fs = 50Hz', fontsize=15)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.subplot(2, 2, 4)
plt.plot(nT, x2, 'g-', linewidth=3)
plt.title('Reconstruted Sine wave', fontsize=15)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

plt.show()
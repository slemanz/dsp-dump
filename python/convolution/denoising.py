import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 25
plt.rcParams['ytick.labelsize'] = 25

# create signal
srate = 256 # Hz
t  = np.arange(0, 3, 1/srate)
pnts = len(t)

print(pnts)

# creating a noiseless signal
x = np.sin(2*np.pi*2*t)

# creating a random noise
noise = 5*np.random.randn(pnts)

# adding noise on signal
noisy_signal = x + noise

# plotting
plt.figure(figsize=(16, 9))

plt.plot(t, noisy_signal, label='Noisy Signal')
plt.legend(fontsize=15)
plt.show()

# select filter for denoising
filter = 2*np.ones(50)/10 # moving avarage filter

# filtering by convolution
filtered_singal = np.convolve(noisy_signal, filter, mode='same')

# plotting filtered signal

plt.figure(figsize=(16, 9))
plt.plot(filtered_singal, label='Filtered Signal')
plt.legend(fontsize=15)
plt.show()

# Plotting Noisy signal and filtered signal
plt.figure(figsize=(16, 9))
plt.plot(noisy_signal, 'g', label='Noisy Signal')
plt.plot(filtered_singal, 'r', label='Filtered Signal')
plt.legend(fontsize=15)
plt.title('Signal Denoising', fontsize=20)
plt.show()
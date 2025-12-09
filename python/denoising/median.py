import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

# create signal
srate = 256 # Hz
t  = np.arange(0,3,1/srate)
pnts = len(t)

# creating a noiseless signal
x = np.sin(2*np.pi * 2 * t)

# creating a random noise
noise = 5 * np.random.randn(pnts)

# Adding noise on signal
signal = x + noise

plt.figure(figsize=(16, 9)) # set the size of figure
plt.plot(t,signal, 'g', label='Noisy Signal')
plt.xlabel('time in sec', fontsize=20)
plt.ylabel('Amplitude', fontsize=20)
plt.legend(fontsize = 15)
plt.show()

N = 50             

# Initialize denoised signal    
filt_sig = np.zeros(signal.shape[0])

# Applying Median filter

for i in range(0,signal.shape[0]):
    filt_sig[i] = np.median(signal[i:N+i])

# Applying moving average filter
mean_filt_sig = np.zeros(signal.shape[0])
for i in range(0,signal.shape[0]):
    mean_filt_sig[i] = np.mean(signal[i:N+i])

plt.figure(figsize=(16, 9)) # set the size of figure
plt.plot(t, signal, 'g-', label='NoisySignal')
plt.plot(t, filt_sig, 'r-', linewidth=3, label='Median Filtered Signal')
plt.plot(t, mean_filt_sig, 'b-', linewidth=3, label='Moving Average Filtered Signal')
plt.xlabel('time in sec', fontsize=20)
plt.ylabel('Amplitude', fontsize=20)
plt.title('Median and Moving average filters with order=%d.' %N, fontsize = 25)
plt.legend(fontsize = 15)
plt.show()
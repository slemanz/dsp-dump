import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

# create signal
srate = 512 # Hz
t  = np.arange(0, 3, 1/srate)
pnts = len(t)

# creating a noiseless signal
x = np.sin(2*np.pi * 2 * t)

# creating a random noise
noise  = 5*np.random.randn(pnts)

# Adding noise on signal
Noisysignal = x + noise

plt.figure(figsize=(16, 9)) # set the size of figure
plt.plot(t,Noisysignal, 'g', label='Noisy Signal')
plt.xlabel('time in sec', fontsize=20)
plt.ylabel('Amplitude', fontsize=20)
plt.legend(fontsize=15)
plt.show()

# Generating Gaussian filter / kernel

N = 100
fwhm = 50 # ms # full-width half-maximum
Gtime = 1000 * np.arange(-N, N)/srate # since fwhm is in ms, therefore we multiply it by 1000 to get Gtime in ms
Gfilter = np.exp(-(4*np.log(2)*Gtime**2) / fwhm**2 ) # Generating Gaussian filter
Gfilter = Gfilter/np.sum(Gfilter) # Normalizing the Gaussian Filter


# plotting Gaussian filter / kernel

plt.figure(figsize=(16, 9)) # set the size of figure
plt.plot(Gtime, Gfilter, 'm', linewidth=3, label='Gaussian Filter')
plt.xlabel('time in ms', fontsize=15)
plt.ylabel('Gain of the filter', fontsize=15)
plt.xlim([-100, 100])
plt.legend(fontsize=15)
plt.show()

# Zero padding the noisy siganl to avoid edge effect

sig_4_filter = np.concatenate ((np.zeros(N), Noisysignal, np.zeros(N)), axis= 0)  # zero padding to avoid edge effect

K = len(Noisysignal)

timeindex = np.concatenate ((np.arange(-N,0), np.arange(0, K), np.arange(K, K+N)), axis= 0)
time_4_filter = timeindex/srate

plt.figure(figsize=(16, 9))
plt.plot(time_4_filter, sig_4_filter, 'g', label='zero padded Noisy Signal to avoid edge effect')
plt.xlabel('time in s', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=15)
plt.show()

# Initialize the filtered signal
Gfilt_sig = np.zeros(sig_4_filter.shape[0])

# Applying Gaussian Filter
for i in range(0, Noisysignal.shape[0]):
    Gfilt_sig[i] = np.sum(sig_4_filter[i:2*N+i] * Gfilter)

plt.figure(figsize = (16, 9)) # set the size of figure
plt.plot(time_4_filter,sig_4_filter, 'g-', label='NoisySignal')
plt.plot(time_4_filter,Gfilt_sig, 'r-', linewidth=3, label='Filtered Signal')
plt.xlabel('time in sec', fontsize=20)
plt.ylabel('Amplitude', fontsize=20)
plt.title('Gaussian Moving average filter of order=%d.' %N, fontsize=25)
plt.legend(fontsize=15)
plt.show()

Gfilt_sig_clipped = Gfilt_sig[0:K] # clip off the edges to avoid edge effect.

plt.figure(figsize=(16, 9)) # set the size of figure
plt.plot(time_4_filter,sig_4_filter, 'g-', label='NoisySignal')
plt.plot(t,Gfilt_sig_clipped, 'r-', linewidth=3, label='clipped Filtered Signal')
plt.xlabel('time in sec', fontsize=20)
plt.ylabel('Amplitude', fontsize=20)
plt.title('Gaussian Moving average filter order=%d.' %N, fontsize = 25)
plt.legend(fontsize = 15)
plt.show()
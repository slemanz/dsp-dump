import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

# create signal
srate = 256 # Hz
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

N = 30                # N = order of moving average  filetr. FilterWindow is actually (2N + 1). 
                      #Increasing the order of filter will increase the smoothness of filtered signal

# Initialize denoised signal    
filt_sig = np.zeros(Noisysignal.shape[0])

# applying moving average filter

for i in range(0,Noisysignal.shape[0]):
    filt_sig[i] = np.mean( Noisysignal[i:(2*N + 1) + i])

plt.figure(figsize=(16,9)) # set the size of figure
plt.plot(t,Noisysignal, 'g-', label='NoisySignal')
plt.plot(t,filt_sig, 'r-', linewidth=3, label='Filtered Signal')
plt.xlabel('time in sec', fontsize=20)
plt.ylabel('Amplitude', fontsize=20)
plt.title('Moving average filter with order=%d.' %N, fontsize=25)
plt.legend(fontsize = 15)

plt.show()
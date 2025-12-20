import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import style
import scipy

# Generate the Signal

srate = 256  # Hz
Nyquist = srate/2
t = np.arange(0., 1., 1/srate) # time vector in seconds
x = 3 * np.sin(2*np.pi*4*t) 

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

plt.figure(figsize=(16, 9)) # set the size of figure
plt.plot(t,x,'ms', linewidth = 1,label='Original Signal')
plt.legend(fontsize = 15)
plt.show()

# calculating FFT

X = scipy.fft.fft(x) 

# calculating IFFT

reconstruct_x = scipy.fft.ifft(X)

plt.figure(figsize=(16, 9)) # set the size of figure
plt.suptitle('Signal and Reconstructed Signal', fontsize = 30)

plt.plot(t,x,'ms', markersize = 10,label='Original Signal')
plt.plot(t,np.real(reconstruct_x),'y',linewidth = 3, label='Reconstructed Signal')
plt.xlabel('time in sec', fontsize = 20)
plt.ylabel('amplitude', fontsize = 20)
plt.legend(fontsize = 15)
plt.show()
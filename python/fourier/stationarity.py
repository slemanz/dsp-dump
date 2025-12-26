import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import style
import scipy

srate = 256
t = np.arange(0, 10, 1/srate)

amp = np.linspace(1, 10, len(t)) # linearly increasing amplitude


x1 = 5*np.sin(2*np.pi*5*t)   # Stationary Signal
x2 = amp*np.sin(2*np.pi*5*t) # Non Stationary Signal


# Obtain Fourier coefficients and Hz vector

X1 = 2 * np.abs(scipy.fft.fft(x1)/len(t))
X2 = 2 * np.abs(scipy.fft.fft(x2)/len(t))

Hz = np.linspace(0,srate/2,int(np.floor(len(t)/2)+1))

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

plt.figure(figsize = (16, 9)) # set the size of figure
plt.suptitle('Signals and their Fourier tranform', fontsize = 30)

plt.subplot(2,1,1) 
plt.plot(t,x1,'b',linewidth = 3) 
plt.plot(t,x2,'m',linewidth = 3) 
plt.title("Original Signal", fontsize = 25)
plt.xlabel('time in sec', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,1,2) 
plt.plot(Hz,X1[0:len(Hz)],'bo-')
plt.plot(Hz,X2[0:len(Hz)],'ms-')
plt.xlim([1,10])
plt.title('Fourier transform', fontsize =25)
plt.xlabel('Frequency in Hz', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.tight_layout()
plt.show()
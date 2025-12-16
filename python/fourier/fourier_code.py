import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Generating  the signal

srate  = 256 # Hz
t = np.arange(0., 1., 1/srate)  # time vector in seconds
amp = 3
f = 5 #Hz
x = amp*np.sin(2*np.pi*f*t) # Signal

# Initializing Fourier Coefficients
X = np.zeros(len(x), dtype=complex)

for freq in range(0, len(t)):
    # create complex sine wave and compute dot product with signal
    csw = np.exp(-1j*2*np.pi*freq*t)
    X[freq] = np.sum( np.multiply(x,csw) )

# extract amplitudes
amps = np.abs(X)/len(t)

# Plotting Signal and Complex Sine Wave

style.use('dark_background')

plt.figure(figsize=(16, 9))

plt.plot(t, x, linewidth=3, label='Signal With amp = 3 and frquency = 5 Hz')
plt.plot(t, 3*np.real(csw), 'r-', linewidth=3, label='real part of csw')
plt.plot(t, 3*np.imag(csw), 'm-', linewidth=3, label='Imag part of csw')

plt.xlabel('time',fontsize=15)
plt.ylabel('amplitude', fontsize=15)
plt.title('Signal Modelling With Complex Sine Wave',fontsize=20)
plt.xlim([0,1])

plt.legend(fontsize=15, loc="lower left")
plt.show()

# Plotting the Signal and its Fourier Transform

plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.figure(figsize=(16, 9)) # set the size of figure
plt.suptitle('Signal and its Fourier transform', fontsize = 30)

plt.subplot(2,1,1) 
plt.plot(t,x,linewidth = 3) 
plt.title("Signal of amplitude '3' and frequency '5 Hz'", fontsize = 20)
plt.xlabel('time in sec', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)

plt.subplot(2,1,2)
markerline, stemlines, baseline = plt.stem(amps)
plt.setp(stemlines, 'linewidth', 3)
plt.title(" Fourier transform of a signal", fontsize=20)
plt.xlabel('Indices', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)

# The frequency spectrum of a real valued signal is always symmetric. Since the
# symmetric part is exactly a mirror image of  the first part, it provides no
# additional information.

plt.tight_layout() # prevent overlap
plt.show()

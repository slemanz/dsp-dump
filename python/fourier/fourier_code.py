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

plt.legend(fontsize=15)
plt.show()
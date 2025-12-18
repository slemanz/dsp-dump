import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import math
import scipy

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

# Correcting the amplitudes and converting indices to frequencies

srate  = 256 # Hz
t      = np.arange(0.,1.,1/srate)  # time vector in seconds
amp    = 3
f      = 5 #Hz
x      = amp*np.sin(2*np.pi*f*t) # Signal


# Initializing Fourier Coefficients
X   = np.zeros(len(x), dtype=complex)

for freq in range(0, len(t)):
    # create complex sine wave and compute dot product with signal
    csw = np.exp( -1j*2*np.pi*freq*t )
    X[freq] = np.sum( np.multiply(x,csw) )


# extract amplitudes
amps = 2 * np.abs(X)/len(t)

# In the above line of code we multiplt by 2 to incorporate the negative frequecies of complex sinusoidal

# converitng indices to frequency

# There are 0 to 255 indices at which we generate the sine wave . These are frequency indices
# not the frequency in hertz. Since we have n=256 indices including zero, therefore after (n/2) i.e 128 in
# this case, we get the negative waveforms of the first 128 samples. It means after n=128,
# the frequencies are violating the Nyquist criteria.
# Thus in order to convert indices into hertz we need (n/2+1) or (n/2) linearly spaced samples between zero and
# Nyquist (srate/2) as shown below

Nyquist = srate/2

Hz = np.linspace(0, Nyquist, math.floor(len(t)/2 + 1))

# Plotting the Signal and its Fourier Transform

plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.figure(figsize=(16, 9)) # set the size of figure
plt.suptitle('Signal and its Fourier transform', fontsize = 30)

plt.subplot(2, 1, 1) 
plt.plot(t,x,linewidth = 3) 
plt.title("Signal of amplitude '3' and frequency '5 Hz'", fontsize = 25)
plt.xlabel('time in sec', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,1,2)
markerline, stemlines, baseline = plt.stem(Hz, amps[range(0,len(Hz))])
plt.setp(stemlines, 'linewidth', 3)
plt.xlim(0,10)
plt.ylim(0,5)
plt.title(" Fourier transform of a signal", fontsize = 25)
plt.xlabel('Frequency in Hz', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.tight_layout() # prevent overlap
plt.show()

# Fourier transform of a signal with multiple frequencies

srate = 256  # Hz
Nyquist = srate / 2
t = np.arange(0., 1., 1/srate) # time vector in seconds

x1 = 5*np.sin(2*np.pi*2*t) # First sinewave
x2 = 2*np.sin(2*np.pi*4*t) # Second sinewave
x3 = 7*np.sin(2*np.pi*6*t) # Third sinewave

x = x1 + x2 + x3           # Combined sinewave


# Initializing Fourier Coefficients
X   = np.zeros(len(x),dtype=complex)

for freq in range(0, len(t)):
    # create complex sine wave and compute dot product with signal
    csw = np.exp( -1j*2*np.pi*freq*t )
    X[freq] = np.sum( np.multiply(x,csw) )


# extract amplitudes
amps = 2 * np.abs(X)/ len(t)
# In the above line of code we multiplt by 2 to incorporate the negative frequecies of complex sinusoidal

# converitng indices to frequency
Nyquist = srate/2
Hz = np.linspace(0, Nyquist, math.floor(len(t)/2)+1)

# Plotting

plt.figure(figsize=(16, 9)) # set the size of figure
plt.suptitle('Signal and its Fourier transform', fontsize = 30)
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

plt.subplot(2,1,1) 
plt.plot(t,x,linewidth = 3) 
plt.title("Signal with frequencies 2, 4 and 6 Hz", fontsize = 25)
plt.xlabel('time in sec', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,1,2)
markerline, stemlines, baseline = plt.stem(Hz, amps[range(0, len(Hz))])
plt.setp(stemlines, 'linewidth', 5)
plt.xlim(0,10)
plt.ylim(0,8)
plt.title(" Fourier transform of a signal", fontsize = 25)
plt.xlabel('Frequency in Hz', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.tight_layout()
plt.show()

# Fourier transform of a signal with sine, cosine and a DC Component

srate = 256  # Hz
t = np.arange(0.,1.,1/srate) # time vector in seconds

x1 = 5 * np.sin(2 * np.pi * 10 * t) #   sinewave
x2 = 3 * np.cos(2 * np.pi * 20 * t) # Cosinewave
x3 = x1 + x2  # sum of sine and cosine

DC = 2

x = DC + x1 + x2 # sum of sine, cosine and DC.

# Calculating Fourier Coefficients

X = scipy.fft.fft(x)/len(t)
X = np.abs(X)

# Plotting Signal and its Fourier Transform

plt.figure(figsize=(16, 9)) # set the size of figure
plt.suptitle('Signal and its Fourier transform', fontsize = 30)

plt.subplot(2,1,1) 
plt.plot(t,x,linewidth = 3) 
plt.title("Signal with sine, cosine and dc component", fontsize = 25)
plt.xlabel('time in sec', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,1,2)

markerline, stemlines, baseline = plt.stem(X)
plt.setp(stemlines, 'linewidth', 5)
#plt.xlim(-.1,10)
plt.title("Symmetric Fourier transform of a signal", fontsize = 25)
plt.xlabel('Frequency Indices', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.tight_layout()
plt.show()
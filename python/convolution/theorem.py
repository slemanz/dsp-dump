import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import scipy

# The convolution of two signals in time domain is equal to the point-wise
# multiplication of the signals in frequency domain.

sig = np.array([1,2,2,1,1])
ker = np.array([3,2,1])

# convolution in time domain
Time_dom = np.convolve(sig,ker)

nconv = len(Time_dom)

sigF = scipy.fft.fft(sig,nconv)
kerF = scipy.fft.fft(ker,nconv)

# Element-wise multiplication of signal and kernel
sigFFT = sigF * kerF

# Inverse FFT
Freq_dom = np.real( scipy.fft.ifft( sigFFT ) )
Freq_dom


# Plotting time and frequency domain convolution
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 25
plt.rcParams['ytick.labelsize'] = 25

plt.figure(figsize=(16,9))
plt.plot(Time_dom, 'g^',markersize=25, label='Time domain')
plt.plot(Freq_dom, 'r-',linewidth=3, label='Frequency domain')
plt.legend(fontsize = 20)
plt.title('The Convolution theorem', fontsize = 30)
plt.show()
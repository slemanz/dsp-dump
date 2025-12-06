import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 25
plt.rcParams['ytick.labelsize'] = 25

# Generating signal with edges
NewSig = np.zeros(100)
NewSig[15:35]=1
NewSig[65:85]=1

plt.figure(figsize=(16, 9))
plt.xlim(0,100)
plt.plot(NewSig, 'o-', linewidth=3, label='Signal with edges')
plt.legend(fontsize=15)
plt.show()

# Kernel for edge detection
kernel = np.array([0.5, 0.3, 0.1, 0, -0.1, -0.3, -0.5])

# Plotting the kernel
plt.figure(figsize = (16, 9))
plt.plot(kernel, 'o-', linewidth=3, label='Kernel for edge detection')
plt.legend(fontsize=15)
plt.show()

# Performing edge detection by convolution
filt_sig = np.convolve(NewSig,kernel, mode = 'same')

# Plotting Filtered Signal
plt.figure(figsize = (20,8))
plt.plot(filt_sig,linewidth =3, label = 'Filtered Signal')
plt.legend(fontsize = 20)
plt.show()

# Plotting original signal and filtered signal
plt.figure(figsize = (24,12))
plt.plot(NewSig,'o-', linewidth =3, label = 'Original Signal')
plt.plot(filt_sig,'r-',linewidth =3, label = 'Filtered Signal')
plt.legend(fontsize = 20)
plt.title('Edge Detection', fontsize = 30)
plt.show()
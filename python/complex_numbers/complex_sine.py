import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Parameters for Complex Sine wave
t = np.linspace(0, 10, 100) # time 
f = 50;                     # frequency 
A = 1;                      # amplitude 
theta = np.pi/2;            # phase 

# generate the sine wave
Compx_wave = A*np.exp(-1j*(2*np.pi * f * t + theta) );

# plot 
style.use('dark_background')

plt.figure(figsize=(16, 9))
plt.plot(t, np.real(Compx_wave), 'b-', linewidth=3, label='real part')
plt.plot(t, np.imag(Compx_wave), 'm-', linewidth=3, label='imaginary part')
plt.xlim([-0.1, 10])
plt.xlabel('time', fontsize=15)
plt.ylabel('amplitude', fontsize=15)
plt.title('Complex sine wave', fontsize=20)
plt.legend(fontsize=15, loc="upper right")
plt.show()
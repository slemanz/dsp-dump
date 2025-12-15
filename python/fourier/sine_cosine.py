import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

srate = 256  # Hz
t = np.arange(0., 1., 1/srate) # time vector in seconds

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

SineWave = 3*np.sin(2*np.pi*5*t)
CosineWave  = 3*np.cos(2*np.pi*5*t)
plt.figure(figsize=(16, 9))


plt.plot(t, SineWave, 'y', linewidth=3, label='SineWave')
plt.plot(t, CosineWave, 'r', linewidth=3, label='CosineWave')

plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.title('Sine and Cosine waves comparison', fontsize=25)
plt.legend(fontsize=20, loc="upper right")
plt.xlim([0, 1])
plt.show()
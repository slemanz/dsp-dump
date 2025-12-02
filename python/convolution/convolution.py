import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

# Graphical Representation of discrete time signal

n = np.arange(-4,5)
x = [2, 1, -2, -2, 3, 2, 2, -2, 1]

plt.figure(figsize = (16, 9))

plt.stem(n, x)

plt.xlabel('time', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)

plt.show()
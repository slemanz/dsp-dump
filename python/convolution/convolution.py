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

# The convolution sum

x1 = np.array([1,2,2,1,1])
n1 = np.array([0,1,2,3,4])

plt.figure(figsize = (16,9)) # set the size of figure
plt.subplot(2, 2, 1)
markerline, stemlines, baseline = plt.stem(n1, x1, label='X1')
plt.setp(stemlines, 'linewidth', 3) 
plt.legend(fontsize = 20)
plt.xticks([0, 1, 2, 3, 4])
plt.yticks([0, 1, 2])

x2 = np.array([3, 2, 1])
n2 = np.array([0, 1, 2])
plt.subplot(2,2,2)
markerline, stemlines, baseline = plt.stem(n2, x2, label='X2')
plt.setp(stemlines, 'linewidth', 3) 
plt.legend(fontsize=20)
plt.xticks([0, 1, 2])
plt.yticks([0, 1, 2, 3])

plt.subplot(2, 2, 3)
markerline, stemlines, baseline = plt.stem(n1, x1, label='X1')
plt.legend(fontsize=20)
plt.setp(stemlines, 'linewidth', 3) 
plt.xticks([0, 1, 2, 3, 4])
plt.yticks([0, 1, 2])

f_x2 = x2[::-1] 
n3 = np.array([-2, -1, 0])
plt.subplot(2, 2, 4)
markerline, stemlines, baseline = plt.stem(n3, f_x2, label='flip_X2')
plt.setp(stemlines, 'linewidth', 3) 
plt.legend(fontsize=20)
plt.xticks([-2, -1, 0])
plt.yticks([0, 1, 2, 3])

plt.show()
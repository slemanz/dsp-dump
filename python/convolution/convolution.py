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

# Calculating convolution for mode = 'full'

nx1 = len(x1)
nx2 = len(x2)
nconv = nx1 + nx2 - 1

half_nx2 = int(np.round(nx2/2)) # Expanding x1 by zero padding
data_4_conv = np.concatenate((np.zeros(half_nx2),  x1, np.zeros(half_nx2)), axis=0) # zero padding on both sides of x1

plt.figure(figsize=(16,9)) # set the size of figure

markerline, stemlines, baseline = plt.stem(data_4_conv, label = 'data_4_conv')
plt.setp(stemlines, 'linewidth', 3) 
plt.legend(fontsize = 30)

plt.show()

# Convolution by for loops

convres = np.zeros(nconv)
for k in range(0, nconv):
    convres[k] = np.sum(f_x2 * data_4_conv[k:k+nx2])

plt.figure(figsize = (20,8)) # set the size of figure
plt.suptitle('Convolution of X1 and X2', fontsize = 30)

markerline, stemlines, baseline = plt.stem(convres)
plt.setp(stemlines, 'linewidth', 3) 
plt.show()

# Convolution by np.convolve using mode = "full"

plt.figure(figsize=(16,9)) # set the size of figure
plt.suptitle('Convolution of X1 and X2', fontsize=30)

plt.plot(convres,'g^' ,markersize=20, label='Conv using for loop')
plt.plot(np.convolve(x1, x2, mode='full'), 'r-', linewidth =3, label='Conv by np.convolve')
plt.xlabel('Sample', fontsize=15)
plt.ylabel('Value', fontsize=15)
plt.legend(fontsize=15)
plt.show()
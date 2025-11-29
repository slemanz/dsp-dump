import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import scipy
from scipy import signal

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

# Generation of unit impulse signal

x = []
n = []                  # t = nT. Since we are performing uniform sampling, therefore, T=1.

for i in range(-5,6):
    n.append(i)
    if i==0:
        x.append(1)
    else:
        x.append(0)


plt.figure(figsize = (18, 8)) # set the size of figure
plt.title('Unit Impulse', fontsize=28)

plt.stem(n,x,'yo', label='Unit impulse function')

plt.ylim(-0.01,1.2)
plt.xlim(-5,5)

plt.xlabel('time', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=20)

plt.show()

# Time Shifted Impulse (Time delay)

x = []
n = []

for i in range(-5,6):
    n.append(i)
    if i == 2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure

plt.stem(n,x,'yo', label = 'Time Shifted Impulse (Time delay)')

plt.ylim(-0.01,1.2)
plt.xlim(-5,5)

plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)

plt.show()

# Time Shifted Impulse (Time advance)

x = []
n = []

for i in range(-5,6):
    n.append(i)
    if i== -2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure

plt.stem(n,x,'yo', label = 'Time Shifted Impulse (Time advance)')

plt.ylim(-0.01,1.2)
plt.xlim(-5,5)

plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)

plt.show()

# Generation of unit step signal

x = []
n = []

for i in range(-5,10):
    n.append(i)
    if i >= 0:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure

plt.title('Unit Step', fontsize=28)

plt.stem(n, x, 'yo', label='Unit step function')
plt.ylim(0,1.5)
plt.xlim(-5,9)

plt.xlabel('time', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)

plt.show()

# Time Shifted Step (Time delay)

x = []
n = []

for i in range(-5,10):
    n.append(i)
    if i >= 2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize=(18,8)) # set the size of figure

plt.stem(n, x, 'yo', label='Time Shifted Step (Time delay)')

plt.ylim(0,1.5)
plt.xlim(-5,9)
plt.xlabel('time', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=20)

plt.show()

# Time Shifted Step (Time Advance)

x = []
n = []

for i in range(-5,5):
    n.append(i)
    if i >= -2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize=(18, 8)) # set the size of figure
plt.stem(n, x, 'yo', label='Time Shifted Step (Time Advance)')

plt.ylim(0,1.5)
plt.xlim(-5,4)

plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)

plt.show()
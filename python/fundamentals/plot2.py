import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import scipy
from scipy import signal

# Genration of Unit Impulse Signal

x = []
t = []

for i in range(-5, 6):
    t.append(i)
    if(i == 0):
        x.append(1)
    else:
        x.append(0)

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.figure(figsize = (18,8)) # set the size of figure
plt.title('Unit Impulse Signal', fontsize=28)

plt.plot(t,x,linewidth=3, label='Unit impulse function')
plt.ylim(-0.01,1)
plt.xlim(-5,5)

plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)

plt.legend(fontsize = 20)

plt.show()

# Other Genration of Unit Impulse Signal

Impulse = signal.unit_impulse(10, 'mid')
plt.figure(figsize = (18,8)) # set the size of figure

plt.plot(np.arange(-5, 5), Impulse, linewidth = 3, label = 'Unit impulse function')
plt.ylim(-0.01,1)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

# Time Shifted Impulse (Time delay)
shifted_impulse = signal.unit_impulse(7, 2)

plt.figure(figsize=(18,8)) # set the size of figure
plt.plot(shifted_impulse, linewidth=3, label='Shifted impulse function (Time delay)')

plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=20)
plt.show()

# Time Shifted Impulse (Time advance)

x = []
t = []
for i in range(-5,6):
    t.append(i)
    if i == -2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure
plt.plot(t,x,linewidth = 3, label = 'Time Shifted Impulse (Time advance)')

plt.ylim(-0.01,1)
plt.xlim(-5,5)

plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)

plt.show()

# Generation of unit step signal

x = []
t = []
for i in range(-5, 10):
    t.append(i)
    if i >= 0:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure
plt.title('Unit Step Signal', fontsize=28)

plt.plot(t,x,linewidth = 3, label = 'Unit step function')
plt.ylim(0,1.5)
plt.xlim(-5,9)

plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)

plt.show()

# Time Shifted Step (Time delay)

x = []
t = []
for i in range(-5,10):
    t.append(i)
    if i >= 2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure

plt.plot(t,x,linewidth = 3, label = 'Time Shifted Step (Time delay)')
plt.ylim(0,1.5)
plt.xlim(-5,9)

plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)

plt.show()

# Time Shifted Step (Time Advance)

x = []
t = []

for i in range(-5,5):
    t.append(i)
    if i >= -2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure

plt.plot(t,x,linewidth = 3, label = 'Time Shifted Step (Time Advance)')
plt.ylim(0,1.5)
plt.xlim(-5,4)

plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)

plt.show()


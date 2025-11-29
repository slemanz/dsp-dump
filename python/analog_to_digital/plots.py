import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

t = np.arange(0, 11)
x = (0.85)**t

# Plotting Analog Signal

plt.style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 25
plt.rcParams['ytick.labelsize'] = 25
plt.figure(figsize=(12,9))
plt.title("Analog Signal", fontsize=28)


plt.plot(t,x, linewidth=3, label='x(t) = (0.85)^t')

plt.xlabel('t' , fontsize=25)
plt.ylabel('amplitude', fontsize=25)

plt.axis([0,10,0,1])
plt.legend(fontsize = 30)
plt.axis([-0.1,10.1,0,1])

plt.xticks([0, 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.yticks([0.0, 0.1 , 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

plt.show()


# Sampling and Plotting of Sampled signal
plt.rcParams['xtick.labelsize'] = 25
plt.rcParams['ytick.labelsize'] = 25
plt.figure(figsize=(12,9))
plt.title("Sampling", fontsize=28)


n = t
plt.plot(t,x, linewidth =3, label = 'x(t) = (0.85)^t')

plt.axis([-0.1, 10.1, 0, 1])
plt.xticks([0, 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.yticks([0.0, 0.1 , 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

markerline, stemlines, baseline = plt.stem(n, x, label='x(n) = (0.85)^n')
plt.setp(stemlines, 'linewidth', 3)

plt.xlabel('n' , fontsize=25)
plt.ylabel('amplitude', fontsize=25)

plt.axis([-0.1,10.1,0,1])
plt.legend(fontsize=28)
plt.axis([-0.1,10.1,0,1])

plt.xticks([0, 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.yticks([0.0, 0.1 , 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

plt.show()

# Quantization

plt.rcParams['xtick.labelsize'] = 25
plt.rcParams['ytick.labelsize'] = 25
plt.figure(figsize=(12,9))
plt.title("Quantization", fontsize=28)


plt.plot(t,x, linewidth =3)
markerline, stemlines, baseline = plt.stem(n, x)
plt.setp(stemlines, 'linewidth', 3)

plt.xlabel('n', fontsize=25)
plt.ylabel('Range of Quantizer', fontsize=25)

plt.axis([-0.1, 10.1, 0, 1])
plt.xticks([0, 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.yticks([0.0, 0.1 , 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.axhline(y=0.1, xmin=0, xmax=10, color='r', linewidth=3.0)
plt.axhline(y=0.2, xmin=0, xmax=10, color='r', linewidth=3.0)
plt.axhline(y=0.3, xmin=0, xmax=10, color='r', linewidth=3.0)
plt.axhline(y=0.4, xmin=0, xmax=10, color='r', linewidth=3.0)
plt.axhline(y=0.5, xmin=0, xmax=10, color='r', linewidth=3.0)
plt.axhline(y=0.6, xmin=0, xmax=10, color='r', linewidth=3.0)
plt.axhline(y=0.7, xmin=0, xmax=10, color='r', linewidth=3.0)
plt.axhline(y=0.8, xmin=0, xmax=10, color='r', linewidth=3.0)
plt.axhline(y=0.9, xmin=0, xmax=10, color='r', linewidth=3.0)
plt.axhline(y=1.0, xmin=0, xmax=10, color='r', linewidth=3.0)

plt.show()

#   Quantized Signal

xq = np.around(x,1)   # Converting discrete into quantized Signal

plt.rcParams['xtick.labelsize'] = 25
plt.rcParams['ytick.labelsize'] = 25
plt.figure(figsize = (16,12)) # set the size of figure
plt.title('Quantized Signal', fontsize = 28)


plt.xticks([0, 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.yticks([0.0, 0.1 , 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 ])
plt.axis([-0.1,10.1,0,1])

plt.axhline(y = 0.1, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.2, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.3, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.4, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.5, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.6, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.7, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.8, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.9, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 1.0, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)

markerline, stemlines, baseline = plt.stem(n, xq)
plt.setp(stemlines, 'linewidth', 3) 

plt.show()
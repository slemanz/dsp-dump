import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

t = np.arange(0, 11)
x = (0.85)**t

# Plotting Analog Signal

plt.style.use('dark_background')
plt.figure(figsize=(12,9))
plt.title("Analog Signal", fontsize = 28)

plt.rcParams['xtick.labelsize'] = 25
plt.rcParams['ytick.labelsize'] = 25

plt.plot(t,x, linewidth =3, label = 'x(t) = (0.85)^t')

plt.xlabel('t' , fontsize = 25)
plt.ylabel('amplitude', fontsize = 25)

plt.axis([0,10,0,1])
plt.legend(fontsize = 30)
plt.axis([-0.1,10.1,0,1])

plt.xticks([0, 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.yticks([0.0, 0.1 , 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])


plt.show()
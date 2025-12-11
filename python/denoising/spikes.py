import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

signal = pd.read_csv("spike.csv")

signal = np.array(signal)
spiky = abs(signal)

style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

plt.figure(figsize=(16, 9)) # set the size of figure
plt.plot(spiky, label='signal with Spikes')
plt.legend(fontsize = 25)
plt.show()

# use hist to pick threshold

plt.figure(figsize=(16, 9))
plt.hist(spiky, 50)
plt.show()

# Using np.where to find the indices of spiky signal having magnitude greater than 50
threshold = 50

# find signal values above the threshold value
ultra_thresh = np.where(spiky > threshold)[0]

filtsig = np.copy(spiky)

N = 100

# Applying Median Filter

for ii in range(0,ultra_thresh.shape[0]):
    filtsig[ultra_thresh[ii]] = np.median(spiky[ultra_thresh[ii]:ultra_thresh[ii]+N])

plt.figure(figsize=(16, 9))
plt.plot(spiky, 'g', label='Spiky Signal')
plt.plot(filtsig, 'r', label='Filtered Signal')
plt.legend(fontsize=20)
plt.show()
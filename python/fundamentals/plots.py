import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Create a time array
t = np.linspace(0, 2, 500)

# Damped sine wave: amplitude decreases with exp(-αt)
alpha = 0.7   # damping factor
freq = 1      # frequency in Hz
y = 25 * np.exp(-alpha * t) * np.sin(2 * np.pi * freq * t)

# Dark background style
plt.style.use("dark_background")

plt.figure(figsize=(12, 5))
plt.plot(t, y, linewidth=3, label='Continuous Signal')

plt.xlabel('time.')
plt.ylabel('Amplitude')
plt.title('')
plt.legend()

plt.grid(False)
plt.show()

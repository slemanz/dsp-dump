import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')


z = 5 + 6j

# Magnitude of a Number
mag_z = np.sqrt(np.real(z)**2 + np.imag(z)**2)
print("Magnitude =", mag_z)

# Angle with positive real axis
ang_z = np.angle(z)
print("Angle =", ang_z)

print("Angle in degrees =", ang_z*57.3) # angle in degrees

plt.figure(figsize=(16, 9))

plt.plot(np.real(z), np.imag(z), 'mo', markersize=15, label='(5+6j)')

plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.plot([-10, 10], [0, 0], 'g',lw=3)
plt.plot([0, 0], [-10, 10], 'g', lw=3)
plt.plot([0, 5], [0, 6], 'r-', lw=3)

plt.xlabel('Real axis', fontsize=15)
plt.ylabel('Imaginary axis', fontsize=15)
plt.title('Complex Plane', fontsize=25)
plt.legend(fontsize=15)
plt.show()
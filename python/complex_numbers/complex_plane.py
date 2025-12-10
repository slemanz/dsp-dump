import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')

# Few methods of creating complex numbers

z1 = 5 + 6j
z2 = 5 + 6*1j
z3 = complex(5,6)

print(z1)
print(z2)
print(z3)

# Extracting Real and Imaginary part of complex number.

print(np.real(z1))
print(np.imag(z1))

# Plotting a complex numbers on complex plane

z1 = complex(3,0)
z2 = complex(-7,0)
z3 = complex(2,3)
z4 = complex(0,5)

plt.figure(figsize=(16, 9))

plt.plot(np.real(z1), np.imag(z1), 'yo', markersize=15, label='(3)' )
plt.plot(np.real(z2), np.imag(z2), 'mo', markersize=15, label='(-7)' )
plt.plot(np.real(z3), np.imag(z3), 'bo', markersize=15, label='(2+3j)' )
plt.plot(np.real(z4), np.imag(z4), 'ro', markersize=15, label='(5j)' )

plt.xlim([-10, 10])
plt.ylim([-10, 10])

plt.plot([-10, 10], [0, 0], 'g', lw=3)
plt.plot([0, 0], [-10, 10], 'g', lw=3)
plt.plot([0, 2], [0, 3], 'r-', lw=3)

plt.xlabel('Real axis', fontsize=20)
plt.ylabel('Imaginary axis', fontsize=20)
plt.title('Complex Plane', fontsize=25)
plt.legend(fontsize=15)
plt.show()
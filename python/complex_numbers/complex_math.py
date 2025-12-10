import numpy as np

z1 = 2 + 3j
z2 = 7 + 5j

# Extracting real and imaginary parts of both complex numbers.

z1_r = np.real(z1)
z1_i = np.imag(z1)
z2_r = np.real(z2)
z2_i = np.imag(z2)

ZM = (z1_r   +   1j*z1_i) * (z2_r   +    1j*z2_i)

print(ZM)

### COMPLEX CONJUGATE OF A NUMBER ###

z1 = 4 + 3j

c_conj_z1 = np.conj(z1) # complex conjugate

print("Conjugate:", c_conj_z1)

## Important property of a complex Number

Mag_square = z1 * c_conj_z1
print(Mag_square)

print("Mag:", np.abs(z1)**2)

## Division of Complex Numbers ##
z1 = 2 + 3j
z2 = 7 + 5j

ZD = z1 / z2
print ("Division", ZD)
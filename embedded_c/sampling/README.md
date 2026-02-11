# Quantization and Sampling

Quantization is the process of mapping continuous infinite values to a smaller
set of discrite finite values.

- **The sample and hold** sub-module converts independent variables (x-axis
value) from continuous to discrete.

- **The quantizer** sub-module converts dependent variables (y-axis values) from
continuous to discrete.

## Sampling Theorem

The sampling theorem states that a continuous signal can properly be sample only
if it does not contain frequency components above half of the sampling rate.

E.g: if we are sampling at 50 Hz (50 samples/second), the analog signal we are
sampling must be made of frequencies from 25 Hz (25 cycles/second) and below.

This is also known as Nyquist Theorem.

# DSP System Based on the Sampling Theorem
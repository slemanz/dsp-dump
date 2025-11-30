# Sampling and Reconstruction

A continuous time signal $x(t)$ can be converted into discrete time signal $x(n)$
by replacing $t$ with $nT$.

$$x(n) = x(nT)$$

where $x(n)$ is the discrete time signal obtained by taking samples of the
continuoue time signal $x(t)$ every $T$ seconds. The time interval $T$ between
successive samples is called the sampling period or sample interval and is given
by

$$T = \dfrac{1}{f_s}$$

where $f_s$ is called the sampling rate or the sampling frequency (Hertz).

## Nyquist sampling theorem

The Nyquist sampling theorem states that “the sampling frequency fs should be
greater or equal than twice the maximum frequency of the signal (continuous
time signal) to be sampled."

If $F_{max}$ is the maximum frequency of the signal then according to sampling
theorem

$$f_s \geq 2F_{mах}$$

Sampling theorem is very important if we want to reconstruct the signal
after sampling.

**Sampling a Sine wave of Fmax = 20Hz with fs = 35 Hz:**


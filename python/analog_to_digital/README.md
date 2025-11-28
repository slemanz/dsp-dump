# Analog to Digital Conversion

![](ad.svg)

**Example:**

Consider the following Analog signal

![](analog.png)

Our analog signal is given by: $x(t) = (0.85)^t$

For sampling, we have to define a sampling interval, T. We define sampling
interval by setting sampling frequency “f,”. For simplicity suppose

$f_s = 1Hz$

$T = \dfrac{1}{f_s}$

$T = 1s$

For sampling replace $t = nT$

Thus,

$x(nT) = (0.85)^{nT}$

Since $T = 1s$, therefore,

$x(n) = (0.85)^n$

$x(n)$ is the discrete time signal with sampling interval of 1s.

![](sampling.png)
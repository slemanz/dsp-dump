# Denoising

## Signal Denoising by Moving Average Filter

$$y(n) = \dfrac{1}{M}\sum^{M-1}_{i=0} x(n+1)$$

If we have a five point filter moving on the 10th point then for symmetrically
chosen points.

$$y[10] = \dfrac{y[8]+y[9]+y[10]+y[11+y[12]]}{5}$$

The other possibility is

$$y[10] = \dfrac{y[10]+y[11]+y[12]+y[13+y[14]]}{5}$$

[Code](moving_average.py)

![](plots/moving_noise.png)

![](plots/moving_filter.png)

## Gaussian Average or Gaussian Mean Filter

$$ GaussianFilter = e^{\frac{-4ln(2)t^2}{(f\omega h m)^2}} $$

Where $f\omega hm$ is an important parameter of Gaussian and is called full width
half maximum. The spread of the Gaussian depends upon this parameter. It is
approximately 2.4 times the standard deviation.

[Code](gaussian_mean.py)

![](plots/gaussian_noise.png)

**Gaussian filter/kernel**

![](plots/gaussian_kernel.png)

**Zero padding the noisy siganl to avoid edge effect**

![](plots/gaussian_zero.png)

**Filtered signal**

![](plots/gaussian_filtered.png)

**Clipped filtered signal**

![](plots/gaussian_filtered_clipped.png)
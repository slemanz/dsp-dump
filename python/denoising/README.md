# Denoising

## Signal Denoising by Moving Average Filter

$$y(n) = \dfrac{1}{M}\sum^{M-1}_{i=0} x(n+1)$$

If we have a five point filter moving on the 10th point then for symmetrically
chosen points.

$$y[10] = \dfrac{y[8]+y[9]+y[10]+y[11+y[12]]}{5}$$

The other possibility is

$$y[10] = \dfrac{y[10]+y[11]+y[12]+y[13+y[14]]}{5}$$
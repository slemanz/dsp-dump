# Convolution

## Representing a discrete time signal

Following are the two commonly used methods for representing a
signal.

1. Sequential method.
2. Graphical method.

## Sequential Representation of discrete time signal

Sequential representation of discrete time signal is shown below

$$x(n) = [2,1,-2,-2,3,2,2,-1,1]$$

## Graphical Representation of discrete time signal

![](plots/graphical.png)

## The Convolution Sum

The response or the convolution sum $y(n)$ of the two input signals $x_1(n)$ and
$x_2(n)$ is defined by the following equation.

$y(n) = x_1(n)  \circledast x_2(n)$

$x_2(n)$ is called kernel or filter.

## Steps for performing convolution sum

1. Flipping/Folding.
2. Shifting.
3. Multiplication.
4. Addition.

$y(n) = x_1(n)  \circledast x_2(n)$

$y(n) = \sum_{k=0}^{N-1} x_1(k)x_2(n-k)$

$x_2(n)$ is called kernel or filter.

## Example

![](plots/conv_sum.png)

**The output sequence:**

![](plots/mode_full.png)

## Convolution for mode = “full"

The number of samples in first signal = $nx_1 = 5$

The number of samples in the kernel = $nx_2 = 3$

Number of samples in output sequence = nconv = $nx_1 + nx_2 - 1 = 5 + 3 - 1 = 7$

### More Examples in Python

**Convolution by for loops:**

![](plots/for_loop.png)

**Convolution by np.convolve using mode="full":**

![](plots/conv_full.png)

**Convolution by np.convolve using mode="same":**

![](plots/conv_same.png)

## Aplications

### Denoising

[Code](denoising.py)

![](plots/denoising_1.png)

![](plots/denoising_2.png)

![](plots/denoising_3.png)

### Edge Detection Using Convolution

[Code](edge.py)

![](plots/edge.png)

![](plots/edge_kernel.png)

![](plots/edge_filtered.png)

![](plots/edge_detection.png)

## The Convolution Theorem

In mathematics, the convolution theorem states that under suitable conditions
the Fourier transform of a convolution of two functions (or signals) is the
product of their Fourier transforms. More generally, convolution in one domain
(e.g., time domain) equals point-wise multiplication in the other domain (e.g.,
frequency domain). Other versions of the convolution theorem are applicable to
various Fourier-related transforms.

[Code](theorem.py)

![](plots/theorem.png)


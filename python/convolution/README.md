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
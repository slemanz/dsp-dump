# Signal Statistics and Noise

## Introduction to Signals

What is a signal?

- A signal describes how one parameter relates to another.

Continuous vs Discrete Signal

- Signal in the real-world are continuous by nature
- Passing a continous signal through an analog-to-digial converter converts it
to a digitized or discrete signal.

Independent vs Dependent Variables

- A signal is made up of two parameters, the independent variable and the
dependent variable.
- The vertical axis represents the dependent variable while the horizontal axis
represents hte independent variable.
- The dependent variable (y-axis) is a function of the independent variable
(x-axis)
- The independent variable describes how and when a sample is taken, the
dependent variable is actual measurement.

Signal Samples

- Each digitized signal point is known as a sample.
- The total number of sample is denoted by **N**

## Mean and Standard Deviation

- The mean is the average of a signal
- It is found by adding all samples together and the dividing the sum by the
total number of samples (*N*)
- The mean is denoted by $\mu$, pronounced **mu**
- In electronics, the mean is known as the **DC value**

$$ \mu = \dfrac{1}{N}\sum^{N-1}_{i=0} x_i $$

- The standard devition is a measure of how far the signal fluctuates from the
mean.
- The power of this fluctuation is known as the variance.
- The standard deviation iss denoted by $\sigma$, pronounced **sigma**

$$ \sigma = \sqrt{\dfrac{1}{N-1} \sum^{N-1}_{i=0}(x_i - \mu)^2}$$

$$ \sigma = \sqrt{\dfrac{(x_0 - \mu)^2 + (x_1 - \mu)^2 + ... + (x_N - \mu)^2}{N-1}}$$

- The **variance** is computed by squaring the standard deviation $\mu^2$

$$ \mu^2 = \dfrac{1}{N}\sum^{N-1}_{i=0} (x_i - \mu)^2 $$

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

### Application

**[Source code](Src/main.c)**

The mean:

```C
float32_t signal_mean(float32_t *sig_src_arr, uint32_t sig_length);
arm_mean_f32(sig_src_arr, sig_length, &g_mean_value); // cmsis
```

- **Identifying DC Offset:** Most real-world sensors (like microphones or heart
rate monitors) add a constant electrical voltage to the signal. This "tilt" can
mess up further calculations. The mean tells you exactly how much to shift the
signal back to zero.

- **Noise Reduction:** If you have a static signal buried in random white noise,
the mean of that noise over time is usually zero. By averaging multiple samples,
the random noise cancels itself out, leaving you with the "true" underlying
value.

- **Energy Calculations:** To calculate the Variance or Standard Deviation
(which represents the AC power or "shakiness" of a signal), you must first know
the mean.

**Note:** The CMSIS version is highly optimized to run faster by using
hardware-specific instructions.

The variance:

```C
float32_t signal_variance(float32_t *sig_src_arr, float32_t sig_mean, uint32_t sig_length);
arm_var_f32(sig_src_arr, sig_length, &g_variance_value); // cmsis
```

- **Measuring Signal Power (AC):** Variance represents the average power of the
AC (varying) part of a signal. In communication systems (like Wi-Fi or Radio),
engineers need to know how strong the actual data signal is compared to the
static background.

- **Quantifying Noise (SNR):** Variance is the primary tool for measuring Noise.
If you have a sensor sitting perfectly still and the reading is "jittery," the
variance of those readings tells you exactly how "noisy" your sensor is. This is
crucial for calculating the Signal-to-Noise Ratio (SNR).
    - Low Variance: Clean signal, very little noise.
    - High Variance: Corrupted signal, hard to distinguish data from "static."

- **Step Detection and Activity Monitoring:** In wearable devices like a Fitbit,
variance is used to detect movement.
    - If you are sitting still, the variance of the accelerometer data is near
    zero.
    - When you start walking, the signal starts swinging wildly, causing the
    variance to spike. This spike triggers the "step counting" algorithm.

The Standard Deviation:

```C
float32_t signal_std(float32_t sig_variance);
arm_std_f32(sig_src_arr, sig_length, &g_std_value);
```

- **Defining "Normal" vs. "Anomaly":** In DSP, we often use the 68 − 95 − 99.7 rule.
    - Roughly 68% of your signal samples will fall within ±1 standard deviation
    of the mean.
    - If a new sample comes in that is 3 or 4 standard deviations away, your
    algorithm can flag it as an anomaly or a "glitch." This is how
    spike-rejection filters work.

- **Signal-to-Noise Ratio (SNR):** Standard deviation is used to calculate the
RMS (Root Mean Square) amplitude of noise. When you see a datasheet for a
high-end ADC (Analog-to-Digital Converter) that says "Low Noise," they are
usually defining that noise in terms of its standard deviation.

- **Setting Dynamic Range:** If you know the standard deviation of your input
signal, you can set your gains and thresholds correctly. For example, if you
know your signal has a $\sigma = 0.5V$, you know that a range of 2V (which is
$4\sigma$) will capture almost every single peak without clipping.
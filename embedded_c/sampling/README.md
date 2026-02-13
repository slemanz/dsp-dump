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

## DSP System Based on the Sampling Theorem

```
Analog Filter (analog input) -> ADC ->Digital processing -> DAC -> Analog Filter
```

- Before the analog signal enters the ADC it is first passd through an analog
filter.
- This filter removes frequency components above half of the sampling rate. A
filtered analog signal is produced by this filter
- If we wish to reconstruct our final analog signal, we can pass the output from
our digital processing through a digital-to-analog-converter (DAC).
- This output filter is called the reconstruction filter.

## Analog Filters

### Passive Low-Pass Filter

- This filter passes low frequencies and blocks high frequencies.
- It is constructed using only resistors and capacitors, it is also called RC
passive lowpass filter.

```
          R
Vin o--/\/\/\--+---o Vout
               |
              === C
               |
              GND
```

- The range of frequencies for which a filter does not cause significant
attenuation is called the **passband**.
- The range of frequencies for which the filter does cause significant
attenuation is called the **stopband**.
- The **cuttof frequency** of an RC filter is the frequency at which the
amplitude of the input signal is reduced by 3db.
- It is denoted by $f_c$.
- 3db reduction in amplitude corresponds to a 50% reduction in power.

- How does this work?
    - At high frequency capacitor becomes a short circuit.
    - At low frequency capacitor is an open circuit.
    - $f_c = \dfrac{1}{2\pi RC}$

### Passive High-Pass Filter

- This filter passs high frquencies and blocks low frequencies.
- It is constructed using only resistors and capacitors hence RC.

```
       C
Vin o--||--+---o Vout
           |
           <
           > R
           <
           |
          GND
```

- How does this work?
    - At high frequency capacitor becomes a short circuit.
    - At low frequecy capacitor is an open circuit.
    - $f_c = \dfrac{1}{2\pi RC}$

### Passive vs Active Filters

- Passive filters are made up of passive components only.
- Examples of passive components include resistors, capacitors and inductors.
- Active filters are made up of both passive and active components.
- Examples of active components include operational amplifiers and transistors.
- One advantage of active filters over passive filters is ther ability to
provide signal gain (i.e amplify the signal)

**Most common configurations:**

- Analog filters often used in realworld applications include:
    - Chebyshev
    - Butterworth
    - Bessel
- Each of these filters is designed to optimize a different performance
parameter.
- The complexity of each filter can be adjusted by selecting the number of polos
and zeros.
- The more poles of in a filter, the more electronics it requires, and the
better it performs.

### Modified Sallen Key Filter

- The modified sallen-key filter servers ad a building block for designing
active filters such as Chebyshev, butterworth and bessel.
- $ R = \dfrac{k_1}{Cf_c} $, $ R_f = R_1k_2$

```
C1
           +-----||-----+
           |            |
       R   |    R       |         |\
Vin o-/\/\-+---/\/\/-+--+---------|+\
                     |            |  >---+---o Vout
                    === C2 +------|-/    |
                     |     |      |/     <
                    GND    |             > Rf
                           |             <
                           |             |
                           +-------------+
                                         |
                                         <
                                         > R1
                                         <
                                         |
                                        GND
```

### Butterworth, Chebyshev and Bessel filters

```
[STAGE 1: BUTTERWORTH]                             [STAGE 2: CHEBYSHEV]                               [STAGE 3: BESSEL]
                    C1A                                                C1B                                                C1C
              +-----||-----+                                     +-----||-----+                                     +-----||-----+
              |            |                                     |            |                                     |            |
          R   |    R       |         |\                  R       |    R       |         |\                  R       |    R       |         |\
Vin o----/\/\-+---/\/\/-+--+---------|+\           +----/\/\/\---+---/\/\/-+--+---------|+\           +----/\/\/\---+---/\/\/-+--+---------|+\
                        |            |  >----------+                       |            |  >----------+                       |            |  >---+---o Vout
                       === C2A +-----|-/          |                      === C2B  +-----|-/           |                      === C2C +-----|-/     |
                        |     |      |/            <                       |      |     |/            <                       |      |     |/      <
                       GND    |                    > RfA                  GND     |                   > RfB                  GND     |             > RfC
                              |                    <                              |                   <                              |             <
                              |                    |                              |                   |                              |             |
                              +--------------------+                              +-------------------+                              +-------------+
                                                   |                                                  |                                            |
                                                   <                                                  <                                            <
                                                   > R1A                                              > R1B                                        > R1C
                                                   <                                                  <                                            <
                                                   |                                                  |                                            |
                                                  GND                                                GND                                          GND
```
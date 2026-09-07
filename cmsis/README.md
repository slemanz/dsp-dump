# The CMSIS-DSP Library

Every chapter before this one used the library and explained the one call it
needed. This one is the library itself, and it closes the repository.

Arm publishes several hundred functions here, and they are not several hundred
things to learn. They are a handful of rules applied consistently, and once the
rules are in place the reference manual becomes an index rather than a course.

## Four Rules

```
arm_<operation>_<type>              the name
(pSrcA, pSrcB, pDst, blockSize)     the order, sources first
void or arm_status                  whether the call can refuse
instance and init                   whether the routine has to remember
```

The type suffix is the number format from the fixed point chapter: `f64`, `f32`,
`f16`, `q31`, `q15`, `q7`. Most operations exist in most of them and behave the
same way, which makes choosing a format a decision about the whole program
rather than about each call.

The argument order has exactly one variation and it is not an inconsistency.
`arm_dot_prod_f32` takes the length before the destination, because its result
is a single number and there is no block for the length to describe.

The return type is the cheapest documentation in the library. `void` means the
call cannot be given a request it must refuse. `arm_status` means it can, and
almost every one of those is an init. An init whose status is ignored is a
transform that silently does nothing on an uninitialised instance.

## The Rule That Sorts the Rest

One question decides which half of the library a routine is in, and it answers
several others at once:

| | |
| --- | --- |
| output n depends on input n only | no instance, and it works in place |
| output n depends on more than that | instance, init, state buffer |

That is more useful than any list, because it tells you which side a function
you have not met yet will fall on. [`lib_blocks`](app/Src/lib_blocks.c) tests
the in-place half rather than trusting it, and every elementwise routine passes:
`add`, `sub`, `mult`, `scale`, `offset`, `negate`, `abs`, `clip`.

A filter cannot, because output $n$ needs inputs $n$ through $n - \text{numTaps}$.
A transform cannot, because it needs all of them. Routines that want scratch
space ask for it in the arguments rather than borrowing yours.

## The State Buffer Is Yours

The stateful half always goes declare, init, call:

```c
arm_fir_instance_f32 fir;
arm_fir_init_f32(&fir, numTaps, pCoeffs, pState, blockSize);
arm_fir_f32(&fir, pSrc, pDst, blockSize);
```

The state buffer holds the overlap between one call and the next, which is where
the block chapter ends up, and its size is fixed by that job:

| routine | state | floats here |
| --- | --- | --- |
| `arm_fir_f32` | `numTaps + blockSize - 1` | 63 |
| `arm_biquad_cascade_df2T_f32` | 2 per stage | 4 |
| `arm_rfft_fast_f32` | none, the tables are the instance | 0 |

The library does not allocate it and does not check its length, so a wrong
formula writes past the end of an array and the symptom appears somewhere else.

## FIR or Biquad

The choice nobody spells out, from [`lib_stateful`](app/Src/lib_stateful.c):

| | FIR | biquad |
| --- | --- | --- |
| coefficients | 32 | 10 |
| state floats | 63 | 4 |
| phase | linear | not |
| can ring forever | no | yes |
| can be unstable | no | yes |

The biquad does a similar job with a sixth of the arithmetic and pays for it by
feeding its output back in, which is where both the instability and the
nonlinear phase come from. That is why every filter in this repository up to now
has been an FIR.

Its coefficients go in as `b0 b1 b2 a1 a2` per stage with `a1` and `a2` already
negated. scipy hands them back with the opposite sign, so a design copied
straight across gives a filter that is not the one that was designed.

## Two Things the Statistics Group Does Not Say

[`lib_stats`](app/Src/lib_stats.c) found both of these by checking an identity
from the very first chapter, and both change numbers that chapter reported.

**`arm_power_f32` is the sum of squares, not the mean.** The name suggests mean
square, which is what `arm_rms_f32` squares back down from. This one grows with
the block length, so it is not comparable between blocks of different sizes.

**`arm_var_f32` and `arm_std_f32` divide by $N-1$, not $N$.** That is the sample
variance, correct when the block is a sample of something larger and wrong when
the block is the whole signal:

```
rms^2 - mean^2              0.236671
times N/(N-1) = 256/255     0.237599
arm_var_f32 returned        0.237599
```

At 256 samples the difference is 0.4% and invisible. At 8 samples it is 14%, and
a routine reporting noise per short block will be wrong by that much, always in
the same direction.

## Which Call, for Which Question

The library's own documentation is organised the way a library has to be, by
what the functions are. [`lib_choose`](app/Src/lib_choose.c) is organised by
what you were trying to do when you went looking, which is the order they are
needed in.

| I want to | call |
| --- | --- |
| add, subtract or multiply two signals | `arm_add / sub / mult _f32` |
| multiply by a constant, or add one | `arm_scale_f32`, `arm_offset_f32` |
| hold it inside a range | `arm_clip_f32` |
| one number out of two signals | `arm_dot_prod_f32` |
| know how big it is, ignoring sign | `arm_rms_f32` |
| know how much it varies | `arm_std_f32` |
| know if it is clipping | `arm_absmax_f32`, then compare |
| filter a block, and keep filtering | `arm_fir_f32` |
| convolve two finite signals | `arm_conv_f32` |
| find one signal inside another | `arm_correlate_f32` |
| filter cheaply, phase no object | `arm_biquad_cascade_df2T_f32` |
| resample down or up | `arm_fir_decimate_f32`, `arm_fir_interpolate_f32` |
| the spectrum of a real signal | `arm_rfft_fast_f32` |
| magnitude from its packed output | `arm_cmplx_mag_f32` |
| change number format | `arm_float_to_q15` and friends |

The app prints the full card and stops, which makes it the one to leave on the
terminal while writing something else.

## When It Is Worth Calling

A library routine has a fixed cost before it does any work: the call, the
instance to read, the loop to set up. On a long block that is nothing; on a short
one it can be most of the call, so there is a crossover.
[`lib_cost`](app/Src/lib_cost.c) measures where it sits for `arm_add_f32` and
`arm_dot_prod_f32` against plain loops, which is the measurement the block
chapter promised.

The crossover is not the whole decision, though. A hand written loop that is
right today is a loop somebody has to keep right, and every convention on this
page is somewhere it can go quietly wrong.

## Seven Ways to Get a Wrong Answer That Compiles

[`lib_traps`](app/Src/lib_traps.c) gathers every place this repository got
caught. None of them is a criticism of the library; most are documented, and the
rest are consequences of decisions that were correct for the library and
surprising from outside it. What they have in common is that not one of them
announces itself.

1. `arm_fir` wants the taps time reversed, and a symmetric kernel hides it
   completely.
2. The transform output is packed: slot 0 is bin 0, slot 1 is bin $N/2$, then
   real and imaginary pairs.
3. `arm_rfft_fast_init_f32` refuses lengths below 32 and says so only in its
   return value.
4. `arm_var_f32` divides by $N-1$.
5. `arm_power_f32` returns a sum, not a mean.
6. `arm_float_to_q15` truncates rather than rounds, doubling the error spread.
7. The generic transform init carries every twiddle table, at about 78 kB.

Plus three that each needed a chapter: the transform's negated sine convention,
q15 headroom being $\sum |h|$ rather than $\sum h$, and the biquad's
pre-negated denominator.

The seventh trap has a postscript worth reading. This app weighs about 107 kB
and [`lib_choose`](app/Src/lib_choose.c) weighs about 23, and the entire
difference is that demonstrating the third trap needs an init that can refuse,
which means the generic one, which means the tables. The trap catching the app
that explains it is the lesson in one column of `arm-none-eabi-size`.

## Watching the Signals in Ozone

This chapter is mostly conventions, so most of what it has to say is on the
terminal. The graph carries the one thing worth seeing:

| probe | carries |
| --- | --- |
| `g_in` | the signal going in |
| `g_out` | what a library routine returned |
| `g_ref` | the same thing computed another way |
| `g_gap` | the difference |

When the conventions have been read correctly `g_gap` is a flat line at zero.
When they have not, the shape of what is left says which convention was missed,
which is the same diagnostic the block chapter used for seams.

`STEP_MS` is 100 rather than a few milliseconds, because the sampler misses
points at the faster rate.

## Apps

Each app is a self-contained `main` that prints its tables once and then streams
the probes, so `make monitor` catches the output and the Timeline shows the
traces. Only the timing app needs the board.

0. [The conventions](app/Src/lib_naming.c): one operation in three formats with
   the identical shape of call, the two argument orders and why the second is
   not an inconsistency, and the return type as the cheapest documentation in
   the library.
1. [The stateless half](app/Src/lib_blocks.c): the elementwise group with each
   one tested for whether it works in place, and the rule that predicts the
   answer for routines not on the list.
2. [The stateful half](app/Src/lib_stateful.c): declare, init, call, with the
   state buffer size for each and an FIR set against a biquad on the terms that
   actually decide between them.
3. [Asking about a signal](app/Src/lib_stats.c): the statistics group used for
   real questions, including the two whose names promise something other than
   what they return.
4. [The reference card](app/Src/lib_choose.c): the library indexed by the
   question rather than by the category, printed and left on screen.
5. [Library against loop](app/Src/lib_cost.c): where the fixed cost of a call
   stops mattering, measured for two routines across block lengths from 4 to
   256.
6. [Everywhere this went wrong](app/Src/lib_traps.c): seven traps demonstrated
   in a few lines each, three more pointed at the chapter that measured them,
   and a size column in which the app catches itself.


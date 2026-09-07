/*
 * Every place this repository got caught, in one list.
 *
 * These are not criticisms of the library. Most of them are documented, and the
 * ones that are not are consequences of decisions that were correct for the
 * library and surprising from outside it. What they have in common is that none
 * of them announces itself: in every case the code compiles, runs, produces
 * numbers, and the numbers are wrong.
 *
 * They are gathered here because they were found one at a time across seven
 * chapters, and finding them one at a time is the expensive way.
 *
 * The ones that can be demonstrated in a few lines are demonstrated. The rest
 * point at the chapter that measured them.
 *
 *     make lib_traps && make load && make monitor
 */

#include <stdio.h>
#include "config.h"
#include "probe.h"
#include "testsig.h"

#define SMALL       8U
#define FFT_LEN     32U

static float32_t fft_in[FFT_LEN];
static float32_t fft_out[FFT_LEN];

int main(void)
{
    config_app();
    probe_reset();

    printf("\r\nseven ways to get a wrong answer that compiles\r\n");

    /* 1. the coefficient order */
    {
        float32_t h[3] = { 0.5f, 0.3f, 0.2f };
        float32_t flip[3] = { 0.2f, 0.3f, 0.5f };
        float32_t impulse[SMALL] = { 1.0f };
        float32_t state[3U + SMALL - 1U];
        float32_t got[SMALL];
        arm_fir_instance_f32 fir;

        printf("\r\n1. arm_fir wants the taps time reversed\r\n\r\n");

        arm_fir_init_f32(&fir, 3U, h, state, SMALL);
        arm_fir_f32(&fir, impulse, got, SMALL);
        printf("   taps as written    %.2f %.2f %.2f\r\n",
               (double)got[0], (double)got[1], (double)got[2]);

        arm_fir_init_f32(&fir, 3U, flip, state, SMALL);
        arm_fir_f32(&fir, impulse, got, SMALL);
        printf("   taps reversed      %.2f %.2f %.2f\r\n",
               (double)got[0], (double)got[1], (double)got[2]);
        printf("   a symmetric kernel hides this completely\r\n");
    }

    /* 2. the packed transform output */
    {
        arm_rfft_fast_instance_f32 fft;

        for (uint32_t i = 0U; i < FFT_LEN; i++)
        {
            fft_in[i] = 1.0f;
        }

        (void)arm_rfft_fast_init_f32(&fft, FFT_LEN);
        arm_rfft_fast_f32(&fft, fft_in, fft_out, 0U);

        printf("\r\n2. the transform output is packed, not a plain array\r\n\r\n");
        printf("   a constant signal, first four slots: %.1f %.1f %.1f %.1f\r\n",
               (double)fft_out[0], (double)fft_out[1], (double)fft_out[2],
               (double)fft_out[3]);
        printf("   slot 0 is bin 0, slot 1 is bin N/2, then re,im pairs\r\n");
        printf("   reading it as pairs puts the nyquist bin where bin 1"
               " belongs\r\n");
    }

    /* 3. the init that refuses */
    {
        arm_rfft_fast_instance_f32 fft;

        printf("\r\n3. an init can refuse, and returning void is not the"
               " same as\r\n   succeeding\r\n\r\n");
        printf("   arm_rfft_fast_init_f32(&fft, 32)  status %d\r\n",
               (int)arm_rfft_fast_init_f32(&fft, 32U));
        printf("   arm_rfft_fast_init_f32(&fft,  8)  status %d\r\n",
               (int)arm_rfft_fast_init_f32(&fft, 8U));
        printf("   ignore the second and the transform runs on an"
               " uninitialised\r\n   instance\r\n");
    }

    /* 4. variance divides by N-1 */
    {
        float32_t rms;
        float32_t mean;
        float32_t var;

        arm_rms_f32(sig, SIG_LEN, &rms);
        arm_mean_f32(sig, SIG_LEN, &mean);
        arm_var_f32(sig, SIG_LEN, &var);

        printf("\r\n4. arm_var_f32 and arm_std_f32 divide by N-1\r\n\r\n");
        printf("   rms^2 - mean^2       %.6f\r\n",
               (double)((rms * rms) - (mean * mean)));
        printf("   arm_var_f32          %.6f\r\n", (double)var);
        printf("   the ratio is N/(N-1), invisible at %lu and 14%% at 8\r\n",
               (unsigned long)SIG_LEN);
    }

    /* 5. power is a sum */
    {
        float32_t power;
        float32_t rms;

        arm_power_f32(sig, SIG_LEN, &power);
        arm_rms_f32(sig, SIG_LEN, &rms);

        printf("\r\n5. arm_power_f32 is the sum of squares, not the mean\r\n\r\n");
        printf("   arm_power_f32        %.4f\r\n", (double)power);
        printf("   divided by N         %.6f\r\n",
               (double)(power / (float32_t)SIG_LEN));
        printf("   rms squared          %.6f\r\n", (double)(rms * rms));
        printf("   so it doubles when the block doubles\r\n");
    }

    /* 6. float to q15 truncates */
    {
        float32_t f[4] = { 0.1f, 0.25f, 0.3f, 0.7f };
        q15_t q[4];
        float32_t back[4];

        arm_float_to_q15(f, q, 4U);
        arm_q15_to_float(q, back, 4U);

        printf("\r\n6. arm_float_to_q15 truncates rather than rounds\r\n\r\n");
        printf("   %10s %14s %14s\r\n", "wanted", "came back", "error, steps");

        for (uint32_t i = 0U; i < 4U; i++)
        {
            printf("   %10.4f %14.6f %14.3f\r\n", (double)f[i],
                   (double)back[i], (double)((back[i] - f[i]) * 32768.0f));
        }

        printf("   half a bit of resolution, for a missing 0.5\r\n");
    }

    /* 7. the twiddle tables */
    printf("\r\n7. the generic transform init carries every table\r\n\r\n");
    printf("   arm_rfft_fast_init_f32       tables for 32 through 4096\r\n");
    printf("   arm_rfft_fast_init_128_f32   only the one asked for\r\n");
    printf("   measured twice in this repository, at 77 and 78 kB of"
           " flash\r\n");
    printf("\r\n   and a third time by this app: demonstrating trap 3 needs"
           " the generic\r\n   init, so this image runs about 107 kB against"
           " lib_choose's 23.\r\n");

    printf("\r\nand three more that need a whole chapter each\r\n\r\n");
    printf("  %-36s %s\r\n", "the sine convention is negated",
           "see dft");
    printf("  %-36s %s\r\n", "q15 headroom is sum |taps|",
           "see fixed_point");
    printf("  %-36s %s\r\n", "biquad wants a1 a2 already negated",
           "scipy hands them back positive");

    printf("\r\nwhat every one of them has in common: the code compiles, runs,"
           "\r\nand produces numbers.\r\n");

    while (1)
    {
        for (uint32_t n = 0U; n < SIG_LEN; n++)
        {
            g_in = sig[n];
            probe_step();
        }
    }
}
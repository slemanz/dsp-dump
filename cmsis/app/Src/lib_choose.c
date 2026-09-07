/*
 * The reference card. What to reach for, sorted by the question rather than by
 * the category.
 *
 * The library's own documentation is organised the way a library has to be, by
 * what the functions are. This is organised by what you were trying to do when
 * you went looking, which is the order they are actually needed in.
 *
 * Nothing is computed here. It prints and stops, and it is the app to keep on
 * the terminal while writing something else.
 *
 *     make lib_choose && make load && make monitor
 */

#include <stdio.h>
#include "config.h"
#include "probe.h"

typedef struct
{
    const char *want;
    const char *call;
} entry_t;

static const entry_t arithmetic[] =
{
    { "add, subtract or multiply two signals", "arm_add / sub / mult _f32" },
    { "multiply a signal by a constant",       "arm_scale_f32" },
    { "add a constant",                        "arm_offset_f32" },
    { "flip the sign",                         "arm_negate_f32" },
    { "throw away the sign",                   "arm_abs_f32" },
    { "hold it inside a range",                "arm_clip_f32" },
    { "one number out of two signals",         "arm_dot_prod_f32" },
    { "sine, cosine, square root",             "arm_sin / cos / sqrt _f32" },
    { "log, exp, atan2 over a block",          "arm_vlog / vexp / atan2 _f32" },
};

static const entry_t about[] =
{
    { "the dc offset",                    "arm_mean_f32" },
    { "how big it is, ignoring sign",     "arm_rms_f32" },
    { "how much it varies",               "arm_std_f32, arm_var_f32" },
    { "the sum of squares",               "arm_power_f32" },
    { "the largest, and where",           "arm_max_f32, arm_min_f32" },
    { "the largest ignoring sign",        "arm_absmax_f32" },
    { "is it clipping",                   "arm_absmax_f32, then compare" },
};

static const entry_t filtering[] =
{
    { "filter a block with a kernel",      "arm_fir_f32, init first" },
    { "keep filtering across blocks",      "the same, the state carries it" },
    { "convolve two finite signals",       "arm_conv_f32" },
    { "find one signal inside another",    "arm_correlate_f32" },
    { "a cheaper filter, phase no object", "arm_biquad_cascade_df2T_f32" },
    { "a filter that tunes itself",        "arm_lms_norm_f32" },
    { "the same signal at a lower rate",   "arm_fir_decimate_f32" },
    { "the same signal at a higher rate",  "arm_fir_interpolate_f32" },
};

static const entry_t frequency[] =
{
    { "the spectrum of a real signal",  "arm_rfft_fast_f32" },
    { "magnitude from its packed out",  "arm_cmplx_mag_f32" },
    { "back to the time domain",        "arm_rfft_fast_f32, ifftFlag 1" },
    { "a complex spectrum",             "arm_cfft_f32" },
};

static const entry_t housekeeping[] =
{
    { "change number format",       "arm_float_to_q15, arm_q15_to_float, ..." },
    { "copy or fill a block",       "arm_copy_f32, arm_fill_f32" },
    { "sort it",                    "arm_sort_f32" },
    { "look up between two points", "arm_linear_interp_f32" },
    { "matrices",                   "arm_mat_mult_f32 and the rest" },
    { "a pid loop",                 "arm_pid_f32" },
};

static void section(const char *title, const entry_t *pList, uint32_t len)
{
    printf("\r\n%s\r\n\r\n", title);

    for (uint32_t k = 0U; k < len; k++)
    {
        printf("  %-38s %s\r\n", pList[k].want, pList[k].call);
    }
}

int main(void)
{
    config_app();
    probe_reset();

    printf("\r\nevery name below takes a type suffix. f32 is written"
           " throughout;\r\nq31, q15 and q7 exist for most of them and behave"
           " the same way.\r\n");

    section("arithmetic on a whole block", arithmetic, ARRAY_LEN(arithmetic));
    section("questions about a block", about, ARRAY_LEN(about));
    section("filtering", filtering, ARRAY_LEN(filtering));
    section("frequency", frequency, ARRAY_LEN(frequency));
    section("housekeeping", housekeeping, ARRAY_LEN(housekeeping));

    printf("\r\nand the two rules that decide which half of the library a"
           " routine is in\r\n\r\n");
    printf("  %-38s %s\r\n", "output n depends on input n only",
           "no instance, no init");
    printf("  %-38s %s\r\n", "output n depends on more than that",
           "instance, init, state buffer");

    printf("\r\nthe first half can work in place. the second cannot, and its"
           " state\r\nbuffer belongs to you: the library does not allocate it"
           " and does not\r\ncheck its length.\r\n");

    while (1)
    {
        probe_step();
    }
}
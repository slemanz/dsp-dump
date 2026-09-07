/*
 * When the library wins, and when it does not.
 *
 * The block chapter promised this measurement and here it is. A library routine
 * has a fixed cost before it does any work: the call, the instance to read, the
 * loop set up. On a long block that is nothing. On a short one it can be most
 * of the call.
 *
 * So there is a crossover, and it is worth knowing roughly where it sits
 * because it decides whether a per sample handler should be calling into the
 * library at all. Below it, a plain loop written inline is faster and smaller.
 * Above it, the library wins and keeps winning.
 *
 * The other half of the answer is that the crossover is not the only reason to
 * use the library. A hand written loop that is right today is a loop somebody
 * has to keep right, and every convention in this chapter is a place it can go
 * quietly wrong.
 *
 *     make lib_cost && make load && make monitor
 */

#include <stdio.h>
#include "config.h"
#include "probe.h"
#include "testsig.h"
#include "driver_clock.h"
#include "driver_systick.h"

#define REPEATS     64U

static const uint32_t lengths[] = { 4U, 8U, 16U, 32U, 64U, 128U, 256U };

static float32_t out[SIG_LEN];
static float32_t other[SIG_LEN];

__attribute__((optimize("O2"), noinline))
static void add_by_hand(const float32_t *pA, const float32_t *pB,
                        float32_t *pDst, uint32_t len)
{
    for (uint32_t i = 0U; i < len; i++)
    {
        pDst[i] = pA[i] + pB[i];
    }
}

__attribute__((optimize("O2"), noinline))
static void dot_by_hand(const float32_t *pA, const float32_t *pB,
                        uint32_t len, float32_t *pResult)
{
    float32_t sum = 0.0f;

    for (uint32_t i = 0U; i < len; i++)
    {
        sum += pA[i] * pB[i];
    }

    *pResult = sum;
}

int main(void)
{
    config_app();
    probe_reset();

    for (uint32_t n = 0U; n < SIG_LEN; n++)
    {
        other[n] = sig[SIG_LEN - 1U - n];
    }

    printf("\r\ncore at %lu Hz, each figure averaged over %lu calls\r\n\r\n",
           (unsigned long)clock_hclk(), (unsigned long)REPEATS);

    printf("%8s %12s %12s %10s   %12s %12s %10s\r\n",
           "len", "add lib", "add hand", "ratio",
           "dot lib", "dot hand", "ratio");

    for (uint32_t k = 0U; k < ARRAY_LEN(lengths); k++)
    {
        uint32_t len = lengths[k];
        float32_t scrap;

        cycles_start();
        for (uint32_t r = 0U; r < REPEATS; r++)
        {
            arm_add_f32(sig, other, out, len);
        }
        uint32_t add_lib = cycles_read() / REPEATS;
        systick_init(TICK_HZ);

        cycles_start();
        for (uint32_t r = 0U; r < REPEATS; r++)
        {
            add_by_hand(sig, other, out, len);
        }
        uint32_t add_hand = cycles_read() / REPEATS;
        systick_init(TICK_HZ);

        cycles_start();
        for (uint32_t r = 0U; r < REPEATS; r++)
        {
            arm_dot_prod_f32(sig, other, len, &scrap);
        }
        uint32_t dot_lib = cycles_read() / REPEATS;
        systick_init(TICK_HZ);

        cycles_start();
        for (uint32_t r = 0U; r < REPEATS; r++)
        {
            dot_by_hand(sig, other, len, &scrap);
        }
        uint32_t dot_hand = cycles_read() / REPEATS;
        systick_init(TICK_HZ);

        printf("%8lu %12lu %12lu %10.2f   %12lu %12lu %10.2f\r\n",
               (unsigned long)len, (unsigned long)add_lib,
               (unsigned long)add_hand,
               (double)((float32_t)add_hand / (float32_t)add_lib),
               (unsigned long)dot_lib, (unsigned long)dot_hand,
               (double)((float32_t)dot_hand / (float32_t)dot_lib));

        g_in  = (float32_t)len;
        g_out = (float32_t)add_lib;
        g_ref = (float32_t)add_hand;
        g_gap = (float32_t)add_hand / (float32_t)add_lib;
    }

    printf("\r\na ratio above 1 means the library is ahead: where a column"
           " crosses 1 is\r\nthe shortest block worth calling the library"
           " for.\r\n");

    printf("\r\nthe library's advantage is unrolling and load pairing, which"
           " need\r\nenough elements to amortise the setup that is its"
           " disadvantage.\r\n");

    printf("\r\nthe crossover is not the whole decision: a hand written loop"
           " that is\r\nright today is one somebody has to keep right.\r\n");

    while (1)
    {
        for (uint32_t k = 0U; k < ARRAY_LEN(lengths); k++)
        {
            g_in = (float32_t)lengths[k];
            probe_step();
        }
    }
}
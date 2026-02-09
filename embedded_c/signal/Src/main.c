#include <stdio.h>
#include "config.h"
#include "arm_math.h"

#include "driver_systick.h"
#include "driver_gpio.h"

#include "signals.h"

#define TEST_LENGTH_SAMPLES 4

float g_in_sig_sample; // debug this


extern float _5hz_signal[HZ_5_SIG_LEN];
extern float32_t input_signal_f32_1kHz_15kHz[KHZ1_15_SIG_LEN];

static void plot_input_signal(void);
static void pseudo_dly(int dly);

static float32_t signal_mean(float32_t *sig_src_arr, uint32_t sig_length);

float32_t g_mean_value;
float32_t g_mean_value_arm;

int main(void)
{
    config_app();

    (void)input_signal_f32_1kHz_15kHz;

    g_mean_value = signal_mean((float32_t*)input_signal_f32_1kHz_15kHz, (uint32_t)KHZ1_15_SIG_LEN);
    arm_mean_f32((float32_t*)input_signal_f32_1kHz_15kHz, (uint32_t)KHZ1_15_SIG_LEN, &g_mean_value_arm);

    while(1)
    {
        plot_input_signal();
    }
}

static float32_t signal_mean(float32_t *sig_src_arr, uint32_t sig_length)
{
    float32_t _mean = 0.0;
    uint32_t i;

    for(i = 0; i < sig_length; i++)
    {
        _mean = _mean + sig_src_arr[i];
    }

    _mean = _mean/(float32_t)sig_length;

    return _mean;
}


static void plot_input_signal(void)
{
	int i;
	for( i = 0; i < HZ_5_SIG_LEN; i++)
	{
		g_in_sig_sample = _5hz_signal[i];
        printf("%f\r\n", g_in_sig_sample);
		pseudo_dly(9000);
	}
}

static void pseudo_dly(int dly)
{
	for( int i = 0; i < dly; i++ ){}
}


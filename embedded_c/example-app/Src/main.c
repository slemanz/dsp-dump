#include "config.h"
#include "arm_math.h"

#include "driver_systick.h"
#include "driver_gpio.h"

#define TEST_LENGTH_SAMPLES 4

int main(void)
{
    config_app();

    float32_t srcA[TEST_LENGTH_SAMPLES] = {1.0, 2.0, 3.0, 4.0};
    float32_t srcB[TEST_LENGTH_SAMPLES] = {5.0, 6.0, 7.0, 8.0};
    float32_t dst[TEST_LENGTH_SAMPLES];
    uint32_t blockSize = TEST_LENGTH_SAMPLES;

    // Perform optimized addition: dst = srcA + srcB
    arm_add_f32(srcA, srcB, dst, blockSize);
    (void)dst;
    
    uint64_t start_time = ticks_get();

    while(1)
    {
        if((ticks_get() - start_time) >= 500)
        {
            GPIO_ToggleOutputPin(GPIOA, GPIO_PIN_NO_5);
            start_time = ticks_get();
        }
    }
}

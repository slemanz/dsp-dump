#include "config.h"
#include "common-defines.h" 
#include <stdio.h>

#include "driver_gpio.h"
#include "driver_systick.h"



int main(void)
{
    config_drivers();
    printf("Init OK!\n");

    uint64_t start_time = systick_get();
    uint64_t start_time2 = systick_get();


    GPIO_WriteToOutputPin(GPIOB, GPIO_PIN_NO_2, GPIO_PIN_RESET);
    GPIO_WriteToOutputPin(GPIOA, GPIO_PIN_NO_5, GPIO_PIN_SET);

    while (1)
    {
        if((systick_get() - start_time) >= 500)
        {
            GPIO_ToggleOutputPin(GPIOA, GPIO_PIN_NO_5);
            GPIO_ToggleOutputPin(GPIOB, GPIO_PIN_NO_2);
            start_time = systick_get();
        }

        if((systick_get() - start_time2) >= 30000)
        {
            printf("Teste\n");
            start_time2 = systick_get();
        }
    }
}

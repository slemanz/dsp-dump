TARGET=flash
TARGET_ELF=App/Build/$(TARGET).elf
CC=arm-none-eabi-gcc
MACH=cortex-m4
FLOAT=soft
LINKER_SCRIPT=Linkers/STM32F401xC.ld

#DEFINES+= -DNDEBUG

CFLAGS= -c -mcpu=$(MACH) -mthumb -mfloat-abi=$(FLOAT) -std=gnu11 -Wall -O0 -ggdb $(DEFINES)
LDFLAGS =  -mcpu=$(MACH) -mthumb -mfloat-abi=$(FLOAT) --specs=nano.specs -T $(LINKER_SCRIPT) -Wl,-Map=App/Build/$(TARGET).map -ggdb -u _printf_float -Wl,--print-memory-usage
OBJCOPY=arm-none-eabi-objcopy

###########################################
#				 INCLUDES

INCLUDES+= -I App/Inc/
INCLUDES+= -I Drivers/Inc/ 
INCLUDES+= -I Common/Inc/ 


############################################
# 				OUTPUT FILES

OBJS		+= App/Build/main.o

OBJS		+= App/Build/config.o
OBJS		+= App/Build/syscalls.o
OBJS		+= App/Build/startup.o

DRIVERS		+= App/Build/driver_clock.o
DRIVERS		+= App/Build/driver_systick.o
DRIVERS		+= App/Build/driver_interrupt.o
DRIVERS		+= App/Build/driver_gpio.o
DRIVERS		+= App/Build/driver_uart.o




all: App/Build $(TARGET_ELF)

App/Build:
	mkdir App/Build

App/Build/%.o: App/Src/%.c
	$(CC) $(CFLAGS) $(INCLUDES) -o App/Build/$(*).o App/Src/$(*).c

App/Build/%.o: Src/%.S
	$(CC) $(CFLAGS) $(INCLUDES) -o App/Build/$(*).o App/Src/$(*).S

App/Build/%.o: Linkers/%.c
	$(CC) $(CFLAGS) $(INCLUDES) -o App/Build/$(*).o Linkers/$(*).c

App/Build/%.o: Drivers/Src/%.c
	$(CC) $(CFLAGS) $(INCLUDES) -o App/Build/$(*).o Drivers/Src/$(*).c

App/Build/%.o: Common/Src/utils/%.c
	$(CC) $(CFLAGS) $(INCLUDES) -o App/Build/$(*).o Common/Src/utils/$(*).c

App/Build/%.o: Common/Src/comms/%.c
	$(CC) $(CFLAGS) $(INCLUDES) -o App/Build/$(*).o Common/Src/comms/$(*).c

$(TARGET_ELF): $(OBJS) $(DRIVERS)
	$(CC) $(LDFLAGS) -o $@ $^
	$(OBJCOPY) -O binary $(TARGET_ELF) App/Build/$(TARGET).bin

load:
	openocd -f interface/jlink.cfg -c "transport select swd" -f target/stm32f4x.cfg -c "program $(TARGET_ELF) verify reset exit"

debug:
	openocd -f interface/jlink.cfg -c "transport select swd" -f target/stm32f4x.cfg -c init -c "reset init"

reset:
	openocd -f interface/jlink.cfg -c "transport select swd" -f target/stm32f4x.cfg -c init -c "reset run" -c shutdown

clean:
	rm -rf *.o *.map App/Build/*.o
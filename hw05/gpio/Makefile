# // #//////////////////////////////////////
# // # Author: Christina Rogers
# // # CM: 473
# // # Date: 10/3/2020
# // # Description: Makefile for gpio_test.c
# // #//////////////////////////////////////

obj-m+=gpio_test.o

all:
	make -C /lib/modules/$(shell uname -r)/build/ M=$(PWD) modules
clean:
	make -C /lib/modules/$(shell uname -r)/build/ M=$(PWD) clean

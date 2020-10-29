Author: Christina Rogers (rogersc@rose-hulman.edu)

CM: 473

Date: 10/26/2020

What is included:

| Name      | Description |
| ----------- | ----------- |
| 

## Summary of Results Table: ##

| File      | Frequency |
| ----------- | ----------- | 
| led.pru0.c | 12.51 MHz
| pwmGenerator.pru0.c | 66.65 MHz
| pwnFrequency.pru0.c |  326.8 kHz
| readInput.pru0.c | 6.0846 HZ

## Project: ##


## Blinking an LED: ##
This command made my PRU code run: 

    bone$ make TARGET=hello.pru0 

This command made it stop: 
    
    bone$ make TARGET=hello.pru0 stop

Highest frequency:

    12.51 MHz -> I obtained this value when __delay_cycles was set to 0

Is there jitter? Is it stable?:

    The signal is slighyly unstable and there is a some jitter at a high frquency.
    

## PWM Generator: ##
What’s the Std Dev?:

    9.746 K
    
Highest frequency:

    66.65 MHz -> I obtained this value when __delay_cycles was set to 0

Is there jitter? Is it stable?:

    The signal is still unstable and there is jitter.


## Controlling PWM Frequency: ##
What output pins are being driven?         

    P9_28, P9_29, P9_30, and P9_31

What bits of __R30 are being used?          
    
    0 (P9_31), 1(P9_30), 2(P9_29), 3(P9_28)

Highest frequency:

    326.8 kHz

Is there jitter? Is it stable?:

    The signal is the most stable up until this point, but it is still unstavle with a little jitter. It may be a more stable signal because the frequency is lower then that of the others.

Run the pwm-test.c program to change the on and off times. Does it work?

    Yes, the program does work the code it outputs is included below:
        Servo tester
        Using /dev/mem.
        countOn: 1, countOff: 19, count: 20
        countOn: 2, countOff: 18, count: 20
        countOn: 3, countOff: 17, count: 20
        countOn: 4, countOff: 16, count: 20
        munmap succeeded


## Reading an Input at Regular Intervals: ##

How fast the code can transfer the input to the output:

    The highest frquenct I could obtain was 6.0846 HZ. The reason this number is lower than the others is I am slow when pressing the button compared to a computer toggling.

## Analog Wave Genorator: ##


Author: Christina Rogers (rogersc@rose-hulman.edu)

CM: 473

Date: 10/26/2020

What is included:

| Name      | Description |
| ----------- | ----------- |
| 

## Project: ##


## Blinking an LED: ##
This command made my PRU code run: 

    bone$ make TARGET=hello.pru0 

This command made it stop: 
    
    bone$ make TARGET=hello.pru0 stop

How fast can you toggle the pin?:


    ... Hz

Is there jitter?:

    BLA

Is it stable?:

    BLA
    

## PWM Generator: ##
[___ ]                                      FILL THIS IN
Waveform Capture

What’s the Std Dev?:

    BLA
    
Is there jitter?:

    BLA


## Controlling PWM Frequency: ##
What output pins are being driven?         

    P9_28, P9_29, P9_30, and P9_31

What bits of __R30 are being used?          
    
    0 (P9_31), 1(P9_30), 2(P9_29), 3(P9_28)

What’s the highest frequency you can get with four channels?

Is there jitter? 

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

    BLA

## Analog Wave Genorator: ##


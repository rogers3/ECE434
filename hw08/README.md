Author: Christina Rogers (rogersc@rose-hulman.edu)

CM: 473

Date: 10/26/2020

What is included:

| Name      | Description |
| ----------- | ----------- |
| analogWaveGen.pru0.c | PRU code to create an analog sine wave
| led.pru0.c | PRU code to toggle an LED through ARM GPIO
| pwmFreqTest.c | This file was used to set the different frequencies in pwmFrequency.pru0.c
| pwmFrequency.pru0.c | PRU code to toggle four LEDs at different frequencies through PRU GPIO
| pwmGenerator.pru0.c | PRU code to toggle an LED through PRU GPIO
| readInput.pru0.c | PRU code to read an input and write it to an output
| setup.sh | This is the setup file for this folder

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

    The signal is slighyly unstable and there is some jitter at a high frquency.

Waveform:
![alt text](https://github.com/rogers3/ECE434/blob/master/hw08/picrutes/led.png.png)

## PWM Generator: ##
What’s the Std Dev?:

    9.746 KHz
    
Highest frequency:

    66.65 MHz -> I obtained this value when __delay_cycles was set to 0

Is there jitter? Is it stable?:

    The signal is still unstable and there is jitter.

Waveform at highest frequency:
![alt text](https://github.com/rogers3/ECE434/blob/master/hw08/picrutes/pwmGenerator_MaxFreq.png)


Waveform at 50 MHz:
![alt text](https://github.com/rogers3/ECE434/blob/master/hw08/picrutes/pwmGenerator_50MHz.png

## Controlling PWM Frequency: ##
What output pins are being driven?         

    P9_28, P9_29, P9_30, and P9_31

What bits of __R30 are being used?          
    
    0 (P9_31), 1(P9_30), 2(P9_29), 3(P9_28)

Highest frequency:

    326.8 kHz

Is there jitter?:

    Yes, there is jitter.

Run the pwm-test.c program to change the on and off times. Does it work?

    Yes, the program does work the code it outputs is included below:
        Servo tester
        Using /dev/mem.
        countOn: 1, countOff: 19, count: 20
        countOn: 2, countOff: 18, count: 20
        countOn: 3, countOff: 17, count: 20
        countOn: 4, countOff: 16, count: 20
        munmap succeeded

Waveform at four signals:
![alt text]https://github.com/rogers3/ECE434/blob/master/hw08/picrutes/pwmFrequency.png)


## Reading an Input at Regular Intervals: ##

How fast the code can transfer the input to the output:

    The highest frquenct I could obtain was 6.0846 HZ. The reason this number is lower than the others is I am slow when pressing the button compared to a computer toggling.

## Analog Wave Genorator: ##

Waveform of sine wave:
![alt text](https://github.com/rogers3/ECE434/blob/master/hw08/picrutes/sineWave.png)


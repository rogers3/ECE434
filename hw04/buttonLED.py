#!/usr/bin/python3

#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 9/29/2020
# Description: This is a pthon program that reads from two buttons and controlls
#   two LEDs. So when one button is pressed its corresponding LED turns on and 
#   when the button is not pressed the LED is off
#//////////////////////////////////////

#import necessary libraries
from mmap import mmap
import time, struct 

#define adress of the ports
GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
GPIO_DATAIN = 0x138
blueLED = 1<<13
redLED = 1<<12

# open /dev/mem
with open("/dev/mem", "r+b" ) as f:
  mem = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)
# read the 4 byte value to set to output
packed_reg = mem[GPIO_OE:GPIO_OE+4]
# unpack the value
reg_status = struct.unpack("<L", packed_reg)[0]
# toggle the bit
reg_status &= ~(redLED)
reg_status &= ~(blueLED)
# save the 4-byte value
mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)

while(True):
    # read the values of the buttons
    blueButton = (mem[GPIO_DATAIN+1] & 1<<7) >> 7
    redButton = (mem[GPIO_DATAIN+1] & 1<<6) >> 6

    # if blue button is one turn on blue led. Else turn off blue led.
    if(blueButton == 1):
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", blueLED) 
    else:
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", blueLED)
        
    # if red button is one turn on red led. Else turn off red led.
    if(redButton == 1):
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", redLED) 
    else:
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", redLED)


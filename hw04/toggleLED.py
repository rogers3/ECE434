#!/usr/bin/python3

#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 9/29/2020
# Description: This is a pthon program that toggles a GPIO port (LED) as fast 
#   as possible using mmap. 
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
# save the 4-byte value
mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)

while(True):
    # toggle the LEDs
    # period = 1
    mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", redLED) 
    # time.sleep(period/2)
    mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", redLED)
    # time.sleep(period/2)


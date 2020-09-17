#!/usr/bin/python3

#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 9/19/2020
# Description: This is a python program that will continously read the 
#           temperature from a temprature sensor (TMP101)
#//////////////////////////////////////

#import necessary libraries
import smbus
import time

# Use i2c bus 1 adress 0x4a and 0x48
bus = smbus.SMBus(1)
adress1 = 0x4a
adress2 = 0x48

while True:
        # read temperatures and convert them to farienheit
        temp1 = bus.read_byte_data(adress1, 0)
        temp1 = temp1*9/5+32
        temp2 = bus.read_byte_data(adress2, 0)
        temp2 = temp2*9/5+32
        
        print("temp1: ", temp1, "   temp2: ", temp2, end="\r")
        time.sleep(0.25)
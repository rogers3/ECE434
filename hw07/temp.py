#!/usr/bin/env python3
#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 10/20/2020
# Description: Displays temperature read from TMP101 sensor in farenheight on virtual
#       display V2)
#//////////////////////////////////////
import blynklib
import os
import time
import smbus
import Adafruit_BBIO.GPIO as GPIO

# Use i2c bus 1 adress 0x4a and 0x48
bus = smbus.SMBus(2)
adress1 = 0x4a
adress2 = 0x48

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# Register Virtual Pins
# The V* says to response to all virtual pins
@blynk.handle_event('write V*')
def my_write_handler(pin, value):
    print('Current V{} value: {}'.format(pin, value))
    GPIO.output(LED, int(value[0])) 
    

while True:
        blynk.run()
        
        # read temperatures and convert them to farienheit
        temp1 = bus.read_byte_data(adress1, 0)
        temp1 = temp1*9/5+32
        temp2 = bus.read_byte_data(adress2, 0)
        temp2 = temp2*9/5+32
        
        print("temp=: ", temp1, end="\r")
        blynk.virtual_write(1, temp1)  # Virtual LED: 255 max brightness
        time.sleep(0.25)


while True:
    blynk.run()
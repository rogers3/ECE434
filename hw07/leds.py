#!/usr/bin/env python3
#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 10/20/2020
# Description: Blink the USR3 and a virtual LED (V0) in response to a button (P8_16) press
#/////////////////////////////////////
import blynklib
import os
import Adafruit_BBIO.GPIO as GPIO

# Setup the LED
LED = 'USR3'
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 1) 

# Setup the button
button = 'P8_16'
GPIO.setup(button, GPIO.IN)
# print("button: " + str(GPIO.input(button)))

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
    
# This calback is called everytime the button changes
# channel is the name of the pin that changed
def pushed(channel):
    # Read the current value of the input
    state = GPIO.input(channel)
    print('Edge detected on channel {}, value={}'.format(channel, state))
    # Write it out
    GPIO.output(LED, state)     # Physical LED
    blynk.virtual_write(0, 255*state)  # Virtual LED: 255 max brightness

# This is a non-blocking event 
GPIO.add_event_detect(button, GPIO.BOTH, callback=pushed) 


while True:
    blynk.run()
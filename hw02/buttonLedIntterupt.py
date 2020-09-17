#!/usr/bin/python3
#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 9/14/2020
# Description: This is a python program that will turn an LED on when its
#       button is pressed. I used P8_11, P8_12, P8_13, P8_14 as my buttons
#       and P9_14, P9_12, P9_16, P9_18 as my leds. The buttons pin corresponded
#       to its led pin accordingly.
#//////////////////////////////////////

#import necessary libraries
import Adafruit_BBIO.GPIO as GPIO
import time

#define buttons and led then create a dictionary
buttons = ["P8_11", "P8_12", "P8_13", "P8_14"]
leds = ["P9_14", "P9_12", "P9_16", "P9_18"]
ledButtonDict = {buttons[i]: leds[i] for i in range(len(buttons))}

#setup all the pins: led->output, button->input
for i  in range(4):
    GPIO.setup(leds[i], GPIO.OUT)
    GPIO.setup(buttons[i], GPIO.IN)

#callback funtion for when a button is pressed
def toggleLed(pin):
    if(GPIO.input(pin)):
        GPIO.output(ledButtonDict.get(pin), GPIO.HIGH)
    else:
        GPIO.output(ledButtonDict.get(pin), GPIO.LOW)

#add event detects on buttons with callback function
for i in range(4):
    GPIO.add_event_detect(buttons[i], GPIO.BOTH, toggleLed)

#loop indefinatly
while True:
    time.sleep(2)


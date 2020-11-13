#!/usr/bin/python3
#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 9/16/2020
# Description: This is a python program that toggles an LED on and off
#//////////////////////////////////////

#import necessary libraries
import Adafruit_BBIO.GPIO as GPIO
import time

#define led and set as output
led = "P8_11"
GPIO.setup(led, GPIO.OUT)

#callback funtion for when a button is pressed
def toggleLed(pin):
    if(GPIO.input(pin)):
        GPIO.output(ledButtonDict.get(pin), GPIO.HIGH)
    else:
        GPIO.output(ledButtonDict.get(pin), GPIO.LOW)

#loop indefinatly
while True:
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.001/2)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.001/2)


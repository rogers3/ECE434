#!/usr/bin/python3

#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 9/19/2020
# Description: Whenever the alert pin on one of the TMP101 toggles the temprature of
#               each of the TMP101 as well as the value of the alert pins will be printed
#//////////////////////////////////////

#import necessary libraries
import smbus
import time
import Adafruit_BBIO.GPIO as GPIO

# Use i2c bus 1 adress 0x4a and 0x48
bus = smbus.SMBus(1)
adress1 = 0x4a
adress2 = 0x48

# setup the alert pins as GPIO inputs
alert1 = "P8_14"
alert2 = "P8_13"
GPIO.setup(alert1, GPIO.IN)
GPIO.setup(alert2, GPIO.IN)

def alertTriggered(pin):
        # read temperatures and convert them to farienheit
        temp1 = bus.read_byte_data(adress1, 0)
        temp1 = temp1*9/5+32
        temp2 = bus.read_byte_data(adress2, 0)
        temp2 = temp2*9/5+32
        
        print("temp1: ", temp1, "   temp2: ", temp2, "    alert1: ", GPIO.input(alert1), "     alert2: ", GPIO.input(alert2))

# add event detects to the alert pin so when ever they chang (low or high) alertTriggered() is called
GPIO.add_event_detect(alert1, GPIO.BOTH, alertTriggered)
GPIO.add_event_detect(alert2, GPIO.BOTH, alertTriggered)

#loop indefinatly
while True:
        time.sleep(0.25)
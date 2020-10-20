#!/usr/bin/env python3

#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 10/20/2020
# Description: This is code (Python) for the game etch a sketch. When ran, buttons on 
#              Blynk app can draw a picture on an 8x8 LED matrix. The the user 
#              can move left/right and up/down using buttons on the app. The red 
#              light represents the cursor and green lights represents the drawing. 
#              Moving the rotary encoders move the cursor leaving an green light in  
#              the previous position and a red one in the current position.
#//////////////////////////////////////

#import necessary libraries
import Adafruit_BBIO.GPIO as GPIO
import blynklib
import os
import time
import smbus

#declare initial variables
xpos, ypos = 0, 0
width, height = 8, 8
encoderLRValue = 0
picture = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
         0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
greenPicture = {7:0, 6:2, 5:4, 4:6, 3:8, 2:10, 1:12, 0:14}  #green picture location
redPicture = {7:1, 6:3, 5:5, 4:7, 3:9, 2:11, 1:13, 0:15}  #red picture location
yposPicture = {0:0x01, 1: 0x02, 2: 0x04, 3: 0x08, 4: 0x10, 5:0x20, 6: 0x40, 7: 0x80} #y curosr location

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')
# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# Use i2c bus 1 adress 0x70
bus = smbus.SMBus(2)  
matrix = 0x70
bus.write_byte_data(matrix, 0x21, 0) # Start oscillator (page 10)
bus.write_byte_data(matrix, 0x81, 0) # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0) # Full brightness (p15)
    
#callback funtion-- moves cursor based of used input
def userInput(direction):
    global xpos, ypos
    if(direction=="r"):  # If right, move the cursor to the right
        xpos += 1
    elif(direction=="l"):  # If left, move the cursor to the left
        xpos -= 1
    elif(direction=="u"):  # If up, move the cursor up
        ypos -= 1
    elif(direction=="d"):  # If down, move the cursor down
        ypos += 1
    time.sleep(0.2)
    drawPicture() #redraw picture
    
def drawPicture():
    global xpos, ypos
    
    # Ensure the cursor is still within the picture. If not reset it.
    if(xpos<0): xpos=0; return;
    if(xpos>=width): xpos = width-1; return;
    if(ypos<0): ypos=0; return;
    if(ypos>=height): ypos = height-1; return;
    
    # Place red square on current position
    picture[redPicture[xpos]] = picture[redPicture[xpos]] | yposPicture[ypos]
    picture[greenPicture[xpos]] = picture[greenPicture[xpos]] & ~yposPicture[ypos]
    
    bus.write_i2c_block_data(matrix, 0, picture) #redraw picture
    
    # Place green square on current position
    picture[redPicture[xpos]] = picture[redPicture[xpos]] & ~yposPicture[ypos]
    picture[greenPicture[xpos]] = picture[greenPicture[xpos]] | yposPicture[ypos]

# Register Virtual Pins
# The V* says to response to all virtual pins
@blynk.handle_event('write V*')
def my_write_handler(pin, value):
    if((pin == 2)&(value == ['1'])): direction = 'l'
    if((pin == 3)&(value == ['1'])): direction = 'r'
    if((pin == 4)&(value == ['1'])): direction = 'u'
    if((pin == 5)&(value == ['1'])): direction = 'd'
    userInput(direction)
    
drawPicture()

#loop unil exit
while True: 
    blynk.run()


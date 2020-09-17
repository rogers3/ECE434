#!/usr/bin/python3

#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 9/19/2020
# Description: This is code (Python) for the game etch a sketch. When ran, rotary 
#              encoders can draw a picture on an 8x8 LED matrix. The the user 
#              can move left/right on one encoder and up/down on the other. The red 
#              light represents the cursor and green lights represents the drawing. 
#              Moving the rotary encoders move the cursor leaving an green light in  
#              the previous position and a red one in the current position.
#//////////////////////////////////////

#import necessary libraries
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
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

#setup rotaery encoders 1 and 2
myEncoderLR = RotaryEncoder(eQEP1)
myEncoderLR.setAbsolute()
myEncoderLR.enable()
myEncoderUD = RotaryEncoder(eQEP2)
myEncoderUD.setAbsolute()
myEncoderUD.enable()

# Use i2c bus 1 adress 0x70
bus = smbus.SMBus(1)  
matrix = 0x70
bus.write_byte_data(matrix, 0x21, 0) # Start oscillator (page 10)
bus.write_byte_data(matrix, 0x81, 0) # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0) # Full brightness (p15)
    
#callback funtion-- moves cursor based of used input
def userInput(encoderValue, encoderdirection):
    global xpos, ypos
    if((encoderValue < 0)&(encoderdirection=="lr")):  # If right, move the cursor to the right
        xpos += 1
    elif((encoderValue > 0)&(encoderdirection=="lr")):  # If left, move the cursor to the left
        xpos -= 1
    if((encoderValue > 0)&(encoderdirection=="ud")):  # If up, move the cursor up
        ypos -= 1
    elif((encoderValue < 0)&(encoderdirection=="ud")):  # If down, move the cursor down
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


drawPicture()

#loop unil exit
while True: 
    
    #if left/right encoder is moved go to userInput()
    encoderLRValue = myEncoderLR.position
    if(encoderLRValue != 0): userInput(encoderLRValue, "lr");
    myEncoderLR.zero()

    #if up/dowm encoder is moved go to userInput()
    encoderUDValue = myEncoderUD.position
    if(encoderUDValue != 0): userInput(encoderUDValue, "ud");
    myEncoderUD.zero()

    time.sleep(0.5)

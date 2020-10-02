#!/usr/bin/env python3

#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 10/1/2020
# Description: This is code (Python) for the game etch a sketch. When ran, buttons on 
#              a browser can draw a picture on an 8x8 LED matrix. The the user 
#              can move left/right and up/down using the buttons on the browawe. The red 
#              light represents the cursor and green lights represents the drawing. 
#              Moving the rotary encoders move the cursor leaving an green light in  
#              the previous position and a red one in the current position. There is
#              also a clear button that will reset the display, but cursor position
#              will remain the same.
#//////////////////////////////////////

#import necessary libraries
from flask import Flask, render_template, request
import time
import smbus

#declare initial variables
xpos, ypos = 0, 0
width, height = 8, 8
picture = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
greenPicture = {7:0, 6:2, 5:4, 4:6, 3:8, 2:10, 1:12, 0:14}  #green picture location
redPicture = {7:1, 6:3, 5:5, 4:7, 3:9, 2:11, 1:13, 0:15}  #red picture location
yposPicture = {0:0x01, 1: 0x02, 2: 0x04, 3: 0x08, 4: 0x10, 5:0x20, 6: 0x40, 7: 0x80} #y curosr location

# Use i2c bus 1 adress 0x70
bus = smbus.SMBus(1)  
matrix = 0x70
bus.write_byte_data(matrix, 0x21, 0) # Start oscillator (page 10)
bus.write_byte_data(matrix, 0x81, 0) # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0) # Full brightness (p15)
bus.write_i2c_block_data(matrix, 0, picture) #redraw picture

def drawPicture():
    global xpos, ypos, picture
    
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

app = Flask(__name__)
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	global xpos, ypos, picture
	if action == "left": # If left, move the cursor to the left
	    xpos -= 1
	if action == "right": # If right, move the cursor to the right
	    xpos += 1
	if action == "up": # If up, move the cursor up
	    ypos -= 1
	if action == "down": # If down, move the cursor down
		ypos += 1
	if action == "clear": # If clear, reset the picture
	    picture = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
	drawPicture()
	return render_template('index.html')
	
if __name__ == "__main__":
   app.run(debug=True, port=8081, host='0.0.0.0')
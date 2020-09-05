#!/usr/bin/python3
#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 9/5/2020
# Description: This is code (Python) for the game etch a sketch. When ran an 
#              empty picture is created by thrspecified height and width. Then
#              the user can move left/right, up/down, clear or exit. The '#'
#              represents the cursor and an 'X' represents the drawing. 
#              Left/right and up/down move the cursor leaving an X in the 
#              previous position. Clear resets the grid but save the cursor
#              positin and exits leaves the game.
#//////////////////////////////////////

#import necessary libraries
import Adafruit_BBIO.GPIO as GPIO
import time
from array import *

#declare initial variables
xpos, ypos = 0, 0
width = int(input("Enter desired width:   "))
height = int(input("Enter desired height:   "))
picture = [["." for x in range(width)] for y in range(height)] 

#code to repeat
while True: 
    
    # Mark cursor on picture
    picture[ypos][xpos] = "#" 
    
    #print picture
    for i in range(height):
        print("   ", end = "")
        for j in range(width):
            print(picture[i][j], " ", end ="")
        print("")
    
    # Mark old positin of cursor with draeing
    picture[ypos][xpos] = "X"
    
    # Get user instruction
    move = input("Please enter an instruction [Right (R/r), Left (L/l), Up (U/u), Down (D/d), clear (C/c), or Exit (E/e]:   ")
    
    # Execute instruction of user
    if(move.lower() == "r" or move.lower() =="right"):  # If right, move the cursor to the right
            xpos += 1 
    elif(move.lower() == "l" or move.lower() =="left"):  # If left, move the cursor to the left
            xpos -= 1
    elif(move.lower() == "u" or move.lower() =="up"):  # If up, move the cursor up
            ypos -= 1 
    elif(move.lower() == "d" or move.lower() =="down"):  # If down, move the cursor down
            ypos += 1 
    elif(move.lower() == "c" or move.lower() =="clear"):  # If clear, reset the picture
        picture = [["." for x in range(width)] for y in range(height)] 
    elif(move.lower() == "e" or move.lower() =="exit"):  # If exit, stop the program
            break
    else:
        print("Invalid input")
        
    # Ensure the cursor is still within the picture. If not reset it.
    if(xpos<0): xpos=0
    if(xpos>=width): xpos = width-1
    if(ypos<0): ypos=0
    if(ypos>=height): ypos = height-1
    
    time.sleep(0.5)


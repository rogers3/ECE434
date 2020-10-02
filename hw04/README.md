Author: Christina Rogers (rogersc@rose-hulman.edu)
CM: 473
Date: 10/2/2020

What is included in this folder:

| Name      | Description |
| ----------- | ----------- |
|  LedMatrixViaFlask.py | TThis is code (Python) for the game etch a sketch. When ran, buttons on a browser can draw a picture on an 8x8 LED matrix. The the user can move left/right and up/down as well as clear the drawing using the buttons on the browawe. The red light represents the cursor and green lights represents the drawing. Moving the rotary encoders move the cursor leaving an green light in the previous position and a red one in the current position. 
|  buttonLED.py | This is a pthon program that reads from two buttons and controlls two LEDs. So when one button is pressed its corresponding LED turns on and when the button is not pressed the LED is off
|  i2cViaKernel.sh | This is a shell script that will continously read the temperature from a temprature sensor (TMP101) via the kernel driver
|  toggleLED.py | This is a pthon program that toggles a GPIO port (LED) as fast as possible using mmap. 

Embedded System Memory Map for Beagle Bone:
**insert pic**

GPIO Via MMAP:
Write a C or python program that toggles a GPIO port as fast as it can. Measure the speed with an oscilloscope and compare with your previous measurements. Try toggling with no usleep. Is it faster?

Display Images:
**insert pictures**

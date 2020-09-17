Author: Christina Rogers (rogersc@rose-hulman.edu)
CM: 473
Date: 9/5/2020

What is included in this folder

| Name      | Description |
| ----------- | ----------- |
|  config.sh | This shell script configures all pins to the correct modes for this project.
|  etchASketchV3.py | This is a python script for the game etchASketch. Two rotary encoders control the position on the screen (an 8x8 matrix). A red light represents where the cursor is and a green light represents where the cursor has prviously been (drawing).
|  tempInterrpt.py | This is a python script that waits for an interrupt on the TMP101s alert pins then prints the temperature in F.
|  tempRead.py | This python script continously reads the temperatures of the two connected TMP101s (bus 1 adresses 0x4a and 0x48) and prints them out in F.
|  tempRead.sh | This shell script continously reads the temperatures of the two connected TMP101s (bus 1 adresses 0x4a and 0x48) and prints them out in F.


Note: Before running another scipt, first run configure.sh, to correctly configure the pins
Author: Christina Rogers (rogersc@rose-hulman.edu)
CM: 473
Date: 9/5/2020

This is a folder for hw02. This is what is included:

    1. buttonLedIntterupt.py -> This is a python program that will turn an LED on when its
            button is pressed. I used P8_11, P8_12, P8_13, P8_14 as my buttons
            and P9_14, P9_12, P9_16, P9_18 as my leds. The buttons pin corresponded
            to its led pin accordingly.
            
    2. etchASketchButtons.py -> This is an etch and sketch program. The user can specify 
            the width and height of the picture they desire. The picture will then be created. 
            A '.' represents an empty space on the picture. A '#' represents where the users 
            cursor currently is. A 'X' represents where the cursor has previousy been
            (drawing). Next the user enters one of the following instructions by either pushing
            a button or entering it into the teminal:
                1. Right/R (Button)- this moves the cursor to the right. If the cursor is at the
                    right most position it will do nothing.
                2. Left/L (Button)- this moves the cursor to the left. If the cursor is at the
                    left most position it will do nothing.
                3. Up/U (Button)- this moves the cursor up. If the cursor is at the highest position
                    it will do nothing.
                4. Down/D (Button) - this moves the cursor dpwn. If the cursor is at the lowest
                    position it will do nothing.
                5. Clear/C (Terminal)- this will clear the grid (all '.' other then cursor) but NOT 
                    reset the cursor
                6. Exit/E (Terminal)- this exits the program
                
    3. toggleLed.Py -> This is a program that toggles an LED. It was used to measure a python scripts
            toggle speed on an oscilliscpoe
            

Oscilliscope Measurements:

| Question      | Shell | Python | C w/o lseeek() | C w/ lseek | gpiod - python | gpiod - c |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
|  1: Max Voltage (V) | 3.361 V | 3.3545 | 3.3545 | 3.6363 | 3.2442 | 3.2167 |
|  2: Period (ms) | 189.21 | 100.71 | 100.37 | 100.21 | 100.25 | 99.98 |
|  3: How close to 100 ms? | far (89.21 ms) | close (.71 ms) | close (.37 ms) | close (.21 ms) | close (.25 ms) | very close (.02 ms) |
|  4: Why do they differ? | You have to start the sysfs process over and over making it slower| Python is an interpretive language so it is a little slower | Without lseek the programs opens/close the file every toggle making it slower | With lseek the program does not open/close the file every toggle making it faster| gpiod is faster then other methods but python is slower then c b/c it is an interpretiv language |  gpiod is faster then other methods and c is faster then python | 
|  5: Processor usage (at 10 ms period) | 20.6% | 6.1% | 5.2% | 5.3% | 3.9% | 4.0% |
|  6: Table of period and processor usage | Table 1 | Table 2 | Table 3 | Table 4 | Table 5 | Table 6 |
|  7: Stability of period | Bad (10 ms range) | good (.1 ms range) | good (.05 ms range) | very good (.01 ms range) | good (.2 ms range) | good (.15 ms range) |
|  8: How is period while lanching vi? | spikes  then stabilizes | spikes  then stabilizes | spikes  then stabilizes | spikes  then stabilizes | spikes  then stabilizes | spikes  then stabilizes |
|  9: Is period shorter after removing uneeded lines |  slighly | n/a | n/a | n/a | n/a | n/a |
|  10: Is period shorter using sh? | yes | n/a | n/a | n/a | n/a | n/a |
|  11: Shortest period (ms) | 43.44 ms | .1695 | .31195 | .17733 | .01734 | .0099187 |


Table 1 -  Shell
| Value set (ms) | Period (ms) | Processor usage (%) |
| ----------- | ----------- | ----------- |
| 100 | 189.21 | 20.60 |
| 50 | 142.85 | 32.0 |
| 10 | 62.5 | 70.8 |
| 5 | 52.58 | 83.1 |
| 1 | 43.45 | 96.7 |
| 0.5 | 43.45 | 98.1 |
| 0.1 | 43.44 | 99.4 |

Table 2  - Python
| Value set (ms) | Period (ms) | Processor usage (%) |
| ----------- | ----------- | ----------- |
| 100 | 100.71 | 3.3 |
| 50 | 50.49 | 3.9 |
| 10 | 10.043 | 6.6 |
| 5 | 5.4392 | 9.5 |
| 1 | 1.4104 | 25.2 |
| 0.5 | 0.88789 | 55.0 |
| 0.1 | 0.47009 | 78.3 |

Table 3 - C w/o lseeek()
| Value set (ms) | Period (ms) | Processor usage |
| ----------- | ----------- | ----------- |
| 100 | 100.37 | 3.2 |
| 50 | 50.040 | 3.3 |
| 10 | 10.34 | 3.9 |
| 5 | 5.3414 | 4.6 |
| 1 | 1.3350 | 8.2 |
| 0.5 | .80859 | 11.0 |
| 0.1 | .41252 | 25.9 |

Table 4 - C w/ lseek
| Value set (ms) | Period (ms) | Processor usage |
| ----------- | ----------- | ----------- |
| 100 | 100.21 | 3.3 |
| 50 | 50.0422 | 3.3 |
| 10 | 10.3419 | 3.9 |
| 5 | 5.1905 | 4.6 |
| 1 | 1.1811 | 8.2 |
| 0.5 | .67688 | 9.8 |
| 0.1 | .27541 | 24.1 |

Table 5 - gpiod - python
| Value set (ms) | Period (ms) | Processor usage |
| ----------- | ----------- | ----------- |
| 100 | 100.25 | 3.3 |
| 50 | 50.24 | 3.3 |
| 10 | 10.24 | 4.6 |
| 5 | 5.1833 | 5.3 |
| 1 | 1.2196 | 11.0 |
| 0.5 | .71155 | 18.2 |
| 0.1 | .30658 | 47.4 |

Table 6 - gpiod - c
| Value set (ms) | Period (ms) | Processor usage |
| ----------- | ----------- | ----------- |
| 100 | 99.98 | 2.6 |
| 50 | 49.999 | 3.2 |
| 10 | 10.20 | 3.9 |
| 5 | 5.1833 | 5.2 |
| 1 | 1.1710 | 9.2 |
| 0.5 | .66981 | 9.7 |
| 0.1 | .26656 | 23.4 |

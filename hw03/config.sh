#! /bin/bash

#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 9/19/2020
# Description: This is a shell script that will configure all the pins
#              for this folder.
#//////////////////////////////////////


#TMP101s
config-pin P9_17 i2c 
config-pin P9_18 i2c
i2cset -y 1 0x48 2 0x1d  #tLow
i2cset -y 1 0x4a 2 0x1d  #tLow
i2cset -y 1 0x48 3 0x1e  #tHigh
i2cset -y 1 0x4a 3 0x1e  #tHigh
config-pin P8_13 gpio  #alert
config-pin P8_14 gpio  #alert

#8x8 LED Matrix
config-pin P9_19 i2c
config-pin P9_20 i2c

# eQEP 1
config-pin P8_33 eqep
config-pin P8_35 eqep

# eQEP 2b
config-pin P8_11 eqep
config-pin P8_12 eqep

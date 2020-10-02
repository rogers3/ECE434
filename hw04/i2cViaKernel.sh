#! /bin/bash

#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 9/19/2020
# Description: This is a shell script that will continously read the 
#           temperature from a temprature sensor (TMP101) via the kernel driver
#//////////////////////////////////////

echo Hit ^c to stop

while true; do 
    cd /sys/class/i2c-adapter/i2c-1/1-0048/hwmon/hwmon0
    cat temp1_input | tr -s '\n\r'

done
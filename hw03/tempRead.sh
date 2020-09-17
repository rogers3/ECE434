#! /bin/bash

#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 9/19/2020
# Description: This is a shell script that will continously read the 
#           temperature from a temprature sensor (TMP101)
#//////////////////////////////////////

echo Hit ^c to stop

while true; do 
    # get the values at TMP101 sensors
    temp1=`i2cget -y 1 0x4a`
    temp2=`i2cget -y 1 0x48`
    
    # convert to farenhight
    temp1=$(($temp1 *9/5 +32))
    temp2=$(($temp2 *9/5 +32))
    
    echo -ne "temp1:  $temp1      temp2: $temp2 \r"
done
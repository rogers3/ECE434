#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 10/20/2020
# Description: Sets up for this folder
#//////////////////////////////////////

# ######################################### led
# config-pin P9_31 gpio
# echo out > /sys/class/gpio/gpio110/direction

######################################### pwm
HEADER=P9_
PINS="25 27 28 29 30 31"	#  41 42 don't work

echo "-Configuring pinmux"
	for PIN_NUMBER in $PINS
	do
		config-pin $HEADER$PIN_NUMBER pruout
	done
	
# ########################################## reading an input
# export TARGET=input.pru0
# echo TARGET=$TARGET

# # Configure the PRU pins based on which Beagle is running
# machine=$(awk '{print $NF}' /proc/device-tree/model)
# echo -n $machine
# if [ $machine = "Black" ]; then
#     echo " Found"
#     config-pin P9_31 pruout
#     config-pin -q P9_31
#     config-pin P9_25 pruin
#     config-pin -q P9_25
# elif [ $machine = "Blue" ]; then
#     echo " Found"
#     pins=""
# elif [ $machine = "PocketBeagle" ]; then
#     echo " Found"
#     config-pin P1_36 pruout
#     config-pin -q P1_36
#     config-pin P1_29 pruin
#     config-pin -q P1_29
# else
#     echo " Not Found"
#     pins=""
# fi

# Setup speaker
config-pin P9_14 pwm

# TMP101s
config-pin P9_21 i2c 
config-pin P9_22 i2c
i2cset -y 2 0x4a 2 0x1d  #tLow
i2cset -y 2 0x4a 3 0x1e  #tHigh

# Authenitcate ngrok
./ngrok authtoken YOUR_AUTH_TOKEN
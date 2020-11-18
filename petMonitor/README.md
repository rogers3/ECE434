Author: Christina Rogers (rogersc@rose-hulman.edu)

CM: 473

Date: 10/26/2020

## What is included: ##

| Name      | Description |
| ----------- | ----------- |
| templates | Folder containing HTML/CSS templates for this project
| PWMmay.py | This is required to use pwm on the speaker
| httpMonitor.py | This is the main program. It is what is executed to run the Pet Monitor. It runs flask and has functions for when buttons are pressed on Flask. 
| install.sh | This is the installation file for this folder
| motion.conf | This contains the configuration details for the camera being used (PlayStation 3 Eye). It is used when the video stream is started.
| motion.log | This folder contains log information for motion which streams video. If the video is not working properly, check this log.
| ngrok | This is required to run ngrok
| setup.sh | This is the setup file for this folder
| sound.py | This pthon script contains the function to play the speaker at a praticular frequency as well as the song Old McDonald. It is called in httpMonitor.py and requires PWMmay.py



## Description: ##
This project is a Pet Monitor. When ran it displays a website for the Pet Monitor on yourLocalHost:434 using Flask. The variable yourLocalHost should be the same IP
address used to open cloud9. For me, this number is 192.168.7.2. So, to open the Pet Monitor I enter 192.168.7.2:434 into a web browser. From here the features for
the Pet Monitor can be accesed. This includes a camera which can be toggled on a button press and a speaker which can play at a specific frequency and the meoldy Old 
McDonald using buttons. It also tracks data such as temperature, time since last fed, and time since last let out.

## Installation: ##
First to install clone this git page to your Bone. Next, add an authentication token for ngrok. To do this, first create a ngrok account by visiting 
https://ngrok.com/ and clicking sign up. After the account is created, a authentication token should be available. Open setup.sh and replace 'YOUR_AUTH_TOKEN' 
in line 11 with your authentication token. Finally run ./install.sh on your bone. After this the Pet Monitor is ready to go!

## Running the Pet Monitor: ##
To run the pet monitor first ensure the installation steps have been completed. Then in this folder run:

    bone$ ./setup.sh. 
    
This configures the pins and ngrok. Then run:

    bone$ sudo ./httpMonitor.py
    
This should open the Pet Monitor on yourLocalHost:434 (read Installation for more info on yourLocalHost). From here the program is ran and the features of the Pet
Monitor can be accessed

## Making Pet Monitor Publically accesable: ##
If desired, the pet monitor can be made available on non-local hosts as well. This is done by first configuring ngrok (see Installation Instructions) and then in a 
'''new''' terminal entering

    bone$ ./ngrok http 434
    
Note: If using ngrok there will be two terminals connected to the Bone at once. One is running httpmoniter.py and the other is running ngrok.

In the terminal running ngrok, a screen will appear with a public browser that can be used to view the pet monitor from anywhere. One issue with this is that
each time ngrok is ran, a new url for the public browser is generated. This should not be an issue if the pet monitor is not restarted often. However, if this
is an issue it is possible to use the same url each time the pet monitor is ran. It costs $60/year for the subscription to ngrok that allows this. For more 
information visit https://ngrok.com/pricing

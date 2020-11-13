#!/usr/bin/env python3

#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 10/1/2020
# Description: 
#//////////////////////////////////////

#import necessary libraries
from flask import Flask, render_template, request
import Adafruit_BBIO.GPIO as GPIO
import threading 
import time

import os
import subprocess
import sys

#define buzzer and set as output
buzzer = "P8_11"
GPIO.setup(buzzer, GPIO.OUT)

cameraOn=False;
soundOn=False;
csb = 'switchOffBackground';
csc = 'switchOffCircle';
ssb = 'switchOffBackground';
ssc = 'switchOffCircle';

def startVideo():
	subprocess.run((["motion", "-n"]) )

	
app = Flask(__name__)
@app.route("/")
def hello():
	templateData = {
    	'cameraSwitchBackground' : csb,
		'cameraSwitchCircle' : csc,
    	'soundSwitchBackground' : ssb,
    	'soundSwitchCircle': ssc
	}
	return render_template('index.html', **templateData)
   
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	global cameraOn, soundOn, csb, csc, ssb, ssc
	print(deviceName, action)
	
	if((deviceName=="camera") & (action=="toggle")):
		templateData = {}
		cameraOn = ~cameraOn
		if(cameraOn):
			csb = 'switchOnBackground'
			csc = 'switchOnCircle'
			print("before motion")
			t1 = threading.Thread(target=startVideo)
			t1.start()
			# subprocess.run((["motion", "-n"]) )
			print("before on")
			time.sleep(4)
			print("after on")
		else:
			subprocess.run((["pkill", "motion"]) )
			csb = 'switchOffBackground'
			csc = 'switchOffCircle'
	if((deviceName=="sound") & (action=="toggle")):
		# soundOn = ~soundOn
		# if(soundOn):
			ssb = 'switchOnBackground'
			ssc = 'switchOnCircle'
			for i in range(1000):
				GPIO.output(buzzer, GPIO.HIGH)
				time.sleep(0.001/2)
				GPIO.output(buzzer, GPIO.LOW)
				time.sleep(0.001/2)
			ssb = 'switchOffBackground'
			ssc = 'switchOffCircle'
		# else:
		# 	ssb = 'switchOffBackground'
		# 	ssc = 'switchOffCircle'
	templateData = {
				'cameraSwitchBackground' : csb,
				'cameraSwitchCircle' : csc,
		    	'soundSwitchBackground' : ssb,
		    	'soundSwitchCircle': ssc
			}
	return render_template('index.html', **templateData)
	
   
if __name__ == "__main__":
   app.run(debug=True, port=434, host='0.0.0.0')
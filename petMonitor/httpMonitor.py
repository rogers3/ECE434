#!/usr/bin/env python3

#//////////////////////////////////////
# Author: Christina Rogers
# CM: 473
# Date: 10/1/2020
# Description: 
#//////////////////////////////////////

#import necessary libraries
from flask import Flask, render_template, request, redirect
import Adafruit_BBIO.GPIO as GPIO
import threading 
import sound
import time
import os
import subprocess
import sys

cameraOn=False;
freqOn=False;
csb = 'switchOffBackground';
csc = 'switchOffCircle';
fsb = 'switchOffBackground';
fsc = 'switchOffCircle';
inputFreq = "1000";

def startVideo():
	subprocess.run((["motion", "-n"]) )

	
app = Flask(__name__)
@app.route("/")
def hello():
	templateData = {
    	'cameraSwitchBackground' : csb,
		'cameraSwitchCircle' : csc,
    	'freqSwitchBackground' : fsb,
    	'freqSwitchCircle': fsc,
    	'freqValue' : inputFreq
	}
	return render_template('index.html', **templateData)
   
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	global cameraOn, freqOn, csb, csc, fsb, fsc, inputFreq
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
			print("before on")
			time.sleep(4)
			print("after on")
		else:
			subprocess.run((["pkill", "motion"]) )
			csb = 'switchOffBackground'
			csc = 'switchOffCircle'
			
	if((deviceName=="sound") & (action=="freq")):
		freqOn = ~freqOn
		print(inputFreq, type(inputFreq))
		if(freqOn):
			# sound.playFrequency(int(inputFreq))
			fsb = 'switchOnBackground'
			fsc = 'switchOnCircle'
		else:
			sound.stopSpeaker()
			fsb = 'switchOffBackground'
			fsc = 'switchOffCircle'
			
	if((deviceName=="sound") & (action=="song")):
		sound.playSong()
		
	templateData = {
				'cameraSwitchBackground' : csb,
				'cameraSwitchCircle' : csc,
		    	'freqSwitchBackground' : fsb,
		    	'freqSwitchCircle': fsc,
		    	'freqValue' : inputFreq
		}
	return render_template('index.html', **templateData)
	
@app.route('/read', methods=['POST'])
def getData():
	global inputFreq
	if request.method == 'POST': 
		if(inputFreq == None):
			inputFreq = "10000"
		else:
			inputFreq = request.form['inputFreq']
		return redirect ('/sound/freq')
	else:
		return redirect ('/')
	
   
if __name__ == "__main__":
   app.run(debug=True, port=434, host='0.0.0.0')
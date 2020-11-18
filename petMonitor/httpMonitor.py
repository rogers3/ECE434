#!/usr/bin/env python3

#import necessary libraries
from flask import Flask, render_template, request, redirect
import Adafruit_BBIO.GPIO as GPIO
import threading 
import sound
import time
import subprocess
import smbus

cameraOn=False;
freqOn=False;
songOn=False;
csb = 'switchOffBackground';
csc = 'switchOffCircle';
fsb = 'switchOffBackground';
fsc = 'switchOffCircle';
inputFreq = "1000";
sb = "playButton"
temp = "0"
initialMealTime = time.time()
initialOutTime = time.time()

# Use i2c bus 1 adress 0x4a and 0x48
bus = smbus.SMBus(2)
adress = 0x4a

app = Flask(__name__)
@app.route("/")
def hello():
	global temp
	temp = bus.read_byte_data(adress, 0)*9/5+32
	initialMealOutput = getTimeSince(initialMealTime)
	initialOutOutput = getTimeSince(initialOutTime)
	templateData = {
    	'cameraSwitchBackground' : csb,
		'cameraSwitchCircle' : csc,
    	'freqSwitchBackground' : fsb,
    	'freqSwitchCircle': fsc,
    	'freqValue' : inputFreq,
    	'songButton': sb,
    	'temp' : temp,
    	'mealTime' : initialMealOutput,
    	'outTime' : initialOutOutput
	}
	return render_template('index.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	global cameraOn, freqOn, csb, csc, fsb, fsc, inputFreq, songOn, sb, initialMealTime, initialOutTime
	t2 = threading.Thread(target=startSound)

	if((deviceName=="camera") & (action=="toggle")):
		cameraOn = ~cameraOn
		if(cameraOn):
			csb = 'switchOnBackground'
			csc = 'switchOnCircle'
			t1 = threading.Thread(target=startVideo)
			t1.start()
			time.sleep(4)
		else:
			subprocess.run((["pkill", "motion"]) )
			csb = 'switchOffBackground'
			csc = 'switchOffCircle'
			
	if((deviceName=="sound") & (action=="freq")):
		freqOn = ~freqOn
		print(inputFreq, type(inputFreq))
		if(freqOn):
			sound.playFrequency(int(inputFreq))
			fsb = 'switchOnBackground'
			fsc = 'switchOnCircle'
		else:
			sound.stopSpeaker()
			fsb = 'switchOffBackground'
			fsc = 'switchOffCircle'
			
	if((deviceName=="sound") & (action=="song")):
		songOn = ~songOn
		if(songOn):
			sb = "pauseButton"
			t2.start()
		else:
			sb = "playButton"
			try:
				sound.stopSpeaker()
			except:
				print("speaker not playing")
				
	if((deviceName=="letOut") & (action=="press")):
		initialOutTime = time.time()
		
	if((deviceName=="feed") & (action=="press")):
		initialMealTime = time.time()
		
	return redirect ('/')
	
@app.route('/read', methods=['POST'])
def getData():
	print("reading")
	global inputFreq
	if request.method == 'POST': 
		if(inputFreq == None):
			inputFreq = "10000"
		else:
			inputFreq = request.form['inputFreq']
		return redirect ('/sound/freq')
	else:
		return redirect ('/')
		
def startVideo():
	subprocess.run((["motion", "-n"]) )
	
def startSound():
	global sb, songOn
	sound.playSong()
	sb = "playButton"
	songOn = False;

def getTimeSince(initialTime):
	if((time.time()-initialTime)>=3600):
		initialMealOutput = str(int(int(time.time()-initialTime))/3600)+" hr    "+str(int(int(time.time()-initialTime)/60))+" m    "+str(int(time.time()-initialTime)%60)+" s"
	elif((time.time()-initialTime)>=60):
		initialMealOutput = str(int(int(time.time()-initialTime)/60))+" m    "+str(int(time.time()-initialTime)%60)+" s"
	else:
		initialMealOutput = str(int(time.time()-initialTime)%60)+" s"
	return initialMealOutput
   
if __name__ == "__main__":
   app.run(debug=True, port=434, host='0.0.0.0')
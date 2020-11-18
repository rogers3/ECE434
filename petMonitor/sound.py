#!/usr/bin/python3

#!/usr/bin/env python3
import time
import sys
sys.path.insert(0, '/lib')
import PWMmay as PWM


speaker = "P9_14"
PWM

notes = {
    "A" : 440,
    "B" : 494,
    "C" : 262,
    "D" : 294,
    "E" : 330,
    "F" : 349,
    "G" : 392	
}

oldMcDonald = "CCCGAAG EEDDC GCCCGAAG EEDDC";


def playSong():
    err = PWM.start(speaker, 50, freq=262)
    if err == None:
        exit()
    
    for i in range(len(oldMcDonald)):
        if(oldMcDonald[i]!=" "):
            PWM.set_duty_cycle(speaker, 50)
            PWM.set_frequency(speaker, notes.get(oldMcDonald[i]))
        time.sleep(.2)
        PWM.set_duty_cycle(speaker, 0)
        time.sleep(.05)
        
    PWM.stop(speaker)
        
def playFrequency(f):
    err = PWM.start(speaker, 50, freq=f)
    if err == None:
        exit()
    
    
def stopSpeaker():
    PWM.stop(speaker)
    

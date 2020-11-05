Author: Christina Rogers (rogersc@rose-hulman.edu)

CM: 473

Date: 10/26/2020

What is included:

| Name      | Description |
| ----------- | ----------- |
| pictures | Folder containing pictures relevent to hw
| credentials.json | Credentials to log to google sheets
| demo.py | Script that logs temperatures of two TMP101 sesnors vs time once every second.
| setup.sh | This is the setup file for this folder
| temp.py" Script that logs temperatures of two TMP101 sesnors and time once every minute.
| token.pickle | Credentials for logging to google sheets


## Project: ##

Project Link: 


Project Time :


    ![alt text]()


## Logging in Sheets: ##


Sheet Link: https://docs.google.com/spreadsheets/d/1fn7VuquCIexN2MM47orb_cxh6AY2Y_qZV6-GXTi4naY/edit#gid=0


Running the demo.py script logs the data from two TMP101 sensors into a google sheet. The sheet
can be found by opening the link above. The sheet has three colums. The first is time which 
records date time (mm/d/yyyy hh:mm:ss). The other two coulumns are Temperatures 1 and 2 which 
records the temp in °F. Data is recorded once a second, but this can be changed by edditing the 
variable PERIOD in demo.py. The credential file for logging to google sheets is credentials.json. 


    ![alt text]()


Next a plot was made of the temperature over time. 


    ![alt text]()


I ran this program for a long period of time and got 1370 points of data. There was nothing
intresting that happened in the actual data. The google sheet did eventually fill and prompted me
to add more rows. I did add more rows and data continued to record.


## ThinkSpeak: ##


ThinkSpeak link: https://thingspeak.com/channels/1220275


Running the temp.py script logs the data from two TMP101 sensors into ThnkSpeak. I made the
ThnkSpeak channel public so it can be opened from the link above. The channel has two
plots. They plot temperature in °C vs time for each of the two TMP101 sensors.


    ![alt text]()
    
    
I ran this program for around ___ ...
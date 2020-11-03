#!/usr/bin/env node

var Blynk = require('blynk-library');
const b = require('bonescript');
var AUTH = 'ONG0sBpHCDsOrdpqSo0fIga1koAqmZG9';
var blynk = new Blynk.Blynk(AUTH);
var v0 = new blynk.VirtualPin(0);
var v9 = new blynk.VirtualPin(9);


var exec = require('child_process').exec;

v0.on('write', function(param) {
	console.log("v0 ", param);
});

v9.on('write', function(param) {
    console.log("button press: ", param[0]);

     if(param[0] == 1){
        console.log("start motion");
        exec('motion -c motion.conf');
    }
    if(param[0] == 0){
        console.log("start motion");
        exec('pkill motion');
    }
	//pkill motion
});

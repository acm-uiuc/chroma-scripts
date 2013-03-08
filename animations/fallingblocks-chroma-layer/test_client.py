import sys
from simpleOSC import initOSCClient, sendOSCMsg

ip = "127.0.0.1"
port = 9123

NUMBER_OF_LIGHTS = 24 # currently 24, EOH 48
DEFAULT_COLOR = [(25.0, 25.0, 25.0)] # dim white light
canvas = DEFAULT_COLOR * NUMBER_OF_LIGHTS

def rainbow():
	WAIT = 0.05
	import time
	initOSCClient(ip, port)
	i = 0
	while (1):
		for j in range(0,360):
			for i in range(0,48):
				sendOSCMsg("/asteroid", [i,0,0,0,0,j,1,0])
		time.sleep(WAIT)
	
def dim():
	WAIT = 0.05
	initOSCClient(ip, port)
	
	for i in range(0,48):
		sendOSCMsg("/asteroid", [i,0,0,0,0,240,1,0])
	sendOSCMsg("/asteroid", [56,0,0,0,0,219,1,0])
	sendOSCMsg("/asteroid", [49,0,0,0,0,261,1,0])
	sendOSCMsg("/asteroid", [102,0,0,0,0,219,1,0])
	sendOSCMsg("/asteroid", [507,0,0,0,0,261,1,0])
	sendOSCMsg("/asteroid", [800,0,0,0,0,219,1,0])
	sendOSCMsg("/asteroid", [900,0,0,0,0,261,1,0])
	
def max_color():
	initOSCClient(ip, port)
	import time
	for i in range(0,48):
		sendOSCMsg("/asteroid", [i,0,0,0,0,240,1,0])
	
	time.sleep(5)
	
	sendOSCMsg("/set_max_brightness", [256.0])
	
# max_color()
# dim()
rainbow()

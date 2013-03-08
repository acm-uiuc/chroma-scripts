import sys
from simpleOSC import initOSCClient, sendOSCMsg

ip = "127.0.0.1"
port = 9199

NUMBER_OF_LIGHTS = 24 # currently 24, EOH 48
DEFAULT_COLOR = [(25.0, 25.0, 25.0)] # dim white light
canvas = DEFAULT_COLOR * NUMBER_OF_LIGHTS

def test():
	WAIT = 0.25
	import time
	initOSCClient(ip, port)
	for i in range(0,50):
		sendOSCMsg("/entry", [i,0,0] + [(1024,200,900)])
		time.sleep(WAIT)
	for i in range(0,50):
		sendOSCMsg("/exit", [i,0,0] + [(0,0,0)])
		time.sleep(WAIT)

test()

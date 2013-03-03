import sys
from animations import FadeAnimation
from simpleOSC import initOSCServer, startOSCServer, closeOSC, setOSCHandler
import OSC
from random import random

DEBUG = 1

ip = "127.0.0.1" # receiving osc from 
port = 9125
NUMBER_OF_LIGHTS = 24 # currently 24, EOH 48
DEFAULT_COLOR = [(25.0, 25.0, 25.0)] # dim white light
canvas = DEFAULT_COLOR * NUMBER_OF_LIGHTS
orbs = [[]] * NUMBER_OF_LIGHTS # data on the orbs on the screen
out = FadeAnimation()

def run():
	# SETUP #
	resetCanvas()
	import time
	out.FADERATE = 8.0 # 8 second fading
	out.start()  # start visualization
	initOSCServer(ip, port) # start OSC server
	
	# OSC HANDLERS #
	setOSCHandler('/entry', entry)
	setOSCHandler('/exit', exit)

	# SERVER START #
	startOSCServer()
	print "server is running, listening at " + str(ip) + ":" + str(port)

	try:
		clock = 0
		while(1):
			out.write(canvas) #write to canvas
			time.sleep(0.1)
			if ((clock%100 == 0)): # every 100 ticks
				plasmaCanvas()
			clock = (clock+1)%10000 # reset clock every 10000 ticks
	except KeyboardInterrupt:
		print "closing all OSC connections... and exit"
		closeOSC() # finally close the connection before exiting or program.	
	
def entry(addr, tags, data, source):
	if (DEBUG):
		print "entry handler called"
		print "addr = " + str(addr) # /entry
		print "tags = " + str(tags) # is
		print "data = " + str(data) # [orbID, entryX, entryY, (R, G, B)]
		print "sour = " + str(source) # (network info)
	idx = data[0] % NUMBER_OF_LIGHTS
	orbs[idx] = data # store orb data
	canvas[idx] = data[3] # change pixel color to orb color
	
def exit(addr, tags, data, source):
	if (DEBUG):
		print "exit handler called"
		print "addr = " + str(addr) # /exit
		print "tags = " + str(tags) # is
		print "data = " + str(data) # [orbID, entryX, entryY, (R, G, B)]]
		print "sour = " + str(source) # (network info)
	idx = data[0] % NUMBER_OF_LIGHTS
	if (orbs[idx][0] == data[0]): # if the exiting orb is in orbs
		orbs[idx] = [] # remove the data from the list
	
def resetCanvas():
	r = random() * 100
	g = random() * 100
	b = random() * 100
	for i in NUMBER_OF_LIGHTS:
		canvas[i] = (r,g,b)
		
def plasmaCanvas():
	for i in NUMBER_OF_LIGHTS:
		canvas[i] = canvas[i] * (random() * 2 + 0.1)

if __name__ == "__main__":
	run()

	# import time
    # out = FadeAnimation()
    # out.FADERATE = 8.0
    # out.start()

    # while True:
        # for i in range(24):
            # pix = [(0.0,0.0,0.0)]*24
            # if i%8 == 0:
                # pix[i] = (1023.0,0.0,0.0)
            # else:
                # pix[i] = (0.0,1023.0,1023.0)
            # out.write(pix)
            # time.sleep(0.7)
            # time.sleep(0.2)

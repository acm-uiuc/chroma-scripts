import sys
from animations import FadeAnimation
from simpleOSC import initOSCServer, startOSCServer, closeOSC, setOSCHandler
import OSC
import oscapi
from random import random, randint

DEBUG = 1

ip = "127.0.0.1" # receiving osc from 
port = 9199
MAX_COLOR = 1024
NUMBER_OF_LIGHTS = 48 # working for 24, EOH 48
default_color = [(102.4, 102.4, 102.4)] # dim white light
canvas = default_color * NUMBER_OF_LIGHTS
default_orb = [-1,-1,-1,-1,-1,-1,-1]
orbs = [default_orb] * NUMBER_OF_LIGHTS # [orbID, entryX, entryY, R, G, B, canvasidx]
out = FadeAnimation()

def run():
	# SETUP #
	resetCanvas()
	import time
	out.FADERATE = 8 #fade rate, currently broken?
	out.start()
	initOSCServer(ip, port) # start OSC server
	
	# OSC HANDLERS #
	setOSCHandler('/entry', entry)	# when a new orb enters the screen
	setOSCHandler('/exit', exit)	# when an orb exits the screen
	setOSCHandler('/reset', reset)	# resets the visualization
	setOSCHandler('/move', move)	# when an orb moves on the screen

	# SERVER START #
	startOSCServer()
	print "server is running, listening at " + str(ip) + ":" + str(port)

	try:
		clock = 1
		while(1):
			out.write(canvas) #write to canvas
			time.sleep(0.1)
			if ((clock%1000) == 0):
				plasmaCanvas()
			clock = (clock+1)%10000 # reset clock every 10000 ticks
	except KeyboardInterrupt:
		print "closing all OSC connections... and exit"
		closeOSC() # finally close the connection before exiting or program.	
	
def entry(addr, tags, data, source):
	if (DEBUG):
		print "entry handler called"
		print "addr = " + str(addr) # /entry
		# print "tags = " + str(tags) # is
		print "data = " + str(data) # [orbID, entryX, entryY, R, G, B]
		# print "sour = " + str(source) # (network info)
	idx = data[0] + randint(0,NUMBER_OF_LIGHTS)
	idx = idx % NUMBER_OF_LIGHTS
	orbs[idx] = data + [idx] # store orb data
	pix = (data[3],data[4],data[5])
	canvas[idx] = pix # change pixel color to orb color
	
def exit(addr, tags, data, source):
	if (DEBUG):
		print "exit handler called"
		print "addr = " + str(addr) # /exit
		# print "tags = " + str(tags) # is
		print "data = " + str(data) # [orbID, exitX, exitY, R, G, B]
		# print "sour = " + str(source) # (network info)
		# print "orbs = " + str(orbs)
	for i in range(0, NUMBER_OF_LIGHTS): # for all orb data
		if (orbs[i][0] == data[0]): # if the orb is currently in the array
			if (DEBUG):
				print "found orb for removal: " + str(orbs[i])
			canvas[orbs[i][6]] = default_color[0]	# reset the color of its light
			orbs[i] = [-1,-1,-1,-1,-1,-1,-1] # reset the orb
			
def move(addr, tags, data, source):
	if (DEBUG):
		print "move handler called"
		print "addr = " + str(addr) # /move
		# print "tags = " + str(tags) # is
		print "data = " + str(data) # [orbID, exitX, exitY, R, G, B]
		# print "sour = " + str(source) # (network info)
		# print "orbs = " + str(orbs)
	for i in range(0, NUMBER_OF_LIGHTS): # for all orb data
		if (orbs[i][0] == data[0]): # if the orb is currently in the array
			if (DEBUG):
				print "found orb for change: " + str(orbs[i])
			canvas[orbs[i][6]] = (data[3], data[4], data[5]) # reset the pixel
			orbs[i] = data + [orbs[i][6]] # reset the orb
			if (DEBUG):
				print "new orb: " + str(orbs[i])
			
def reset(addr, tags, data, source):
	resetCanvas()
	
def resetCanvas():
	for i in range(0, NUMBER_OF_LIGHTS):
		orbs[i] = default_orb
	r = random() * MAX_COLOR / 3 + MAX_COLOR / 10.0
	g = random() * MAX_COLOR / 3 + MAX_COLOR / 10.0
	b = random() * MAX_COLOR / 3 + MAX_COLOR / 10.0
	default_color[0] = (r,g,b)
	for i in range(0, NUMBER_OF_LIGHTS):
		canvas[i] = (r,g,b)
	plasmaCanvas()
		
def plasmaCanvas():
	for i in range(0, NUMBER_OF_LIGHTS):
		r = ((random()*0.1) + 0.95)
		#if (DEBUG): print r
		canvas[i] = oscapi.mult(canvas[i], r)
	default_color[0] = oscapi.mult(default_color[0], ((random()*0.5) + 0.75))

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

#################
#	IMPORTS		#
#################
import sys
from animations import FadeAnimation
from simpleOSC import initOSCServer, startOSCServer, closeOSC, setOSCHandler
import OSC
import oscapi
from random import random, randint, shuffle
import colorsys

#################
#	VARIABLES	#
#################
DEBUG = 1 # 0/1, gives more program feedback
ip = "127.0.0.1" # receiving osc from 
port = 9199
MAX_COLOR = 1024 # max intensity of any color value
NUMBER_OF_LIGHTS = 48
default_color = [(102.4, 102.4, 102.4)] # dim white light
canvas = default_color * NUMBER_OF_LIGHTS # this gets sent to chroma
default_orb = [-1,-1,-1, -1] # [orbID, distance, hue, canvasID]
orbs = [default_orb] * NUMBER_OF_LIGHTS # this stores orb data
map_IDs = [-1] * NUMBER_OF_LIGHTS # maps from orbID to canvasID
out = FadeAnimation() 

#################
#	MAIN		#
#################
def run():
	# SETUP #
	resetCanvas()
	import time
	out.FADERATE = 8 # fade rate, currently broken?
	out.start()
	
	# OSC SERVER/HANDLERS #
	initOSCServer(ip, port) # setup OSC server
	setOSCHandler('/reset', reset)	# resets the visualization
	setOSCHandler('/orb', orb)	# when an orb moves on the screen

	# SERVER START #
	startOSCServer()
	print "server is running, listening at " + str(ip) + ":" + str(port)

	# SERVER LOOP#
	try:
		clock = 1
		while(1):
			out.write(canvas) # write to canvas
			time.sleep(0.1) # tick every 0.1 seconds
			if ((clock%100) == 0): # every 1000 ticks
				plasmaCanvas()
			clock = (clock+1)%10000 # increment clock, reseting every 10000 ticks
	except KeyboardInterrupt:
		print "closing all OSC connections... and exit"
		closeOSC() # close the osc connection before exiting	


#####################
#	OSC HANDLERS	#
#####################
def orb(addr, tags, data, source):
	if (DEBUG):
		print "orb handler called"
		print "addr = " + str(addr) # /move
		# print "tags = " + str(tags) # is
		print "data = " + str(data) # [orbID, x, y, curvature, force, hue, distance, age]
		# print "sour = " + str(source) # (network info)
		# print "orbs = " + str(orbs)
	index		= data[0] % NUMBER_OF_LIGHTS
	orbs[index]	= [data[0],data[6],data[5],map_IDs[index]] # [orbID, distance, hue, canvasID]
	raw_color	= colorsys.hsv_to_rgb(data[5] / 360.0, 1, 1) #(h, s, v)
	color		= oscapi.mult(raw_color, (MAX_COLOR / 2.0) + (MAX_COLOR / 2.0 * data[6])) # go from [0, 1) to [0, MAX_COLOR)
	canvas[map_IDs[index]] = color
		
def reset(addr, tags, data, source):
	resetCanvas()


#############################
#	CANVAS MANIPULATION		#
#############################
def resetCanvas():
	for i in range(0, NUMBER_OF_LIGHTS):
		orbs[i] = default_orb
	r = random() * MAX_COLOR / 3 + MAX_COLOR / 10.0
	g = random() * MAX_COLOR / 3 + MAX_COLOR / 10.0
	b = random() * MAX_COLOR / 3 + MAX_COLOR / 10.0
	default_color[0] = (r,g,b)
	for i in range(0, NUMBER_OF_LIGHTS):
		canvas[i] = (r,g,b)
		map_IDs[i] = i
	shuffle(map_IDs)
	if (DEBUG): print "shuffle: " + str(map_IDs)
	plasmaCanvas()
		
def plasmaCanvas():
	for i in range(0, NUMBER_OF_LIGHTS):
		r = ((random()*0.1) + 0.95)
		#if (DEBUG): print r
		canvas[i] = oscapi.mult(canvas[i], r)
	shuffle(map_IDs)
	

#################
#	???			#
#################
if __name__ == "__main__":
	run()

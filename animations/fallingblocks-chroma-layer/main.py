#################
#	IMPORTS		#
#################
import sys
from animations import FadeAnimation
#from oscapi import ColorsOut as FadeAnimation 
from simpleOSC import initOSCServer, startOSCServer, closeOSC, setOSCHandler
import OSC
import oscapi
from random import random, randint, shuffle
import colorsys

#################
#	VARIABLES	#
#################
DEBUG = 0 # 0/1, gives more program feedback
ip = "127.0.0.1" # receiving osc from 
port = 9125
MAX_BRIGHTNESS = [1024.0] # max intensity of any color value
MIN_BRIGHTNESS = [102.4]  # min intensity of any color value
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
	setOSCHandler('/asteroid', orb)	# when an orb moves on the screen
	setOSCHandler('/set_max_brightness', setMax)
	setOSCHandler('/set_min_brightness', setMin)

	# SERVER START #
	startOSCServer()
	print "server is running, listening at " + str(ip) + ":" + str(port)

	# SERVER LOOP#
	try:
		clock = 1
		while(1):
			out.write(canvas) # write to canvas
			time.sleep(0.1) # tick every 0.1 seconds
			if ((clock%1000) == 0): # every 1000 ticks
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
	mul			= 0
	if (data[5] > 220 and data[5] < 260): # color is blue
		mul		= (MIN_BRIGHTNESS[0])
	else: # color is not blue
		mul		= (MIN_BRIGHTNESS[0]) + ((MAX_BRIGHTNESS[0] - MIN_BRIGHTNESS[0]) * data[6]) # go from [0, 1) to [0, MAX_BRIGHTNESS)
	color = oscapi.mult(raw_color, mul)
	canvas[map_IDs[index]] = color
		
def reset(addr, tags, data, source):
	resetCanvas()
	
def setMax(addr, tags, data, source):
	if (DEBUG):
		print "orb handler called"
		print "addr = " + str(addr) # /move
		# print "tags = " + str(tags) # is
		print "data = " + str(data) # [MAX_BRIGHTNESS[0]]
		# print "sour = " + str(source) # (network info)
		# print "orbs = " + str(orbs)
	# OLD_MAX_BRIGHTNESS = MAX_BRIGHTNESS[0]
	MAX_BRIGHTNESS[0] = data[0]
	#for i in range(0, NUMBER_OF_LIGHTS):
		# if (DEBUG): print "NEW/OLD = " + str(MAX_BRIGHTNESS[0] / OLD_MAX_BRIGHTNESS)
	#	canvas[i] = oscapi.mult(canvas[i], MAX_BRIGHTNESS[0] / OLD_MAX_BRIGHTNESS)
	
def setMin(addr, tags, data, source):
	if (DEBUG):
		print "orb handler called"
		print "addr = " + str(addr) # /move
		# print "tags = " + str(tags) # is
		print "data = " + str(data) # [MAX_BRIGHTNESS[0]]
		# print "sour = " + str(source) # (network info)
		# print "orbs = " + str(orbs)
	MIN_BRIGHTNESS[0] = data[0]

#############################
#	CANVAS MANIPULATION		#
#############################
def resetCanvas():
	for i in range(0, NUMBER_OF_LIGHTS):
		orbs[i] = default_orb
	for i in range(0, NUMBER_OF_LIGHTS):
		canvas[i] = default_color[0]
		map_IDs[i] = i
	plasmaCanvas()
	MAX_BRIGHTNESS[0] = 1024.0
	MIN_BRIGHTNESS[0] = 102.4
		
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
